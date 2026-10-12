# Evidence contracts

Verification activity: ID, addressed requirements, method, procedure, preconditions, input/configuration, expected observation, acceptance criterion, environment/limitations, responsible reviewer, planned evidence.

Executed evidence: ID, activity, result (pass/fail/inconclusive), observed values, artifact path, tool/version, exact input and design revision or hashes, execution time when available, deviations, and scope. Review and acceptance are separate records with their owner and disposition.

A proposed file path is not an artifact. A pass against a reference model says nothing by itself about deployed hardware. A proof establishes the encoded properties under encoded assumptions; inspect missing properties, vacuity, fairness, time bounds, and the relationship between the model and implementation.

Coverage should report planned activities, executed results, failed/inconclusive claims, stale evidence, and unverified requirements separately. Do not count a planned test as a passed requirement.

For controlled exports, retain baseline, query/filter, transformation version, IDs, link types, and reconciliation results so evidence can be traced back to its source.
