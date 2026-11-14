#!/usr/bin/env python3
"""Validate historical teaching records and their local evidence references.

This checks structure and attribution, never remote availability, source truth,
model quality, or engineering acceptance. check_gallery(repo_root) returns errors.
"""

from __future__ import annotations

import argparse
import csv
from datetime import date
import json
from pathlib import Path
import re
from urllib.parse import urlparse


SOURCE_TYPES = {
    "original_investigation", "original_project_record", "original_specification",
    "original_project_proposal", "original_program_audit", "original_author_investigation",
    "contemporaneous_official_inquiry_summary", "official_retrospective",
    "official_initiative_summary",
}
EVIDENCE_STATUS = {
    "historical_facts": "attributed_to_identified_sources",
    "analysis": "new_retrospective_teaching_synthesis",
    "artifact": "proposed_not_historical",
    "simulation": "not_performed",
}
EXERCISE_FILES = {
    "review-task.md", "source-facts.csv", "interfaces.csv", "claim-evidence.csv",
    "change.json", "relations.mmd", "review-guide.md",
}


def check_gallery(repo_root: Path) -> list[str]:
    """Return actionable errors for a repository root; do not mutate files."""
    errors: list[str] = []
    gallery = repo_root / "examples/historical"
    seen_ids: set[str] = set()
    records: dict[str, dict] = {}

    def error(where: str, message: str) -> None:
        errors.append(f"{where}: {message}")

    def read_json(path: Path):
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(value, dict):
                raise ValueError("expected an object")
            return value
        except (OSError, ValueError) as exc:
            error(str(path.relative_to(repo_root)), f"invalid JSON: {exc}")
            return None

    def register(identifier, pattern: str, where: str) -> None:
        if not isinstance(identifier, str) or not re.fullmatch(pattern, identifier):
            error(where, f"invalid teaching ID {identifier!r}")
        elif identifier in seen_ids:
            error(where, f"duplicate teaching ID {identifier}")
        else:
            seen_ids.add(identifier)

    def strings(obj: dict, keys: tuple[str, ...], where: str) -> None:
        for key in keys:
            if not isinstance(obj.get(key), str) or not obj[key].strip():
                error(where, f"missing nonempty {key}")

    def local_file(directory: Path, name, where: str) -> Path | None:
        if not isinstance(name, str) or not name:
            error(where, "missing local asset path")
            return None
        relative = Path(name)
        path = directory / relative
        if relative.is_absolute() or ".." in relative.parts or not path.resolve().is_relative_to(directory.resolve()):
            error(where, f"asset escapes case directory: {name}")
            return None
        if not path.is_file():
            error(where, f"missing local artifact: {name}")
            return None
        return path

    def read_csv(path: Path | None) -> list[dict]:
        if path is None:
            return []
        try:
            with path.open(encoding="utf-8", newline="") as stream:
                rows = list(csv.DictReader(stream))
            if not rows:
                error(str(path.relative_to(repo_root)), "empty artifact register")
            if any(any(not isinstance(key, str) or not isinstance(value, str) for key, value in row.items()) for row in rows):
                error(str(path.relative_to(repo_root)), "CSV rows must match the declared columns")
                return []
            return rows
        except (OSError, csv.Error, UnicodeError) as exc:
            error(str(path.relative_to(repo_root)), f"invalid CSV: {exc}")
            return []

    paths = sorted(gallery.glob("*/analysis.json"))
    if not paths:
        error("historical gallery", "no case records")
    for path in paths:
        where = str(path.relative_to(repo_root))
        case = read_json(path)
        if case is None:
            continue
        cid = case.get("id", "")
        register(cid, r"HG-\d{2}", where)
        if case.get("schema_version") != 1:
            error(where, "unsupported schema_version")
        strings(case, ("slug", "title", "domain", "outcome", "focus"), where)
        if case.get("slug") != path.parent.name:
            error(where, "slug does not match directory")
        year = case.get("year")
        if type(year) is not int or not 0 < year < 2015:
            error(where, "historical year must be an integer before 2015")
        if case.get("evidence_status") != EVIDENCE_STATUS:
            error(where, "evidence statuses must distinguish attributed facts, new analysis, proposals, and no local simulation")
        if not isinstance(case.get("competencies"), list) or not case["competencies"]:
            error(where, "missing competencies")
        sources = case.get("sources", [])
        if not isinstance(sources, list) or not sources:
            error(where, "missing sources")
            sources = []
        source_ids = set()
        for source in sources:
            if not isinstance(source, dict):
                error(where, "source must be an object")
                continue
            register(source.get("id"), re.escape(str(cid)) + r"-S\d+", where)
            if isinstance(source.get("id"), str):
                source_ids.add(source["id"])
            strings(source, ("title", "url", "publication_date", "locator", "limitations"), where)
            url = urlparse(source.get("url", "") if isinstance(source.get("url", ""), str) else "")
            if url.scheme != "https" or not url.netloc:
                error(where, "source URL must be an absolute HTTPS publisher/institutional URL")
            if not isinstance(source.get("source_type"), str) or source["source_type"] not in SOURCE_TYPES:
                error(where, "unrecognized source_type")
            if source.get("access_status") != "relevant_content_inspected":
                error(where, "source access must state inspected relevant content")
            try:
                date.fromisoformat(source.get("accessed_on", ""))
            except (ValueError, TypeError):
                error(where, "invalid accessed_on date")
        facts = case.get("facts", [])
        if not isinstance(facts, list) or not facts:
            error(where, "missing attributed facts")
            facts = []
        fact_ids = set()
        for fact in facts:
            if not isinstance(fact, dict):
                error(where, "fact must be an object")
                continue
            register(fact.get("id"), re.escape(str(cid)) + r"-F\d+", where)
            if isinstance(fact.get("id"), str):
                fact_ids.add(fact["id"])
            strings(fact, ("statement", "locator"), where)
            refs = fact.get("source_ids", [])
            if not isinstance(refs, list) or not refs or any(not isinstance(ref, str) or ref not in source_ids for ref in refs):
                error(where, f'fact {fact.get("id")} has missing or unknown source references')
        analysis = case.get("retrospective", {})
        if not isinstance(analysis, dict):
            error(where, "missing retrospective analysis")
            analysis = {}
        strings(analysis, ("boundary", "transfer_exercise", "limits"), where)
        for key in ("interfaces", "questions", "answer_signals"):
            value = analysis.get(key)
            if not isinstance(value, list) or not value or any(not isinstance(item, str) or not item.strip() for item in value):
                error(where, f"missing substantive {key}")
        decision = analysis.get("decision", {})
        if not isinstance(decision, dict):
            decision = {}
        strings(decision, ("question", "recommendation", "uncertainty"), where)
        options = decision.get("options")
        if not isinstance(options, list) or len(options) < 2 or any(not isinstance(item, str) or not item.strip() for item in options):
            error(where, "decision needs at least two explicit alternatives")
        artifact = analysis.get("artifact", {})
        if not isinstance(artifact, dict):
            artifact = {}
        register(artifact.get("id"), re.escape(str(cid)) + r"-A\d+", where)
        strings(artifact, ("type",), where)
        if artifact.get("status") != "new_teaching_proposal":
            error(where, "artifact status must remain new_teaching_proposal")
        columns, rows = artifact.get("columns"), artifact.get("rows")
        if not isinstance(columns, list) or not columns or not isinstance(rows, list) or not rows:
            error(where, "missing concrete artifact table")
        elif any(not isinstance(row, list) or len(row) != len(columns) or any(not isinstance(cell, str) or not cell.strip() for cell in row) for row in rows):
            error(where, "malformed artifact table row")
        local_file(path.parent, "README.md", where)
        assets = case.get("exercise_assets", [])
        if not isinstance(assets, list):
            error(where, "exercise_assets must be a list")
            assets = []
        asset_paths = {}
        for asset in assets:
            if not isinstance(asset, dict):
                error(where, "exercise asset must be an object")
                continue
            strings(asset, ("path", "label", "purpose"), where)
            local = local_file(path.parent, asset.get("path"), where)
            if isinstance(asset.get("path"), str):
                asset_paths[asset["path"]] = local
        if assets:
            if set(asset_paths) != EXERCISE_FILES or len(assets) != len(EXERCISE_FILES):
                error(where, "connected exercise must declare all seven distinct artifact files")
            source_rows = read_csv(asset_paths.get("source-facts.csv"))
            expected = [{"id": fact["id"], "statement": fact["statement"], "source_ids": ";".join(fact["source_ids"]), "locator": fact["locator"], "status": "attributed_historical_finding"} for fact in facts if isinstance(fact, dict) and all(key in fact for key in ("id", "statement", "source_ids", "locator")) and isinstance(fact["source_ids"], list) and all(isinstance(ref, str) for ref in fact["source_ids"])]
            if source_rows != expected:
                error(where, "source-facts.csv disagrees with canonical facts or their attribution")
            interface_ids, claim_ids = set(), set()
            for filename, suffix, collection in (("interfaces.csv", "I", interface_ids), ("claim-evidence.csv", "C", claim_ids)):
                for row in read_csv(asset_paths.get(filename)):
                    register(row.get("id"), re.escape(str(cid)) + rf"-{suffix}\d+", where)
                    if row.get("id"):
                        collection.add(row["id"])
                    refs = [ref for ref in row.get("basis_fact_ids", "").split(";") if ref]
                    if any(ref not in fact_ids for ref in refs):
                        error(where, f"{filename} has unknown basis_fact_ids")
                    if suffix == "I":
                        strings(row, ("producer", "consumer", "meaning"), where)
                        if row.get("status") != "new_retrospective_reconstruction":
                            error(where, "interface must be labeled as a new reconstruction")
                    else:
                        strings(row, ("claim", "evidence_gap", "proposed_next_check"), where)
                        if row.get("status") not in {"source_supported", "unsupported_extension", "proposed_unexecuted"}:
                            error(where, "claim status cannot assert unprovided execution or acceptance")
                        if row.get("status") == "source_supported" and not refs:
                            error(where, "source_supported claim lacks fact references")
            change_path = asset_paths.get("change.json")
            change = read_json(change_path) if change_path else None
            if change:
                register(change.get("id"), re.escape(str(cid)) + r"-CH\d+", where)
                strings(change, ("title", "description", "decision_requested"), where)
                if change.get("status") != "synthetic_transfer_exercise" or change.get("historical_provenance") is not False:
                    error(where, "new change must explicitly deny historical provenance")
                for key, known in (("affected_interface_ids", interface_ids), ("affected_claim_ids", claim_ids)):
                    refs = change.get(key)
                    if not isinstance(refs, list) or not refs or any(not isinstance(ref, str) or ref not in known for ref in refs):
                        error(where, f"change has unknown or missing {key}")
            graph_path = asset_paths.get("relations.mmd")
            if graph_path:
                graph = graph_path.read_text(encoding="utf-8")
                known = interface_ids | claim_ids | ({change.get("id")} if change else set())
                if not graph.startswith("flowchart LR\n") or "-->" not in graph:
                    error(where, "missing directed teaching relation view")
                for reference in re.findall(r"HG-\d{2}-(?:CH|I|C)\d+", graph):
                    if reference not in known:
                        error(where, f"relation view has unknown teaching reference {reference}")
        if isinstance(case.get("slug"), str):
            records[case["slug"]] = case
    catalog = read_json(gallery / "catalog.json")
    if catalog:
        if catalog.get("schema_version") != 1 or catalog.get("teaching_ids") is not True:
            error("catalog.json", "missing schema or teaching-ID declaration")
        entries = catalog.get("cases", [])
        if not isinstance(entries, list):
            error("catalog.json", "cases must be a list")
            entries = []
        slugs = [entry.get("slug") for entry in entries if isinstance(entry, dict) and isinstance(entry.get("slug"), str)]
        if len(slugs) != len(entries) or len(set(slugs)) != len(slugs) or set(slugs) != set(records):
            error("catalog.json", "case index does not match canonical records")
        for entry in entries:
            if not isinstance(entry, dict) or not isinstance(entry.get("slug"), str) or entry["slug"] not in records:
                continue
            case = records[entry["slug"]]
            for key in ("id", "title", "year", "domain", "outcome", "focus", "competencies"):
                if entry.get(key) != case.get(key):
                    error("catalog.json", f'{case["id"]} stale {key}')
            for key, filename in (("path", "README.md"), ("analysis_path", "analysis.json")):
                if entry.get(key) != f'{case["slug"]}/{filename}':
                    error("catalog.json", f'{case["id"]} incorrect {key}')
            if entry.get("source_ids") != [source["id"] for source in case.get("sources", []) if isinstance(source, dict) and "id" in source]:
                error("catalog.json", f'{case["id"]} stale source_ids')
            if entry.get("exercise_paths") != [f'{case["slug"]}/{asset["path"]}' for asset in case.get("exercise_assets", []) if isinstance(asset, dict) and "path" in asset]:
                error("catalog.json", f'{case["id"]} stale exercise_paths')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate without modification (the default).")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = check_gallery(args.root.resolve())
    if errors:
        print("Historical gallery validation failed:\n" + "\n".join(errors))
        return 1
    print("Historical gallery valid: local IDs, provenance, references, and artifact files checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
