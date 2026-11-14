# Safety Goals and Functional Safety Concept

Record: **EVD-026**. System: **Autonomous Emergency Braking System**. Lifecycle: **Drafted**. Configuration: versioned teaching document. Review: **not yet independently assessed**. Acceptance: **not granted**.

## Purpose and scope

This record identifies the current proposed requirement subset and its review obligations. The linked canonical baseline remains authoritative; the selected statements below are a review view, not a separately approved specification.

| Requirement | Proposed statement |
| --- | --- |
| REQ-SAF-001 | The AEB system shall detect at least 95% of relevant obstacles (vehicles, pedestrians, cyclists) within the operational design domain using dual-sensor (camera + radar) fusion, and the probability of undetected obstacle leading to collision shall not exceed 1 x 10^-8 per hour of operation. |
| REQ-SAF-002 | The sensor fusion algorithm shall require confirmation from at least one sensor source (camera or radar) with a track history of at least 3 cycles before accepting an object as valid for braking decisions. |
| REQ-SAF-003 | The AEB system shall limit false positive braking activations (braking when no collision threat exists) to fewer than 1 event per 100,000 km of driving under representative traffic conditions. |
| REQ-SAF-004 | The Braking Control ECU shall achieve the commanded deceleration within 150 ms of brake command receipt for full emergency braking (TTC <= 0.8 s). |
| REQ-SAF-005 | The AEB system shall coordinate with the ESC system such that ESC stability corrections take precedence over AEB deceleration commands when the ESC detects loss of vehicle stability. |
| REQ-SAF-006 | The end-to-end latency from camera frame capture to brake pressure rise initiation shall not exceed 300 ms under worst-case processing conditions. |
| REQ-SAF-007 | The AEB system shall automatically release braking intervention within 3 seconds of the braking trigger, or when the object tracker confirms the collision threat has cleared, whichever occurs first. |
| REQ-SAF-008 | The Braking Control ECU shall achieve a single-point fault metric (SPFM) of not less than 99% and a latent fault metric (LFM) of not less than 90% for the braking actuation path, verified by quantitative hardware fault analysis per ISO 26262-5. |
| REQ-SAF-009 | When the AEB system operates in MODE-003 (Degraded Perception), the system shall extend TTC warning and braking thresholds by a factor of 1.5 and shall limit AEB operating speed to 80 km/h. |
| REQ-SAF-010 | The AEB system shall monitor sensor fusion confidence continuously and shall transition to MODE-003 when the aggregate fusion confidence drops below 60% for more than 500 ms, indicating a SOTIF triggering condition. |

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
