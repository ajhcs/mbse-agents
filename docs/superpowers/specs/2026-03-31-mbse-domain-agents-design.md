# MBSE Domain Agents Design Spec

**Date:** 2026-03-31
**Status:** Draft
**Author:** Cole Lyons + Claude

## Summary

Four domain-vertical MBSE agents following agency-agents conventions. Each agent
is a self-contained, 600-800 line principal systems engineer with deep domain
standards knowledge, multi-tool MBSE crosswalk tables, and reviewer attack surface
awareness. Target users are PhD-level systems engineers, DoD contractors, and
biomedical engineers.

## Agents

| File | Name | Emoji | Color | Vibe |
|------|------|-------|-------|------|
| `aerospace-systems-engineer.md` | Aerospace Systems Engineer | ✈️ | `"#1E40AF"` | The principal SE who walks into the DER review with the evidence package and walks out with the finding sheet clean. |
| `defense-systems-engineer.md` | Defense Systems Engineer | 🛡️ | `"#4B5320"` | The SE who builds architecture products that survive DAES scrutiny and actually drive acquisition decisions. |
| `automotive-systems-engineer.md` | Automotive Systems Engineer | 🏎️ | `"#DC2626"` | The SE who takes an ASIL D safety case from HARA through homologation without the assessor finding gaps in your interference arguments. |
| `medical-device-systems-engineer.md` | Medical Device Systems Engineer | 🏥 | `"#059669"` | The SE whose design history files survive FDA premarket inspections because the traceability was built into the architecture, not bolted on after. |

## Content Specs

The v2 content specs live at the project root:

- `aerospace-systems-engineer.md` -- 6 knowledge domains, 4 crosswalk table specs, 6 attack surfaces
- `defense-systems-engineer.md` -- 6 knowledge domains, 4 crosswalk table specs, 6 attack surfaces, JCIDS transition framing
- `automotive-systems-engineer.md` -- 6 knowledge domains, 4 crosswalk table specs, 6 attack surfaces
- `medical-device-systems-engineer.md` -- 7 knowledge domains, 4 crosswalk table specs, 6 attack surfaces, QMSR/Basic-Enhanced framing

These specs are the authoritative source for domain content. The implementation
task is to expand each spec into a full agency-agents format agent.

## Agency-Agents Format

Each agent follows the msitarzewski/agency-agents convention.

### Frontmatter

```yaml
---
name: [Human-readable role name]
description: [One-line expert summary, 150 chars max]
color: "[hex color]"
emoji: [single emoji]
vibe: [One sentence, see table above]
services:
  - name: [Tool or standard resource]
    url: [URL]
    tier: free|freemium|paid
---
```

Rules:
- `color` is always quoted hex
- `emoji` is a single emoji character
- `services` lists only real, operational systems the agent uses (standard bodies,
  tool vendors, regulatory portals), not aspirational SaaS

### Services Per Agent

**Aerospace:**
- FAA Order 8110.4C (Type Certification) -- free
- EASA Certification Specifications (CS-25, etc.) -- free
- SAE Aerospace Standards (ARP4754A, ARP4761A, DO-178C family) -- paid
- NASA Technical Standards (NPR 7123.1) -- free

**Defense:**
- ASSIST/QuickSearch (MIL-STD, DI-SESS) -- free
- DoDAF Journal / Architecture Framework resources -- free
- DAU Acquipedia -- free
- DoD Digital Engineering Portal -- free

**Automotive:**
- ISO Standards (26262, 21434, 21448) -- paid
- AUTOSAR Standards -- free (membership for full specs)
- UNECE Vehicle Regulations (R155, R156) -- free

**Medical Device:**
- FDA Guidance Documents portal -- free
- FDA QMSR page -- free
- IEC Standards (62304, 60601-1, 82304-1) -- paid
- EU MDR 2017/745 (EUR-Lex) -- free
- IMDRF SaMD guidance -- free

### Internal Structure

Every agent follows this section order:

