from pathlib import Path
import html
import importlib.util
import json
import re
import sys
import tempfile
import unittest
from unittest import mock
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from catalog import ROOT
from documentation import (References, Rewrite, Document, architecture_graph,
                           architecture_svg, build_outputs, document_id, local_target, stale_outputs)

MARKDOWN_AVAILABLE = importlib.util.find_spec("markdown") is not None


class DiagramTests(unittest.TestCase):
    def test_actual_source_retains_operator_and_all_interfaces(self):
        source = ROOT / "examples/worked/cold-storage-alarm/architecture.md"
        graph = architecture_graph(source.read_text())
        self.assertEqual(len(graph["nodes"]), 5)
        self.assertTrue(any("Technician" in label for label in graph["nodes"].values()))
        self.assertEqual({edge["label"].split()[0] for edge in graph["edges"]},
                         {"IFC-01", "IFC-02", "IFC-03", "IFC-04"})
        svg = ET.fromstring(architecture_svg(graph))
        rendered = {(element.attrib["data-from"], element.attrib["data-to"], element.attrib["data-interface"])
                    for element in svg.iter() if "data-interface" in element.attrib}
        self.assertEqual(rendered, {(e["from"], e["to"], e["label"].split()[0]) for e in graph["edges"]})

    def test_unsupported_and_undefined_edges_do_not_disappear(self):
        for diagram in ("flowchart LR\n A[Sensor] --> B[Evaluator]", "flowchart LR\n A -->|IFC-01 data| B[Evaluator]"):
            with self.subTest(diagram=diagram), self.assertRaises(ValueError):
                architecture_graph("```mermaid\n" + diagram + "\n```")

    def test_cycles_are_not_misrendered_as_layers(self):
        graph = architecture_graph("```mermaid\nflowchart LR\n A[One] -->|IFC-01 data| B[Two]\n B -->|IFC-02 data| A\n```")
        with self.assertRaisesRegex(ValueError, "cycle"):
            architecture_svg(graph)

    def test_direct_relations_do_not_cross_unrelated_intermediate_nodes(self):
        source = '''```mermaid
flowchart LR
 G["HG-03 reference geometry"]
 P["HG-03 primary measurement"]
 X["HG-03 auxiliary measurement"]
 A["HG-03 acceptance review"]
 G -->|HG-03-I1 reference dependence| P
 G -->|HG-03-I3 assembly evidence| A
 P -->|HG-03-C3 acceptance claim| A
 X -->|HG-03-I2 conflicting evidence| A
```'''
        sources = {"synthetic_four_node_regression": source}
        for path in sorted((ROOT / "examples/historical").glob("*/relations.mmd")):
            sources[path.parent.name] = "```mermaid\n" + path.read_text() + "\n```"
        for name, source in sources.items():
            with self.subTest(source=name):
                svg = ET.fromstring(architecture_svg(architecture_graph(source)))
                bounds = {}
                for group in svg.iter():
                    if "data-node" in group.attrib:
                        rectangle = next(element for element in group if element.tag.endswith("rect"))
                        bounds[group.attrib["data-node"]] = tuple(float(rectangle.attrib[key]) for key in ("x", "y", "width", "height"))
                for group in svg.iter():
                    if "data-interface" not in group.attrib:
                        continue
                    path = next(element for element in group if element.tag.endswith("path"))
                    points = [(float(x), float(y)) for x, y in re.findall(r"[ML]([\d.]+),([\d.]+)", path.attrib["d"])]
                    for node, (x, y, width, height) in bounds.items():
                        if node in {group.attrib["data-from"], group.attrib["data-to"]}:
                            continue
                        for (x1, y1), (x2, y2) in zip(points, points[1:]):
                            horizontal = y1 == y2 and y < y1 < y + height and max(x1, x2) > x and min(x1, x2) < x + width
                            vertical = x1 == x2 and x < x1 < x + width and max(y1, y2) > y and min(y1, y2) < y + height
                            self.assertFalse(horizontal or vertical, f'{group.attrib["data-interface"]} crosses unrelated node {node}')

    def test_inline_svg_reference_ids_are_namespaced(self):
        document = Document("README.md", ROOT / "README.md", "Example", "", set())
        rewriter = Rewrite(ROOT, document, {})
        rewriter.feed('<svg aria-labelledby="title"><title id="title">Example</title><marker id="arrow"/><path marker-end="url(#arrow)"/></svg>')
        output = "".join(rewriter.output)
        self.assertIn(f'aria-labelledby="{document.id}--title"', output)
        self.assertIn(f'marker-end="url(#{document.id}--arrow)"', output)


