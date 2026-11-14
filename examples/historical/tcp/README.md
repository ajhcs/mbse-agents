# TCP: define what an acknowledgment means

**HG-15 · 1981 · communications computing · design baseline**

A useful interface states both the service it provides and the stronger claims it does not establish.

All `HG-` identifiers are new teaching identifiers. Historical facts below
are attributed to sources; the boundary, decisions, artifact, questions, and
transfer exercise are newly authored. No local historical simulation was performed.

## Source-grounded facts

- **HG-15-F1:** RFC 793 describes reliable ordered delivery using sequence numbers, acknowledgments, retransmission, and receive windows. [HG-15-S1](https://www.rfc-editor.org/rfc/rfc793.txt); Section 2.6, pp. 9–10.
- **HG-15-F2:** It explicitly distinguishes receiving-TCP responsibility from delivery to the end user when describing acknowledgment semantics. [HG-15-S1](https://www.rfc-editor.org/rfc/rfc793.txt); Section 2.6, p. 10.

## Retrospective systems analysis

**Boundary.** Application sender, transport endpoints, network, receiving application, and any durable business operation must be distinguished.

**Interfaces to examine**

- Transport → application: receipt by a transport endpoint is weaker than application processing or durable commit.
- Application retry → remote operation: retry semantics require an application-level decision.

**Decision.** Can a transport acknowledgment close a claim that a business operation completed?

- Treat receipt as completion.
- Define an application result and recovery protocol with separate durability and duplicate-handling claims.

**Teaching recommendation.** State the acceptance boundary in the vocabulary of the stakeholder’s operation.

**Uncertainty.** The historical protocol alone does not establish exactly-once processing, persistent storage, or operator acknowledgment.

## HG-15-A1: Layered acknowledgment contract

This proposed artifact is a compact starting point for review. Its evidence
requests are unexecuted; its rows are not recovered project requirements.

| Item | Proposed disposition | Evidence to seek |
| --- | --- | --- |
| Transport receipt | Bytes accepted by the receiving transport | Protocol-level observation |
| Application acceptance | Request parsed and accepted for a named operation | Application response with request identity |
| Durable outcome | Committed or explicitly unresolved after interruption | Recovery query and duplicate-handling evidence |

## Practice engineering judgment

1. Which stronger claims are often smuggled into the word delivered?
2. What should a client do when an operation times out after possibly completing?
3. Explain acknowledgment semantics to a non-network stakeholder in two sentences.

**Reasoning signals for a formative review**

- Separates receipt, processing, persistence, and business outcome.
- Identifies ambiguity without promising exactly-once semantics.
- Places evidence at the layer responsible for the claim.

**Transfer exercise.** Synthetic: an industrial controller receives a command over a reliable connection. Define the acknowledgments needed before an operator can claim the physical action occurred.

**Limits.** No networking benchmark or current protocol compliance test was run. The artifact is an application-level teaching proposal.

## Sources and access

- **HG-15-S1: [RFC 793, Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc793.txt)**
  — 1981-09; original specification.
  Locator: Sections 1.4–1.5, 2.4, and 2.6; section 3.9.
  Relevant content inspected 2026-11-13. Historical specification, subsequently superseded. This case studies the 1981 service boundary, not current TCP implementation requirements.

[Structured case record](analysis.json) · [Gallery](../README.md) · [Source register](../../../docs/sources-historical.md)
