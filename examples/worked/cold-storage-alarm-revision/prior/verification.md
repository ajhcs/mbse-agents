# Verification procedures

Run `python examples/worked/cold-storage-alarm/run_checks.py` from repository root.
The runner uses explicit inputs, saves observations, and hashes implementation,
baseline, procedure, and design sources. No model API or physical equipment is used.

| ID | Requirement | Procedure | Acceptance |
| --- | --- | --- | --- |
| VER-01 | REQ-01 | Feed 8 deg C from t=0 through 2100 ms. | No early high; first at 2000 ms. |
| VER-02 | REQ-01 | High, one 7.9 deg C sample at 1900 ms, then high through 3800 ms. | Pending interval restarts; no high yet. |
| VER-03 | REQ-02 | Missing readings t=0 through 1100 ms. | First fault 1000 ms. |
| VER-04 | REQ-03 | Latch high, acknowledge at 9 deg C, recover without acknowledgement, acknowledge at 7 deg C. | Only final action clears high. |
| VER-05 | REQ-04 | Inspect VER-04 records, including unchanged ticks. | Exactly assertion at 2000 and clearance at 2300, correct states. |
| VER-06 | REQ-02, REQ-04 | NaN through 1000 ms, then valid 7 deg C. | Fault and recovery with exactly their two records. |
| VER-07 | REQ-01–REQ-04 | Traverse every reachable finite abstract state against an independent sample-counter oracle, using low/high/invalid temperature and both acknowledgement inputs. | No output or event mismatch in any reachable transition. |
| VER-08 | REQ-02 | Exercise eight invalid-temperature classes, eight invalid next timestamps, and nonboolean acknowledgement. | Invalid readings produce fault at the specified interval; invalid call contracts are rejected without changing state. |

VER-07 quotients absolute time by translation and saturates elapsed timers once
their decision threshold is reached. The implementation uses only those timer
threshold comparisons for control decisions. The oracle counts samples instead
of reading the implementation's timestamps. Every transition checks flags,
local-alarm output, and exact event production. This establishes equivalence
for that finite sampled abstraction and its six input combinations per state;
it does not establish real clock, scheduler, sensor, actuator, or persistence behavior.

The runner records start/finish timestamps, command, Python/platform versions,
source hashes, and measured observations. Each execution has an immutable file
under `evidence/runs/`; `evidence/results.json` selects the current record.
The previous selected bytes are archived before a replacement. `--output` refuses
an existing file, and `--check` reproduces observations without rewriting history.

Input-contract rejection and additional boundaries/interactions are in
`tests/test_reference_model.py`, separate from the stored evidence record.
None establishes physical performance, accuracy, persistence, or stakeholder acceptance.
The tracked evidence is executed against the reference model. Design is proposed;
review and hardware acceptance remain separate. Changed hashes or procedures need
rerun and applicability review. Structural trace checks do not prove semantic adequacy.
