from pathlib import Path
import json
import re
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from install import install, inspect, uninstall, restore, fingerprints, ROOT
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
            self.assertEqual((package / "LICENSE").read_bytes(), (ROOT / "LICENSE").read_bytes())
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
            source.joinpath("LICENSE").write_bytes((ROOT / "LICENSE").read_bytes())
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

    def make_source(self, base, names=("first", "second")):
        source = base / "source"
        source.mkdir()
        source.joinpath("LICENSE").write_bytes((ROOT / "LICENSE").read_bytes())
        source.joinpath("catalog.json").write_text(json.dumps({"skills": [
            {"name": name, "path": f".agents/skills/{name}"} for name in names
        ]}))
        for name in names:
            skill = source / ".agents/skills" / name
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text(f'---\nname: {name}\ndescription: "A fixture task"\n---\nOld\n')
        return source

    def test_nested_receipt_named_file_is_a_local_edit(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            destination = Path(temp) / "skills"
            install(destination, ["mbse-requirements"])
            note = destination / "mbse-requirements/references/.mbse-install.json"
            note.write_text("Local work")
            with self.assertRaises(ValueError):
                install(destination, ["mbse-requirements"], update=True)
            self.assertEqual(note.read_text(), "Local work")

    def test_staged_content_must_match_preflight(self):
        import shutil
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            base = Path(temp)
            source = self.make_source(base, ("first",))
            destination = base / "skills"
            original_copy = shutil.copytree

            def changing_copy(src, dst, *args, **kwargs):
                result = original_copy(src, dst, *args, **kwargs)
                (Path(dst) / "SKILL.md").write_text("Changed during copy")
                return result

            with patch("install.shutil.copytree", side_effect=changing_copy):
                with self.assertRaisesRegex(ValueError, "Source changed"):
                    install(destination, ["first"], root=source)
            self.assertFalse((destination / "first").exists())

    def test_late_commit_failure_restores_all_selected_packages(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            base = Path(temp)
            source = self.make_source(base)
            destination = base / "skills"
            names = ["first", "second"]
            install(destination, names, root=source)
            old = {name: fingerprints(destination / name) for name in names}
            for name in names:
                path = source / ".agents/skills" / name / "SKILL.md"
                path.write_text(path.read_text().replace("Old", "New"))
            original_rename = Path.rename

            def fail_second_stage(path, target):
                if path.name == "second" and path.parent.name.startswith(".mbse-stage-"):
                    raise OSError("Simulated second commit failure")
                return original_rename(path, target)

            with patch.object(Path, "rename", fail_second_stage):
                with self.assertRaisesRegex(RuntimeError, "prior packages restored"):
                    install(destination, names, root=source, update=True)
            for name in names:
                self.assertEqual(fingerprints(destination / name), old[name])

    def test_inspection_separates_local_and_incoming_changes_without_writes(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            base = Path(temp)
            source = self.make_source(base, ("first",))
            destination = base / "skills"
            install(destination, ["first"], root=source)
            (destination / "first/notes.md").write_text("My local notes\n")
            upstream = source / ".agents/skills/first/SKILL.md"
            upstream.write_text(upstream.read_text().replace("Old", "New"))
            before = fingerprints(destination / "first")
            row = inspect(destination, ["first"], root=source, show_diff=True)[0]
            self.assertEqual(row["state"], "modified")
            self.assertEqual(row["local_changes"], {"notes.md": "added"})
            self.assertEqual(row["incoming_changes"], {"SKILL.md": "changed"})
            self.assertTrue(any("+New" in diff for diff in row["diffs"]))
            self.assertEqual(fingerprints(destination / "first"), before)

    def test_uninstall_and_restore_preserve_backups_and_dry_runs(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            destination = Path(temp) / "skills"
            name = "mbse-requirements"
            install(destination, [name])
            old = fingerprints(destination / name)
            uninstall(destination, [name], dry_run=True)
            self.assertTrue((destination / name).is_dir())
            self.assertFalse((destination.parent / ".mbse-backups").exists())
            backup = Path(uninstall(destination, [name])[0][1])
            self.assertFalse((destination / name).exists())
            self.assertEqual(fingerprints(backup), old)
            restore(destination, name, backup, dry_run=True)
            self.assertFalse((destination / name).exists())
            restore(destination, name, backup)
            self.assertEqual(fingerprints(destination / name), old)
            self.assertEqual(fingerprints(backup), old)
            (destination / name / "notes.md").write_text("Local change")
            with self.assertRaises(ValueError):
                uninstall(destination, [name])
            with self.assertRaises(ValueError):
                restore(destination, name, backup)
            (backup / "SKILL.md").write_text("Modified backup")
            with self.assertRaisesRegex(ValueError, "unchanged managed backup"):
                restore(destination, name, backup, dry_run=True)
            with self.assertRaisesRegex(ValueError, "skill name"):
                restore(destination, "../outside", backup, dry_run=True)

    def test_restore_retains_current_package(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            base = Path(temp)
            source = self.make_source(base, ("first",))
            destination = base / "skills"
            install(destination, ["first"], root=source)
            old = fingerprints(destination / "first")
            upstream = source / ".agents/skills/first/SKILL.md"
            upstream.write_text(upstream.read_text().replace("Old", "New"))
            install(destination, ["first"], root=source, update=True)
            current = fingerprints(destination / "first")
            backup = next((base / ".mbse-backups/first").iterdir())
            previous = restore(destination, "first", backup)
            self.assertEqual(fingerprints(destination / "first"), old)
            self.assertEqual(fingerprints(previous), current)
            self.assertEqual(fingerprints(backup), old)
