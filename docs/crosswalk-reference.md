# Model and evidence crosswalks

These mappings are proposed engineering practice, not normative equivalents,
vendor endorsements, or a promise of supported automation. Confirm the tool,
metamodel/profile, edition, extensions, and exchange configuration for the project.

## Engineering concepts and SysML v1-style views

This table retains the repository's illustrative v1-style vocabulary. Select an
actual language/profile version before creating or exchanging model elements.
It is not a tested mapping for every tool that advertises SysML support.

| Engineering intent | Capella / Arcadia content | SysML v1-style content | Linked records |
| --- | --- | --- | --- |
| Stakeholder context | Operational actors, capabilities, activities | Actors, use cases, context blocks | Needs and ConOps |
| Functional behavior | System/logical functions and exchanges | Activities, states, interactions | Requirements and scenarios |
| Physical allocation | Components, physical functions, links | Blocks, parts, ports, allocations | Design decisions and budgets |
| Requirement satisfaction | Requirement integration/links as configured | Requirements and satisfy/derive/trace relations | Controlled requirement baseline |
| Verification | Linked scenario/analysis results | Test cases and verify relations | Procedure, configuration, outcome |
| Hazard/threat control | Linked analysis and allocated behavior | Profile-specific analysis and requirements | Risk/control/evidence records |

## SysML v2 work

SysML v2 uses definitions and usages for the concepts below. Keep its source
model and notation distinct from v1 blocks/stereotypes; a similar engineering
intent does not establish a lossless conversion.

| Engineering intent | Relevant SysML v2 concepts | Work still requiring project decisions |
| --- | --- | --- |
| Structure and external interaction | Parts, ports, connections, and interfaces | Boundary, multiplicity, exchanged items, responsibility |
| Behavior and modes | Actions and states | Conditions, transitions, timing, failure and recovery meaning |
| Responsibility and requirements | Allocations, requirements, and satisfy requirement usages | Relation semantics, actual allocation, satisfaction rationale |
| Verification planning | Verification cases | Procedure, configuration, result, and evidence applicability |

Concept names were checked in [OMG SysML 2.0 Part 1](https://www.omg.org/spec/SysML/2.0/Language/PDF),
formal/2026-03-02, sections 7.6, 7.11–7.15, 7.17–7.18, 7.21, and 7.24.
The [OMG version catalogs](https://www.omg.org/spec/SysML/2.0/)
identify the published language and transformation specifications. This narrow
terminology check does not validate a parser, exporter, transformation, or tool
integration. Use the project's supported version and verify representative
round trips before adopting an exchange.

## Tools and controlled exchange

Cameo/CATIA Magic, Rhapsody, and Sparx Enterprise Architect can express
SysML/UML concepts with their configured profiles. Exact element creation and
export behavior depend on the version and extensions; do not invent stereotype
names. DOORS/DOORS Next can provide linked controlled requirements. Simulink or
other analysis tools can provide scoped models/results. FMI/FMU, ReqIF, and OSLC
are integration mechanisms, not evidence that trace semantics survive transfer.

For a controlled exchange, specify ID preservation, relation direction/type,
units, version, source of truth, conflict handling, extraction/filter settings,
and reconciliation. Inspect a representative round trip. Check that a verify
link connects an activity which actually tests the requirement's conditions.

Keep source obligations, proposed design satisfaction, planned verification,
executed outcomes, and authorized acceptance separate. The optional
[trace meanings](../.agents/skills/mbse-systems-engineering/references/engineering-records.md#trace-meanings)
are local record conventions, not normative SysML relationship definitions.

Domain-specific threads and reviewer questions live in the domain packages'
references. Use [the catalog](skills.md) to find the relevant package. Live tool
access requires an available, authorized connector/API; these skills do not
install or qualify one.
