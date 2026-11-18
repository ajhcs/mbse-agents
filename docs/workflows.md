# Work through a systems engineering question

Start with the system, the decision or artifact you need, and what you will
look for in review. State the scope where you need complete coverage. Use
`mbse-systems-engineering` for a problem that spans tasks or disciplines.
Use a focused skill directly when the work is clear. Add a domain skill when
its operating context or assurance basis changes the analysis.

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

For sustained work, keep decisions and assumptions with the baseline so a later
session can resume from the actual records. If parts can advance independently,
specify whether Codex can use subagents and the shared revision, interfaces, or
evidence you want checked before handoff. Set the depth by what could change the
decision and what coverage you need to review.

Record splits, merges, replacements, and retirements without recycling IDs or
silently inheriting evidence. A useful handoff identifies the source revision,
changed artifacts, decisive rationale, affected IDs, checks actually performed,
and unresolved decisions with owners. For optional record shapes and an
illustrative connected thread, see the core skill's
[engineering records](../.agents/skills/mbse-systems-engineering/references/engineering-records.md)
and [connected work](../.agents/skills/mbse-systems-engineering/references/connected-work.md).

## Example requests

> Use $mbse-systems-engineering to check whether our staffing plan can support
> the recovery promised by the architecture. Walk through an outage on an
> unstaffed shift. Cite the conflicting assumptions and identify who owns the
> decision. Use subagents as needed to inspect the operating notes and interface
> records in parallel, then reconcile against the same baseline.

> Use $mbse-requirements and $mbse-architecture on our cold-storage alarm brief.
> Carry source IDs into measurable requirements and component allocations.
> Continue through verification planning and run the local reference-model checks.
> Deliver a linked baseline, executed evidence with its configuration, and open
> hardware validation work. Save reviewable artifacts in the project workspace.

> Use $mbse-architecture to update this interface view from the current model.
> Match the notation in the attached reference. Render the result at the width
> of our review slide, check that the exchange labels and directions are readable,
> and deliver the editable source with the rendered view.

See the [worked example](../examples/worked/cold-storage-alarm/README.md) and
[model setup](models.md). This repository supplies instructions and offline
maintenance tools. It does not supply an MBSE engine or certification authority.
