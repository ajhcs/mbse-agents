# Working on MBSE Agents

The reusable workflows live in `.agents/skills`. Read the relevant `SKILL.md`
before changing a skill; use its references only when the task needs them.
`catalog.json` identifies the shipped skills. Generate its derived discovery
files with `python scripts/catalog.py --write` after changing metadata.

Preserve useful engineering substance. Prefer decision criteria and evidence
contracts over fictional personas, forced itineraries, or length targets.
Separate requirements, guidance, engineering judgment, and illustrative data.
Check exact regulatory and standards claims against accessible primary sources;
record the edition, locator, and limits in `docs/sources.md`. Do not invent clause
numbers, approvals, tool access, or provenance for unsupplied course material.

The local checks use disposable fixtures and no production or paid model access.
Run `python scripts/validate.py` and `python -m unittest discover -s tests` for
changes to packaging or validation. Fix relevant failures and rerun without
asking at each step. Passing these checks does not demonstrate model quality.
Use `docs/evaluation.md` when making a behavioral or model upgrade claim.

Examples are instructional baselines. Preserve IDs and evidence status when
editing them. A planned test or plausible narrative is not executed evidence.
Installation must preserve existing project instructions and refuse collisions.
