# Archived migration notices

These six files formerly occupied the repository's root `agents/` and `skills/`
directories. They are historical notices, not installable agents or skills.
They were moved here to keep host discovery from treating notices as working
packages. Their contents are preserved unchanged; relative links inside them
refer to their former locations and are not maintained archive navigation.

[The manifest](manifest.json) records former paths, archived paths, content hashes,
and the source checkout's HEAD. Git retains the earlier file history. The founder
notice includes the in-progress expansion's archival pointer; the original
founder skill itself is separately preserved in
[the skill archive](../skills/defense-founder-review/README.md).

Use [the current migration guide](../../migration.md) for installation and
replacement choices. Canonical packages live in `.agents/skills` at the
repository root and are selected by `catalog.json`.
