# HG-10 proposed integrated trial scenarios

All three scenarios are planned and unexecuted. The sequences are synthetic proposals for review, not actual historical events or adopted airport procedures. The complete operational and security procedures are not supplied. All physical steps require a controlled test configuration and site authorization; a simulated step must be labeled as such in the evidence record and excluded from physical-performance claims.

## Common trial contract

Roles: airline check-in/front-line agent, airline baggage/reconciliation lead and duty manager; terminal operator baggage controller, facility/handling representative and duty manager; passenger representative; observer/recorder from each organization; joint trial lead; joint readiness chair. Confirm local role allocation before the exercise: contractual custody boundaries and the organization providing handling personnel are not specified in the packet.

Use the same scoped service configuration, staff access, communications, bag-status records and operating procedures proposed for opening. Identify test passengers and bags without using real customer data. Define the acceptance point, custody acknowledgements, operating restrictions, disruption cues, escalation time limits, permitted holding locations, and recovery criteria before execution. The packet supplies no numerical timing, load or capacity thresholds; owners must establish them from the actual service envelope. Do not declare capacity or timeliness on the strength of these qualitative scenarios alone.

Stage A can be run jointly as a tabletop with clearly labeled simulated equipment/status events. Stage B repeats the selected journey physically on a representative available route with actual interfaces, trained roles and identified test articles. An unavailable area is an explicit coverage exclusion. Separate briefings remain preparation for the exercise, not its replacement.

## HG-10-SC01 — nominal passenger and baggage journey

**Purpose and trace:** test normal airline/operator handovers and staff performance under HG-10-I1, I2 and I4; challenge HG-10-C2. Initial state: the selected route is available, staff are in their assigned positions, systems and communication channels are in the declared mode, and the controlled passenger/bag identity and service destination are known. Start only when the trial lead has recorded which states are real and which are simulated.

**Trigger:** the passenger representative requests the in-scope journey with a test bag. The airline agent confirms eligibility under the trial rules, creates the bag/passenger association and destination, and submits the bag plus acceptance information to the operator's defined interface. The operator acknowledges the identifier, destination and custody/status, routes the test bag through the agreed facility steps, and reports completion or exception. Required screening steps follow the site-approved test procedure; simulated screening provides no evidence of screening performance.

The designated handling role acknowledges the next custody transfer. The airline reconciliation lead matches the bag and passenger/service records before a simulated or controlled dispatch decision. The airline communicates the passenger's service status. The observers trace the same bag identity across each boundary rather than inferring completion from one subsystem's success indicator.

**Observable result:** every handover has matched identifiers, sender, receiver, time and acknowledgement; no unowned bag or inconsistent passenger/bag status remains; the passenger reaches the agreed endpoint and the bag reaches its assigned controlled disposition. Completion alone does not establish performance under opening load.

**Recovery authority:** either front-line party may raise an anomaly and stop the local test step. The operator duty manager controls facility restrictions; the airline duty manager controls new airline acceptance and passenger/service disposition. The trial lead pauses the exercise if the declared route or configuration ceases to hold; restart uses the applicable exception scenario.

**Retain:** configuration/procedure versions; facility map and exclusions; staff roles and familiarity; test identities and characteristics; ordered handover log; actual/simulated steps; screen or status observations; observer findings; elapsed observations without an invented target; deviations and unresolved issues; separate review disposition.

## HG-10-SC02 — baggage route unavailable after acceptance

**Purpose and trace:** challenge HG-10-I2 and HG-10-C3 by requiring joint service restriction and recovery. Initial state: SC01 has reached airline acceptance with a traceable set of test bags in the route; the designated holding/recovery arrangements and escalation contacts are known. Use a controlled failure injection or a clearly simulated interruption, never an unapproved live fault.

**Trigger:** the trial controller declares the selected downstream route unavailable after bag acceptance. The operator controller detects/receives the interruption, identifies the affected route and bag set, notifies the airline, and requests acknowledgement of the service restriction. The airline duty manager stops additional acceptance into the affected route and directs passenger messaging and any permitted rebooking/alternative service. The operator controls affected equipment and secure holding under the trial procedure; neither party silently routes bags into an unverified manual workaround.

