# Hardware Requirements Specification (HRS)

Record: **EVD-031**. System: **Integrated Flight Management System**. Lifecycle: **Drafted**. Configuration: versioned teaching document. Review: **not yet independently assessed**. Acceptance: **not granted**.

## Purpose and scope

This record identifies the current proposed requirement subset and its review obligations. The linked canonical baseline remains authoritative; the selected statements below are a review view, not a separately approved specification.

| Requirement | Proposed statement |
| --- | --- |
| REQ-FUN-001 | The FMS shall allow the flight crew to create a lateral flight plan consisting of up to 250 waypoints with defined leg types per ARINC 424. |
| REQ-FUN-002 | The FMS shall allow modification of the active flight plan during flight without interrupting guidance output for more than one guidance computation cycle (50 ms). |
| REQ-FUN-003 | The FMS shall accept and process uplinked flight plan amendments received via the FANS datalink interface within 5 seconds of message receipt. |
| REQ-FUN-004 | The FMS shall validate each flight plan leg for performance feasibility before sequencing the leg as active, and shall annunciate to the flight crew if a leg exceeds aircraft performance capabilities. |
| REQ-FUN-005 | The FMS shall compute aircraft position using multi-sensor fusion of IRS, GNSS, DME, and VOR inputs with a position update rate of not less than 50 Hz. |
| REQ-FUN-006 | The FMS shall output the computed position solution to the cross-channel comparator within 20 ms of sensor data receipt. |

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
