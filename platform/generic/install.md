# Portable use

Read the [catalog](../../docs/skills.md), then provide the chosen canonical
`SKILL.md` and its local references to your assistant through the host's documented
context or skill mechanism. Describe the task, inputs, desired artifacts, and
completion boundary. If the host lacks skill discovery, load context manually.
Do not paste all domains into an always-on system prompt.

Each canonical package is self-contained. Task/domain combinations are optional;
select those that improve the current decision. A Markdown file does not grant
MBSE tool access or establish certification. Use available authorized connectors
or label the output as a proposal.

The installer supports `--destination /explicit/skills/directory` for hosts that
read this skill format. Check that host's current documentation for discovery
and invocation. The original named-agent formats are no longer maintained.
