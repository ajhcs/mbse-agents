# RF-protection and sequence-validation controls: next evidence campaign

Lifecycle: **drafted procedure**. These activities have not executed. The [current model study](report.md) is the executed evidence; its event meanings, parameters and physical implications require the challenges below.

Before execution, identify the implementation and instrument configuration, operating scenario, observation points, stimulus timing, oracle and numerical acceptance limits. Where a requirement leaves a deadline or safe state unresolved, record that decision before assigning a result. Preserve failed trials and configuration changes.

| Challenge | Procedure | Observation and decision | Current boundary |
| --- | --- | --- | --- |
| Sequence-check boundary | Present declared valid and invalid command sequences, then inject faults downstream of the verifier at the modeled DAC/amplifier boundaries. | Retain sequence properties, solver outcomes and independently observed RF values. Do not credit sequence precheck for downstream hardware faults. | Only protection logic has been enumerated; no sequence solver or RF plant has run here. |
| Shared protection cause | Identify shared references, power, sensors, configuration and actuation resources between limiter and comparator; challenge each actual common resource. | Capture both trip decisions and the protection output at independent points. Retain failures that bypass claimed separation. | BE8 represents an explicit dependency hypothesis, not established physical independence. |
| Passive attenuation envelope | Define frequency, input power, temperature, assembly tolerance and damage conditions for the intended attenuation path. | Measure delivered power and thermal response over that declared envelope. Record bypasses, failed parts and conditions beyond the verified limit. | BE7 appears in every derived cut; this credit cannot be unconditional. |
| Integrity and coverage allocation | Enumerate the protection functions and fault population; determine applicable framework, demand mode, risk criterion and required reduction. | Derive diagnostic coverage using justified weights and executed detection observations. Trace every claimed property to a model, test or reviewed argument. | The retained SIL proposals and detection percentages are hypotheses, not achieved integrity or measured coverage. |

Retain input/replay bytes, software/firmware and configuration hashes, instrument identity/calibration where applicable, raw observations, event timestamps, calculation/procedure version, expected and observed outcomes, exceptions and reviewer disposition. A rerun must preserve the prior evidence. Separate procedure execution, technical result, independent review and risk acceptance.

Use the [requirements](../requirements.md), [hazards and controls](../hazard-analysis.md), [trace records](../traceability.md), and [source review](../source-review.md) to determine the final scope and obligations.
