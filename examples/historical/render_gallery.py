#!/usr/bin/env python3
"""Render the historical gallery from authored case records, without network use."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def table_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def case_markdown(case: dict, directory: Path) -> str:
    sources = {source["id"]: source for source in case["sources"]}
    analysis = case["retrospective"]
    decision = analysis["decision"]
    artifact = analysis["artifact"]
    lines = [
        f'# {case["title"]}',
        "",
        f'**{case["id"]} · {case["year"]} · {case["domain"].replace("_", " ")} · '
        f'{case["outcome"].replace("_", " ")}**',
        "",
        case["focus"],
        "",
        "All `HG-` identifiers are new teaching identifiers. Historical facts below",
        "are attributed to sources; the boundary, decisions, artifact, questions, and",
        "transfer exercise are newly authored. No local historical simulation was performed.",
        "",
        "## Source-grounded facts",
        "",
    ]
    for fact in case["facts"]:
        citations = ", ".join(
            f'[{sid}]({sources[sid]["url"]})' for sid in fact["source_ids"]
        )
        lines.append(f'- **{fact["id"]}:** {fact["statement"]} {citations}; {fact["locator"]}.')
    lines += [
        "",
        "## Retrospective systems analysis",
        "",
        f'**Boundary.** {analysis["boundary"]}',
        "",
        "**Interfaces to examine**",
        "",
        *[f"- {interface}" for interface in analysis["interfaces"]],
        "",
        f'**Decision.** {decision["question"]}',
        "",
        *[f"- {option}" for option in decision["options"]],
        "",
        f'**Teaching recommendation.** {decision["recommendation"]}',
        "",
        f'**Uncertainty.** {decision["uncertainty"]}',
        "",
        f'## {artifact["id"]}: {artifact["type"]}',
        "",
        "This proposed artifact is a compact starting point for review. Its evidence",
        "requests are unexecuted; its rows are not recovered project requirements.",
        "",
        "| " + " | ".join(artifact["columns"]) + " |",
        "| " + " | ".join("---" for _ in artifact["columns"]) + " |",
    ]
    lines += ["| " + " | ".join(table_cell(cell) for cell in row) + " |" for row in artifact["rows"]]
    if case.get("exercise_assets"):
        lines += ["", "## Connected review exercise", ""]
        lines += [f'- [{asset["label"]}]({asset["path"]}) — {asset["purpose"]}' for asset in case["exercise_assets"]]
        for asset in case["exercise_assets"]:
            if asset["path"].endswith(".mmd"):
                lines += ["", "New teaching relation view; arrows show information dependencies.", "", "```mermaid", (directory / asset["path"]).read_text(encoding="utf-8").rstrip(), "```"]
    lines += ["", "## Practice engineering judgment", ""]
    lines += [f"{i}. {question}" for i, question in enumerate(analysis["questions"], 1)]
    lines += ["", "**Reasoning signals for a formative review**", ""]
    lines += [f"- {signal}" for signal in analysis["answer_signals"]]
    lines += ["", f'**Transfer exercise.** {analysis["transfer_exercise"]}', "", f'**Limits.** {analysis["limits"]}', "", "## Sources and access", ""]
    for source in case["sources"]:
        lines += [
            f'- **{source["id"]}: [{source["title"]}]({source["url"]})**',
            f'  — {source["publication_date"]}; {source["source_type"].replace("_", " ")}.',
            f'  Locator: {source["locator"]}.',
            f'  Relevant content inspected {source["accessed_on"]}. {source["limitations"]}',
        ]
    lines += ["", "[Structured case record](analysis.json) · [Gallery](../README.md) · [Source register](../../../docs/sources-historical.md)", ""]
    return "\n".join(lines)


def expected_files(repo_root: Path) -> dict[Path, str]:
    gallery = repo_root / "examples/historical"
    cases = sorted(
        (json.loads(path.read_text(encoding="utf-8")) for path in gallery.glob("*/analysis.json")),
        key=lambda case: case["id"],
    )
    if not cases:
        raise ValueError("No historical case records found")
    files = {gallery / case["slug"] / "README.md": case_markdown(case, gallery / case["slug"]) for case in cases}
    index = {
        "schema_version": 1,
        "title": "Historical systems engineering gallery",
        "scope": "Historical events and design baselines before 2015; source publication may be later.",
        "teaching_ids": True,
        "cases": [
            {**{key: case[key] for key in ("id", "slug", "title", "year", "domain", "outcome", "focus", "competencies")},
             "path": f'{case["slug"]}/README.md',
             "analysis_path": f'{case["slug"]}/analysis.json',
             "source_ids": [source["id"] for source in case["sources"]],
             "exercise_paths": [f'{case["slug"]}/{asset["path"]}' for asset in case.get("exercise_assets", [])]}
            for case in cases
        ],
    }
    files[gallery / "catalog.json"] = json.dumps(index, indent=2, ensure_ascii=False) + "\n"
    domains = len({case["domain"] for case in cases})
    lines = [
        "# Historical systems engineering gallery", "",
        f"{len(cases)} cases across {domains} domains, centered on events and design baselines before 2015.", "",
        "Study a system's purpose, boundaries, interfaces, alternatives, evidence,",
        "lifecycle, and organizational decisions. The collection includes successful",
        "delivery and recovery, early design baselines, and failures. It is a curated",
        "teaching collection, not a representative sample for estimating failure rates.", "",
        "Every case includes source-attributed facts, a new retrospective analysis,",
        "a proposed artifact, reasoning questions, and a clearly synthetic transfer exercise.",
        "All `HG-` IDs are teaching IDs, never original project identifiers. Source",
        "inspection is not independent verification of the historical investigation,",
        "and proposed tests are not executed evidence.", "",
        "| ID | Case | Year | Domain | Focus |", "| --- | --- | --- | --- | --- |",
    ]
    for case in cases:
        lines.append(f'| {case["id"]} | [{table_cell(case["title"])}]({case["slug"]}/README.md) | {case["year"]} | {case["domain"].replace("_", " ")} | {table_cell(case["focus"])} |')
    lines += [
        "", "## Follow a decision across domains", "",
        "- **Evidence independence:** Hubble, Boston ceiling, San Bruno. What claim does each record actually support?",
        "- **Interfaces and shared causes:** Mars Climate Orbiter, Ariane 501, United 232, TCP. Where does one team's assurance stop?",
        "- **Operational readiness:** Heathrow Terminal 5, Herald of Free Enterprise, London 2012. What must work together at the transition?",
        "- **Information and authority:** Challenger, Columbia, Northeast blackout, Therac-25. Which observation reaches which decision-maker?",
        "- **Mission value and adaptation:** Apollo 13, Mars Exploration Rovers, DNS, the Web proposal. What changes when objectives or context change?",
        "- **Lifecycle learning:** Texas City, infusion pumps, San Bruno. How does a weak field signal become an owned change?",
        "", "## Connected review tasks", "",
        "Some cases add editable interface and evidence registers, a hypothetical change,",
        "and a relation view. Start from the review task and make a disposition using",
        "the connected files. Historical records establish context; the change requests",
        "are deliberately new teaching scenarios.", "",
    ]
    for case in cases:
        if case.get("exercise_assets"):
            lines.append(f'- [{case["title"]}]({case["slug"]}/review-task.md)')
    lines += [
        "", "## Reproduce and extend", "",
        "The canonical records are each case's `analysis.json`. The [catalog](catalog.json)",
        "indexes them for the documentation site. [Authoring and use guidance](../../docs/historical-gallery.md)",
        "describes the evidence boundaries; the [source register](../../docs/sources-historical.md)",
        "records inspected URLs, publication dates, locators, and source-specific limits.", "",
        "```bash", "python3 examples/historical/render_gallery.py --write",
        "python3 examples/historical/render_gallery.py --check",
        "python3 scripts/check_historical.py --check", "```", "",
        "These local checks validate structure, references, and generated-file freshness.",
        "They do not measure agent quality or validate historical engineering models.", "",
        "[All examples](../README.md) · [Evaluation guidance](../../docs/evaluation.md)", "",
    ]
    files[gallery / "README.md"] = "\n".join(lines)
    lines = [
        "# Historical source register", "",
        "Generated from `examples/historical/*/analysis.json`. Each entry records the",
        "specific source and relevant content inspected during curation. Access status",
        "`relevant_content_inspected` means the cited sections were available and read;",
        "it does not assert that every page was inspected, preserve a remote snapshot,",
        "or promise future link availability. URLs are public publisher or institutional",
        "copies. No complete third-party reports are redistributed.", "",
        "The historical year describes the project event or design baseline. Source",
        "publication dates may be later, and an official retrospective is identified",
        "separately from an original record. Publication does not make every witness",
        "statement, estimate, or counterfactual a settled fact. The case fact register",
        "states the narrow claims used for teaching.", "",
        "Locators use printed page numbers when specified, otherwise named sections",
        "or paragraphs. PDF viewer page indices may differ. `HG-` identifiers are new",
        "teaching IDs; original report identifiers appear in source titles where known.", "",
    ]
    for case in cases:
        lines += [f'## {case["id"]}: {case["title"]}', "", f'Historical year: **{case["year"]}**. [Case](../examples/historical/{case["slug"]}/README.md).', ""]
        for source in case["sources"]:
            lines += [
                f'**{source["id"]} — [{source["title"]}]({source["url"]})**', "",
                f'- Publication: {source["publication_date"]}.',
                f'- Type: {source["source_type"].replace("_", " ")}.',
                f'- Locator: {source["locator"]}.',
                f'- Access: `{source["access_status"]}`, {source["accessed_on"]}.',
                f'- Limits: {source["limitations"]}', "",
            ]
    lines += [
        "## Reuse and maintenance", "",
        "Paraphrases are compact; no long excerpts or publisher illustrations are",
        "copied. The authored analyses, artifacts, and hypothetical variants are new",
        "teaching material. They are not original requirements, approved changes,",
        "calibrated models, or evidence that a counterfactual intervention would succeed.", "",
        "When a link changes, preserve its source identity and locator, record the new",
        "access observation, and review the affected claims before replacing the URL.",
        "Do not silently substitute a secondary narrative for an unavailable original.", "",
    ]
    files[repo_root / "docs/sources-historical.md"] = "\n".join(lines)
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        files = expected_files(root)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"Cannot render historical gallery: {error}\n")
    stale = []
    for path, text in files.items():
        if args.write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        elif not path.is_file() or path.read_text(encoding="utf-8") != text:
            stale.append(str(path.relative_to(root)))
    if stale:
        print("Historical generated files are stale:\n" + "\n".join(stale))
        return 1
    print(f'Historical gallery: {len(files)} generated files {"written" if args.write else "current"}.')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
