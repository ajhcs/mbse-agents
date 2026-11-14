# REQ-7 timing change — impact and evidence review

**The 200 ms baseline is not verified by the supplied information.** Preserve REQ-7's ID and its 500 ms revision history, but reopen its verification and timing allocation. The reported 460 ms result passed the former 500 ms criterion; it does not pass a comparable 200 ms criterion. A planned report path with no file supplies no result. This review uses the facts in `../request.md`; the original test report, design, logs, timing specification and new report are not present for inspection.

## Timing consequence

For a serial dependency from interface processing through detection to actuation, the supplied upper bounds sum to:

`150 ms + 80 ms + 30 ms = 260 ms`

That budget exceeds 200 ms by **60 ms**, before any unallocated sensing, queues, scheduling, communications, output rendering or physical alert delay. This shows the stated serial budget cannot substantiate a 200 ms worst-case guarantee. It does not prove that every run takes 260 ms or that all stage maxima occur simultaneously; dependencies and conditions need inspection. Conversely, a typical faster run would not repair the missing worst-case argument.

The old observed 460 ms had 40 ms margin against 500 ms and would exceed 200 ms by 260 ms if its reference events and conditions are comparable. Its being 200 ms longer than the 260 ms stage sum is an unresolved discrepancy, not proof of a particular 200 ms overhead. Possible causes include omitted work, different configurations, time origins or incomparable definitions. Inspect the actual report and timeline before allocating that difference.

## Located findings and impacts

| ID | Locator and observed fact | Consequence | Concrete repair; proposed owner/status |
| --- | --- | --- | --- |
| F-01 | REQ-7 verification claim: reused reported PASS at 460 ms after limit changed 500 → 200 ms | Current verification claim is unsupported; if the recorded observation applies to the same claim, it contradicts the new limit | Retain old result and historical verdict; record its 500 ms scope. Set current REQ-7 verification to open/unverified. Retrieve report and perform explicit applicability review. Verification lead; open, blocks a supported verification claim |
| F-02 | Interface 150 ms, detector 80 ms, actuator 30 ms allocations | Serial upper-bound total is 260 ms with negative margin. Locally conforming elements can still miss the system deadline | Establish end-to-end path and overhead; redistribute or redesign timing allocations, then obtain analysis and measurement. Architecture/performance lead; open |
| F-03 | Planned new report path is reported absent | Trace points to intended evidence, not an executed artifact | Mark activity planned, outcome unset, artifact absent. Execute approved procedure on the revised configuration and attach actual report/raw logs. Verification lead; open |
| F-04 | No trigger/alert definitions, baseline identifiers, operating envelope or timing uncertainty supplied | Neither evidence reuse nor a precise pass decision can be assessed | Define timing endpoints, inclusive ≤ 200 ms criterion, loads and alert visibility; identify exact design/test versions and measurement uncertainty. Requirement owner + test lead; open question, not an invented defect in unseen files |

Affected work includes REQ-7's acceptance procedure and trace coverage; every stage and shared resource on its critical path; interfaces whose latency/rate/queue contracts change; scheduling, priority and buffering; resource contention with other functions; alert semantics and any safety/operational analysis relying on alert timing. Revisit suppliers only where their components carry changed allocations. No hazards, supplier commitments, certification requirements or particular alert technology were supplied, so their actual impacts remain to be assessed rather than asserted.

## Evidence disposition

| Record | Lifecycle/outcome | Configuration applicability | Review/acceptance |
| --- | --- | --- | --- |
| Old report, reported 460 ms against 500 ms | Reported executed PASS for old criterion; actual artifact/logs not examined | Historical evidence for the former requirement if identity and conditions are confirmed. Not positive evidence of ≤ 200 ms. Potentially reusable for unchanged functions or method only after a scoped argument | Prior review/acceptance unknown; no current acceptance inferred |
| New planned report | Planned; no execution outcome; reported file absent | No executed configuration exists in the supplied evidence | No review or acceptance |
| This 260 ms arithmetic | Desk analysis of supplied stage bounds under stated serial assumption | Conditional; no deployed-controller timing measured | Shows an allocation gap, not an executed system failure |

A linked requirement, component, test and report is a navigation chain. It establishes neither that the report exists nor that the procedure exercises the current deadline under the intended conditions.

## Repair options

1. **Keep 200 ms and reduce the serial path.** After accounting for all overhead `H`, allocations must satisfy `I + D + A + H ≤ 200 ms`. With detector and actuator unchanged, interface allowance is at most `90 ms − H`, a reduction of at least 60 ms even if H were zero. Investigate queue delay, transport, scheduling and avoidable processing before selecting changes. No such reduction is yet demonstrated.
2. **Introduce genuine parallelism or a shorter alert path.** If interface processing and detection can validly run concurrently on the required fresh input, `max(150,80) + 30 = 180 ms`, leaving at most 20 ms for every other delay and uncertainty. This is a conditional architecture candidate, not a validated budget. If detection depends on interface completion, this arithmetic is invalid. A local earlier alert path might help only if it preserves the required alert meaning and conditions; an early acknowledgment is not automatically an alert.
3. **Change components, algorithms or partitioning.** Use an independently scheduled critical path or faster stages if measurements identify the limiting mechanism. Reassess shared queues, false/missed alerts, ordering and interference after any optimization. Faster component specifications alone do not verify the system.
4. **Reconsider the requirement through its authorized owner.** If no feasible architecture meets 200 ms within constraints, present the timing need, consequences and cost/scope trade. A justified alternate deadline or phased objective is a change decision, not a verification waiver disguised as a pass. Do not silently restore 500 ms or rewrite the old verdict to fit the new requirement.

## Verification work and next decision

First obtain a timestamped end-to-end trace for the actual critical path and resolve the 460 ms versus stage-budget discrepancy. In parallel, the requirement owner must define the initiating event and the observable alert completion; revisions and loads must be comparable before subtracting timings.

Prepare **V-7-REV** against the final REQ-7 revision and frozen implementation: stimulate the specified event, measure from its defined time origin to observable alert, and collect stage timestamps on a common or demonstrably aligned clock. Exercise specified worst-load and queue conditions, event/sample phase boundaries, contention and relevant degraded/recovery modes. Determine the needed run set and analysis coverage from the actual timing model; do not invent a sample count or percentile for a hard deadline.

Acceptance requires ≤ 200 ms for the applicable conditions with documented measurement uncertainty and a justified bound on unobserved worst cases. A conservative observation criterion is measured elapsed time plus its uncertainty ≤ 200 ms; the adopted uncertainty treatment must be explicit. Record any > 200 ms result as a failure for that tested configuration, preserve the logs and identify repair. Regression checks must cover unchanged alert semantics and neighboring functions affected by changed scheduling/interfaces.

The resulting report must include exact requirement/design/firmware/configuration hashes, procedure and instruments, environment/load, trigger/end definitions, raw values and maxima, uncertainty, deviations and limits. Then perform applicability review and a separate authorized acceptance decision. Until that work exists, retain the new requirement as **unverified**, with an unresolved timing budget. No system test was run in preparing this review.
