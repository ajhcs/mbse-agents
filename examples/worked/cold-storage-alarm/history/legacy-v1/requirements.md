# Proposed requirement baseline

Values come from [the brief](brief.md), not regulation. Requirements apply to
sampled reference behavior. Timer intervals begin at the first applicable sample,
not a physical threshold crossing between samples.

| ID | Requirement | Source | Acceptance |
| --- | --- | --- | --- |
| REQ-01 | The evaluator shall latch high within 100 ms after valid samples have been at or above 8 deg C continuously for 2 s, and not before that interval. | NEED-01 | First high 2000-2100 ms from first qualifying sample; below-threshold/invalid sample resets pending interval. |
| REQ-02 | The evaluator shall assert sensor fault within 100 ms after readings have been invalid continuously for 1 s; the next valid sample shall clear sensor fault. | NEED-02 | First fault 1000-1100 ms; clearance on next valid sample. Nonfinite/nonnumeric readings are invalid. |
| REQ-03 | The evaluator shall retain latched high until acknowledgement while the current sample is valid and below 8 deg C. | NEED-03 | Early acknowledgement, recovery alone, and sensor recovery cannot silently clear high. |
| REQ-04 | The event recorder shall record each change of high/fault state once, with sample time and resulting states. | NEED-04 | Exact ordered transition records; no event for unchanged state. |

Derived interface IFC-01 uses contiguous 100 ms ticks, supporting the model timing
claims. Jitter, transport/actuator latency, and persistence need further requirements.
No requirement is marked stakeholder approved.
