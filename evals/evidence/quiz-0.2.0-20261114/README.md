# Revised quiz observations, bank 0.2.0

Three new participants answered the same 24 development questions after the
bank's choices, ambiguous stems and scoring contracts were independently repaired.
All three arms selected 24/24 keyed answers: no packaged skills, task skills, and
task-plus-domain skills. The [comparison](comparison.json) is descriptive.

Independent explanation review rated each arm 94/96 across 48 criteria. The same
two partial criteria remained in every arm: allocating responsibility for stale
data semantics (SEJ-029) and specifying a concrete way to resolve test-applicability
disagreement (SEJ-048). No critical errors or material key disagreement were found.
This is a selection ceiling with small reasoning gaps, not evidence that the
skills improve performance or that the benchmark discriminates expert systems
engineering.

Each arm retains its packet, original answers, usage when supplied, independently
bound review, and [reviewed score](none/reviewed-score.json). All three original
answers truthfully used the template's model:null value, which the scorer rejected.
The same producers created metadata-only corrected copies using the explicit
string unknown and an amendment note. Answers, packet bindings, run IDs and
original timestamps were unchanged; the raw submissions and old/new hashes are
preserved. Future templates now default to unknown.

The exact [0.2.0 source capsule](../../archive/benchmark-0.2.0/manifest.json)
retains the bank, key, catalog, skills and scoring implementation. Reproduce a
reviewed score with that version, using a new output path:

```sh
python3 evals/archive/benchmark-0.2.0/scripts/benchmark.py score --packet evals/evidence/quiz-0.2.0-20261114/none --answers evals/evidence/quiz-0.2.0-20261114/none/answers-metadata-corrected.json --review evals/evidence/quiz-0.2.0-20261114/none/review.json --output /workspace/mbse-score-reproduction.json
```

Bank 0.2.1 subsequently aligns three explanations/criteria with their existing
choices; all 60 answer selections and all question text remain unchanged. These
observations and reviews remain bound to 0.2.0 rather than being relabeled.
The [independent benchmark review](../../../docs/evidence/reviews/benchmark-independent.md.txt)
and [0.2.1 addendum](../../../docs/evidence/reviews/benchmark-0.2.1-addendum.md.txt)
record both revisions and their limits.

Participants had instruction-restricted packet access on a shared host with
ambient skill descriptions and general guidance. Exact model identity/settings,
tokens and costs were unavailable. Each arm is one context, not repeated samples;
reviewers are separate agents, not a human expert panel. No native activation,
statistical effect, leaderboard position or broad engineering competence is inferred.