Both sides reconcile which bags were accepted, transferred, held or remain unlocated. The airline owns passenger/service decisions; the operator duty manager owns facility isolation and technical restoration. Any fallback must be pre-agreed, accessible, staffed and compatible with capacity limits. If these conditions are absent, hold the affected service and exercise the delay/return/rebooking decision rather than inventing spare capacity.

**Observable result:** an acknowledged restriction reaches the airline acceptance point; the test records show no further acceptance into the blocked route after that restriction takes effect under the agreed timing rule; every affected bag and passenger has an owned status and disposition. A restored equipment indication does not alone trigger resumption.

**Recovery authority and end state:** the operator duty manager confirms route availability and bag/status reconciliation; the airline duty manager confirms staffing and service readiness; both record joint permission to resume within the approved envelope. The joint trial lead restarts the controlled scenario from an identified state. If reconciliation, capacity or authority is unresolved, the defined final state is affected-service hold with passenger/bag dispositions recorded, not nominal completion.

**Retain:** failure-injection identity and timing; initial bag set; alarm/notification/acknowledgement chronology; acceptance-stop observation; holding/custody and passenger decision logs; fallback evidence or explicit absence; restoration checks; joint restart/hold decision; issues and owners.

## HG-10-SC03 — missing handover acknowledgement and inconsistent status

**Purpose and trace:** expose an organization/communication failure through HG-10-I2 and I3, while challenging HG-10-C3. Initial state: one test bag is at a controlled airline/operator boundary; both sides have the same initial identity and know the approved acknowledgement/escalation rule. Declare how acknowledgement timeout will be represented; no time value is supplied by this packet.

**Trigger:** suppress the agreed acknowledgement in the test channel and introduce a controlled disagreement: the airline record shows transfer attempted, while the operator record does not establish receipt. The airline front-line agent identifies the missing acknowledgement, records the concern under I3, and contacts the operator through the approved alternative channel. The operator checks its physical/test custody and record before asserting receipt. Neither side fabricates an acknowledgement or duplicates the bag merely to clear a queue.

The two duty managers establish one reconciled record of the bag's actual controlled location and status. They identify other transfers potentially affected by the channel failure and restrict further use of that handover until a safe defined method exists. The airline directs passenger/service information; the operator directs facility/custody actions. If no alternative communication or custody proof is available, place the affected transfer/service on hold and escalate to the joint readiness chair through the recorded issue process.

**Observable result:** front-line concern is acknowledged and assigned; a consistent bag/passenger disposition is agreed or explicitly marked unresolved; the record preserves original conflicting statuses, communication attempts and correction lineage. No lost ownership or duplicate transfer is hidden by overwriting a record.

**Recovery authority and end state:** communication restoration is followed by reconciliation of all potentially affected transactions, resolution of duplicate/stale statuses, and a controlled acknowledgement check. Both duty managers authorize service resumption; the trial lead resumes the test. An unlocated bag or unreconciled transaction ends in a documented hold, with an owner and next action. The readiness chair decides whether the unresolved issue prevents opening the selected scope.

**Retain:** injected failure and initial state; both unaltered status records; channel and acknowledgement logs; concern/issue ID; physical/test custody evidence; reconciliation and correction history; passenger/service disposition; named-role decisions and restart observation; residual gaps.

## Review and coverage boundary

The joint trial lead assembles the configuration-specific record; observers from both organizations identify disagreements rather than averaging them. Each issue has an owner, corrective action, due/review trigger and affected scenario. Changed procedures, equipment, route, staff allocation or interface semantics require a justified applicability decision and rerun of affected scenarios. Record expected and observed behavior, actual deviations and the result only after execution. Acceptance remains a separate joint readiness decision.

These scenarios cover one nominal journey, route interruption and a failed organizational handover. They do not establish opening throughput, all bag classes, every staffing shift, security compliance or every failure combination. Select additional coverage using the real service envelope and observed issues rather than declaring this set exhaustive.
