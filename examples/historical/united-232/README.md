# United 232: functional redundancy is not physical independence

**HG-09 · 1989 · aviation · failure with partial recovery**

Test redundant architecture against shared physical hazards and the operational capability remaining after damage.

All `HG-` identifiers are new teaching identifiers. Historical facts below
are attributed to sources; the boundary, decisions, artifact, questions, and
transfer exercise are newly authored. No local historical simulation was performed.

## Source-grounded facts

- **HG-09-F1:** The FAA describes an uncontained tail-engine fan-disk failure whose debris damaged all three hydraulic systems. [HG-09-S1](https://www.faa.gov/lessons_learned/transport_airplane/accidents/N1819U); Accident Overview; Airplane.
- **HG-09-F2:** The systems were functionally isolated but physically close in parts of the tail; the crew used wing-engine thrust to obtain limited control. [HG-09-S1](https://www.faa.gov/lessons_learned/transport_airplane/accidents/N1819U); Airplane; Flight Crew.

## Retrospective systems analysis

**Boundary.** Engines, debris zones, hydraulic routing, flight controls, crew coordination, airport options, and emergency response define the damaged-aircraft system.

**Interfaces to examine**

- Engine debris → multiple channels: a single event can cross logical redundancy boundaries.
- Remaining propulsion → crew control: residual authority may be difficult to use and insufficient for stable flight.

**Decision.** How should a redundancy claim be challenged?

- Count independent functional channels.
- Trace shared locations, supplies, controls, maintenance, and external hazards.

**Teaching recommendation.** Pair functional decomposition with a physical dependency review and degraded-operation evidence.

**Uncertainty.** Physical separation is one design choice; effectiveness depends on the hazard envelope and achievable residual control.

## HG-09-A1: Common-cause dependency review

This proposed artifact is a compact starting point for review. Its evidence
requests are unexecuted; its rows are not recovered project requirements.

| Item | Proposed disposition | Evidence to seek |
| --- | --- | --- |
| Three hydraulic channels | Map proximity and common exposure | Layout and credible debris-zone analysis |
| Residual control | State achievable tasks after shared damage | Representative handling evidence |
| Crew allocation | Assign navigation, control, communication, and cabin coordination | Observed workload and coordination evidence |

## Practice engineering judgment

1. Which diagram would reveal a weakness hidden by a logical block diagram?
2. What is the difference between having some control and meeting a landing requirement?
3. Write a qualified redundancy claim for a new design.

**Reasoning signals for a formative review**

- Identifies shared hazard exposure instead of multiplying nominal reliabilities.
- Defines residual capability in operational tasks.
- Recognizes human adaptation without turning it into a guaranteed design control.

**Transfer exercise.** Synthetic: three power channels share a service duct. Produce a common-cause review and compare relocation, shielding, and diverse backup.

**Limits.** No reliability probability, debris simulation, or claim that training alone would resolve the failure is made.

## Sources and access

- **HG-09-S1: [FAA Lessons Learned: United Airlines Flight 232, N1819U](https://www.faa.gov/lessons_learned/transport_airplane/accidents/N1819U)**
  — official retrospective; date not stated; official retrospective.
  Locator: Accident Overview; Airplane; Flight Crew.
  Relevant content inspected 2026-11-13. The FAA account was inspected. The original NTSB report URL was unavailable during curation; this case does not represent direct access to that report.

[Structured case record](analysis.json) · [Gallery](../README.md) · [Source register](../../../docs/sources-historical.md)
