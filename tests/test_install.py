from pathlib import Path
import json
import re
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from install import install, ROOT
from catalog import entries


class InstallTests(unittest.TestCase):
    def test_every_package_can_be_copied_with_its_references(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            destination = Path(temp) / "skills"
            names = [s["name"] for s in entries()]
            install(destination, names)
            for name in names:
                package = destination / name
                for path in package.rglob("*.md"):
                    for target in re.findall(r"\]\(([^\s)]+)\)", path.read_text(encoding="utf-8")):
                        if ":" not in target and not target.startswith("#"):
                            resolved = (path.parent / target.split("#")[0]).resolve()
                            self.assertTrue(resolved.is_relative_to(package.resolve()), target)
                            self.assertTrue(resolved.is_file(), target)

    def test_selected_package_is_portable_and_does_not_touch_instructions(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            project = Path(temp)
            instructions = project / "AGENTS.md"
            instructions.write_text("Local instructions", encoding="utf-8")
            destination = project / ".agents/skills"
            install(destination, ["mbse-requirements"])
            package = destination / "mbse-requirements"
            self.assertTrue((package / "references/requirement-contracts.md").is_file())
            self.assertTrue((package / "agents/openai.yaml").is_file())
            self.assertEqual(instructions.read_text(), "Local instructions")
            self.assertEqual(install(destination, ["mbse-requirements"]), [("mbse-requirements", "unchanged")])

    def test_collision_preflights_entire_selection(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            destination = Path(temp) / "skills"
            existing = destination / "mbse-architecture"
            existing.mkdir(parents=True)
            (existing / "notes.md").write_text("My work")
            with self.assertRaises(ValueError):
                install(destination, ["mbse-requirements", "mbse-architecture"])
            self.assertFalse((destination / "mbse-requirements").exists())
            self.assertEqual((existing / "notes.md").read_text(), "My work")

    def test_local_edits_are_preserved_even_with_update(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            destination = Path(temp) / "skills"
            install(destination, ["mbse-requirements"])
            path = destination / "mbse-requirements/SKILL.md"
            path.write_text("Local change", encoding="utf-8")
            with self.assertRaises(ValueError):
                install(destination, ["mbse-requirements"], update=True)
            self.assertEqual(path.read_text(), "Local change")

    def test_managed_update_retains_recoverable_old_package(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            base = Path(temp)
            source = base / "source"
            skill = source / ".agents/skills/example"
            skill.mkdir(parents=True)
            source.joinpath("catalog.json").write_text(json.dumps({"skills": [{"name": "example", "path": ".agents/skills/example"}]}))
            skill.joinpath("SKILL.md").write_text('---\nname: example\ndescription: "An example task"\n---\nOld\n')
            destination = base / "project/skills"
            install(destination, ["example"], root=source)
            old = (destination / "example/SKILL.md").read_bytes()
            skill.joinpath("SKILL.md").write_text('---\nname: example\ndescription: "An example task"\n---\nNew\n')
            with self.assertRaises(ValueError):
                install(destination, ["example"], root=source)
            install(destination, ["example"], update=True, root=source)
            backups = list((destination.parent / ".mbse-backups/example").glob("*/SKILL.md"))
            self.assertEqual(len(backups), 1)
            self.assertEqual(backups[0].read_bytes(), old)
            self.assertIn("New", (destination / "example/SKILL.md").read_text())

    def test_dry_run_and_invalid_selection_do_not_write(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            destination = Path(temp) / "new"
            install(destination, ["mbse-conops"], dry_run=True)
            self.assertFalse(destination.exists())
            for names in [["../outside"], ["mbse-conops", "mbse-conops"]]:
                with self.assertRaises(ValueError):
                    install(destination, names)
            self.assertFalse(destination.exists())
