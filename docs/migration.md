# Migrate an older MBSE Agents installation

The current collection uses canonical packages in `.agents/skills`, with
`catalog.json` identifying the shipped inventory. The old root `agents/` prompt
files and root `skills/defense-founder-review` notice are archived outside normal
discovery. Loading an old migration notice does not install the replacement.

| Earlier entrypoint | Current choice |
| --- | --- |
| `agents/aerospace-systems-engineer.md` | `mbse-aerospace` |
| `agents/defense-systems-engineer.md` | `mbse-defense` |
| `agents/automotive-systems-engineer.md` | `mbse-automotive` |
| `agents/medical-device-systems-engineer.md` | `mbse-medical-device` |
| `agents/electronic-systems-engineer.md` | `mbse-electronic-systems` |
| `skills/defense-founder-review/SKILL.md` | Venture-review skill retired from the shipped catalog; original source remains archived |

Use `mbse-systems-engineering` for system understanding, explanation, synthesis,
and connected lifecycle decisions. Choose a focused task or add a domain package
when it serves the request. This is broader engineering guidance; it does not
claim equivalent venture-advisory coverage or carry forward old evaluation results.

Follow the current guide for [Codex](../platform/codex/install.md),
[Claude Code](../platform/claude-code/install.md), or
[another host](../platform/generic/install.md). Install the complete canonical
package, including its references. Source manifests and packaged builds select
the canonical skills; users do not need a second hand-maintained copy in the
repository's root `skills/` directory.

Before replacing a copy in another project or a personal host directory,
identify its origin and preserve local changes. Review the installer's dry-run
or the host's package preview. Use the documented managed update path when a
receipt exists; reconcile unmanaged or edited copies explicitly. Preserve the
project's `AGENTS.md`, `CLAUDE.md`, model settings, and unrelated skills.

After migration, confirm that the host offers the intended current skill and
that an older personal/project copy is not also being loaded. Check the active
package and its references before interpreting a new result as an assessment
of this release.

The [archived notices](archive/migration-notices/README.md) and
[retired founder skill](archive/skills/defense-founder-review/README.md) remain
available for historical interpretation.