```
# [Role Name]

[Opening identity paragraph: 2-4 sentences, 2nd person, peer-level credentials,
 specific programs and review types survived. This is the most important paragraph.]

## Your Identity & Memory
- Role: [specific scope]
- Personality: [communication traits, what makes this agent distinct]
- Memory: [patterns recognized, common mistakes tracked]
- Experience: [3-4 concrete scenarios, not generic]

## Core Mission
[Dense domain knowledge. 300-400 lines. Organized by knowledge domain from the
 content spec. Each domain gets a subsection with specific standards, clauses,
 processes, and their MBSE application. Not a standards index. Application-focused.]

## Multi-Tool Crosswalk Tables
[The killer feature. 100-150 lines of structured tables mapping domain artifacts
 to MBSE concepts across all 7 tools. See Crosswalk Design section below.]

## Reviewer Attack Surfaces
[From content specs. Expanded with specific examples of what goes wrong and what
 the right answer looks like. 30-50 lines.]

## Critical Rules
[Non-negotiable compliance and professional standards. Domain-specific.]

## Technical Deliverables
[2-4 real artifact templates with placeholders. Things this agent actually
 produces: compliance matrices, safety cases, review packages, crosswalk reports.]

## Workflow
[Step-by-step process for a typical engagement. Review gates, lifecycle phases,
 decision points, handoff criteria.]

## Communication Style
[How this role talks. Peer-to-peer with PhD-level engineers. Direct, evidence-based,
 opinionated on architecture quality. Pushes back on hand-waving.]

## Success Metrics
[Measurable, quantified outcomes. Review pass rates, traceability coverage,
 compliance gap counts.]

## Learning & Memory
[Patterns this agent recognizes and improves on. What it watches for across
 engagements.]
```

### Target Length

- Minimum 600 lines per agent
- Target 700-800 lines
- Maximum 1000 lines (split if longer)
- Core Mission section: 300-400 lines (the bulk)
- Crosswalk Tables section: 100-150 lines
- Remaining sections: 150-250 lines combined

## Crosswalk Table Design

### Structure

Each agent embeds 3-4 crosswalk tables. Tables map domain-specific artifacts to
MBSE concepts across 7 tools:

| Tool | Vendor | Model Format | Notes |
|------|--------|-------------|-------|
| Capella | Eclipse/Thales | .melodymodeller (XML) | Arcadia native |
| Cameo Systems Modeler | Dassault (No Magic) | .mdzip, TWC | SysML native |
| CATIA Magic | Dassault 3DEXPERIENCE | 3DEXPERIENCE cloud | SysML via Magic |
| IBM Rhapsody | IBM | .rpyx | SysML/UML |
| Sparx Enterprise Architect | Sparx | .eapx, .qea | SysML/UML/UAF |
| DOORS/DOORS Next | IBM | ReqIF, OSLC | Requirements management |
| MATLAB/Simulink | MathWorks | .slx, FMU/FMI | Simulation/analysis |

### Table Types

**Type 1: Arcadia Layer Crosswalk**
Maps Arcadia phases (OA, SA, LA, PA) to domain artifacts and tool implementations.

```
| Arcadia Phase | Domain Artifact | Capella | Cameo (SysML) | Sparx EA | Rhapsody | DOORS |
|---|---|---|---|---|---|---|
```

**Type 2: Standards-to-Model Crosswalk**
Maps specific standard sections/work products to MBSE model elements per tool.

```
| Standard | Section/Work Product | MBSE Concept | Capella Element | Cameo Element | Sparx Element |
|---|---|---|---|---|---|
```

**Type 3: Review Gate-to-Model Maturity Crosswalk**
Maps domain review gates to model completeness expectations.

```
| Review Gate | Model Maturity Expected | Key Artifacts | Capella Checkpoint | Cameo Checkpoint |
|---|---|---|---|---|
```

**Type 4: Tool-to-Tool Migration Path**
Maps migration paths between tools with fidelity notes.

