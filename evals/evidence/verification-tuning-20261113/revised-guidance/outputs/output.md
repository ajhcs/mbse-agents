N-1 remains open. Recommend withholding operational use because compliance across the specified operating envelope is not established. The records are authored teaching fixtures; this review does not constitute hardware testing, executed verification, or an authorized acceptance decision.

The supplier's nominal-time rule ignores the supplied error bound. No project rule has been adopted, so the following is a proposal for review and adoption, conditional on confirming that U is a valid guaranteed symmetric bound, including clock alignment. It is not a statistical confidence interval.

For observed elapsed time t, the bound-derived interval of compatible elapsed times is [t − U, t + U]. N-1 permits elapsed times at or below 120 ms. Apply one mutually exclusive outcome per record:

- **Pass:** t + U ≤ 120 ms; every compatible elapsed time meets the limit.
- **Fail:** t − U > 120 ms; every compatible elapsed time exceeds the limit.
- **Inconclusive:** t − U ≤ 120 ms < t + U; both compliant and noncompliant elapsed times remain possible.

These are conditional record-level conformity outcomes under the proposed rule. They neither adopt that rule nor authorize acceptance or use.

| ID | Observed elapsed time (ms) | U (ms) | Supplier status, preserved | Bound-derived interval (ms) | Proposed outcome | Basis |
| --- | ---: | ---: | --- | --- | --- | --- |
| OBS-1 | 111 | 3 | pass | [108, 114] | Pass | Upper bound 114 ≤ 120. |
| OBS-2 | 121 | 4 | fail | [117, 125] | Inconclusive | Interval includes values on both sides of 120; nominal exceedance alone does not establish noncompliance. |
| OBS-3 | 130 | 2 | fail | [128, 132] | Fail | Lower bound 128 > 120. |
| OBS-4 | 120 | 0 | pass | [120, 120] | Pass | Equality satisfies “no later than”; relies on the supplied zero-error assumption. |
| OBS-5 | 116 | 4 | pass | [112, 120] | Pass | Inclusive upper bound equals the permitted limit. |
| OBS-6 | 117 | 6 | pass | [111, 123] | Inconclusive | A nominal time below 120 does not exclude an actual time above 120. |

The intervals are derived from the supplied observations and bounds, not additional observations. The preserved supplier statuses are historical inputs; the proposed outcomes show the consequences of a different, explicitly stated rule. No authorized acceptance decision is supplied for any record or for N-1.

Even if these were applicable executed measurements, OBS-3 would demonstrate an over-limit result under the supplied assumptions, OBS-2 and OBS-6 would remain unresolved, and the missing envelope-coverage argument would prevent whole-requirement closure. Three record-level passes cannot close N-1.

Before closure or use, the project needs to adopt a decision rule; confirm the bounds and their applicability to actual timing measurements; establish the operating envelope, relevant configuration, and a justified coverage plan; obtain traceable executed evidence; and resolve the represented failure and inconclusive cases. Evidence that distinguishes which side of 120 ms a crossing interval lies on could include a justified tighter bound or appropriately specified new measurements; no such evidence exists in this packet. Record review and an authorized acceptance decision with its owner and scope separately.

Withholding use follows the operations lead's stated preference whenever compliance is unestablished. It is an operational recommendation, not a claim that an inconclusive observation is a measurement failure, and no release or acceptance authority is exercised here.
