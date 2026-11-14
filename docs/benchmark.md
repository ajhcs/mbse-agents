# Systems engineering judgment benchmark

This benchmark asks whether an agent understands a system, makes defensible
engineering judgments and explains them usefully. Writing a document or running
a tool is only part of that work.

There are two complementary tracks:

| Track | What the participant does | What can be assessed |
| --- | --- | --- |
| Judgment questions | Select a defensible response and explain the reasoning | Selection accuracy against a proposed key; independently assessed reasoning, assumptions and communication |
| Engineering performance | Work from supplied project facts or a multi-file baseline and deliver a useful result | Problem understanding, preserved intent, causal analysis, artifacts, change propagation, evidence judgment and explanation |

The question bank spans problem framing, lifecycle context, causal dependencies,
evidence, requirements, interfaces, alternatives, uncertainty, human and
organizational systems, communication, source interpretation and change review.
Its historical questions use supplied facts from projects before 2015 and ask
what transfers to a new situation. They do not reward recalling obscure accident
details or treating an old document as a current requirement.

The current inventory and source locators are in the
[question bank](../evals/benchmark/items.json). The
[historical gallery](../examples/historical/README.md) provides deeper studies.
The question keys and reviewer criteria are authored proposals that received
independent agent review. Their existence is not evidence of agent performance.
The [observed runs](../evals/evidence/quiz-0.2.0-20261114/README.md) reached a
selection ceiling in every arm and retained common reasoning gaps. Appropriate
domain adjudication and harder performance work remain necessary for broader claims.

The [initial three-arm diagnostic](../evals/evidence/quiz-diagnostic-20261113/README.md)
produced 24/24 selections in every arm. Independent review found that choosing
the longest option answered 54 of 55 single-choice questions correctly. Those
results establish no improvement from the skills. Version 0.2.0 revises the
choices and two ambiguous stems, clarifies one system boundary and strengthens
the scoring contract. The original questions, keys, code and results remain
unchanged in the archive. The revised questions require fresh assessment;
reducing a surface cue does not establish useful difficulty or valid keys.

## Try a question

From the repository, use Python 3.10 or newer. On Windows, `py` can replace
`python3` in these commands.

```sh
python3 scripts/benchmark.py list --split practice
python3 scripts/benchmark.py practice --item SEJ-001
python3 scripts/benchmark.py practice --item SEJ-001 --answer A --reason "Explain why you selected this option."
```

Replace `A` and the explanation with your answer. Multiple-selection questions
accept several letters after `--answer`. Feedback says whether the selection
matches the proposed key and explains its basis. It does not automatically grade
your explanation. A defensible challenge to a key is a finding to adjudicate.

## Run an agent exercise

Prepare a fresh packet and give only that packet to a new participant chat:

```sh
python3 scripts/benchmark.py prepare --split development --arm task-domain --output /workspace/mbse-evaluation/development-task-domain
```

The packet contains the request, selected questions, a response template, a
manifest of exact input hashes and the selected skills. It does not include
keys, reviewer criteria, historical answers or other runs. The participant fills
the response template and saves `answers.json`, preserving its `schema_version`
and `packet` fields as well as the original packet inputs. These fields bind the
answers to that packet and its input revision. Moving answers to another arm or
new packet requires a new run; the scorer rejects an unchanged replay.
The run fields record the actual producer, model, host, settings, times, tools
and unavailable information. Use explicit `unknown` when a host does not expose
a value; do not infer model identity from marketing names.

Use `--item SEJ-003 --item SEJ-008` to select a small exercise or `--dimension
interfaces` to focus on one reasoning area. Comparison arms are:

| Arm | Skills exposed |
| --- | --- |
| `none` | No skill packages |
| `task` | Relevant task packages |
| `task-domain` | Relevant task and domain packages |
| `catalog` | All shipped packages, for discovery and nonactivation assessment |

Use identical selected questions and host/tool access across comparison arms.
A `none` packet contains no skill files; it does not disable personal, global or
parent-directory skills in the host. Record the effective discovery inventory
and prevent unintended skill loading when evaluating a no-skill baseline. A
fresh conversation alone does not establish host isolation.
A full-catalog packet tests exposure; the evaluator must also observe which
skills the host actually activates. Merely copying packages is not an activation
result. Model settings, context, prior exposure and order effects also matter.

```sh
python3 scripts/benchmark.py score --packet /workspace/mbse-evaluation/development-task-domain --answers /workspace/mbse-evaluation/development-task-domain/answers.json --output /workspace/mbse-evaluation/development-score.json
```

The score reports each item, unanswered items, accuracy by reasoning dimension,
an equal-dimension summary and a mathematical uniform-choice reference. For a
single-choice question the reference is `1 / number of options`; for a
multiple-selection question it is `1 / number of nonempty subsets`. This is not
a claim about how an informed person or model guesses.

An incorrect or omitted selection receives no selection credit. No partial
credit is inferred from a subset of a multiple-selection answer. An explanation
may still reveal valuable reasoning or a flawed question; it needs separate
assessment. Correct letters without sound explanation do not establish
engineering competence.

## Assess explanations independently

