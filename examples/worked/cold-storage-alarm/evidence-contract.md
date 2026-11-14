# Checked reference-model evidence contract

The version 2 baseline identifies sources, requirements, functions, components,
external actors, interfaces, verification activities, and evidence. Every ID is
unique within the baseline. A source locator is exact text that occurs once in
its artifact. IFC-02 connects ACTOR-01 to COMP-02, so operator acknowledgement
appears in the checked trace as well as the architecture diagram.

The source files and the baseline itself must be included in configuration
coverage. An executed record hashes exactly the baseline's declared configuration
files. The input baseline must equal its configured artifact. Changing the
requirement text, model, procedure, evidence-writing code, or baseline invalidates
old evidence until a new execution and applicability assessment are performed.

Current runners bind each loaded Python module to its source bytes at import.
The binding compares the actual module code object with compilation of those
bytes, which also catches a stale bytecode cache or a source edit during import.
Execution rejects any later change to the model, procedures, explorer or writer,
and records those loaded-source hashes. The workflow comparison applies the same
binding to its comparison code, writer and trace checker. Historical snapshots
retain their original collection mechanism and provenance.

| Field | Meaning |
| --- | --- |
| `status: planned` | Proposed work; no artifact or execution credit is claimed. |
| `status: drafted` | A named artifact exists; no execution credit is claimed. |
| `status: executed` | A version 2 execution record supplies run ID, timestamps, command, Python/platform, hashes, outcomes and observations. |
| `result: pass/fail/inconclusive` | The procedure's observed outcome, independent of whether its record is structurally valid. |
| `review: pending/reviewed` | Review is separate from execution; Reviewed requires a reviewer and a hashed review artifact. |
| `acceptance: not_accepted_for_hardware` | This reference-model contract provides no hardware or stakeholder acceptance. |

The checker rejects unsupported record versions, inconsistent scopes, missing
provenance, stale or incomplete hashes, duplicate/missing outcomes, unstructured
or nonfinite observations, and contradictory acceptance claims. Outcomes from a
rejected record contribute zero executed or passing procedure counts. A baseline
with any integrity error receives zero requirements with passing evidence credit.
A valid record containing a failure still counts as an executed procedure; a
requirement receives passing credit only if all its linked procedures pass.

The summary therefore separates reported procedure count, valid execution
records, rejected records, pass/fail/inconclusive outcomes, and requirement
coverage. Those checks establish consistency and applicability of the supplied
record. They do not authenticate a producer, prove that an arbitrary recorded
observation is truthful, or establish that a procedure adequately tests its claim.
`run_checks.py --check` separately reruns this example's actual procedures and
compares observations. The finite-state procedure's precise abstraction is in
[verification](verification.md).

The runner and trace checker use the same review-reference validation, including
reviewer identity, contained artifact path and artifact hash. Workflow receipts
also require complete execution provenance; reproducing observations does not
repair missing timestamps, commands, run identity or loaded-source bindings.
Current model reproduction requires the saved loaded-source map to match the
actual bound modules. The generic checker validates any supplied map against
Python configuration hashes; immutable historical records without that later
field retain their original, more limited provenance contract.

Execution files under `evidence/runs/` are created exclusively. Selecting a new
result archives prior selected bytes before atomic replacement. A run ID collision
with different content fails. Explicit output paths never overwrite. Historical
v1 files remain in [the original snapshot](history/legacy-v1/README.md); their
recorded Python version is preserved and their missing execution timestamp is
not retroactively invented.
