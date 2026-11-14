# Herald of Free Enterprise: close the loop between physical state and permission

**HG-14 · 1987 · maritime · failure**

A safety-critical departure condition needs observable state, accountable confirmation, and a response to unknown or failed indication.

All `HG-` identifiers are new teaching identifiers. Historical facts below
are attributed to sources; the boundary, decisions, artifact, questions, and
transfer exercise are newly authored. No local historical simulation was performed.

## Source-grounded facts

- **HG-14-F1:** The court found that the ferry went to sea with its bow doors open and examined both individual duties and management failures. [HG-14-S1](https://assets.publishing.service.gov.uk/media/54c1704ce5274a15b6000025/FormalInvestigation_HeraldofFreeEnterprise-MSA1894.pdf); Paragraph 10; paragraphs 14–18.
- **HG-14-F2:** Requests for bridge door indication preceded the accident; the report discussed fail-safe indication, procedures, and berth arrangements. [HG-14-S1](https://assets.publishing.service.gov.uk/media/54c1704ce5274a15b6000025/FormalInvestigation_HeraldofFreeEnterprise-MSA1894.pdf); Paragraph 18; paragraphs 28–30.

## Retrospective systems analysis

**Boundary.** Doors, sensing, bridge display, crew responsibilities, berth geometry, departure authority, and shore management form the departure-control system.

**Interfaces to examine**

- Door state → bridge: absence of a reported problem is not a positive closed-and-secured indication.
- Crew improvement request → management: safety significance needs tracked disposition and feedback.

**Decision.** How should an unknown door state affect departure permission?

- Assume completion unless a problem is reported.
- Require positive confirmation and define the response to failed or contradictory indication.

**Teaching recommendation.** Review the physical condition, reporting loop, and harbor transition together.

**Uncertainty.** An indicator is also fallible; its diagnostic coverage and procedures need evidence rather than an assumption of perfection.

## HG-14-A1: Departure condition contract

This proposed artifact is a compact starting point for review. Its evidence
requests are unexecuted; its rows are not recovered project requirements.

| Item | Proposed disposition | Evidence to seek |
| --- | --- | --- |
| Required condition | Define closed and secured separately from command issued | Physical confirmation and sensing basis |
| Unknown state | Make failed indication visible and assign a response | Fault injection and crew scenario evidence |
| Improvement request | Record safety consequence, decision, and completion | Owner acknowledgment and installation verification |

## Practice engineering judgment

1. What is the difference between no alarm and confirmed readiness?
2. How could a berth interface constrain a safe departure sequence?
3. Write a technical response to a crew suggestion that makes its disposition accountable.

**Reasoning signals for a formative review**

- Models positive confirmation and loss of feedback.
- Includes both vessel and port interfaces.
- Treats reporting culture as part of the control process.

**Transfer exercise.** Synthetic: a loading system starts motion after a remote operator assumes a guard is closed. Draft its permission states and unknown-state response.

**Limits.** The proposed contract is not a recovered ship specification. No stability or flooding calculation is supplied.

## Sources and access

- **HG-14-S1: [Formal Investigation, mv Herald of Free Enterprise, Report of Court No. 8074](https://assets.publishing.service.gov.uk/media/54c1704ce5274a15b6000025/FormalInvestigation_HeraldofFreeEnterprise-MSA1894.pdf)**
  — 1987; original investigation.
  Locator: Front matter (publication and addendum); paragraphs 10, 14–18, and 28–30.
  Relevant content inspected 2026-11-13. The scanned copy states first published 1987 and third impression 1988. Its September 1987 addendum corrects attribution in paragraph 19.6; that addendum date is not the original publication date. Fatality counts vary between this contemporary report and later official summaries; no count is used here.

[Structured case record](analysis.json) · [Gallery](../README.md) · [Source register](../../../docs/sources-historical.md)
