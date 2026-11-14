# Medication-container transport — operational scenario draft

Status: proposed operational agreement, not an approved policy or implemented robot design. Source is `../request.md` (HO-07). The supplied facts are: a service robot hands a medication transport container to authorized staff; medication selection and dosing are outside the boundary; unavailable recipients, connectivity loss and recovery need coverage. All scenario and decision IDs below are newly assigned draft IDs.

The intended outcome is delivery of the identified container to a staff member authorized for that handoff, with an accountable custody record and a controlled disposition when delivery cannot complete. Delivery speed alone is insufficient. No current workflow, staffing plan, authorization technology, lock, local storage capability, clinical handling limit or timing target was supplied.

## Boundary, roles and authority

Inside the operational boundary are mission assignment, transport, recipient contact, authorization checking, container identification, physical handoff, custody acknowledgment, exception management and recovery. Medication selection, dose determination, administration and judgment about medication suitability stay with the responsible clinical service outside this boundary. Transport staff may identify a handling concern and refer it; the robot does not infer suitability.

These are proposed responsibilities to confirm with the service owner, not claims that the roles are staffed today:

| Actor | Decision or responsibility | Limit |
| --- | --- | --- |
| Dispatching staff/custodian | Identify the container and destination, establish the initial custody record, accept an authorized return | Dispatch does not establish dosing correctness within this transport system |
| Receiving staff | Establish identity and current authority for this container/handoff; accept or decline receipt; acknowledge physical possession | Proximity, a uniform or knowing the destination does not establish authority |
| Duty transport supervisor | Own exceptions; authorize wait, reassignment, assisted collection, return or mission cancellation within policy; reconcile uncertain custody | Cannot create clinical authority or waive handling limits without the responsible service |
| Robot/transport system | Execute an authorized mission, present status, support verification and record transport/handoff events; retain control pending an allowed transfer | Does not choose a substitute recipient, waive authorization or assign medication decisions |
| Authorization service/policy owner | Define who may receive which deliveries and how that authority is checked, including expiry and revocation | Connectivity restoration alone does not reauthorize a recipient |
| Maintenance/recovery staff | Restore transport capability under supervisor direction | Maintenance access does not itself confer authority to take the container |

Distinguish **physical possession** from **accountability**. While a robot carries the container, the service must name an accountable dispatch/transport custodian; a machine is not assumed to hold human accountability. The custody record links container ID, mission ID, prior custodian, receiving identity, authorization basis, transfer event and exception state. Minimize content to what transport needs; no medication-selection data is assumed necessary.

Proposed modes are awaiting dispatch, in transit, waiting for recipient, handoff pending, completed, degraded/held, returning and reconciliation required. Transitions require observable guards, below. The service must choose the authoritative custody-transfer event (D-02); the draft uses confirmed physical receipt plus an attributable acceptance record. A delivery command or an unlock action alone is not proof of receipt.

## SC-01 — normal authorized handoff

**Trigger:** dispatching staff assign an identified container to a destination. **Preconditions:** mission authorized; route/handling conditions are within an agreed envelope; the transporting custodian and intended recipient role are known; a method exists to retain and identify the container. **Initial mode:** awaiting dispatch.

1. Dispatching staff confirm container and mission identities and place the container under the transport service's agreed control. The system records dispatch acceptance and presents the destination. Staff resolve discrepancies before departure.
2. The robot transports the container and reports mission state by the available approved means. The accountable custodian remains recorded during transit.
3. At the destination, the robot enters waiting-for-recipient mode and requests the designated staff role. A staff member responds. This contact is not a custody transfer.
4. Staff provide identity; the system or responsible operator checks current authority for this handoff using the approved process. Staff and system match container/mission identity. A mismatch, expired authority or refusal leads to SC-02 or supervisor review with no release.
5. Once authority and container identity are confirmed, the system enters handoff-pending mode. Staff intentionally accept the transfer; the container is made available using the selected mechanism. The system observes or obtains attributable confirmation of physical receipt and records the agreed custody event. The exact order and mechanism need D-02/D-03 so that a failure cannot silently produce two custodians or none.
6. Only after the transfer completion conditions are satisfied does the mission become completed. Staff can see that they have accepted custody; dispatch/supervision can see the completed or pending-reconciliation status.

