from pathlib import Path
import json
import re
import sys
import tempfile
import unittest
import zipfile
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from catalog import ROOT, entries
from package_plugin import build, source_manifests
import package_plugin


class PluginPackageTests(unittest.TestCase):
    def test_source_host_manifests_use_only_canonical_skills(self):
        for relative, content in source_manifests().items():
            self.assertEqual((ROOT / relative).read_text(encoding="utf-8"), content)
            self.assertEqual(json.loads(content)["skills"], "./.agents/skills/")

    def test_plugin_contains_canonical_skills_manifests_and_licenses(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            folder, archive = build(Path(temp) / "plugin", make_zip=True)
            portable = json.loads((folder / "plugin.json").read_text())
            claude = json.loads((folder / ".claude-plugin/plugin.json").read_text())
            self.assertNotIn("skills", portable)
            self.assertEqual(claude["name"], portable["name"])
            self.assertEqual(claude["skills"], "./skills/")
            self.assertEqual({p.name for p in (folder / "skills").iterdir()}, {s["name"] for s in entries()})
            for item in entries():
                for source in (ROOT / item["path"]).rglob("*"):
                    if source.is_file():
                        copied = folder / "skills" / item["name"] / source.relative_to(ROOT / item["path"])
                        self.assertEqual(copied.read_bytes(), source.read_bytes())
                self.assertEqual((folder / "skills" / item["name"] / "LICENSE").read_bytes(), (ROOT / "LICENSE").read_bytes())
            with zipfile.ZipFile(archive) as zipped:
                self.assertIn("plugin.json", zipped.namelist())
                self.assertIn(".claude-plugin/plugin.json", zipped.namelist())
                self.assertNotIn(".git/config", zipped.namelist())
                self.assertNotIn("evals/rubrics.json", zipped.namelist())

    def test_zip_is_reproducible_and_existing_outputs_are_preserved(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            base = Path(temp)
            first, first_zip = build(base / "first", names=["mbse-requirements"], make_zip=True)
            _, second_zip = build(base / "second", names=["mbse-requirements"], make_zip=True)
            self.assertEqual(first_zip.read_bytes(), second_zip.read_bytes())
            note = first / "local.txt"
            note.write_text("Keep")
            with self.assertRaises(ValueError):
                build(first, names=["mbse-requirements"])
            self.assertEqual(note.read_text(), "Keep")

    def test_archive_created_after_preflight_is_preserved(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            output = Path(temp) / "plugin"
            archive = output.with_name(output.name + ".zip")
            original_archive = package_plugin.archive_package

            def create_concurrent_archive(folder, staged_archive):
                original_archive(folder, staged_archive)
                archive.write_bytes(b"Existing local archive; keep this")

            with patch("package_plugin.archive_package", side_effect=create_concurrent_archive):
                with self.assertRaisesRegex(OSError, "Visible outputs preserved"):
                    build(output, names=["mbse-requirements"], make_zip=True)
            self.assertEqual(archive.read_bytes(), b"Existing local archive; keep this")
            self.assertTrue((output / "plugin.json").is_file())

    def test_zip_publication_failure_preserves_new_local_work(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            output = Path(temp) / "plugin"
            original_publish = package_plugin.publish_file

            def fail_archive(source, destination):
                if source.name == "package.zip":
                    (output / "local.txt").write_text("User work after folder appeared")
                    raise OSError("Simulated ZIP publication failure")
                original_publish(source, destination)

            with patch("package_plugin.publish_file", side_effect=fail_archive):
                with self.assertRaisesRegex(OSError, "Visible outputs preserved"):
                    build(output, names=["mbse-requirements"], make_zip=True)
            self.assertEqual((output / "local.txt").read_text(), "User work after folder appeared")
            self.assertTrue((output / "plugin.json").is_file())
            self.assertFalse(output.with_name(output.name + ".zip").exists())

    def test_output_directory_created_after_preflight_is_preserved(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            output = Path(temp) / "plugin"
            original_publish = package_plugin.publish_directory

            def create_concurrent_directory(source, destination):
                output.mkdir()
                original_publish(source, destination)

            with patch("package_plugin.publish_directory", side_effect=create_concurrent_directory):
                with self.assertRaisesRegex(OSError, "Visible outputs preserved"):
                    build(output, names=["mbse-requirements"])
            self.assertEqual(list(output.iterdir()), [])

    def test_databricks_export_contains_selected_context_and_resolved_links(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            folder, _ = build(Path(temp) / "databricks", names=["mbse-requirements"], target="databricks")
            self.assertEqual({p.name for p in (folder / ".assistant/skills").iterdir()}, {"mbse-requirements"})
            context = (folder / "context.md").read_text()
            self.assertIn("mbse-requirements / references/requirement-contracts.md", context)
            self.assertIn((ROOT / "LICENSE").read_text(), context)
            for target in re.findall(r"\]\(([^\s)]+)\)", context):
                if ":" not in target and not target.startswith("#"):
                    self.assertTrue((folder / target.split("#")[0]).is_file(), target)
            self.assertFalse((folder / "plugin.json").exists())

    def test_dry_run_and_missing_context_selection_do_not_write(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            folder = Path(temp) / "new"
            build(folder, dry_run=True, make_zip=True)
            self.assertFalse(folder.exists())
            self.assertFalse(folder.with_name("new.zip").exists())
            with self.assertRaises(ValueError):
                build(folder, target="databricks")
            self.assertFalse(folder.exists())
