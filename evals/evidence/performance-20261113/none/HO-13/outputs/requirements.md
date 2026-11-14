# Controller requirements, proposed revision B

CR-1 approves the REQ-7 timing criterion change below. It does not approve an implementation or establish compliance. REQ-8 and the project-controlled pressure threshold and input validity contract are unchanged.

| ID | Requirement | Source | Status |
| --- | --- | --- | --- |
| REQ-7 | The controller shall assert the local high-pressure warning within 200 ms after the valid pressure input first meets the high-pressure condition during operation. | N-01 | Timing change approved by CR-1 for fixture revision B; implementation compliance unverified |
| REQ-8 | The controller shall inhibit motion while local stop is asserted and shall retain the inhibit after stop is released until an explicit local resume action occurs. | N-02 | Approved requirement retained verbatim; implementation compliance unverified |

Pressure threshold and input validity contract remain project-controlled parameters; this change does not alter them.
