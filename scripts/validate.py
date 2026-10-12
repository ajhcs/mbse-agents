"""Offline packaging, discovery, link, and worked-evidence checks."""
from pathlib import Path
import json
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

from catalog import ROOT, entries, generated, metadata
from check_trace import check


def validate(root=ROOT):
    errors = []
    names = set()
    paths = set()
    try:
        for skill in entries(root):
            name = skill["name"]
            if name in names:
                errors.append(f"Duplicate catalog name: {name}")
            names.add(name)
            expected = f".agents/skills/{name}"
            if skill["path"] != expected or len(name) > 64:
                errors.append(f"Invalid canonical path/name: {name}")
                continue
            paths.add(expected)
            meta = metadata(root / expected / "SKILL.md")
            if name != meta["name"] or skill["kind"] not in {"task", "domain", "strategy"}:
                errors.append(f"Invalid inventory record: {name}")
            if not 25 <= len(skill["short_description"]) <= 64 or f"${name}" not in skill["default_prompt"]:
                errors.append(f"Invalid UI metadata: {name}")
        actual = {p.parent.relative_to(root).as_posix() for p in (root / ".agents/skills").glob("*/SKILL.md")}
        if paths != actual:
            errors.append("Catalog and discoverable package inventory differ")
        for relative, content in generated(root).items():
            file = root / relative
            if not file.exists() or file.read_text(encoding="utf-8") != content:
                errors.append(f"Stale generated file: {relative}")
    except (OSError, KeyError, TypeError, ValueError) as error:
        errors.append(f"Invalid package inventory: {error}")
    for path in root.rglob("*.md"):
        relative = path.relative_to(root)
        if ".git" in relative.parts or relative.parts[:2] == ("docs", "superpowers"):
            continue  # Explicitly marked historical planning records.
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^\s)]+)\)", text):
            target = target.strip("<>")
            if urlsplit(target).scheme or target.startswith("#"):
                continue
            file = (path.parent / unquote(target.split("#")[0])).resolve()
            if not file.is_relative_to(root.resolve()) or not file.exists():
                errors.append(f"Broken/escaping local link: {relative} -> {target}")
    baseline = root / "examples/worked/cold-storage-alarm/baseline.json"
    try:
        trace_errors, _ = check(json.loads(baseline.read_text(encoding="utf-8")), baseline.parent)
        errors.extend(trace_errors)
    except (OSError, ValueError, TypeError) as error:
        errors.append(f"Worked example: {error}")
    return errors


def main():
    errors = validate()
    if not errors:
        result = subprocess.run([sys.executable, str(ROOT / "examples/worked/cold-storage-alarm/run_checks.py"), "--check"], capture_output=True, text=True)
        if result.returncode:
            errors.append(result.stderr or result.stdout)
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print("PASS: packaging, discovery, local links, trace/configuration, and six reference-model procedures")
    print("No comparative Sol/Astra evaluation or hardware acceptance was performed.")


if __name__ == "__main__":
    main()
