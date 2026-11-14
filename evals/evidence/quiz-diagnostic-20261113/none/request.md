# Systems engineering judgment exercise

Answer from the supplied facts. These are engineering reasoning questions, not requests to certify a system. Use only this packet and tools permitted by the evaluation controller. Do not look for answer keys or other runs. Report unavailable facts honestly. Save answers.json using the response template. Select options and provide your own explanation for each item. Record the model/host/settings actually used; do not guess.

## SEJ-003: Boundary versus ownership

A municipal flood-warning service consumes a commercial rainfall feed. The supplier controls its infrastructure. The warning authority remains accountable for issuing timely warnings when the feed is delayed.

How should the supplier be represented? Select one option.

- A. As a fixed environmental assumption until the supplier contract is renegotiated.
- B. Inside the authority's boundary because accountability implies control of all supporting components.
- C. Outside the architecture because its implementation cannot be changed by the authority.
- D. Outside the system-of-interest boundary, with an explicit operational dependency and an owned degraded-service response.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-004: Conflicting outcomes

Airport operations wants shorter gate turnaround; maintenance wants enough inspection time; crews report increasing last-minute changes. The team proposes automation of the inspection signoff. No causal study is available.

Which pair of actions is justified before committing to that automation? Select all supported options.

- A. Define the competing outcomes and the conditions under which each must be protected.
- B. Assign the delay to maintenance because it owns the signoff.
- C. Use the fastest observed turnaround as the acceptance threshold.
- D. Trace late changes and inspection decisions across responsible roles.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-008: End of service

A sensor network stores configuration keys in modules expected to remain installed for fifteen years. The design review covers commissioning and operation but not replacement or retirement.

Which issues belong in the lifecycle review? Select all supported options.

- A. Whether every module should be physically destroyed on replacement.
- B. Who maintains compatibility and spares when the supplier ends support.
- C. How replacement modules acquire the authorized configuration.
- D. How retired modules lose credentials and retained sensitive data.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-009: Reliability across a mission

Two alternatives have the same measured failure frequency during operation. One restores within minutes after a fault; the other requires a specialist visit. Missions are daily and unattended sites have limited access.

What conclusion follows? Select one option.

- A. Equal failure frequency establishes equal operational availability.
- B. Restoration time and access arrangements must be included before comparing mission availability and lifecycle effort.
- C. Availability cannot be studied until a complete long-term field trial has finished.
- D. The faster-restoring alternative is preferable regardless of acquisition and mission effects.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-013: A shared event in a tree

A fault tree is (A AND B) OR (A AND C). Event A represents the same loss of a shared supply wherever it appears.

Which minimal cut sets follow from that Boolean model? Select one option.

- A. {A,B,C} only.
- B. Two separate independent copies of A, one in each branch.
- C. {A} and {B,C}.
- D. {A,B} and {A,C}.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-014: A warning that causes more work

An alarm threshold is lowered. Detection rises, but operators receive many more alarms and begin delaying acknowledgment. Reported unresolved incidents also rise.

Which next model is most useful? Select one option.

- A. A feedback model connecting alarm load, attention, acknowledgment, escalation and unresolved events.
- B. A ranking of operators by acknowledgment time.
- C. A detector-only ROC curve with an increased penalty for missed events.
- D. A human-response model using the old acknowledgment time as a constant.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-018: Zero observed failures

An engineer tests twenty identical units for one hour each and observes no failures. The report claims the system failure probability is zero.

Which response is most appropriate? Select one option.

- A. Pool the twenty units as a single unit tested for twenty consecutive hours without checking assumptions.
- B. State the observed exposure and zero events, then use an explicitly justified statistical model and uncertainty if estimating reliability.
- C. Declare the test inconclusive and discard the observations.
- D. Use one failure divided by exposure as the exact failure probability.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-019: Coverage with an unrealistic assumption

A formal check proves that every accepted request is eventually served under an assumption that the shared resource is continuously available. Deployed operation allows outages and bounded recovery.

Which next step best strengthens the evidence? Select one option.

- A. Report the proof as conditional, assess the environment assumption, and analyze request behavior during outage and recovery.
- B. Remove the availability assumption and call the resulting timeout a requirement defect.
- C. Increase the proof bound while leaving the environment assumption unchanged.
- D. Replace the proof with line coverage because the deployed environment is uncertain.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-023: Decomposition loses a condition

