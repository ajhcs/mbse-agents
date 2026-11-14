# HG-05-CH1 — decision brief

**Recommendation: reject HG-05-CH1 as submitted for the planned integration exercise.** Adding a unit field is useful, but continued acceptance of numeric-only files without recovered provenance retains the ambiguity the change is meant to remove. Resubmit the controlled interface proposal in `interface-contract.md`; use a quarantined test environment while its conditions are evaluated. This is an engineering recommendation, not an approval, flight decision, or executed integration result.

HG-05-F1 and HG-05-F2 are attributed historical findings. HG-05-I1–I3 and HG-05-C1–C3 are teaching reconstructions; HG-05-CH1 is synthetic. The supplier's assertion that export tests pass is part of the fictional change narrative. No export report, software build, sample file, raw measurement, or consumer execution is supplied.

The inspected [Phase I investigation report](https://discovery.larc.nasa.gov/pdf_files/MCO_report_2.pdf), executive summary pp. 6–8 and sections 4–5, supports the unit mismatch and wider transition, communication, staffing, training, and verification issues. It does not establish that this proposed format or legacy adapter works. This review introduces no mission or certification standard.

## Claim disposition

| Existing ID and status | Assessment and acceptance boundary |
| --- | --- |
| HG-05-C1 — `source_supported` | Retain the narrow historical finding; the relevant report content was inspected. The complete historical interface specification is not supplied. |
| HG-05-C2 — `unsupported_extension` | Retain as an explicitly unsupported assertion. A label can be recognized while the number is wrong, converted twice, assigned to the wrong event, or used incorrectly downstream. A producer-only test cannot establish consumer or navigation behavior. |
| HG-05-C3 — `proposed_unexecuted` | Keep open. Rejection must be observed at the ingestion boundary and in downstream accepted state, including mixed batches, parser failure, and recovery. A rejection message alone is insufficient. |

`claim-evidence.proposed.csv` preserves every original field and adds the proposed review and ownership fields. It does not silently rewrite C2 into a weaker true claim or promote C3 to passed.

## Conditions for a revised proposal

| Condition | Minimum evidence | Proposed accountable role |
| --- | --- | --- |
| HG-05-P01: remove ambiguous ingress | Reviewed version/unit contract, exact parser and adapter configuration, and an explicit list of permitted paths. No fall-through from a failed new-format parse to legacy parsing. | Consumer integration owner, with producer interface owner |
| HG-05-P02: recover legacy provenance | Byte-identifiable files, producing configuration, source quantity/units, derivation history, and a reviewer-supported mapping. Files without that evidence stay quarantined. | Producer data custodian; consumer owner decides admissibility |
| HG-05-P03: establish an independent oracle | A controlled paired sample linking a known impulse quantity to source values, expected serialized values, and expected consumer results, with units, frame, event/time definition, derivation, and tolerance basis. | Navigation verification lead; supplier contributes source information but does not solely approve its own oracle |
| HG-05-P04: exercise both successful and rejected paths | The acceptance matrix, executed later against identified producer/consumer builds; input/output hashes, expected/observed comparison, rejection reasons, accepted-state comparison, logs, and deviations. | Consumer integration test owner; navigation verification lead reviews |
| HG-05-P05: transfer operating responsibility | Agreed quarantine/replay procedure, legacy inventory disposition, anomaly contact, configuration owner, and demonstrated development-to-operations handover. | Operations lead and development lead through HG-05-I2 |

Proposed roles have not been assigned to named people in the supplied packet. The integration lead must confirm role holders before scheduling the review. The next review is triggered by delivery of P01–P03 plus a runnable, versioned ingestion path; final exercise acceptance additionally needs P04–P05 and disposition of anomalies.

## What can be reused

| Available or asserted material | Permitted use and limitation |
| --- | --- |
| `source-facts.csv` and `sources.json` | Establish rationale and historical source scope; they are not test vectors. |
| `interfaces.csv`, `claim-evidence.csv`, `change.json`, `relations.mmd` | Identify interfaces, claims, and coverage to turn into a procedure. The graph is an information-flow aid, not an executable model. |
| `request.md`, `review-task.md`, `packet-manifest.json`, supplied skills | Define the task, provenance boundary, file integrity, and engineering guidance. Hash agreement is not verification of an engineering claim. |
| Supplier export tests | Reported only in the synthetic change. Recover actual procedure, inputs, expected results, execution logs, producer release and configuration before claiming any reuse. Even then, they cover only their demonstrated scope. |
| Existing legacy data files | None are supplied. Recover identities, units, generating releases and transformations before use as semantic acceptance data. Unknown files may later be used as clearly labeled negative rejection fixtures; they cannot become a valid oracle by assertion. |
| Producer, adapter, consumer implementation and released interface | Not supplied; obtain the actual versions for integration execution. No fabricated sample in these outputs is historical flight data. |

The proposed matrix has no passed rows and contains no executed result. `sample-plan.json` supplies a concrete analytical fixture: an ideal 2 N force for 3 s gives a 6 N*s impulse; the disagreement fixture carries 7 N*s. These are invented, labeled software-test inputs with an independently derivable mathematical answer, not physical calibration or historical data. The navigation verification lead must review them, agree the comparison rule, and obtain the provenance-supported physical sample still needed for broader meaning. Structural validity and physical correctness remain different claims.

## Message to the integration lead

Reject HG-05-CH1 as submitted: the uncontrolled legacy path leaves unit meaning unresolved. The gap is a provenance-bound interface and an independently established producer-to-consumer acceptance sample. The consumer integration owner owns the revised ingress contract; the producer data custodian owns legacy recovery; the navigation verification lead owns the oracle. Reopen when those artifacts and a runnable configuration are available, then require the recorded ingestion results and operations handover before accepting the exercise.
