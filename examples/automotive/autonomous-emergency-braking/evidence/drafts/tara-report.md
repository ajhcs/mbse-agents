# Cybersecurity TARA Report

Record: **EVD-029**. System: **Autonomous Emergency Braking System**. Lifecycle: **Drafted**. Configuration: versioned teaching document. Review: **not yet independently assessed**. Acceptance: **not granted**.

## Purpose and scope

This draft separates malicious alteration, unauthorised commands, unavailable communication, stale data and compromised update/configuration paths. Identify each asset, trust boundary, initiating access condition, affected safety function, preventive/detective control and recovery behavior. A signature verifies an authorised signer under key assumptions; it does not establish software correctness or safe clinical/operational behavior.

Review the proposed isolation boundaries under corrupt inputs, resource exhaustion and loss of authentication services. Carry each safety consequence into the hazard register and confirm that mitigation does not delay time-critical controls. Record key lifecycle, replay handling, privilege separation and configuration dependencies before assigning effectiveness.

## Connected evidence

- [Requirement baseline](../../requirements.md)
- [Architecture and interfaces](../../architecture.md)
- [Hazard and control analysis](../../hazard-analysis.md)
- [Trace and planned verification](../../traceability.md)
- [Detailed proposed threat analysis](../../cybersecurity.md)
- [Executed HZ-001 model evidence](../../analysis/report.md)
- [Candidate source/applicability register](../../source-review.md)

## Decisions still required

Identify the real system configuration and adopted process; validate assumptions against representative operating data; assign accountable reviewers and acceptance authority; obtain missing physical, supplier and human-performance evidence. The draft is available for review now; those decisions are not implied by its existence.
