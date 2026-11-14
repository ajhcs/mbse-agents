# Traceability, decisions and risk register

Baseline: GH-DRAFT-01. All links describe draft allocation or planned coverage; none denote a satisfied or accepted requirement. Raw source wording/locators are in [00-review-guide.md](00-review-guide.md).

## Source-to-requirement disposition

| Raw source ID / locator | Meaning retained | Draft requirement disposition | Architecture and verification implication |
|---|---|---|---|
| N-01; request stakeholder paragraph | Valid inside reading, `>=32 deg C` for 30 s; brief below-32 dip resets; close `<28 deg C` after 60 s. | RQ-01/RQ-02/RQ-03; DR-01 supports eligibility. Opening reset is preserved; closing reset semantics remain D-02. | F-01/F-02/F-03; I-01; VA-01/VA-02/VA-03/VA-11/VA-14; SV-01. Sampling cannot prove all unseen physical dips. |
| N-02; request stakeholder paragraph | Local manual stop overrides motion; explicit action to resume automatic mode. | RQ-04/RQ-05; DR-02 supports arbitration. | F-03/F-04/F-05; I-02/I-03/I-04/I-07; VA-04/VA-05/VA-12/VA-13/VA-14; SV-02. |
| N-03; request stakeholder paragraph | Missing data for 5 s stops motion, shows fault; returning data does not automatically resume. | RQ-06/RQ-07/RQ-08; DR-01/DR-02 support enforcement. | F-01/F-03/F-04/F-05/F-06; VA-06/VA-07/VA-08/VA-11/VA-12/VA-13/VA-14; SV-02/SV-03. Missing-data origin and physical stop budget remain open. |
| N-04; request stakeholder paragraph | Remote access desired; local stop must work during network failure. | RQ-09 is an unmeasurable intent pending D-07; RQ-10 preserves local operation during network failure. | F-04/F-05/F-07; AD-01 proposes local direct inhibit; VA-09/VA-10/VA-13/VA-14; SV-04. |
| No raw ID; request candidate paragraph | Nominal 1 s shared-network sensing; one MCU, driver, end switches and dashboard. | Architecture design input only. DR-01/DR-02 derive engineering constraints from N-01/N-02/N-03/N-04 and this topology. | C-02/C-03/C-05/C-07; single-point/common dependencies recorded. Maximum rate, travel and stale detection unproved. |
| No raw ID; request manager sentence in candidate paragraph | Universal 50 ms stop deadline proposed without a source. | Not adopted as a requirement, budget, acceptance criterion or proven result. D-04 requires a justified stop criterion. | VA-04/VA-10/VA-14 cannot use 50 ms as an authoritative threshold. |
| No raw ID; request uncertainty/evidence sentences | Jitter, travel, stale detection, operator response, weather/safe position unknown; no test/reliability data. | D-01/D-03/D-04/D-05/D-08/D-09/D-10/D-11/D-12; no invented numerical replacements. | All physical performance and reliability claims remain unsupported. |

## Requirement-to-allocation and verification trace

| Requirement | Raw source basis | Functions → components | Interfaces | Planned verification | Current evidence |
|---|---|---|---|---|---|
| RQ-01 | N-01, constrained by N-02/N-03 | F-02/F-03 → C-02/C-03/C-04 | I-01/I-04/I-07 | VA-01/VA-13/VA-14 | None; unverified |
| RQ-02 | N-01 | F-01/F-02 → C-02 | I-01 | VA-02/VA-11/VA-14 | None; unverified |
| RQ-03 | N-01, constrained by N-02/N-03 | F-02/F-03 → C-02/C-03/C-04 | I-01/I-04/I-07 | VA-03/VA-13/VA-14 | None; unverified |
| RQ-04 | N-02/N-04 | F-03/F-04/F-05 → C-01/C-02/C-03/C-04 | I-02/I-03/I-04/I-07 | VA-04/VA-10/VA-13/VA-14 | None; unverified |
| RQ-05 | N-02 | F-03/F-05 → C-01/C-02/C-05 | I-02/I-04/I-05 | VA-05/VA-13 | None; unverified |
| RQ-06 | N-03 | F-01/F-03/F-04 → C-02/C-03/C-04 | I-01/I-04/I-07 | VA-06/VA-11/VA-13/VA-14 | None; unverified |
| RQ-07 | N-03 | F-06 → C-02/C-05/proposed C-06 | I-05/I-08 | VA-07/VA-13/VA-14 | None; unverified |
| RQ-08 | N-03 | F-03/F-05 → C-01/C-02/C-05 | I-01/I-02/I-04/I-05 | VA-08/VA-13 | None; unverified |
| RQ-09 | N-04 | F-07 → C-05/C-02/network | I-05 | VA-09 | None; scope undefined |
| RQ-10 | N-04/N-02 | F-04/F-05 → C-01/C-03/C-04 | I-02/I-03/I-07 | VA-10/VA-13/VA-14 | None; unverified |
| DR-01 | N-01/N-03; RQ-01/RQ-02/RQ-03/RQ-06/RQ-08 | F-01/F-02 → C-02/sensor/network | I-01 | VA-11/VA-06/VA-14 | None; provisional |
| DR-02 | N-02/N-03/N-04; RQ-04/RQ-06/RQ-10 | F-03/F-04 → C-02/C-03 | I-03/I-04/I-07 | VA-12/VA-04/VA-13/VA-14 | None; provisional |

