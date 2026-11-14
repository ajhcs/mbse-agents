# Databricks Genie Code

Export only the skills needed for the current task:

```sh
python3 scripts/package_plugin.py --target databricks --skill mbse-requirements --skill mbse-architecture --output build/databricks-review --zip
```

Use `py` on Windows. The fresh output contains `.assistant/skills/<name>/`
packages, their licenses, and a combined `context.md` with the selected Markdown
references. The ZIP is a file-transfer artifact, not a claimed Databricks plugin
import format. Existing outputs are refused.

For native user skills, transfer the selected package directories into
`/Users/<username>/.assistant/skills/` in your Databricks workspace. Preserve
existing packages; reconcile a name collision before replacing anything. Genie
Code also documents registering a different parent skills folder through its
settings, which is useful for a Databricks Git folder.

Start a new Genie Code chat and select a skill with an `@` mention. Supply the
system brief and state the expected artifact. If native skills are unavailable,
provide `context.md` through the chat's available context mechanism. Keep this
task-specific material out of workspace-wide instructions.

The export's files, references, and selected contents are tested locally. No
Databricks upload, workspace discovery, or engineering behavior evaluation has
been performed. This export does not connect to Unity Catalog, deploy an agent,
or grant data access. See the [support matrix](../support.md).

Source checked 2026-11-13:
[Databricks Genie Code skills](https://docs.databricks.com/aws/en/genie-code/skills/).
