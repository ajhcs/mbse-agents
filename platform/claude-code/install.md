# Claude Code

Build a fresh plugin directory from this checkout:

```sh
python3 scripts/package_plugin.py --output build/claude-local
claude plugin validate ./build/claude-local
claude --plugin-dir ./build/claude-local
```

Use `py` instead of `python3` on Windows. The build includes
`.claude-plugin/plugin.json`, `skills/`, references, and licenses. In the new
Claude Code session, invoke a packaged skill by its plugin-qualified command:

```text
/mbse-agents:mbse-requirements
```

Supply the engineering brief and desired artifact with the request. Keep existing
project instructions and host settings. For ongoing installation and updates,
use Claude Code's marketplace/plugin controls after the local trial works.

The local package tests verify files and manifests. Claude Code is not installed
on the validation host, so its validator and native skill activation have not been
executed here. See the [support matrix](../support.md).

Official sources checked 2026-11-13:
[plugin layout and validation](https://code.claude.com/docs/en/plugins-reference)
and [local loading and skill commands](https://code.claude.com/docs/en/plugins).
