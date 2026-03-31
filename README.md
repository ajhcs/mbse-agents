# MBSE Agents

Portable AI agents packed with practitioner-level systems engineering knowledge. Drop one into your AI coding assistant and get a principal SE who knows the standards at the clause level, maps artifacts across 7 MBSE tools, and has survived the reviews your program is heading into.

Four domain verticals. Six MBSE tools. Seven AI platforms. One source of truth per agent.

## Agents

| Agent | Domain | Key Standards | Lines |
|-------|--------|---------------|-------|
| [Aerospace Systems Engineer](agents/aerospace-systems-engineer.md) | Civil aviation, space | ARP4754A, ARP4761A, DO-178C/DO-254, DO-326A | 600+ |
| [Defense Systems Engineer](agents/defense-systems-engineer.md) | DoD acquisition | DoDAF/UAF, MIL-STD-882E, DI-SESS, JCIDS transition | 600+ |
| [Automotive Systems Engineer](agents/automotive-systems-engineer.md) | ADAS, powertrain | ISO 26262, ISO 21434, ISO 21448 (SOTIF), AUTOSAR | 600+ |
| [Medical Device Systems Engineer](agents/medical-device-systems-engineer.md) | Class II/III, SaMD | IEC 62304, ISO 14971, FDA QMSR, EU MDR 2017/745 | 600+ |

Each agent includes multi-tool crosswalk tables, reviewer attack surfaces, workflow guidance, and deliverable templates.

## Supported MBSE Tools

The crosswalk tables in each agent map domain artifacts to model elements across:

| Tool | Vendor | Coverage |
|------|--------|----------|
| Capella | Eclipse/Thales | Arcadia phases, element types, checkpoints |
| Cameo Systems Modeler / CATIA Magic | Dassault | SysML elements, profiles, stereotypes |
| IBM Rhapsody | IBM | SysML/UML elements, model structure |
| Sparx Enterprise Architect | Sparx | SysML/UML/UAF elements, MDG profiles |
| DOORS / DOORS Next | IBM | ReqIF, OSLC, requirements structure |
| MATLAB / Simulink | MathWorks | FMU/FMI, analysis model integration |

See [docs/crosswalk-reference.md](docs/crosswalk-reference.md) for all crosswalk tables in one place.

## Quick Start

**Claude Code** (recommended):

```bash
# Copy agents to your project
cp -r agents/ /path/to/your-project/agents/

# Or install globally
cp agents/*.md ~/.claude/agents/
```

Then invoke: `subagent_type="Aerospace Systems Engineer"`

**ChatGPT Custom GPT:**

1. Go to ChatGPT > Explore GPTs > Create
2. Paste the agent markdown (below the frontmatter `---`) as Instructions
3. Set GPT name and description from the frontmatter fields

See [platform/](platform/) for install guides for all 7 platforms: [Claude Code](platform/claude-code/install.md) | [Claude Desktop](platform/claude-desktop/install.md) | [Codex CLI](platform/codex/install.md) | [ChatGPT](platform/chatgpt/install.md) | [Cursor](platform/cursor/install.md) | [Aider](platform/aider/install.md) | [Generic](platform/generic/install.md)

## Example: What These Agents Actually Do

Ask the Aerospace agent:

> "I have a dual-channel flight control system and need to demonstrate independence for my PSSA. What common-mode failures should I analyze?"

The agent walks you through ARP4761A CMA methodology: zonal safety analysis for physical proximity, particular risks (lightning, HIRF, bird strike), common-cause failures across redundant channels, cascading failures through shared resources. It maps each analysis type to specific Arcadia model views and Cameo SysML elements. It tells you what the DER will look for at SOI #3.

That is not a generic AI answer. That is the answer from someone who has closed an SSA with 200+ failure conditions.

### More Examples

**Defense:** "Map this system-of-systems architecture to DoDAF OV-5b and SV-1 views for the upcoming DAES review." The agent produces viewpoint-specific guidance with DI-SESS deliverable mappings and DAES scrutiny points.

**Automotive:** "Walk me through ASIL decomposition for a redundant braking system where the primary is ASIL D." The agent explains Part 9 decomposition rules, freedom-from-interference arguments, and what the assessor will challenge.

**Medical Device:** "My IEC 62304 Class C software has SOUP components. How do I handle SOUP risk management for my FDA submission?" The agent distinguishes IEC 62304 SOUP requirements from FDA expectations on OTS software, maps the risk controls to ISO 14971 artifacts, and identifies the documentation gaps that trip up premarket inspections.

## Companion: Cameo MCP Bridge

For direct MBSE tool integration, pair these agents with [cameo-mcp-bridge](https://github.com/ajhcs/cameo-mcp-bridge), an MCP server that connects AI assistants to a running Cameo/CATIA Magic instance with 37 tools for querying, creating, and modifying SysML models.

The agents provide the domain knowledge. The MCP bridge provides the tool access. Together: an AI that knows ARP4754A at the clause level AND can modify your Cameo model directly.

## Also Included

**[Defense Founder Review](skills/defense-founder-review/SKILL.md)** -- A strategic review skill for defense, autonomy, and dual-use ventures. Evaluates capability gaps, incumbent failure modes, vertical integration decisions, and prototype paths. Not a persona. An operating system for reviewing defense product concepts.

## Standards Attribution

Standards referenced in these agents are the property of their respective standards bodies: SAE International (ARP4754A, ARP4761A), RTCA/EUROCAE (DO-178C, DO-254, DO-326A, DO-330, DO-331), ISO (26262, 21434, 14971, 13485), IEC (62304, 60601-1), IEEE, and others. This project provides practitioner guidance and synthesis, not reproductions of copyrighted standard text. Clause numbers, work product identifiers, and process descriptions reference publicly available standard metadata. Purchase standards from their respective publishers for authoritative text.

## Disclaimer

These agents are reference material for experienced systems engineering practitioners. They are not a substitute for reading the applicable standards, consulting with your program's designated engineering representative (DER/DAR/DA), or obtaining program-specific compliance guidance. Tool crosswalk mappings are illustrative based on publicly available tool documentation and are not endorsed by tool vendors. All content is derived from publicly available information. No export-controlled, classified, or proprietary content is included.

## Contributing

Domain experts welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add new agents, improve crosswalk tables, or report inaccuracies.

## License

[MIT](LICENSE)
