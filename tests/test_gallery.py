"""Adversarial checks for exact logic, evidence boundaries and temporal behavior."""
from copy import deepcopy
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import os
import py_compile
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import analyze_gallery as analysis
import check_gallery as gallery

PUMP = ROOT / "examples/medical-device/smart-infusion-pump/analysis"
sys.path.insert(0, str(PUMP))
from clamp_model import Clamp
import run_clamp_checks


def model():
    return {
        "schema_version": 1, "scope": "authored-static-fault-model",
        "id": "SharedEvent", "system": "Unit fixture", "hazard": "HZ-001",
        "mission": "One synthetic demand", "basis": "Unit fixture only",
        "interpretation": "Two paths reuse the same basic event.",
        "probability_assumption": analysis.INDEPENDENCE,
        "events": {name: {"description": name, "basis": "Synthetic fixture", "probability": p}
                   for name, p in (("A", "1/2"), ("B", "1/3"), ("C", "1/5"))},
        "gates": {"AB": {"operator": "and", "inputs": ["A", "B"]},
                  "AC": {"operator": "and", "inputs": ["A", "C"]},
                  "TOP": {"operator": "or", "inputs": ["AB", "AC"]}},
        "top_event": "TOP", "scenarios": [{"id": "base", "basis": "Fixture", "overrides": {}}],
        "claims": [{"id": "NO-A", "description": "A is necessary", "when": {"A": False},
                    "expected_top": False, "expectation": "holds"},
                   {"id": "A-ONLY", "description": "A alone prevents the hazard", "when": {"A": True},
                    "expected_top": False, "expectation": "counterexample"}],
    }


