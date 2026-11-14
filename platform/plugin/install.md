# Build an installable plugin

From the source checkout, build a fresh folder and optional ZIP:

```sh
python3 scripts/package_plugin.py --output build/local-plugin --zip --dry-run
python3 scripts/package_plugin.py --output build/local-plugin --zip
```

Use `py` on Windows. The builder reads `config/plugin.json` and `catalog.json`,
copies canonical `.agents/skills/` packages into root `skills/`, includes the
license in every package, and adds a Claude Code manifest. It excludes archived
skills, repository instructions, evaluation rubrics, and private host settings.
ZIP file order and timestamps are fixed. Existing outputs are refused, including
paths created during the build. Completed files are published with atomic
no-replacement links on the output filesystem. A publication failure preserves
and reports visible outputs; a directory may be partial. Choose a fresh output
path for another build. `--skill NAME` selects a smaller bundle.

The built folder contains:

```text
plugin.json
.claude-plugin/plugin.json
skills/<name>/SKILL.md
skills/<name>/references/
skills/<name>/LICENSE
LICENSE
README.md
```

The root source checkout supplies compatibility manifests pointing at canonical
`.agents/skills/`; the release build supplies the portable layout above. Build
for portable distribution. Building does not install, publish, or modify host
settings. After changing `config/plugin.json`, regenerate source compatibility
manifests with `python3 scripts/package_plugin.py --source-manifests write`;
use `--source-manifests check` to check freshness without writing.

## Codex local marketplace

For a local trial, merge this entry into the checkout's
`.agents/plugins/marketplace.json`, preserving any existing entries:

```json
{
  "name": "mbse-agents-local",
  "plugins": [
    {
      "name": "mbse-agents",
      "source": {"source": "local", "path": "./build/local-plugin"},
      "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
      "category": "Productivity"
    }
  ]
}
```

Register the marketplace through your host's plugin interface or the supported
CLI command below, then install the listed plugin in the desktop interface:

```sh
codex plugin marketplace add /absolute/path/to/mbse-agents
```

These registration steps are for the operator to run; the builder does not run
them. Open a fresh chat and verify that the expected skill is available. For a
smaller project installation, use the [standalone installer](../codex/install.md).

## Other maintained paths

[Claude Code](../claude-code/install.md) loads the built folder directly.
[Databricks](../databricks/install.md) uses a separate selected-skills export.
See the [support matrix](../support.md) for what has actually been tested.

Manifest/layout source checked 2026-11-13:
[OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins),
[Agent Plugins manifest schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json),
and [Claude Code manifest reference](https://code.claude.com/docs/en/plugins-reference).
