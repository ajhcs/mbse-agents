# Executed model study: Integrated Flight Management System

Selected hazard: **HZ-001**. Model: **FMSGuidance**. Run: `abd60c975770f723ddea`.

## Engineering interpretation

The comparator compares channels, not truth. Because this selected hazard path produces mutually consistent wrong outputs, BE6 is intentionally unused. External monitoring coverage and its independence must be established for the actual failure condition; TAWS is not assumed to cover all guidance errors.

## Executed scope

Exhaustive enumeration evaluated **512 Boolean states** over 9 declared events. It derived **10 complete minimal cut sets** for the authored static model. This is exact static analysis, not a temporal or physical simulation.

One guidance decision with an erroneous mutually consistent output possible; all probabilities are per this declared demand, not per flight hour.

All numerical inputs below are synthetic scenario assumptions. The probability calculation assumes mutual independence of distinct basic events after shared causes have been represented as reused IDs. It sums disjoint complete assignments; it does not multiply repeated events twice or approximate a union by summing overlapping cut probabilities.

## Complete minimal cut sets

| Cut | Basic events |
| --- | --- |
| 1 | BE1, BE9 |
| 2 | BE2, BE9 |
| 3 | BE3, BE9 |
| 4 | BE4, BE9 |
| 5 | BE5, BE9 |
| 6 | BE1, BE7, BE8 |
| 7 | BE2, BE7, BE8 |
| 8 | BE3, BE7, BE8 |
| 9 | BE4, BE7, BE8 |
| 10 | BE5, BE7, BE8 |

## Conditional parameter scenarios

| Scenario | Exact probability per declared demand | Decimal | Basis |
| --- | --- | --- | --- |
| nominal-synthetic | 134173030809261370330999/1000000000000000000000000000000 | 1.3417303e-07 | Synthetic reference inputs, not an aircraft rate estimate. |
| external-common-cause-stress | 123195137580383359321999/100000000000000000000000000000 | 1.2319514e-06 | Explore tenfold increase in shared detection-dependency probability. |
| perfect-comparator | 134173030809261370330999/1000000000000000000000000000000 | 1.3417303e-07 | A perfect equality comparator cannot detect identical wrong outputs. |
| external-monitor-improvement | 1341741285985842581320999/100000000000000000000000000000000 | 1.3417413e-08 | Hypothetical improvement in independently supported external detection. |

## Checked claims and retained counterexamples

A passing check can mean that an expected counterexample was found. It does not make the rejected engineering claim true.

| Claim | Property holds in selected states? | States examined | Counterexamples | Check outcome |
| --- | --- | --- | --- | --- |
| No initiating guidance error prevents this top event | True | 16 | 0 | pass |
| External detection prevents the top event when its common dependency is absent | True | 64 | 0 | pass |
| A perfect comparator alone is sufficient to prevent this top event | False | 256 | 155 | pass |
| Dissimilar toolchains eliminate every shared guidance error | False | 256 | 150 | pass |

## Evidence and next decisions

- [Authored model and event basis](failure-model.json)
- [Executed exact results, including counterexample states](../evidence/analysis/model-results.json)
- [Independent CSE implementation cross-check](../evidence/analysis/cse-crosscheck.json)
- [Requirements and proposed acceptance conditions](../requirements.md)
- [Source/applicability review](../source-review.md)

The CSE receipt compares a separate implementation's complete cuts and baseline exact probability; it is not independent engineering acceptance of the event model. Immutable run directories preserve the model, engine, source snapshots and result bytes. Physical rates, timing, control effectiveness, human performance, adopted standards and acceptance remain separate evidence obligations.
