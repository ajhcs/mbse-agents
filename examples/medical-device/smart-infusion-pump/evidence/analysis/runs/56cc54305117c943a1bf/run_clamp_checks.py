"""Execute temporal clamp challenges, preserving positive and negative outcomes."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import platform
import sys

import clamp_model
from clamp_model import Clamp

_LOADED_MODULE_CODE = sys._getframe().f_code
HERE = Path(__file__).resolve().parent


def bind_loaded_sources():
    bindings = {}
    for name, loaded_code in (("analysis/clamp_model.py", clamp_model._LOADED_MODULE_CODE),
                              ("analysis/run_clamp_checks.py", _LOADED_MODULE_CODE)):
        path = (HERE.parent / name).resolve()
        if Path(loaded_code.co_filename).resolve() != path:
            raise ValueError(f"Loaded source origin differs: {name}")
        source = path.read_bytes()
        compiled = compile(source, loaded_code.co_filename, "exec", dont_inherit=True, optimize=sys.flags.optimize)
        if compiled != loaded_code:
            raise ValueError(f"Loaded code differs from source bytes: {name}")
        bindings[name] = hashlib.sha256(source).hexdigest()
    return bindings


_BOUND_SOURCES = bind_loaded_sources()


def capture_configuration():
    names = ("analysis/clamp_model.py", "analysis/run_clamp_checks.py", "requirements.md")
    sources = {name: (HERE.parent / name).read_bytes() for name in names}
    configuration = {name: hashlib.sha256(content).hexdigest() for name, content in sources.items()}
    if any(configuration[name] != value for name, value in _BOUND_SOURCES.items()):
        raise ValueError("Source changed after import; no clamp evidence published")
    return sources, configuration


def unchanged_configuration(expected):
    sources, configuration = capture_configuration()
    if configuration != expected:
        raise ValueError("Configuration changed during execution; no clamp evidence published")
    return sources


def execute():
    _, configuration = capture_configuration()
    results = []
    for cause in ("door", "power", "watchdog"):
        for delay in range(0, 701, 100):
            model = Clamp(closing_ms=delay)
            trace = []
            for time_ms in range(100, 1101, 100):
                trace.append(model.step(time_ms, door_open=cause == "door", power=cause != "power",
                                        cpu_services=cause != "watchdog"))
            first = next((row["time_ms"] for row in trace if row["closed"]), None)
            origin = 0 if cause == "watchdog" else 100
            observed = first is not None and first - origin <= 500
            predicted = delay <= (300 if cause == "watchdog" else 500)
            watchdog_release = next((row["release_ms"] for row in trace if row["release_ms"] is not None), None)
            requirement_observed = watchdog_release == 200 if cause == "watchdog" else observed
            results.append({"id": f"CLAMP-{cause}-{delay}", "requirements": ["REQ-SAF-002" if cause == "watchdog" else "REQ-SAF-001"],
                            "criterion": "PROPOSED-COMBINED-500-MS" if cause == "watchdog" else "REQ-SAF-001-CLOSURE",
                            "scope": "conditional_release_plus_assumed_closing_delay", "assumed_closing_ms": delay,
                            "trigger_ms": origin, "first_closed_ms": first,
                            "criterion_outcome": "pass" if observed else "fail",
                            "expected_criterion_outcome": "pass" if predicted else "fail",
                            "requirement_outcome": "pass" if requirement_observed else "fail",
                            "requirement_scope": "watchdog release only; mechanical safe-state interpretation unresolved" if cause == "watchdog" else "logical closure under assumed plant delay",
                            "test_outcome": "pass" if observed == predicted and (cause != "watchdog" or requirement_observed) else "fail", "trace": trace})
    for fault in ("jammed", "interlock_failed"):
        model = Clamp()
        trace = [model.step(time_ms, door_open=True, **{fault: True}) for time_ms in range(100, 1101, 100)]
        failed = not trace[5]["closed"]
        results.append({"id": f"CLAMP-{fault}", "requirements": ["REQ-SAF-001"],
                        "scope": "injected_uncovered_fault_counterexample", "requirement_outcome": "fail" if failed else "pass",
                        "criterion": "REQ-SAF-001-CLOSURE", "criterion_outcome": "fail" if failed else "pass",
                        "expected_criterion_outcome": "fail", "test_outcome": "pass" if failed else "fail", "trace": trace})
    model = Clamp()
    trace = [model.step(time_ms, power=False, cpu_services=False) for time_ms in range(100, 601, 100)]
    trace += [model.step(time_ms, power=True, cpu_services=True) for time_ms in (700, 800)]
    held_closed = trace[-1]["closed"] and trace[-1]["latched"]
    trace.append(model.step(900, manual_rearm=True))
    rearmed = not trace[-1]["closed"] and trace[-1]["hold_open"]
    results.append({"id": "CLAMP-recovery", "requirements": ["REQ-SAF-001"],
                    "scope": "proposed_no_automatic_rearm_policy", "requirement_outcome": "not_assessed",
                    "test_outcome": "pass" if held_closed and rearmed else "fail", "trace": trace})
    model = Clamp()
    trace = [model.step(time_ms, door_open=True, manual_rearm=True) for time_ms in range(100, 901, 100)]
    inhibited = all(not row["hold_open"] for row in trace) and trace[-1]["closed"]
    results.append({"id": "CLAMP-rearm-door-open", "requirements": ["REQ-SAF-001"],
                    "scope": "proposed_rearm_interlock", "requirement_outcome": "not_assessed",
                    "test_outcome": "pass" if inhibited else "fail", "trace": trace})
    unchanged_configuration(configuration)
    report = {"schema_version": 1, "scope": "sampled_logical_clamp_release_no_fluid_or_mechanical_plant",
              "initial_condition": "Door closed; clamp held open; processor serviced at t=0; infusion-enabled design state.",
              "tick_ms": 100, "watchdog_ms": 200, "closure_target_ms": 500,
              "assumptions": ["Closure delay is a chosen input, not measured or derived from mechanics.",
                              "Input changes occur on ticks; timing between ticks and jitter are unmodeled.",
                              "Closed means model state only; tubing occlusion and delivered dose are unmeasured.",
                              "Post-fault manual rearm is a new proposed policy, not an accepted product requirement."],
              "configuration": configuration, "loaded_sources": dict(_BOUND_SOURCES), "results": results,
              "test_count": len(results), "expected_requirement_failures": sum(r["requirement_outcome"] == "fail" for r in results),
              "expected_criterion_failures": sum(r.get("criterion_outcome") == "fail" for r in results),
              "physical_validation": "not_performed", "acceptance": "not_assessed"}
    report["run_id"] = hashlib.sha256(json.dumps(report, sort_keys=True).encode()).hexdigest()[:20]
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    record = execute()
    sources = unchanged_configuration(record["configuration"])
    path = HERE.parent / "evidence/analysis/clamp-results.json"
    if args.check:
        if json.loads(path.read_text(encoding="utf-8")) != record:
            parser.exit(1, "Stored clamp evidence is stale or differs from execution\n")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        content = (json.dumps(record, indent=2) + "\n").encode()
        receipt = {"schema_version": 1, "run_id": record["run_id"], "executed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                   "python": platform.python_version(), "command": list(sys.orig_argv),
                   "entrypoint": str(Path(__file__).resolve()), "scope": record["scope"], "loaded_sources": record["loaded_sources"],
                   "result_sha256": hashlib.sha256(content).hexdigest()}
        run_dir = path.parent / "runs" / record["run_id"]
        run_dir.mkdir(parents=True, exist_ok=True)
        run_path = run_dir / "execution.json"
        if not run_path.exists():
            run_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
        archived = {"clamp-results.json": content, "clamp_model.py": sources["analysis/clamp_model.py"],
                    "run_clamp_checks.py": sources["analysis/run_clamp_checks.py"],
                    "requirements.md.snapshot": sources["requirements.md"]}
        for name, content in archived.items():
            archive_path = run_dir / name
            if archive_path.exists() and archive_path.read_bytes() != content:
                raise ValueError("Immutable clamp archive collision")
            if not archive_path.exists():
                archive_path.write_bytes(content)
        unchanged_configuration(record["configuration"])
        path.write_bytes(archived["clamp-results.json"])
    failures = [result["id"] for result in record["results"] if result["test_outcome"] != "pass"]
    if failures:
        parser.exit(1, "Unexpected temporal outcomes: " + ", ".join(failures) + "\n")
    print(f"{record['test_count']} temporal cases; {record['expected_criterion_failures']} retained criterion violations ({record['expected_requirement_failures']} requirement-scope failures); no physical validation")


if __name__ == "__main__":
    main()
