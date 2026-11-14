# Independent evidence review

Review target: the working tree compared with `b54b0b673eb80ea22bd6c4987955192b22332923`.
Scope: `scripts/check_trace.py`, both cold-storage worked examples, `tests/test_trace.py`, and `tests/test_reference_model.py`.
Reviewer owns no implementation changes. All extra fixtures, scripts, and logs are under `.mbse-review`. No external calls, model calls, package installs, or code commits were made.

The review applies the project's baseline-review and verification-evidence skill contracts. It assesses the declared illustrative reference-model scope, not a general MBSE platform, hardware validation, authentication of arbitrary producer claims, or a proof of procedure adequacy.

## Final disposition

All five independently reproduced findings are repaired and closed in the final reviewed working tree. There are no remaining actionable findings within this review's declared scope. Final independent execution ran **32 focused tests with zero failures, errors, or skips**, reproduced both current models and the complete revision comparison, and verified the exact expected four-procedure failed snapshot. Fresh fixture probes also rejected source edits, stale timestamp/size bytecode caches, wrong-origin imported modules, malformed review/receipt provenance, and changed selected results during collection. Reviewed production files did not change during these checks.

The original observations below are retained as review history. The closure evidence and final artifacts are listed after them.

## Initial findings

All four findings below were reproduced against the initial reviewed working tree. Bounded repair requests were sent to the parent and then to the implementation author `evidence_review`. They are now closed by the independent rechecks below.

### EIR-01 — P2 — Source hashes can describe code different from the code executed

Location: `examples/worked/cold-storage-alarm/evidence_io.py:13-26`, with imports at `run_checks.py:7-9` and the already-bound callable at `run_checks.py:63-64`; the repaired revision has the same arrangement.

`Alarm`, the procedures, explorer, and writer are loaded before `capture` reads their source bytes. A source edit after import but before `evidence()` means capture records the new file's hash while invoking the old loaded implementation. Its pre/post-execution hashes are equal, so the stale in-memory implementation is not rejected.

Reproduction: copy the example under `.mbse-review/evidence-independent-fixtures/source-changed-after-import`, import its `run_checks`, change the model's fault threshold from 1000 to 2000 ms, and call its real `evidence()`. It emits eight passes bound to the 2000 ms model source. `check_trace` reports valid integrity and four requirements with passing evidence. A fresh `run_checks.py --check` exits 1 with `results` disagreement. This is a source-to-execution binding defect in the supplied collector, not a demand for an authenticated producer.

Repair: bind the runner to the bytes actually loaded, or reliably reject loaded-source drift before capture. Cover model, procedure, explorer, and evidence-writing code. Add a regression that imports, edits a bound source, and attempts collection; ordinary replay of unchanged sources must continue to work.

### EIR-02 — P2 — Model reproduction accepts unsupported review status

Location: `examples/worked/cold-storage-alarm/run_checks.py:74-82` and the equivalent revised runner; `scripts/check_trace.py:validate_record_metadata` only checks that a reviewed record's reference is an object.

Reproduction: set a copied selected record to `review: reviewed` with `review_reference: {}`. `run_checks.py --check` exits 0 and prints that eight procedures pass. The full trace checker rejects the same record for missing reviewer identity and malformed/missing review artifact, with zero evidence credit.

The `--check` path explicitly validates metadata but uses a weaker subset than the contract requires for a reviewed record. The observed model result still reproduces; the stored record's claimed lifecycle status does not satisfy its declared contract.

Repair: share review identity and review-artifact path/hash validation between the full checker and reproduction path. Do not compare a historical review or timestamp to a newly generated run; validate that historical metadata on its own terms.

### EIR-03 — P2 — Workflow receipt reproduction does not validate execution provenance

Location: `examples/worked/cold-storage-alarm-revision/compare_revisions.py:90-93`.

Reproduction: delete the entire `execution` object from a copy of `evidence/revision-check.json` and pass it with `compare_revisions.py --check --output <copy>`. The command exits 0 and reports successful reproduction. No run ID, time, command, interpreter, or host provenance remains in the accepted stored receipt.

