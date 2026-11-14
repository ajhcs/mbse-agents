"""Check current gallery identities, allocated references and evidence records.

Historical JSON snapshots are verified for byte integrity and excluded from
current claims. This checker does not validate standards or physical behavior.
"""
from pathlib import Path, PurePosixPath, PureWindowsPath
import argparse
import datetime
import hashlib
import json
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

from analyze_gallery import DOMAINS, ROOT, cse_record, digest, load_json, parse_json, render_report, run

ID = re.compile(r"\b(?:REQ|CMP|FUN|IFC|HZ|CTL|VER|EVD)-[A-Z0-9]+(?:-[A-Z0-9]+)*\b")


def execution_metadata(receipt):
    """Require execution provenance; presence is not external authentication."""
    if not isinstance(receipt, dict) or receipt.get("schema_version") != 1:
        raise ValueError("Missing or unsupported execution provenance schema")
    timestamp = receipt.get("executed_at")
    try:
        when = datetime.datetime.fromisoformat(timestamp)
    except (TypeError, ValueError) as error:
        raise ValueError("Missing or invalid execution provenance timestamp") from error
    if when.utcoffset() != datetime.timedelta(0):
        raise ValueError("Execution provenance timestamp must include UTC offset")
    if not isinstance(receipt.get("python"), str) or not re.fullmatch(r"\d+\.\d+\.\d+", receipt["python"]):
        raise ValueError("Missing or invalid execution provenance Python version")
    command = receipt.get("command")
    if not isinstance(command, list) or not command or any(not isinstance(part, str) or not part.strip() for part in command):
        raise ValueError("Missing or invalid execution provenance command")


def validate_execution(receipt, report, result_sha256, entrypoint):
    execution_metadata(receipt)
    if receipt.get("run_id") != report["run_id"] or receipt.get("scope") != report["scope"]:
        raise ValueError("Execution provenance run identity or scope differs")
    origin = receipt.get("entrypoint")
    # A saved execution identity belongs to its producer's host, not this host.
    if not isinstance(origin, str) or not any(
            path.is_absolute() and path.name == entrypoint
            for path in (PurePosixPath(origin), PureWindowsPath(origin))):
        raise ValueError("Execution provenance entrypoint is missing or invalid")
    if receipt.get("loaded_sources") != report["loaded_sources"]:
        raise ValueError("Execution provenance loaded-source bindings differ")
    if receipt.get("result_sha256") != result_sha256:
        raise ValueError("Execution provenance result hash differs")


def validate_crosscheck_provenance(receipt):
    execution_metadata(receipt)
    if receipt.get("scope") != "independent_implementation_crosscheck_not_independent_engineering_review":
        raise ValueError("CSE provenance scope is missing or invalid")
    helper = receipt.get("helper_entrypoint")
    # These CSE receipts declare a POSIX execution command and source inventory.
    if not isinstance(helper, str) or not PurePosixPath(helper).is_absolute() or len(PurePosixPath(helper).parents) < 4:
        raise ValueError("CSE helper provenance entrypoint is missing or invalid")
    helper = PurePosixPath(helper)
    runtime = helper.parents[3]
    required = {str(helper), *(str(runtime / name) for name in (
        "scripts/failure_analysis.py", "verifier/failure_analysis.py", "verifier/core.py", "verifier/foundation.py"))}
    hashes = receipt.get("helper_sources")
    if receipt.get("helper_source_hash_scope") != "observed_before_and_after_execution_not_loaded_module_binding":
        raise ValueError("CSE source inventory scope must distinguish it from a loaded-code binding")
    if not isinstance(hashes, dict) or set(hashes) != required or any(
            not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value) for value in hashes.values()):
        raise ValueError("CSE helper provenance must contain all five declared source hashes")
    command = receipt["command"]
    if (receipt.get("bytecode_cache_policy") != "fresh_empty_prefix_with_writes_disabled"
            or len(command) != 10 or command[1:3] != ["-B", "-X"]
            or not command[3].startswith("pycache_prefix=/") or command[4] != str(helper)
            or PurePosixPath(command[5]).name != "cse-failure-model.json"
            or command[6:] != ["--required", "fault_tree", "--required", "probability"]):
        raise ValueError("CSE provenance command or cache policy differs from the declared execution")
    if receipt["cse_result"].get("input_sha256") != receipt.get("input_sha256"):
        raise ValueError("CSE reported input hash differs from execution provenance")


