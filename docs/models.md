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
codex -m gpt-6.1-sol
codex -m gpt-6-astra
```

These commands are candidate examples. Check model availability and supported
settings in the actual account and host before use; a provider's API setting need
not match a host's interface. This project supplies no credentials and does not
silently change models, reasoning effort or spending limits.

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
