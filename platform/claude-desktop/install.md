# Claude Desktop Install Guide

## Option A: Project Knowledge (Simple)

1. Open Claude Desktop and start a new project.
2. Click the project settings icon and select **Add Content**.
3. Upload each agent file from `agents/`:
   - `aerospace-systems-engineer.md`
   - `defense-systems-engineer.md`
   - `automotive-systems-engineer.md`
   - `medical-device-systems-engineer.md`
4. Optionally upload `skills/defense-founder-review/SKILL.md` for defense review capability.

Claude Desktop will use these as project knowledge in every conversation within that project.

## Option B: MCP Filesystem Server

For dynamic access without re-uploading after updates:

1. Install the filesystem MCP server in Claude Desktop settings:

```json
{
  "mcpServers": {
    "mbse-agents": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/path/to/your-project/agents"
      ]
    }
  }
}
```

2. Replace `/path/to/your-project/agents` with the absolute path to your `agents/` directory.

3. Restart Claude Desktop. The agent files will be available as MCP resources.

## Usage

Reference agents by name in your prompts:

> "Act as the Aerospace Systems Engineer and review this requirements document against ARP4754A."

> "As the Defense Systems Engineer, map this system to DoDAF OV-1 and SV-1 views."

The frontmatter in each agent file contains the agent's name, description, and domain context.
