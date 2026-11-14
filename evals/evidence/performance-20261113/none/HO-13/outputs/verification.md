# Verification index, proposed revision B

All revision-B activities below are planned and unexecuted. No live controller or controller execution tool is supplied. Document consistency checks do not verify controller behavior.

| Verification | Requirement | Evidence disposition |
| --- | --- | --- |
| VER-7 | REQ-7 | EVD-A-7 remains a historical revision-A record against 500 ms. Revision-B evidence is pending. |
| VER-8 | REQ-8 | Existing indicator-only plan is inadequate. Expanded motion and recovery verification below is pending. |

VER-7: establish the actual implementation configuration, controlled threshold and validity contract, and operating modes before execution. Retain the trigger “after the valid pressure input first meets the high-pressure condition during operation” and end event “assert the local high-pressure warning.” Identify an observable input-contract boundary and the actual local annunciator assertion. Do not substitute detector recognition or transmission of an alarm command for either endpoint.

Plan a synchronized end-to-end timing measurement from that trigger to that end event. Document stimulus accuracy, sensor/input observation, annunciator observation, timestamp alignment, instrument calibration, resolution and uncertainty. Before running, agree the conformance decision rule; a proposed conservative rule is that measured latency plus stated timing uncertainty must not exceed 200 ms. Values near the limit with unresolved uncertainty do not establish conformance.

Exercise the valid threshold transition under the project's operating conditions, including applicable worst-case sampling phase, processing load, communication/scheduling delay and annunciator behavior. Identify which stresses actually apply to the chosen implementation and record the coverage. Check input validity and threshold-boundary behavior to ensure timing improvements did not change the trigger semantics. Pair measurements with a complete timing allocation and justified worst-case path analysis: the largest observed sample by itself is not proof of a worst-case bound. Use the unchanged 200 ms criterion for revision B; do not average away an observed exceedance.

For each executed case, retain configuration/build identity, requirement revision or digest and criterion, VER-7 linkage, setup and instrument records, stimulus and operating conditions, raw synchronized traces, calculated latency, uncertainty, decision rule and outcome. Record actual deviations and coverage gaps. Bind results to the tested implementation and assess applicability again after relevant implementation changes.

VER-8: verify motion inhibition and stop-latch indication with observable motion or a justified motion-permission measurement, not the fault indicator alone. Prepare the following sequences and expected results:

1. Assert local stop while operating. Observe motion inhibition and the stop-latch indication. Keep stop asserted and attempt resume; inhibition must remain.
2. Release stop without resume. Inhibition must remain. A new explicit local resume with required conditions satisfied may remove this inhibit; it must not bypass independent interlocks or itself be treated as a motion command.
3. Assert stop, lose communication/sensor data, release stop and restore data/network without resume. Verify retained inhibition and visible stop latch after restoration. Repeat with restoration before stop release.
4. Lose required data without a local stop. Restore it without resume and verify no automatic authorization of motion, consistent with N-02 and the proposed state machine.
5. Attempt resume before required data is valid or before stop is released; restore the conditions afterward without a new resume. Verify inhibition remains. Check simultaneous stop/resume with stop precedence.
6. Change operator shifts during the outage. Confirm the incoming operator can see the retained stop latch after reconnect and that neither handover nor reconnection counts as local resume.

Record event ordering, the actual stop/data/resume inputs, motion or permission observations, display observations and the tested configuration. Verify warning behavior in every mode covered by the unchanged operating-condition contract as well; resolving motion recovery must not silently suppress REQ-7.

The proposed result path is `evidence/revision-b-results.json` relative to this revised baseline. It is intentionally absent because no revision-B tests have run. Its future contents must distinguish executed observations from analysis and planned work. The unchanged `report-old.json` is retained as historical evidence, not copied into that result path.
