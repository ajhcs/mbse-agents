from pathlib import Path
import sys
import tempfile
import unittest
import json
import hashlib
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from catalog import ROOT, entries
from prepare_eval import prepare


class EvaluationPacketTests(unittest.TestCase):
    def test_negative_routing_case_can_expose_the_full_catalog_without_answers(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            folder = prepare("HO-08", Path(temp) / "packet", expose_catalog=True)
            self.assertEqual({p.name for p in (folder / ".agents/skills").iterdir()}, {s["name"] for s in entries()})
            self.assertFalse(any(p.name in {"rubrics.json", "baseline.json", "results.json"} for p in folder.rglob("*")))

    def test_packet_contains_only_request_and_selected_packages(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            folder = prepare("HO-01", Path(temp) / "packet")
            self.assertTrue((folder / "request.md").is_file())
            skills = {p.name for p in (folder / ".agents/skills").iterdir()}
            self.assertEqual(skills, {"mbse-requirements", "mbse-architecture", "mbse-verification-evidence"})
            self.assertEqual({p.name for p in folder.iterdir()}, {"request.md", ".agents", "packet-manifest.json"})
            self.assertFalse(any(p.name in {"rubrics.json", "baseline.json", "results.json"} for p in folder.rglob("*")))

    def test_existing_packet_and_unknown_case_preserve_work(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            folder = Path(temp) / "packet"
            folder.mkdir()
            note = folder / "local.txt"
            note.write_text("My artifact", encoding="utf-8")
            with self.assertRaises(ValueError):
                prepare("HO-01", folder)
            with self.assertRaises(ValueError):
                prepare("MISSING", Path(temp) / "new")
            self.assertEqual(note.read_text(), "My artifact")
            self.assertFalse((Path(temp) / "new").exists())

    def test_fixture_packet_records_exact_inputs_without_rubrics(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            folder = prepare("HO-13", Path(temp) / "packet")
            manifest = json.loads((folder / "packet-manifest.json").read_text())
            self.assertEqual(manifest["status"], "complete")
            self.assertEqual(len(list((folder / "inputs").iterdir())), 6)
            for relative, expected in manifest["files"].items():
                self.assertEqual(hashlib.sha256((folder / relative).read_bytes()).hexdigest(), expected)
            self.assertFalse((folder / "rubrics.json").exists())
            self.assertEqual((folder / "inputs/source.md").read_bytes(), (ROOT / "evals/fixtures/control-change/source.md").read_bytes())

    def test_copy_failure_does_not_leave_a_complete_looking_packet(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            target = Path(temp) / "packet"
            with patch("prepare_eval.shutil.copytree", side_effect=OSError("copy interrupted")):
                with self.assertRaises(OSError):
                    prepare("HO-01", target)
            self.assertFalse(target.exists())
            self.assertEqual(list(Path(temp).iterdir()), [])

    def test_retired_founder_case_is_preserved_but_not_shipped(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            with self.assertRaisesRegex(ValueError, "retired"):
                prepare("HO-06", Path(temp) / "packet")
        original = json.loads((ROOT / "evals/archive/v1/cases.json").read_text())
        self.assertEqual(next(c for c in original["cases"] if c["id"] == "HO-06")["skills"], ["defense-founder-review"])

    def test_active_case_selection_covers_shipped_skills(self):
        cases = json.loads((ROOT / "evals/cases.json").read_text())["cases"]
        selected = set().union(*(set(c["skills"]) for c in cases if c.get("status", "active") == "active"))
        self.assertEqual(selected, {s["name"] for s in entries()})
