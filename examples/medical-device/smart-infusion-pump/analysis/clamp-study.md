# Temporal clamp-release study

This executes a sampled state model of the proposed spring-closed clamp,
powered hold-open path, door interlock, watchdog release and recovery latch.
The existing **REQ-SAF-001** proposes closure within 500 ms after door opening
or hold-open power loss; **REQ-SAF-002** proposes a 200 ms watchdog response.
The model does not simulate spring mechanics, actuator dynamics, tubing occlusion,
gravity flow or delivered dose. Its `closed` output is a logical state whose
physical meaning must be demonstrated separately.

## Inputs and timing contract

The initial condition is an operating state at time zero: door closed, clamp
held open and processor service recorded. Calls occur on contiguous 100 ms ticks.
Door and power changes are observed on the stated tick. Watchdog expiry occurs
when 200 ms have elapsed since the last service. A release is latched and starts
an assumed closing delay. No CPU command is required after release. Jamming
prevents closure; an interlock fault masks door opening but does not mask loss
of hold-open power. These are explicit proposed failure semantics.

Closing delays from 0 through 700 ms are design hypotheses, not measurements.
The default 300 ms allocation leaves 200 ms for watchdog expiry within a separate
500 ms illustrative combined-response challenge. The original requirement must
clarify whether its safe-state deadline includes mechanical closure; the study
does not silently adopt that interpretation as an approved requirement.

Here `power` means the hold-open actuator supply; `cpu_services` independently
states whether the processor actually serviced the watchdog on that tick. Loss
of actuator power does not imply loss of processor service. A primary AC interruption that
the battery bridges is a different case: hold-open power may remain available.
REQ-PRF-004's proposed automatic recovery after short power interruptions must
be reconciled with the latched-fault rearm policy. The study does not replace
that requirement or establish infusion continuity during a supply transition.

## Executed challenges

| Challenge | Expected observation | Meaning |
| --- | --- | --- |
| Door opens; CPU continues servicing | Release on the observed opening tick; closure after the assumed delay | Door release is independent of a CPU command in the model |
| Hold-open power lost | Release remains latched; closure after the assumed delay | Power recovery alone cannot resume the modeled operation |
| Processor stops servicing | Watchdog releases at 200 ms; assumed closure follows | Combined response is within 500 ms only for closing delays at most 300 ms |
| Assumed closing delay exceeds budget | Retained failed requirement outcome | A functional release signal does not establish timely closure |
| Actuator jam | Clamp remains open after release | The current proposal lacks this fault coverage |
| Door interlock fault | Opening can leave hold-open active | A door-open stimulus is not itself evidence that the release path works |
| Power returns after release | Clamp remains latched closed | No automatic restart under the proposed recovery policy |
| Explicit rearm with healthy conditions | Hold-open can be requested again | Manual rearm is a proposed policy requiring usability/operational review |
| Rearm while door remains open | Release remains latched | Unsafe rearm request is rejected in the model |

The [saved results](../evidence/analysis/clamp-results.json) retain all timed
traces and ten criterion violations: six violate the modeled REQ-SAF-001 closure
condition and four violate the additional proposed 500 ms watchdog-plus-closure
challenge. The latter do not fail the separately checked 200 ms watchdog-release
condition. The mechanical interpretation of REQ-SAF-002 remains unresolved.
The harness reports these negative cases as successful discoveries; it does not
report the violated criteria as passed. Twenty-eight cases execute the timing sweep,
fault injections and recovery policies.

## Reproduction and evidence needed next

```sh
python3 examples/medical-device/smart-infusion-pump/analysis/run_clamp_checks.py --check
```

The [model](clamp_model.py) and [procedure runner](run_clamp_checks.py) are editable.
Content-addressed run directories preserve exact model/procedure bytes,
requirement snapshots, outputs, runtime and execution time.

Measure actual release, clamp displacement, occlusion and delivered volume at
the required observation points, across tubing and actuator tolerances,
temperature, orientation, wear and specified fault cases. Determine whether a
stuck mechanism is detected and what independent control limits exposure. Test
watchdog, power and door dependencies on the actual circuit. Validate the rearm
policy with representative users. Those results are required before claiming
physical closure performance, acceptable residual risk or clinical benefit.
