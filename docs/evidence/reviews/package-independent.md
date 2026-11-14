# Independent package and installer review

Reviewed the working changes against `b54b0b673eb80ea22bd6c4987955192b22332923`, including `AGENTS.md`, installer and builder code, focused tests, manifests, and platform documentation. No implementation files were edited. All test fixtures were confined to `.mbse-review`; no host installation, model call, or external write was performed.

## Confirmed findings, repaired and independently re-verified

No unresolved blocking finding remains in the reviewed installer/package changes. The line numbers in the two original findings below refer to the pre-repair builder; current publication logic is at `scripts/package_plugin.py:57-74` and `165-176`.

1. **P2: A ZIP created during a build is overwritten.** In the reviewed version, `scripts/package_plugin.py:142-145` publishes the archive with `Path.rename()` after the only existence check at lines 94-95. On POSIX this replaces an existing file. Reproduction: wrap `archive_package()` to call the original and then create the final archive path with sentinel bytes before returning. `build(..., make_zip=True)` succeeds and replaces the sentinel with ZIP bytes. Publication needs an exclusive no-clobber operation, with a collision surfaced to the caller.

2. **P2: ZIP publication failure deletes newly created local files in the exposed output folder.** In the reviewed version, `scripts/package_plugin.py:142-147` makes the folder visible, then on archive rename failure moves it back into the temporary directory. Cleanup removes it. Reproduction: make the archive rename hook write `output/local.txt` and then raise `OSError`. Both the output and local file disappear. Once a folder is exposed, preserve and report it on publication failure, or establish that removal cannot discard intervening local changes.

Original reproduction observations are recorded in `package-adversarial-results.json`. The package author replaced rename publication with exclusive directory creation and no-clobber file links, and now preserves/reports visible outputs on failure. Independent re-verification confirms that a late archive collision is refused without replacing its sentinel, an injected archive I/O failure preserves `local.txt` and reports the retained folder, and a late archive symlink collision preserves both link and referent. See `package-adversarial-results-final.json`, which also records SHA-256 hashes of the reviewed implementation and test files. A failed publication can leave a partial folder; this is explicitly documented and reported.

## Checks completed

- All 17 original focused tests passed, followed by all 20 tests after the publication fixes. Their top-level temporary directories were redirected into `.mbse-review` without modifying test or implementation files. See `package-focused-tests.log` and `package-focused-tests-final.log`.
- Six additional installer probes passed: source symlink refusal; target symlink refusal; backup-root symlink refusal; target modification during a batch with earlier-package rollback; local changes made during rollback retaining both the new target and old backup; and late uninstall failure restoring earlier removals. See `installer-adversarial-results.json`.
- Exported all 13 canonical skills to Databricks context and verified all 19 generated local links. Both source manifests match their generator. Root migration `skills/*/SKILL.md` files are now absent. See `package-layout-results.json`.
- `codex plugin marketplace add --help` confirms the documented local command exists. `claude` is absent on this host. No installation command was executed.

## Manifest and support claims

Current portable manifest fields, root `skills/` layout, inline `extensions.com.openai`, and optional compatibility overlay match the [OpenAI packaging documentation](https://developers.openai.com/plugins/build/plugins) and [Agent Plugins schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json), read on 2026-11-13. The Claude manifest and root skill layout match the [Claude manifest reference](https://code.claude.com/docs/en/plugins-reference). The Databricks user-skill path, `@` invocation, and task-scoped fallback are consistent with the [Genie Code skill documentation](https://docs.databricks.com/aws/en/genie-code/skills/). These are documentation and file-layout checks, not host activation or model-quality evidence.

The parent independently recorded native Codex source discovery; that evidence must remain distinct from invoking a skill and evaluating its engineering behavior. No unsupported native-activation claim was found in the reviewed platform docs.

## Non-blocking boundary

Installer fingerprints cover file bytes, not permission bits or empty directories. That behavior predates this change and is not a blocker for the current Markdown/YAML-only skills. If executable helpers are added, test updates that change only executable mode before relying on this fingerprint format.
