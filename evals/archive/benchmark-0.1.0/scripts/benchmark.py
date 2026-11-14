"""Prepare and assess public systems-engineering judgment exercises; no model API."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone

from catalog import ROOT, entries

BANK = Path("evals/benchmark/items.json")
KEYS = Path("evals/benchmark/keys.json")
SPLITS = ("practice", "development", "evaluation-public")
ARMS = ("none", "task", "task-domain", "catalog")


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_json(path):
    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result
    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=unique_pairs)


def load_bank(root=ROOT):
    bank = read_json(root / BANK)
    keys = read_json(root / KEYS)
    if bank.get("schema_version") != 1 or keys.get("schema_version") != 1:
        raise ValueError("Unsupported benchmark schema")
    if bank.get("version") != keys.get("version") or bank.get("id") != keys.get("benchmark"):
        raise ValueError("Question bank and answer key identities differ")
    dimensions = bank.get("dimensions")
    if not isinstance(dimensions, dict) or not dimensions:
        raise ValueError("A nonempty dimension map is required")
    if not isinstance(bank.get("items"), list) or not bank["items"]:
        raise ValueError("A nonempty question bank is required")
    seen = set()
    source_ids = set(bank.get("sources", {}))
    for item in bank["items"]:
        ident = item.get("id")
        if not isinstance(ident, str) or not ident or ident in seen:
            raise ValueError(f"Missing or duplicate item ID: {ident}")
        seen.add(ident)
        if item.get("dimension") not in dimensions or item.get("split") not in SPLITS:
            raise ValueError(f"Invalid dimension or split: {ident}")
        choices = item.get("choices")
        if not isinstance(choices, dict) or not 3 <= len(choices) <= 6 or not all(
            isinstance(k, str) and k and isinstance(v, str) and v.strip() for k, v in choices.items()
        ):
            raise ValueError(f"Invalid choices: {ident}")
        if item.get("format") not in {"single", "multiple"}:
            raise ValueError(f"Invalid question format: {ident}")
        for field in ("title", "scenario", "question"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                raise ValueError(f"Missing {field}: {ident}")
        if not isinstance(item.get("skills"), list) or not item["skills"]:
            raise ValueError(f"Missing skill selection: {ident}")
        if not isinstance(item.get("source_ids"), list) or any(s not in source_ids for s in item["source_ids"]):
            raise ValueError(f"Unknown source: {ident}")
        key = keys.get("keys", {}).get(ident, {})
        answer = key.get("answer")
        if not isinstance(answer, list) or not answer or len(set(answer)) != len(answer) or not set(answer) <= set(choices):
            raise ValueError(f"Invalid keyed selection: {ident}")
        if item["format"] == "single" and len(answer) != 1:
            raise ValueError(f"Single-choice item has multiple keyed answers: {ident}")
        if not isinstance(key.get("rationale"), str) or not key["rationale"].strip():
            raise ValueError(f"Missing rationale: {ident}")
        criteria = key.get("reasoning_criteria")
        if not isinstance(criteria, list) or not criteria or not all(isinstance(c, str) and c.strip() for c in criteria):
            raise ValueError(f"Missing reasoning criteria: {ident}")
    if seen != set(keys.get("keys", {})):
        raise ValueError("Question and answer-key inventories differ")
    return bank, keys


def select_items(bank, *, split=None, ids=None, dimension=None):
    if ids and len(ids) != len(set(ids)):
        raise ValueError("Select distinct question IDs")
    available = {q["id"] for q in bank["items"]}
    if ids and not set(ids) <= available:
        raise ValueError("Unknown question ID")
    if dimension and dimension not in bank["dimensions"]:
        raise ValueError("Unknown reasoning dimension")
    result = [q for q in bank["items"] if (not split or q["split"] == split)
              and (not ids or q["id"] in ids) and (not dimension or q["dimension"] == dimension)]
    if not result:
        raise ValueError("Selection contains no questions")
    return result


def question_text(item):
    multiple = "Select all supported options." if item["format"] == "multiple" else "Select one option."
    return (f"## {item['id']}: {item['title']}\n\n{item['scenario']}\n\n{item['question']} {multiple}\n\n"
            + "\n".join(f"- {letter}. {text}" for letter, text in item["choices"].items())
            + "\n\nExplain the facts and reasoning that support your selection; identify a consequential limitation if one applies.\n")


def source_revision(root):
    result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else None


def source_dirty(root):
    result = subprocess.run(["git", "status", "--porcelain"], cwd=root, capture_output=True, text=True)
    return bool(result.stdout.strip()) if result.returncode == 0 else None


def write_json(path, data):
    Path(path).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def safe_files(folder):
    folder = Path(folder)
    if folder.is_symlink() or not folder.is_dir():
        raise ValueError(f"Invalid package directory: {folder}")
    files = []
    for path in sorted(folder.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Symlink is not an evaluation input: {path}")
        if path.is_file():
            files.append(path)
    if not (folder / "SKILL.md").is_file():
        raise ValueError(f"Missing skill entrypoint: {folder}")
    return files


def prepare(destination, *, root=ROOT, split=None, ids=None, dimension=None, arm="none"):
    bank, _ = load_bank(root)
    items = select_items(bank, split=split, ids=ids, dimension=dimension)
    if arm not in ARMS:
        raise ValueError("Unknown comparison arm")
    destination = Path(destination).absolute()
    if destination.exists() or destination.is_symlink():
        raise ValueError("Use a fresh packet directory; existing work is preserved")
    inventory = {s["name"]: s for s in entries(root)}
    requested = set().union(*(set(q["skills"]) for q in items))
    if not requested <= set(inventory):
        raise ValueError("Question bank names an unavailable skill")
    selected = (set(inventory) if arm == "catalog" else requested if arm == "task-domain" else
                {s for s in requested if inventory[s]["kind"] == "task"} if arm == "task" else set())
    packages = [(name, root / inventory[name]["path"]) for name in sorted(selected)]
    for _, source in packages:
        safe_files(source)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".mbse-packet-", dir=destination.parent) as temporary:
        stage = Path(temporary) / "packet"
        stage.mkdir()
        request = ("# Systems engineering judgment exercise\n\n"
                   "Answer from the supplied facts. These are engineering reasoning questions, not requests to certify a system. "
                   "Use only this packet and tools permitted by the evaluation controller. Do not look for answer keys or other runs. "
                   "Report unavailable facts honestly. Save answers.json using the response template. "
                   "Select options and provide your own explanation for each item. Record the model/host/settings actually used; do not guess.\n\n"
                   + "\n".join(question_text(item) for item in items))
        (stage / "request.md").write_text(request, encoding="utf-8")
        write_json(stage / "questions.json", {"schema_version": 1, "benchmark": bank["id"], "version": bank["version"], "items": items})
        write_json(stage / "response-template.json", {
            "schema_version": 1,
            "run": {"run_id": None, "producer": None, "model": None, "host": None, "settings": {},
                    "started_at": None, "completed_at": None, "source_access": "packet-only", "tools": [],
                    "tokens": None, "latency_seconds": None, "cost": None, "exceptions": []},
            "answers": [{"id": q["id"], "selection": [], "reasoning": "", "confidence": None} for q in items]
        })
        for name, source in packages:
            shutil.copytree(source, stage / ".agents/skills" / name)
        manifest = {"schema_version": 1, "kind": "se-judgment-input-packet", "status": "complete",
                    "benchmark": bank["id"], "version": bank["version"], "arm": arm,
                    "prepared_at": datetime.now(timezone.utc).isoformat(), "source_revision": source_revision(root),
                    "source_tree_dirty": source_dirty(root),
                    "revision_meaning": "HEAD at preparation; file hashes identify actual inputs, including uncommitted changes.",
                    "bank_sha256": digest(root / BANK), "key_sha256": digest(root / KEYS),
                    "item_ids": [q["id"] for q in items], "skills": sorted(selected),
                    "exposure": "public_items_and_keys; packet_separation_is_not_a_security_boundary",
                    "files": {p.relative_to(stage).as_posix(): digest(p) for p in sorted(stage.rglob("*")) if p.is_file()}}
        write_json(stage / "packet-manifest.json", manifest)
        if destination.exists() or destination.is_symlink():
            raise ValueError("Destination appeared during preparation; existing work is preserved")
        stage.rename(destination)
    return destination


def verify_packet(packet, root=ROOT):
    packet = Path(packet).resolve()
    manifest = read_json(packet / "packet-manifest.json")
    if manifest.get("schema_version") != 1 or manifest.get("kind") != "se-judgment-input-packet" or manifest.get("status") != "complete":
        raise ValueError("Incomplete or unsupported packet")
    if manifest.get("arm") not in ARMS or not isinstance(manifest.get("files"), dict):
        raise ValueError("Invalid packet manifest")
    if manifest.get("bank_sha256") != digest(root / BANK) or manifest.get("key_sha256") != digest(root / KEYS):
        raise ValueError("Bank or key changed; score with the recorded benchmark revision")
    for relative, expected in manifest["files"].items():
        file = (packet / relative).resolve()
        if not file.is_relative_to(packet) or not file.is_file() or digest(file) != expected:
            raise ValueError(f"Packet input changed or missing: {relative}")
    questions = read_json(packet / "questions.json")
    if [q["id"] for q in questions.get("items", [])] != manifest.get("item_ids"):
        raise ValueError("Question inventory differs from packet manifest")
    bank, _ = load_bank(root)
    expected_items = {q["id"]: q for q in bank["items"]}
    if any(expected_items.get(q["id"]) != q for q in questions["items"]):
        raise ValueError("Packet question differs from the recorded bank")
    return manifest, questions["items"]


def score(packet, answers_path, *, root=ROOT, review_path=None):
    manifest, items = verify_packet(packet, root)
    _, keys = load_bank(root)
    answers = read_json(answers_path)
    if answers.get("schema_version") != 1 or not isinstance(answers.get("run"), dict) or not isinstance(answers.get("answers"), list):
        raise ValueError("Unsupported response record")
    run = answers["run"]
    for field in ("run_id", "producer", "model", "host", "started_at", "completed_at"):
        if not isinstance(run.get(field), str) or not run[field].strip():
            raise ValueError(f"Missing run provenance: {field}; use explicit 'unknown' when unavailable")
    if not isinstance(run.get("settings"), dict):
        raise ValueError("Run settings must be an object")
    rows = {}
    questions = {q["id"]: q for q in items}
    for row in answers["answers"]:
        ident = row.get("id")
        if ident not in questions or ident in rows:
            raise ValueError(f"Unknown or duplicate response: {ident}")
        selection = row.get("selection")
        if not isinstance(selection, list) or not all(isinstance(s, str) for s in selection) or len(selection) != len(set(selection)) or not set(selection) <= set(questions[ident]["choices"]):
            raise ValueError(f"Invalid selection: {ident}")
        if questions[ident]["format"] == "single" and len(selection) > 1:
            raise ValueError(f"Multiple selections for a single-choice item: {ident}")
        if not isinstance(row.get("reasoning"), str):
            raise ValueError(f"Missing reasoning field: {ident}")
        confidence = row.get("confidence")
        if confidence is not None and (type(confidence) not in (int, float) or not 0 <= confidence <= 1):
            raise ValueError(f"Confidence must be null or a number in [0,1]: {ident}")
        rows[ident] = row
    outcomes = []
    for item in items:
        row = rows.get(item["id"])
        answered = bool(row and row["selection"])
        correct = bool(answered and set(row["selection"]) == set(keys["keys"][item["id"]]["answer"]))
        outcomes.append({"id": item["id"], "dimension": item["dimension"], "split": item["split"],
                         "answered": answered, "selection_correct": correct,
                         "explanation_supplied": bool(row and row["reasoning"].strip()),
                         "reasoning_assessment": "not_reviewed"})
    counts = {}
    for outcome in outcomes:
        group = counts.setdefault(outcome["dimension"], {"items": 0, "answered": 0, "correct": 0})
        group["items"] += 1
        group["answered"] += outcome["answered"]
        group["correct"] += outcome["selection_correct"]
    result = {"schema_version": 1, "kind": "se-judgment-score", "benchmark": manifest["benchmark"],
              "version": manifest["version"], "bank_sha256": manifest["bank_sha256"], "key_sha256": manifest["key_sha256"],
              "packet_manifest_sha256": digest(Path(packet) / "packet-manifest.json"), "answers_sha256": digest(answers_path),
              "arm": manifest["arm"], "run": run, "items": len(items), "answered": sum(o["answered"] for o in outcomes),
              "selection_correct": sum(o["selection_correct"] for o in outcomes), "by_dimension": counts,
              "selection_accuracy": sum(o["selection_correct"] for o in outcomes) / len(items),
              "macro_dimension_accuracy": sum(v["correct"] / v["items"] for v in counts.values()) / len(counts),
              "uniform_choice_reference": sum(1 / (len(q["choices"]) if q["format"] == "single" else 2 ** len(q["choices"]) - 1) for q in items) / len(items),
              "uniform_choice_definition": "Uniform random selection among single options, or among all nonempty subsets for multiple-choice items; a mathematical reference, not measured guessing behavior.",
              "outcomes": outcomes, "reasoning_review": {"status": "not_reviewed"},
              "interpretation": "Selection accuracy against a proposed curated key; not a measure of explanation quality or overall engineering competence.",
              "release_acceptance": "not_assessed"}
    if review_path:
        review = read_json(review_path)
        if review.get("schema_version") != 1 or review.get("answers_sha256") != result["answers_sha256"]:
            raise ValueError("Review does not identify these answer bytes")
        if not isinstance(review.get("reviewer"), str) or not review["reviewer"].strip() or review["reviewer"] == run["producer"]:
            raise ValueError("Identify a reviewer distinct from the producer")
        if review.get("independent_of_production") is not True:
            raise ValueError("Review must declare its independence from production")
        assessed = review.get("items")
        if not isinstance(assessed, dict) or set(assessed) != set(questions):
            raise ValueError("Review must disposition every selected item")
        for ident, assessment in assessed.items():
            ratings = assessment.get("criteria")
            expected = keys["keys"][ident]["reasoning_criteria"]
            if not isinstance(ratings, list) or len(ratings) != len(expected) or any(type(v) is not int or v not in (0, 1, 2) for v in ratings):
                raise ValueError(f"Rate every reasoning criterion 0, 1 or 2: {ident}")
            if not isinstance(assessment.get("comment"), str) or not assessment["comment"].strip():
                raise ValueError(f"Explain the assessment: {ident}")
            if not isinstance(assessment.get("critical_errors"), list) or not all(isinstance(e, str) and e for e in assessment["critical_errors"]):
                raise ValueError(f"List critical errors explicitly: {ident}")
        for outcome in outcomes:
            outcome["reasoning_assessment"] = "independently_reviewed"
        result["reasoning_review"] = {"status": "reviewer_reported", "sha256": digest(review_path), "review": review,
                                      "interpretation": "Named review of the submitted explanation; rubric/key validity still requires expert adjudication."}
    return result


def report(paths):
    runs = [read_json(path) for path in paths]
    if not runs or any(r.get("schema_version") != 1 or r.get("kind") != "se-judgment-score" for r in runs):
        raise ValueError("Supply one or more benchmark score records")
    identities = {(r["benchmark"], r["version"], r["bank_sha256"], r["key_sha256"], tuple(o["id"] for o in r["outcomes"])) for r in runs}
    if len(identities) != 1:
        raise ValueError("Comparison requires identical benchmark inputs and key revision")
    ids = [r["run"]["run_id"] for r in runs]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate run IDs cannot be counted as repeated trials")
    return {"schema_version": 1, "kind": "se-judgment-comparison", "benchmark": runs[0]["benchmark"],
            "items": runs[0]["items"], "runs": [{"run_id": r["run"]["run_id"], "arm": r["arm"],
            "model": r["run"]["model"], "selection_accuracy": r["selection_accuracy"],
            "reasoning_review": r["reasoning_review"]["status"], "latency_seconds": r["run"].get("latency_seconds"),
            "cost": r["run"].get("cost")} for r in runs],
            "interpretation": "Descriptive results only. Compare like hosts, settings, tools, exposure and independent samples; no automatic superiority or release claim."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("validate")
    listing = commands.add_parser("list")
    listing.add_argument("--split", choices=SPLITS)
    listing.add_argument("--dimension")
    practice = commands.add_parser("practice")
    practice.add_argument("--item", required=True)
    practice.add_argument("--answer", nargs="+")
    practice.add_argument("--reason")
    packet = commands.add_parser("prepare")
    packet.add_argument("--output", type=Path, required=True)
    packet.add_argument("--split", choices=SPLITS)
    packet.add_argument("--item", action="append")
    packet.add_argument("--dimension")
    packet.add_argument("--arm", choices=ARMS, default="none")
    scoring = commands.add_parser("score")
    scoring.add_argument("--packet", type=Path, required=True)
    scoring.add_argument("--answers", type=Path, required=True)
    scoring.add_argument("--review", type=Path)
    scoring.add_argument("--output", type=Path)
    reporting = commands.add_parser("report")
    reporting.add_argument("scores", nargs="+", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "validate":
            bank, _ = load_bank()
            print(f"PASS: {len(bank['items'])} curated items, {len(bank['dimensions'])} reasoning dimensions; answer-key validity and agent quality remain separately assessed")
        elif args.command == "list":
            bank, _ = load_bank()
            for item in select_items(bank, split=args.split, dimension=args.dimension):
                print(f"{item['id']} | {item['split']} | {item['dimension']} | {item['title']}")
        elif args.command == "practice":
            bank, keys = load_bank()
            item = select_items(bank, ids=[args.item])[0]
            if item["split"] != "practice":
                raise ValueError("Interactive feedback is restricted to the practice split; prepare other splits without answers")
            print(question_text(item))
            if args.answer:
                if not args.reason or not args.reason.strip():
                    raise ValueError("Supply --reason before requesting practice feedback")
                if len(args.answer) != len(set(args.answer)) or not set(args.answer) <= set(item["choices"]) or (item["format"] == "single" and len(args.answer) != 1):
                    raise ValueError("Invalid practice selection")
                key = keys["keys"][item["id"]]
                print("Selection matches the proposed key." if set(args.answer) == set(key["answer"]) else "Selection differs from the proposed key.")
                print(key["rationale"])
                print("Your reasoning has not been automatically graded.")
        elif args.command == "prepare":
            print(prepare(args.output, split=args.split, ids=args.item, dimension=args.dimension, arm=args.arm))
        elif args.command == "score":
            result = score(args.packet, args.answers, review_path=args.review)
            if args.output:
                if args.output.exists():
                    raise ValueError("Score output exists; preserve prior assessment and choose a new path")
                args.output.parent.mkdir(parents=True, exist_ok=True)
                write_json(args.output, result)
            print(json.dumps(result, indent=2))
        elif args.command == "report":
            print(json.dumps(report(args.scores), indent=2))
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        parser.exit(1, str(error) + "\n")


if __name__ == "__main__":
    main()
