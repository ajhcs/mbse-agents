# Requirements to architecture to executed evidence

This fictional walkthrough demonstrates the skills' artifact contracts. It is
hand-authored and executed locally, not a controlled Sol/Astra evaluation output.

1. [Brief](brief.md): needs, scenarios, boundary, teaching assumptions.
2. [Requirements](requirements.md): sources, conditions, time reference, units, acceptance.
3. [Architecture](architecture.md): allocations, interfaces, decisions, hazards/controls.
4. [Verification](verification.md): eight reproducible procedures, including finite-state exploration and invalid-input checks.
5. [Baseline](baseline.json): connected sources, allocations, verification, evidence.
   [Executed record](evidence/results.json): configuration hashes and measured results.

The [original v1 snapshot](history/legacy-v1/README.md) retains all supplied
artifacts and results byte-for-byte; its six original procedures still reproduce.
The current schema adds exact source locators, the ACTOR-01/IFC-02 acknowledgement
interface, execution provenance, and separate integrity/outcome/acceptance reporting.
Run history is append-only under `evidence/runs/`; the selected result can change
only after its previous bytes have been archived. Each `--check` executes a fresh
reproduction and leaves the historical record's date and host untouched.

Continue with the [executed revision walkthrough](../cold-storage-alarm-revision/README.md)
to see a shorter requirement deadline fail against the old implementation,
invalidate prior evidence, and pass after an actual model repair. The
[evidence contract](evidence-contract.md) describes what the checker establishes.

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
