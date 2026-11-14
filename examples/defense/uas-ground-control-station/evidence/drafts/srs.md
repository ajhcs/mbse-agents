# System Requirements Specification (SRS)

Record: **EVD-021**. System: **UAS Ground Control Station**. Lifecycle: **Drafted**. Configuration: versioned teaching document. Review: **not yet independently assessed**. Acceptance: **not granted**.

## Purpose and scope

This record identifies the current proposed requirement subset and its review obligations. The linked canonical baseline remains authoritative; the selected statements below are a review view, not a separately approved specification.

| Requirement | Proposed statement |
| --- | --- |
| REQ-FUN-001 | The GCS shall allow the operator to create a mission plan consisting of up to 500 waypoints with defined leg types, loiter patterns, and altitude constraints per STANAG 4586. |
| REQ-FUN-002 | The GCS shall validate each mission plan leg for airspace deconfliction, terrain clearance, and fuel feasibility before transmitting the plan to the air vehicle. |
| REQ-FUN-003 | The GCS shall display air vehicle state (position, altitude, heading, airspeed, engine status, fuel state) on the operator display with a refresh rate of not less than 10 Hz. |
| REQ-FUN-004 | The GCS shall transmit flight commands (waypoint changes, heading, altitude, airspeed) to the air vehicle with an end-to-end latency of not more than 250 ms from operator input to C2 link transmission. |
| REQ-FUN-005 | The GCS shall support simultaneous control of up to four Group 4/5 air vehicles with independent mission plans, C2 links, and sensor tasking. |
| REQ-FUN-006 | The GCS shall detect loss of all C2 links to an air vehicle within 10 seconds of the last valid telemetry receipt and shall declare lost link status. |

For each record, establish a source and rationale, operating conditions, measurable acceptance criterion, allocation and verification intent. Check compound statements and parent/derived meaning. A numeric teaching target does not become a regulatory obligation through trace linkage. All physical satisfaction claims remain open.

## Connected evidence

- [Requirement baseline](../../requirements.md)
- [Architecture and interfaces](../../architecture.md)
- [Hazard and control analysis](../../hazard-analysis.md)
- [Trace and planned verification](../../traceability.md)
- [Executed HZ-001 model evidence](../../analysis/report.md)
- [Candidate source/applicability register](../../source-review.md)

## Decisions still required

Identify the real system configuration and adopted process; validate assumptions against representative operating data; assign accountable reviewers and acceptance authority; obtain missing physical, supplier and human-performance evidence. The draft is available for review now; those decisions are not implied by its existence.
