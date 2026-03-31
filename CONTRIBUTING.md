# Contributing to MBSE Agents

We welcome contributions from systems engineers who work with these standards and tools daily. Domain accuracy is everything here. A single wrong clause reference does more damage than a missing feature.

## What We Need

- **New domain agents** (nuclear, naval, space, railway, industrial control systems)
- **Crosswalk table improvements** (new tool mappings, version-specific corrections)
- **Standards accuracy fixes** (clause references, process descriptions, regulatory updates)
- **Platform install guide updates** (when AI platform APIs or workflows change)

## Adding a New Domain Agent

Follow the structure in [docs/design-spec.md](docs/design-spec.md). Every agent uses the same format:

### 1. Frontmatter

```yaml
---
name: [Domain] Systems Engineer
description: [One-line expert summary]
color: "[hex color]"
emoji: [single emoji]
vibe: [One sentence describing the practitioner this agent embodies]
services:
  - name: [Standards body or tool vendor]
    url: [URL]
    tier: free|freemium|paid
last_verified: [YYYY-MM-DD]
---
```

### 2. Section order

```
# [Role Name]
[Opening identity paragraph: 2-4 sentences, peer-level]

## Your Identity & Memory
## Core Mission          (bulk of the agent, 300-400 lines)
## Multi-Tool Crosswalk Tables
## Reviewer Attack Surfaces
## Critical Rules
## Technical Deliverables
## Workflow
## Communication Style
## Success Metrics
## Learning & Memory
```

### 3. Quality bar

- Target density over length. Every line should teach something a junior SE doesn't know.
- Assume the reader has a PhD or equivalent depth. Never explain what MBSE is.
- Reference specific clause numbers, work product IDs, and tool element types.
- Distinguish between what the standard requires, what the authority expects, and what actually works.
- Crosswalk tables must cover: Capella, Cameo/CATIA Magic, Rhapsody, Sparx EA, DOORS, MATLAB/Simulink.

### 4. Crosswalk table format

Each agent includes 3-4 crosswalk tables. See existing agents for the exact column structure. Tables map domain artifacts to MBSE concepts across all supported tools.

## Improving Existing Agents

- **Report inaccuracies:** Open an issue with the specific clause, section, or table entry that's wrong. Include the correct information and a reference.
- **Add standards coverage:** Submit a PR adding new sections to the Core Mission area. Follow the existing density and voice.
- **Update for regulatory changes:** When a standard gets a new edition or a regulatory body changes requirements, update the agent and bump the `last_verified` date.

## Standards Currency

Agents are maintained against current standard editions. When a standard is superseded:

1. Update the agent to reflect the current edition as the primary reference
2. Retain legacy content with clear `[LEGACY]` markers for backward compatibility
3. Update `last_verified` in frontmatter
4. Note the change in your PR description

Report outdated content via GitHub Issues.

## Domain Maintainers

Each agent has a named maintainer responsible for domain accuracy review:

| Agent | Maintainer | Standards Scope |
|-------|-----------|----------------|
| Aerospace Systems Engineer | Cole Lyons (@ajhcs) | ARP4754A, DO-178C family, ARP4761A |
| Defense Systems Engineer | Cole Lyons (@ajhcs) | DoDAF/UAF, MIL-STD-882E, DI-SESS |
| Automotive Systems Engineer | Cole Lyons (@ajhcs) | ISO 26262, ISO 21434, AUTOSAR |
| Medical Device Systems Engineer | Cole Lyons (@ajhcs) | IEC 62304, ISO 14971, FDA QMSR |

All contributions require review by the domain maintainer before merge. This is non-negotiable for regulated-domain content.

## Review Process

1. Fork the repo and create a branch
2. Make your changes following the style guide above
3. Open a PR with a clear description of what changed and why
4. The domain maintainer reviews for accuracy, voice, and completeness
5. Address review feedback
6. Maintainer merges when satisfied

We prioritize accuracy over speed. PRs that introduce unverified claims or unsourced assertions will be rejected.

## Style Guide

- **Voice:** Peer-to-peer with experienced engineers. Direct, evidence-based, opinionated on quality.
- **Specificity:** Clause numbers, not "the standard says." Tool element types, not "model it in the tool."
- **No filler:** Every sentence earns its place. If removing a sentence loses no information, remove it.
- **Full design spec:** See [docs/design-spec.md](docs/design-spec.md) for the complete conventions.
