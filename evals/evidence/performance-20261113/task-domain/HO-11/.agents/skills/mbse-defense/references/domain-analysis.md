# Defense analysis and review

This reference is engineering guidance, not a substitute for the current contract, directives, or adopted standards. Acquisition frameworks, requirements governance, data item descriptions, and acceptance authorities change; verify the actual program documents instead of assuming a repository-wide date or policy transition.

## Mission and architecture

Start with the operational mission, stakeholder roles, environment, constraints, effects desired, and measurable success. Follow a mission thread across systems and organizations, including degraded resources, contested communications, handovers, maintenance, and recovery. Name dependencies outside the contractor's or system's control.

Choose DoDAF/UAF views for the decision they support. DoDAF is data-centric: a viewpoint presentation should be consistent with its underlying activities, performers, resources, exchanges, and relationships. Maintain a shared vocabulary and IDs. Do not manufacture a full viewpoint catalog for a focused acquisition question.

Useful DoDAF choices include OV-1 for context; OV-5b for operational activities; OV-6c for event traces; SV-1 for system interfaces; SV-4 for system functionality; and SV-5a for operational-activity/system-function trace. **SV-5a is not a generic requirements-allocation matrix.** Keep requirements-to-function and function-to-component allocation separately identifiable. Verify view definitions in the [official DoDAF material](https://dodcio.defense.gov/Library/DoD-Architecture-Framework/).

For UAF, retain domain concepts rather than assuming each stereotype maps one-to-one to a DoDAF view. When exchanging data, establish metamodel/profile version, relation semantics, identifier policy, and export reconciliation. Fit-for-purpose viewpoints are useful only if they answer the program's question from consistent underlying data.

## Technical baselines and contract obligations

Distinguish the functional, allocated, and product baseline and the authority controlling each. A review such as SRR, SFR, PDR, CDR, TRR, FCA, or PCA is a decision at a particular maturity, not an automatic schedule milestone. Identify entry conditions, decision criteria, unresolved issues, and controlled records for the actual program.

Treat CDRLs and data item descriptions as contractual inputs. Fetch the exact revision, tailoring, and deliverable requirements from the contract and [ASSIST](https://quicksearch.dla.mil/). Do not infer that a similarly named DID has the same scope or require every standard task on every program. A SEMP describes the engineering approach and management; a system design description records the design. Check the exact required data item before asserting its number or content.

For a change, trace mission need and capability requirement into system requirements, architecture, interface agreements, hazard controls, verification, and accepted evidence. Capture approval authority, affected baseline, configuration, and impact. Reused test evidence requires an applicability argument.

Legacy ICD/CDD/CPD, KPP, and KSA vocabulary can remain in active program artifacts. Establish which records are actually authoritative and what supersedes them. Avoid unsupported assertions that a governance transition cancels a program's baselined obligations.

## Safety and lifecycle assurance

MIL-STD-882-family system safety should connect hazards to design and operational decisions. Use the adopted revision and tasks. Keep hazard, causal factors, mishap, initial risk, control, residual risk, verification, and acceptance record distinct. Choose PHL/PHA, subsystem/system hazard analysis, operating/support analysis, or health hazard assessment for the relevant scope.

Account for operation, transport, maintenance, training, disposal, and interfaces to other systems. A design control can introduce a new maintenance exposure. Software-intensive hazard analysis needs credible causal mechanisms and software contribution analysis; unsupported random software failure probabilities do not establish safety.

Read severity definitions, probability categories, risk matrix, and acceptance authorities from the adopted process. Do not reuse a guessed matrix or equate a project manager's signoff with required risk acceptance. Hazard tracking links support the process but do not close the hazard without verified controls and authorized residual-risk disposition.

## Integration, support, and review

Inspect interoperability beyond protocol names: message meaning, units, freshness, time base, authentication, ownership, latency, failure response, and version compatibility. Include support equipment, training, spare parts, supply dependencies, deployability, and software updates where they affect mission availability.

| Engineering thread | Proposed architecture content | Reviewable evidence |
| --- | --- | --- |
| Mission outcome | Context, activity/event thread | Scenario and success measure |
| Operational exchange | Performer/resource/interface | Semantic and timing contract |
| System function | SV-4 or functional decomposition | Requirement allocation |
| Operational/system trace | SV-5a relation | Activity-to-function rationale |
| Hazard control | Function, component, support action | Verification and residual-risk record |
| Technical review | Baseline and decision log | Maturity and issue disposition |

Use Capella for operational/functional/physical decomposition; use the chosen SysML/UAF profile for the corresponding concepts; use requirement and analysis tools as controlled linked sources. These mappings are proposed practice, not an interchange certification.

Review pressure points: a view disconnected from data; missing mission-thread links; interface disagreement; misused SV-5a; unjustified risk acceptance; stale contract basis; unaddressed maintenance hazards; manufacturing/sustainment assumptions concealed by an attractive architecture.
