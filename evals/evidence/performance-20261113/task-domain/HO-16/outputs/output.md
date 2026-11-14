The two “response times” currently measure different intervals. Starting the automatic clock at hazard onset includes time that the human clock omits by starting after recognition and diagnosis. Those labels cannot support a comparison of complete emergency response. The stopping event must also match: issuing a command and bringing the hazard under control are different outcomes.

The request-supplied historical fact from NTSB/AAR-10/03, sections 1.16.3 and 2.3.2, illustrates why decision time matters to simulator conclusions. I have not independently retrieved that report. It does not supply a numerical correction for this new system.

Use a common measurement contract:

| Contract item | Proposed definition |
| --- | --- |
| Main measure | Elapsed time from independently timestamped hazard onset, t0, to the same observable controlled state, tS. Define the state and required duration of stability before testing. Measure tS − t0 for both responses. |
| Supporting events | Record detection/recognition, diagnosis/decision, command, and physical action timestamps where observable. Include automatic sensing and decision latency as well as human latency. Identify inferred or unobservable events. |
| Conditions | Match initial plant state, hazard severity, available information, communications, actuation limits, and relevant failures. Represent realistic operator workload, training, staffing, and surprise. Do not give automation direct simulator truth unless the real installation has equivalent information. |
| Recording quality | Use synchronized clocks or a measured alignment, stated sampling resolution, event rules, uncertainty, and exact simulator/system versions. Preserve raw traces and deviations. |
| Outcome reporting | Report timing distributions and scenario conditions together with unsuccessful responses, wrong actions, false activations, and timeouts. Do not discard nonresponses to make the successful cases appear fast. |
| Decision rule | Agree required outcome, deadline, and tolerable failure behavior from the operational safety need before comparing results. No such limits are supplied. |

Where task phases overlap, the timestamp trace remains authoritative; summing separately measured averages can misstate total time. Repeated simulator runs should control practice and foreknowledge, for example through varied scenarios and balanced order. Document the simulator's fidelity limits before applying results to operations.

If raw timestamps contain a common onset and outcome, recompute comparable intervals. Otherwise collect new matched runs; relabeling the existing columns cannot restore missing time.

Present data cannot establish which complete response is faster, whether either meets an operational deadline, whether automation should replace an operator, or which option is safer. Speed without correct action and a controlled outcome is inadequate evidence. At most, sufficiently documented existing results describe their own measured subintervals and conditions. This contract is proposed; no new comparison has been executed.
