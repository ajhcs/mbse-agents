# Executable domain studies

The five flagship examples now contain explicit fault models, complete static
Boolean analysis, exact conditional probability scenarios, checked claims and
retained counterexamples. The pump additionally contains a temporal clamp-release
model with fault injection and recovery sequences. The remaining fifteen systems
have current identity, source and evidence-status inventories; they have no
executed system simulation.

| Study | Concrete question | Executed artifact |
| --- | --- | --- |
| Flight management | Can equality comparison detect mutually consistent wrong guidance? | [FMS model study](../examples/aerospace/flight-management-system/analysis/report.md) |
| Emergency braking | Can fusion or a common environment defeat nominal sensor redundancy? | [AEB model study](../examples/automotive/autonomous-emergency-braking/analysis/report.md) |
| Ground control | Can shared infrastructure or stale-data dependencies defeat separate links/monitors? | [GCS model study](../examples/defense/uas-ground-control-station/analysis/report.md) |
| Infusion pump | Does a liveness watchdog prevent running-but-wrong delivery, and what shared sensor/drive paths remain? | [Pump model study](../examples/medical-device/smart-infusion-pump/analysis/report.md) |
| Quantum control | Does a sequence precheck protect against downstream RF faults, and is attenuation actually credited? | [RF-protection model study](../examples/electronic-systems/quantum-processor-control/analysis/report.md) |
| Pump clamp | What release/closing allocations meet a 500 ms proposal, which faults defeat closure, and can recovery reopen automatically? | [Temporal study](../examples/medical-device/smart-infusion-pump/analysis/clamp-study.md) |

## Reproduce the analyses

From the repository root, using Python 3.10 or newer and its standard library:

```sh
python3 scripts/analyze_gallery.py --check
python3 examples/medical-device/smart-infusion-pump/analysis/run_clamp_checks.py --check
python3 scripts/check_gallery.py
```

Omitting `--check` explicitly writes a fresh current report and preserves its
content-addressed run, including exact inputs and outputs. Historical evidence
is retained. Initial prototype runs whose inputs were not captured are explicitly
marked incomplete; their result bytes remain historical observations. Current
runs retain full sources and results. The pre-hardening baselines are stored as content-and-hash JSON
snapshots under each example's `history/`; they are not current claims.

An installed CSE failure-analysis tool was executed as a separate implementation
cross-check of each static model. Its input, source hashes, command and complete
result are retained. Normal reproduction needs no CSE installation; an optional
fresh cross-check uses an explicitly selected helper:

```sh
python3 scripts/analyze_gallery.py --cse-helper /path/to/cse/skills/analyze-system-failures/scripts/failure_analysis.py
```

The local collectors bind loaded module code to its source and origin, capture
the exact input bytes they parse, and reject configuration changes before
publication. Current execution receipts require run identity, timestamp, command,
Python version, scope, loaded-source bindings and the archived result hash.
CSE runs use a fresh empty bytecode-cache prefix with cache writes disabled.
The five CSE source hashes are an inventory observed before and after execution;
they are not instrumented loaded-module bindings for the external implementation.
Previous CSE receipts are retained by content hash.

## What the results establish

Static models enumerate every assignment over the declared bounded set of basic
events. Minimal cuts preserve repeated-event identity. Scenario probabilities
are exact rational sums conditioned on synthetic per-demand parameters and a
declared mutual-independence assumption after shared causes are represented.
They do not use ungrounded products of failure rates or rare-event Monte Carlo.

Temporal clamp runs execute an explicit sampled transition model. A test can
pass because it finds the expected requirement violation; such a requirement
remains failed in that scenario. The studies expose architectural assumptions
and candidate improvements, while retaining adversarial failure conditions.

These results do not establish measured failure rates, flight-hour reliability,
ASIL/SIL attainment, actual fluid occlusion, clinical benefit, aircraft behavior,
RF/quantum/thermal dynamics, certification or risk acceptance. The next evidence
is specific: validate event meanings and dependencies against implementation;
replace scenario parameters with appropriately conditioned observations; test
the physical observation and actuation paths; evaluate representative operation.

The [source ledger](sources-domain.md) identifies the method sources and their
limits. The gallery checker separately verifies record identities, explicit
open references, real drafted/executed artifacts and reproducible model results.
Passing those structural checks is not a semantic or standards audit.
