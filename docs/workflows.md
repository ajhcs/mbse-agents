# Work through a systems engineering question

Start with the question, the system, and the decision the user needs to make.
The result may be an explanation, a better question, a diagnosis, a comparison,
or an engineering baseline. Use `mbse-systems-engineering` for an open problem
or connected work that needs reasoning across tasks and disciplines. Use a
focused task directly when its purpose is already clear. Add a domain skill
when its operating context or assurance basis changes the analysis.

For an older prompt-based installation, use the [migration guide](migration.md)
to select current packages and preserve existing project instructions.

| User goal | Task skill | Useful input | Reviewable result |
| --- | --- | --- | --- |
| Understand a system or reason through a connected problem | `mbse-systems-engineering` | Question, observations, context, available sources | Explained system understanding, synthesis, recommendation, or consequential next question |
| Explore a system idea | `mbse-system-concept` | Problem, desired outcome, constraints | Alternatives, boundaries, feasibility tests, recommendation |
| Explain how a system will be used | `mbse-conops` | Stakeholders, environment, mission | Operations concept, responsibilities, lifecycle, open decisions |
| Walk through an operation | `mbse-operational-scenarios` | Actors, trigger, context | Normal and exception flows, modes, exchanges, evaluation conditions |
| Establish a requirement baseline | `mbse-requirements` | Needs, scenarios, constraints | Identified requirements, rationale, source links, acceptance conditions |
| Allocate behavior to an architecture | `mbse-architecture` | Requirements, functions, interfaces | Alternatives, allocations, contracts, trade decisions, unresolved risks |
| Plan verification and evidence | `mbse-verification-evidence` | Baseline, risks, available methods | Procedures, criteria, configuration, trace, evidence gaps |
| Challenge a baseline or change | `mbse-baseline-review` | Artifacts and review decision | Located findings, impact, repair options, disposition |

## Choose the work by its purpose

A concept asks which way of delivering the outcome is worth pursuing. A ConOps
asks how people and systems will operate together. A scenario follows a specific
trigger, sequence, exception, and outcome. They can inform each other, but a
request to explain one outage does not require all three documents.

Architecture work develops or explains how the system is organized and why its
interactions should produce the required behavior. Baseline review challenges
an existing argument or change. Verification/evidence work asks what an
observation can establish and what remains untested. An unclear requirement may
first need discussion of stakeholder intent before a polished replacement.

Domain choice follows applicability. Aerospace separates aircraft and space
program bases; defense includes mission, organizational, acquisition, and
sustainment constraints; automotive includes driver, vehicle, and field context;
medical-device work begins with intended use and clinical workflow; electronics
addresses the detailed physical and HW/SW assumptions. For a medical-device FPGA,
combine the device context with electronics when both affect the question. Do
not load every domain because a system contains software or a sensor.

## Connect sustained work

For a full workflow, carry the same IDs and assumptions from needs through
requirements, functions, components, interfaces, verification, and evidence.
Establish authoritative input paths/revisions and one shared baseline before
combining results. Reconcile specialist terminology, units, timing references,
operating conditions, and responsibilities. A domain contribution refines that
baseline; it does not create a separate version of the same requirements.
Feed architecture-derived requirements and test failures back into the earlier
artifacts. A diagram cannot close a verification gap. Verification asks whether
the specified requirements are met; validation asks whether the system serves
stakeholder needs in the intended use context.

For a small task, produce the relevant artifact directly. For sustained work,
maintain a brief decision and assumption log so a later session can continue
from the actual baseline. Ask about missing facts that could change the answer;
make labeled provisional assumptions for independent work. Scale artifact depth
to the decision, system risk, and user's chosen process.

Record splits, merges, replacements, and retirements without recycling IDs or
silently inheriting evidence. A useful handoff identifies the source revision,
changed artifacts, decisive rationale, affected IDs, checks actually performed,
and unresolved decisions with owners. For optional record shapes and an
illustrative connected thread, see the core skill's
[engineering records](../.agents/skills/mbse-systems-engineering/references/engineering-records.md)
and [connected work](../.agents/skills/mbse-systems-engineering/references/connected-work.md).

## Example requests

> Use $mbse-systems-engineering to explain why our proposed staffing and recovery
> concept conflicts with the architecture team's assumptions. Identify the
> decisions that need to change and give a recommendation grounded in the
> supplied operating notes. Keep the answer useful to both teams.

> Use $mbse-requirements and $mbse-architecture on our cold-storage alarm brief.
> Carry source IDs into measurable requirements and component allocations.
> Continue through verification planning and run the local reference-model checks.
> Deliver a linked baseline, executed evidence with its configuration, and open
> hardware validation work. Save reviewable artifacts in the project workspace.

See the [worked example](../examples/worked/cold-storage-alarm/README.md) and
[model setup](models.md). This repository supplies instructions and offline
maintenance tools. It does not supply an MBSE engine or certification authority.