**Final condition:** receiving staff possess the identified container, the prior transporting custodian is relieved under the agreed policy, and the record reflects the same event. If acknowledgment is missing after apparent removal, enter reconciliation required; do not declare failure and deliver a second container automatically. Connectivity interruption branches to SC-03.

## SC-02 — recipient unavailable, declines, or is unauthorized

**Trigger:** no eligible recipient responds at the destination, staff decline receipt, or authority cannot be established. **Initial mode:** waiting for recipient; container remains under transport control with the existing accountable custodian.

1. Present an intelligible waiting/not-completed state. Do not leave the container unattended, transfer it to a convenient nearby person, or record delivery based on arrival.
2. Use the approved contact method to notify the receiving team and duty supervisor. Record whether the notification was sent, delivered or acknowledged; sending it does not establish that someone knows about the delay.
3. Wait only within the service-approved waiting period, route occupancy constraints, energy reserve and container handling conditions. No values are supplied. If continued waiting would violate a limit, use the predefined contingency and escalate; do not assume a supervisor will respond in time.
4. The supervisor chooses an allowed disposition: continue waiting, name an authorized substitute, arrange authorized assisted collection, or return to the dispatching service. Reassignment is explicit, traceable and checked against current authority; it is not a robot guess.
5. A substitute recipient rejoins SC-01 at identity/authority verification. An authorized return ends only when dispatch staff accept physical possession and return custody. Cancellation while still carrying the container changes mission intent, not custody.

**Final conditions:** either a valid handoff completes, an authorized return completes, or the mission remains visibly held with a named accountable custodian and escalation owner. Absence of both recipient and supervisor is an unresolved operational contingency in D-04, not permission to release.

## SC-03 — connectivity loss

**Trigger:** loss of connectivity needed for supervision, authorization or custody records. **Detection:** the system identifies the affected service and makes degraded state locally observable by an available method; network alert delivery cannot be assumed during the outage. Detection latency and remaining functions need D-03/D-05.

| Loss point | Proposed operational response and custody consequence |
| --- | --- |
| Before dispatch or en route | Do not initiate a new mission that depends on unavailable authorization or supervision. For an active mission, retain container control and the existing accountable custodian. Use an approved local route to an agreed holding point or controlled halt, according to the motion/obstruction assessment. Do not assume that stopping immediately in a doorway is acceptable or that navigation works offline. |
| At recipient check, before release | Hold the handoff if current authority cannot be verified. An offline authorization route is allowed only if the service explicitly approves its scope, freshness/revocation rules and record method. Cached identity alone does not establish current authority. |
| During physical handoff, before completion is certain | Determine what can actually be observed. If still retained, keep it retained. If staff already possess it, do not pretend robot custody persists or automatically take it back. Enter reconciliation required, show transfer uncertainty, retain mission/container/identity/time evidence and invoke the approved local supervisor contact or witnessed fallback. |
| After confirmed physical receipt and acceptance but before central acknowledgment | Preserve the completion event in the approved local or witnessed record and flag synchronization pending. Do not repeat the handoff, replay a release command or assign a second delivery merely because the server did not acknowledge. If no trustworthy local record exists, treat it as an uncertain transfer and reconcile. |

Functions that depend on connectivity remain unavailable. Local containment, motion, recipient prompts and record persistence are **design assumptions to verify**, not capabilities established by this scenario. D-03 must identify a viable manual fallback if the platform cannot preserve the needed state. While held, handling-condition and energy limits continue to apply; communications loss does not pause them. The appropriate clinical service decides the disposition of a container whose handling acceptability is in doubt.

