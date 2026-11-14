# Therac-25: treat interaction timing and hazard communication as design concerns

**HG-18 · 1987 · medical devices · failure**

A credible safety argument must account for temporal interactions, operator feedback, and what users are told when a defect is found.

All `HG-` identifiers are new teaching identifiers. Historical facts below
are attributed to sources; the boundary, decisions, artifact, questions, and
transfer exercise are newly authored. No local historical simulation was performed.

## Source-grounded facts

- **HG-18-F1:** The authors describe a race condition involving rapid edits and interacting software tasks, not simply an incorrect static input value. [HG-18-S2](https://web.mit.edu/6.033/2004/wwwdocs/papers/Therac_3.html); Opening race-condition discussion.
- **HG-18-F2:** They report that the FDA objected to an initial corrective notification because it failed to explain the defect, associated hazard, and urgency. [HG-18-S2](https://web.mit.edu/6.033/2004/wwwdocs/papers/Therac_3.html); Government and user response.

## Retrospective systems analysis

**Boundary.** Treatment prescription, software tasks, beam configuration, interlocks, operator display, patient feedback, manufacturer, and clinical users form the safety system.

**Interfaces to examine**

- Operator editing → control state: valid individual actions can form an unsafe temporal sequence.
- Manufacturer → clinical user: corrective instructions need a truthful hazard explanation and clear scope.

**Decision.** What evidence supports a corrective release after a timing-dependent fault?

- Patch the observed input sequence and send brief workaround instructions.
- Reassess interacting states, independent protection, user feedback, and the complete corrective communication.

**Teaching recommendation.** Require mechanism-focused tests and a bounded safety claim for the changed system.

**Uncertainty.** A reproduced software fault does not establish all contributing conditions or prove the resulting clinical system safe.

## HG-18-A1: Corrective-action evidence slice

This proposed artifact is a compact starting point for review. Its evidence
requests are unexecuted; its rows are not recovered project requirements.

| Item | Proposed disposition | Evidence to seek |
| --- | --- | --- |
| Interaction timing | Exercise edits at relevant state boundaries | Reproducible event traces and independent review |
| Protection | Identify safeguards independent of the faulty path | Failure-mode evidence and coverage limits |
| User notification | Explain hazard, affected configuration, action, and urgency | Readable instructions reviewed with representative users |

## Practice engineering judgment

1. Why do static input tests miss temporal hazards?
2. What must a defect notice say beyond the workaround?
3. How would you communicate uncertain accident details without dismissing a credible safety signal?

**Reasoning signals for a formative review**

- Examines shared state, scheduling, and feedback.
- Separates root-cause reproduction from overall safety acceptance.
- Communicates hazard and uncertainty without minimizing either.

**Transfer exercise.** Synthetic: a therapy-planning interface allows rapid mode edits while configuration is pending. Define a test plan and a hypothetical user notice; do not prescribe patient treatment.

**Limits.** No clinical advice, medical-device certification, or simulated radiation exposure is provided. The original authors’ uncertainty is retained.

## Sources and access

- **HG-18-S1: [Leveson and Turner, An Investigation of the Therac-25 Accidents, Part I](https://web.mit.edu/6.033/2004/wwwdocs/papers/Therac_1.html)**
  — 1993-07; original author investigation.
  Locator: Introduction and investigation limitations.
  Relevant content inspected 2026-11-13. Original investigators’ article, reprinted with permission from IEEE Computer 26(7), pp. 18–41. It explicitly notes uncertain details and the absence of a single official commission report.
- **HG-18-S2: [An Investigation of the Therac-25 Accidents, Part III](https://web.mit.edu/6.033/2004/wwwdocs/papers/Therac_3.html)**
  — 1993-07; original author investigation.
  Locator: Race-condition discussion; Government and user response.
  Relevant content inspected 2026-11-13. Same article as Part I; one underlying publication. Regulatory descriptions are historical and are not current regulatory guidance.

[Structured case record](analysis.json) · [Gallery](../README.md) · [Source register](../../../docs/sources-historical.md)
