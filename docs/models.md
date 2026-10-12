# Choosing and upgrading a model

The skills are authored for GPT-6.1 Sol and GPT-6 Astra, using the same engineering
contracts. No comparative model evaluation has been run for this release.
OpenAI describes Sol as a balance of speed, cost, and intelligence, and Astra
as the choice for demanding reasoning. Use Sol as a practical starting point;
consider Astra for difficult cross-domain tradeoffs or unresolved review findings.
This routing is a project recommendation to evaluate, not a measured advantage.
See the [official GPT-6 guide](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra).

`config/model-profiles.json` records editable model IDs and documentation links.
It is informational; installing a skill does not change the host's model setting.
Choose a model and supported reasoning setting in your host. For Codex CLI,
explicit selection looks like:

```sh
codex -m gpt-6.1-sol
codex -m gpt-6-astra
```

Check the models available to your account and the current CLI documentation.
The documented API limitation is that these two models do not support `none`
reasoning effort. This project deliberately has no API runner, credentials, or
hardcoded budget defaults.

The [Astra skill guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
informs our authoring choices: precise discovery descriptions, task-specific
references, fewer repeated instructions, and completion boundaries tied to the
requested result. Keep local assumptions and engineering evidence visible while
giving the model room to choose methods. Do not require every skill or every
reference for every request.

To upgrade:

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