## SC-04 — recovery and resumption

**Trigger:** communication or a failed capability returns, or authorized recovery staff attend. **Initial mode:** degraded/held or reconciliation required.

1. The system reports restored service while retaining the prior mission, fault and custody state. Reconnection alone does not trigger movement, release or a new mission.
2. The supervisor and system reconcile container identity and actual possession against local and central events. Resolve incomplete or conflicting transfers with the people involved. Preserve the discrepancy and resolution rather than overwriting the history to make records agree.
3. Revalidate current recipient authority, destination, mission status, handling conditions, route and available power. Discard or explicitly reject expired/duplicate queued commands; identify events so reconnect/retry does not cause a second physical transfer.
4. With custody known and all required guards satisfied, the authorized supervisor/operator explicitly chooses resume, reassign, return, assisted collection or cancellation. Continuing to hold is a valid unresolved state if the guards cannot be established.
5. Resume at a defined point: in-transit mission resumes transport; an unreleased container resumes SC-01 at authority verification; an already completed handoff reconciles its record without another release; a return resumes the authorized-return path in SC-02.

**Final condition:** one known accountable custody state, an explicit mission disposition, resolved or visibly outstanding discrepancies, and an operator-visible status. Restored network availability without these conditions is not completed recovery.

## Decisions, assumptions and observations

| ID | Operational decision to obtain; proposed owner | Design assumption that must not be mistaken for that decision |
| --- | --- | --- |
| D-01 | Which staff roles may receive each mission and who may reassign? Service/authorization owner | Badge, password, biometric or online service is a mechanism choice; none is supplied |
| D-02 | What exact physical/acknowledgment event transfers custody, and how is a disputed event resolved? Dispatch/receiving services | A lock sensor, camera or database transaction may provide evidence but does not alone define accountability |
| D-03 | Which transport/handoff functions may continue offline, with what authority freshness and audit fallback? Service owner + platform lead | Local navigation, secure retention, offline credentials and persistent logs are unverified capabilities |
| D-04 | What are the waiting/escalation/return rules, reachable duty roles, handling limits and no-response contingency? Operations + responsible clinical service | A notification or nominal staffing roster does not establish timely human availability |
| D-05 | What are outage-detection and controlled-halt/holding rules, energy reserve, local indicators and recovery authority? Operations + platform safety lead | Connectivity and motion failure are different; no safe halt position or sensor reliability is supplied |

Proposed validation is a staffed walkthrough followed by controlled transport trials with representative containers, roles and outages. No trial has run. Agree time and workload targets before claiming acceptable service performance.

| Validation case | Observable condition for a useful decision |
| --- | --- |
| VC-01 / SC-01 normal and wrong-recipient attempts | Authorized staff can identify and accept the correct container; wrong/expired/declining recipients receive no release; physical possession and custody record agree. Observe steps, errors and staff effort. |
| VC-02 / SC-02 recipient and supervisor unavailable | Container stays controlled, a named custodian persists, status does not show delivered, and the approved timeout/contingency produces an observable authorized hold or return. Measure waiting and response times against subsequently agreed limits. |
| VC-03 / SC-03 outage at each handoff phase | Record which functions survive; no release without the approved authorization basis; no unrecorded assumed transfer. Interruption during removal produces a visible uncertain state and successful human reconciliation. |
| VC-04 / SC-04 reconnection with duplicate commands, expired authority or conflicting records | No automatic repeat release or motion; stale commands are rejected; current authority and custody are reconciled before explicit resumption. The completed mission has one physical transfer with attributable history. |
| VC-05 / SC-02–SC-04 busy-staff walkthrough | Staff can recognize who holds custody and who must act using the information actually available, including network outage. Observe missed prompts, informal workarounds and whether the named supervisor role can fulfill its duty under workload. |

These scenarios cover normal handoff and the requested exception/recovery paths. They do not establish exhaustive hazard coverage, clinical efficacy, legal compliance or platform verification.
