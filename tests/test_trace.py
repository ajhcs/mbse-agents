from pathlib import Path
import copy
import json
import shutil
import sys
import tempfile
import unittest
import hashlib
import subprocess
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_trace import check
sys.path.insert(0, str(ROOT / "examples/worked/cold-storage-alarm"))
from evidence_io import capture, save


class TraceTests(unittest.TestCase):
    def setUp(self):
        self.folder = ROOT / "examples/worked/cold-storage-alarm"
        self.data = json.loads((self.folder / "baseline.json").read_text(encoding="utf-8"))

    def test_executed_model_trace_is_complete_without_acceptance_claim(self):
        errors, summary = check(self.data, self.folder)
        self.assertEqual(errors, [])
        self.assertEqual(summary["requirements_with_passing_model_evidence"], 4)
        self.assertEqual(summary["acceptance"], "not_assessed")
        self.assertEqual(summary["integrity"], "valid")
        self.assertEqual(summary["valid_execution_records"], ["EVD-01"])

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

    def test_stale_scope_or_configuration_never_contribute_passing_totals(self):
        original = json.loads((self.folder / "evidence/results.json").read_text())
        for mutation in ("scope", "configuration"):
            record = copy.deepcopy(original)
            if mutation == "scope":
                record["scope"] = "a-different-model"
            else:
                record["configuration"]["reference_model.py"] = "0" * 64
            # Only intercept the evidence parse; the configured baseline still
            # parses normally, so this probe makes no filesystem changes.
            loads = json.loads
            def parse(value, *args, **kwargs):
                result = loads(value, *args, **kwargs)
                return record if isinstance(result, dict) and "results" in result else result
            with patch("check_trace.json.loads", side_effect=parse):
                errors, summary = check(self.data, self.folder)
            self.assertTrue(errors, mutation)
            self.assertEqual(summary["reported_procedures"], 8)
            self.assertEqual(summary["executed_procedures"], 0)
            self.assertEqual(summary["requirements_with_passing_model_evidence"], 0)
            self.assertEqual(summary["rejected_execution_records"], ["EVD-01"])

    def test_rejects_unsupported_or_contradictory_record_contracts(self):
        original = json.loads((self.folder / "evidence/results.json").read_text())
        mutations = {
            "schema": lambda r: r.update(schema_version=99),
            "tool": lambda r: r.pop("tool"),
            "hardware acceptance": lambda r: r.update(acceptance="accepted_for_hardware"),
            "claim scope": lambda r: r.update(claim_support="physical-device-validated"),
            "run ID": lambda r: r["execution"].update(run_id="../outside"),
            "timestamp": lambda r: r["execution"].update(started_at="yesterday"),
            "naive timestamp": lambda r: r["execution"].update(started_at="2026-01-01T00:00:00"),
            "command": lambda r: r["execution"].update(command=[]),
            "observations": lambda r: r["results"][0].update(observed=True),
            "nonfinite": lambda r: r["results"][0].update(observed={"time": float("nan")}),
            "duplicate": lambda r: r["results"].append(copy.deepcopy(r["results"][0])),
            "unsubstantiated review": lambda r: r.update(review="reviewed"),
        }
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            folder = Path(temp) / "case"
            shutil.copytree(self.folder, folder)
            for name, mutate in mutations.items():
                record = copy.deepcopy(original)
                mutate(record)
                (folder / "evidence/results.json").write_text(json.dumps(record))
                errors, summary = check(self.data, folder)
                self.assertTrue(errors, name)
                self.assertEqual(summary["requirements_with_passing_model_evidence"], 0, name)
                self.assertEqual(summary["executed_procedures"], 0, name)

    def test_external_actor_and_source_locators_are_checked(self):
        self.assertIn({"id": "IFC-02", "from": "ACTOR-01", "to": "COMP-02"}, self.data["interfaces"])
        for mutation in ("actor", "source locator", "source coverage"):
            data = copy.deepcopy(self.data)
            if mutation == "actor":
                data["actors"] = []
            elif mutation == "source locator":
                data["sources"][0]["locator"] = "ABSENT SOURCE"
            else:
                data["configuration_files"].remove("brief.md")
            self.assertTrue(check(data, self.folder)[0], mutation)

    def test_drafted_requires_an_existing_artifact_but_never_counts_as_execution(self):
        data = copy.deepcopy(self.data)
        data["evidence"][0].update(status="drafted", artifact="verification.md")
        errors, summary = check(data, self.folder)
        self.assertEqual(errors, [])
        self.assertEqual(summary["executed_procedures"], 0)
        self.assertEqual(summary["requirements_with_passing_model_evidence"], 0)
        data["evidence"][0]["artifact"] = "absent.pdf"
        self.assertTrue(check(data, self.folder)[0])

    def test_supplied_baseline_must_match_configuration_for_executed_evidence(self):
        data = copy.deepcopy(self.data)
        data["actors"][0]["authority"] = "Changed without updating the recorded baseline"
        errors, summary = check(data, self.folder)
        self.assertTrue(any("differs from its configured artifact" in e for e in errors))
        self.assertEqual(summary["requirements_with_passing_model_evidence"], 0)

    def test_runner_and_trace_checker_agree_on_review_reference_integrity(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            folder = Path(temp) / "case"
            shutil.copytree(self.folder, folder)
            path = folder / "evidence/results.json"
            original = json.loads(path.read_text())
            review = folder / "review.md"
            review.write_text("Review fixture: sampled model only; no hardware acceptance.\n")
            valid = {"reviewer": "test fixture", "artifact": "review.md", "sha256": hashlib.sha256(review.read_bytes()).hexdigest()}
            for reference, expected_valid in (({}, False), ({**valid, "sha256": "0" * 64}, False), (valid, True)):
                record = copy.deepcopy(original)
                record.update(review="reviewed", review_reference=reference)
                path.write_text(json.dumps(record))
                errors, _ = check(self.data, folder)
                run = subprocess.run([sys.executable, "-B", str(folder / "run_checks.py"), "--check"], capture_output=True, text=True)
                self.assertEqual(not errors, expected_valid, errors)
                self.assertEqual(run.returncode == 0, expected_valid, run.stdout + run.stderr)

    def test_current_runner_requires_saved_loaded_source_bindings(self):
        original = json.loads((self.folder / "evidence/results.json").read_text())
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            path = Path(temp) / "record.json"
            for mutation in ("missing", "empty", "altered"):
                record = copy.deepcopy(original)
                if mutation == "missing":
                    record["execution"].pop("loaded_sources")
                elif mutation == "empty":
                    record["execution"]["loaded_sources"] = {}
                else:
                    record["execution"]["loaded_sources"]["reference_model.py"] = "0" * 64
                path.write_text(json.dumps(record))
                run = subprocess.run([sys.executable, "-B", str(self.folder / "run_checks.py"), "--check", "--output", str(path)], capture_output=True, text=True)
                self.assertNotEqual(run.returncode, 0, mutation)
                self.assertIn("loaded-source bindings", run.stderr)

    def test_trace_checker_rejects_supplied_bindings_that_disagree_with_configuration(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            folder = Path(temp) / "case"
            shutil.copytree(self.folder, folder)
            path = folder / "evidence/results.json"
            record = json.loads(path.read_text())
            record["execution"]["loaded_sources"]["reference_model.py"] = "0" * 64
            path.write_text(json.dumps(record))
            errors, summary = check(self.data, folder)
            self.assertTrue(any("loaded-source bindings differ" in error for error in errors), errors)
            self.assertEqual(summary["executed_procedures"], 0)
            self.assertEqual(summary["requirements_with_passing_model_evidence"], 0)

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
            self.assertEqual(summary["integrity"], "valid")
            self.assertEqual(summary["executed_procedures"], 8)
            self.assertEqual(summary["failed_procedures"], 1)
            self.assertEqual(summary["inconclusive_procedures"], 1)

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


class EvidenceHistoryTests(unittest.TestCase):
    def test_capture_requires_bindings_for_configured_python_sources(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            folder = Path(temp)
            (folder / "baseline.json").write_text(json.dumps({"configuration_files": ["model.py"]}))
            (folder / "model.py").write_text("value = 1\n")
            with self.assertRaisesRegex(ValueError, "require loaded-source bindings"):
                capture(folder, lambda: [], ["test"])
            self.assertFalse((folder / "evidence").exists())

    def test_default_history_refuses_symlink_escape_without_writing_outside(self):
        record = json.loads((ROOT / "examples/worked/cold-storage-alarm/evidence/results.json").read_text())
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            folder, outside = Path(temp) / "case", Path(temp) / "outside"
            folder.mkdir()
            outside.mkdir()
            try:
                (folder / "evidence").symlink_to(outside, target_is_directory=True)
            except OSError:
                self.skipTest("Host does not permit directory symlink fixtures")
            with self.assertRaises(ValueError):
                save(folder, record)
            self.assertEqual(list(outside.iterdir()), [])

    def test_new_execution_preserves_prior_selected_bytes_and_refuses_archive_collision(self):
        source = ROOT / "examples/worked/cold-storage-alarm/evidence/results.json"
        original = source.read_bytes()
        record = json.loads(original)
        record["execution"]["run_id"] = "test-second-run"
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            folder = Path(temp)
            selected = folder / "evidence/results.json"
            selected.parent.mkdir()
            selected.write_bytes(original)
            archive = save(folder, record)
            self.assertEqual(selected.read_bytes(), archive.read_bytes())
            original_id = json.loads(original)["execution"]["run_id"]
            self.assertEqual((folder / "evidence/runs" / (original_id + ".json")).read_bytes(), original)
            selected_before = selected.read_bytes()
            record["results"][0]["result"] = "fail"
            with self.assertRaises(ValueError):
                save(folder, record)
            self.assertEqual(selected.read_bytes(), selected_before)
            with self.assertRaises(ValueError):
                save(folder, record, selected)
            self.assertEqual(selected.read_bytes(), selected_before)

    def test_configuration_change_during_execution_is_not_recorded(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            folder = Path(temp)
            (folder / "baseline.json").write_text(json.dumps({"configuration_files": ["model.txt"]}))
            (folder / "model.txt").write_text("before")
            def changing_execution():
                (folder / "model.txt").write_text("after")
                return []
            with self.assertRaises(ValueError):
                capture(folder, changing_execution, ["test"])
            self.assertFalse((folder / "evidence").exists())
