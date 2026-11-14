# Requirements to architecture to executed evidence

This fictional walkthrough demonstrates the skills' artifact contracts. It is
hand-authored and executed locally, not a controlled Sol/Astra evaluation output.

1. [Brief](brief.md): needs, scenarios, boundary, teaching assumptions.
2. [Requirements](requirements.md): sources, conditions, time reference, units, acceptance.
3. [Architecture](architecture.md): allocations, interfaces, decisions, hazards/controls.
4. [Verification](verification.md): six reproducible procedures and observations.
5. [Baseline](baseline.json): connected sources, allocations, verification, evidence.
   [Executed record](evidence/results.json): configuration hashes and measured results.

```sh
python examples/worked/cold-storage-alarm/run_checks.py
python examples/worked/cold-storage-alarm/run_checks.py --check
python scripts/check_trace.py examples/worked/cold-storage-alarm/baseline.json
```

In an authorized host, provide the brief and invoke `$mbse-requirements`, then
`$mbse-architecture` and `$mbse-verification-evidence`. Preserve IDs and request
artifacts through local execution. Withhold this worked answer when evaluating behavior.

Results establish sampled reference behavior only. Physical sensing/annunciation,
power loss, jitter, calibration, persistence, environmental qualification, and
operator response remain open. No real device, risk acceptance, or stakeholder
validation is claimed.
