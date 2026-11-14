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

Input-contract rejection and additional boundaries/interactions are in
`tests/test_reference_model.py`, separate from the stored evidence record.
None establishes physical performance, accuracy, persistence, or stakeholder acceptance.
The tracked evidence is executed against the reference model. Design is proposed;
review and hardware acceptance remain separate. Changed hashes or procedures need
rerun and applicability review. Structural trace checks do not prove semantic adequacy.
