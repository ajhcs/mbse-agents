# Flood-permit service — recommendation to the director

The online application has reduced applicant effort from 40 minutes to 10 minutes. That is a useful improvement, but the service still takes 30 days to reach approval and urgent work is delayed. The next decision should target the time between submission and a usable decision. A chatbot may help applicants understand the process; the supplied facts do not show that it will increase engineering-review capacity, retrieve land records sooner or make outside inspections available.

The service crosses several queues and organizations:

`Application → completeness/triage → engineering review, land records and inspection dependencies → authorized decision → applicant notification`

That is a provisional map, not a claim that all reviews run in parallel or in that order. Map the actual dependencies. The shared bottlenecks may involve insufficient capacity, work waiting for another input, repeated corrections, scheduling or priority rules. We know the bottlenecks are shared; we do not yet know which mechanism accounts for most delay. Making intake easier could increase arrivals into the same queues, and automating questions could free reviewers' time, but neither effect is established by the supplied information.

Use three connected boundaries. The **applicant boundary** begins when someone seeks permission and ends with a clear decision they can act on, including requests for correction, refusal and accessibility needs. The **operating boundary** includes intake, triage, engineering, records, inspections, handoffs, rework and decision authority. The **resource boundary** includes the other city services and organizations competing for those same reviewers, records staff and inspectors. A faster permit queue that simply delays their other obligations is not an established system improvement. Outside inspection providers may be beyond the director's direct control; their commitments and escalation contacts still belong in the service design.

Measure the service before choosing the automation:

| Measure | What to observe and why |
| --- | --- |
| End-to-end elapsed time | First submission to communicated decision, separating ordinary and urgent cases; report the distribution and oldest open cases, not only an average. Establish what the reported 30 days actually measures. |
| Waiting versus active work | Time entering each queue, work start/finish, missing-input waits and handoff delays. These distinguish a capacity shortage from coordination or rework. |
| Flow and backlog | Arrivals, completed decisions and open work by stage and case type, including age. Track shared resource demand from other services, not just permit staffing. |
| Completeness and rework | Missing/incorrect submissions, correction cycles and reasons, where defects originate, and who must redo the work. These reveal whether better guidance would remove material delay. |
| Urgent service | Time to triage, time to decision, cases missing an agreed urgent target, and the consequence of delay. The authorized owner must define urgency and targets; none are supplied. |
| Quality and burden | Review errors, reopened decisions, applicant/staff effort and effects on routine cases and other services. Faster decisions are useful only if the required review remains effective. |

Trace a recent cohort across all involved teams using case events, then inspect representative urgent, delayed, returned and still-open cases with the people doing the work. Include unfinished applications so completed cases do not hide the longest waits. Use common timestamp definitions and identify missing records; a blank timestamp does not mean zero waiting. The event trace and staff walkthrough should explain the mechanism before anyone promises a reduction in the 30-day figure.

My conditional recommendation is to authorize a bounded service-flow review and a jointly owned urgent-work pilot before a general chatbot build. Assign one owner to reconcile the queues and decision rights with engineering, land records and inspection providers. If urgent cases are waiting because they enter ordinary queues without a visible owner or scheduling rule, pilot an explicit triage/escalation path and coordinated review slots. Set the authority, entry criteria and fairness rules first; expedited coordination does not waive required review. Observe urgent elapsed time alongside routine-case aging, other-service delays, rework and decision quality.

If the trace instead shows that incomplete applications or repetitive status questions consume substantial bottleneck staff time, compare improved forms, clear guidance and visible case status with a narrow chatbot pilot. Judge any chatbot by reduced rework or recovered review time and resulting service delay, plus answer accuracy and escalation failures—not conversation count. It should not imply approval, invent a case status or make the authorized permit decision. If delay is principally a shortage of qualified review or inspection capacity, the director needs a staffing, scheduling or interagency service decision; adding another intake interface would leave that constraint in place.

The questions most likely to change this recommendation are: **Where do urgent cases spend their waiting time, and who can change that queue's allocation? What proportion of reviewer effort is caused by avoidable applicant questions or corrections? Which sequencing and review steps are fixed obligations, and which are local working practices?** These can be answered while developing the flow pilot. No full requirements document, new legal interpretation or quantified chatbot benefit is justified by the current facts.

Basis: supplied HO-12 request. This is a conditional recommendation; no service data analysis or pilot was executed.
