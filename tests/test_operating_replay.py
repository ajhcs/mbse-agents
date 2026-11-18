from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from package_plugin import build

NAME = "mbse-verification-evidence"
SCRIPT = Path("scripts/replay_gates.py")
TABLE = """| Event | Low | High | Instruction |
| --- | --- | --- | --- |
| Start | 2.1 kg | 4 kg | Continue if both gates hold. |
| Late | 1.8 kg | 5 kg | Continue if both gates hold. |
"""


class GateReplayTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT)
        self.addCleanup(temp.cleanup)
        self.work = Path(temp.name)
        self.script = ROOT / ".agents/skills" / NAME / SCRIPT
        self.table = self.work / "handoff.md"
        self.table.write_text(TABLE, encoding="utf8")
        self.case = {"name": "Arrival", "basis": "Contract fixture",
                     "initial": {"Low": "2.1", "High": 4},
                     "steps": [{"event": "Start", "expect": "allow"},
                               {"event": "Late", "delta": {"Low": "-3/10", "High": 1},
                                "expect": "allow"}]}
        self.plan = {"event_column": "Event",
                     "gates": {"Low": {"sense": "min", "unit": "kg"},
                               "High": {"sense": "max", "unit": "kg"}},
                     "cases": [self.case]}

    def invoke(self):
        path = self.work / "cases.json"
        path.write_text(json.dumps(self.plan), encoding="utf8")
        return subprocess.run([sys.executable, str(self.script), str(self.table), str(path)],
                              cwd=self.work, capture_output=True, text=True)

    def test_packaged_script_replays_issued_bytes_and_inclusive_limits(self):
        folder, _ = build(self.work / "plugin", names=[NAME])
        self.script = folder / "skills" / NAME / SCRIPT
        result = self.invoke()
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(result.stdout)
        self.assertEqual(data["table_sha256"], hashlib.sha256(self.table.read_bytes()).hexdigest())
        self.assertEqual([r["actual"] for r in data["checks"]], ["allow", "allow"])
        self.table.write_text(TABLE.replace("1.8 kg", "1.9 kg"), encoding="utf8")
        result = self.invoke()
        self.assertEqual(result.returncode, 1)
        last = json.loads(result.stdout)["checks"][-1]
        self.assertEqual((last["line"], last["state"]["Low"], last["violations"][0]["issued"]),
                         (4, "9/5", "1.9 kg"))

    def test_loose_maximum_allows_a_required_block(self):
        self.case["steps"][-1].update(expect="block", delta={"High": 2})
        self.assertEqual(self.invoke().returncode, 0)
        self.table.write_text(TABLE.replace("5 kg", "6 kg"), encoding="utf8")
        result = self.invoke()
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)["checks"][-1]["actual"], "allow")

    def test_invalid_and_ambiguous_inputs_do_not_pass(self):
        for invalid in (TABLE + "\n" + TABLE, TABLE.replace("1.8 kg", "1.8 lb"),
                        TABLE.replace("| Late |", "| Start |"), "```\n" + TABLE + "```\n"):
            with self.subTest(invalid=invalid):
                self.table.write_text(invalid, encoding="utf8")
                self.assertEqual(self.invoke().returncode, 2)
        self.table.write_text(TABLE, encoding="utf8")
        self.plan["cases"] = []
        self.assertEqual(self.invoke().returncode, 2)
