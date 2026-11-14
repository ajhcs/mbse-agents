from pathlib import Path
import copy
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from benchmark import load_bank, prepare, score, report, digest, write_json, verify_packet, review_template, diagnostics, write_new_json


class JudgmentBenchmarkTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT)
        self.folder = Path(self.temporary.name)
        self.bank, self.keys = load_bank()

    def tearDown(self):
        self.temporary.cleanup()

    def responses(self, packet, *, run_id="fixture-run"):
        questions = json.loads((packet / "questions.json").read_text())["items"]
        answers = json.loads((packet / "response-template.json").read_text())
        answers.update({"run": {"run_id": run_id, "producer": "fixture-producer",
            "model": "synthetic-test-data", "host": "unittest", "settings": {},
            "started_at": "2026-01-01T00:00:00Z", "completed_at": "2026-01-01T00:00:01Z"},
            "answers": [{"id": q["id"], "selection": self.keys["keys"][q["id"]]["answer"],
                         "reasoning": "Synthetic fixture; not an agent explanation or quality result.", "confidence": None} for q in questions]})
        file = self.folder / f"{run_id}.json"
        write_json(file, answers)
        return file, answers

    def test_bank_has_distinct_dimensions_sources_and_nonempty_splits(self):
        for split in ("practice", "development", "evaluation-public"):
            self.assertEqual({q["dimension"] for q in self.bank["items"] if q["split"] == split}, set(self.bank["dimensions"]))
        self.assertTrue(all(s["year"] < 2015 for s in self.bank["sources"].values()))
        self.assertGreater(len({q["scenario"] for q in self.bank["items"]}), 40)

    def test_packet_excludes_keys_and_preserves_selected_inputs(self):
        packet = prepare(self.folder / "packet", ids=["SEJ-001", "SEJ-017"], arm="task-domain")
        manifest, items = verify_packet(packet)
        self.assertEqual([q["id"] for q in items], ["SEJ-001", "SEJ-017"])
        self.assertTrue(manifest["skills"])
        self.assertFalse(any(p.name in {"keys.json", "rubrics.json", "results.json"} for p in packet.rglob("*")))
        self.assertEqual(manifest["status"], "complete")
        for relative, expected in manifest["files"].items():
            self.assertEqual(digest(packet / relative), expected)

    def test_comparison_arms_expose_only_their_selected_packages(self):
        packets = {arm: prepare(self.folder / arm, ids=["SEJ-025"], arm=arm) for arm in ("none", "task", "task-domain", "catalog")}
        manifests = {arm: verify_packet(packet)[0] for arm, packet in packets.items()}
        self.assertEqual(manifests["none"]["skills"], [])
        self.assertNotIn("mbse-automotive", manifests["task"]["skills"])
        self.assertIn("mbse-automotive", manifests["task-domain"]["skills"])
        self.assertGreater(len(manifests["catalog"]["skills"]), len(manifests["task-domain"]["skills"]))
        self.assertEqual((packets["none"] / "questions.json").read_bytes(), (packets["task-domain"] / "questions.json").read_bytes())

    def test_scoring_missing_and_incorrect_answers_does_not_credit_reasoning(self):
        packet = prepare(self.folder / "packet", ids=["SEJ-001", "SEJ-002", "SEJ-017"])
        path, answers = self.responses(packet)
        answers["answers"].pop(1)
        multiple = answers["answers"][-1]
        multiple["selection"] = [self.keys["keys"]["SEJ-017"]["answer"][0]]
        write_json(path, answers)
        result = score(packet, path)
        self.assertEqual(result["items"], 3)
        self.assertEqual(result["answered"], 2)
        self.assertEqual(result["selection_correct"], 1)
        self.assertEqual(result["reasoning_review"]["status"], "not_reviewed")
        self.assertEqual(result["release_acceptance"], "not_assessed")
        self.assertAlmostEqual(result["uniform_choice_reference"], (0.25 + 0.25 + 1 / 15) / 3)

    def test_invalid_duplicate_and_unknown_answers_are_rejected(self):
        packet = prepare(self.folder / "packet", ids=["SEJ-001"])
        path, original = self.responses(packet)
        for mutation in ("duplicate", "unknown", "invalid-option", "no-provenance", "invalid-confidence"):
            answers = copy.deepcopy(original)
            if mutation == "duplicate": answers["answers"].append(answers["answers"][0])
            elif mutation == "unknown": answers["answers"][0]["id"] = "SEJ-999"
            elif mutation == "invalid-option": answers["answers"][0]["selection"] = ["Z"]
            elif mutation == "no-provenance": answers["run"]["model"] = None
            else: answers["answers"][0]["confidence"] = True
            write_json(path, answers)
            with self.assertRaises(ValueError, msg=mutation): score(packet, path)

    def test_changed_packet_or_changed_key_cannot_be_scored(self):
        packet = prepare(self.folder / "packet", ids=["SEJ-001"])
        path, _ = self.responses(packet)
        request = packet / "request.md"
        request.write_text(request.read_text() + "\nChanged input\n")
        with self.assertRaisesRegex(ValueError, "input changed"):
            score(packet, path)
        packet2 = prepare(self.folder / "packet2", ids=["SEJ-001"])
        manifest_path = packet2 / "packet-manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["key_sha256"] = "0" * 64
        write_json(manifest_path, manifest)
        with self.assertRaisesRegex(ValueError, "Bank or key changed"):
            score(packet2, path)

    def test_independent_review_is_bound_to_answer_bytes_and_every_criterion(self):
        packet = prepare(self.folder / "packet", ids=["SEJ-001"])
        path, answers = self.responses(packet)
        review = review_template(packet, path)
        review.update({"reviewer": "fixture-reviewer", "independent_of_production": True,
                       "items": {"SEJ-001": {"criteria": [2, 1],
                       "comment": "Synthetic assessment fixture; no agent quality claim.", "critical_errors": []}}})
        review_path = self.folder / "review.json"
        write_json(review_path, review)
        result = score(packet, path, review_path=review_path)
        self.assertEqual(result["reasoning_review"]["status"], "reviewer_reported")
        review["reviewer"] = answers["run"]["producer"]
        write_json(review_path, review)
        with self.assertRaisesRegex(ValueError, "distinct"):
            score(packet, path, review_path=review_path)
        review["reviewer"] = "fixture-reviewer"
        review["items"]["SEJ-001"]["criteria"] = [2]
        write_json(review_path, review)
        with self.assertRaisesRegex(ValueError, "every reasoning criterion"):
            score(packet, path, review_path=review_path)

    def test_comparison_refuses_different_questions_and_duplicate_trials(self):
        packet = prepare(self.folder / "packet", ids=["SEJ-001"])
        answers, _ = self.responses(packet)
        result = score(packet, answers)
        path = self.folder / "score.json"
        write_json(path, result)
        self.assertEqual(report([path])["items"], 1)
        with self.assertRaisesRegex(ValueError, "Duplicate run"):
            report([path, path])
        other_packet = prepare(self.folder / "other-packet", ids=["SEJ-002"])
        other_answers, _ = self.responses(other_packet, run_id="other-run")
        changed = score(other_packet, other_answers)
        second = self.folder / "other-score.json"
        write_json(second, changed)
        with self.assertRaisesRegex(ValueError, "identical benchmark"):
            report([path, second])

    def test_failed_preparation_and_existing_destination_preserve_work(self):
        packet = self.folder / "packet"
        with patch("benchmark.shutil.copytree", side_effect=OSError("interrupted")):
            with self.assertRaises(OSError): prepare(packet, ids=["SEJ-001"], arm="task")
        self.assertFalse(packet.exists())
        packet.mkdir()
        note = packet / "note.txt"
        note.write_text("Local work")
        with self.assertRaises(ValueError): prepare(packet, ids=["SEJ-001"])
        self.assertEqual(note.read_text(), "Local work")

    def test_duplicate_json_keys_are_rejected(self):
        packet = prepare(self.folder / "packet", ids=["SEJ-001"])
        path = self.folder / "answers.json"
        path.write_text('{"schema_version":1,"schema_version":1}')
        with self.assertRaisesRegex(ValueError, "Duplicate JSON"):
            score(packet, path)

    def test_nonfinite_numbers_including_exponent_overflow_are_rejected(self):
        packet = prepare(self.folder / "packet", ids=["SEJ-001"])
        path, answers = self.responses(packet)
        for number in ("NaN", "Infinity", "-Infinity", "1e999", "-1e999"):
            invalid = json.dumps(answers).replace('"settings": {}', '"settings": {"overflow": ' + number + '}')
            path.write_text(invalid)
            with self.assertRaisesRegex(ValueError, "Nonfinite JSON", msg=number):
                score(packet, path)

    def test_response_cannot_silently_acquire_another_packet_or_arm(self):
        first = prepare(self.folder / "none", ids=["SEJ-001"], arm="none")
        other = prepare(self.folder / "task", ids=["SEJ-001"], arm="task")
        repeated = prepare(self.folder / "repeated", ids=["SEJ-001"], arm="none")
        path, _ = self.responses(first)
        for packet in (other, repeated):
            with self.assertRaisesRegex(ValueError, "not bound to this packet"):
                score(packet, path)

    def test_review_binding_rejects_changed_packet_key_and_criteria(self):
        packet = prepare(self.folder / "packet", ids=["SEJ-001"])
        path, _ = self.responses(packet)
        original = review_template(packet, path)
        original.update({"reviewer": "fixture-reviewer", "independent_of_production": True})
        original["items"]["SEJ-001"] = {"criteria": [2, 1], "comment": "Synthetic review only.", "critical_errors": []}
        review_path = self.folder / "review.json"
        for field in ("answers_sha256", "packet_manifest_sha256", "key_sha256", "criteria_sha256"):
            changed = copy.deepcopy(original)
            changed[field] = "0" * 64
            write_json(review_path, changed)
            with self.assertRaises(ValueError, msg=field):
                score(packet, path, review_path=review_path)

    def test_manifest_requires_complete_inputs_and_matching_exposure(self):
        for mutation in ("omitted-request", "false-arm", "extra-package-file", "unlisted-package"):
            packet = prepare(self.folder / mutation, ids=["SEJ-001"], arm="task" if mutation == "extra-package-file" else "none")
            manifest_path = packet / "packet-manifest.json"
            manifest = json.loads(manifest_path.read_text())
            if mutation == "omitted-request":
                del manifest["files"]["request.md"]
                (packet / "request.md").write_text("Changed question without a manifest hash")
            elif mutation == "false-arm": manifest["arm"] = "catalog"
            elif mutation == "extra-package-file":
                next((packet / ".agents/skills").iterdir()).joinpath("unlisted.md").write_text("Additional input")
            else:
                (packet / ".agents/skills/unlisted").mkdir(parents=True)
                (packet / ".agents/skills/unlisted/SKILL.md").write_text("Additional skill")
            write_json(manifest_path, manifest)
            with self.assertRaises(ValueError, msg=mutation): verify_packet(packet)

    def test_report_recomputes_item_and_dimension_aggregates(self):
        packet = prepare(self.folder / "packet", ids=["SEJ-001", "SEJ-017"])
        answers, _ = self.responses(packet)
        original = score(packet, answers)
        output = self.folder / "score.json"
        for mutation in ("accuracy", "count", "dimension", "outcome", "chance", "review"):
            changed = copy.deepcopy(original)
            if mutation == "accuracy": changed["selection_accuracy"] = 7.0
            elif mutation == "count": changed["answered"] = 99
            elif mutation == "dimension": changed["by_dimension"][next(iter(changed["by_dimension"]))]["correct"] = 99
            elif mutation == "outcome": changed["outcomes"][0]["selection_correct"] = False
            elif mutation == "chance": changed["uniform_choice_reference"] = 0.5
            else: changed["outcomes"][0]["reasoning_assessment"] = "independently_reviewed"
            write_json(output, changed)
            with self.assertRaises(ValueError, msg=mutation): report([output])

    def test_new_output_refuses_dangling_symlink_without_creating_target(self):
        target = self.folder / "missing-target.json"
        output = self.folder / "symlink.json"
        output.symlink_to(target)
        with self.assertRaisesRegex(ValueError, "Output exists"):
            write_new_json(output, {"result": "synthetic"})
        self.assertFalse(target.exists())
        self.assertTrue(output.is_symlink())

    def test_diagnostic_reports_measured_shortcuts_and_explicit_ties(self):
        bank = {"id": "fixture", "version": "test", "items": [
            {"id": "one", "split": "practice", "format": "single", "choices": {"A": "a", "B": "longer option", "C": "two words"}},
            {"id": "two", "split": "development", "format": "single", "choices": {"A": "cat", "B": "dog", "C": "a long phrase"}},
            {"id": "multi", "split": "practice", "format": "multiple", "choices": {"A": "a", "B": "b", "C": "c"}}]}
        keys = {"keys": {"one": {"answer": ["B"]}, "two": {"answer": ["B"]}, "multi": {"answer": ["A", "B"]}}}
        result = diagnostics(bank, keys)
        group = result["groups"]["all"]
        self.assertEqual(group["single_items"], 2)
        self.assertEqual(group["key_positions"], {"B": 2})
        self.assertEqual(group["shortcuts"]["longest_characters"]["accuracy"], 0.5)
        self.assertEqual(group["shortcuts"]["shortest_characters"]["accuracy"], 0)
        self.assertEqual(group["shortcuts"]["shortest_characters"]["ties"], 1)
        self.assertEqual(group["shortcuts"]["shortest_characters"]["key_among_ties"], 1)
        self.assertEqual(result["items"][1]["shortcuts"]["shortest_characters"]["selected"], "A")
        self.assertAlmostEqual(group["uniform_choice_reference"], 1 / 3)

    def test_diagnose_cli_can_read_preserved_bank_without_modifying_it(self):
        archived = ROOT / "evals/archive/benchmark-0.1.0"
        bank_path = archived / "evals/benchmark/items.json"
        keys_path = archived / "evals/benchmark/keys.json"
        before = (digest(bank_path), digest(keys_path))
        result = subprocess.run([sys.executable, str(ROOT / "scripts/benchmark.py"), "diagnose",
                                 "--bank", str(bank_path), "--keys", str(keys_path)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        diagnostic = json.loads(result.stdout)
        self.assertEqual(diagnostic["version"], "0.1.0")
        self.assertEqual(diagnostic["groups"]["all"]["single_items"], 55)
        self.assertEqual((digest(bank_path), digest(keys_path)), before)


if __name__ == "__main__":
    unittest.main()