@unittest.skipUnless(MARKDOWN_AVAILABLE, "optional docs dependency: requirements-docs.txt")
class PreviewTests(unittest.TestCase):
    def fixture(self, root):
        (root / "docs").mkdir()
        (root / "catalog.json").write_text('{"schema_version": 1, "skills": []}\n')
        (root / "README.md").write_text("# Overview\n\n## Shared heading\n\n[Detail](docs/details.md#shared-heading)\n")
        (root / "docs/details.md").write_text("# Detail\n\n## Shared heading\n\n[Overview](../README.md#shared-heading)\n")

    def test_complete_bundle_preserves_cross_document_fragments(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            root = Path(temp)
            self.fixture(root)
            output = build_outputs(root)
            page = output["docs/site/index.html"].decode()
            for name in ("README.md", "docs/details.md"):
                anchor = document_id(name) + "--shared-heading"
                self.assertIn(f'id="{anchor}"', page)
                self.assertIn(f'href="#{anchor}"', page)
            parsed = References()
            parsed.feed(page)
            self.assertFalse([link for link in parsed.links if link.startswith("#") and link[1:] not in parsed.ids])
            self.assertNotIn('href="docs/details.md', page)

    def test_links_pull_in_references_and_raw_data(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            root = Path(temp)
            self.fixture(root)
            (root / "data").mkdir()
            (root / "data/result.json").write_text('{"status": "planned"}')
            with (root / "docs/details.md").open("a") as stream:
                stream.write("\n[Record](../data/result.json)\n")
            page = build_outputs(root)["docs/site/index.html"].decode()
            self.assertIn('data-document="data/result.json"', page)
            self.assertIn("&quot;planned&quot;", page)

    def test_reviewer_keys_and_archives_are_not_bundled(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            root = Path(temp)
            self.fixture(root)
            (root / "evals/benchmark").mkdir(parents=True)
            (root / "evals/benchmark/keys.json").write_text('{"answer":"WITHHELD-ANSWER-SENTINEL"}')
            (root / "docs/archive").mkdir()
            (root / "docs/archive/old.md").write_text("# OLD-PLAN-SENTINEL\n")
            (root / "docs/evidence").mkdir()
            receipts = ("documentation-qualification.json", "repository-qualification.json")
            for name in receipts:
                (root / "docs/evidence" / name).write_text('{"status":"QUALIFICATION-PENDING"}')
            with (root / "README.md").open("a") as stream:
                stream.write("\n[Reviewer key](evals/benchmark/keys.json)\n[Archive](docs/archive/old.md)\n")
                for name in receipts:
                    stream.write(f"\n[Qualification receipt](docs/evidence/{name})\n")
            output = build_outputs(root)
            for data in output.values():
                self.assertNotIn(b"WITHHELD-ANSWER-SENTINEL", data)
                self.assertNotIn(b"OLD-PLAN-SENTINEL", data)
                self.assertNotIn(b"QUALIFICATION-PENDING", data)
            manifest = json.loads(output["docs/site/build-manifest.json"])
            self.assertNotIn("evals/benchmark/keys.json", manifest["sources"])
            for name in receipts:
                self.assertNotIn("docs/evidence/" + name, manifest["sources"])
                (root / "docs/evidence" / name).write_text('{"status":"recorded after generation"}')
            self.assertEqual(output, build_outputs(root), "Qualification receipts must not create a generation hash cycle")

    def test_preserved_inputs_are_excluded_without_hiding_outputs_or_canonical_skills(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            root = Path(temp)
            self.fixture(root)
            canonical = ".agents/skills/current/SKILL.md"
            files = {
                canonical: "# Current canonical skill\n",
                "evals/evidence/run/arm/.agents/skills/current/SKILL.md": "# OLD-HIDDEN-INPUT\n",
                "evals/evidence/run/arm/skills/current/SKILL.md": "# OLD-PORTABLE-INPUT\n",
                "evals/evidence/run/preparation-v1/case/README.md": "# OLD-PREPARATION\n",
                "evals/evidence/run/rubrics-snapshot.json": '{"criterion":"HIDDEN-RUBRIC"}',
                "evals/evidence/run/reviewer-key-snapshot.md": "# HIDDEN-REVIEWER-KEY\n",
                "evals/evidence/run/review-guide-snapshot.md": "# HIDDEN-GUIDE-SNAPSHOT\n",
                "evals/evidence/run/outputs/output.md": "# Observed response\n\n[Outcome](outcome.md)\n",
                "evals/evidence/run/outputs/outcome.md": "# Observed outcome\n\nAn actual failure remains recorded.\n",
                "evals/evidence/run/outputs/rubric-review.md": "# Actual assessment\n",
                "docs/evidence/reviews/assessment.md.txt": "# Retained raw assessment  \n[Original unresolved reference](absent.md)\t\n",
            }
            for name, content in files.items():
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content)
            (root / "catalog.json").write_text(json.dumps({"skills": [{"path": ".agents/skills/current"}]}))
            with (root / "README.md").open("a") as stream:
                for index, name in enumerate(files):
                    stream.write(f"\n[Source {index}]({name})\n")
            outputs = build_outputs(root)
            page = outputs["docs/site/index.html"].decode()
            for sentinel in ("OLD-HIDDEN-INPUT", "OLD-PORTABLE-INPUT", "OLD-PREPARATION",
                             "HIDDEN-RUBRIC", "HIDDEN-REVIEWER-KEY", "HIDDEN-GUIDE-SNAPSHOT"):
                self.assertNotIn(sentinel, page)
            for name in (canonical, "evals/evidence/run/outputs/output.md", "evals/evidence/run/outputs/outcome.md",
                         "evals/evidence/run/outputs/rubric-review.md", "docs/evidence/reviews/assessment.md.txt"):
                self.assertIn(f'data-document="{name}"', page)
            self.assertIn(f'href="#{document_id("evals/evidence/run/outputs/outcome.md")}"', page)
            raw = files["docs/evidence/reviews/assessment.md.txt"]
            encoded = "# Retained raw assessment&#32;&#32;\n[Original unresolved reference](absent.md)&#9;\n"
            self.assertIn(encoded, page)
            self.assertEqual(html.unescape(encoded), raw)
            self.assertNotRegex(page, r"[ \t]+\n")
            manifest = json.loads(outputs["docs/site/build-manifest.json"])
            self.assertNotIn("evals/evidence/run/rubrics-snapshot.json", manifest["sources"])
            self.assertIn(canonical, manifest["sources"])

    def test_missing_and_escaping_links_fail_the_build(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            root = Path(temp)
            self.fixture(root)
            with self.assertRaisesRegex(ValueError, "leaves repository"):
                local_target(root, root / "README.md", "../../private.md")
            (root / "README.md").write_text("# Missing\n[Missing](missing.md)\n")
            with self.assertRaisesRegex(ValueError, "missing linked file"):
                build_outputs(root)

    def test_unknown_heading_fails_instead_of_dropping_fragment(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            root = Path(temp)
            self.fixture(root)
            (root / "README.md").write_text("# Overview\n[Detail](docs/details.md#not-present)\n")
            with self.assertRaisesRegex(ValueError, "unresolved heading"):
                build_outputs(root)

    def test_determinism_and_freshness_cover_source_and_output_changes(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            root = Path(temp)
            self.fixture(root)
            output = build_outputs(root)
            self.assertEqual(output, build_outputs(root))
            for name, data in output.items():
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
            self.assertEqual(stale_outputs(output, root), [])
            (root / "docs/site/index.html").write_text("altered output")
            self.assertIn("docs/site/index.html", stale_outputs(output, root))
            with (root / "docs/details.md").open("a") as stream:
                stream.write("\nChanged source.\n")
            self.assertIn("docs/preview.html", stale_outputs(build_outputs(root), root))
            (root / "docs/site/obsolete.html").write_text("old generated document")
            self.assertIn("unexpected docs/site/obsolete.html", stale_outputs(output, root))

    def test_selected_print_and_explicit_packet_print_remain_separate(self):
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            root = Path(temp)
            self.fixture(root)
            page = build_outputs(root)["docs/site/index.html"].decode()
            self.assertIn('id="print-selected"', page)
            self.assertIn('id="print-all"', page)
            self.assertIn("body.print-all article[hidden]", page)
            self.assertIn("addEventListener('afterprint'", page)

    def test_source_changes_during_render_do_not_receive_a_fresh_manifest(self):
        import markdown
        original_render = markdown.markdown
        with tempfile.TemporaryDirectory(prefix=".mbse-test-", dir=ROOT) as temp:
            root = Path(temp)
            self.fixture(root)
            def change_during_render(text, **kwargs):
                rendered = original_render(text, **kwargs)
                if text.startswith("# Overview"):
                    (root / "README.md").write_text(text + "\nConcurrent source edit.\n")
                return rendered
            with mock.patch("markdown.markdown", side_effect=change_during_render):
                with self.assertRaisesRegex(ValueError, "source changed during build"):
                    build_outputs(root)


if __name__ == "__main__":
    unittest.main()
