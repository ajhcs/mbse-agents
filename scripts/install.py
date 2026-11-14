"""Install, inspect, restore, or remove selected skills without overwriting local work."""
from pathlib import Path
import argparse
import difflib
import hashlib
import json
import re
import shutil
import sys
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
        # Only this package's receipt is metadata. Nested files belong to the user.
        if path.is_file() and path != folder / RECEIPT:
            result[path.relative_to(folder).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def receipt(folder, name):
    try:
        record = json.loads((folder / RECEIPT).read_text(encoding="utf-8"))
        if record["managed_by"] == "mbse-agents" and record["name"] == name and isinstance(record["files"], dict):
            return record
    except (OSError, ValueError, KeyError, TypeError):
        pass
    return None


def owned_unchanged(folder, name):
    record = receipt(folder, name)
    try:
        return record is not None and record["files"] == fingerprints(folder)
    except (OSError, ValueError):
        return False


def contained(path, parent):
    """Check resolved absolute paths before any directory move."""
    if not path.resolve().is_relative_to(parent.resolve()) or path.resolve() == parent.resolve():
        raise ValueError(f"Path escapes destination: {path}")


def destination_path(destination):
    destination = Path(destination).absolute()
    if destination.is_symlink():
        raise ValueError("Refusing a symlinked destination")
    if destination.exists() and not destination.is_dir():
        raise ValueError(f"Skills destination is not a directory: {destination}")
    return destination


def selected_sources(names, root=ROOT):
    selected = {s["name"]: s for s in entries(root)}
    if not names or len(names) != len(set(names)) or any(name not in selected for name in names):
        raise ValueError("Select unique names from --list")
    result = []
    for name in names:
        source = root / selected[name]["path"]
        if metadata(source / "SKILL.md")["name"] != name:
            raise ValueError(f"Invalid package metadata: {name}")
        result.append((name, source))
    return result


def package_fingerprints(source, root=ROOT):
    files = fingerprints(source)
    if "LICENSE" not in files:
        files["LICENSE"] = hashlib.sha256((root / "LICENSE").read_bytes()).hexdigest()
    return files


def copy_package(source, target, *, root=ROOT, expected=None):
    """Copy a standalone package and check exactly the bytes planned for it."""
    expected = package_fingerprints(source, root) if expected is None else expected
    shutil.copytree(source, target)
    if not (target / "LICENSE").exists():
        shutil.copy2(root / "LICENSE", target / "LICENSE")
    if fingerprints(target) != expected:
        raise ValueError(f"Source changed while copying {source.name}; no package was committed")


def valid_skill_name(name):
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError("Choose a skill name, not a filesystem path")


def backup_path(destination, name):
    valid_skill_name(name)
    root = destination.parent / ".mbse-backups"
    parent = root / name
    for path in (root, parent):
        if path.is_symlink():
            raise ValueError(f"Refusing symlinked backup directory: {path}")
    backup = parent / uuid.uuid4().hex
    contained(backup, root)
    return backup


def _commit(plans, destination):
    """Commit staged packages; undo earlier changes if a later move fails."""
    touched = []
    try:
        for plan in plans:
            target, name = plan["target"], plan["name"]
            contained(target, destination)
            if plan["before"] is None:
                if target.exists() or target.is_symlink():
                    raise ValueError(f"A target appeared during installation; preserved: {target}")
            elif not owned_unchanged(target, name) or fingerprints(target) != plan["before"]:
                raise ValueError(f"Target changed during operation; preserved: {target}")
            plan["moved"] = plan["installed"] = False
            touched.append(plan)
            if plan["before"] is not None:
                plan["backup"].parent.mkdir(parents=True, exist_ok=True)
                target.rename(plan["backup"])
                plan["moved"] = True
            if plan["stage"] is not None:
                plan["stage"].rename(target)
                plan["installed"] = True
    except BaseException as error:
        failures = []
        for plan in reversed(touched):
            target = plan["target"]
            try:
                if plan["installed"]:
                    if not owned_unchanged(target, plan["name"]) or fingerprints(target) != plan["after"]:
                        raise ValueError(f"New local changes preserved at {target}")
                    target.rename(plan["stage"])
                if plan["moved"]:
                    if target.exists() or target.is_symlink():
                        raise ValueError(f"Target appeared during rollback; preserved: {target}")
                    plan["backup"].rename(target)
            except (OSError, ValueError) as rollback_error:
                failures.append(f"{rollback_error}; original package: {plan['backup']}")
        if failures:
            raise RuntimeError(f"Operation failed: {error}. Recovery needs attention: " + "; ".join(failures)) from error
        raise RuntimeError(f"Operation failed; prior packages restored: {error}") from error


def install(destination, names, *, update=False, dry_run=False, root=ROOT, report=None):
    destination = destination_path(destination)
    plans = []
    for name, source in selected_sources(names, root):
        files = package_fingerprints(source, root)
        target = destination / name
        contained(target, destination)
        if target.is_symlink():
            raise ValueError(f"Refusing symlinked target: {target}")
        before, action = None, "install"
        if target.exists():
            if not owned_unchanged(target, name):
                raise ValueError(f"Existing unmanaged or modified skill preserved: {target}. Use --inspect or --diff to review it.")
            before = fingerprints(target)
            action = "unchanged" if before == files else "update"
            if action == "update" and not update:
                raise ValueError(f"Managed skill needs --update: {target}")
        plans.append({"name": name, "source": source, "target": target, "before": before,
                      "after": files, "action": action, "backup": backup_path(destination, name) if action == "update" else None})
    result = [(p["name"], p["action"]) for p in plans]
    changes = [p for p in plans if p["action"] != "unchanged"]
    if dry_run or not changes:
        return result
    destination.mkdir(parents=True, exist_ok=True)
    # Finish every copy before replacing any installed package.
    with tempfile.TemporaryDirectory(prefix=".mbse-stage-", dir=destination) as temp:
        for plan in changes:
            stage = Path(temp) / plan["name"]
            copy_package(plan["source"], stage, root=root, expected=plan["after"])
            (stage / RECEIPT).write_text(json.dumps({"managed_by": "mbse-agents", "name": plan["name"], "files": plan["after"]}, indent=2) + "\n", encoding="utf-8")
            plan["stage"] = stage
        _commit(changes, destination)
    if report:
        for plan in changes:
            if plan["backup"] is not None:
                report(f"backup: {plan['backup']}")
    return result


def differences(before, after):
    return {key: "added" if key not in before else "removed" if key not in after else "changed"
            for key in sorted(before.keys() | after.keys()) if before.get(key) != after.get(key)}


def inspect(destination, names, *, root=ROOT, show_diff=False):
    """Read local and incoming changes without changing receipts or files."""
    destination = destination_path(destination)
    result = []
    for name, source in selected_sources(names, root):
        target = destination / name
        contained(target, destination)
        if target.is_symlink():
            raise ValueError(f"Refusing symlinked target: {target}")
        actual = fingerprints(target) if target.exists() else {}
        record = receipt(target, name)
        baseline = record["files"] if record else {}
        incoming = package_fingerprints(source, root)
        state = "missing" if not target.exists() else "unmanaged" if not record else "managed" if baseline == actual else "modified"
        row = {"name": name, "path": str(target), "state": state,
               "local_changes": differences(baseline, actual) if record else {},
               "incoming_changes": differences(baseline, incoming), "diffs": []}
        if show_diff:
            for relative in differences(actual, incoming):
                local = target / relative
                proposed = source / relative
                if relative == "LICENSE" and not proposed.exists():
                    proposed = root / "LICENSE"
                try:
                    old = local.read_text(encoding="utf-8").splitlines(keepends=True) if local.is_file() else []
                    new = proposed.read_text(encoding="utf-8").splitlines(keepends=True) if proposed.is_file() else []
                    row["diffs"].append("".join(difflib.unified_diff(old, new, fromfile=f"local/{relative}", tofile=f"incoming/{relative}")))
                except UnicodeDecodeError:
                    row["diffs"].append(f"Binary content differs: {relative}\n")
        result.append(row)
    return result


def uninstall(destination, names, *, dry_run=False):
    """Move unchanged managed packages into recoverable backups; never delete them."""
    destination = destination_path(destination)
    if not names or len(names) != len(set(names)):
        raise ValueError("Select unique --skill names for removal")
    plans = []
    for name in names:
        valid_skill_name(name)
        target = destination / name
        contained(target, destination)
        if not owned_unchanged(target, name):
            raise ValueError(f"Unmanaged, missing, or modified skill preserved: {target}")
        plans.append({"name": name, "target": target, "before": fingerprints(target), "after": None,
                      "stage": None, "backup": backup_path(destination, name)})
    if not dry_run:
        _commit(plans, destination)
    return [(p["name"], str(p["backup"])) for p in plans]


def restore(destination, name, backup, *, dry_run=False):
    """Restore a verified backup, retaining both the source and any current package."""
    destination = destination_path(destination)
    valid_skill_name(name)
    backup = Path(backup).absolute()
    expected_parent = destination.parent / ".mbse-backups" / name
    contained(backup, expected_parent)
    if backup.parent != expected_parent or not owned_unchanged(backup, name):
        raise ValueError(f"Choose an unchanged managed backup for {name} under {expected_parent}")
    target = destination / name
    contained(target, destination)
    before = None
    if target.exists() or target.is_symlink():
        if not owned_unchanged(target, name):
            raise ValueError(f"Unmanaged or modified skill preserved: {target}")
        before = fingerprints(target)
    files = fingerprints(backup)
    previous = backup_path(destination, name) if before is not None else None
    if before == files:
        return None
    if dry_run:
        return previous
    destination.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".mbse-stage-", dir=destination) as temp:
        stage = Path(temp) / name
        shutil.copytree(backup, stage)
        if not owned_unchanged(stage, name) or fingerprints(stage) != files:
            raise ValueError("Backup changed while copying; installed package preserved")
        _commit([{"name": name, "target": target, "before": before, "after": files,
                  "stage": stage, "backup": previous}], destination)
    return previous


