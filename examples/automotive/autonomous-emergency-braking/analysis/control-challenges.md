# Emergency-braking perception and fusion controls: next evidence campaign

Lifecycle: **drafted procedure**. These activities have not executed. The [current model study](report.md) is the executed evidence; its event meanings, parameters and physical implications require the challenges below.

Before execution, identify the implementation and instrument configuration, operating scenario, observation points, stimulus timing, oracle and numerical acceptance limits. Where a requirement leaves a deadline or safe state unresolved, record that decision before assigning a result. Preserve failed trials and configuration changes.

| Challenge | Procedure | Observation and decision | Current boundary |
| --- | --- | --- | --- |
| Single observation path loss | Replay the same labeled scenario with camera omissions and then radar omissions, preserving timestamps and target reference state. | Record fused tracks, confidence, decision latency and proposed degraded behavior; compare each case with the intact replay. | The model assumes particular missed-detection paths; it does not establish a perception operating envelope. |
| Common environment | Construct a declared set of scenes or recorded stimuli in which both modalities degrade; retain the scene parameters and labeling method. | Record correlated omissions and false detections. Do not multiply marginal sensor error estimates without a justified dependence model. | BE8 explicitly preserves this common cause; synthetic scenarios estimate no fleet rate. |
| Fusion fault despite useful sensors | Supply useful sensor tracks and inject a dropped, stale, misassociated or rejected fused track at a documented processing boundary. | Use an independent replay oracle for object and timing truth; observe the collision decision and degraded indication. | A redundant sensor pair does not eliminate the separate fusion path identified in the cut sets. |
| Timing and interference | Load the selected processing/communication paths while replaying the declared observation cases; include restart and timeout boundaries. | Measure each latency segment against the proposed 300 ms end-to-end allocation and explicitly account for the unallocated 80 ms margin. | This is a planned computational/platform campaign; vehicle stopping response needs separate representative testing. |

Retain input/replay bytes, software/firmware and configuration hashes, instrument identity/calibration where applicable, raw observations, event timestamps, calculation/procedure version, expected and observed outcomes, exceptions and reviewer disposition. A rerun must preserve the prior evidence. Separate procedure execution, technical result, independent review and risk acceptance.

Use the [requirements](../requirements.md), [hazards and controls](../hazard-analysis.md), [trace records](../traceability.md), and [source review](../source-review.md) to determine the final scope and obligations.