def references(text):
    result = []
    for name in ID.findall(text):
        span = re.fullmatch(r"(EVD)-(\d{3})-(\d{3})", name)
        if span:
            prefix, first, last = span.groups()
            if not 0 <= int(last) - int(first) <= 999:
                raise ValueError("Invalid evidence-ID range")
            result.extend(f"{prefix}-{index:03d}" for index in range(int(first), int(last) + 1))
        else:
            result.append(name)
    return result


def tables(text):
    result, current = [], []
    for line in text.splitlines() + [""]:
        if line.startswith("|"):
            current.append([cell.strip() for cell in line.strip().strip("|").split("|")])
        elif current:
            if len(current) > 2:
                result.append(current)
            current = []
    return result


def primary_table(text, prefix):
    for table in tables(text):
        if table[0][0].replace(" ", "").lower().startswith(prefix.lower()):
            return [row for row in table[2:] if row[0].startswith(prefix + "-")]
    return []


def inventory(folder):
    requirements = (folder / "requirements.md").read_text(encoding="utf-8")
    architecture = (folder / "architecture.md").read_text(encoding="utf-8")
    rows = {"REQ": re.findall(r"^### (REQ-[A-Z0-9-]+)\s*$", requirements, re.M)}
    for group in ("CMP", "FUN", "IFC"):
        rows[group] = [row[0] for row in primary_table(architecture, group)]
        if group == "IFC":
            # External and internal interfaces are separate declaration tables.
            rows[group] = [row[0] for table in tables(architecture)
                           if table[0][0].replace(" ", "").lower().startswith("ifc")
                           for row in table[2:] if row[0].startswith("IFC-")]
    hazard = folder / "hazard-analysis.md"
    if hazard.exists():
        content = hazard.read_text(encoding="utf-8")
        for group in ("HZ", "CTL"):
            rows[group] = [row[0] for row in primary_table(content, group)]
    else:
        rows.update(HZ=[], CTL=[])
    trace = folder / "traceability.md"
    rows["VER"] = [row[0] for row in primary_table(trace.read_text(encoding="utf-8"), "VER")] if trace.exists() else []
    if trace.exists():
        rows["VER"] += [row[0] for table in tables(trace.read_text(encoding="utf-8"))
                        if table[0][0] == "Activity" for row in table[2:] if row[0].startswith("VER-")]
    assurance = folder / "assurance-evidence.md"
    evidence = primary_table(assurance.read_text(encoding="utf-8"), "EVD") if assurance.exists() else []
    rows["EVD"] = [row[0] for row in evidence]
    return rows, evidence


