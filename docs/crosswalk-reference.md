# Model and evidence crosswalks

These mappings are proposed engineering practice, not normative equivalents,
vendor endorsements, or a promise of supported automation. Confirm the tool,
metamodel/profile, edition, extensions, and exchange configuration for the project.

| Engineering intent | Capella / Arcadia content | SysML-oriented content | Linked records |
| --- | --- | --- | --- |
| Stakeholder context | Operational actors, capabilities, activities | Actors, use cases, context blocks | Needs and ConOps |
| Functional behavior | System/logical functions and exchanges | Activities, states, interactions | Requirements and scenarios |
| Physical allocation | Components, physical functions, links | Blocks, parts, ports, allocations | Design decisions and budgets |
| Requirement satisfaction | Requirement integration/links as configured | Requirements and satisfy/derive/trace relations | Controlled requirement baseline |
| Verification | Linked scenario/analysis results | Test cases and verify relations | Procedure, configuration, outcome |
| Hazard/threat control | Linked analysis and allocated behavior | Profile-specific analysis and requirements | Risk/control/evidence records |

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

Domain-specific threads and reviewer questions live in the domain packages'
references. Use [the catalog](skills.md) to find the relevant package. Live tool
access requires an available, authorized connector/API; these skills do not
install or qualify one.
