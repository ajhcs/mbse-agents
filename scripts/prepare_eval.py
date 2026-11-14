"""Prepare isolated task inputs without reviewer criteria or worked answers."""
from pathlib import Path
import argparse
import json
import shutil
import hashlib
import tempfile
from datetime import datetime, timezone

from catalog import ROOT, entries


def prepare(case_id, destination, root=ROOT, *, expose_catalog=False, arm="task-domain"):
    cases = json.loads((root / "evals/cases.json").read_text(encoding="utf-8"))["cases"]
    case = next((c for c in cases if c["id"] == case_id), None)
    if case is None:
        raise ValueError("Unknown case")
    if case.get("status", "active") != "active":
        raise ValueError("Case is retired; historical inputs are preserved under evals/archive")
    destination = Path(destination).absolute()
    if destination.exists() or destination.is_symlink():
        raise ValueError("Use a fresh output directory; existing work is preserved")
    inventory = {s["name"]: s for s in entries(root)}
    if arm not in {"none", "task", "task-domain", "catalog"}:
        raise ValueError("Unknown comparison arm")
    if expose_catalog:
        arm = "catalog"
    names = (list(inventory) if arm == "catalog" else case["skills"] if arm == "task-domain" else
             [name for name in case["skills"] if inventory[name]["kind"] == "task"] if arm == "task" else [])
    sources = [root / inventory[name]["path"] for name in names]
    inputs = case.get("inputs", {})
    for source in sources:
        if source.is_symlink() or not (source / "SKILL.md").is_file() or any(p.is_symlink() for p in source.rglob("*")):
            raise ValueError(f"Missing or symlinked package: {source}")
    for relative, source in inputs.items():
        target = Path(relative)
        source = root / source
        if target.is_absolute() or ".." in target.parts or not target.parts or target.parts[0] != "inputs":
            raise ValueError(f"Input must be inside inputs/: {relative}")
        if not source.resolve().is_relative_to(root.resolve()) or source.is_symlink() or not source.is_file():
            raise ValueError(f"Missing or escaping raw input: {source}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".mbse-eval-stage-", dir=destination.parent) as temporary:
        stage = Path(temporary) / "packet"
        stage.mkdir()
        (stage / "request.md").write_text(case["request"] + "\n", encoding="utf-8", newline="\n")
        for source in sources:
            shutil.copytree(source, stage / ".agents/skills" / source.name)
        for relative, source in inputs.items():
            target = stage / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / source, target)
        manifest = {"schema_version": 1, "kind": "artifact-performance-packet", "status": "complete",
                    "case": case_id, "case_version": case.get("version", "1.0"),
                    "prepared_at": datetime.now(timezone.utc).isoformat(), "skills": names,
                    "arm": arm, "full_catalog_exposed": arm == "catalog",
                    "case_bank_sha256": hashlib.sha256((root / "evals/cases.json").read_bytes()).hexdigest(),
                    "files": {p.relative_to(stage).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                              for p in sorted(stage.rglob("*")) if p.is_file()},
                    "exposure": "Public inputs; packet separation is not a secure held-out environment."}
        (stage / "packet-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        if destination.exists() or destination.is_symlink():
            raise ValueError("Destination appeared during preparation; existing work is preserved")
        stage.rename(destination)
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True)
    parser.add_argument("--output", required=True, type=Path)
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--catalog", action="store_true", help="Expose every package for discovery/routing assessment")
    selection.add_argument("--arm", choices=["none", "task", "task-domain", "catalog"], default="task-domain")
    args = parser.parse_args()
    try:
        print(prepare(args.case, args.output, expose_catalog=args.catalog, arm=args.arm))
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, str(error) + "\n")


if __name__ == "__main__":
    main()
