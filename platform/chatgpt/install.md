# ChatGPT use

Build the portable package with the [plugin build guide](../plugin/install.md).
Use the plugin import or local marketplace workflow available to your account.
The builder prepares files; it does not publish or install them. Local package
validation has run, but ChatGPT account/workspace import has not been exercised.
See the [support matrix](../support.md) and
[official packaging workflow](https://developers.openai.com/plugins/build/plugins).

For a manual experiment, provide the selected `SKILL.md` and its referenced files
as project/conversation context, state the engineering task, and request artifact
outputs. This is manual context loading, not automatic skill discovery. Keep
references alongside the entrypoint; uploading a migration notice is insufficient.

`gpt-manifest.json` is a generated adaptation index covering all shipped skills.
The built package's root `plugin.json` is the native portable manifest; the
adaptation index does not provision GPTs, tools, or access.
Use [the catalog](../../docs/skills.md) to select relevant packages. Choose the
available model in ChatGPT; installing instructions does not change it.
