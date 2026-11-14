# Verification index, revision B — proposed evidence work

REQ-7 now carries the CR-1-approved 200 ms limit. REQ-8 is unchanged. VER-7 and VER-8 retain their IDs, with revised procedures and scope recorded here. No controller test, timing measurement or simulated controller execution was performed for this package. The supplied inputs are assessment fixtures, not installation evidence.

## Existing evidence and present status

| ID/activity | Lifecycle and outcome | Configuration applicability | Review/acceptance |
| --- | --- | --- | --- |
| EVD-A-7 / VER-7 | Supplied historical fixture record; `recorded_result: pass`, criterion 500 ms, observed 460 ms. This package did not execute that run. | `controller-revision-A`; historical meaning retained unchanged in [report-old.json](report-old.json). Stale for a positive B timing claim. A comparable 460 ms observation exceeds 200 ms, but this is not a newly executed revision-B failure. | Actual instrument, uncertainty, procedure and detailed setup records are absent. Prior review/acceptance unknown; no B acceptance. |
| VER-7 revision B | Revised plan, unexecuted; outcome unset | Current requirement identified, implementation/configuration to be selected | Review and execution pending |
| VER-8 revision A | Supplied plan only: visibility after communication loss; no result | Does not exercise REQ-8's stop, retained inhibit or explicit-resume behavior; useful visibility intent retained below | No pass or acceptance available |
| VER-8 revision B | Expanded plan, unexecuted; outcome unset | Proposed guard/display behavior identified; output binding and implementation pending | Review and execution pending |
| `evidence/revision-b-results.json` | Proposed path only; **file absent** | No evidence/configuration recorded | Not created as a placeholder; no review or acceptance |

EVD-A-7 remains applicable as a record of what was reported for revision A and as input to investigating prior timing. It cannot support ≤ 200 ms because its recorded value exceeds that limit, its configuration is A, and the detailed method is absent. It supplies no stop/recovery observation for REQ-8. Reusing parts of its method or unchanged-function results would require the actual procedure/configuration and a scoped applicability argument; a surviving REQ-7 link is insufficient.

## VER-7 — changed timing requirement

**Addresses:** REQ-7/N-01 and CR-1. **Methods:** end-to-end timing analysis plus instrumented integration test on the selected revision-B implementation. **Proposed owner/reviewer:** timing test lead and requirement/architecture reviewer; actual assignments pending.

Before execution, freeze the revised requirement and design, COMP-1–COMP-3 hardware/software/configuration identities, IFC-1/IFC-2 implementation, project-controlled pressure threshold/validity contract, operating conditions, clock source, test harness and instruments. Retrieve the unchanged threshold and validity values; do not invent replacements or alter the trigger to obtain a favorable result. Document loads, scheduling, communication behavior and relevant environmental conditions. Choose an instrument whose uncertainty is suitable for the 200 ms decision and record calibration/timestamp alignment.

The procedure will:

1. Establish equipment operation under the unchanged project definition; apply a valid pressure input below the controlled high-pressure threshold and confirm initial warning state.
2. Apply an input that first meets the high-pressure condition. Record `t0` at that defined valid-input event; map the observation point to the existing input contract. Do not move t0 downstream to COMP-2 detection. Capture intermediate stage times without replacing the end-to-end measurement.
3. Record `t1` when the local high-pressure warning is actually asserted at COMP-3. A software command, bus message or acknowledgment alone is not the end event. Match the sensing method to the annunciator's physical form, which is not supplied.
4. Measure `Δt = t1 − t0` and uncertainty. Repeat over the specified load/environment envelope, queue/scheduling and sample-phase boundaries, and relevant communication conditions. Include cases around the project-controlled pressure/validity boundaries; invalid input must not be relabeled valid to simplify measurement. Confirm repeated qualifying events and any reset sequence follow the existing warning semantics.
5. Use worst-case analysis to justify coverage beyond observed trials and reconcile any discrepancy with stage budgets. Determine the number and selection of trials from the actual timing model; no sample count, percentile or reliability claim is invented.
6. Regress REQ-8 where timing changes affect COMP-2 scheduling/resources or IFC-3. Exercise warning behavior during motion inhibition whenever that lies within the unchanged operating conditions; do not silently redefine those conditions.

**Acceptance:** the defined end-to-end warning assertion is within 200 ms for the required operating conditions. Use a documented uncertainty rule; a conservative measured pass requires `Δt + U ≤ 200 ms` for the applicable nonnegative uncertainty bound U, plus an adequate worst-case coverage argument. A result above 200 ms is a failure for its executed configuration. A result whose uncertainty straddles the limit, whose stimulus validity is unknown or whose endpoint was not observed is inconclusive, not a pass. The existing 260 ms allocation must be repaired or replaced with a justified tighter bound before a general timing guarantee is supportable.

Record raw timestamps/observations, exact baseline hashes, setup and instrument identity, environment/load, procedure revision, deviations, uncertainty, maximum measured latency and analysis assumptions. Preserve failures. Planned output is `evidence/revision-b-results.json` plus referenced raw data; neither exists now. An authorized reviewer must assess applicability and any residual gaps before a separate acceptance decision.

## VER-8 — stop, recovery, motion and retained visibility

**Addresses:** unchanged REQ-8, N-02 and the protected operator note. **Methods:** implementation inspection and controlled integration test with observable motion inhibition, local stop/resume events, communications and sensor validity. **Proposed owner/reviewer:** controls test lead and operator representative.

Resolve the motion-output/recipient and latch-display bindings before execution. Record their configuration and instrument both logical permission and actual motion response. No stop-time bound is supplied in REQ-8; do not invent a deadline or treat a state bit as physical-motion evidence.

| Case | Stimulus | Required observation/criterion |
| --- | --- | --- |
| VER-8.a | While motion is requested, assert local stop | Motion is inhibited while stop is asserted; retained latch is visible. Local stop dominates a competing resume/motion request. |
| VER-8.b | Release stop with valid data available; provide no resume | Motion remains inhibited after release. No automatic transition to OPERATING. |
| VER-8.c | Assert stop, lose data/network, then release stop; restore data/network without resume | Inhibit persists through restoration, stop latch remains visible and no motion is authorized. A shift-handoff walkthrough can establish whether the display communicates that retained state. |
| VER-8.d | Restore data before releasing stop, and then release without resume | Same retained inhibition and visibility; event order must not create automatic recovery. |
| VER-8.e | Exercise inherited missing-data inhibit without a manual-stop event; restore data without resume | N-02 recovery rule holds: data restoration alone does not authorize motion. |
| VER-8.f | Request explicit local resume while stop remains asserted or data remains invalid | Remain inhibited. Later release/restoration must not treat that rejected request as a fresh authorization. Test a held/replayed request under the agreed IFC-3 semantics. |
| VER-8.g | With stop released, valid data and all other applicable guards satisfied, perform explicit local resume | The latch clears only via the eligible action; motion permission changes consistently with the operating logic. Observe subsequent commanded motion to avoid a test that passes merely because no motion was requested. |
| VER-8.h | Reconnect with queued remote commands; apply simultaneous stop/resume | Reconnection and queued remote commands do not substitute for local resume; stop remains dominant. Record ordering and operator-visible outcome. |

The old visibility intent remains a portion of this plan, but visibility alone cannot verify REQ-8. Separate raw motion, latch, interface and display observations; give every case an executed outcome only after it runs. Operator interpretation is a validation observation distinct from controller requirement verification.

Current coverage: REQ-7 and REQ-8 have planned activities; zero revision-B executions/results are supplied or produced, and neither requirement is verified or accepted for B by this package.
