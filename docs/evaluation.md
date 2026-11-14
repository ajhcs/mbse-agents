# Evidence and agent evaluation

The systems engineering agent is evaluated on how it understands, reasons,
explains and completes engineering work. Repository checks and agent assessments
answer different questions.

## Repository and artifact checks

`python3 scripts/validate.py` checks the catalog, package discovery, generated
indexes, local links and the worked example's trace/evidence contract.
`python3 -m unittest discover -s tests` exercises meaningful behavior and failure
cases in the maintenance tools. Benchmark checks cover packet separation,
input hashes, score integrity, omitted/invalid responses and reviewer binding.
Fixtures use disposable folders inside the checkout. No credentials or model API
are needed for these checks.

Passing maintenance tests establishes the tested software behavior. It does not
establish the quality of the agent, standards conformity, risk acceptance or
physical behavior of an illustrative design. A gallery simulation establishes
only the named modeled observables under its documented assumptions.

## Judgment and performance tracks

Use [the benchmark guide](benchmark.md). The judgment bank covers twelve
reasoning dimensions using selections plus explanations. Automatic scoring is
limited to matching selections against a proposed key. Independent explanation
review and open engineering performance tasks assess the reasoning itself.
A high quiz score can reveal a ceiling and is not a substitute for difficult
artifact work.

`evals/cases.json` supplies performance requests and raw input fixtures;
`evals/rubrics.json` supplies separate proposed review criteria. All currently
shipped skills are selected by active cases. The former founder-review case is
retained as retired, and the original case/rubric bytes are archived under
`evals/archive/v1`. Existing HO-01 output and assessment bytes remain historical.

```sh
python3 scripts/prepare_eval.py --case HO-13 --arm task-domain --output /workspace/mbse-evaluation/ho13
python3 scripts/prepare_eval.py --case HO-08 --catalog --output /workspace/mbse-evaluation/routing
```

Packets include only the request, explicitly selected raw fixtures, chosen skills
and an input manifest. All sources are preflighted; copying is staged before the
complete packet appears. Existing destinations are refused. Keys, review criteria
and prior outputs are not copied. These public cases are separated from producer
inputs, not a protected hidden test set. After exposure, use a fresh reviewed
variant and record the exposure rather than claiming an untouched evaluation.

## Run and review contract

Before running, record:

- Case/question version and exact input/package hashes; candidate source revision.
- Comparison arm: no skills, task skills, task plus domain, or full catalog.
- Effective host skill inventory, including global and parent-directory packages;
  a no-skills packet does not itself disable those sources.
- Producer, actual model ID, supported settings, host and available tools/sources.
- Intended task and observations, important failure categories, and decision criteria.
- Permitted resources and where independent outputs and review will be saved.

At completion, record output hashes, start/end times, tokens/latency/cost when
available, exceptions and actual skill activation when evaluating discovery.
Preserve unknown metadata as unknown. Do not backfill it from an assumed model
or transfer metadata from another run.

The independent reviewer receives unchanged outputs, original facts and criteria
after production. Report located errors and their consequences, missing decisions,
source fidelity, preserved identities/human edits, interface and evidence
coherence, task completion, communication and the work needed to repair the result.
Check the proposed rubric and answer key as well as the output. A generated key
is not an authoritative engineering oracle. Consequential domain disagreements
need appropriate expert adjudication.

For change tasks, check actual before/after artifacts. A fluent paragraph about
impact analysis does not establish that IDs, accepted wording and evidence
applicability were preserved through a multi-file revision. Planned tests remain
planned until actual execution records establish otherwise.

## Comparisons and tuning

Compare the same model, settings, raw task, tools and source access across arms
when measuring the contribution of the skills. Keep model-upgrade comparisons
separate. Use fresh participant contexts and independent repeated runs where the
decision warrants them; record order effects, known exposure and variability.

Inspect failures on practice/development work, make a specific agent change, and
reassess using fresh or genuinely withheld work. Evaluate important errors,
completion, explanation quality, repair effort and task cost. Do not optimize for
particular wording, prescribed document length or successful option guessing.
Predeclare the workload-specific acceptance criteria; no automatic aggregate
score authorizes publication, engineering acceptance or a claim of superiority.

## Current evidence

The [evidence index](../evals/evidence/README.md) links actual quiz responses,
24 engineering-task outputs, three connected historical project exercises,
and a targeted guidance revision with two fresh transfer outputs. Separate
agent assessments retain individual criteria, located gaps, hashes and limits.
The earlier HO-01 exercise remains historical evidence with its original metadata.

The new quizzes reach the same selection and reasoning scores in every arm.
Most matched artifact cases also tie; one skill-assisted change review contains
an uncertainty-rule ambiguity absent from its baseline. Its original result is
preserved, and the fresh transfer check does not demonstrate an incremental gain.
These observations do not establish general superiority or a causal skill effect.

The [initial quiz diagnostic](../evals/evidence/quiz-diagnostic-20261113/README.md)
records three 24-question runs with identical 24/24 selection scores. Independent
review showed that the longest-option shortcut answered 54/55 single-choice
questions across that bank. Preserve this as a failed question-construction
diagnostic, not evidence of skill benefit. The original bank and scorer are
archived; version 0.2.0 revises the questions and adds packet-bound answers,
revision-bound reviews, input inventory checks and validated report aggregates.
Independent content review and fresh production must be identified by their
recorded outputs when assessing the revision; a scorer repair alone establishes
no change in agent performance.

No paid model runner is supplied or invoked automatically.
