# Replay a numeric operating table

Use this check when operator action depends on one or more inclusive minimum or maximum readings. The checker reads a Markdown pipe table with a unique event label per row, a separate column for each numeric gate, and plain decimal thresholds in consistent units. Confirm that the operator prose agrees with the gate meanings and the action on a failed gate. If the checker is unavailable or the requested handoff uses an unsupported format or rule, compare the actual delivered decisions with the source-derived cases and record the method and its limits.

From the source records, derive feasible starting readings, signed changes before each event, and the action the source permits. Include changes in rate, measurement bias, reserve, and the entire fallback interval where applicable. Use separate paths for alternative events. Include equality and a just-insufficient reading for each binding threshold, varying one reading at a time. A replay from a comfortable starting state can miss a gate that allows an infeasible continuation. Work from the sources independently of the draft thresholds.

For example, given the following handoff row:

| Event | Minimum stock | Maximum occupied | Action |
| --- | --- | --- | --- |
| Late arrival | 14 bins | 22 bins | Accept only if both limits hold. |

Set each step’s `expect` to `"allow"` when the source permits proceeding or `"block"` when it requires holding. A blocked step ends that case. This example exercises equality at the minimum:

```json
{
  "event_column": "Event",
  "gates": {
    "Minimum stock": {"sense": "min", "unit": "bins"},
    "Maximum occupied": {"sense": "max", "unit": "bins"}
  },
  "cases": [{
    "name": "Late arrival at minimum stock",
    "basis": "Example dispatch record permits acceptance after six bins leave the opening stock of twenty.",
    "initial": {"Minimum stock": 20, "Maximum occupied": 19},
    "steps": [{"event": "Late arrival", "delta": {"Minimum stock": -6}, "expect": "allow"}]
  }]
}
```

From the skill directory, run `python3 scripts/replay_gates.py /path/to/decision.md /path/to/cases.json`. You can also call the script by its path from the workspace. The checker reads thresholds from the supplied table, adds each step's net change to the preceding state, and allows the action only when all its gates hold. Use an empty unit string for bare numbers whose unit is defined by the column. JSON changes can use exact fractions such as `"-5/12"`. Convert rates and duration to changes in the display units, and apply any display quantization in the case model.

Exit 0 means the replayed actions match the specified expectations. Exit 1 identifies a decision mismatch. Exit 2 means the inputs could not be checked. Only numeric gate rows named by the cases are exercised. A mandated rollback with no decision threshold belongs in the branch model and procedural review. The checker relies on the supplied state transitions, units, gate directions and expected actions. It does not infer physical behavior, certify coverage or interpret free-form procedural prose. Rerun after editing the issued table and retain its hash with the results.
