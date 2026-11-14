# Software Design Description (SDD)

Record: **EVD-032**. System: **Integrated Flight Management System**. Lifecycle: **Drafted**. Configuration: versioned teaching document. Review: **not yet independently assessed**. Acceptance: **not granted**.

## Purpose and scope

This draft describes the existing architecture view and the evidence required to qualify it. Follow functions through allocated components and the declared external/internal interfaces. Preserve direction, units, timing origins, validity, ownership and failure/recovery semantics. Treat diagrams and tables as coordinated views of the same proposed entities.

Review dependency boundaries explicitly: separate processors, process groups, tools or sensors may still share specifications, power, clocks, data and operating conditions. The executed HZ-001 model documents selected common-cause and barrier counterexamples. Reconcile each changed design decision with its requirements, hazards and verification procedures before advancing the baseline.

Interface closure requires agreement with the actual external provider and observation at both endpoints. The current textual views do not establish a live-tool model, implementation conformance, supplier commitment or acceptance.

## Connected evidence

- [Requirement baseline](../../requirements.md)
- [Architecture and interfaces](../../architecture.md)
- [Hazard and control analysis](../../hazard-analysis.md)
- [Trace and planned verification](../../traceability.md)
- [Executed HZ-001 model evidence](../../analysis/report.md)
- [Candidate source/applicability register](../../source-review.md)

## Decisions still required

Identify the real system configuration and adopted process; validate assumptions against representative operating data; assign accountable reviewers and acceptance authority; obtain missing physical, supplier and human-performance evidence. The draft is available for review now; those decisions are not implied by its existence.
