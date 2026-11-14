# Codex installation and maintenance

Run the commands from this checkout. Use Python 3.10 or newer: `python3` on
Linux/macOS, or `py` on Windows. The installer needs only the standard library.

```sh
python3 --version
python3 scripts/install.py --list
python3 scripts/install.py --diagnose --skill mbse-requirements
python3 scripts/install.py --project /path/to/project --skill mbse-requirements --skill mbse-architecture --dry-run
python3 scripts/install.py --project /path/to/project --skill mbse-requirements --skill mbse-architecture
```

PowerShell accepts quoted paths:

```powershell
py scripts/install.py --project 'C:\Projects\pump-study' --skill mbse-medical-device --skill mbse-verification-evidence --dry-run
```

Canonical packages are `.agents/skills/<name>`. Launching Codex in this checkout
uses those packages directly. The installer copies selected packages, references,
and license into the target project's `.agents/skills/`. Use `--destination` for
an explicit different skills directory. Existing project instructions, model
settings, and credentials are preserved.

In the destination project, open a new Codex chat and select the skill with `$`:

> Use $mbse-requirements on this brief. Show the source and acceptance condition
> for each proposed requirement, and identify the decisions that need my input.

If discovery fails, run `--diagnose --project /path/to/project --skill NAME`,
confirm the reported path and host project match, then start a new chat. A ready
package report checks files; it does not prove native discovery or answer quality.
See the [support matrix](../support.md) for the tested boundary.

## Inspect and update

```sh
python3 scripts/install.py --project /path/to/project --skill mbse-requirements --inspect
python3 scripts/install.py --project /path/to/project --skill mbse-requirements --diff
python3 scripts/install.py --project /path/to/project --skill mbse-requirements --update --dry-run
python3 scripts/install.py --project /path/to/project --skill mbse-requirements --update
```

Inspection separates local changes since the managed install from changes in
the incoming package. `--diff` displays current-to-incoming text differences;
it never merges or writes. For an unmanaged package, the original local baseline
is unknown. Review changes in a separate copy before deciding what to retain.

The installer refuses unmanaged or modified targets. It stages and checks every
selected package before replacement. A failed commit rolls earlier replacements
back; if rollback encounters new local changes or another I/O failure, the error
identifies the preserved target and original backup for recovery. Abrupt process
termination or power loss is not a transaction guarantee. Successful updates
print their backup paths under the skills parent's `.mbse-backups/`.

## Remove or restore a managed package

```sh
python3 scripts/install.py --project /path/to/project --skill mbse-requirements --uninstall --dry-run
python3 scripts/install.py --project /path/to/project --skill mbse-requirements --uninstall
python3 scripts/install.py --project /path/to/project --skill mbse-requirements --restore /path/to/project/.agents/.mbse-backups/mbse-requirements/BACKUP_ID --dry-run
```

Removal moves an unchanged managed package into a backup. It does not delete it.
Replace `BACKUP_ID` with the printed identifier; remove `--dry-run` to restore.
Restore checks the backup, preserves its source copy, and backs up any unchanged
current package. Modified current packages and modified backups are refused.
For plugin-manager installations, use that host's lifecycle controls instead of
this standalone-package installer.

## Build a native plugin

Use the [plugin build guide](../plugin/install.md) for a portable plugin and
local marketplace setup. Source compatibility manifests point at `.agents/skills/`;
the built folder supplies the portable root `skills/` directory.

Sources checked 2026-11-13: [Codex skills](https://developers.openai.com/codex/skills)
and [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins).
