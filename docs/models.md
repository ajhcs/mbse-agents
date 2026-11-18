# Choosing and upgrading a model

The engineering contracts do not depend on a particular model. Choose a model
available in the intended host, then evaluate it on the tasks and evidence limits
that matter to the project. No comparative model advantage has been established
for this release. Host discovery, tool access, context limits and model behavior
need separate checks.

`config/model-profiles.json` records optional candidate model IDs and documentation
links, not a support guarantee or measured ranking. It is informational;
installing a skill does not change the host's model setting.
Choose a model and supported reasoning setting in your host. For Codex CLI,
explicit selection looks like:

```sh
codex -m gpt-6.2-sol
codex -m gpt-6.2-astra
```

Both IDs appeared in `codex debug models` on Codex CLI 0.169.0 on 2026-11-17.
Check the catalog in the account and host that will run the task. Historical
judgment studies retain the model and settings pinned in their protocols.

## Set the review criteria and reasoning effort

Give the model the decision, the relevant inputs, and what you intend to check.
For a timing requirement change, provide both baseline revisions and ask which
prior tests still apply. Ask for the affected requirement IDs, the conditions
each test actually exercised, and any evidence gaps that block closure.

Choose the reasoning effort by the depth of the investigation. A short answer
can still require following several evidence threads and checking them against
each other. The following settings are available where the Codex host supports
them. [Prompting GPT-6.2 in Codex](https://learn.chatgpt.com/guides/prompting-gpt-6-2-astra)

| Effort | Engineering use |
| --- | --- |
| Medium | Survey a bounded brief or check a well-specified record. |
| High | Trace a suspected timing discrepancy through several interfaces, configurations, and tests. |
| Extra High | Investigate several interacting explanations and test the recommendation against the strongest alternatives. |
| Ultra | Take on an unusually broad investigation with several independent questions. Codex decides when to use subagents in this mode. |

For work that splits cleanly, ask Codex to use subagents as needed and say what
you want reconciled before handoff. For visuals, supply the reference and the
intended viewing size or interactive action when those affect acceptance.

## Upgrade a model

1. Fetch official guidance for the exact candidate model and verify availability,
   tool support, output contracts, and supported settings in the intended host.
2. Change only the relevant profile and documented invocation. Preserve a baseline
   revision and record the candidate revision, settings, tools, and sources.
3. Run the same task cases with baseline and candidate, withholding reviewer
   rubrics from the producing model. Use [the evaluation protocol](evaluation.md).
4. Review failures and total task quality, evidence accuracy, latency, and cost.
   Update a skill only for observed needs; retain or revert the profile if the
   candidate does not meet the workload's acceptance conditions.

No promised capability of a future model is part of a skill's contract.