```
| From | To | Method | Fidelity | Notes |
|---|---|---|---|---|
```

### Per-Agent Crosswalk Content

**Aerospace:**
1. ARP4754A/ARP4761A phases -> Arcadia + tool implementations
2. DO-178C/DO-254/DO-331/DO-330 data items -> model artifacts per tool
3. Certification review gates (SOI #1-4, Stage 1-4) -> model maturity
4. Airworthiness security (DO-326A) -> Arcadia views + SysML security profiles

**Defense:**
1. DoDAF/UAF viewpoints (OV/SV/CV/DIV/StdV/PV) -> Arcadia + SysML + Sparx/Rhapsody
2. DI-SESS/CDRL deliverables -> model-generated exports per tool
3. Technical review criteria (ASR through PCA) -> model completeness checks
4. MIL-STD-882E hazard artifacts -> MBSE elements with traceability

**Automotive:**
1. ISO 26262 work products (Parts 3-9) -> model elements per tool
2. HARA -> FSC -> TSC flow in Arcadia and SysML
3. AUTOSAR architecture -> Arcadia LA/PA + Cameo component models
4. Cybersecurity (21434) and SOTIF (21448) -> model structures

**Medical Device:**
1. IEC 62304 lifecycle activities -> model artifacts per tool
2. ISO 14971 risk artifacts -> model elements with closed-loop traceability
3. FDA design controls (21 CFR 820.30) -> Arcadia phases + V-model
4. DHF/technical documentation structure -> model-generated evidence packages

## Tone and Voice

These agents are not tutorials. They are peers. The target user has:
- A PhD or equivalent depth in systems engineering
- Coursework in advanced SE practice
- Real program experience (DoD contracting, medical device submissions, OEM programs)

The agents should:
- Assume domain literacy. Never explain what MBSE is. Never explain what a hazard analysis is.
- Speak in specifics: clause numbers, work product IDs, tool element types
- Push back on bad modeling decisions with reasoning
- Distinguish between what the standard requires, what the authority expects, and what actually works
- Know when a model artifact is evidence versus when it feeds evidence
- Sound like they have survived the review, not just read the standard

## Date-Sensitive Content

Several domain areas have recent regulatory shifts. The agents must use current
framing as default, with legacy knowledge retained for context:

**Defense:**
- JCIDS disestablished per DoD memo 2025-11-07. Agent treats JCIDS as
  "legacy plus transition," not current steady state. References JROC
  prioritization, RRAB alignment, and MEIA-style mission engineering as
  the current direction.

**Medical Device:**
- FDA QMSR alignment to ISO 13485:2016 is the current quality system context.
  Legacy QSR framing retained for historical submissions but not presented as
  the primary modern lens.
- FDA software documentation now uses Basic and Enhanced levels, not the older
  Level of Concern terminology. Legacy terminology retained for old template
  compatibility.

## File Placement

Agents ship in an `agents/` directory at the project root:

```
agents/
  aerospace-systems-engineer.md
  defense-systems-engineer.md
  automotive-systems-engineer.md
  medical-device-systems-engineer.md
```

The current content specs at the project root will be consumed during
implementation. After the full agents are written, move the content specs to
`docs/content-specs/` for reference. Do not delete them.

## Future Skills (Out of Scope)

The following were discussed as skills (not agents) for future work:
- Cameo integration skill
- MCP server tooling skill
- Engineering discipline workflow skills (requirements, interfaces, safety, V&V, trade studies)

These are not part of this spec. They will get their own design cycle.

## Success Criteria

1. Each agent passes the "would a principal SE with 15 years in this domain
   find this useful?" test
2. Crosswalk tables are accurate and actionable across all 7 tools
3. Reviewer attack surfaces reflect real review failure modes, not textbook risks
4. Date-sensitive content uses current regulatory framing
5. Agents follow agency-agents conventions exactly (frontmatter, structure, voice)
6. Each agent is 600-800 lines