The parent requires emergency shutdown on loss of either pressure sensing or temperature sensing. Two children require a diagnostic on pressure loss and a diagnostic on temperature loss. The allocation matrix links both children to the parent.

What remains missing? Select one option.

- A. A third sensor is needed to satisfy the parent.
- B. The two links establish complete decomposition because each input is represented.
- C. The children must use identical wording to the parent.
- D. The required shutdown response and its connection to either diagnostic need explicit treatment.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-024: Resolving conflicting authorities

A signed contract requires a maximum mass of 40 kg. A later meeting note proposes 45 kg to improve endurance but contains no approval. The team is preparing a design trade.

Which treatment preserves the decision basis? Select one option.

- A. Stop all concept work until the contract is formally changed.
- B. Keep 40 kg as the current obligation, record 45 kg as a proposed change, and show the trade consequence and needed disposition.
- C. Use 45 kg because it is the latest statement.
- D. Average the two values to avoid bias toward either stakeholder.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-028: Mars Climate Orbiter: a contract existed

The 1999 Mars Climate Orbiter investigation reports that a ground software interface specified metric impulse data, while a producer supplied English-unit data. The report also identifies verification and communication weaknesses.

Which action best transfers this lesson to a new project? Select one option.

- A. Add unit labels to the interface document and consider the problem resolved.
- B. Require one organization to write every component to remove organizational interfaces.
- C. Convert every engineering quantity to a single storage type.
- D. Make interface semantics executable at producer/consumer boundaries and verify representative exchanged data with clear ownership.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-029: Ownership at an interface

A sensor supplier guarantees nominal one-second updates. The controller designer assumes the latest value is usable for five seconds. Neither defines timestamps, loss detection or clock alignment.

Which clarification has the highest immediate value? Select one option.

- A. The validity/age contract, clock reference, guaranteed update bounds and responsibilities when those conditions are violated.
- B. Whether the supplier uses UDP or TCP internally.
- C. The exact color of the stale-data indicator.
- D. Whether five seconds is a common industry setting.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-033: A reversible trial

Two scheduling policies meet hard constraints in preliminary analysis. A can be trialed at one site with rapid rollback; B requires a year-long infrastructure change. Demand forecasts are uncertain and likely to change within six months.

Which factor belongs in the decision? Select one option.

- A. The number of requirements each option references.
- B. The option value of reversible learning, alongside expected performance and implementation effects.
- C. A rule that the smallest change should always be selected.
- D. A preference for B because it demonstrates long-term commitment.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-034: Build, buy and the supporting system

A defense logistics team can buy a sensor that meets laboratory accuracy requirements. Field repair, export/access constraints, supply continuity and integration with existing maintenance records remain unresolved.

What should a build/buy comparison include? Select one option.

- A. Only components designed by the program because external products cannot be controlled.
- B. The sensor plus integration, support, supply and operational constraints, with uncertainties and owners.
- C. Total project cost with all unknowns assigned the same contingency percentage.
- D. The sensing function and its measured accuracy only.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-038: An estimate becomes a fact

A preliminary model assumes a 20-minute restoration time because no maintenance data exists. Several slides later, the executive summary calls this the measured restoration time.

What correction is needed? Select one option.

- A. Rename the model output a prediction and leave the summary unchanged.
- B. Delete every result calculated using the assumed value.
- C. Increase the value until the conclusion becomes conservative.
- D. Retain the value but restore its assumption status and trace its effect on conclusions.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-039: US Airways 1549: decision time in a simulation

The NTSB's report on the 2009 US Airways 1549 accident distinguishes immediate-return simulator attempts from scenarios including crew decision time. An immediate turn toward an airport does not represent the same starting conditions as the actual crew's situation.

What is the strongest transferable lesson? Select one option.

- A. Alternative assessment must include information, recognition and decision delays available at the actual decision point.
- B. A successful simulator trajectory establishes that the crew should have selected it.
- C. Human decision time should be removed when evaluating aircraft performance.
- D. A failed delayed attempt proves no aircraft could have returned under any conditions.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-043: Columbia: routine success and unresolved evidence