def diagnose(destination, names, *, root=ROOT):
    lines = [f"Python: {sys.version.split()[0]} ({sys.executable})", f"Source: {root}"]
    for name, source in selected_sources(names, root):
        lines.append(f"package ready: {name} ({len(package_fingerprints(source, root))} files including LICENSE)")
    if destination is not None:
        for row in inspect(destination, names, root=root):
            lines.append(f"{row['state']}: {row['path']}")
    lines.append("This checks local package readiness; verify skill discovery in the intended host.")
    return lines


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    targets = parser.add_mutually_exclusive_group()
    targets.add_argument("--project", type=Path, help="Use PROJECT/.agents/skills")
    targets.add_argument("--destination", type=Path, help="Explicit skills directory in another host")
    parser.add_argument("--skill", action="append", help="Select a skill; repeat to select more")
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument("--list", action="store_true")
    actions.add_argument("--diagnose", action="store_true", help="Read package and optional destination readiness")
    actions.add_argument("--inspect", action="store_true", help="Show local and incoming file changes")
    actions.add_argument("--diff", action="store_true", help="Inspect and show local-to-incoming text diffs")
    actions.add_argument("--uninstall", action="store_true", help="Move selected unchanged packages into backups")
    actions.add_argument("--restore", type=Path, metavar="BACKUP", help="Restore one verified backup; requires one --skill")
    actions.add_argument("--update", action="store_true", help="Update unchanged managed packages; retain backups")
    parser.add_argument("--dry-run", action="store_true", help="Plan an install, update, restore, or removal without writing")
    args = parser.parse_args()
    destination = args.destination or (args.project / ".agents" / "skills" if args.project else None)
    try:
        if args.list:
            for s in entries():
                print(f"{s['name']}: {metadata(ROOT / s['path'] / 'SKILL.md')['description']}")
            return
        names = args.skill or [s["name"] for s in entries()]
        if args.diagnose:
            print("\n".join(diagnose(destination, names)))
            return
        if destination is None:
            parser.error("Choose --project or --destination; nothing is installed by default")
        prefix = "would " if args.dry_run else ""
        if args.inspect or args.diff:
            for row in inspect(destination, names, show_diff=args.diff):
                print(f"{row['state']}: {row['path']}")
                if row["state"] == "unmanaged":
                    print("  No trusted managed baseline; local edits cannot be distinguished from the original.")
                for category in ("local_changes", "incoming_changes"):
                    for path, change in row[category].items():
                        print(f"  {category}: {change}: {path}")
                for diff in row["diffs"]:
                    print(diff, end="" if diff.endswith("\n") else "\n")
        elif args.uninstall:
            if not args.skill:
                parser.error("Removal requires explicit --skill selections")
            for name, backup in uninstall(destination, names, dry_run=args.dry_run):
                print(f"{prefix}uninstall: {name}; backup: {backup}")
        elif args.restore:
            if not args.skill or len(args.skill) != 1:
                parser.error("Restore requires exactly one --skill")
            previous = restore(destination, names[0], args.restore, dry_run=args.dry_run)
            print(f"{prefix}restore: {names[0]} from {args.restore}")
            if previous:
                print(f"{prefix}retain current package: {previous}")
        else:
            for name, action in install(destination, names, update=args.update, dry_run=args.dry_run, report=print):
                print(f"{prefix}{action}: {name}")
    except (OSError, ValueError, RuntimeError) as error:
        parser.exit(1, str(error) + "\n")


if __name__ == "__main__":
    main()