class ExactLogicTests(unittest.TestCase):
    def test_shared_event_and_overlapping_cuts(self):
        result = analysis.analyze(model())
        self.assertEqual(result["completed_assignments"], 8)
        self.assertEqual(result["minimal_cut_sets"], [["A", "B"], ["A", "C"]])
        self.assertEqual(Fraction(result["scenarios"][0]["probability"]), Fraction(7, 30))

    def test_repeated_event_is_idempotent(self):
        value = model()
        value["gates"]["TOP"] = {"operator": "and", "inputs": ["A", "A"]}
        result = analysis.analyze(value)
        self.assertEqual(result["minimal_cut_sets"], [["A"]])
        self.assertEqual(result["scenarios"][0]["probability"], "1/2")

    def test_counterexample_check_does_not_make_claim_true(self):
        claim = analysis.analyze(model())["claims"][1]
        self.assertEqual(claim["result"], "pass")
        self.assertFalse(claim["property_holds"])
        self.assertEqual(claim["counterexamples"], 3)
        self.assertTrue(claim["first_counterexample"]["A"])

    def test_unexpected_counterexample_fails_check(self):
        value = model()
        value["claims"][1]["expectation"] = "holds"
        self.assertEqual(analysis.analyze(value)["result"], "fail")

    def test_boundary_and_tiny_probabilities_are_exact(self):
        value = model()
        value["gates"]["TOP"] = {"operator": "or", "inputs": ["A"]}
        value["events"]["A"]["probability"] = "1/1000000000000000000000000000000"
        value["scenarios"] += [{"id": "zero", "basis": "Boundary", "overrides": {"A": "0"}},
                               {"id": "one", "basis": "Boundary", "overrides": {"A": "1"}}]
        result = analysis.analyze(value)
        self.assertEqual([s["probability"] for s in result["scenarios"]],
                         [value["events"]["A"]["probability"], "0", "1"])

    def test_independence_must_be_explicit_and_supported(self):
        for assumption in (None, "correlated", "unknown"):
            value = model()
            value["probability_assumption"] = assumption
            with self.subTest(assumption=assumption), self.assertRaisesRegex(ValueError, "independence"):
                analysis.analyze(value)

    def test_malformed_graphs_and_records_are_rejected(self):
        variants = []
        value = model(); value["gates"]["TOP"]["operator"] = "xor"; variants.append(value)
        value = model(); value["gates"]["AB"]["inputs"] = ["TOP"]; variants.append(value)
        value = model(); value["gates"]["TOP"]["inputs"] = ["MISSING"]; variants.append(value)
        value = model(); value["gates"]["TOP"]["inputs"] = [None]; variants.append(value)
        value = model(); value["events"]["A"] = []; variants.append(value)
        value = model(); value["gates"]["A"] = {"operator": "or", "inputs": ["B"]}; variants.append(value)
        value = model(); value["claims"][0]["when"]["A"] = 0; variants.append(value)
        value = model(); value["claims"][0]["when"] = []; variants.append(value)
        value = model(); value["scenarios"][0]["overrides"] = []; variants.append(value)
        value = model(); value["scenarios"].append(deepcopy(value["scenarios"][0])); variants.append(value)
        value = model(); del value["top_event"]; variants.append(value)
        for index, value in enumerate(variants):
            with self.subTest(index=index), self.assertRaises(ValueError):
                analysis.analyze(value)

    def test_probability_parser_rejects_unsafe_or_inexact_inputs(self):
        for value in (0.1, True, "1/0", "NaN", "1e99999999", "2", "-1/3", "x"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                analysis.fraction(value)

    def test_duplicate_json_keys_are_rejected(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-gallery-", dir=ROOT) as directory:
            path = Path(directory) / "model.json"
            for text in ('{"events":{"A":1,"A":2}}', '{"value":NaN}', '{"value":Infinity}'):
                path.write_text(text)
                with self.subTest(text=text), self.assertRaises(ValueError):
                    analysis.load_json(path)


class GalleryContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix=".mbse-test-gallery-", dir=ROOT)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.folder = self.root / "examples/aerospace/fixture"
        self.folder.mkdir(parents=True)
        files = {
            "system.yaml": "id: fixture\n",
            "README.md": "[Architecture](architecture.md)\n",
            "requirements.md": "### REQ-FUN-001\n\n**Allocation**: CMP-001\n",
            "architecture.md": "| CMP ID | Name |\n| --- | --- |\n| CMP-001 | Controller |\n",
            "traceability.md": "| VER ID | Requirement |\n| --- | --- |\n| VER-001 | REQ-FUN-001 |\n",
            "assurance-evidence.md": "| EVD ID | Name | Location | Status |\n| --- | --- | --- | --- |\n| EVD-001 | Plan | evidence/plan.md | Drafted |\n",
            "source-review.md": "Candidate basis requires review.\n",
            "evidence/plan.md": "# Draft procedure\n\nFixture only.\n",
        }
        for name, text in files.items():
            path = self.folder / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)
        self.review = {"open_references": [], "source_reviews": [{"requirement": "REQ-FUN-001", "status": "candidate_basis_requires_applicability_review"}]}
        self.write_review()
        snapshot = {"status": "superseded_instructional_baseline_not_current_evidence",
                    "files": {"README.md": {"text": "original", "sha256": hashlib.sha256(b"original").hexdigest()}}}
        (self.folder / "history").mkdir()
        (self.folder / "history/pre-hardening.json").write_text(json.dumps(snapshot))

    def write_review(self):
        (self.folder / "review-status.json").write_text(json.dumps(self.review))

    def assert_error(self, expected):
        errors, _ = gallery.check(self.root)
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_valid_fixture_has_no_errors(self):
        self.assertEqual(gallery.check(self.root)[0], [])

    def test_duplicate_requirement_declaration(self):
        with (self.folder / "requirements.md").open("a") as stream:
            stream.write("\n### REQ-FUN-001\n")
        self.assert_error("duplicate REQ")

    def test_dangling_table_reference_requires_explicit_disposition(self):
        with (self.folder / "traceability.md").open("a") as stream:
            stream.write("| VER-002 | REQ-FUN-999 |\n")
        self.assert_error("unresolved declared record link REQ-FUN-999")
        self.review["open_references"] = [{"id": "REQ-FUN-999", "disposition": "Reserved future requirement"}]
        self.write_review()
        self.assertEqual(gallery.check(self.root)[0], [])

    def test_stale_disposition_is_not_a_blanket_waiver(self):
        self.review["open_references"] = [{"id": "REQ-FUN-999", "disposition": "Reserved"}]
        self.write_review()
        self.assert_error("stale open-reference")

    def test_drafted_artifact_must_exist(self):
        (self.folder / "evidence/plan.md").unlink()
        self.assert_error("drafted artifact absent")

    def test_planned_artifact_can_remain_unproduced(self):
        path = self.folder / "assurance-evidence.md"
        path.write_text(path.read_text().replace("Drafted", "Planned"))
        (self.folder / "evidence/plan.md").unlink()
        self.assertEqual(gallery.check(self.root)[0], [])

    def test_repeated_status_cannot_silently_promote_evidence(self):
        with (self.folder / "assurance-evidence.md").open("a") as stream:
            stream.write("\n| Activity | Evidence | Status |\n| --- | --- | --- |\n| Review | EVD-001 | Executed |\n")
        self.assert_error("conflicting repeated evidence status")

    def test_escaping_evidence_path_is_rejected(self):
        path = self.folder / "assurance-evidence.md"
        path.write_text(path.read_text().replace("evidence/plan.md", "../outside.md"))
        self.assert_error("escaping evidence path")

    def test_broken_markdown_link_is_reported(self):
        (self.folder / "README.md").write_text("[Missing](absent.md)\n")
        self.assert_error("broken local Markdown path")

    def test_historical_bytes_are_checked_but_not_current_claims(self):
        path = self.folder / "history/pre-hardening.json"
        value = json.loads(path.read_text())
        value["files"]["README.md"]["text"] = "changed"
        path.write_text(json.dumps(value))
        self.assert_error("historical snapshot bytes changed")

    def test_source_review_must_cover_unique_current_requirements(self):
        self.review["source_reviews"] *= 2
        self.write_review()
        self.assert_error("duplicate source-review")

    def test_real_gallery_results_and_archives_are_current(self):
        errors, report = gallery.check(ROOT)
        self.assertEqual(errors, [])
        self.assertEqual(len(report["systems"]), 20)
        self.assertEqual(sum(row["boolean_assignments"] for row in report["systems"]), 1664)
        self.assertEqual(sum(row["temporal_cases"] for row in report["systems"]), 28)

    def test_tampered_report_and_archive_are_detected(self):
        source = ROOT / "examples/aerospace/flight-management-system"
        copied = self.root / "examples/aerospace/flight-management-system"
        shutil.copytree(source, copied)
        result = copied / "evidence/analysis/model-results.json"
        data = analysis.load_json(result)
        data["scenarios"][0]["probability"] = "0"
        result.write_text(json.dumps(data))
        errors, _ = gallery.check(self.root)
        self.assertTrue(any("model results stale" in error for error in errors), errors)
        self.assertTrue(any("immutable run differs" in error for error in errors), errors)

    def copy_case(self, case):
        source = next((ROOT / "examples").glob("*/" + case))
        copied = self.root / source.relative_to(ROOT)
        shutil.copytree(source, copied)
        (self.root / "docs").mkdir(exist_ok=True)
        shutil.copyfile(ROOT / "docs/sources-domain.md", self.root / "docs/sources-domain.md")
        return copied

    def test_execution_receipts_require_full_provenance(self):
        for case, result_name in (("flight-management-system", "model-results.json"),
                                  ("smart-infusion-pump", "clamp-results.json")):
            copied = self.copy_case(case)
            report = analysis.load_json(copied / "evidence/analysis" / result_name)
            receipt = copied / "evidence/analysis/runs" / report["run_id"] / "execution.json"
            original = analysis.load_json(receipt)
            receipt.write_text(json.dumps({"result_sha256": original["result_sha256"]}))
            errors, _ = gallery.check(self.root)
            with self.subTest(case=case):
                self.assertTrue(any(case in error and "execution provenance" in error.lower() for error in errors), errors)
            receipt.write_text(json.dumps(original))

    def test_cse_receipt_requires_timestamp_command_and_helper_inventory(self):
        copied = self.copy_case("flight-management-system")
        receipt = copied / "evidence/analysis/cse-crosscheck.json"
        original = analysis.load_json(receipt)
        for field in ("executed_at", "command", "helper_sources"):
            value = deepcopy(original)
            del value[field]
            receipt.write_text(json.dumps(value))
            with self.subTest(field=field):
                self.assert_error("provenance")

    def test_cse_selected_receipt_requires_identical_archived_bytes(self):
        copied = self.copy_case("flight-management-system")
        receipt = copied / "evidence/analysis/cse-crosscheck.json"
        archive = receipt.parent / "cse-runs" / (analysis.digest(receipt) + ".json")
        original = archive.read_bytes()
        self.assertEqual(gallery.check(self.root)[0], [])
        archive.write_text("{}")
        self.assert_error("CSE receipt archive missing or differs")
        archive.unlink()
        self.assert_error("CSE receipt archive missing or differs")
        archive.write_bytes(original)
        self.assertEqual(gallery.check(self.root)[0], [])

    def test_collector_rejects_static_source_drift_after_import(self):
        copied = self.copy_case("flight-management-system")
        (self.root / "scripts").mkdir()
        shutil.copyfile(ROOT / "scripts/analyze_gallery.py", self.root / "scripts/analyze_gallery.py")
        output = copied / "evidence/analysis/model-results.json"
        before = output.read_bytes()
        code = """from pathlib import Path
import sys
sys.path.insert(0, 'scripts')
import analyze_gallery
p=Path('scripts/analyze_gallery.py')
p.write_text(p.read_text().replace('mass *= p if state[name] else 1 - p', 'mass *= p if state[name] else 2 - p'))
analyze_gallery.main()
"""
        observed = subprocess.run([sys.executable, "-B", "-c", code], cwd=self.root, capture_output=True, text=True)
        self.assertNotEqual(observed.returncode, 0)
        self.assertIn("Source changed after import", observed.stderr)
        self.assertEqual(output.read_bytes(), before)

    def test_parsed_input_change_during_analysis_is_rejected(self):
        copied = self.copy_case("flight-management-system")
        (self.root / "scripts").mkdir()
        shutil.copyfile(ROOT / "scripts/analyze_gallery.py", self.root / "scripts/analyze_gallery.py")
        output = copied / "evidence/analysis/model-results.json"
        before = output.read_bytes()
        code = """from pathlib import Path
import sys,json
sys.path.insert(0, 'scripts')
import analyze_gallery
p=next(Path('examples').glob('*/flight-management-system/analysis/failure-model.json'))
original=analyze_gallery.analyze
def changed(model):
    record=json.loads(p.read_text())
    record['events']['BE1']['probability']='1/2'
    p.write_text(json.dumps(record))
    return original(model)
analyze_gallery.analyze=changed
analyze_gallery.main()
"""
        observed = subprocess.run([sys.executable, "-B", "-c", code], cwd=self.root, capture_output=True, text=True)
        self.assertNotEqual(observed.returncode, 0)
        self.assertIn("Configuration changed during execution", observed.stderr)
        self.assertEqual(output.read_bytes(), before)

    def test_clamp_source_drift_after_import_is_rejected(self):
        copied = self.copy_case("smart-infusion-pump")
        output = copied / "evidence/analysis/clamp-results.json"
        before = output.read_bytes()
        code = """from pathlib import Path
import run_clamp_checks
p=Path('clamp_model.py')
p.write_text(p.read_text().replace('last_service_ms >= 200', 'last_service_ms >= 300'))
run_clamp_checks.main()
"""
        observed = subprocess.run([sys.executable, "-B", "-c", code], cwd=copied / "analysis", capture_output=True, text=True)
        self.assertNotEqual(observed.returncode, 0)
        self.assertIn("Source changed after import", observed.stderr)
        self.assertEqual(output.read_bytes(), before)

    def test_clamp_stale_bytecode_is_rejected_even_with_B_flag(self):
        copied = self.copy_case("smart-infusion-pump")
        source = copied / "analysis/clamp_model.py"
        before = source.stat()
        py_compile.compile(str(source), doraise=True)
        source.write_text(source.read_text().replace('last_service_ms >= 200', 'last_service_ms >= 300'))
        os.utime(source, ns=(before.st_atime_ns, before.st_mtime_ns))
        output = copied / "evidence/analysis/clamp-results.json"
        preserved = output.read_bytes()
        for flags in ([], ["--check"]):
            observed = subprocess.run([sys.executable, "-B", str(copied / "analysis/run_clamp_checks.py"), *flags],
                                      capture_output=True, text=True)
            with self.subTest(flags=flags):
                self.assertNotEqual(observed.returncode, 0)
                self.assertIn("Loaded code differs from source bytes", observed.stderr)
        self.assertEqual(output.read_bytes(), preserved)
        self.assert_error("temporal result check failed")


