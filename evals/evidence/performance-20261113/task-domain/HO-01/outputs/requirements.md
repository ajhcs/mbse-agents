# Greenhouse vent controller — proposed requirements baseline

Status: review draft. Source: `../request.md`, supplied packet HO-01, case version 1.0. No design approval, implementation, executed test, or reliability estimate is implied. Source IDs are retained below; new R-, F-, C-, I-, D-, and V-IDs identify draft records and their links.

## Source register

- **N-01 Owner:** Open the vent when a valid inside-temperature reading stays at or above 32 deg C for 30 s. A brief dip below 32 resets the interval. Close below 28 deg C after 60 s.
- **N-02 Technician:** A local manual stop overrides motion; resuming automatic mode requires an explicit action.
- **N-03 Maintenance:** If data is missing for 5 s, stop motion and show a fault; do not automatically resume motion after data returns.
- **N-04 Owner:** We want remote access, but the local stop must work during network failure.

The candidate parts and nominal 1 s sampling rate are proposals, not source obligations. The manager's 50 ms deadline has no supplied rationale and is **not adopted**. It remains D-03, distinct from the sourced 5 s missing-data interval.

## Draft requirements

Acceptance below refers to commanded behavior unless a physical response is explicitly stated. Final timing tolerances and measurement reference points remain open in D-01 through D-03.

| ID | Statement and acceptance intent | Basis/type | Allocation; verification | Status |
| --- | --- | --- | --- | --- |
| R-01 | In automatic mode with motion permitted, the controller shall request opening when valid inside-temperature readings have satisfied T ≥ 32 °C for a continuous 30 s qualification interval. It shall not request opening earlier on that interval. | N-01; source-derived | F-02/C-02; V-01 | Draft; sampled continuity and request latency need D-01 |
| R-02 | The controller shall reset the opening qualification interval when an accepted valid reading is below 32 °C, including a single brief sampled dip. A subsequent qualifying reading shall begin a new interval. | N-01; source-derived | F-02/C-02; V-01 | Draft |
| R-03 | In automatic mode with motion permitted, the controller shall request closing after valid inside-temperature readings are below 28 °C for 60 s. A reading of exactly 28 °C shall not qualify as below 28 °C. | N-01; source-derived; continuous low interval interpretation proposed | F-02/C-02; V-02 | Draft; reset and observation semantics in D-01 |
| R-04 | Actuation of the local manual stop shall override automatic and remote motion requests and stop vent motion. | N-02, N-04; source-derived | F-03/C-03,C-04; V-03,V-06 | Draft; physical stopping time needs D-03 |
| R-05 | Following a local manual stop, the controller shall remain inhibited until an explicit operator action requests resumption of automatic mode; releasing the stop alone shall not resume motion. | N-02; source-derived | F-03,F-06/C-02,C-03,C-07; V-03,V-05 | Draft; authority/action definition in D-04 |
| R-06 | If temperature data is missing for 5 s, the controller shall stop motion. | N-03; source-derived | F-01,F-03/C-02,C-04; V-04 | Draft; missing-data age and physical response defined by D-02,D-03 |
| R-07 | On detection of the R-06 condition, the controller shall show a data fault. | N-03; source-derived | F-04/C-02,C-06; V-04 | Draft; indication location/latency in D-02,D-04 |
| R-08 | Return of temperature data alone shall not resume vent motion after an R-06 stop. | N-03; source-derived | F-03,F-06/C-02,C-07; V-05 | Draft; authorized reset policy in D-04 |
| R-09 | The system shall provide remote access. | N-04; stakeholder objective captured | F-05/C-05; V-06 | Incomplete: monitoring/control, users, availability, and security scope in D-05 |
| R-10 | The local manual stop shall remain effective during a network failure, including failure of the network carrying temperature data or dashboard commands. | N-04 with N-02; source-derived | F-03/C-03,C-04; V-06 | Draft; implementation effectiveness unverified |
| R-11 | On a fault or stop, the controller shall clear qualification timers and require a new qualifying interval following authorized resumption with valid data. | Derivation proposal from N-01–N-03: avoid stale timer completing immediately after recovery | F-02,F-06/C-02; V-05 | Proposed, requires D-04 decision |
| R-12 | Invalid, duplicate, or stale readings shall not advance a temperature qualification interval or silently clear a missing-data fault. | Derivation proposal from valid-reading condition in N-01 and missing data in N-03 | F-01,F-02/C-02; V-04,V-05 | Proposed; validity/freshness limits in D-02 |

N-01 is covered by R-01–R-03; N-02 by R-04–R-05; N-03 by R-06–R-08; N-04 by R-09–R-10. R-11–R-12 carry explicit derivation rationales and are not accepted additions. No requirement claims the candidate architecture already satisfies it.

## Decisions needed for a final baseline

| ID | Decision and proposed owner | Why it changes the design; evidence needed |
| --- | --- | --- |
| D-01 | Owner + control engineer: define sampled continuity, timer start, jitter tolerance, threshold accuracy, and opening/closing output deadlines. | Nominal 1 s sampling cannot establish physical continuity between samples. Proposed timer starts at first accepted qualifying sample, uses elapsed monotonic time, and resets on disqualifying or invalid/gapped data; 30 samples alone do not equal 30 s. Need sensor accuracy, sample/transport jitter measurements and owner agreement. Confirm closing interval reset on T ≥ 28 °C. |
| D-02 | Controls + maintenance: define validity, stale data, startup with no samples, age reference, clock synchronization and fault indication. | Proposed timeout at age ≥ 5 s since last genuinely fresh valid sample; first-sample wait begins at startup. Replayed packets must not reset freshness. Source timestamps with bounded skew or sequence/age protocol are needed if network buffering can hide stale readings. Need transport behavior and sensor failure modes. |
| D-03 | Mechanical/control lead + owner: define safe stopping response, its reference points, and allowable time. | The sourced 5 s absence trigger is separate from detection scheduling, driver disable and mechanical stopping. Measure travel/coast/load and assess injury/overtravel/weather consequences. A universal 50 ms deadline is unsupported; accept, revise or reject it only with a hazard/performance basis. |
| D-04 | Owner + maintenance: define reset authority and explicit action, local fault visibility, operator response, startup/power-return behavior, and behavior when several stop causes overlap. | Proposed acknowledged reset only after stop released and data healthy, with new timers; clearing one cause must not clear another. Operator response cannot be assumed fast enough to protect plants or people. Need operational walkthrough and power-loss review. |
| D-05 | Owner + network lead: define remote-access functions, authorization, unavailable/stale dashboard behavior and command expiration. | Monitoring and remote motion control impose different risks. No remote request may bypass local inhibit or clear a fault without an approved explicit recovery action. Need intended users and command semantics. |
| D-06 | Owner + mechanical/environment lead: define operating envelope, wind/rain behavior, safe position, travel limits and actuator holding. | Stopping mid-travel is a sourced motion response, not proof of an environmentally safe position. Need vent/load data and outdoor conditions; opening, closing or holding can have different consequences. |
| D-07 | Reliability/maintenance lead: establish required availability, fault handling and diagnostic coverage if quantitative claims are wanted. | One MCU, shared network, power and motor driver are common dependencies. No failure probabilities or supplier reliability data were supplied; no reliability total or independence claim is supportable. |