The reviewer receives the unchanged participant output, original facts and the
separate reviewer key after production is finished. For each question, review
the listed reasoning criteria on this scale:

| Rating | Meaning |
| --- | --- |
| 0 | Missing, contradicted or materially unsupported |
| 1 | Partly addressed, with a consequential gap or ambiguity |
| 2 | Addressed coherently using the supplied facts and appropriate limits |

Review the selection and the key as well as the explanation. Record critical
errors separately; a fluent response must not conceal an invented source,
unsupported acceptance claim or important loss of stakeholder intent.

Generate a separate review template after production:

```sh
python3 scripts/benchmark.py review-template --packet /workspace/mbse-evaluation/development-task-domain --answers /workspace/mbse-evaluation/development-task-domain/answers.json --output /workspace/mbse-evaluation/review.json
```

The template contains no ratings. It binds the assessment to the exact answer
bytes, packet manifest, key revision and selected reasoning criteria:

```json
{
  "schema_version": 2,
  "answers_sha256": "SHA256_OF_THE_ACTUAL_ANSWERS_FILE",
  "packet_manifest_sha256": "SHA256_OF_THE_PACKET_MANIFEST",
  "key_sha256": "SHA256_OF_THE_KEY_FILE",
  "criteria_sha256": "HASH_GENERATED_BY_REVIEW_TEMPLATE",
  "reviewer": "identified-reviewer",
  "independent_of_production": true,
  "items": {
    "SEJ-003": {
      "criteria": [2, 1],
      "comment": "Explain the assessment against the actual response.",
      "critical_errors": []
    }
  }
}
```

Disposition every selected question and every reasoning criterion; the example
above is only the file shape. Pass the file with `score --review review.json`.
The tool labels it a reviewer-reported assessment. It cannot authenticate the
reviewer's competence or prove independence from a name. Domain disagreements
and consequential claims require appropriate expert adjudication.

## Assess engineering performance

The performance bank is [cases.json](../evals/cases.json). Cases include broad
systems questions, automotive and defense reasoning, historical transfer,
source criticism and a concrete multi-file revision exercise. HO-13 supplies
approved source wording, requirements, architecture, an old observation and a
change request. The participant must preserve the inputs and produce a coherent
revision and review.

```sh
python3 scripts/prepare_eval.py --case HO-13 --arm none --output /workspace/mbse-evaluation/change-baseline
python3 scripts/prepare_eval.py --case HO-13 --arm task-domain --output /workspace/mbse-evaluation/change-skills
```

Independent reviewers assess outputs against source facts and case criteria.
Record located findings, important omissions, invented claims, preserved human
edits, task completion and the effort needed to repair the result. These
performance tasks are the primary evidence for an improvement in engineering
reasoning. Quiz scores are a diagnostic, particularly when most participants
choose the correct options.

## Practice, development and evaluation

The bank separates practice, development and `evaluation-public` questions.
Every split covers all reasoning dimensions. Practice supports feedback.
Development supports examining failures and revising the agent. The reserved
public evaluation split is withheld from the prepared development packet, but
its questions and keys are in this public repository. It is not a secret or
leak-proof test set. Historical projects may also be familiar from model training.
Version 0.2.0 was revised after authors and reviewers inspected the full bank;
none of its splits should be described as untouched by the development process.

After a producer has seen a question or key, record the exposure and use a new
reviewed variant for a credible later assessment. Do not tune on the reserved
set and then describe it as untouched. A future protected evaluation must be
held outside the producer's accessible repository and tools.

Before a comparison, state the workload, outcomes, errors that are unacceptable,
required review, and conditions for retaining or rejecting a change. Use repeated
independent runs where the decision justifies it. Separate gains in reasoning
from longer answers, additional tool access or more expensive model settings.

```sh
python3 scripts/benchmark.py report /workspace/mbse-evaluation/baseline-score.json /workspace/mbse-evaluation/candidate-score.json
```

The report requires matching questions, bank and key revisions and distinct run
IDs. It validates outcome fields and recomputes selection aggregates before
reporting them. Packet checks require every mandatory input and every file in
the declared skill packages, and reconcile the arm with actual package exposure.
These consistency checks do not authenticate the producer or prevent a person
from deliberately fabricating a complete record. It presents descriptive results;
it does not automatically announce a
winner, statistical significance or release readiness. Follow
[the evaluation protocol](evaluation.md) for recorded judgments and the limits
of current evidence.

## Inspect question construction

```sh
python3 scripts/benchmark.py diagnose
python3 scripts/benchmark.py diagnose --bank evals/archive/benchmark-0.1.0/evals/benchmark/items.json --keys evals/archive/benchmark-0.1.0/evals/benchmark/keys.json
```

The diagnostic reports keyed positions and actual accuracy for selecting the
longest or shortest option by character count and by word count, both overall
and by split. It exposes item lengths, ties and the deterministic tie rule.
Multiple-selection questions are excluded from these single-option shortcuts.
Use the results to investigate cues alongside independent content review, rather
than imposing a numeric threshold as a substitute for question quality. Output
can be preserved with `--output` to a fresh path. Score, diagnostic and review
template commands refuse existing output files, including dangling symlinks.
