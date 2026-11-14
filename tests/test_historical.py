"""Exercise provenance and reference failures with disposable local fixtures."""

import csv
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_historical", ROOT / "scripts/check_historical.py")
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class HistoricalGalleryTests(unittest.TestCase):
    def setUp(self):
        # Keep disposable working data on the repository's /workspace volume.
        self.temp = tempfile.TemporaryDirectory(prefix=".historical-test-", dir=ROOT / "tests")
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / "examples/historical", self.root / "examples/historical")
        self.gallery = self.root / "examples/historical"

    def tearDown(self):
        self.temp.cleanup()

    def mutate(self, slug, function):
        path = self.gallery / slug / "analysis.json"
        record = json.loads(path.read_text())
        function(record)
        path.write_text(json.dumps(record))

    def assertError(self, fragment):
        errors = CHECKER.check_gallery(self.root)
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_curated_gallery_has_consistent_attribution_and_assets(self):
        self.assertEqual([], CHECKER.check_gallery(self.root))

    def test_unknown_source_cannot_support_a_fact(self):
        self.mutate("apollo-13", lambda case: case["facts"][0].update(source_ids=["HG-01-S999"]))
        self.assertError("unknown source references")

    def test_proposal_cannot_be_promoted_to_executed_evidence(self):
        self.mutate("apollo-13", lambda case: case["evidence_status"].update(simulation="passed"))
        self.assertError("evidence statuses")

    def test_missing_declared_artifact_is_an_error(self):
        (self.gallery / "hubble-optics/interfaces.csv").unlink()
        self.assertError("missing local artifact")

    def test_synthetic_change_cannot_claim_historical_provenance(self):
        path = self.gallery / "mars-climate-orbiter/change.json"
        record = json.loads(path.read_text())
        record["historical_provenance"] = True
        path.write_text(json.dumps(record))
        self.assertError("deny historical provenance")

    def test_asset_path_cannot_escape_case(self):
        self.mutate("hubble-optics", lambda case: case["exercise_assets"][0].update(path="../README.md"))
        self.assertError("asset escapes case directory")

    def test_project_year_and_source_publication_are_different_fields(self):
        self.mutate("apollo-13", lambda case: case["sources"][0].update(publication_date="2018 official retrospective"))
        self.assertEqual([], CHECKER.check_gallery(self.root))
        self.mutate("apollo-13", lambda case: case.update(year=2015))
        self.assertError("historical year")

    def test_duplicate_teaching_id_is_an_error(self):
        self.mutate("apollo-13", lambda case: case["facts"][1].update(id=case["facts"][0]["id"]))
        self.assertError("duplicate teaching ID")

    def test_evidence_register_cannot_assert_unprovided_execution(self):
        path = self.gallery / "mars-climate-orbiter/claim-evidence.csv"
        with path.open(newline="") as stream:
            rows = list(csv.DictReader(stream))
        rows[-1]["status"] = "passed"
        with path.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        self.assertError("claim status cannot assert unprovided execution")

    def test_change_references_must_resolve(self):
        path = self.gallery / "heathrow-terminal-5/change.json"
        record = json.loads(path.read_text())
        record["affected_interface_ids"] = ["HG-10-I404"]
        path.write_text(json.dumps(record))
        self.assertError("unknown or missing affected_interface_ids")

    def test_view_cannot_invent_a_relation_reference(self):
        path = self.gallery / "hubble-optics/relations.mmd"
        path.write_text(path.read_text().replace("HG-03-I1", "HG-03-I404"))
        self.assertError("unknown teaching reference HG-03-I404")

    def test_generated_fact_register_preserves_source_attribution(self):
        path = self.gallery / "hubble-optics/source-facts.csv"
        path.write_text(path.read_text().replace("HG-03-S1", "HG-03-S404"))
        self.assertError("source-facts.csv disagrees")

    def test_malformed_source_metadata_reports_an_error(self):
        self.mutate("apollo-13", lambda case: case["sources"][0].update(source_type=[]))
        self.assertError("unrecognized source_type")

    def test_missing_fact_references_do_not_crash_connected_review(self):
        self.mutate("hubble-optics", lambda case: case["facts"][0].update(source_ids=None))
        self.assertError("unknown source references")

    def test_malformed_csv_cannot_hide_a_missing_field(self):
        path = self.gallery / "hubble-optics/interfaces.csv"
        path.write_text("id,producer,consumer\nHG-03-I1,fixture\n")
        self.assertError("CSV rows must match the declared columns")


if __name__ == "__main__":
    unittest.main()
