# Infusion-pump delivery and clamp controls: next evidence campaign

Lifecycle: **drafted procedure**. These activities have not executed. The [current model study](report.md) is the executed evidence; its event meanings, parameters and physical implications require the challenges below.

Before execution, identify the implementation and instrument configuration, operating scenario, observation points, stimulus timing, oracle and numerical acceptance limits. Where a requirement leaves a deadline or safe state unresolved, record that decision before assigning a result. Preserve failed trials and configuration changes.

| Challenge | Procedure | Observation and decision | Current boundary |
| --- | --- | --- | --- |
| Running but wrong output | Exercise a nonclinical controller harness with a wrong delivery command while processor liveness service continues. | Observe watchdog service, independent flow/drive limit and stop request. Keep liveness and correctness observations separate. | The static model rejects watchdog sufficiency for this path; no fluid delivery is simulated. |
| Shared sensing and drive paths | Map the real sensor and limiter dependencies, then inject declared under-reading and shared-drive faults at their actual interfaces. | Capture command, sensor, independent reference and limiter action separately; identify where a single fault affects both initiation and protection. | The model reuses BE3/BE7 rather than treating repeated use as independent faults. |
| Clamp timing and physical meaning | Repeat the temporal study conditions on an appropriate nonclinical bench using representative tubing, supply, temperature, orientation and wear. | Measure release signal, displacement, occlusion and delivered volume with independent instruments. Compare each observable with its adopted threshold; a closed Boolean state is insufficient. | Logical timing is executed; mechanical closure and dose consequences remain planned. |
| Fault recovery policy | Distinguish primary AC loss bridged by battery from actual hold-open supply loss; exercise latch, restart and manual-rearm cases. | Reconcile REQ-PRF-004 with the proposed latch policy. Define when continuation is permitted and demonstrate that door-open rearm is inhibited. | No usability review or accepted recovery policy is supplied; preserve the model counterexamples. |

Retain input/replay bytes, software/firmware and configuration hashes, instrument identity/calibration where applicable, raw observations, event timestamps, calculation/procedure version, expected and observed outcomes, exceptions and reviewer disposition. A rerun must preserve the prior evidence. Separate procedure execution, technical result, independent review and risk acceptance.

Use the [requirements](../requirements.md), [hazards and controls](../hazard-analysis.md), [trace records](../traceability.md), and [source review](../source-review.md) to determine the final scope and obligations.