The 2003 Columbia Accident Investigation Board analyzes both physical damage mechanisms and organizational practices. A contemporary team argues that a recurring anomaly is acceptable because previous missions succeeded.

What should a review require? Select one option.

- A. A causal and evidence-based assessment of the anomaly, including why prior success does or does not bound the present risk.
- B. A ban on using operational history in risk assessment.
- C. A count of successful missions as a direct estimate that the anomaly cannot cause loss.
- D. A requirement that the subsystem owner make the final decision without cross-program review.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-044: London 2012: a supplier cannot deliver

The National Audit Office's post-Games review describes extensive operational preparation for London 2012 and contingency action when the security contractor could not provide planned staffing.

Which preparation best transfers to a new major event? Select one option.

- A. Duplicate contracts for every event function regardless of consequence.
- B. A detailed organization chart with no need to rehearse transitions.
- C. Exercised scenarios connecting delivery shortfalls to decision authority, available reserves and operational changes.
- D. Contract penalties large enough to remove the need for alternate staffing.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-048: Reporting disagreement

Two reviewers disagree about whether an old environmental test covers a revised connector. One cites unchanged materials; the other cites a changed seal geometry. A report must be delivered today.

Which report is most useful? Select one option.

- A. Report disagreement, the evidence supporting each position, the geometry-dependent question and the decision or test needed to resolve it.
- B. Choose the senior reviewer's conclusion and omit the disagreement.
- C. Present both conclusions as equally valid without identifying the unresolved mechanism.
- D. Average the two reviewer ratings and report the resulting confidence.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-049: Choosing a useful view

A review board cannot tell who controls motion during startup, normal operation, manual stop and recovery. It already has a component hierarchy with complete part names.

Which additional view best answers the question? Select one option.

- A. A more detailed component hierarchy with supplier names.
- B. A table of all software function names sorted alphabetically.
- C. A high-resolution rendering of the enclosure.
- D. A state/authority view showing transitions, guards and who may enable or inhibit motion, tied to the existing components.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-053: TCP: acknowledgment at the right layer

RFC 793 (1981) explains that TCP acknowledgment means the receiving TCP has taken responsibility for data, not necessarily that it has been delivered to the end user. A system logs TCP acknowledgment as proof that a remote operator acted.

What should the review conclude? Select one option.

- A. Replacing TCP with a newer transport protocol resolves the semantic gap.
- B. TCP acknowledgments are unreliable and should not be recorded.
- C. The log supports transport-level receipt but not operator action; the application/workflow needs its own relevant acknowledgment evidence.
- D. The operator action is established whenever both endpoints use TCP.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-054: DNS: a historical design trade

RFC 1034 (1987) describes distributed maintenance and caching, including a trade among acquisition cost, update speed and cache accuracy. A team proposes a very long cache lifetime to reduce server load for rapidly changing control data.

What transfers from the source? Select one option.

- A. A long lifetime is correct because the original design favored caching.
- B. The trade must be evaluated against this application's update and stale-data consequences; the historical mechanism does not supply its acceptance limits.
- C. Caching should be avoided whenever data can change.
- D. A cache hit demonstrates that the value is current.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-058: A supplier changes its service contract

A cloud service previously guaranteed delivery of events in order. Its new version preserves all events but allows reordering. The consumer uses arrival order to authorize a sequence of physical actions.

Which review scope is necessary? Select one option.

- A. Only the API field names and types.
- B. The supplier's event count, because no data is lost.
- C. Every requirement in the organization, regardless of dependency.
- D. The changed ordering semantics, consumer state/authority logic, recovery behavior and related verification evidence.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.

## SEJ-059: A rejected alternative becomes relevant

A system chose a wired sensor because radio coverage was poor at remote sites. The new deployment is indoors with existing radio infrastructure, but battery replacement staffing is limited.

What should the concept review do? Select one option.

- A. Delete the previous decision record to avoid confusing reviewers.
- B. Reuse the old decision because its documented rationale makes it authoritative in every deployment.
- C. Select radio because the original objection is absent.
- D. Reopen the alternative against the new context, retaining the old rationale and examining new support constraints.

Explain the facts and reasoning that support your selection; identify a consequential limitation if one applies.
