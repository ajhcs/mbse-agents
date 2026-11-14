# A changed requirement, failed evidence, and a verified model repair

This executed walkthrough shortens REQ-02's invalid-reading qualification interval
from 1 s to 500 ms, while preserving its identifier and the unchanged requirements.
The deliberate teaching change is recorded as [CR-01](change-request.md). Its value
is an instructional choice; no real stakeholder approval is implied.

| Configuration | Requirement interval | Implementation interval | Actual execution |
| --- | --- | --- | --- |
| [Prior snapshot](prior/README.md) | 1000 ms | 1000 ms | Eight procedures pass; first sensor fault at 1000 ms. |
| [Failed snapshot](failed/README.md) | 500 ms | 1000 ms | VER-03, VER-06, VER-07 and VER-08 fail. The shortened deadline is missed. |
| [Repaired model](reference_model.py) | 500 ms | 500 ms | Eight procedures pass; first sensor fault at 500 ms. |
| Prior record reused against current baseline | 500 ms | Prior record | Configuration/selection mismatch rejects the record; zero requirements receive passing evidence credit. |

The failed execution is retained with its source configuration, observations,
run ID and timestamps. It is valid evidence of a failed design. The repaired run
supports the revised sampled behavior, with all original requirement, function,
component, actor, interface and procedure IDs preserved. CR-01 is a new source;
the original NEED-02 brief remains available rather than being rewritten.

```sh
python3 -B examples/worked/cold-storage-alarm-revision/compare_revisions.py --check
python3 -B scripts/check_trace.py examples/worked/cold-storage-alarm-revision/failed/baseline.json
python3 -B scripts/check_trace.py examples/worked/cold-storage-alarm-revision/baseline.json
```

The [workflow receipt](evidence/revision-check.json) records actual reproduction
of every stage and the attempt to reuse stale evidence. The failed snapshot's
`run_checks.py --check` deliberately exits 1 after reproducing four failures;
the comparison command expects exactly those failures. It does not mask an
unrelated execution error as the expected failure.

The repaired model's finite-state exploration checks all reachable states under
low/high/invalid readings and both acknowledgement values, comparing each output
and event against the independent sample-counter oracle. The abstraction and
its assumptions are defined in [verification](verification.md). These executions
establish model behavior, evidence rejection and ID preservation. Sensor hardware,
clock jitter, annunciation, persistence and operator effectiveness remain outside
the executed scope.

To record another model execution, run `run_checks.py` in the relevant snapshot;
its previous selection is archived before replacement. `compare_revisions.py
--record` likewise archives the previous workflow receipt before selecting a new
one. `--record --output <new-path>` creates an additional receipt and refuses to
overwrite an existing file.
