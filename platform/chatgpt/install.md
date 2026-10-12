# ChatGPT use

For the desktop app's standalone skills, select/create skills through the host's
supported interface or use its available skill installer on a canonical package
folder. For broader web/mobile distribution, follow the current plugin packaging
workflow; this repository does not claim a published plugin or universal ZIP import.
See [official authoring and distribution](https://learn.chatgpt.com/docs/build-skills).

For a manual experiment, provide the selected `SKILL.md` and its referenced files
as project/conversation context, state the engineering task, and request artifact
outputs. This is manual context loading, not automatic skill discovery. Keep
references alongside the entrypoint; uploading a migration notice is insufficient.

`gpt-manifest.json` is a generated adaptation index covering all shipped skills.
It is not an OpenAI plugin manifest and does not provision GPTs, tools, or access.
Use [the catalog](../../docs/skills.md) to select relevant packages. Choose the
available model in ChatGPT; installing instructions does not change it.
