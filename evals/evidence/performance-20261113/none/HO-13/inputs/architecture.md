# Controller architecture, revision A

COMP-1 input interface forwards the sensor input to COMP-2 detector. COMP-2 sends the alarm command to COMP-3 local annunciator over IFC-2. IFC-1 is the sensor-to-detector interface. IFC-3 carries operator stop/resume intent to COMP-2.

Current worst-case path allocation, assumed serial and nonoverlapping:

| Stage | Maximum |
| --- | --- |
| COMP-1 interface processing | 150 ms |
| COMP-2 detection | 80 ms |
| COMP-3 warning assertion | 30 ms |

The recorded state diagram says: OPERATING -> INHIBITED on local stop or missing data; INHIBITED -> OPERATING when stop is released and valid data returns. No separate resume guard is shown.

No physical timing measurements for revision B are available.
