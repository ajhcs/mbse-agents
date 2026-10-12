# Codex installation and discovery

Canonical packages are `.agents/skills/<name>`. Codex discovers repository skills
from the working directory up to the repository root. Launching Codex in this
checkout exposes the catalog. In another project, copy selected self-contained
packages using the installer (Python 3.10+, standard library only):

```sh
python scripts/install.py --list
python scripts/install.py --project /path/to/project --skill mbse-medical-device --skill mbse-verification-evidence --dry-run
python scripts/install.py --project /path/to/project --skill mbse-medical-device --skill mbse-verification-evidence
```

PowerShell example from this checkout:

```powershell
py scripts/install.py --project 'C:\Projects\pump-study' --skill mbse-medical-device --skill mbse-verification-evidence
```

Use `--destination` for an explicit personal skills directory, such as
`$HOME/.agents/skills`, if you want the packages available beyond one project.
Select only what you need. The installer leaves existing project instructions,
credentials, and host model settings alone. It preflights all selected targets;
unmanaged or locally edited packages cause a refusal before any package is copied.
Repeat installation is idempotent. To update unchanged managed packages, rerun
with `--update`; previous folders remain under the skills parent's `.mbse-backups`.
Locally edited packages need manual reconciliation in a separate location.

Use `/skills` or type `$` to select a skill. Explicit invocation:

> Use $mbse-aerospace and $mbse-baseline-review to examine our flight-control
> architecture's independence argument. Locate shared dependencies and evidence
> gaps. Produce a review with affected IDs and concrete repair options.

Implicit discovery is enabled through the descriptions; the model chooses the
relevant skill rather than loading every package. If a change does not appear,
restart Codex. Verify model availability in the host; see [model setup](../../docs/models.md).

For removal, identify the selected package and its `.mbse-install.json` receipt
before removing it through your ordinary file manager. Keep local work and backups.
No uninstall or update requires overwriting the project's `AGENTS.md`.

Source: [official skill discovery](https://learn.chatgpt.com/docs/build-skills).
The old `agents/*.md` files are migration notices, not skill packages.
