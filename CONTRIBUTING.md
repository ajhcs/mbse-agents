# Help improve MBSE Agents

Bug reports, domain corrections, workflow ideas, examples, and requests for new
skills or agents are welcome. You do not need a finished implementation or deep
MBSE experience to open an issue. Tell us the task you wanted to complete, what
happened, and what a useful result would look like. Please omit confidential,
classified, export-controlled, proprietary, or patient-identifying material.

Use the issue forms for a [bug](https://github.com/ajhcs/mbse-agents/issues/new?template=bug.yml),
[feature](https://github.com/ajhcs/mbse-agents/issues/new?template=feature.yml), or
[new skill/agent](https://github.com/ajhcs/mbse-agents/issues/new?template=new-agent.yml).
Sources and small reproductions help, but are optional for an initial request.

Cole Lyons (@ajhcs) maintains the project and decides what ships. Illustrative
PRs are welcome; they may inform an independently implemented change rather
than be merged directly. Opening one does not guarantee acceptance or review
timing. This policy applies consistently to all five domains and the task skills.

For an implementation:

1. Start a branch and keep the change tied to a concrete engineering use case.
2. Follow [the skill design](docs/design-spec.md); read the relevant skill and
   references. Preserve domain substance without invented credentials or rigid
   output itineraries.
3. Cite corrections at the precision you verified. Include edition, locator,
   access limits, and the practical impact of a standards change. Do not globally
   replace a legacy program's approved basis with a new edition.
4. Regenerate discovery metadata with `python scripts/catalog.py --write`.
   Run `python scripts/validate.py` and `python -m unittest discover -s tests`.
   For behavior changes, add a realistic case and describe independent assessment
   under [the evaluation protocol](docs/evaluation.md).
5. Explain the problem, resulting behavior, verification, and remaining gaps in
   the PR. A standards-aware reviewer should assess regulated-domain changes.

There is no word count or skill count target. Good additions improve decisions
and artifact quality. Remove repeated scaffolding when it obstructs the task;
keep a constraint when violating it could cause a concrete engineering error.
