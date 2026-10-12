<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/images/logo-dark.svg">
  <img alt="MBSE Agents" src=".github/images/logo-light.svg" width="520">
</picture>

# Engineering skills for reviewable system decisions

MBSE Agents turns system questions into usable concepts, scenarios, requirements,
architectures, risk analyses, and verification/evidence plans. Its skills preserve
domain analysis and review questions while giving GPT-6.1 Sol and GPT-6 Astra
room to work. No persona claims, prescribed document size, or future-model promises.

The collection contains **13 skills: seven engineering tasks, five domains, and
one founder review**. The [generated catalog](docs/skills.md) is the inventory.
This is an instruction/resource library with offline maintenance tools; it is
not a running agent service or an MBSE modeling engine. Model quality has not
been comparatively evaluated for this release.

## Start with a task

Requires Python 3.10+ for the optional installer/checks; no packages or credentials.
Clone the repository, then either launch Codex here (the `.agents/skills` folders
are discoverable) or install selected packages into your own project:

```sh
git clone https://github.com/ajhcs/mbse-agents.git
cd mbse-agents
python scripts/install.py --list
python scripts/install.py --project /path/to/project --skill mbse-requirements --skill mbse-architecture --dry-run
python scripts/install.py --project /path/to/project --skill mbse-requirements --skill mbse-architecture
```

On Windows, replace `/path/to/project` with a quoted Windows path; use `py` if
that is your Python launcher. The installer never overwrites `AGENTS.md` or model
settings. Existing unmanaged or edited skills are preserved. Updates to unchanged
managed packages require `--update` and retain backups.

> Use $mbse-requirements and $mbse-architecture on our system brief. Develop
> measurable requirements, function/component allocations, interface contracts,
> and design rationale. Carry source IDs through the artifacts and identify the
> missing decisions that could change the design. Save a coherent reviewable draft.

Add a domain skill when domain context matters: `mbse-aerospace`, `mbse-defense`,
`mbse-automotive`, `mbse-medical-device`, or `mbse-electronic-systems`.
For operations, use the concept, ConOps, or scenario skills. For assurance work,
use verification/evidence or baseline review. See [task workflows](docs/workflows.md).

## Follow the evidence

The [cold-storage alarm walkthrough](examples/worked/cold-storage-alarm/README.md)
carries a stakeholder brief through requirements, architecture, procedures, and
actual local reference-model results. It demonstrates trace and evidence handling,
with hardware validation still open. The [domain gallery](examples/README.md)
retains 20 illustrative system baselines; their planned evidence is not executed
or accepted evidence. It is teaching material, not an approved design.

[Primary-source corrections](docs/sources.md) include the general infusion-pump
classification and the aerospace tool-qualification mapping. Exact licensed
standard clauses still need the program's applicable edition. Cole's formalized
chapter/lecture methods will be integrated after the actual source material is
supplied, with provenance.

## Install, maintain, and contribute

- [Codex](platform/codex/install.md), [ChatGPT](platform/chatgpt/install.md), and
  [portable hosts](platform/generic/install.md): installation and discovery.
- [Model choice and upgrades](docs/models.md): profiles that can change without
  rewriting the engineering contracts.
- [Evaluation](docs/evaluation.md): offline checks and separate behavioral review.
- [Crosswalks](docs/crosswalk-reference.md): proposed relationships and export checks.
- [Contributing](CONTRIBUTING.md): welcoming reports, features, and new skill/agent requests.

```sh
python scripts/catalog.py --write
python scripts/validate.py
python -m unittest discover -s tests
```

Skills do not supply tool authentication, authority approvals, or access to a live
model. Use available authorized tools or deliver a clearly labeled proposal.
Standards remain the property of their publishers; this project synthesizes
engineering guidance and does not reproduce their text. [MIT license](LICENSE).
