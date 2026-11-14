"""Offline packaging, discovery, link, and worked-evidence checks."""
from pathlib import Path
import json
import os
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

from catalog import ROOT, entries, generated, metadata
from check_trace import check


def markdown_sources(root):
    """Inspect maintained sources, excluding generated work and preserved snapshots."""
    for folder, dirs, files in os.walk(root):
        relative = Path(folder).relative_to(root)
        dirs[:] = [name for name in dirs if name not in {
            ".git", "__pycache__", "build", ".cache", "node_modules"
        } and not name.startswith((".venv", ".mbse-"))
            and relative / name not in {
                Path("docs/site"), Path("docs/archive"), Path("docs/superpowers"),
                Path("evals/runs")
            } and not (name == "history" and relative.parts[:1] == ("examples",))]
        for name in files:
            if name.endswith(".md"):
                yield Path(folder) / name


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
    for path in markdown_sources(root):
        relative = path.relative_to(root)
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
        checks = [
            ("reference model", "examples/worked/cold-storage-alarm/run_checks.py", ["--check"]),
            ("revision and reverification", "examples/worked/cold-storage-alarm-revision/compare_revisions.py", ["--check"]),
            ("domain analysis", "scripts/analyze_gallery.py", ["--check"]),
            ("domain gallery", "scripts/check_gallery.py", []),
            ("historical case records", "scripts/check_historical.py", ["--check"]),
            ("historical presentation", "examples/historical/render_gallery.py", ["--check"]),
            ("judgment benchmark", "scripts/benchmark.py", ["validate"]),
            ("source plugin manifests", "scripts/package_plugin.py", ["--source-manifests", "check"]),
        ]
        for label, script, arguments in checks:
            try:
                result = subprocess.run([sys.executable, "-B", str(ROOT / script), *arguments],
                                        cwd=ROOT, capture_output=True, text=True, timeout=120)
                if result.returncode:
                    errors.append(f"{label}: " + (result.stderr or result.stdout).strip())
            except (OSError, subprocess.TimeoutExpired) as error:
                errors.append(f"{label}: {error}")
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print("PASS: skills, source links, worked revisions, gallery models, historical records, benchmark structure, and plugin manifests")
    print("This command does not assess agent judgment, standards conformity, or hardware acceptance.")


if __name__ == "__main__":
    main()
