from pathlib import Path
import copy
import json
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_trace import check


class TraceTests(unittest.TestCase):
    def setUp(self):
        self.folder = ROOT / "examples/worked/cold-storage-alarm"
        self.data = json.loads((self.folder / "baseline.json").read_text(encoding="utf-8"))

    def test_executed_model_trace_is_complete_without_acceptance_claim(self):
        errors, summary = check(self.data, self.folder)
        self.assertEqual(errors, [])
        self.assertEqual(summary["requirements_with_passing_model_evidence"], 4)
        self.assertEqual(summary["acceptance"], "not_assessed")

    def test_broken_allocations_duplicate_ids_and_uncovered_requirement_fail(self):
        for mutation in ["allocation", "duplicate", "coverage"]:
            data = copy.deepcopy(self.data)
            if mutation == "allocation":
                data["functions"][0]["components"] = ["MISSING"]
            elif mutation == "duplicate":
                data["requirements"].append(data["requirements"][0])
            else:
                data["requirements"].append({"id": "REQ-99", "source": "NEED-01", "functions": ["FUN-01"], "status": "proposed"})
            self.assertTrue(check(data, self.folder)[0], mutation)

    def test_planned_evidence_does_not_count_as_passing(self):
        data = copy.deepcopy(self.data)
        data["evidence"][0]["status"] = "planned"
        data["evidence"][0]["artifact"] = "not-created.pdf"
        errors, summary = check(data, self.folder)
        self.assertEqual(errors, [])
        self.assertEqual(summary["requirements_with_passing_model_evidence"], 0)

    def test_stale_or_missing_evidence_and_path_escape_fail(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            folder = Path(temp) / "case"
            shutil.copytree(self.folder, folder)
            folder.joinpath("reference_model.py").write_text("Changed")
            self.assertTrue(check(self.data, folder)[0])
        for path in ["missing.json", "../outside.json"]:
            data = copy.deepcopy(self.data)
            data["evidence"][0]["artifact"] = path
            self.assertTrue(check(data, self.folder)[0])

    def test_failed_or_inconclusive_outcomes_are_not_passing_requirements(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            folder = Path(temp) / "case"
            shutil.copytree(self.folder, folder)
            path = folder / "evidence/results.json"
            record = json.loads(path.read_text(encoding="utf-8"))
            record["results"][0]["result"] = "fail"
            record["results"][3]["result"] = "inconclusive"
            path.write_text(json.dumps(record), encoding="utf-8")
            errors, summary = check(self.data, folder)
            self.assertEqual(errors, [])
            self.assertEqual(summary["requirements_with_passing_model_evidence"], 2)

    def test_missing_configuration_or_outcome_is_rejected(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            folder = Path(temp) / "case"
            shutil.copytree(self.folder, folder)
            path = folder / "evidence/results.json"
            record = json.loads(path.read_text(encoding="utf-8"))
            record["configuration"].pop("baseline.json")
            record["results"].pop()
            path.write_text(json.dumps(record), encoding="utf-8")
            self.assertTrue(check(self.data, folder)[0])

    def test_malformed_input_reports_failure_without_crash(self):
        for data in [None, [], {}, {"sources": [None]}, {**self.data, "verification": [{"id": "VER-01", "requirements": None, "evidence": []}]}]:
            self.assertTrue(check(data, self.folder)[0])
