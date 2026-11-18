# Start with an engineering question

MBSE Agents helps investigate a system, explain the relationships that matter,
develop connected engineering artifacts and challenge proposed decisions. Begin
with the question and available material. A complete document set is optional.

## Install selected skills

From this repository, use Python 3.10 or newer. The commands below use `python3`;
on Windows use `py` and a quoted project path.

```sh
python3 scripts/install.py --list
python3 scripts/install.py --project /path/to/project --skill mbse-systems-engineering --skill mbse-requirements --skill mbse-architecture --skill mbse-verification-evidence --dry-run
python3 scripts/install.py --project /path/to/project --skill mbse-systems-engineering --skill mbse-requirements --skill mbse-architecture --skill mbse-verification-evidence
```

Open the destination project in a host that discovers `.agents/skills` and confirm
the intended skills appear. [Host-specific installation](../platform/codex/install.md)
explains discovery; the [portable guide](../platform/generic/install.md) covers
other context-loading mechanisms. A release plugin is built from the canonical
packages; see [distribution](SUBMISSIONS.md).

## Try the supplied brief

Read [the cold-storage stakeholder brief](../examples/worked/cold-storage-alarm/brief.md).
Copy that brief into your project as input, without the worked answer. Ask:

> Use $mbse-systems-engineering to turn this cold-storage alarm brief into
> reviewable requirements, an architecture, and verification procedures. I’ll
> check that NEED-01 through NEED-04 each have a disposition, the temperature
> and timing conditions carry through to the tests, and the operator’s response
> is reflected in the design. Mark proposed values, unresolved decisions, and
> tests still to run.

Review the actual output against the brief. Check whether it preserves the
temperature/time conditions, identifies sensor failures and acknowledgement,
connects the operator to the architecture, and gives procedures that could
distinguish a correct design from an incorrect one. Ask the agent to repair
specific disagreements while retaining existing IDs and accepted wording.

Then compare the result with the [worked baseline](../examples/worked/cold-storage-alarm/README.md).
It is an instructional implementation, not the only acceptable design. From the
repository you can reproduce its saved model observations:

```sh
python3 scripts/check_trace.py examples/worked/cold-storage-alarm/baseline.json
python3 examples/worked/cold-storage-alarm/run_checks.py --check
```

These commands inspect and execute the supplied reference model. They do not
execute a newly generated design unless its model and procedure are explicitly
connected to the run.

## Bring an existing project

Supply the current baseline, the change or review decision, the relevant source
material and the location where outputs belong. State which decisions and wording
are already agreed. For example:

> Review the proposed alarm-response change in this baseline. Identify affected
> requirements, interfaces, operating procedures and old evidence. Preserve the
> accepted source text and IDs. Explain the consequences, implement authorized
> draft repairs, and show what needs new verification.

Use [task workflows](workflows.md) to choose a focused entry point. Explore
[historical engineering cases](historical-gallery.md) to practice reasoning from
project evidence, and [the benchmark](benchmark.md) to assess judgment separately
from tool execution.
