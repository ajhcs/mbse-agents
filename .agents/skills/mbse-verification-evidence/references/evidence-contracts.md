# Evidence contracts

Verification activity: ID, addressed requirements, method, procedure, preconditions, input/configuration, expected observation, acceptance criterion, environment/limitations, responsible reviewer, planned evidence.

Executed evidence: ID, activity, result (pass/fail/inconclusive), observed values, artifact path, tool/version, exact input and design revision or hashes, execution time when available, deviations, and scope. Review and acceptance are separate records with their owner and disposition.

Keep these facts independent:

| Field | Meaning |
| --- | --- |
| Activity lifecycle | Planned, prepared, or executed work, according to the project's definitions |
| Execution outcome | Pass, fail, or inconclusive for a particular executed procedure/configuration; no outcome for unexecuted work |
| Configuration applicability | Current, stale, or awaiting an applicability decision, with the referenced baseline |
| Review | Reviewer, reviewed scope, findings, and disposition |
| Acceptance | Authorized decision, accepted claim/scope, conditions, and owner; never inferred from a pass |

A failed result can be reviewed and preserved as useful evidence. A passing result can be stale or unaccepted. A controlled baseline is a configuration fact, not another word for successful verification.

For a numerical limit, distinguish the observed value, the uncertainty representation, the requirement, and the rule for making a conformity decision. A standard uncertainty, confidence interval, and guaranteed error bound have different meanings. Use the adopted project rule; if none is supplied, propose a rule explicitly and leave its adoption open. Check observations below, above, exactly on, and overlapping the limit: the categories must be mutually consistent, or have explicit precedence. Under an illustrative interval-based rule for an upper limit, an interval wholly within the permitted range can support pass, an interval wholly outside can support fail, and an interval crossing the boundary remains inconclusive. This is one possible rule, not a universal acceptance obligation. A conservative operational rejection may be appropriate even when the measurement alone is inconclusive; record that decision separately.

A proposed file path is not an artifact. A pass against a reference model says nothing by itself about deployed hardware. A proof establishes the encoded properties under encoded assumptions; inspect missing properties, vacuity, fairness, time bounds, and the relationship between the model and implementation.

Coverage should report planned activities, executed results, failed/inconclusive claims, stale evidence, and unverified requirements separately. Do not count a planned test as a passed requirement.

For controlled exports, retain baseline, query/filter, transformation version, IDs, link types, and reconciliation results so evidence can be traced back to its source.
