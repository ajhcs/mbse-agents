# Aider Install Guide

## Setup

1. Copy the `agents/` directory into your project root:

```bash
cp -r agents/ /path/to/your-project/agents/
```

2. Add agent files as read-only context in `.aider.conf.yml`:

```yaml
read:
  - agents/aerospace-systems-engineer.md
  - agents/defense-systems-engineer.md
  - agents/automotive-systems-engineer.md
  - agents/medical-device-systems-engineer.md
  - skills/defense-founder-review/SKILL.md
```

This makes all agent files available as reference context in every Aider session without including them in the edit set.

## Selective Loading

To load only the agents relevant to your domain, include just the ones you need:

```yaml
# Aerospace-only project
read:
  - agents/aerospace-systems-engineer.md
```

```yaml
# Defense project with founder review
read:
  - agents/defense-systems-engineer.md
  - skills/defense-founder-review/SKILL.md
```

## Command-Line Usage

You can also add agents per-session without modifying the config:

```bash
aider --read agents/automotive-systems-engineer.md
```

## Usage

Once loaded, reference agents in your Aider prompts:

```
/ask Using the Medical Device Systems Engineer context, review this risk management file against ISO 14971.
```

```
/ask Apply the Defense Systems Engineer guidance to generate a DoDAF OV-1 description.
```
