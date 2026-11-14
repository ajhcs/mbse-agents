# Safety Requirements Specification

Record: **EVD-021**. System: **Quantum Processor Control System**. Lifecycle: **Drafted**. Configuration: versioned teaching document. Review: **not yet independently assessed**. Acceptance: **not granted**.

## Purpose and scope

This record identifies the current proposed requirement subset and its review obligations. The linked canonical baseline remains authoritative; the selected statements below are a review view, not a separately approved specification.

| Requirement | Proposed statement |
| --- | --- |
| REQ-SAF-001 | The QPCS shall enforce a maximum RF output power of -20 dBm at the cryostat input flange via a hardware power limiter that operates independently of all software, with a response time of not more than 10 us from limit exceedance to output suppression. |
| REQ-SAF-002 | The QPCS shall detect RF power limiter trip events and shall inhibit all RPG output channels within 100 ms of trip detection, requiring explicit operator acknowledgment before resuming RF output. |
| REQ-SAF-003 | The QPCS shall enforce a maximum flux bias current of 10 mA per channel via a hardware current limiter that operates independently of all software, with a response time of not more than 10 us from limit exceedance to current clamping. |
| REQ-SAF-004 | The QPCS shall detect flux bias current limiter trip events and shall set all FBC channels to zero current within 100 ms of trip detection, requiring explicit operator acknowledgment before resuming flux bias output. |
| REQ-SAF-005 | The calibration automation software shall request Safety Monitor approval before setting any RF power or flux bias parameter that exceeds 80% of the hardware limit, and the Safety Monitor shall validate the requested parameter against the authorized calibration range before granting approval. |
| REQ-SAF-006 | The safety PLC shall execute a diagnostic self-test cycle at least once per second and shall transition the system to a safe state (all RF output inhibited, all flux bias set to zero) if the self-test detects any internal fault. |
| REQ-SAF-007 | The safety interlock module shall achieve a probability of dangerous failure on demand (PFDavg) of not more than 1 x 10^-2, consistent with IEC 61508 SIL 2 for a low-demand safety function. |
| REQ-SAF-008 | The analog comparator trip circuits shall operate on independent analog sense points, with no shared sensing path with the control system measurements, and shall function correctly with the safety PLC in a faulted state. |
| REQ-SAF-009 | The QPCS shall transition to a safe state (MODE-003 equivalent: all RF inhibited, all flux bias zeroed) within 200 ms of detecting loss of communication with the safety PLC. |
| REQ-SAF-010 | The QPCS shall log all safety interlock trip events, calibration parameter changes, and safety limit modifications in a tamper-evident audit log with timestamps traceable to the system clock. |

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