def check(root=ROOT):
    root = Path(root)
    errors, summaries = [], []
    for domain in DOMAINS:
        for metadata in sorted((root / "examples" / domain).glob("*/system.yaml")):
            folder = metadata.parent
            key = folder.relative_to(root).as_posix()
            try:
                for name in ("README.md", "requirements.md", "architecture.md", "review-status.json", "source-review.md"):
                    if not (folder / name).is_file():
                        errors.append(f"{key}: missing {name}")
                identities, evidence = inventory(folder)
                for group, names in identities.items():
                    if len(names) != len(set(names)):
                        errors.append(f"{key}: duplicate {group} declaration")
                known = {name for group in identities.values() for name in group}
                review = load_json(folder / "review-status.json")
                accepted_open = {row["id"] for row in review["open_references"] if row.get("disposition")}
                unresolved = set()
                # Allocation and parent fields are actual record contracts.
                req_text = (folder / "requirements.md").read_text(encoding="utf-8")
                for line in req_text.splitlines():
                    if any(field in line for field in ("**Allocation**", "**Parent**", "**Source**")):
                        unresolved.update(name for name in references(line) if name not in known)
                for name in ("architecture.md", "hazard-analysis.md", "traceability.md", "assurance-evidence.md"):
                    path = folder / name
                    if path.exists():
                        for table in tables(path.read_text(encoding="utf-8")):
                            unresolved.update(ref for row in table[2:] for ref in references(" ".join(row)) if ref not in known)
                for name in sorted(unresolved - accepted_open):
                    errors.append(f"{key}: unresolved declared record link {name}")
                if accepted_open - unresolved:
                    errors.append(f"{key}: stale open-reference dispositions")
                source_rows = review["source_reviews"]
                if {row["requirement"] for row in source_rows} != set(identities["REQ"]):
                    errors.append(f"{key}: source review does not cover current requirement IDs")
                if len(source_rows) != len({row["requirement"] for row in source_rows}):
                    errors.append(f"{key}: duplicate source-review requirement")
                for row in source_rows:
                    if row.get("status") not in {"candidate_basis_requires_applicability_review", "primary_source_checked"}:
                        errors.append(f"{key}: invalid source-review status")
                counts = {"planned": 0, "drafted": 0, "executed": 0}
                for row in evidence:
                    state = row[-1].lower()
                    if state not in counts:
                        errors.append(f"{key}: unsupported evidence index status {row[0]}: {state}")
                        continue
                    counts[state] += 1
                    location = row[2].strip("`")
                    target = (folder / location.split("#")[0]).resolve()
                    if not target.is_relative_to(folder.resolve()):
                        errors.append(f"{key}: escaping evidence path {location}")
                    if state in {"drafted", "executed"} and not target.is_file():
                        errors.append(f"{key}: {row[0]} {state} artifact absent: {location}")
                if evidence:
                    # Repeated mapping tables must agree with the authoritative index.
                    states = {row[0]: row[-1].lower() for row in evidence}
                    for table in tables((folder / "assurance-evidence.md").read_text(encoding="utf-8")):
                        if table[0][-1].lower() != "status":
                            continue
                        for row in table[2:]:
                            repeated = [name for name in references(" ".join(row[:-1])) if name.startswith("EVD-")]
                            if repeated and row[-1].lower() in counts and any(states.get(name) != row[-1].lower() for name in repeated):
                                errors.append(f"{key}: conflicting repeated evidence status for {repeated}")
                for path in [*folder.glob("*.md"), *folder.glob("analysis/*.md"), *folder.glob("evidence/drafts/*.md")]:
                    for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", path.read_text(encoding="utf-8")):
                        parts = urlsplit(target)
                        if parts.scheme or parts.netloc or not parts.path:
                            continue
                        if not (path.parent / unquote(parts.path)).exists():
                            errors.append(f"{key}: broken local Markdown path in {path.name}: {target}")
                snapshot = load_json(folder / "history/pre-hardening.json")
                if snapshot.get("status") != "superseded_instructional_baseline_not_current_evidence":
                    errors.append(f"{key}: historical boundary missing")
                for name, record in snapshot["files"].items():
                    if hashlib.sha256(record["text"].encode()).hexdigest() != record["sha256"]:
                        errors.append(f"{key}: historical snapshot bytes changed: {name}")
                model_path = folder / "analysis/failure-model.json"
                assignments = 0
                if model_path.exists():
                    expected = run(model_path)
                    saved = load_json(folder / "evidence/analysis/model-results.json")
                    if expected != saved or saved["result"] != "pass":
                        errors.append(f"{key}: model results stale or expected observation failed")
                    if model_path.with_name("report.md").read_text(encoding="utf-8") != render_report(load_json(model_path), expected):
                        errors.append(f"{key}: generated interpretation view is stale")
                    assignments = expected["completed_assignments"]
                    cross_path = folder / "evidence/analysis/cse-crosscheck.json"
                    cross_bytes = cross_path.read_bytes()
                    cross = parse_json(cross_bytes)
                    cross_archive = cross_path.parent / "cse-runs" / (hashlib.sha256(cross_bytes).hexdigest() + ".json")
                    if not cross_archive.is_file() or cross_archive.read_bytes() != cross_bytes:
                        errors.append(f"{key}: CSE receipt archive missing or differs from selected receipt")
                    validate_crosscheck_provenance(cross)
                    if not cross.get("matched") or cross.get("model_sha256") != digest(model_path):
                        errors.append(f"{key}: CSE cross-check no longer matches model")
                    cross_input = model_path.with_name("cse-failure-model.json")
                    if (cross.get("input_sha256") != digest(cross_input)
                            or load_json(cross_input) != cse_record(load_json(model_path))):
                        errors.append(f"{key}: CSE input no longer matches its execution receipt")
                    baseline = next(s for s in expected["scenarios"] if not s["overrides"])
                    if (cross["cse_result"]["status"] != "pass"
                            or cross["cse_result"]["checks"]["fault_tree"]["minimal_cut_sets"] != expected["minimal_cut_sets"]
                            or cross["cse_result"]["checks"]["probability"]["probability"] != baseline["probability"]):
                        errors.append(f"{key}: CSE receipt result disagrees with current model")
                    archived = folder / "evidence/analysis/runs" / saved["run_id"]
                    for name in ("model-results.json", "failure-model.json", "analyze_gallery.py", "execution.json"):
                        if not (archived / name).is_file():
                            errors.append(f"{key}: missing immutable run artifact {name}")
                    if ((archived / "model-results.json").read_bytes() != (folder / "evidence/analysis/model-results.json").read_bytes()
                            or digest(archived / "failure-model.json") != digest(model_path)
                            or digest(archived / "analyze_gallery.py") != expected["configuration"]["scripts/analyze_gallery.py"]):
                        errors.append(f"{key}: immutable run differs from its current view")
                    for name in ("requirements.md", "architecture.md", "hazard-analysis.md"):
                        if digest(archived / (name + ".snapshot")) != expected["configuration"][name]:
                            errors.append(f"{key}: immutable source snapshot differs: {name}")
                    validate_execution(load_json(archived / "execution.json"), saved,
                                       digest(archived / "model-results.json"), "analyze_gallery.py")
                temporal = folder / "analysis/run_clamp_checks.py"
                temporal_cases = 0
                if temporal.exists():
                    observed = subprocess.run([sys.executable, "-B", str(temporal), "--check"], capture_output=True, text=True, timeout=15)
                    if observed.returncode:
                        errors.append(f"{key}: temporal result check failed: {observed.stderr.strip()}")
                    current = folder / "evidence/analysis/clamp-results.json"
                    record = load_json(current)
                    temporal_cases = record["test_count"]
                    archived = current.parent / "runs" / record["run_id"]
                    if (archived / current.name).read_bytes() != current.read_bytes():
                        errors.append(f"{key}: immutable temporal report differs")
                    for name, expected_hash in record["configuration"].items():
                        archived_name = Path(name).name + (".snapshot" if name.endswith(".md") else "")
                        if digest(archived / archived_name) != expected_hash:
                            errors.append(f"{key}: immutable temporal source differs: {name}")
                    validate_execution(load_json(archived / "execution.json"), record, digest(current), "run_clamp_checks.py")
                summaries.append({"case": folder.name, "identities": {g: len(ids) for g, ids in identities.items()},
                                  "evidence": counts, "open_references": sorted(unresolved),
                                  "boolean_assignments": assignments,
                                  "temporal_cases": temporal_cases,
                                  "standards_review": "partial", "physical_validation": "not_performed"})
            except (OSError, ValueError, TypeError, KeyError, AttributeError, subprocess.TimeoutExpired) as error:
                errors.append(f"{key}: {error}")
    return errors, {"schema_version": 1, "scope": "declared_gallery_records_and_reproducible_abstract_models",
                    "systems": summaries, "physical_validation": "not_performed", "risk_acceptance": "not_assessed"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    errors, summary = check()
    print(json.dumps(summary, indent=2))
    if errors:
        parser.exit(1, "\n".join(errors) + "\n")


if __name__ == "__main__":
    main()
