# What validation establishes

`python scripts/validate.py` checks the catalog against discoverable packages,
frontmatter/UI metadata, generated indexes, local Markdown links, the worked
example's trace/configuration hashes, and rerun reference-model outcomes.
`python -m unittest discover -s tests` adds negative cases for installer collisions,
local edits, managed updates/backups, missing allocations/evidence, stale hashes,
planned/failed/inconclusive evidence, input-contract failures, and alarm recovery.
Fixtures use owned temporary folders inside the checkout, avoiding host temp
permission differences. No dependencies, credentials, network, or model calls.

These are offline checks of packaging and selected artifact behavior. They do
not establish standards compliance, stakeholder validation, or Sol/Astra quality.
The domain gallery remains illustrative and source review is incomplete.

## Separate behavior assessment

`evals/cases.json` contains requests and raw input facts. `evals/rubrics.json`
contains reviewer criteria, stored separately and omitted from installed packages
and prepared task packets. Prepare a case for an authorized host:

```sh
python scripts/prepare_eval.py --case HO-01 --output /path/to/isolated-packet
```

The packet contains only the request and selected skill packages. Its inputs
exclude the worked answer, previous benchmark prose, and reviewer criteria.
The public cases are held out from the skill entrypoints/references, not a secure
hidden benchmark. After an agent has seen one, use a fresh variant for a credible
subsequent assessment. Do not claim leak-proof evaluation or tune on a final
test set and report it as untouched.

Run realistic artifact-producing tasks, including ambiguous inputs, changes,
evidence gaps, and misleading source claims. Judge observable results:
source-grounded requirements, plausible alternatives, preserved IDs and semantics,
usable interface/verification contracts, truthful execution status, completed
artifacts, and useful handling of unresolved decisions. Include narrow tasks
and requests that should not load domain skills. For discovery tests, expose the
whole catalog with `--catalog` (for example, HO-08) and observe actual activation
in the host; an empty selected-skills packet cannot establish implicit routing.
No full-catalog behavioral routing run has been performed here. Do not grade wording similarity
or require a particular document length.

For each run, record case/version, skill commit and hashes, model ID and supported
settings, host/tool versions, source access, actual output paths, tokens/latency/cost
when available, exceptions, and reviewer identity/dispositions. Separate producer
from reviewer and withhold expected findings from the producer. Review accepted
and rejected outcomes against original facts and primary sources; generated
rubrics are proposals requiring expert adjudication, not validated oracles.

For comparisons, use baseline and candidate with the same inputs and available
tools. Include repeated runs for consequential decisions and document variability.
Track completion, important errors, evidence integrity, reviewer repairs, and task
cost. Set workload-specific acceptance before deciding on the upgrade. No paid
runner is provided or invoked automatically.

Independent repository review and a fresh skill-use smoke exercise can identify
defects, but are not a controlled comparison of GPT-6.1 Sol and GPT-6 Astra. Record
what was actually done and any unavailable model/settings or primary sources.
