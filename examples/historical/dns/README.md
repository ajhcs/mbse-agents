# DNS: distribute authority and manage stale information

**HG-16 · 1987 · communications computing · design baseline**

Scalability changes who owns data, how long others may reuse it, and what temporary disagreement means.

All `HG-` identifiers are new teaching identifiers. Historical facts below
are attributed to sources; the boundary, decisions, artifact, questions, and
transfer exercise are newly authored. No local historical simulation was performed.

## Source-grounded facts

- **HG-16-F1:** The design goals call for distributed maintenance and caching rather than collecting a continuously consistent copy of the entire database. [HG-16-S1](https://www.rfc-editor.org/rfc/rfc1034.txt); Section 2.2.
- **HG-16-F2:** The document places the trade among acquisition cost, update speed, and cache accuracy under control of the data source. [HG-16-S1](https://www.rfc-editor.org/rfc/rfc1034.txt); Section 2.2.

## Retrospective systems analysis

**Boundary.** Authoritative data owners, delegated zones, resolvers, caches, clients, and update operations form the naming system.

**Interfaces to examine**

- Authority → cache: reuse reduces load while retaining information that may become stale.
- Delegation → organization: a naming boundary is also an administrative responsibility boundary.

**Decision.** How should a team choose freshness behavior for a distributed lookup service?

- Demand instant global consistency without considering cost or failures.
- Choose an explicit reuse window and update plan consistent with the consumer’s tolerance for stale data.

**Teaching recommendation.** State authority, freshness, temporary-failure behavior, and rollback together.

**Uncertainty.** The acceptable window depends on the decision being supported; a historical design principle supplies no universal duration.

## HG-16-A1: Authority and freshness contract

This proposed artifact is a compact starting point for review. Its evidence
requests are unexecuted; its rows are not recovered project requirements.

| Item | Proposed disposition | Evidence to seek |
| --- | --- | --- |
| Ownership | Identify the authoritative owner and delegated scope | Zone or dataset ownership record |
| Reuse | State allowable age and conditions invalidating cached data | Consumer tolerance and measured update path |
| Failure | Distinguish unavailable answer from absent entity | Fault scenario and recovery behavior |

## Practice engineering judgment

1. Why is cached information useful even when it is not current everywhere?
2. Which organizational failure can defeat a technically valid delegation?
3. Explain a stale answer without incorrectly calling it fabricated data.

**Reasoning signals for a formative review**

- Makes consistency, availability, and operating cost explicit.
- Connects technical delegation to ownership and handover.
- Distinguishes freshness, authority, and truth.

**Transfer exercise.** Synthetic: a fleet stores remote configuration locally during disconnection. Define who owns it, when it expires, and what operations remain allowed.

**Limits.** No live DNS changes or experiments were performed; security requirements for a present-day deployment require separate current evidence.

## Sources and access

- **HG-16-S1: [RFC 1034, Domain Names — Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.txt)**
  — 1987-11; original specification.
  Locator: Sections 2.2–2.4, 4.2, and 5.2.3.
  Relevant content inspected 2026-11-13. The historical document has many later updates. Its design rationale is used here; it is not a complete current DNS deployment or security specification.

[Structured case record](analysis.json) · [Gallery](../README.md) · [Source register](../../../docs/sources-historical.md)
