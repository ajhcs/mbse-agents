# N-1 — review and proposed decision sheet

**Keep N-1 open and withhold operational use pending an authorized decision supported by adequate evidence.** The six supplied records do not establish compliance across the specified operating envelope. They are authored teaching fixtures; no hardware was available and no test was executed in this exercise.

## Proposed rule

For observed elapsed time **x**, use the interval **[x − U, x + U] ms**, conditional on the supplier's assertion that U is a guaranteed symmetric error bound including clock alignment. This is a range of compatible true elapsed times, not additional observed readings or a statistical confidence interval. Confirm that assertion before actual use.

Apply the unchanged, inclusive requirement **elapsed time ≤ 120 ms**:

- **Compliance established for this observation:** x + U ≤ 120 ms.
- **Noncompliance established for this observation:** x − U > 120 ms.
- **Indeterminate:** the interval includes both compliant and noncompliant times, so x − U ≤ 120 < x + U.

This rule is proposed, not adopted. The supplier's nominal-time rule does not establish compliance or noncompliance when the interval straddles the limit. No tolerance or margin is added to N-1.

## Revised observation dispositions

All times are milliseconds. Input IDs, values, and supplier statuses are preserved.

| ID | Observed elapsed time | U | Supplier status | Compatible elapsed-time interval | Outcome under proposed rule and basis |
| --- | ---: | ---: | --- | --- | --- |
| OBS-1 | 111 | 3 | pass | [108, 114] | Compliance established for this observation: upper bound 114 ≤ 120. |
| OBS-2 | 121 | 4 | fail | [117, 125] | Indeterminate: interval spans 120; nominal exceedance does not establish noncompliance under the bound assumption. |
| OBS-3 | 130 | 2 | fail | [128, 132] | Noncompliance established for this observation: lower bound 128 > 120. |
| OBS-4 | 120 | 0 | pass | [120, 120] | Compliance established for this observation: equality is permitted, conditional on the asserted zero error bound. |
| OBS-5 | 116 | 4 | pass | [112, 120] | Compliance established for this observation: upper bound equals the inclusive limit. |
| OBS-6 | 117 | 6 | pass | [111, 123] | Indeterminate: interval spans 120; nominal compliance does not establish compliance under the bound assumption. |

**Acceptance status for every row and for N-1: no authorized acceptance decision is supplied.** These are analytical dispositions of supplied fixtures, not new executed-test results, accepted evidence, or release authorization.

## Closure and operational disposition

N-1 cannot now be closed. OBS-3 conflicts with the timing requirement under the supplied assumption; OBS-2 and OBS-6 remain unresolved. Even the three favorable dispositions establish only their individual timing claims. No argument connects six observations to coverage of the entire specified operating envelope.

For the operations lead's requested policy, any unresolved or established noncompliance means compliance is not established and use is withheld. Both conditions occur here. Record this as a recommendation; an indeterminate result is not a demonstrated violation, and withholding is not itself an authorized acceptance or rejection decision.

Before closure or use, the project needs to adopt and document the decision rule and identify the authorized decision owner; confirm U's guaranteed-bound meaning and applicability, including OBS-4's zero bound; establish the records' provenance, relevant configuration, operating conditions, valid-trip trigger, warning-assertion endpoint, and timing method; define and justify coverage of the specified envelope; and resolve OBS-3 plus the indeterminate records with traceable investigation and appropriate evidence. Any proposed additional verification remains planned until executed and recorded. Review and acceptance must identify their scope, conditions, owner, and disposition separately from the observation outcomes.
