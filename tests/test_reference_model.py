from pathlib import Path
import sys
import unittest
import hashlib
import json
import subprocess
import copy
import shutil
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "examples/worked/cold-storage-alarm"))
from reference_model import Alarm
from explore_states import explore, check_inputs


class ReferenceModelTests(unittest.TestCase):
    def test_high_latch_survives_sensor_failure_and_recovers_only_with_valid_ack(self):
        model = Alarm()
        for t in range(0, 2100, 100):
            model.step(t, 8)
        for t in range(2100, 3200, 100):
            model.step(t, None, True)
        self.assertTrue(model.high and model.sensor_fault)
        state = model.step(3200, 7)
        self.assertTrue(state["high"])
        self.assertFalse(state["sensor_fault"])
        self.assertFalse(model.step(3300, 7, True)["local_alarm"])

    def test_invalid_reading_restarts_pending_high_interval(self):
        model = Alarm()
        for t in range(0, 2000, 100):
            model.step(t, 8)
        model.step(2000, float("inf"))
        for t in range(2100, 4100, 100):
            self.assertFalse(model.step(t, 8)["high"])
        self.assertTrue(model.step(4100, 8)["high"])

    def test_invalid_temperature_types_have_fault_semantics(self):
        for value in [None, float("nan"), float("inf"), "8", True]:
            model = Alarm()
            for t in range(0, 1100, 100):
                model.step(t, value)
            self.assertTrue(model.sensor_fault)
            self.assertFalse(model.high)

    def test_time_contract_rejects_gaps_duplicates_and_wrong_types(self):
        for t in [0, -100, 200, 1, 100.0, True]:
            model = Alarm()
            model.step(0, 7)
            with self.assertRaises(ValueError):
                model.step(t, 7)
        with self.assertRaises(ValueError):
            Alarm().step(0, 7, "yes")

    def test_exhaustive_finite_state_exploration_checks_every_input_at_every_state(self):
        passed, observed = explore(Alarm)
        self.assertTrue(passed, observed)
        self.assertGreater(observed["states"], 1)
        self.assertEqual(observed["transitions"], observed["states"] * 6)
        self.assertEqual(observed["counterexamples"], 0)

    def test_explorer_detects_unsafe_acknowledgement_and_missing_events(self):
        class UnsafeAcknowledgement(Alarm):
            def step(self, time_ms, temperature_c, acknowledge=False):
                result = super().step(time_ms, temperature_c, acknowledge)
                if acknowledge:
                    self.high = False
                    result["high"] = False
                    result["local_alarm"] = self.sensor_fault
                return result

        class MissingEvents(Alarm):
            def step(self, *args, **kwargs):
                result = super().step(*args, **kwargs)
                self.events = []
                return result

        for broken in (UnsafeAcknowledgement, MissingEvents):
            passed, observed = explore(broken)
            self.assertFalse(passed, broken.__name__)
            self.assertTrue(observed["counterexample"])

    def test_input_exploration_covers_rejection_and_invalid_reading_semantics(self):
        passed, observed = check_inputs(Alarm)
        self.assertTrue(passed, observed)
        self.assertEqual(observed["failures"], [])

    def test_input_exploration_detects_mutation_before_invalid_acknowledgement_rejection(self):
        class RejectionMutates(Alarm):
            def step(self, time_ms, temperature_c, acknowledge=False):
                if type(acknowledge) is not bool:
                    self.high = True
                    raise ValueError("Acknowledge must be boolean")
                return super().step(time_ms, temperature_c, acknowledge)
        passed, observed = check_inputs(RejectionMutates)
        self.assertFalse(passed)
        self.assertIn("changed state on rejected nonboolean acknowledgement", observed["failures"])

    def test_evidence_rejects_each_python_source_changed_after_import(self):
        root = Path(__file__).resolve().parents[1]
        original = root / "examples/worked/cold-storage-alarm"
        code = '''
from pathlib import Path
import sys
folder = Path(sys.argv[1])
sys.path.insert(0, str(folder))
import run_checks
source = folder / sys.argv[2]
text = source.read_text()
if source.name == "reference_model.py":
    text = text.replace("self.sensor_fault = time_ms - self.invalid_since >= 1000",
                        "self.sensor_fault = time_ms - self.invalid_since >= 2000")
else:
    text += "\\n# Source changed after the module was loaded.\\n"
source.write_text(text)
try:
    run_checks.evidence(command=["test-source-binding"])
except ValueError as error:
    if "Source changed after import" not in str(error):
        raise
    print(error)
else:
    raise AssertionError("Produced evidence using source bytes that were not loaded")
'''
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=root) as temp:
            for filename in ("reference_model.py", "run_checks.py", "explore_states.py", "evidence_io.py"):
                folder = Path(temp) / filename.removesuffix(".py")
                shutil.copytree(original, folder)
                selected_before = (folder / "evidence/results.json").read_bytes()
                run = subprocess.run([sys.executable, "-B", "-c", code, str(folder), filename], capture_output=True, text=True)
                self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
                self.assertEqual((folder / "evidence/results.json").read_bytes(), selected_before)

    def test_revision_receipt_requires_execution_provenance(self):
        root = Path(__file__).resolve().parents[1]
        folder = root / "examples/worked/cold-storage-alarm-revision"
        original = json.loads((folder / "evidence/revision-check.json").read_text())
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=root) as temp:
            output = Path(temp) / "receipt.json"
            for mutation in ("missing", "timestamps", "command", "bindings"):
                record = copy.deepcopy(original)
                if mutation == "missing":
                    record.pop("execution")
                elif mutation == "timestamps":
                    record["execution"]["finished_at"] = "not-a-time"
                elif mutation == "command":
                    record["execution"]["command"] = []
                else:
                    record["execution"].pop("loaded_sources")
                output.write_text(json.dumps(record))
                run = subprocess.run([sys.executable, "-B", str(folder / "compare_revisions.py"), "--check", "--output", str(output)], capture_output=True, text=True)
                self.assertNotEqual(run.returncode, 0, mutation)
                self.assertTrue("provenance" in run.stderr or "bindings" in run.stderr, run.stderr)

    def test_finite_integer_reading_does_not_overflow_float_conversion(self):
        model = Alarm()
        for tick in range(0, 2100, 100):
            model.step(tick, 10 ** 400)
        self.assertTrue(model.high)
        self.assertFalse(model.sensor_fault)

    def test_original_snapshot_is_byte_preserved_and_still_reproduces(self):
        root = Path(__file__).resolve().parents[1]
        snapshot = root / "examples/worked/cold-storage-alarm/history/legacy-v1"
        manifest = json.loads((snapshot / "snapshot.json").read_text())
        for name, digest in manifest["files"].items():
            self.assertEqual(hashlib.sha256((snapshot / name).read_bytes()).hexdigest(), digest, name)
        run = subprocess.run([sys.executable, "-B", str(snapshot / "run_checks.py"), "--check"], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)

    def test_revision_walkthrough_reproduces_expected_failure_then_repair(self):
        root = Path(__file__).resolve().parents[1]
        path = root / "examples/worked/cold-storage-alarm-revision/compare_revisions.py"
        run = subprocess.run([sys.executable, "-B", str(path), "--check"], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
