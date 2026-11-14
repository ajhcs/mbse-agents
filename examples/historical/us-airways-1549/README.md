# US Airways 1549: model the decision-maker’s time

**HG-08 · 2009 · aviation · recovery**

Validate scenarios against the time and information available to the operator, including recognition and decision delays.

All `HG-` identifiers are new teaching identifiers. Historical facts below
are attributed to sources; the boundary, decisions, artifact, questions, and
transfer exercise are newly authored. No local historical simulation was performed.

## Source-grounded facts

- **HG-08-F1:** The investigation examined the loss of thrust in both engines after a bird encounter and the subsequent Hudson River ditching. [HG-08-S1](https://www.ntsb.gov/investigations/AccidentReports/Reports/AAR1003.pdf); Executive summary.
- **HG-08-F2:** Immediate-turn simulator attempts omitted recognition and decision time. The report describes one delayed return-to-LaGuardia attempt with a 35-second delay that did not succeed. [HG-08-S1](https://www.ntsb.gov/investigations/AccidentReports/Reports/AAR1003.pdf); Section 1.16.3, printed pp. 49–50; section 2.3.2; footnotes 88–89.

## Retrospective systems analysis

**Boundary.** Aircraft energy, available landing areas, crew cognition, procedures, air traffic control, cabin preparation, and rescue response form the emergency system.

**Interfaces to examine**

- Failure cues → crew action: detection, interpretation, decision, and execution consume time.
- Flight deck → cabin: protective preparation must fit the remaining time and information.

**Decision.** What does a favorable simulator outcome establish about an actual emergency choice?

- Treat the best trial as proof that a different choice was available.
- Compare initial state, information, delays, training, and outcome variability before transferring a result.

**Teaching recommendation.** Report scenario applicability before judging the historical decision.

**Uncertainty.** One delayed failed trial does not estimate a general success probability or prove all alternative paths impossible.

## HG-08-A1: Scenario applicability matrix

This proposed artifact is a compact starting point for review. Its evidence
requests are unexecuted; its rows are not recovered project requirements.

| Item | Proposed disposition | Evidence to seek |
| --- | --- | --- |
| Initial state | Match position, energy, damage, and environment | Validated reconstruction and uncertainty |
| Human timing | Include recognition and decision tasks | Observed timing or justified sensitivity range |
| Outcome claim | State which tested conditions support the conclusion | All attempts, failures, and exclusions |

## Practice engineering judgment

1. Why is immediate response a strong modeling assumption?
2. What evidence would be needed to estimate success probability?
3. Explain the difference between a possible trajectory and an available decision.

**Reasoning signals for a formative review**

- Includes information and action latency in the system model.
- Avoids extrapolating one run into a universal conclusion.
- Communicates the limits of counterfactual evidence.

**Transfer exercise.** Synthetic: an emergency controller proposes a recovery action that succeeds only with zero delay. Specify a fair comparison protocol.

**Limits.** Simulation results are attributed to the NTSB. This repository did not rerun the flight or conduct new pilot trials.

## Sources and access

- **HG-08-S1: [NTSB Aircraft Accident Report AAR-10/03](https://www.ntsb.gov/investigations/AccidentReports/Reports/AAR1003.pdf)**
  — 2010-05-04; original investigation.
  Locator: Section 1.16.3, Operational Factors and Human Performance Simulations, printed pp. 49–50; section 2.3.2; footnotes 88–89.
  Relevant content inspected 2026-11-13. Relevant sections inspected; this is not a reconstruction of every event or finding.

[Structured case record](analysis.json) · [Gallery](../README.md) · [Source register](../../../docs/sources-historical.md)
