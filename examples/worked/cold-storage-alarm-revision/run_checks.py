"""Run explicit procedures and save measured reference-model evidence. No model API."""
from pathlib import Path
import argparse
import json
import sys
import reference_model
import evidence_io
import explore_states

from reference_model import Alarm
from evidence_io import bind_loaded_sources, capture, compare, save
from explore_states import check_inputs, explore

HERE = Path(__file__).resolve().parent
_LOADED_MODULE_CODE = sys._getframe().f_code
_LOADED_SOURCES = bind_loaded_sources(HERE, {
    "run_checks.py": _LOADED_MODULE_CODE,
    "reference_model.py": reference_model._LOADED_MODULE_CODE,
    "evidence_io.py": evidence_io._LOADED_MODULE_CODE,
    "explore_states.py": explore_states._LOADED_MODULE_CODE,
})


def exercise(alarm_type=Alarm):
    results = []

    def record(identifier, passed, observed):
        results.append({"verification": identifier, "result": "pass" if passed else "fail", "observed": observed})

    model = alarm_type()
    samples = [(t, model.step(t, 8)["high"]) for t in range(0, 2200, 100)]
    first = next((t for t, active in samples if active), None)
    record("VER-01", first == 2000 and not any(v for t, v in samples if t < 2000),
           {"first_high_ms": first, "asserted_before_2s": any(v for t, v in samples if t < 2000)})

    model = alarm_type()
    states = [model.step(t, 8 if t < 1900 or t >= 2000 else 7.9) for t in range(0, 3900, 100)]
    record("VER-02", not any(s["high"] for s in states), {"high_assertions": sum(s["high"] for s in states), "below_threshold_ms": 1900})

    model = alarm_type()
    states = [(t, model.step(t, None)["sensor_fault"]) for t in range(0, 700, 100)]
    first = next((t for t, active in states if active), None)
    record("VER-03", first == 500, {"first_sensor_fault_ms": first})

    model = alarm_type()
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

    model = alarm_type()
    for t in range(0, 600, 100):
        model.step(t, float("nan"))
    fault = model.sensor_fault
    recovered = model.step(600, 7)
    expected = [{"time_ms": 500, "high": False, "sensor_fault": True},
                {"time_ms": 600, "high": False, "sensor_fault": False}]
    record("VER-06", fault and not recovered["local_alarm"] and model.events == expected,
           {"invalid_nan_fault": fault, "recovered": recovered, "events": model.events})
    passed, observed = explore(alarm_type, fault_delay_ms=500)
    record("VER-07", passed, observed)
    passed, observed = check_inputs(alarm_type, fault_delay_ms=500)
    record("VER-08", passed, observed)
    return results


def evidence(command=None):
    return capture(HERE, exercise, command or [sys.executable, __file__, *sys.argv[1:]], loaded_sources=_LOADED_SOURCES)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check stored evidence against the current model and files")
    parser.add_argument("--output", type=Path, help="New output file, or record to reproduce with --check")
    args = parser.parse_args()
    try:
        record = evidence()
    except (OSError, ValueError) as error:
        parser.exit(1, str(error) + "\n")
    output = args.output or HERE / "evidence" / "results.json"
    if args.check:
        saved = json.loads(output.read_text(encoding="utf-8"))
        # Locate the repository validator from both the live example and its snapshots.
        root = next(p for p in HERE.parents if (p / "scripts/check_trace.py").is_file())
        sys.path.insert(0, str(root / "scripts"))
        from check_trace import validate_record_metadata
        problems = validate_record_metadata(saved, HERE) + compare(saved, record)
        if problems:
            parser.exit(1, "Stored evidence is invalid/stale or disagrees with execution: " + ", ".join(problems) + "\n")
    else:
        try:
            archive = save(HERE, record, args.output)
        except (OSError, ValueError) as error:
            parser.exit(1, str(error) + "\n")
        print(f"Recorded execution: {archive}")
    failures = [r["verification"] for r in record["results"] if r["result"] != "pass"]
    if failures:
        parser.exit(1, "Failed: " + ", ".join(failures) + "\n")
    print(f"{len(record['results'])} reference-model procedures pass; hardware acceptance remains open")


if __name__ == "__main__":
    main()
