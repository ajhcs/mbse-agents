# Executed model study: Autonomous Emergency Braking System

Selected hazard: **HZ-001**. Model: **AEBDetection**. Run: `fbabfc076dd0bf2fda20`.

## Engineering interpretation

Misses in both sensor paths, a fusion omission, or a shared sensor-loss event can each defeat detection. Fusion is not an additional independent barrier after both inputs are unavailable. The model does not address false positives, collision dynamics, braking effectiveness, or the entire operating domain.

## Executed scope

Exhaustive enumeration evaluated **256 Boolean states** over 8 declared events. It derived **11 complete minimal cut sets** for the authored static model. This is exact static analysis, not a temporal or physical simulation.

One obstacle-detection demand within an explicitly selected operating condition; hardware unavailability must be estimated for this demand before using empirical data.

All numerical inputs below are synthetic scenario assumptions. The probability calculation assumes mutual independence of distinct basic events after shared causes have been represented as reused IDs. It sums disjoint complete assignments; it does not multiply repeated events twice or approximate a union by summing overlapping cut probabilities.

## Complete minimal cut sets

| Cut | Basic events |
| --- | --- |
| 1 | BE7 |
| 2 | BE8 |
| 3 | BE1, BE4 |
| 4 | BE1, BE5 |
| 5 | BE1, BE6 |
| 6 | BE2, BE4 |
| 7 | BE2, BE5 |
| 8 | BE2, BE6 |
| 9 | BE3, BE4 |
| 10 | BE3, BE5 |
| 11 | BE3, BE6 |

## Conditional parameter scenarios

| Scenario | Exact probability per declared demand | Decimal | Basis |
| --- | --- | --- | --- |
| nominal-synthetic | 352001134189919821781/200000000000000000000000 | 0.0017600057 | Illustrative demand mixture; not an ASIL-derived rate. |
| shared-environment-stress | 215063175460262324681/20000000000000000000000 | 0.010753159 | Tenfold common environmental demand probability. |
| fusion-improvement | 33203433762368219/20000000000000000000 | 0.0016601717 | Hypothetical elimination of the modeled fusion omission only. |
| common-cause-control | 1721380721486494792781/2000000000000000000000000 | 0.00086069036 | Hypothetical reduction in shared environmental loss by operating restriction. |

## Checked claims and retained counterexamples

A passing check can mean that an expected counterexample was found. It does not make the rejected engineering claim true.

| Claim | Property holds in selected states? | States examined | Counterexamples | Check outcome |
| --- | --- | --- | --- | --- |
| Camera-path failures are tolerated when radar and fusion remain usable | True | 8 | 0 | pass |
| Radar-path failures are tolerated when camera and fusion remain usable | True | 8 | 0 | pass |
| Two healthy sensors guarantee detection despite arbitrary fusion behavior | False | 2 | 1 | pass |
| Perfect fusion resolves every common environmental sensor loss | False | 128 | 113 | pass |

## Evidence and next decisions

- [Authored model and event basis](failure-model.json)
- [Executed exact results, including counterexample states](../evidence/analysis/model-results.json)
- [Independent CSE implementation cross-check](../evidence/analysis/cse-crosscheck.json)
- [Requirements and proposed acceptance conditions](../requirements.md)
- [Source/applicability review](../source-review.md)

The CSE receipt compares a separate implementation's complete cuts and baseline exact probability; it is not independent engineering acceptance of the event model. Immutable run directories preserve the model, engine, source snapshots and result bytes. Physical rates, timing, control effectiveness, human performance, adopted standards and acceptance remain separate evidence obligations.
