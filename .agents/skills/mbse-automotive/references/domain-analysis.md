# Automotive analysis and review

This reference preserves analysis and evidence questions, not a verified clause-by-clause reproduction of ISO standards. Use the adopted ISO 26262, ISO 21448, ISO/SAE 21434, AUTOSAR release, and applicable vehicle regulations for precise obligations.

## Item and safety concept

Define the item, vehicle context, interfaces, modes, driver roles, operating situations, and external measures before assessing hazards. Relate hazardous events to severity, exposure, and controllability using justified conditions. An ASIL is not a badge chosen from the component's name or a marketing claim.

Maintain a thread from safety goal through functional safety requirements, technical safety requirements, hardware/software allocations, and verification. Define safe/degraded behavior, warning, fault detection and reaction, and timing reference points. Budget the response from fault occurrence through sensing, scheduling, communication, and mitigation against the justified fault-tolerant interval. A fast algorithm cannot compensate for an unbounded upstream timeout.

For ASIL decomposition, verify the permitted decomposition and notation in the actual standard. Assess dependent failure and sufficient independence of the allocated redundant requirements. Separate decomposition from changing an item's hazard assessment or omitting process work. Two channels on the same supply or shared code can fail together.

## Hardware/software evidence and AUTOSAR

For hardware architectural metrics and failure analyses, retain failure-rate sources, circuit/application-specific failure modes, diagnostic coverage rationale, latent-fault intervals, and exclusions. Generic percentages or block-level guesses can conceal a dangerous failure mode. Quantitative estimates should expose uncertainty and operating assumptions.

For mixed-criticality software, assess interference in time, memory, communication, and shared resources. Identify mechanisms and evidence: scheduling/resource bounds, memory protection, message validation, watchdog behavior, integration tests, and fault injection as applicable. A process ASIL and a component supplier certificate do not by themselves establish the item's safety argument.

Choose AUTOSAR Classic/Adaptive or another architecture from execution, timing, compute, lifecycle, and safety constraints. Do not assume Classic automatically satisfies ASIL D or Adaptive categorically cannot. Inspect OS/platform evidence, update behavior, service discovery, partitioning, and integration responsibilities for the selected implementation. Validate exact interfaces against the [AUTOSAR release documentation](https://www.autosar.org/standards).

Requirements-based, integration, robustness, and structural coverage evidence address different claims. Check the adopted standard's method recommendations and rationale for alternatives rather than inventing blanket coding or coverage mandates.

## SOTIF, cybersecurity, and operation

A malfunction and a performance insufficiency without malfunction can produce the same unsafe vehicle behavior through different causal paths. For SOTIF work, define the intended functionality, operational design domain, triggering conditions, perception/decision limitations, foreseeable misuse, and validation envelope. A nominal success rate does not demonstrate safety at the boundary of the ODD.

For cybersecurity, link assets, trust boundaries, attack paths, consequences, goals, controls, verification, incident response, and updates. Check the relevant UNECE type-approval context and organizational obligations separately from product engineering. A TARA cannot establish a whole CSMS or SUMS.

Validate driver/operator behavior and degraded modes under representative conditions. Include maintenance, calibration, production variation, replacement parts, field monitoring, and decommissioning when they affect the safety assumptions. Keep release acceptance and engineering verification separate.

| Engineering thread | Proposed architecture content | Evidence focus |
| --- | --- | --- |
| Hazardous event / safety goal | Item context and modes | Justified event classification |
| FSR / TSR / HSR / SSR | Requirement decomposition/allocation | Preserved meaning, timing, ownership |
| Independence | Components, resources, fault paths | Dependent failure/interference analysis |
| Perception insufficiency | Scenario/ODD and function limits | Triggering-condition validation |
| Cybersecurity control | Trust boundary and interface | Attack-path coverage and lifecycle |
| Production/field assumption | Configuration and support process | Manufacturing and monitoring evidence |

Capella or SysML content can carry this trace; a DOORS baseline can carry requirements; simulation and vehicle tests supply scoped evidence. Confirm profile/version and export semantics before relying on model-generated records.

Review pressure points: implausible controllability/exposure; unallocated safety goals; decomposition without independence; optimistic timing; unsupported diagnostic coverage; conflation of SOTIF and malfunction safety; platform labels used as safety proof; field/maintenance assumptions absent from the evidence plan.
