# Teaching change request

This is a deliberate instructional baseline change, not a real stakeholder
approval or a claim that 500 ms is a clinically appropriate limit.

| Source | Changed need | Supersedes | Reason |
| --- | --- | --- | --- |
| CR-01 | Assert the sensor-unavailable indication within 100 ms after readings have remained invalid for 500 ms; clear on the next valid sample. | NEED-02 1 s qualification interval | Exercise a shorter detection interval and its evidence impact. |

Keep REQ-02, FUN-02, COMP-01/COMP-02, IFC-01, and procedure IDs stable.
The original brief remains preserved. REQ-01, REQ-03, and REQ-04 are unchanged.
The 100 ms sampling interface remains unchanged, so 500 ms spans five elapsed
ticks from the first invalid sample. No physical sensing or operator result is
established by this choice.
