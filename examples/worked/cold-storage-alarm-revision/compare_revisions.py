"""Reproduce prior success, a real failed change, the repair, and stale-evidence rejection."""
from datetime import datetime, timezone
from pathlib import Path
import argparse
import copy
import hashlib
import json
import platform
import subprocess
import sys
import uuid

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "scripts/check_trace.py").is_file())
sys.path.insert(0, str(ROOT / "scripts"))
import check_trace
import evidence_io
from check_trace import check, validate_execution
from evidence_io import bind_loaded_sources, save

_LOADED_COMPARISON_SOURCES = bind_loaded_sources(HERE, {
    "compare_revisions.py": sys._getframe().f_code,
    "evidence_io.py": evidence_io._LOADED_MODULE_CODE,
})
_LOADED_COMPARISON_SOURCES["repository:scripts/check_trace.py"] = bind_loaded_sources(
    ROOT, {"scripts/check_trace.py": check_trace._LOADED_MODULE_CODE})["scripts/check_trace.py"]


def evaluate():
    observations = []
    for name, folder, expected_failures in (("prior", HERE / "prior", 0), ("changed_requirement_old_model", HERE / "failed", 4), ("repaired", HERE, 0)):
        baseline = json.loads((folder / "baseline.json").read_text())
        errors, summary = check(baseline, folder)
        process = subprocess.run([sys.executable, "-B", str(folder / "run_checks.py"), "--check"], cwd=folder, text=True, capture_output=True, check=False)
        expected_exit = 1 if expected_failures else 0
        if errors or process.returncode != expected_exit or summary.get("failed_procedures") != expected_failures:
            raise ValueError(f"{name}: reproduction failed: {errors}; {process.stdout}; {process.stderr}")
        if expected_failures and process.stderr.strip() != "Failed: VER-03, VER-06, VER-07, VER-08":
            raise ValueError(f"{name}: exit 1 was not the preserved expected failure: {process.stderr}")
        saved = json.loads((folder / "evidence/results.json").read_text())
        by_id = {r["verification"]: r for r in saved["results"]}
        observations.append({"phase": name, "integrity": summary["integrity"],
                             "executed_procedures": summary["executed_procedures"],
                             "passed_procedures": summary["passed_procedures"],
                             "failed_procedures": summary["failed_procedures"],
                             "requirements_with_passing_model_evidence": summary["requirements_with_passing_model_evidence"],
                             "first_sensor_fault_ms": by_id["VER-03"]["observed"]["first_sensor_fault_ms"],
                             "state_exploration": by_id["VER-07"]["observed"]})
    current = json.loads((HERE / "baseline.json").read_text())
    old = json.loads((HERE / "prior/baseline.json").read_text())
    for group in ("requirements", "functions", "components", "actors", "interfaces", "verification"):
        if {r["id"] for r in current[group]} != {r["id"] for r in old[group]}:
            raise ValueError(f"Changed stable IDs in {group}")
    attempted = copy.deepcopy(current)
    attempted["evidence"][0]["artifact"] = "prior/evidence/results.json"
    errors, summary = check(attempted, HERE)
    if not any("stale or invalid configuration" in e for e in errors) or summary["requirements_with_passing_model_evidence"] != 0 or summary["executed_procedures"] != 0:
        raise ValueError("Old evidence was not excluded from the changed baseline")
    observations.append({"phase": "reuse_prior_evidence_for_changed_baseline", "integrity": summary["integrity"],
                         "rejected_execution_records": summary["rejected_execution_records"],
                         "requirements_with_passing_model_evidence": summary["requirements_with_passing_model_evidence"],
                         "executed_procedures": summary["executed_procedures"],
                         "reasons": errors, "stable_ids_preserved": True})
    return observations


def configuration():
    paths = {"compare_revisions.py": HERE / "compare_revisions.py", "repository:scripts/check_trace.py": ROOT / "scripts/check_trace.py"}
    for prefix, folder in (("prior/", HERE / "prior"), ("failed/", HERE / "failed"), ("", HERE)):
        baseline = json.loads((folder / "baseline.json").read_text())
        for name in [*baseline["configuration_files"], "evidence/results.json"]:
            paths[prefix + name] = folder / name
    hashes = {name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in sorted(paths.items())}
    changed = [name for name, digest in _LOADED_COMPARISON_SOURCES.items() if hashes.get(name) != digest]
    if changed:
        raise ValueError("Comparison source changed after import: " + ", ".join(changed))
    return hashes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--record", action="store_true", help="Archive a new workflow receipt and preserve the previous selection")
    group.add_argument("--check", action="store_true", help="Reproduce the selected workflow receipt without writing")
    parser.add_argument("--output", type=Path, help="New receipt path; explicit output never overwrites")
    args = parser.parse_args()
    start = datetime.now(timezone.utc)
    try:
        before = configuration()
        results = evaluate()
        if configuration() != before:
            raise ValueError("Revision inputs changed during comparison")
        record = {"schema_version": 1, "scope": "instructional-revision-workflow",
                  "execution": {"run_id": start.strftime("%Y%m%dT%H%M%S.%fZ-") + uuid.uuid4().hex[:12],
                                "started_at": start.isoformat(), "finished_at": datetime.now(timezone.utc).isoformat(),
                                "command": [sys.executable, __file__, *sys.argv[1:]],
                                "python_version": platform.python_version(), "platform": platform.platform(),
                                "loaded_sources": _LOADED_COMPARISON_SOURCES},
                  "configuration": before, "observations": results,
                  "acceptance": "not_assessed", "physical_validation": "not_performed"}
        if args.record:
            save(HERE, record, args.output, selection="revision-check.json")
            print(f"Recorded workflow receipt: {args.output or HERE / 'evidence/revision-check.json'}")
        if args.check:
            saved = json.loads((args.output or HERE / "evidence/revision-check.json").read_text())
            problems = validate_execution(saved.get("execution"))
            if problems:
                raise ValueError("Invalid workflow execution provenance: " + ", ".join(problems))
            if saved["execution"].get("loaded_sources") != _LOADED_COMPARISON_SOURCES:
                raise ValueError("Workflow receipt has missing or stale loaded-source bindings")
            if any(saved.get(key) != record[key] for key in ("schema_version", "scope", "configuration", "observations", "acceptance", "physical_validation")):
                raise ValueError("Stored revision-workflow receipt is stale or differs from execution")
        print("Prior pass, changed-requirement failure, repaired pass, and stale-evidence rejection reproduced; stable IDs preserved")
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, str(error) + "\n")


if __name__ == "__main__":
    main()
