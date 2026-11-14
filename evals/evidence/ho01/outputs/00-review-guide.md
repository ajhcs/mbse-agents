# Greenhouse vent controller — review guide

Revision: GH-DRAFT-01. Prepared: 2026-10-12. Status: review draft; no requirement, architecture, result, or design decision is approved by this packet.

## Deliverables

- [Requirements](01-requirements.md): source-grounded obligations, provisional derived requirements, acceptance gaps and allocations.
- [Architecture](02-architecture.md): boundary, functions, components, modes, interfaces, alternatives and timing dependencies.
- [Verification and validation plan](03-verification-plan.md): planned activities, acceptance conditions, configuration and evidence records.
- [Traceability and decisions](04-trace-and-decisions.md): bidirectional source coverage, dependencies, risks and decisions needed for a final design.
- [Artifact checks](05-artifact-checks.md): actual local document checks and their limited scope.

These are textual proposals. No live model was changed, no controller was implemented, and no operational test, simulation, proof, reliability study or certification was executed. There are no supplied test results or supplier reliability data. Proposed future evidence locations in the plan do not denote existing results.

## Input and provenance

Only `../request.md` and the three packet skills and their referenced contracts were used. Raw source IDs are retained below and throughout the deliverables. The unlabeled candidate-design paragraph and manager proposal are cited by locator, not given invented raw source IDs. Artifact IDs such as RQ-01, F-01 and D-01 are local draft identifiers.

### Raw stakeholder input

Source locator: `../request.md`, paragraph beginning `N-01 Owner:`. The following wording is retained verbatim:

> N-01 Owner: Open the vent when a valid inside-temperature reading stays at or above 32 deg C for 30 s. A brief dip below 32 resets the interval. Close below 28 deg C after 60 s. N-02 Technician: A local manual stop overrides motion; resuming automatic mode requires an explicit action. N-03 Maintenance: If data is missing for 5 s, stop motion and show a fault; do not automatically resume motion after data returns. N-04 Owner: We want remote access, but the local stop must work during network failure.

### Raw candidate and uncertainty input

Source locator: `../request.md`, paragraph beginning `Candidate design:`. The following wording is retained verbatim:

> Candidate design: temperature samples nominally every 1 s over a shared network, one MCU, one motor driver, end switches, dashboard. Unknown: sample jitter, motor travel time, stale-data detection, operator response, wind/rain constraints and safe position. A manager proposes a universal 50 ms stop deadline without a source. There are no test results or supplier reliability data.

The candidate component list is a design input, not an approved requirement baseline. Nominal 1 s sampling is not a maximum interval or an end-to-end latency bound. The unsupported 50 ms proposal is not used as a deadline or acceptance limit.

## Review disposition

The requirement register contains 10 source-grounded draft records and 2 provisional derived records. All 12 have planned verification links; this is planning coverage only. The plan contains 14 verification activities and 4 stakeholder-validation activities, all planned, with execution, review and acceptance absent. The decision register contains D-01 through D-12. It locates incomplete acceptance criteria instead of supplying unsupported limits.

Immediate review priorities are D-01/D-02 (temperature qualification), D-03/D-04 (restart and local stop), D-05/D-06 (data loss and fault indication), and D-08/D-09 (movement and weather hazards). Remote scope and timing/reliability evidence also need resolution. The work can proceed as a draft; approval, firmware completion and physical acceptance require those decisions and measured evidence.

Execution environment: inherited Windows/PowerShell workspace. Host identity beyond the supplied environment, actual model identity, and actual model settings were unavailable to this exercise and are recorded as **unknown**. No model identity was inferred from tool documentation. No network, model API, credential, publication or live application mutation was used.
