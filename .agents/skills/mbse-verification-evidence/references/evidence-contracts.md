# Evidence contracts

Record each activity so another engineer can tell what to run and what it would establish. Include the ID, addressed requirements, method, procedure, preconditions, input and design configuration, expected observation, decision rule, environment, limitations, and reviewer as relevant.

Bind an executed result to the activity, observed values, saved artifact, tool/version, exact input and design revision or hashes, execution time when available, deviations, and scope. Record who reviewed what and who accepted which claim.

Keep these facts independent:

| Field | Meaning |
| --- | --- |
| Activity lifecycle | Planned, prepared, or executed work, according to the project's definitions |
| Execution outcome | Pass, fail, or inconclusive for a particular executed procedure/configuration; no outcome for unexecuted work |
| Configuration applicability | Current, stale, or awaiting an applicability decision, with the referenced baseline |
| Review | Reviewer, reviewed scope, findings, and disposition |
| Acceptance | Authorized decision, accepted claim/scope, conditions, and owner; never inferred from a pass |

A failed result can be reviewed and preserved as useful evidence. A passing result can be stale or unaccepted. A controlled baseline is a configuration fact, not another word for successful verification.

For an event-triggered deadline, compare how long the test holds the input with what qualifies as an event at the specified interface. Exercise the shortest permitted event when its duration could affect detection. If that duration is unresolved, record which event durations the procedure covers and who can settle the interface assumption.

For a numerical limit, report the observed value, kind of uncertainty, requirement, and conformity rule. A standard uncertainty, confidence interval, and guaranteed error bound have different meanings. Use the adopted rule or label a proposed rule and leave its adoption open. Check below, above, at, and overlapping the limit. Pass, fail, and inconclusive need mutually exclusive conditions or explicit precedence.

For example, under one interval-based rule for an upper limit, an interval wholly within the permitted range can support pass, one wholly outside can support fail, and one crossing the boundary remains inconclusive. Record an operational hold or rejection separately from the measured disposition when they differ.

A proposed file path is not an artifact. A pass against a reference model says nothing by itself about deployed hardware. A proof establishes the encoded properties under encoded assumptions; inspect missing properties, vacuity, fairness, time bounds, and the relationship between the model and implementation.

For coverage, reconcile each claim to executed results that apply, planned activities, or an explicit gap. Keep failed and inconclusive results and stale evidence visible alongside unverified requirements.

For controlled exports, retain baseline, query/filter, transformation version, IDs, link types, and reconciliation results so evidence can be traced back to its source.
