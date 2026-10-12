# Aerospace analysis and review

This reference preserves useful analysis topics from the former aerospace prompt. It is engineering guidance; normative details depend on the adopted edition and certification basis. Do not infer that a public source validates every clause of a licensed standard.

## Development assurance and safety

For civil aviation, establish the applicable regulations, aircraft or installation context, authority, means of compliance, and accepted development process. ARP4754-family development assurance and ARP4761-family safety work should inform each other as the architecture matures. Distinguish aircraft/function/item allocation and software/hardware assurance levels; their assignment needs a supported safety and development argument.

Relate failure conditions and operating phases to the proposed functions. Use functional hazard assessment, preliminary architecture safety analysis, and implementation safety assessment at the maturity appropriate to the task. FTA, FMEA, dependence modeling, and state-dependent analyses answer different questions; choose what the failure mechanism requires. Retain failure-rate provenance, exposure, independence assumptions, and uncertainty rather than manufacturing a quantitative target.

When redundancy or partitioning contributes to a safety argument, assess shared supplies, clocks, cooling, enclosure, environment, software/configuration, maintenance, and cascading failures. Keep common-cause analysis categories distinct: zonal analysis, particular-risk analysis, and common-mode analysis are related work, rather than interchangeable names for one analysis. Check exact terminology in the adopted ARP4761 edition. Architectural mitigation does not automatically lower every contributing item's assurance level.

Derived requirements and new hazards should flow back to the system and safety baseline. A historical PSSA against an obsolete allocation cannot support an implemented design without reconciliation.

## Software, hardware, models, and tools

DO-178C software evidence and DO-254 hardware evidence have different objectives and methods. Assess planning, requirements, design, implementation, verification, configuration, quality assurance, and authority liaison against the program's basis. Requirements-based coverage and structural coverage answer different questions. Do not substitute RTL line coverage for hardware requirement verification.

DO-331 is the model-based supplement to DO-178C/DO-278A, not a general DO-254 supplement. Assess how a model is used: specification, design, code generation, or verification. Track model standards, transformation configuration, model/code relationships, and relevant coverage. A drawing used only for communication does not automatically establish the same obligations as production code generation. [FAA AC 20-115D](https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-115D.pdf), paragraphs 6 and 10, provides the official recognition context.

Tool qualification is decided by tool use, potential impact, credit claimed, and checks on outputs. DO-178C section 12.2 supplies the decision framework; DO-330 supplies qualification objectives and lifecycle data. Criterion 3 can fail to detect an error in its intended use; it does **not** mean an output with no effect or automatic exemption.

FAA AC 20-115D, paragraph 10 and Table 2 (printed page 11), publishes the following correlation in its legacy-tool context:

| Software level | Criterion 1 | Criterion 2 | Criterion 3 |
| --- | --- | --- | --- |
| A | TQL-1 | TQL-4 | TQL-5 |
| B | TQL-2 | TQL-4 | TQL-5 |
| C | TQL-3 | TQL-5 | TQL-5 |
| D | TQL-4 | TQL-5 | TQL-5 |

Apply the licensed DO-178C Table 12-1 and actual qualification decision for a new use. A requirements repository, code generator, coverage analyzer, or equivalence checker is not assigned a criterion merely by its name. Explain which process is reduced or eliminated, how outputs are checked, and what faults could escape. Do not claim that this skill or a general language model is qualified.

## Security and space

Connect airborne security work to system safety, interfaces, assets, trust boundaries, threat assumptions, lifecycle updates, and verification. Consider adversarial inputs and dependencies alongside accidental failures. Establish the accepted security basis rather than assuming a generic penetration test closes it.

For space, identify mission class, human involvement, environment, lifetime, redundancy strategy, ground segment, launch dependencies, and NASA/ECSS or other applicable process. Examine radiation, fault management, command authorization, communications loss, thermal/power budgets, and recovery. Mission risk classes are not automatic equivalents to aircraft DALs. Tailoring belongs to the actual mission's authorized process.

## Artifact mappings and review questions

These are proposed relationships, not mandatory standard-to-tool equivalences:

| Engineering thread | Model content | Evidence or review focus |
| --- | --- | --- |
| Aircraft/mission need | Context, activities, scenarios | Intended use, certification/mission basis |
| Failure condition | Affected function, mode, dependence | Assumptions, severity and quantitative basis |
| Safety requirement | Identified requirement and allocation | Derived feedback and implemented control |
| HW/SW boundary | Interface and component allocation | Timing, coupling, reset, fault propagation |
| Model transformation | Source IDs and controlled export | Configuration, reconciliation, credit/qualification |
| Authority review | Baseline and evidence index | Actual review scope, maturity, open dispositions |

Adapt into Capella operational/system/logical/physical content or SysML requirements, activities, blocks, ports, and trace relationships in the project's profile. DOORS can hold the controlled requirement baseline; simulation can supply a scoped analysis artifact. Inspect integration and exports rather than assuming a diagram satisfies an assurance objective.

Review pressure points: unsupported independence; stale safety analysis; missing derived feedback; wrong tool criterion; unverified transformation; software/hardware objective conflation; security controls that disrupt safety behavior; simulation results presented as implementation evidence. Report concrete locations and affected IDs.
