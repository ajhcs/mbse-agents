# Controller architecture, proposed revision B

This is a proposed reconciliation and implementation work plan. No implementation option has been selected or measured for revision B.

COMP-1 input interface forwards the sensor input to COMP-2 detector. COMP-2 sends the alarm command to COMP-3 local annunciator over IFC-2. IFC-1 is the sensor-to-detector interface. IFC-3 carries operator stop/resume intent to COMP-2.

The current allocations are retained below as an unresolved design baseline, not a feasible revision-B budget. They assume serial, nonoverlapping stages.

| Stage | Current maximum allocation |
| --- | --- |
| COMP-1 interface processing | 150 ms |
| COMP-2 detection | 80 ms |
| COMP-3 warning assertion | 30 ms |
| Sum | 260 ms |

The sum exceeds the 200 ms REQ-7 criterion by 60 ms. This allocation cannot guarantee the new requirement. It is not a measurement proving every implementation run takes 260 ms. Establish whether sampling phase, scheduling, queuing, IFC-2 transfer and annunciator response are already included; any uncovered delay must also be budgeted from the unchanged input trigger through actual local warning assertion. The historical 460 ms observation cannot be explained by the supplied 260 ms allocation alone; its configuration and detailed timing records are insufficient to reconcile that gap.

Engineering options for selection, not approved changes:

- Reduce COMP-1 processing latency through a measured and justified implementation change. With the other two allocations unchanged, 90 ms for COMP-1 would merely reach 200 ms and leave no allowance for uncovered delay or uncertainty. A robust allocation must include those contributions and justified margin.
- Reduce latency across COMP-1, COMP-2 and COMP-3 and explicitly allocate any interface or scheduling delay. Demonstrate a complete worst-case path bound rather than moving delay into an uncounted stage.
- Consider architectural concurrency or a shorter alarm path only if causal dependencies, input validity, detection correctness and interface behavior remain satisfied. Replace the serial sum with a justified critical-path analysis if stages genuinely overlap.

Select an option after investigating the path and the 260/460 ms discrepancy. Do not change the pressure threshold, move the trigger downstream, terminate timing at command transmission, or weaken operating conditions to meet the criterion.

Proposed motion-inhibit transitions reconcile the recorded diagram with N-02 and unchanged REQ-8:

| State and event | Proposed next state and observable behavior |
| --- | --- |
| OPERATING; local stop asserted or required sensor data missing | INHIBITED; motion inhibited and latch state recorded |
| INHIBITED; stop released, data restored, or network reconnected, without a new explicit local resume | Remain INHIBITED; retain motion inhibit and the visible stop latch after reconnection |
| INHIBITED; resume requested while stop remains asserted or data remains invalid | Remain INHIBITED; do not retain this request as permission for automatic later recovery |
| INHIBITED; new explicit local resume with stop released and required data valid | Permit removal of this inhibit and transition to OPERATING, subject to existing independent interlocks; this does not itself command motion |
| Any state; stop assertion coincident with resume | Stop takes precedence; remain or enter INHIBITED |

The fresh-resume and precedence details are proposed design resolutions for review, not new approvals. Stop release and data restoration must never themselves authorize motion. Preserve the stop-latch indication through network recovery and shift change, consistent with the operator note. A generic fault indicator is not evidence that the stop latch remains visible.

These state labels concern motion permission. They must not redefine REQ-7's existing “during operation” condition or introduce a new exception to warning behavior. Resolve the exact operating-mode and interface observation definitions using the existing project contracts before implementation and verification.

No physical timing measurements for revision B are available.
