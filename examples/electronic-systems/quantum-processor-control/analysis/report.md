# Executed model study: Quantum Processor Control System

Selected hazard: **HZ-001**. Model: **QuantumRFProtection**. Run: `ddf8d5fe353469a481aa`.

## Engineering interpretation

Passive attenuation remains in every cut set. The verifier can intercept software requests but does not prevent faults arising later in the DAC/amplifier. Shared protection causes bypass claimed independence. These tests do not simulate quantum dynamics, RF propagation, cryogenic thermal behavior, or establish a SIL.

## Executed scope

Exhaustive enumeration evaluated **256 Boolean states** over 8 declared events. It derived **6 complete minimal cut sets** for the authored static model. This is exact static analysis, not a temporal or physical simulation.

One excessive-RF challenge at the defined protection boundary; probabilities are per challenge, not a demonstrated PFDavg or rate.

All numerical inputs below are synthetic scenario assumptions. The probability calculation assumes mutual independence of distinct basic events after shared causes have been represented as reused IDs. It sums disjoint complete assignments; it does not multiply repeated events twice or approximate a union by summing overlapping cut probabilities.

## Complete minimal cut sets

| Cut | Basic events |
| --- | --- |
| 1 | BE2, BE7, BE8 |
| 2 | BE3, BE7, BE8 |
| 3 | BE1, BE4, BE7, BE8 |
| 4 | BE2, BE5, BE6, BE7 |
| 5 | BE3, BE5, BE6, BE7 |
| 6 | BE1, BE4, BE5, BE6, BE7 |

## Conditional parameter scenarios

| Scenario | Exact probability per declared demand | Decimal | Basis |
| --- | --- | --- | --- |
| nominal-synthetic | 201190769711029999/10000000000000000000000000000 | 2.0119077e-11 | Synthetic RF protection challenge inputs. |
| attenuation-uncredited | 201190769711029999/10000000000000000000000000 | 2.0119077e-08 | No protective credit until physical worst-case attenuation is established. |
| shared-protection-stress | 201009878891020999/1000000000000000000000000000 | 2.0100988e-10 | Tenfold shared sensing/power dependency. |
| perfect-sequence-verifier | 200189970001/10000000000000000000000 | 2.0018997e-11 | A correct sequence precheck cannot prevent downstream hardware excess RF. |

## Checked claims and retained counterexamples

A passing check can mean that an expected counterexample was found. It does not make the rejected engineering claim true.

| Claim | Property holds in selected states? | States examined | Counterexamples | Check outcome |
| --- | --- | --- | --- | --- |
| Sufficient passive attenuation prevents this selected excessive-RF event | True | 128 | 0 | pass |
| A working limiter prevents the event without the shared protection dependency | True | 64 | 0 | pass |
| A perfect sequence verifier prevents every excessive-RF event | False | 128 | 30 | pass |
| Separate limiter and comparator faults are required for protection loss | False | 64 | 13 | pass |

## Evidence and next decisions

- [Authored model and event basis](failure-model.json)
- [Executed exact results, including counterexample states](../evidence/analysis/model-results.json)
- [Independent CSE implementation cross-check](../evidence/analysis/cse-crosscheck.json)
- [Requirements and proposed acceptance conditions](../requirements.md)
- [Source/applicability review](../source-review.md)

The CSE receipt compares a separate implementation's complete cuts and baseline exact probability; it is not independent engineering acceptance of the event model. Immutable run directories preserve the model, engine, source snapshots and result bytes. Physical rates, timing, control effectiveness, human performance, adopted standards and acceptance remain separate evidence obligations.
