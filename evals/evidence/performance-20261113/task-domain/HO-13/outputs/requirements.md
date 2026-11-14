# Controller requirements, revision B — proposed coherent baseline

| ID | Requirement | Source | Status |
| --- | --- | --- | --- |
| REQ-7 | The controller shall assert the local high-pressure warning within 200 ms after the valid pressure input first meets the high-pressure condition during operation. | N-01 | Timing criterion approved for fixture revision B by CR-1; implementation unverified |
| REQ-8 | The controller shall inhibit motion while local stop is asserted and shall retain the inhibit after stop is released until an explicit local resume action occurs. | N-02 | Approved for fixture revision A |

Pressure threshold and input validity contract remain project-controlled parameters; this change does not alter them.

## Change and authority

CR-1 changes only REQ-7's deadline from 500 ms to 200 ms. Its identity, trigger, end event and operating conditions are unchanged. The revision-A wording remains in `../inputs/requirements.md`. The complete REQ-8 table row and the project-parameter note above are preserved verbatim. REQ-8's revision-A approval is historical; its unchanged obligation is carried forward, with no new implementation-verification claim.

N-01 and N-02 in [source.md](source.md) remain authoritative. That source, including the protected operator note, is copied byte-for-byte. The approved change is retained in [change-request.md](change-request.md). Proposed architecture and evidence work do not approve additional requirements or an implementation.

## Allocation and evidence disposition

| Requirement/source | Responsibility and intended evidence | Current claim |
| --- | --- | --- |
| REQ-7 / N-01 | COMP-1 input processing, COMP-2 detection, COMP-3 local warning over IFC-1/IFC-2; VER-7 timing analysis and measurement | Unverified for B. Existing 260 ms serial allocation does not support ≤ 200 ms; EVD-A-7 remains historical A evidence. |
| REQ-8 / N-02 | COMP-2 inhibit latch and IFC-3 local stop/resume intent; actual motion-output binding remains to be identified; expanded VER-8 | Unverified. Proposed state guards repair the documented contradiction; existing visibility-only plan did not test motion or recovery. |
| N-02 restoring-data restriction and operator note | Latched inhibit must persist across data/network recovery and remain visible to the operator; VER-8 covers those cases | Source-authoritative behavior; no edit to REQ-8. Detailed display binding is an architectural open item. |

See [architecture.md](architecture.md), [verification.md](verification.md), and [change-review.md](change-review.md). A trace is an allocation or evidence intention, not a passed result.
