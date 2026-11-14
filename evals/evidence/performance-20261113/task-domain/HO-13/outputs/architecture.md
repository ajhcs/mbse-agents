# Controller architecture, revision B — proposed revision

Status: coherent document proposal responding to CR-1, with unresolved implementation selection and verification. IDs and component/interface responsibilities are preserved. No physical timing measurements for revision B are available.

COMP-1 input interface forwards the sensor input to COMP-2 detector. COMP-2 sends the alarm command to COMP-3 local annunciator over IFC-2. IFC-1 is the sensor-to-detector interface. IFC-3 carries operator stop/resume intent to COMP-2.

## REQ-7 alert path and budget

The initiating event remains **the valid pressure input first meeting the high-pressure condition during operation**. The end event remains **assertion of the local high-pressure warning**. CR-1 changes neither event, input validity nor operating conditions. Do not restart the timing clock at COMP-2's detection output or stop it at the command on IFC-2; either would omit part of the defined claim. The exact observation points must be tied to the existing project-controlled input contract and warning interface, which are not supplied in detail.

The inherited allocation remains visible as an unresolved budget, not a claim of compliance:

| Stage | Inherited maximum | Responsibility |
| --- | --- | --- |
| COMP-1 interface processing | 150 ms | Input acceptance and forwarding through IFC-1 |
| COMP-2 detection | 80 ms | Determine high-pressure condition; issue warning command |
| COMP-3 warning assertion | 30 ms | Assert the local warning received through IFC-2 |
| Serial, nonoverlapping total | **260 ms** | REQ-7 end-to-end path |
| REQ-7 revision-B limit | **200 ms** | Approved by CR-1 |
| Allocated margin before any omitted delay | **−60 ms** | Unresolved |

These maxima are allocations under the stated serial/nonoverlapping assumption. They do not demonstrate an actual 260 ms observation or simultaneous achievement of all maxima. They cannot support the new guarantee as written. Identify any sensing/queue/transport/scheduling/assertion delays not already included; call their justified total H. Do not double-count delays already within stage bounds or assume H is zero.

The team has selected no implementation change. Engineering options, all unselected:

- **Reduce serial work/latency.** With COMP-2 and COMP-3 unchanged, COMP-1 would need a justified bound ≤ `90 ms − H`. Alternatively redistribute reductions among stages so `I + D + A + H ≤ 200 ms`, with explicit uncertainty/margin treatment. Inspect queueing and scheduling as well as processing time. No feasible reduction is yet demonstrated.
- **Change the critical path or introduce valid overlap.** Only if input causality permits it could parallel interface/detection yield `max(150,80) + 30 = 180 ms`, leaving at most 20 ms for all other terms. The present forwarding relationship implies a dependency; declaring concurrency without a new valid-input mechanism is not a repair. A revised local alert path must preserve the original trigger and actual local warning endpoint.
- **Replace/repartition a limiting function or component.** Obtain measurements and supplier/implementation bounds first; consider interference with motion inhibition and other tasks. No new hardware, priority scheme or supplier capability is assumed.
- **If the 200 ms requirement proves infeasible:** take an explicit trade back to the change authority. This package keeps the approved 200 ms criterion; it does not restore 500 ms or treat a waiver as verification.

IFC-1 needs the existing pressure units, threshold/validity semantics, rate, delay and error behavior recorded by reference to controlled project parameters. IFC-2 needs command semantics, transfer delay and correspondence to locally observable warning assertion. IFC-3 needs distinct local stop state and explicit local resume intent, with ordering/validity semantics. Those details are not supplied and remain open; their absence is not permission to alter them.

## REQ-8 and N-02 recovery correction

The revision-A state record allowed `INHIBITED → OPERATING` when stop was released and valid data returned, with no resume guard. That contradicts both the unchanged REQ-8 and authoritative N-02. It is replaced in this proposed architecture as follows. Names OPERATING and INHIBITED are retained; in this transition description they describe motion permission. They do not redefine REQ-7's operating conditions or imply warning suppression during a motion inhibit.

| Current state and event | Guard/action | Next state and observable condition |
| --- | --- | --- |
| OPERATING; local stop asserted | COMP-2 commands motion inhibition and latches the inhibit cause; active stop dominates any simultaneous resume | INHIBITED; motion remains inhibited and local stop latch is visible |
| OPERATING; missing data | Preserve the inherited transition to inhibition and record the data-loss cause; missing-data detection parameters remain the existing project contract | INHIBITED; motion inhibited; cause/status visible |
| INHIBITED; local stop released | Update current input state; retain the latch and motion inhibit | INHIBITED; release is not a resume event |
| INHIBITED; sensor data or network returns | Update health/connectivity state; retain the latch and motion inhibit | INHIBITED; restoring service is not authorization, and the stop latch remains visible |
| INHIBITED; explicit local resume intent through IFC-3 | Accept only with stop released and valid data present; if another applicable inhibit remains, retain inhibition. The explicit local action is necessary, not implied by health restoration | OPERATING only when eligible; otherwise remain INHIBITED with reason visible |
| Any state; stop assertion and resume arrive together | Stop takes precedence | INHIBITED |

Distinguish active causes from the retained recovery latch: a cause may be gone while deliberate resumption is still required. An eligible resume permits the existing operating logic to act; it is not itself an invented unconditional motion command. Treat replayed network commands or a resume request made while ineligible as incapable of clearing a later latch; this is a proposed implementation rule to enforce explicit local recovery, to be checked in VER-8. Detailed edge/level handling and reset behavior require the interface owner.

The source operator note is preserved verbatim in [source.md](source.md). Visibility must survive communications restoration and remain meaningful across a shift handoff. The source has not identified an indicator component or display interface for this latch. Allocate responsibility for reporting the latch to COMP-2, and leave the display binding open for design. COMP-3 is the high-pressure annunciator; do not silently reinterpret it as a motion actuator or a stop-latch display.

COMP-2's motion-inhibit output and the physical motion recipient are also not specified in the supplied architecture. Their binding and observable effect must be established before claiming REQ-8 implementation compliance. A controller flag alone is not evidence that motion is inhibited.

## Open design decisions

| ID | Affected records | Required decision/evidence; proposed owner |
| --- | --- | --- |
| DEC-B-1 | REQ-7, COMP-1–COMP-3, IFC-1/IFC-2, VER-7 | Select a feasible critical-path change and complete the end-to-end budget, including all dependencies and overhead; architecture/performance lead |
| DEC-B-2 | REQ-7, VER-7, EVD-A-7 | Retrieve existing parameter/configuration/test setup records; reconcile 460 ms historical observation with 260 ms allocations. The numerical 200 ms difference is not a known overhead mechanism; test/configuration lead |
| DEC-B-3 | REQ-8,N-02,IFC-3,VER-8 | Specify local resume event handling, simultaneous events, actual motion-output binding and stop-latch display. Preserve explicit local authority and protected note; controls/operator representatives |
| DEC-B-4 | N-01,N-02,VER-7,VER-8 | Confirm startup/power-return semantics and warning behavior within the unchanged operating envelope. No source change is authorized by this draft; requirement owner + controls lead |

Source links establish basis, allocations assign responsibility, and VER links identify planned evidence. None asserts satisfaction or acceptance.
