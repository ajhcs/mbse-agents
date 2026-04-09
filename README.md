<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/images/logo-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset=".github/images/logo-light.svg">
  <img alt="MBSE Agents" src=".github/images/logo-light.svg" width="520">
</picture>

<br/>

[![License: MIT](https://img.shields.io/github/license/ajhcs/mbse-agents?style=flat)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/ajhcs/mbse-agents?style=flat)](https://github.com/ajhcs/mbse-agents/stargazers)
![Agents](https://img.shields.io/badge/agents-5-blue?style=flat)
![Examples](https://img.shields.io/badge/examples-20-teal?style=flat)
![Standards](https://img.shields.io/badge/standards-30%2B-orange?style=flat)
![Platforms](https://img.shields.io/badge/platforms-7-green?style=flat)

Agent files that turn AI coding assistants into domain-expert principal systems engineers — standards knowledge at the clause level, artifact mapping across six MBSE tools, and reviewer attack surfaces built in.

## Why This Exists

**The Problem.** Ask a general-purpose AI about ARP4761A common-mode analysis or ISO 26262 ASIL decomposition and you get a Wikipedia summary. It knows the acronyms but not the clauses, not the tool mappings, and not what the DER/assessor actually challenges during review.

**The Solution.** Drop a domain agent file into your AI coding assistant. It becomes a principal systems engineer who has closed SSAs, survived DAES reviews, and shipped 510(k) submissions -- with opinions about what the reviewer will flag.

**Why MBSE Agents?**

| | MBSE Agents | Generic AI | No AI |
|:---|:---|:---|:---|
| Standards depth | Clause-level (e.g., ARP4761A Appendix L) | Summary-level | Your memory |
| Tool mapping | 6 MBSE tools, element-by-element | "Use a SysML tool" | Manual lookup |
| Reviewer prep | Attack surfaces per review gate | Generic checklists | Tribal knowledge |
| Setup time | 30 seconds | N/A | N/A |
| Cost | Free, MIT-licensed | Included with LLM | N/A |

## Quick Start

**Claude Code** (recommended):

```bash
# Install globally
mkdir -p ~/.claude/agents
cp agents/*.md ~/.claude/agents/

# Or install per-project
cp -r agents/ /path/to/your-project/.claude/agents/
```

Then invoke by name:

```
subagent_type="Aerospace Systems Engineer"
```

**Other platforms:** [Claude Desktop](platform/claude-desktop/install.md) | [Codex CLI](platform/codex/install.md) | [ChatGPT](platform/chatgpt/install.md) | [Cursor](platform/cursor/install.md) | [Aider](platform/aider/install.md) | [Generic](platform/generic/install.md)

## See It in Action

> *"I have a dual-channel flight control system and need to demonstrate independence for my PSSA. What common-mode failures should I analyze?"*

The Aerospace agent walks you through ARP4761A CMA methodology: zonal safety analysis for physical proximity, particular risks (lightning, HIRF, bird strike), common-cause failures across redundant channels, cascading failures through shared resources. It maps each analysis type to specific Arcadia model views and Cameo SysML elements. It tells you what the DER will look for at SOI #3.

That is not a generic AI answer. That is the answer from someone who has closed an SSA with 200+ failure conditions.

<details>
<summary><strong>More examples</strong></summary>

**Defense:** *"Map this system-of-systems architecture to DoDAF OV-5b and SV-1 views for the upcoming DAES review."* The agent produces viewpoint-specific guidance with DI-SESS deliverable mappings and DAES scrutiny points.

**Automotive:** *"Walk me through ASIL decomposition for a redundant braking system where the primary is ASIL D."* The agent explains Part 9 decomposition rules, freedom-from-interference arguments, and what the assessor will challenge.

**Medical Device:** *"My IEC 62304 Class C software has SOUP components. How do I handle SOUP risk management for my FDA submission?"* The agent distinguishes IEC 62304 SOUP requirements from FDA expectations on OTS software, maps the risk controls to ISO 14971 artifacts, and identifies the documentation gaps that trip up premarket inspections.

</details>

## Agents

| Agent | Domain | Key Standards | Lines |
|:------|:-------|:--------------|------:|
| [Aerospace Systems Engineer](agents/aerospace-systems-engineer.md) | Civil aviation, space | ARP4754A, ARP4761A, DO-178C/DO-254, DO-326A/DO-356A, DO-330/DO-331 | 673 |
| [Defense Systems Engineer](agents/defense-systems-engineer.md) | DoD acquisition | DoDAF/UAF, MIL-STD-882E, DI-SESS, JCIDS | 674 |
| [Automotive Systems Engineer](agents/automotive-systems-engineer.md) | ADAS, powertrain | ISO 26262, ISO 21434, ISO 21448 (SOTIF), AUTOSAR | 653 |
| [Medical Device Systems Engineer](agents/medical-device-systems-engineer.md) | Class II/III, SaMD | IEC 62304, ISO 14971, FDA QMSR, EU MDR 2017/745 | 687 |
| [Electronic Systems Engineer](agents/electronic-systems-engineer.md) | ASIC, FPGA, SoC, quantum | DO-254, IEC 61508, IEEE 1800/1076, AEC-Q100 | 604 |

Each agent includes multi-tool crosswalk tables, reviewer attack surfaces, workflow guidance, and deliverable templates. 3,291 lines total.

## Example Systems

Each agent is grounded in reference architectures with real artifact structure — requirements, architecture decomposition, hazard analysis, traceability matrices, and assurance evidence packages.

| Domain | Flagship (full traceability) | Fleet Systems |
|:-------|:-----------------------------|:--------------|
| Aerospace | [Integrated FMS](examples/aerospace/flight-management-system/) | CubeSat constellation, EVA suit life support, launch vehicle avionics |
| Defense | [UAS Ground Control Station](examples/defense/uas-ground-control-station/) | Ballistic missile defense, tactical SDR radio, naval combat management |
| Automotive | [Autonomous Emergency Braking](examples/automotive/autonomous-emergency-braking/) | EV battery management, steer-by-wire, V2X communication |
| Medical Device | [Smart Infusion Pump](examples/medical-device/smart-infusion-pump/) | Surgical robot, continuous glucose monitor, patient monitoring network |
| Electronic Systems | [Quantum Processor Control](examples/electronic-systems/quantum-processor-control/) | Safety-critical SoC, FPGA radar signal processor, HPC cluster |

5 flagships with end-to-end traceability: requirements, architecture, hazard analysis, traceability matrices, assurance evidence, and cybersecurity analysis where applicable. 15 fleet systems with requirements and architecture artifacts.

Full gallery: [examples/](examples/)

## Supported MBSE Tools

The crosswalk tables in each agent map domain artifacts to model elements across:

| Tool | Vendor | Coverage |
|:-----|:-------|:---------|
| Capella | Eclipse / Thales | Arcadia phases, element types, checkpoints |
| Cameo Systems Modeler / CATIA Magic | Dassault | SysML elements, profiles, stereotypes |
| IBM Rhapsody | IBM | SysML/UML elements, model structure |
| Sparx Enterprise Architect | Sparx | SysML/UML/UAF elements, MDG profiles |
| DOORS / DOORS Next | IBM | ReqIF, OSLC, requirements structure |
| MATLAB / Simulink | MathWorks | FMU/FMI, analysis model integration |

Full crosswalk reference: [docs/crosswalk-reference.md](docs/crosswalk-reference.md)

## Ecosystem

### Companion: Cameo MCP Bridge

Pair these agents with **[cameo-mcp-bridge](https://github.com/ajhcs/cameo-mcp-bridge)** — an MCP server that connects AI assistants to a running Cameo/CATIA Magic instance with 37 tools for querying, creating, and modifying SysML models.

The agents provide the domain knowledge. The MCP bridge provides the tool access. Together: an AI that knows ARP4754A at the clause level **and** can modify your Cameo model directly.

### MCP Servers for Systems Engineers

These MCP servers complement MBSE Agents across the SE toolchain. Sorted by relevance to MBSE practitioners.

**MBSE & Modeling Tools:**

| Server | Connects To | Maintainer | Status |
|:-------|:------------|:-----------|:-------|
| [cameo-mcp-bridge](https://github.com/ajhcs/cameo-mcp-bridge) | Cameo / CATIA Magic | AJHCS | Active — 37 tools |
| [SysML v2 API MCP](https://github.com/redsteve/SysML-v2-API-MCP-Server) | SysML v2 repositories | Community | Early-stage |
| [Sparx EA MCP](https://www.sparxsystems.jp/en/MCP/) | Sparx Enterprise Architect | Sparx Systems (official) | Production — vendor-backed |
| [IBM DOORS MCP](https://github.com/UnknowCao/IBM_Doors_MCP) | IBM DOORS (via DXL) | Community | Proof-of-concept |
| [Polarion MCP](https://github.com/peakflames/PolarionMcpServers) | Siemens Polarion ALM | Community | Active |

**Analysis & Simulation:**

| Server | Connects To | Maintainer | Status |
|:-------|:------------|:-----------|:-------|
| [MATLAB MCP](https://github.com/matlab/matlab-mcp-core-server) | MATLAB / Simulink | MathWorks (official) | Active |
| [CAD-MCP](https://github.com/daobataotie/CAD-MCP) | AutoCAD / GstarCAD / ZWCAD | Community | Active |

**ALM / PLM / Project Management:**

| Server | Connects To | Maintainer | Status |
|:-------|:------------|:-----------|:-------|
| [Atlassian MCP](https://github.com/sooperset/mcp-atlassian) | Jira, Confluence | Community | Active |
| [Azure DevOps MCP](https://github.com/microsoft/azure-devops-mcp) | Azure DevOps | Microsoft (official) | Active |
| [Teamcenter MCP](https://github.com/srgio-es/teamcenter-mcp-server) | Siemens Teamcenter PLM | Community | Early-stage |
| [GitHub MCP](https://github.com/github/github-mcp-server) | GitHub | GitHub (official) | Active |
| [IBM MCP Collection](https://github.com/IBM/mcp) | IBM products | IBM (official) | Active |

**Notable gaps** — no MCP server exists yet for: IBM Rhapsody, Eclipse Capella, PTC Windchill, ANSYS, ReqIF interchange, or OSLC. If you're building one, [open an issue](https://github.com/ajhcs/mbse-agents/issues) — we'll list it here.

## Also Included

**[Defense Founder Review](skills/defense-founder-review/SKILL.md)** — A strategic review skill for defense, autonomy, and dual-use ventures. Evaluates capability gaps, incumbent failure modes, vertical integration decisions, and prototype paths.

## About Contributions

> *About Contributions:* Please don't take this the wrong way, but I do not accept outside contributions for any of my projects. I simply don't have the mental bandwidth to review anything, and it's my name on the thing, so I'm responsible for any problems it causes; thus, the risk-reward is highly asymmetric from my perspective. I'd also have to worry about other "stakeholders," which seems unwise for tools I mostly make for myself for free. Feel free to submit issues, and even PRs if you want to illustrate a proposed fix, but know I won't merge them directly. Instead, I'll have Claude or Codex review submissions via `gh` and independently decide whether and how to address them. Bug reports in particular are welcome. Sorry if this offends, but I want to avoid wasted time and hurt feelings. I understand this isn't in sync with the prevailing open-source ethos that seeks community contributions, but it's the only way I can move at this velocity and keep my sanity.

## Standards Attribution

Standards referenced in these agents are the property of their respective standards bodies: SAE International (ARP4754A, ARP4761A), RTCA/EUROCAE (DO-178C, DO-254, DO-326A, DO-330, DO-331), ISO (26262, 21434, 21448, 14971, 13485), IEC (62304, 61508, 60601-1), IEEE (1800, 1076), and others. This project provides practitioner guidance and synthesis, not reproductions of copyrighted standard text.

<details>
<summary><strong>Full disclaimer</strong></summary>

These agents are reference material for experienced systems engineering practitioners. They are not a substitute for reading the applicable standards, consulting with your program's designated engineering representative (DER/DAR/DA), or obtaining program-specific compliance guidance. Tool crosswalk mappings are illustrative based on publicly available tool documentation and are not endorsed by tool vendors. All content is derived from publicly available information. No export-controlled, classified, or proprietary content is included.

</details>

## License

[MIT](LICENSE)