class TemporalClampTests(unittest.TestCase):
    def test_hold_open_power_loss_does_not_imply_processor_service_loss(self):
        clamp = Clamp(closing_ms=0)
        for time_ms in (100, 200, 300):
            result = clamp.step(time_ms, power=False, cpu_services=True)
            self.assertFalse(result["watchdog"])
            self.assertTrue(result["closed"])

    def test_watchdog_trips_at_boundary_and_closing_delay_is_separate(self):
        clamp = Clamp(closing_ms=300)
        first = clamp.step(100, cpu_services=False)
        second = clamp.step(200, cpu_services=False)
        self.assertFalse(first["watchdog"])
        self.assertTrue(second["watchdog"])
        self.assertEqual(second["release_ms"], 200)
        self.assertFalse(second["closed"])
        for time_ms in (300, 400):
            self.assertFalse(clamp.step(time_ms, cpu_services=False)["closed"])
        self.assertTrue(clamp.step(500, cpu_services=False)["closed"])

    def test_power_recovery_requires_rearm_after_latched_release(self):
        clamp = Clamp(closing_ms=0)
        self.assertTrue(clamp.step(100, power=False)["closed"])
        self.assertTrue(clamp.step(200)["closed"])
        self.assertFalse(clamp.step(300, manual_rearm=True)["closed"])

    def test_jam_and_interlock_fault_preserve_uncovered_failures(self):
        for fault in ("jammed", "interlock_failed"):
            clamp = Clamp()
            for time_ms in range(100, 1001, 100):
                row = clamp.step(time_ms, door_open=True, **{fault: True})
            with self.subTest(fault=fault):
                self.assertFalse(row["closed"])

    def test_unsafe_rearm_and_malformed_inputs_are_rejected(self):
        clamp = Clamp(closing_ms=0)
        self.assertTrue(clamp.step(100, door_open=True, manual_rearm=True)["closed"])
        with self.assertRaises(ValueError):
            clamp.step(300)
        with self.assertRaises(ValueError):
            clamp.step(200, door_open=1)
        with self.assertRaises(ValueError):
            Clamp(closing_ms=250)

    def test_sweep_retains_proposal_and_requirement_failures_separately(self):
        report = run_clamp_checks.execute()
        self.assertEqual(report["test_count"], 28)
        self.assertEqual(report["expected_criterion_failures"], 10)
        self.assertEqual(report["expected_requirement_failures"], 6)
        self.assertTrue(all(row["test_outcome"] == "pass" for row in report["results"]))
        watchdog = next(row for row in report["results"] if row["id"] == "CLAMP-watchdog-400")
        self.assertEqual(watchdog["criterion_outcome"], "fail")
        self.assertEqual(watchdog["requirement_outcome"], "pass")


if __name__ == "__main__":
    unittest.main()
