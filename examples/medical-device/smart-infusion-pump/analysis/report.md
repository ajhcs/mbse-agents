# Executed model study: Smart Infusion Pump System

Selected hazard: **HZ-001**. Model: **PumpOverinfusion**. Run: `8ef40b13dcdb9ebf8239`.

## Engineering interpretation

The same sensor under-reading event is reused in initiation and monitoring; multiplying it twice would understate the probability. A watchdog observes processor liveness, so BE6 is intentionally unused for running-but-wrong output. Clamp free-flow protection, actual flow dynamics, clinical risk, and physical independence require separate tests.

## Executed scope

Exhaustive enumeration evaluated **128 Boolean states** over 7 declared events. It derived **5 complete minimal cut sets** for the authored static model. This is exact static analysis, not a temporal or physical simulation.

One excessive-delivery challenge to the proposed flow-control architecture; physical flow, exposure duration, and harm are outside this static model.

All numerical inputs below are synthetic scenario assumptions. The probability calculation assumes mutual independence of distinct basic events after shared causes have been represented as reused IDs. It sums disjoint complete assignments; it does not multiply repeated events twice or approximate a union by summing overlapping cut probabilities.

## Complete minimal cut sets

| Cut | Basic events |
| --- | --- |
| 1 | BE3, BE5 |
| 2 | BE3, BE7 |
| 3 | BE4, BE7 |
| 4 | BE1, BE4, BE5 |
| 5 | BE2, BE4, BE5 |

## Conditional parameter scenarios

| Scenario | Exact probability per declared demand | Decimal | Basis |
| --- | --- | --- | --- |
| nominal-synthetic | 299999869021999/1000000000000000000000 | 2.9999987e-07 | Synthetic architecture challenge probabilities. |
| shared-drive-stress | 209900977012999/100000000000000000000 | 2.0990098e-06 | Tenfold shared motor/limiter dependency. |
| perfect-watchdog | 299999869021999/1000000000000000000000 | 2.9999987e-07 | A processor-alive watchdog does not establish correct delivered flow. |
| diverse-limiter | 10010988001/100000000000000000 | 1.0010988e-07 | Hypothetical removal of modeled drive/limiter common cause. |

## Checked claims and retained counterexamples

A passing check can mean that an expected counterexample was found. It does not make the rejected engineering claim true.

| Claim | Property holds in selected states? | States examined | Counterexamples | Check outcome |
| --- | --- | --- | --- | --- |
| Working independent hardware limiter prevents this selected overdelivery event | True | 32 | 0 | pass |
| Working deviation sensing prevents the event when its shared under-reading mode is absent | True | 32 | 0 | pass |
| A functioning processor watchdog guarantees safe flow | False | 64 | 35 | pass |
| Independent monitor fault is necessary to miss overdelivery | False | 64 | 24 | pass |

## Evidence and next decisions

- [Authored model and event basis](failure-model.json)
- [Executed exact results, including counterexample states](../evidence/analysis/model-results.json)
- [Independent CSE implementation cross-check](../evidence/analysis/cse-crosscheck.json)
- [Requirements and proposed acceptance conditions](../requirements.md)
- [Source/applicability review](../source-review.md)

The CSE receipt compares a separate implementation's complete cuts and baseline exact probability; it is not independent engineering acceptance of the event model. Immutable run directories preserve the model, engine, source snapshots and result bytes. Physical rates, timing, control effectiveness, human performance, adopted standards and acceptance remain separate evidence obligations.
