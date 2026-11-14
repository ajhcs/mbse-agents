# Ariane 501: requalify reused assumptions

**HG-04 · 1996 · space · failure**

A reused component brings an operating envelope and inactive-looking functions that still require explicit disposition.

All `HG-` identifiers are new teaching identifiers. Historical facts below
are attributed to sources; the boundary, decisions, artifact, questions, and
transfer exercise are newly authored. No local historical simulation was performed.

## Source-grounded facts

- **HG-04-F1:** ESA reported simultaneous failure of both inertial reference systems and loss of guidance information during the initial flight. [HG-04-S1](https://www.esa.int/Newsroom/Press_Releases/Ariane_501_-_Presentation_of_Inquiry_Board_report); Inquiry findings on flight sequence.
- **HG-04-F2:** An alignment function needed before launch remained active afterward; testing did not sufficiently represent the complete flight-control system and its operating context. [HG-04-S1](https://www.esa.int/Newsroom/Press_Releases/Ariane_501_-_Presentation_of_Inquiry_Board_report); Inquiry findings on alignment function and simulations.

## Retrospective systems analysis

**Boundary.** Inherited inertial software, flight trajectory, redundancy, diagnostics, guidance consumers, and integrated qualification form the reuse boundary.

**Interfaces to examine**

- New mission envelope → reused software: inherited validity assumptions need comparison with new trajectories.
- Inertial system → guidance: failure indications must not become plausible control inputs.

**Decision.** What is the acceptance basis for a component already used successfully elsewhere?

- Accept previous flight history as sufficient.
- Compare old and new envelopes, remove or justify unused functions, and qualify integrated behavior.

**Teaching recommendation.** Make every inherited assumption either demonstrated, changed, or explicitly unresolved.

**Uncertainty.** A software-only test cannot establish complete vehicle behavior; this gallery does not reproduce the original flight dynamics.

## HG-04-A1: Reuse assumption ledger

This proposed artifact is a compact starting point for review. Its evidence
requests are unexecuted; its rows are not recovered project requirements.

| Item | Proposed disposition | Evidence to seek |
| --- | --- | --- |
| Operating envelope | List new inputs and modes outside prior experience | Representative trajectory and boundary tests |
| Retained function | Justify post-transition execution or disable it | Mode-transition verification |
| Redundant channels | Identify common software and input dependencies | Common-cause analysis and fault-response evidence |

## Practice engineering judgment

1. Why can two redundant units fail together?
2. Which evidence from the earlier system transfers, and which must be renewed?
3. Explain a reuse qualification gap without describing all legacy software as unsafe.

**Reasoning signals for a formative review**

- Tests assumptions rather than relying on the component name or reputation.
- Connects common inputs and code to correlated failure.
- Defines a bounded acceptance claim and unresolved integration evidence.

**Transfer exercise.** Synthetic: reuse a navigation service on a faster vehicle. Create three assumption-delta entries before choosing tests.

**Limits.** The artifact is a teaching synthesis of an official summary, not the original inquiry’s complete causal analysis.

## Sources and access

- **HG-04-S1: [Ariane 501 — Presentation of Inquiry Board report](https://www.esa.int/Newsroom/Press_Releases/Ariane_501_-_Presentation_of_Inquiry_Board_report)**
  — 1996-07-23; contemporaneous official inquiry summary.
  Locator: Inquiry findings paragraphs on inertial systems, alignment function, and testing.
  Relevant content inspected 2026-11-13. ESA’s contemporaneous summary was inspected; the full inquiry report is not the evidence used here. Numeric conversion details are deliberately not reconstructed.

[Structured case record](analysis.json) · [Gallery](../README.md) · [Source register](../../../docs/sources-historical.md)
