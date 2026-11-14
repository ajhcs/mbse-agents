"""Build a local plugin or selected Databricks context export from canonical skills."""
from pathlib import Path
import argparse
import json
import os
import re
import shutil
import tempfile
import zipfile

from catalog import ROOT, entries
from install import copy_package, package_fingerprints, selected_sources

SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
PORTABLE_FIELDS = {"$schema", "name", "version", "description", "author", "homepage",
                   "repository", "license", "keywords", "extensions"}
CLAUDE_FIELDS = PORTABLE_FIELDS - {"$schema", "extensions"}


def manifest(root=ROOT):
    data = json.loads((root / "config/plugin.json").read_text(encoding="utf-8"))
    if not isinstance(data, dict) or set(data) - PORTABLE_FIELDS or data.get("$schema") != SCHEMA:
        raise ValueError("Use the portable Agent Plugins manifest fields and declared 1.0.0 schema")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", data.get("name", "")):
        raise ValueError("Plugin name must be kebab-case")
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[A-Za-z0-9.-]+)?", data.get("version", "")):
        raise ValueError("Use a semantic release version, for example 2.0.0-alpha.1")
    for key in ("description", "license"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f"Plugin manifest needs {key}")
    return data


def source_manifests(root=ROOT):
    data = manifest(root)
    common = {key: value for key, value in data.items() if key in CLAUDE_FIELDS}
    codex = {**data.get("extensions", {}).get("com.openai", {}), **common, "skills": "./.agents/skills/"}
    claude = {**common, "skills": "./.agents/skills/"}
    return {".codex-plugin/plugin.json": json.dumps(codex, indent=2, ensure_ascii=False) + "\n",
            ".claude-plugin/plugin.json": json.dumps(claude, indent=2, ensure_ascii=False) + "\n"}


