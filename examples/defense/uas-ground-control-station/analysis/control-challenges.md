# Ground-station link-loss monitoring controls: next evidence campaign

Lifecycle: **drafted procedure**. These activities have not executed. The [current model study](report.md) is the executed evidence; its event meanings, parameters and physical implications require the challenges below.

Before execution, identify the implementation and instrument configuration, operating scenario, observation points, stimulus timing, oracle and numerical acceptance limits. Where a requirement leaves a deadline or safe state unresolved, record that decision before assigning a result. Preserve failed trials and configuration changes.

| Challenge | Procedure | Observation and decision | Current boundary |
| --- | --- | --- | --- |
| Separate link interruption | In an offline communications harness, interrupt the declared LOS and BLOS inputs separately, then together. | Record transport state, telemetry age, operator indication and monitoring timestamps against the adopted deadlines. | The top event is undetected ground-station link loss; this does not establish aircraft recovery behavior. |
| Shared station dependency | Inventory actual common power, routing, software and time resources; remove or corrupt each resource in the harness. | Observe both links and all monitors at independent capture points; retain cases in which apparent diversity provides no protection. | BE8 represents shared infrastructure, with no measured occurrence probability. |
| Stale data with apparent liveness | Replay old telemetry while keeping a heartbeat or transport session active; separately disturb the timestamp reference. | Compare freshness decisions with a separate capture clock and known send sequence. A live connection must not be treated as proof of fresh operational data. | BE9 captures a proposed monitoring dependency; the actual freshness logic remains to be verified. |
| Recovery transition | Restore one transport after declared loss and replay delayed messages across the restoration boundary. | Record indication clearance rules, ordering, duplicate handling and freshness. Require an explicit recovery policy before assigning pass/fail to that policy. | Human response and onboard lost-link behavior remain separate obligations. |

Retain input/replay bytes, software/firmware and configuration hashes, instrument identity/calibration where applicable, raw observations, event timestamps, calculation/procedure version, expected and observed outcomes, exceptions and reviewer disposition. A rerun must preserve the prior evidence. Separate procedure execution, technical result, independent review and risk acceptance.

Use the [requirements](../requirements.md), [hazards and controls](../hazard-analysis.md), [trace records](../traceability.md), and [source review](../source-review.md) to determine the final scope and obligations.
