# Cursor Install Guide

## Option A: .cursorrules (Quick)

Append agent references to your `.cursorrules` file:

```bash
cat >> .cursorrules << 'EOF'

## MBSE Domain Agents

When working on systems engineering tasks, read and follow the relevant agent file:
- Aerospace: agents/aerospace-systems-engineer.md
- Defense: agents/defense-systems-engineer.md
- Automotive: agents/automotive-systems-engineer.md
- Medical Device: agents/medical-device-systems-engineer.md

Use the agent's standards, workflows, and domain expertise for all SE-related outputs.
EOF
```

## Option B: Context Folder (Recommended)

1. Create a `.cursor/context/` directory in your project root:

```bash
mkdir -p .cursor/context/
```

2. Copy agent files into the context folder:

```bash
cp agents/*.md .cursor/context/
```

3. Optionally copy the defense founder review skill:

```bash
cp skills/defense-founder-review/SKILL.md .cursor/context/defense-founder-review.md
```

Cursor automatically indexes files in `.cursor/context/` and uses them as reference material.

## Usage

In Cursor chat or Composer, reference agents by name:

> "Using the Aerospace Systems Engineer agent, review this SysML block diagram for DO-178C compliance."

> "Apply the Medical Device Systems Engineer guidance to generate an IEC 62304 software safety classification."

## Setup Checklist

1. Copy `agents/` directory to your project
2. Either append to `.cursorrules` or populate `.cursor/context/`
3. Verify Cursor indexes the files (check the context panel)
