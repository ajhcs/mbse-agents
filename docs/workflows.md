# From a question to an engineering baseline

Start with the decision the user needs to make and the artifacts available.
Choose a task skill for the work, adding a domain skill when the domain changes
the analysis. Neither requires the full catalog to be loaded.

| User goal | Task skill | Useful input | Reviewable result |
| --- | --- | --- | --- |
| Explore a system idea | `mbse-system-concept` | Problem, desired outcome, constraints | Alternatives, boundaries, feasibility tests, recommendation |
| Explain how a system will be used | `mbse-conops` | Stakeholders, environment, mission | Operations concept, responsibilities, lifecycle, open decisions |
| Walk through an operation | `mbse-operational-scenarios` | Actors, trigger, context | Normal and exception flows, modes, exchanges, evaluation conditions |
| Establish a requirement baseline | `mbse-requirements` | Needs, scenarios, constraints | Identified requirements, rationale, source links, acceptance conditions |
| Allocate behavior to an architecture | `mbse-architecture` | Requirements, functions, interfaces | Alternatives, allocations, contracts, trade decisions, unresolved risks |
| Plan verification and evidence | `mbse-verification-evidence` | Baseline, risks, available methods | Procedures, criteria, configuration, trace, evidence gaps |
| Challenge a baseline or change | `mbse-baseline-review` | Artifacts and review decision | Located findings, impact, repair options, disposition |

For a full workflow, carry the same IDs and assumptions from needs through
requirements, functions, components, interfaces, verification, and evidence.
Feed architecture-derived requirements and test failures back into the earlier
artifacts. A diagram cannot close a verification gap. Verification asks whether
the specified requirements are met; validation asks whether the system serves
stakeholder needs in the intended use context.

For a small task, produce the relevant artifact directly. For sustained work,
maintain a brief decision and assumption log so a later session can continue
from the actual baseline. Ask about missing facts that could change the answer;
make labeled provisional assumptions for independent work. Scale artifact depth
to the decision, system risk, and user's chosen process.

Example request:

> Use $mbse-requirements and $mbse-architecture on our cold-storage alarm brief.
> Carry source IDs into measurable requirements and component allocations.
> Continue through verification planning and run the local reference-model checks.
> Deliver a linked baseline, executed evidence with its configuration, and open
> hardware validation work. Save reviewable artifacts in the project workspace.

See the [worked example](../examples/worked/cold-storage-alarm/README.md) and
[model setup](models.md). This repository supplies instructions and offline
maintenance tools. It does not supply an MBSE engine or certification authority.
