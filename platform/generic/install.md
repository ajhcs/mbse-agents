# Generic Install Guide

This guide covers any markdown-aware AI coding tool not listed in the platform-specific guides.

## Requirements

Your tool must support at least one of:
- System prompts or custom instructions (paste markdown content)
- File context or knowledge base uploads (attach markdown files)
- Project-level configuration files (reference file paths)

## Setup

1. Copy the `agents/` directory into your project:

```bash
cp -r agents/ /path/to/your-project/agents/
```

2. Load the relevant agent file(s) using your tool's context mechanism.

## Stripping Frontmatter

Some tools don't parse YAML frontmatter. Strip it before pasting:

```bash
# Remove YAML frontmatter from an agent file
sed '1{/^---$/!q;};1,/^---$/d' agents/aerospace-systems-engineer.md
```

Or with awk:

```bash
awk 'BEGIN{f=0} /^---$/{f++; next} f>=2||f==0' agents/aerospace-systems-engineer.md
```

## Available Agents

| File | Domain |
|---|---|
| `agents/aerospace-systems-engineer.md` | ARP4754A, DO-178C, airborne cyber, civil/space MBSE |
| `agents/defense-systems-engineer.md` | DoDAF/UAF, MIL-STD-882E, acquisition MBSE |
| `agents/automotive-systems-engineer.md` | ISO 26262, AUTOSAR, ISO 21434, SOTIF |
| `agents/medical-device-systems-engineer.md` | IEC 62304, ISO 14971, FDA design controls, EU MDR |

## Additional Skill

`skills/defense-founder-review/SKILL.md` provides a direct strategic review process for defense and dual-use concepts. Load it alongside the Defense Systems Engineer agent for acquisition program reviews.

## Integration Pattern

1. Load the agent markdown as system context or instructions
2. Provide your domain artifacts (requirements, models, specs) as user context
3. Ask domain-specific questions referencing the standards in the agent file
