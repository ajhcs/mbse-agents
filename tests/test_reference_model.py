from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "examples/worked/cold-storage-alarm"))
from reference_model import Alarm


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