def archive_package(folder, archive):
    """Use stable order, timestamps, and file modes for reproducible ZIP bytes."""
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as output:
        for path in sorted(folder.rglob("*")):
            if path.is_symlink():
                raise ValueError(f"Refusing symlink in release: {path}")
            if path.is_file():
                info = zipfile.ZipInfo(path.relative_to(folder).as_posix(), date_time=(1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = (0o100755 if path.stat().st_mode & 0o111 else 0o100644) << 16
                output.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def publish_file(source, destination):
    """Publish complete bytes atomically without replacing an existing path."""
    # Staging and destinations share a filesystem. Unlike rename on POSIX,
    # linking refuses an existing file, directory, or symlink at the destination.
    os.link(source, destination)


def publish_directory(source, destination):
    """Reserve a fresh directory and publish its entries without overwriting."""
    destination.mkdir()
    for path in sorted(source.rglob("*")):
        target = destination / path.relative_to(source)
        if path.is_symlink():
            raise ValueError(f"Refusing symlink in release: {path}")
        if path.is_dir():
            target.mkdir()
        elif path.is_file():
            publish_file(path, target)


def context_document(packages):
    parts = ["# Selected MBSE Agents context", "",
             "Use the selected guidance for the supplied task. Preserve the project's instructions,",
             "source IDs, evidence status, and open decisions. This export grants no tool access.",
             "Review its scope before sharing project data with a host.", ""]
    for name, source in packages:
        for file in [source / "SKILL.md", *sorted((source / "references").rglob("*.md"))]:
            relative = file.relative_to(source)
            content = file.read_text(encoding="utf-8")
            content = re.sub(r"\A---\n.*?\n---\n", "", content, flags=re.S)

            def rewrite(match):
                target = match.group(1)
                if ":" in target or target.startswith("#"):
                    return match.group(0)
                resolved = (file.parent / target.split("#")[0]).resolve()
                if not resolved.is_relative_to(source.resolve()):
                    raise ValueError(f"Package reference escapes {name}: {target}")
                suffix = "#" + target.split("#", 1)[1] if "#" in target else ""
                return f"](.assistant/skills/{name}/{resolved.relative_to(source.resolve()).as_posix()}{suffix})"

            content = re.sub(r"\]\(([^\s)]+)\)", rewrite, content)
            parts += [f"## {name} / {relative.as_posix()}", "", content.rstrip(), ""]
    return "\n".join(parts)


def build(output=None, *, names=None, target="plugin", make_zip=False, dry_run=False, root=ROOT):
    data = manifest(root)
    if target not in {"plugin", "databricks"}:
        raise ValueError("Choose plugin or databricks")
    if target == "databricks" and not names:
        raise ValueError("Databricks exports require explicit --skill selections")
    names = names or [item["name"] for item in entries(root)]
    packages = selected_sources(names, root)
    expected = {name: package_fingerprints(source, root) for name, source in packages}
    suffix = "-databricks" if target == "databricks" else ""
    output = Path(output or root / "build" / f"{data['name']}-{data['version']}{suffix}").absolute()
    archive = output.with_name(output.name + ".zip") if make_zip else None
    if output.exists() or output.is_symlink() or (archive and (archive.exists() or archive.is_symlink())):
        raise ValueError(f"Build output already exists; choose a fresh --output: {output}")
    if any(output.resolve().is_relative_to(source.resolve()) for _, source in packages):
        raise ValueError("Build output must be outside canonical skill packages")
    if dry_run:
        return output, archive
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".mbse-package-", dir=output.parent) as temp:
        stage = Path(temp) / "package"
        stage.mkdir()
        skills = stage / ("skills" if target == "plugin" else ".assistant/skills")
        skills.mkdir(parents=True)
        for name, source in packages:
            copy_package(source, skills / name, root=root, expected=expected[name])
        shutil.copy2(root / "LICENSE", stage / "LICENSE")
        listing = "\n".join(f"- {name}" for name, _ in packages)
        if target == "plugin":
            (stage / "plugin.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            claude = {key: value for key, value in data.items() if key in CLAUDE_FIELDS}
            claude["skills"] = "./skills/"
            (stage / ".claude-plugin").mkdir()
            (stage / ".claude-plugin/plugin.json").write_text(json.dumps(claude, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            guide = (f"# {data['name']} {data['version']}\n\n"
                     "This local build contains portable skills and a Claude Code manifest.\n"
                     "It does not register a marketplace or install into a host.\n\n"
                     "For Claude Code, run:\n\n"
                     "    claude plugin validate /absolute/path/to/this/folder\n"
                     "    claude --plugin-dir /absolute/path/to/this/folder\n\n"
                     "For Codex, add this built folder through the host's local plugin workflow,\n"
                     "or use the source repository's installer for selected project skills.\n\n"
                     "Package structure is checked locally; host discovery and engineering output\n"
                     "quality are separate checks. No tool credentials or live connections are bundled.\n\n")
        else:
            context = context_document([(name, skills / name) for name, _ in packages])
            context += "\n## License\n\n" + (stage / "LICENSE").read_text(encoding="utf-8")
            (stage / "context.md").write_text(context, encoding="utf-8")
            guide = ("# Databricks selected skill export\n\n"
                     "Import the selected folders under .assistant/skills/ into your Databricks\n"
                     "user skills location, /Users/<username>/.assistant/skills/, preserving files.\n"
                     "Choose a fresh folder if a skill with the same name already exists.\n"
                     "Invoke the selected skill with an @ mention in Genie Code.\n\n"
                     "context.md combines the selected instructions and Markdown references for\n"
                     "manual context loading when workspace skill import is unavailable.\n"
                     "Do not place it into workspace-wide instructions: its scope is this task.\n\n"
                     "The export is checked locally. No Databricks workspace upload, native\n"
                     "discovery test, or engineering behavior evaluation was performed.\n\n")
        (stage / "README.md").write_text(guide + "## Included skills\n\n" + listing + "\n", encoding="utf-8")
        staged_archive = Path(temp) / "package.zip"
        if make_zip:
            archive_package(stage, staged_archive)
        try:
            publish_directory(stage, output)
            if make_zip:
                publish_file(staged_archive, archive)
        except (OSError, ValueError) as error:
            # Once visible, an output may contain local changes. Leave it in
            # place; moving it into the temporary directory would delete them.
            visible = [str(path) for path in (output, archive)
                       if path is not None and (path.exists() or path.is_symlink())]
            detail = ", ".join(visible) or "none"
            raise OSError(f"Publication failed: {error}. Visible outputs preserved: {detail}. "
                          "A directory may be partial; use a fresh --output when retrying.") from error
    return output, archive


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Fresh output directory (default: build/name-version)")
    parser.add_argument("--skill", action="append", help="Select canonical skills; repeat as needed")
    parser.add_argument("--target", choices=("plugin", "databricks"), default="plugin")
    parser.add_argument("--zip", action="store_true", help="Also write a reproducible ZIP beside the folder")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--source-manifests", choices=("check", "write"), help="Check or regenerate source host manifests from config/plugin.json")
    args = parser.parse_args()
    try:
        if args.source_manifests:
            if args.output or args.skill or args.zip or args.dry_run or args.target != "plugin":
                parser.error("Use --source-manifests separately from build options")
            for relative, content in source_manifests().items():
                path = ROOT / relative
                if args.source_manifests == "write":
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(content, encoding="utf-8", newline="\n")
                elif not path.is_file() or path.read_text(encoding="utf-8") != content:
                    raise ValueError(f"Stale source manifest: {relative}; run --source-manifests write")
            print("Source manifests " + ("generated" if args.source_manifests == "write" else "current"))
            return
        folder, archive = build(args.output, names=args.skill, target=args.target, make_zip=args.zip, dry_run=args.dry_run)
        prefix = "would build: " if args.dry_run else "built: "
        print(prefix + str(folder))
        if archive:
            print(prefix + str(archive))
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, str(error) + "\n")


if __name__ == "__main__":
    main()
