"""Copy selected skills, preserving local work; no network, dependencies, or host settings."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import tempfile
import uuid

from catalog import ROOT, entries, metadata

RECEIPT = ".mbse-install.json"


def fingerprints(folder):
    result = {}
    if folder.is_symlink():
        raise ValueError(f"Refusing symlinked skill: {folder}")
    for path in sorted(folder.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Refusing symlink: {path}")
        if path.is_file() and path.name != RECEIPT:
            result[path.relative_to(folder).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def owned_unchanged(folder, name):
    try:
        record = json.loads((folder / RECEIPT).read_text(encoding="utf-8"))
        return record["managed_by"] == "mbse-agents" and record["name"] == name and record["files"] == fingerprints(folder)
    except (OSError, ValueError, KeyError, TypeError):
        return False


def contained(path, parent):
    """Check resolved absolute paths before any directory move."""
    if not path.resolve().is_relative_to(parent.resolve()) or path.resolve() == parent.resolve():
        raise ValueError(f"Path escapes destination: {path}")


def install(destination, names, *, update=False, dry_run=False, root=ROOT):
    destination = Path(destination).absolute()
    if destination.is_symlink():
        raise ValueError("Refusing a symlinked destination")
    selected = {s["name"]: s for s in entries(root)}
    if len(names) != len(set(names)) or any(name not in selected for name in names):
        raise ValueError("Select unique names from --list")
    plans = []
    for name in names:
        source = root / selected[name]["path"]
        if metadata(source / "SKILL.md")["name"] != name:
            raise ValueError(f"Invalid package metadata: {name}")
        files = fingerprints(source)
        target = destination / name
        contained(target, destination)
        if target.is_symlink():
            raise ValueError(f"Refusing symlinked target: {target}")
        action = "install"
        if target.exists():
            if not owned_unchanged(target, name):
                raise ValueError(f"Existing unmanaged or modified skill preserved: {target}")
            action = "unchanged" if fingerprints(target) == files else "update"
            if action == "update" and not update:
                raise ValueError(f"Managed skill needs --update: {target}")
        plans.append((name, source, target, files, action))
    # Preflight every selected package before writing any.
    if dry_run:
        return [(p[0], p[4]) for p in plans]
    destination.mkdir(parents=True, exist_ok=True)
    for name, source, target, files, action in plans:
        if action == "unchanged":
            continue
        # The temporary directory is owned by this operation and on the same volume.
        with tempfile.TemporaryDirectory(prefix=".mbse-stage-", dir=destination) as temp:
            stage = Path(temp) / name
            shutil.copytree(source, stage)
            (stage / RECEIPT).write_text(json.dumps({"managed_by": "mbse-agents", "name": name, "files": files}, indent=2) + "\n", encoding="utf-8")
            contained(stage, destination)
            backup = None
            if action == "update":
                if not owned_unchanged(target, name):
                    raise ValueError(f"Target changed during installation: {target}")
                backup = destination.parent / ".mbse-backups" / name / uuid.uuid4().hex
                backup.parent.mkdir(parents=True, exist_ok=True)
                contained(target, destination)
                contained(backup, destination.parent / ".mbse-backups")
                target.rename(backup)
            try:
                stage.rename(target)
            except OSError:
                if backup is not None and not target.exists():
                    backup.rename(target)
                raise
    return [(p[0], p[4]) for p in plans]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    targets = parser.add_mutually_exclusive_group()
    targets.add_argument("--project", type=Path, help="Install into PROJECT/.agents/skills")
    targets.add_argument("--destination", type=Path, help="Explicit skills directory in another host")
    parser.add_argument("--skill", action="append", help="Select a skill; repeat to select more")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--update", action="store_true", help="Update only unchanged, previously managed packages; retain backups")
    args = parser.parse_args()
    if args.list:
        for s in entries():
            print(f"{s['name']}: {metadata(ROOT / s['path'] / 'SKILL.md')['description']}")
        return
    destination = args.destination or (args.project / ".agents" / "skills" if args.project else None)
    if destination is None:
        parser.error("Choose --project or --destination; nothing is installed by default")
    try:
        for name, action in install(destination, args.skill or [s["name"] for s in entries()], update=args.update, dry_run=args.dry_run):
            print(f"{action}: {name}")
    except (OSError, ValueError) as error:
        parser.exit(1, str(error) + "\n")


if __name__ == "__main__":
    main()
