# Engineering performance observations

These runs exercised all 13 shipped skills across 19 active cases, including a
full-catalog typo task, and five matched no-package baseline tasks. Participants
worked from frozen packets; the supplied requests, selected skill bytes, actual
outputs, run records and collection hashes are retained in this directory.
The [protocol](protocol.json) and original case/rubric snapshots precede production.

Independent agent review found 23 of the 24 outputs met every case criterion.
The task-plus-domain HO-13 response had one consequential ambiguity: its timing
plan classified an above-limit point estimate as failed while also classifying
an overlapping uncertainty interval as inconclusive, without precedence.
Its original output remains unchanged; [the targeted tuning record](../verification-tuning-20261113/README.md)
records the subsequent instruction change and fresh exercise.

[Design, reasoning and comparison review](../../../docs/evidence/reviews/performance-reasoning-review.md.txt)
assesses 15 outputs. [Domain and operational review](../../../docs/evidence/reviews/performance-domain-review.md.txt)
assesses the other nine. Their adjacent JSON records retain individual criteria,
located evidence, hashes and limitations. Four of five matched tasks tied at the
rubric ceiling; the baseline HO-13 avoided the ambiguity found in the skill arm.
This sample does not establish an advantage from the skills.

Start with the actual [skill-assisted revision](task-domain/HO-13/outputs/output.md),
[baseline revision](none/HO-13/outputs/output.md),
[director explanation](task-domain/HO-12/outputs/output.md), or
[negative-routing result](catalog/HO-08/outputs/output.md).
The last contains only the requested corrected word; its record reports no
skill file read.

All input bytes were checked. Three early design-case run records received a
final metadata pass after their per-case completion notice; the response bodies
and their hash maps did not change. The independent review retains old/new record
hashes and the producer's clarification. Earlier authoring-end timestamps were
overwritten, so those records cannot support precise production-time comparisons.

These are instruction-restricted smoke exercises on a shared host. Each producer
handled several cases in one context; exact served model/settings and costs were
unavailable. Skill reads are participant-reported, not native activation telemetry.
Reviewers are separate agents, not an independent professional acceptance board.
Criterion coverage is not statistical performance, hardware verification or a
claim of market leadership. Publisher PDFs retrieved during inspection remain at
the original workspace locations; URLs and retrieval hashes are preserved.
