from pathlib import Path
import sys
import tempfile
import unittest

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
            self.assertEqual({p.name for p in folder.iterdir()}, {"request.md", ".agents"})
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