Many-to-many links are deliberate: stop and fault guards constrain thermal behavior, and one scenario can address several requirements. No requirement is orphaned; each has an identifiable source or parent, function allocation and planned activity. Link existence does not demonstrate semantic correctness or verification success.

## Decisions required for a final design

All entries are open. Owners below are proposed accountable roles, not evidence of agreement or assigned personnel. A final disposition should record decision, source amendment if any, rationale, date/approver, changed artifact IDs and affected verification activities.

| ID | Decision / missing acceptance definition | Supported proposal or options, with consequence | Proposed owner; affected records |
|---|---|---|---|
| D-01 | What constitutes a valid inside reading and “stays at/above” in a sampled stream? Define accuracy, sensor identity, first qualifying event, timestamp origin, maximum gap/jitter and invalid/gap reset behavior. | Propose qualification over eligible samples on controller monotonic time, reset high timer on every eligible sub-32 sample and on invalidity/gap per approved rule. This cannot establish all between-sample physical dips. Continuous physical-temperature intent would need additional sampling/sensing justification. No numerical gap/age/accuracy bound is selected. | Owner + sensor/controls engineer; RQ-01/RQ-02/DR-01, I-01, VA-01/VA-02/VA-11/VA-14, SV-01. |
| D-02 | Does the 60 s closing interval require uninterrupted `<28`? What resets it; what happens at 28, gaps and recovery? | Propose uninterrupted eligible below-28 samples and reset at `>=28`, with new qualification after inhibition, but this is unapproved. Source only explicitly states a reset for opening. | Owner + controls engineer; RQ-03, F-02, VA-03/SV-01. |
| D-03 | What explicit actions clear manual-stop authorization and data-fault inhibition? Can acknowledgment and automatic enable be combined? Define startup/power-cycle state and response if operator never acts. | Propose deliberate guarded enable only with stop released and fresh data; preserve fault/stop reasons separately. Propose inhibited startup and restarted thermal timers. N-03 forbids automatic movement on return but does not prescribe the specific reset protocol. Operator response time is unknown and cannot be credited as protection. | Technician + maintenance + owner; RQ-05/RQ-08, F-05, VA-05/VA-08/VA-13, SV-02. |
| D-04 | Define local stop event reference, physical stopping criterion, allowable residual travel/force, load envelope, latency and release/reset wiring. Resolve manager's 50 ms proposal. | Propose AD-01 direct local latching inhibit; distinguish contact-to-driver and driver-to-physical-halt times. Derive justified limits from hazards and mechanical/driver data, then measure. No source supports a universal 50 ms bound; neither acceptance nor feasibility is established. | Technician/owner + hardware/mechanical/safety engineer; RQ-04/RQ-05/RQ-10/DR-02, I-02/I-03/I-04/I-07, VA-04/VA-10/VA-14. |
| D-05 | Does “missing for 5 s” start at last packet receipt, last accepted fresh receipt or sample acquisition? How do stale/duplicate/invalid packets, clock mapping and scheduler latency affect detection? | Propose last accepted fresh receipt on MCU monotonic clock, with separate acquisition-age eligibility and rejected packets not refreshing it. Treat invalid/stale as unavailable only if approved. Define the event at the 5 s threshold and separate detection/output/physical stop response. Do not replace source 5 s with an invented timeout. | Maintenance + controls/sensor engineer; RQ-06/RQ-08/DR-01, I-01, VA-06/VA-08/VA-11/VA-14. |
| D-06 | Where is the missing-data fault observable during network loss? Define indicator content, visibility, timing, persistence and clearing. | Propose C-06 local fault indication plus dashboard status. Dashboard-only depends on the same failed network. Local power-loss display availability still needs assessment. | Maintenance + owner; RQ-07, AD-03, I-08, VA-07/SV-02. |
| D-07 | Define remote access: monitor/control, authorized roles, security, availability, stale-command treatment and whether remote recovery is allowed. | Dashboard is candidate only. Propose stop/fault override all remote commands and no remote clearance of a local stop until expressly approved. Scope and measurable acceptance remain absent. | Owner + software/security/controls engineer; RQ-09/RQ-05/RQ-10, I-05, VA-09/VA-05/VA-10, SV-04. |
| D-08 | How does a qualified demand persist during travel? Define cancellation/reversal, simultaneous demands, end-limit handling, switch failure and travel timeout. | Source does not specify completion time or motion policy. Propose exclusive directions and end-limit inhibit. Reversal deadtime and timeout must follow actual driver/travel evidence; no values selected. | Owner + mechanical/hardware/controls engineer; RQ-01/RQ-03/DR-02, C-03/C-04/C-07, I-04/I-06/I-07, VA-01/VA-03/VA-12/VA-13. |
| D-09 | Define wind/rain/temperature/load envelope, hazards, safe position and holding behavior after stop or power/data loss. | Neither open nor closed is justified as universally safe. N-02/N-03 require stopping; automatic weather repositioning could conflict and needs an explicit source decision. Mid-travel stop can leave exposure or allow wind-driven movement. | Owner + mechanical/safety engineer; RQ-04/RQ-06/RQ-10, C-04, VA-04/VA-06/VA-10/VA-14/SV-03. |
| D-10 | Set timer resolution/accuracy, command/display reaction allowance, end-to-end budgets, observation reference and measurement uncertainty/tolerances. | Preserve 30/60/5 s source values; define their event semantics and justified tolerance. Unknown scheduling and network maxima prevent closed budgets. Nominal 1 s sampling is not a bound. | Controls/hardware engineer + owner/maintenance; RQ-01/RQ-02/RQ-03/RQ-04/RQ-06/RQ-07/RQ-10, VA-14 and affected boundary tests. |
| D-11 | Select actual sensor, MCU, driver, motor/vent, switches, power/defaults, wiring and indicator interfaces. Obtain mechanical travel/holding and electrical disable data. | Retain single MCU/driver as candidate. Validate direct inhibit and default states; do not assume disable brakes, end switches are diagnostic or power restoration cannot move. | Hardware/mechanical engineer; all physical allocations, I-01 through I-08, VA-04/VA-10/VA-12/VA-13/VA-14. |
| D-12 | Establish reliability/availability goals, hazard-review basis, common-cause assessment and required assurance/review/qualification. | No supplier reliability data or execution results exist. Do not infer redundant, fail-safe, certified or quantitatively reliable behavior from component count or a local wire. Get evidence before assigning probabilities. | Owner + responsible systems/safety engineer; component dependencies, RQ-09/RQ-10, future evidence plan, SV-04. |

