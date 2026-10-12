"""Run explicit procedures and save measured reference-model evidence. No model API."""
from pathlib import Path
import argparse
import hashlib
import json
import platform

from reference_model import Alarm

HERE = Path(__file__).resolve().parent


def exercise():
    results = []

    def record(identifier, passed, observed):
        results.append({"verification": identifier, "result": "pass" if passed else "fail", "observed": observed})

    model = Alarm()
    samples = [(t, model.step(t, 8)["high"]) for t in range(0, 2200, 100)]
    first = next((t for t, active in samples if active), None)
    record("VER-01", first == 2000 and not any(v for t, v in samples if t < 2000),
           {"first_high_ms": first, "asserted_before_2s": any(v for t, v in samples if t < 2000)})

    model = Alarm()
    states = [model.step(t, 8 if t < 1900 or t >= 2000 else 7.9) for t in range(0, 3900, 100)]
    record("VER-02", not any(s["high"] for s in states), {"high_assertions": sum(s["high"] for s in states), "below_threshold_ms": 1900})

    model = Alarm()
    states = [(t, model.step(t, None)["sensor_fault"]) for t in range(0, 1200, 100)]
    first = next((t for t, active in states if active), None)
    record("VER-03", first == 1000, {"first_sensor_fault_ms": first})

    model = Alarm()
    for t in range(0, 2100, 100):
        model.step(t, 9)
    high_ack = model.step(2100, 9, True)["high"]
    recovered_without_ack = model.step(2200, 7)["high"]
    low_ack = model.step(2300, 7, True)["high"]
    record("VER-04", high_ack and recovered_without_ack and not low_ack,
           {"high_after_unsafe_ack": high_ack, "high_after_recovery_only": recovered_without_ack, "high_after_valid_ack": low_ack})
    expected = [{"time_ms": 2000, "high": True, "sensor_fault": False},
                {"time_ms": 2300, "high": False, "sensor_fault": False}]
    record("VER-05", model.events == expected, {"events": model.events, "expected_event_count": 2})

    model = Alarm()
    for t in range(0, 1100, 100):
        model.step(t, float("nan"))
    fault = model.sensor_fault
    recovered = model.step(1100, 7)
    expected = [{"time_ms": 1000, "high": False, "sensor_fault": True},
                {"time_ms": 1100, "high": False, "sensor_fault": False}]
    record("VER-06", fault and not recovered["local_alarm"] and model.events == expected,
           {"invalid_nan_fault": fault, "recovered": recovered, "events": model.events})
    return results


def evidence():
    files = ["reference_model.py", "run_checks.py", "baseline.json", "verification.md", "requirements.md", "architecture.md", "brief.md"]
    return {"schema_version": 1, "scope": "illustrative-reference-model", "tool": f"Python {platform.python_version()}",
            "configuration": {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest() for name in files},
            "results": exercise(), "acceptance": "not_accepted_for_hardware", "review": "pending"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check stored evidence against the current model and files")
    parser.add_argument("--output", type=Path, help="Save evidence to an explicit file; default evidence/results.json")
    args = parser.parse_args()
    record = evidence()
    output = args.output or HERE / "evidence" / "results.json"
    if args.check:
        saved = json.loads(output.read_text(encoding="utf-8"))
        if saved["configuration"] != record["configuration"] or saved["results"] != record["results"]:
            parser.exit(1, "Stored evidence is stale or disagrees with execution\n")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8", newline="\n")
    failures = [r["verification"] for r in record["results"] if r["result"] != "pass"]
    if failures:
        parser.exit(1, "Failed: " + ", ".join(failures) + "\n")
    print(f"{len(record['results'])} reference-model procedures pass; hardware acceptance remains open")


if __name__ == "__main__":
    main()
