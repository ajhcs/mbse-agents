# Executed model study: UAS Ground Control Station

Selected hazard: **HZ-001**. Model: **GCSLinkLoss**. Run: `912a32b0850766c79567`.

## Engineering interpretation

The top event is undetected communication loss at the ground station. It does not by itself establish uncontrolled aircraft behavior: onboard lost-link behavior is a separate unresolved interface. Shared monitoring dependency BE9 appears once even though it defeats two monitors.

## Executed scope

Exhaustive enumeration evaluated **512 Boolean states** over 9 declared events. It derived **10 complete minimal cut sets** for the authored static model. This is exact static analysis, not a temporal or physical simulation.

One ground-station supervision interval during a communication-loss demand; no flight-hour rate or air-vehicle trajectory is calculated.

All numerical inputs below are synthetic scenario assumptions. The probability calculation assumes mutual independence of distinct basic events after shared causes have been represented as reused IDs. It sums disjoint complete assignments; it does not multiply repeated events twice or approximate a union by summing overlapping cut probabilities.

## Complete minimal cut sets

| Cut | Basic events |
| --- | --- |
| 1 | BE7, BE8, BE9 |
| 2 | BE1, BE3, BE7, BE9 |
| 3 | BE1, BE4, BE7, BE9 |
| 4 | BE2, BE3, BE7, BE9 |
| 5 | BE2, BE4, BE7, BE9 |
| 6 | BE5, BE6, BE7, BE8 |
| 7 | BE1, BE3, BE5, BE6, BE7 |
| 8 | BE1, BE4, BE5, BE6, BE7 |
| 9 | BE2, BE3, BE5, BE6, BE7 |
| 10 | BE2, BE4, BE5, BE6, BE7 |

## Conditional parameter scenarios

| Scenario | Exact probability per declared demand | Decimal | Basis |
| --- | --- | --- | --- |
| nominal-synthetic | 10121977898580560958001/100000000000000000000000000000000 | 1.0121978e-10 | Synthetic supervision-demand inputs. |
| shared-infrastructure-stress | 10012185723036065976001/1000000000000000000000000000000 | 1.0012186e-08 | Increase common communication and monitoring dependencies. |
| heartbeat-independent | 0 | 0 | Hypothetical reliable heartbeat monitor and removal of its shared dependency. |
| operator-crosscheck-improved | 10121977898580560958001/1000000000000000000000000000000000 | 1.0121978e-11 | Conditional improvement in operator detection opportunity; requires workload validation. |

## Checked claims and retained counterexamples

A passing check can mean that an expected counterexample was found. It does not make the rejected engineering claim true.

| Claim | Property holds in selected states? | States examined | Counterexamples | Check outcome |
| --- | --- | --- | --- | --- |
| A functioning heartbeat monitor prevents an undetected loss when common monitoring failure is absent | True | 128 | 0 | pass |
| An available BLOS path prevents total link loss without shared infrastructure failure | True | 64 | 0 | pass |
| Separate LOS and BLOS equipment faults are necessary for total undetected loss | False | 32 | 5 | pass |
| Two monitoring software modules establish independent detection | False | 128 | 25 | pass |

## Evidence and next decisions

- [Authored model and event basis](failure-model.json)
- [Executed exact results, including counterexample states](../evidence/analysis/model-results.json)
- [Independent CSE implementation cross-check](../evidence/analysis/cse-crosscheck.json)
- [Requirements and proposed acceptance conditions](../requirements.md)
- [Source/applicability review](../source-review.md)

The CSE receipt compares a separate implementation's complete cuts and baseline exact probability; it is not independent engineering acceptance of the event model. Immutable run directories preserve the model, engine, source snapshots and result bytes. Physical rates, timing, control effectiveness, human performance, adopted standards and acceptance remain separate evidence obligations.
