# Claude Code Install Guide

## Project-Level Setup (Recommended)

1. Copy the `agents/` directory into your project root:

```bash
cp -r agents/ /path/to/your-project/agents/
```

2. Reference agents in your project's `CLAUDE.md`:

```markdown
## Specialist Agents

See `agents/` for MBSE domain agents. Use `subagent_type` display names:
- "Aerospace Systems Engineer"
- "Defense Systems Engineer"
- "Automotive Systems Engineer"
- "Medical Device Systems Engineer"
```

3. Copy `platform/claude-code/AGENTS.md` into your project root for auto-discovery.

4. Optionally copy `skills/defense-founder-review/` into your project's `skills/` directory.

## User-Level Setup

Install agents globally so they're available in every project:

```bash
mkdir -p ~/.claude/agents/
cp agents/*.md ~/.claude/agents/
```

## Usage

Invoke agents via the `Agent` tool with display names (spaces, title case):

```
subagent_type="Aerospace Systems Engineer"
subagent_type="Defense Systems Engineer"
subagent_type="Automotive Systems Engineer"
subagent_type="Medical Device Systems Engineer"
```

**Important:** Use display names, not hyphenated filenames. `"Aerospace Systems Engineer"` is correct; `"aerospace-systems-engineer"` will be blocked.

## With Defense Founder Review Skill

If the `defense-founder-review` skill is installed, use `/defense-founder-review` to run a direct strategic review of defense and dual-use concepts and SE outputs.
