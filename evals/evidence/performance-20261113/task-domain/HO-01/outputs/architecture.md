# Greenhouse vent controller — proposed architecture

Status: textual design proposal tied to [requirements.md](requirements.md). No live model or hardware has been changed. Source needs N-01–N-04 and decisions D-01–D-07 retain their meanings.

## Boundary and functional allocation

The system includes temperature sensing, controller logic, local stop/reset and fault indication, motor actuation, travel sensing and a remote dashboard interface. The operator, weather, greenhouse thermal dynamics and external network infrastructure influence behavior. Plant-temperature control performance and weather safety cannot be inferred from threshold logic alone.

| Function | Transformation | Candidate responsibility | Requirement allocation |
| --- | --- | --- | --- |
| F-01 | Accept/reject readings; detect freshness loss | C-01 sensor and C-02 MCU | R-06,R-12 |
| F-02 | Qualify temperature dwell; produce open/close requests | C-02 MCU | R-01–R-03,R-11,R-12 |
| F-03 | Arbitrate stop/fault/travel interlocks; inhibit motor | C-02 MCU, C-03 local stop, C-04 driver/motor | R-04–R-06,R-08,R-10 |
| F-04 | Expose local fault/mode and dashboard status | C-02 MCU, C-06 proposed local indicator | R-07 |
| F-05 | Serve scoped remote access with command/status checks | C-05 dashboard and network endpoint | R-09; constrained by R-04,R-08,R-10 |
| F-06 | Validate explicit recovery request and clear only eligible latches | C-02 MCU, C-07 operator/reset interface | R-05,R-08,R-11 |
| F-07 | Report and act on end-of-travel feedback | C-08 end switches, C-02,C-04 | Supporting design proposal for N-01; travel limits under D-06 |

C-01 → C-02 carries temperature over the candidate shared network. C-02 → C-04 carries mutually exclusive open/close/disable requests. C-08 → C-02 carries end-switch states. **Proposed additional path:** C-03 directly inhibits C-04 independently of successful network communication, with C-03 status also read by C-02 to latch the stopped mode. C-06 makes the N-03 fault visible when C-05 is unreachable. This path and indicator are design proposals beyond the original component list.

## Behavior and precedence

Maintain independent stop/fault causes rather than one flag that a later event can overwrite. Priority is local stop or latched data fault, then travel interlocks, then eligible automatic requests. Remote commands never override an active inhibit. Simultaneous open/close requests are rejected with motion inhibited as a proposed arbitration policy.

| State/event | Proposed response | Trace/status |
| --- | --- | --- |
| Automatic, fresh valid T ≥ 32 °C | Start/continue opening dwell; at elapsed 30 s request open if all inhibits are clear | N-01,R-01; D-01 timing semantics |
| A valid dip to T < 32 °C before opening qualification completes | Clear opening dwell; later high readings start at zero | N-01,R-02 |
| Automatic, fresh valid T < 28 °C | Start/continue closing dwell; at elapsed 60 s request close | N-01,R-03; reset on T ≥ 28 °C is proposal |
| 28 °C ≤ T < 32 °C | No new temperature-triggered move; clear dwell eligibility | Hysteresis proposal; whether an ongoing stroke completes is D-06 |
| Local stop actuated in any mode | Direct inhibit, latch manual-stop cause, clear dwell timers, show mode | N-02,N-04,R-04,R-05,R-10,R-11 |
| Fresh valid data absent for 5 s | Inhibit, latch data-fault cause, indicate fault; do not wait for a network acknowledgment | N-03,R-06–R-08; D-02,D-03 |
| Data returns or stop is released | Update status only; retain corresponding recovery latch | N-02,N-03,R-05,R-08 |
| Explicit authorized resume with stop released, current valid data and other inhibits clear | Clear eligible recovery causes, enter automatic idle, begin new dwell qualification | Proposal under D-04,R-11; never replay buffered motion commands |
| End switch reached in direction of motion | Remove drive in that direction | Proposed travel protection; stuck/conflicting switches and maximum run time need D-06 |
| Power return/startup | Start inhibited until validity and explicit recovery policy are satisfied | Conservative proposal, not supplied obligation; D-02,D-04 |

The requested response to missing data is stopping, not automatic movement to a presumed safe open or closed position. If the stopped position is unsafe in wind/rain, D-06 must reconcile that requirement with N-03 before a design is accepted.

## Interface contracts to complete

| ID | Direction/item | Required semantics and open limits |
| --- | --- | --- |
| I-01 | C-01 → C-02 temperature | °C, sensor identity, validity, unique sequence, acquisition age/timestamp. Nominal 1 s period only; jitter, transport delay, skew and invalid-value limits unknown. C-02 owns freshness decision; reception time alone may accept buffered stale data. |
| I-02 | C-03 → C-04 inhibit; C-03 → C-02 stop state | Local actuation must dominate motion irrespective of network service. Electrical polarity, broken-wire behavior, bounce, driver response and physical stopping measurements require design/verification. No safety rating is claimed. |
| I-03 | C-02 → C-04 motion; C-04 → C-02 status if available | Open/close/disable, exclusive directions, reset/boot default disable proposed. Driver latency, coast/holding behavior, stall sensing and feedback availability unknown. |
| I-04 | C-08 → C-02 travel state | Open/closed limits and invalid combination; switch polarity, debounce and action on failure under D-06. End switches do not themselves establish all intermediate positions. |
| I-05 | C-05 ↔ C-02 remote commands/status | Mode, fault causes, current value, age and acknowledgment; identify command origin and freshness. Missing connection cannot bypass C-03. Remote privileges and timeout/expiry are D-05. |
| I-06 | C-02 ↔ C-06,C-07 indication/recovery | Local data-fault visibility and explicit operator resume request, with clear eligibility/denial feedback. Means and responsible operator require D-04. |

## Timing and failure reasoning

Opening response comprises sample observation delay + transport delay + 30 s qualification from the chosen reference + scheduling/arbitration + driver response + mechanical travel. Closing uses 60 s. Only the dwell values are supplied; neither a full-travel deadline nor a worst-case overall response is established.

Missing-data response comprises the adopted 5 s age threshold + bounded timeout-task dispatch + disable propagation + mechanical stopping. Local-stop response bypasses the data path but still depends on electrical inhibition and mechanical stopping. Until these terms are measured/bounded and D-03 resolved, neither path has a defensible universal 50 ms guarantee.

Alternatives worth assessing: retain network sensing with explicit freshness metadata; move sensing onto a local link to remove network-loss dependence; implement stop solely in MCU logic versus direct driver inhibition plus a latched controller state. The direct local path is proposed because N-04 requires network-independent stop availability. It does not establish processor-fault tolerance, power independence or a safety integrity level. Shared supply, a single driver, MCU, software and mechanical assembly remain dependencies. A brake, watchdog, second sensor or processor would need a specific failure-control rationale, not an unsupported redundancy claim.
