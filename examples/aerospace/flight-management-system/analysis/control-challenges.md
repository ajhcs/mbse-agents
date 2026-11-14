# Flight-management guidance controls: next evidence campaign

Lifecycle: **drafted procedure**. These activities have not executed. The [current model study](report.md) is the executed evidence; its event meanings, parameters and physical implications require the challenges below.

Before execution, identify the implementation and instrument configuration, operating scenario, observation points, stimulus timing, oracle and numerical acceptance limits. Where a requirement leaves a deadline or safe state unresolved, record that decision before assigning a result. Preserve failed trials and configuration changes.

| Challenge | Procedure | Observation and decision | Current boundary |
| --- | --- | --- | --- |
| Equal but wrong outputs | Feed both channels the same incorrect guidance result through the declared navigation or database dependency; keep the equality comparator healthy. | Record reference guidance, both channel outputs, comparator decision and independent-monitor outputs. Agreement alone must not be credited as correctness. | The static study retains this counterexample; actual detection coverage and response time remain untested. |
| Comparator positive control | Inject a disagreement between channels while preserving the same monitor configuration. | Record whether the comparator reports disagreement within the deadline adopted from the current requirement. Keep this distinct from the equal-output case. | Establish the comparator path works before interpreting a missed common error. |
| Shared monitor dependency | Identify whether guidance generation and external monitoring consume the same navigation, database, time or power resource; inject a fault at each actual shared resource. | Record which channels and monitors remain trustworthy. Reclassify dependencies when the same stimulus defeats more than one barrier. | The authored BE9 represents a hypothesis to investigate, not measured common-cause frequency. |
| Operational detection scope | For each proposed crew or external warning-system credit, select representative flight phases and specific misleading-guidance classes from the safety assessment. | Predeclare what is observable, who detects it, the available response window and the safe response. Retain undetectable cases and workload assumptions. | No crew or warning-system effectiveness is inferred from the Boolean probability scenarios. |

Retain input/replay bytes, software/firmware and configuration hashes, instrument identity/calibration where applicable, raw observations, event timestamps, calculation/procedure version, expected and observed outcomes, exceptions and reviewer disposition. A rerun must preserve the prior evidence. Separate procedure execution, technical result, independent review and risk acceptance.

Use the [requirements](../requirements.md), [hazards and controls](../hazard-analysis.md), [trace records](../traceability.md), and [source review](../source-review.md) to determine the final scope and obligations.
