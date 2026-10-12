from pathlib import Path
import json
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from catalog import ROOT, entries, generated, metadata


class CatalogTests(unittest.TestCase):
    def test_manifest_and_ui_cover_the_inventory(self):
        output = generated()
        manifest = json.loads(output["platform/chatgpt/gpt-manifest.json"])
        self.assertEqual({s["name"] for s in manifest["skills"]}, {s["name"] for s in entries()})
        for item in entries():
            self.assertIn(item["path"] + "/agents/openai.yaml", output)

    def test_frontmatter_rejects_duplicate_and_nonstring_fields(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            path = Path(temp) / "SKILL.md"
            for text in ['---\nname: example\nname: duplicate\ndescription: "Task"\n---\n', '---\nname: example\ndescription: []\n---\n', 'No frontmatter']:
                path.write_text(text, encoding="utf-8")
                if 'description: []' in text:
                    # This project's subset rejects YAML structures as scalar descriptions.
                    from catalog import metadata as read
                    with self.assertRaises(ValueError):
                        read(path)
                else:
                    with self.assertRaises(ValueError):
                        metadata(path)
