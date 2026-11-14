"""Execute temporal clamp challenges, preserving positive and negative outcomes."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import platform

from clamp_model import Clamp

HERE = Path(__file__).resolve().parent


def execute():
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
    files = [HERE / "clamp_model.py", HERE / "run_clamp_checks.py", HERE.parent / "requirements.md"]
    configuration = {p.relative_to(HERE.parent).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    report = {"schema_version": 1, "scope": "sampled_logical_clamp_release_no_fluid_or_mechanical_plant",
              "initial_condition": "Door closed; clamp held open; processor serviced at t=0; infusion-enabled design state.",
              "tick_ms": 100, "watchdog_ms": 200, "closure_target_ms": 500,
              "assumptions": ["Closure delay is a chosen input, not measured or derived from mechanics.",
                              "Input changes occur on ticks; timing between ticks and jitter are unmodeled.",
                              "Closed means model state only; tubing occlusion and delivered dose are unmeasured.",
                              "Post-fault manual rearm is a new proposed policy, not an accepted product requirement."],
              "configuration": configuration, "results": results,
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
    path = HERE.parent / "evidence/analysis/clamp-results.json"
    if args.check:
        if json.loads(path.read_text(encoding="utf-8")) != record:
            parser.exit(1, "Stored clamp evidence is stale or differs from execution\n")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        receipt = {"run_id": record["run_id"], "executed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                   "python": platform.python_version(), "command": "python3 analysis/run_clamp_checks.py",
                   "result_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
        run_dir = path.parent / "runs" / record["run_id"]
        run_dir.mkdir(parents=True, exist_ok=True)
        run_path = run_dir / "execution.json"
        if not run_path.exists():
            run_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
        archived = {"clamp-results.json": path.read_bytes(), "clamp_model.py": (HERE / "clamp_model.py").read_bytes(),
                    "run_clamp_checks.py": Path(__file__).read_bytes(),
                    "requirements.md.snapshot": (HERE.parent / "requirements.md").read_bytes()}
        for name, content in archived.items():
            archive_path = run_dir / name
            if archive_path.exists() and archive_path.read_bytes() != content:
                raise ValueError("Immutable clamp archive collision")
            if not archive_path.exists():
                archive_path.write_bytes(content)
    failures = [result["id"] for result in record["results"] if result["test_outcome"] != "pass"]
    if failures:
        parser.exit(1, "Unexpected temporal outcomes: " + ", ".join(failures) + "\n")
    print(f"{record['test_count']} temporal cases; {record['expected_criterion_failures']} retained criterion violations ({record['expected_requirement_failures']} requirement-scope failures); no physical validation")


if __name__ == "__main__":
    main()
