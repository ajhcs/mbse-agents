# OpenAI Codex CLI Install Guide

## Setup

1. Copy `platform/claude-code/AGENTS.md` into your project root:

```bash
cp platform/claude-code/AGENTS.md /path/to/your-project/AGENTS.md
```

Codex reads `AGENTS.md` automatically when present in the project root.

2. Copy the `agents/` directory into your project:

```bash
cp -r agents/ /path/to/your-project/agents/
```

## Direct Execution

Run an agent's instructions directly with `codex exec`:

```bash
# Feed an agent file as context for a task
codex exec --file agents/aerospace-systems-engineer.md \
  "Review this SysML model for ARP4754A compliance"

# Combine with a specific file
codex exec --file agents/defense-systems-engineer.md \
  --file docs/architecture.md \
  "Map this architecture to DoDAF OV-1 and SV-1 views"
```

## In Codex Sessions

Reference agents by path in your prompts:

```
Read agents/automotive-systems-engineer.md and apply its expertise to review
the ISO 26262 ASIL decomposition in docs/safety-analysis.md.
```

## With Defense Founder Review

The `skills/defense-founder-review/SKILL.md` can be passed as an additional context file:

```bash
codex exec --file agents/defense-systems-engineer.md \
  --file skills/defense-founder-review/SKILL.md \
  "Review this acquisition program's SE artifacts"
```
