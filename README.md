<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/images/logo-dark.svg">
  <img alt="MBSE Agents" src=".github/images/logo-light.svg" width="520">
</picture>

# Systems engineering agents

MBSE Agents helps an AI assistant investigate systems, understand relationships,
explain engineering decisions, develop connected artifacts, and challenge claims
against their evidence. It supports work from early concepts through operations,
architecture, assurance and change review.

The agent combines a systems-engineering reasoning core with task and domain
skills. Use it to think through an unfamiliar problem, examine an existing
project, or produce the particular artifacts a decision requires. The
[skill catalog](docs/skills.md) describes the available entry points.

## Start with your system

Launch Codex in this checkout, or install selected skills into an existing
project. The local installer needs Python 3.10+ and no third-party packages or
credentials. Use `python3` on Linux/macOS or `py` on Windows.

```sh
git clone https://github.com/ajhcs/mbse-agents.git
cd mbse-agents
python3 scripts/install.py --list
python3 scripts/install.py --project /path/to/project --skill mbse-systems-engineering --skill mbse-requirements --skill mbse-architecture --dry-run
python3 scripts/install.py --project /path/to/project --skill mbse-systems-engineering --skill mbse-requirements --skill mbse-architecture
```

> Use $mbse-systems-engineering to explain why recovery takes longer than our
> operating plan allows. Trace the delay across the relevant interfaces and
> teams. Show which observations support each plausible cause and identify the
> next check that would distinguish the remaining causes.

Choose a focused task skill when the work is already clear. Domain skills cover
aerospace, defense, automotive, medical devices and electronic systems. The
[workflows guide](docs/workflows.md) explains how to combine them, and the
[first-use tutorial](docs/getting-started.md) supplies a brief and a complete
path to reviewing the result.

## Learn from engineering work

The [gallery](examples/README.md) connects domain baselines, executable teaching
models and historical project studies. The [historical cases](docs/historical-gallery.md)
emphasize projects from before 2015 and connect original source material to
retrospective questions about system boundaries, interfaces, decisions,
operations, organizations and evidence.

The [cold-storage alarm walkthrough](examples/worked/cold-storage-alarm/README.md)
connects stakeholder needs, requirements, architecture, procedures and saved
reference-model observations. [Domain simulation evidence](docs/simulation-evidence.md)
identifies the exact models and assumptions behind generated analyses. Each case
distinguishes original project evidence, new analysis, executed model results and
work that still needs physical or program evidence.

## Assess engineering judgment

The [benchmark and quiz system](docs/benchmark.md) assesses problem framing,
systems thinking, causal reasoning, evidence interpretation, technical judgment
and communication. Artifact tasks assess existing-project review and change
handling as well as drafting. Automatic quiz results and independently reviewed
reasoning are reported separately.

Use [the evaluation protocol](docs/evaluation.md) to compare a model alone with
the same model using the agent skills. Use observed performance on the target
tasks to judge whether a prompt change improves the work.

## Use the host that fits your work

[Codex](platform/codex/install.md), [Claude Code](platform/claude-code/install.md),
[Databricks](platform/databricks/install.md), [ChatGPT](platform/chatgpt/install.md),
and [portable hosts](platform/generic/install.md)
have distinct discovery and installation mechanisms. Guides identify documented
adaptations and the checks actually performed. [Plugin distribution](docs/SUBMISSIONS.md)
describes the generated portable package; the source checkout keeps its canonical
skills under `.agents/skills`. Portable plugin and Databricks archives are available
from [GitHub releases](https://github.com/ajhcs/mbse-agents/releases).

The installer preserves existing project instructions, host settings and local
skill edits. CSE provides optional executable engineering analysis and model
methods; Ingenium supports editable presentation. Available connectors determine
which live tools the host can use. See [model and tool crosswalks](docs/crosswalk-reference.md).

## Develop and verify

```sh
python3 scripts/catalog.py --write
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

[Model guidance](docs/models.md), [source checks](docs/sources.md), and
[contribution instructions](CONTRIBUTING.md) describe the maintained contracts.
The source is [MIT-licensed](LICENSE). Referenced standards and historical
materials remain under their publishers' terms.