Repair: validate required execution metadata independently from comparison of reproducible observations and configuration. Historical execution metadata should remain preserved and need not match a fresh replay, but absent or malformed provenance must fail the receipt check.

### EIR-04 — P2 — VER-08 does not check unchanged state after acknowledgement rejection

Location: `examples/worked/cold-storage-alarm/explore_states.py:87-93` and the equivalent revised explorer; the stated VER-08 acceptance is in each `verification.md`.

Timestamp rejection compares the pre/post state, but nonboolean acknowledgement rejection only checks that `ValueError` occurs. A model that sets `high = True` and then rejects `acknowledge="yes"` passes `check_inputs` with all 17 cases and no failures. The reproduction independently confirms that the rejected call changed state.

The shipped `Alarm` currently rejects before mutation; this finding concerns the actual evidence procedure's promised acceptance condition. VER-07 tests only boolean acknowledgements, so it cannot cover this omitted check.

Repair: compare state before and after the rejected acknowledgement as well, with a mutant regression that changes state and then raises.

### EIR-05 — P2 — New loaded-source provenance could be removed from stored model evidence

This follow-on defect was found during the first repair re-review and is now closed. The newly introduced `execution.loaded_sources` map could be deleted or changed in a selected current model record while `run_checks.py --check --output <copy>` still exited 0. The workflow receipt already required those bindings; model comparison did not. The original failing record is preserved at `.mbse-review/evidence-independent-v2-fixtures/record-missing-loaded-sources.json`.

The author repaired current model comparison to require equality with freshly bound sources and added generic validation of any supplied map against the configuration's Python-file hashes. Historical schema-2 records without the new map retain their previous contract; their snapshots were not rewritten. Current runners require the map and reject missing, empty, or altered bindings.

## Independent repair verification

| Finding | Independently verified final behavior |
| --- | --- |
| EIR-01 | All four configured Python modules reject source changes after import. Four same-size/same-mtime stale bytecode caches are rejected by actual-code/source comparison. Three modules cached from the wrong directory are rejected by origin checks. Comparison code, its writer, and the repository checker reject changes after import; stale caches for the comparison code and checker are rejected. |
| EIR-02 | Both current runners and the trace checker reject empty and stale review references; both accept a complete reviewer identity and correctly hashed contained review artifact. Invalid references receive zero executed and passing requirement credit. |
| EIR-03 | Missing execution object, invalid run ID, invalid timestamp, empty command, missing bindings, and changed bindings each make receipt reproduction exit 1 for the appropriate provenance/binding reason. |
| EIR-04 | The original mutant now returns `passed: false` with `changed state on rejected nonboolean acknowledgement`; all 17 stated input cases still execute. |
| EIR-05 | Both current runners reject missing, empty, and altered stored binding maps. The full trace checker rejects supplied inconsistent maps with zero executed/passing requirement credit. |

The model reference and repaired runner each reproduce eight passes. The complete comparison exits 0; the preserved failed runner exits 1 with exactly `Failed: VER-03, VER-06, VER-07, VER-08`. The three trace checks retain the expected valid execution totals: reference 8 pass, failed snapshot 4 pass/4 fail, repaired 8 pass. Hardware/stakeholder acceptance remains unclaimed.

An additional collection probe changes a selected model result after the comparison's evaluation but before its post-collection hash check. The comparison exits 1 with `Revision inputs changed during comparison`, and the selected workflow receipt remains byte-for-byte unchanged.

History was checked against artifacts retained during the initial review: all five original reference-model run archives and all ten legacy snapshot files (including its manifest) remain byte-identical; all 21 configured prior/failed snapshot source-and-result hashes match the pre-repair receipt. The original repaired selection remains present in the archive with its exact original hash. The archived original workflow receipt's body matches the preserved initial receipt witness. No historical timestamps or host metadata were rewritten to make a fresh execution appear historical.

Final verification artifacts:

- `.mbse-review/evidence-independent-final-checks.py`: reproducible focused tests, model/receipt mutation probes, exact failed-run check, and changed-result collection probe.
- `.mbse-review/evidence-independent-final-results.json`: actual final outputs plus SHA-256 hashes for every reviewed source/evidence file.
- `.mbse-review/evidence-independent-final-tests.log`: all 32 focused test names and results.
- `.mbse-review/evidence-independent-v2-probes.py`: reusable source/cache/origin/history probe implementation.
- `.mbse-review/evidence-independent-final-bindings.json`: fresh final source/cache/origin/comparison binding and history results.
- `.mbse-review/evidence-independent-final-fixtures/` and `evidence-independent-final-binding-fixtures/`: preserved final disposable cases.

## Initial executed checks and positive findings

| Check | Actual result |
| --- | --- |
| Focused `test_trace.py` and `test_reference_model.py` | 25 tests pass, zero failures/errors/skips. Disposable directories redirected under `.mbse-review` without changing the tests. |
| Current `cold-storage-alarm/run_checks.py --check` | Exit 0; eight procedures reproduce. |
| `cold-storage-alarm-revision/compare_revisions.py --check` | Exit 0; actual prior pass, exact expected old-model failure, repaired pass, and stale-evidence rejection reproduce. |
| Current trace checker | Valid; 8 executed / 8 pass / 0 fail; 4 requirements receive passing model evidence. |
| Failed revision trace checker | Valid; 8 executed / 4 pass / 4 fail; 0 requirements receive passing model evidence. |
| Repaired revision trace checker | Valid; 8 executed / 8 pass / 0 fail; 4 requirements receive passing model evidence. |
| Original v1 preservation | All 9 manifest files are byte-identical to their files at the comparison commit, and their manifest hashes match. The original 6 procedures reproduce in the focused tests. |

The finite-state exploration is real executable traversal. It uses an independent sample-counter oracle, exercises each reachable state's six low/high/invalid and acknowledgement combinations, and checks flags plus per-transition event production. The original abstraction closes at 66 states / 396 transitions; the repaired abstraction closes at 56 states / 336 transitions. The failed revision supplies a concrete six-invalid-sample counterexample at 500 ms (12 states / 71 examined transitions before detection). The implementation uses elapsed threshold comparisons, so time translation and timer saturation are applicable to this scoped model. The 10,000-state guard fails closed rather than claiming complete exploration. These are bounded abstraction claims, not arbitrary-code proofs or physical performance claims.

The core trace checker separates execution integrity, pass/fail/inconclusive outcomes, review, and hardware acceptance. Rejected record outcomes contribute zero executed/passing counts; any baseline integrity error yields zero requirements with passing evidence. Valid failure and inconclusive records remain executed evidence. Exact source locators, declared source coverage, configuration hashes, and equality with the configured baseline are checked. The generic checker explicitly does not determine procedure adequacy or authenticate the truth of arbitrary observations.

Archive creation uses exclusive files; replacement archives prior selected bytes; collisions with changed content and explicit-output overwrite are rejected. The focused tests check those behaviors and symlink escape refusal. No destructive overwrite or synthetic rewrite of original execution provenance was observed. The revision receipt hashes all selected result records and checks those inputs before and after comparison, resisting a result-file change during collection.

## Review artifacts

- `.mbse-review/evidence-independent-probes.py`: exact review-only reproducer.
- `.mbse-review/evidence-independent-probes.json`: actual outputs for all four findings.
- `.mbse-review/evidence-independent-focused-tests.log`: focused test output.
- `.mbse-review/evidence-independent-history.json`: independent comparison to the original commit.
- `.mbse-review/evidence-independent-fixtures/`: preserved disposable reproductions.

## Coverage limits

No physical device or stakeholder validation was attempted or claimed. No model quality evaluation or paid/model access was performed. This review does not claim race-proof behavior under a hostile concurrent filesystem writer, cryptographic authenticity of evidence, standards compliance, or correctness outside the declared sampled abstraction. The five findings were concrete discrepancies within the collector/reproduction/procedure contracts, not general-platform requirements.