## Risk and assumption register

These are qualitative concerns, not completed hazard analysis or scored reliability estimates.

| ID | Concern / assumption and source link | Impact, proposed response and remaining evidence |
|---|---|---|
| RK-01 | Nominal 1 s data can omit brief physical dips or mask old readings; N-01/N-03, candidate sample stream. | False thermal qualification or missed data loss. Resolve D-01/D-05; validate schema, age and jitter. No smoothing assumption is permitted to erase a valid dip. |
| RK-02 | Sensing and dashboard share network; N-03/N-04. | Loss of both data and remote fault visibility. Local stop route and proposed local indicator reduce transport dependency; prove their behavior with VA-07/VA-10. |
| RK-03 | One MCU/driver and common power/mechanics; candidate paragraph, N-02/N-03/N-04. | Stop/fault logic or driver can fail together; disable may not arrest/hold the vent. D-04/D-11/D-12 and hardware/load evidence needed. No independence claim. |
| RK-04 | Wind/rain and safe position unknown; request uncertainty, N-01/N-03. | Stopping at an arbitrary position may create damage/exposure. D-09 must reconcile stop obligations and environment; no automatic close/open fallback assumed. |
| RK-05 | Stop release/data restoration/remote reconnect may implicitly restart; N-02/N-03/N-04. | Unintended movement. Separate latch and authorization states; D-03/D-07 and VA-05/VA-08/VA-13. Startup inhibit is proposed, not a source fact. |
| RK-06 | End switches and travel time unspecified; candidate paragraph. | Overtravel, contradictory limits or unsafe reversal. D-08/D-11; obtain mechanism data and verify limit/reversal behavior; do not invent travel timeout. |
| RK-07 | Universal 50 ms lacks source and mechanical evidence; request manager sentence. | Unverifiable requirement or falsely claimed stop performance. Keep unapproved, derive a justified criterion through D-04, then test actual response. |
| RK-08 | Operator response and reliability data absent; request uncertainty/evidence sentences. | Fault recovery may remain inhibited indefinitely; no human timing or availability can be credited. SV-02/SV-04 and D-12 identify needed evidence and operational arrangements. |

There is no blocker to delivering this draft. Final design approval and unconditional verification are blocked by the open contracts above and absent hardware/supplier/test evidence. The next work should resolve the owners' decisions, revise this baseline with preserved IDs and then execute the configured evidence plan.
