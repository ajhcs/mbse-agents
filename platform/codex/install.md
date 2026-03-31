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

Run `codex exec` from the project root and tell Codex which files to read:

```bash
# Run from the repository root so Codex can read the referenced files
cd /path/to/your-project

# Ask Codex to read the agent file and apply it to your artifact
codex exec \
  "Read agents/aerospace-systems-engineer.md, then review docs/model.md for ARP4754A compliance."

# Or point Codex at a different working directory explicitly
codex exec -C /path/to/your-project \
  "Read agents/defense-systems-engineer.md and docs/architecture.md, then map this architecture to DoDAF OV-1 and SV-1 views."
```

## In Codex Sessions

Reference agents by path in your prompts:

```
Read agents/automotive-systems-engineer.md and apply its expertise to review
the ISO 26262 ASIL decomposition in docs/safety-analysis.md.
```

## With Defense Founder Review

Reference the skill file alongside the defense agent in the prompt:

```bash
codex exec -C /path/to/your-project \
  "Read agents/defense-systems-engineer.md and skills/defense-founder-review/SKILL.md, then review this acquisition program's SE artifacts."
```
