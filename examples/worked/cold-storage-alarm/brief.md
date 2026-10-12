# Stakeholder brief

This fictional project monitors a laboratory cabinet holding temperature-sensitive
research reagents. It is not claimed to be a medical device or validated storage system.

| Source | Need / teaching-project decision |
| --- | --- |
| NEED-01 | Local warning after temperature has remained at or above 8 deg C for 2 s. This project threshold is not a sourced clinical/reagent limit. |
| NEED-02 | Distinguishable sensor-unavailable indication after 1 s of invalid readings. |
| NEED-03 | High warning remains visible until temperature is below 8 deg C and a technician acknowledges. |
| NEED-04 | Timestamped alarm changes for investigation. |

SCN-01: monitor storage, detect a sustained excursion, latch warning, observe
recovery, acknowledge, retain event record. SCN-02: invalid/missing readings
produce sensor fault; valid reading clears that fault; an existing high warning
still needs valid recovery and acknowledgement.

Boundary: sensing interface, alarm logic, local annunciation, event record.
Refrigeration control, networks, reagent disposition, and lab quality decisions
are outside this demonstration.

Assumptions: samples every 100 ms; monotonic timestamps; power available; a valid
reading represents cabinet temperature. Physical accuracy, sound/light perception,
power loss, calibration, retention across reset, and staffing/response time require
subsequent design and stakeholder validation.
