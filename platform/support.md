# Host support and validation

The maintained paths are selected Codex project skills, a portable plugin build
with a Claude Code manifest, and a selected Databricks export. Local file checks
and host execution establish different things.

| Host | Maintained path | Evidence for this revision | Remaining host check |
| --- | --- | --- | --- |
| Codex | Repository/project skills; portable plugin build | Installer/package tests; [native source discovery](../docs/evidence/native-codex-discovery.json) found all 13 canonical namespaced skills with codex-cli 0.169.0 and no model call | Behavioral skill activation and packaged-plugin activation remain untested |
| Claude Code | Built plugin with `.claude-plugin/plugin.json` and `skills/` | Canonical-file, manifest, license, and archive tests; current official layout reviewed | Run `claude plugin validate` and invoke a skill; Claude Code is unavailable on the validation host |
| Databricks Genie Code | Selected `.assistant/skills/` export plus `context.md` | Export content and local-reference tests; official user-skill setup reviewed | Import into the target workspace and invoke with `@`; no workspace integration test was performed |
| ChatGPT | Portable plugin package, or selected manual context | Package structure checked | Account/workspace import and activation; no universal upload capability is assumed |
| Claude Desktop chat, Cursor, Aider, other hosts | Selected manual context | Canonical instructions and references supplied | No native adaptation or discovery claim for these surfaces |

Run `python3 scripts/install.py --diagnose --skill NAME` to check a package
without installing it. Use `py` on Windows. A host supports this release only
within the path and evidence stated above; tests do not establish engineering
quality, domain acceptance, or access to a model or external engineering tool.

Setup: [Codex](codex/install.md), [Claude Code](claude-code/install.md),
[Databricks](databricks/install.md), [ChatGPT](chatgpt/install.md),
[portable context](generic/install.md), [plugin build](plugin/install.md).
