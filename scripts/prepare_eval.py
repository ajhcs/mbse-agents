"""Prepare isolated task inputs without reviewer criteria or worked answers."""
from pathlib import Path
import argparse
import json
import shutil

from catalog import ROOT, entries


def prepare(case_id, destination, root=ROOT, *, expose_catalog=False):
    cases = json.loads((root / "evals/cases.json").read_text(encoding="utf-8"))["cases"]
    case = next((c for c in cases if c["id"] == case_id), None)
    if case is None:
        raise ValueError("Unknown case")
    destination = Path(destination)
    if destination.exists():
        raise ValueError("Use a fresh output directory; existing work is preserved")
    inventory = {s["name"]: s for s in entries(root)}
    names = list(inventory) if expose_catalog else case["skills"]
    sources = [root / inventory[name]["path"] for name in names]
    destination.mkdir(parents=True)
    (destination / "request.md").write_text(case["request"] + "\n", encoding="utf-8", newline="\n")
    for source in sources:
        shutil.copytree(source, destination / ".agents/skills" / source.name)
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--catalog", action="store_true", help="Expose every package for discovery/routing assessment")
    args = parser.parse_args()
    try:
        print(prepare(args.case, args.output, expose_catalog=args.catalog))
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, str(error) + "\n")


if __name__ == "__main__":
    main()
