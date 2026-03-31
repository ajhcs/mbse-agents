# MBSE Crosswalk Reference

> Last synced from agent files: 2026-03-31. For the latest crosswalk data, check the individual agent files in `agents/`.

Crosswalk tables mapping domain standards and artifacts to MBSE model elements across 6 tools: Capella, Cameo/CATIA Magic, IBM Rhapsody, Sparx Enterprise Architect, DOORS/DOORS Next, and MATLAB/Simulink.

---

## Aerospace (ARP4754A / DO-178C / DO-326A)

### ARP4754A/ARP4761A Phases to Arcadia and Multi-Tool Mapping

| Phase | Arcadia | Capella | Cameo/MagicDraw | Sparx EA | Rhapsody | DOORS | MATLAB/Simulink |
|---|---|---|---|---|---|---|---|
| **OA** | Operational Capabilities, Activities, Interactions | OAB, OAIB, OCB | Use Case Diagrams, Activity Diagrams (operational context), BDD (stakeholder model) | Use Case Diagrams, Activity Diagrams, Requirements Diagrams | Use Case Diagrams, Activity Diagrams, Sequence Diagrams | Operational requirements module, FHA linkage attributes | Operational scenario scripts, Requirements Toolbox |
| **SA** | System Functions, Functional Chains, Data Flows | SAB, SFCD, SDFB | BDD (system structure), IBD (data flows), Parametric Diagrams (safety budgets) | Component Diagrams, Sequence Diagrams, SysML Requirement Diagrams with PSSA trace | OMD, Sequence Diagrams, Statechart Diagrams (system modes) | System requirements module, PSSA linkage attributes | Simulink system-level models, Stateflow mode logic |
| **LA** | Logical Components, Functions, Exchanges, Interfaces | LAB, LFBD, LCBD | IBD (logical decomposition), BDD (logical hierarchy), Activity Diagrams | Component Diagrams (logical), Composite Structure Diagrams, Allocation Tables | Structure Diagrams, OMD (logical decomposition), Sequence Diagrams | Derived requirements, DAL allocation attributes, CMA linkage | Subsystem reference models, interface blocks |
| **PA** | Physical Components, Functions, Links, Exchanges | PAB, PBD, Component Exchange Scenarios | BDD (physical), IBD (physical interfaces), Deployment Diagrams | Deployment Diagrams, Component Diagrams (physical), Node Diagrams | Deployment Diagrams, Structure Diagrams, Panel Diagrams | Verification linkage (test-to-req-to-component), SSA closure records | HIL models, Embedded Coder targets, test harnesses |

**Usage notes**:
- OA maps to FHA initiation -- operational scenarios drive failure condition identification at the aircraft level
- SA maps to PSSA input -- system functions carry the safety requirement allocation from aircraft-level failure conditions
- LA maps to CMA and DAL allocation -- logical partitioning and independence arguments live here, and this is where the architecture makes or breaks the safety case
- PA maps to SSA evidence -- physical architecture carries the verification linkage and the as-built configuration that the authority audits
- Transitions between phases must preserve traceability -- a system function in SA must trace to one or more logical components in LA, which must trace to physical components in PA
- The crosswalk is bidirectional -- changes in PA (e.g., a supplier substitution) must propagate back through LA and SA to verify safety assessment validity

### DO-178C/DO-254/DO-331 Data Items to Model Artifacts

| Data Item | Capella | Cameo/MagicDraw | Sparx EA | Rhapsody | DOORS | MATLAB/Simulink |
|---|---|---|---|---|---|---|
| **PSAC/PHAC** | External doc; traces to planned baseline | External doc; Package structure mirrors plan | External doc; project config references EA packages | External doc; project references mirror plan | Formal module; traces to requirement modules | External doc; Project references config |
| **SRS/HRS** | Requirements linked to functions via ReqIF | Requirement Diagrams with DAL/verification attributes | Requirement elements with tagged values and trace | Requirement elements linked to use cases/design | Native modules with type/DAL/verification/allocation attributes; ReqIF/OSLC exchange | Requirements Toolbox specs linked to blocks |
| **SDD/HDD** | LAB/PAB hierarchy and exchanges | IBD, State Machines, Activity Diagrams | Component and Composite Structure Diagrams | OMD, Statecharts, Sequence Diagrams at design level | Design linkage attributes to tool-specific elements | Subsystem hierarchy, signal routing, Stateflow |
| **SVP/HVP** | External doc; test refs trace to requirements | Verification-stereotyped requirements with status | Test Cases linked via Verify relationship | Test Cases linked via dependencies | Verification modules with pass/fail and bidirectional trace | Test Manager suites, test harness specs |
| **SVCP/HVCP** | External; trace via requirement ID | Test Case Diagrams, Parametric Diagrams | Test Suites with scripts and expected results | Test Cases with expected results and scripts | Test case modules with procedures and trace | Test cases (equivalence, back-to-back), assessment scripts |
| **SVR/HVR** | External; results reference model element IDs | Status attributes on requirements; Cameo Analyzer dashboards | Test Run results linked to Cases and Requirements | TestConductor execution results | Result attributes on test objects; coverage matrices | Test Manager results, coverage reports (MC/DC) |
| **DO-331 Model Matrix** | Review records against modeling standards; .aird baselines | Checklists per MB.6.3/MB.6.4; CM via Teamwork Cloud | Review records; CM via project baselines or Git | Review per project standards; CM via Model Manager | N/A (requirements tool, not design model) | Model Advisor (MAB/JMAAB), Simulink Projects CM, code gen verification |
| **DO-330 Tool Data** | TQP: Capella version, plugins, export transforms | TQP: Cameo version, profiles, Teamwork Cloud, scripts | TQP: EA version, add-ins, automation scripts | TQP: Rhapsody version, profiles, code generators | TQP: DOORS version, DXL scripts, integrations | TQP: Embedded Coder, Simulink Coverage, Polyspace |

### Certification Review Gates to Model Maturity

| Gate | Maturity Expectation | Capella | Cameo/MagicDraw | Sparx EA | DOORS |
|---|---|---|---|---|---|
| **SOI #1 / Stage 1** | Architecture concept, dev environment, model standards documented | OAB and initial SAB; modeling standards doc | System context diagrams, initial use case model; standards in wiki | Initial use case/context models; project structure | Module structure defined; attribute schemas configured; integration planned |
| **SOI #2 / Stage 2** | Requirements baselined, architecture defined, FHA/PSSA traceable, DAL allocated | SAB/LAB complete; functional chains validated; ReqIF to DOORS; FHA/PSSA visible | BDD/IBD for system and logical arch complete; traceability matrix; PSSA-linked reqs | System/logical architecture complete; traceability matrix; FHA/PSSA tagged values | Requirements baselined (frozen version); bidirectional trace established; FHA/PSSA attributes populated |
| **SOI #3 / Stage 3** | Design final, verification evidence traced, SSA inputs available, compliance populated | PAB complete; physical-to-logical trace; verification linkage to test refs | Physical architecture complete; verification status populated; SSA data exported | Physical deployment models; test results linked; compliance matrix populated | Verification results captured; coverage complete; all reqs traced to test results |
| **SOI #4 / Stage 4** | Findings closed, compliance summary complete, config index final, as-built reflected | Final baseline tagged; all issues resolved; export matches compliance summary | Final Teamwork Cloud baseline; freeze applied; dashboard at 100% | Final baseline created; relationships verified; compliance report generated | Final baselines frozen; all attributes verified; compliance summary generated; archive created |

### Airworthiness Security (DO-326A) to Arcadia Views

| Security Element | Arcadia OA | Arcadia SA | Arcadia LA | DO-326A Artifact |
|---|---|---|---|---|
| **Assets** | Operational entities/exchanges carrying security-relevant data | System functions and exchanges identified as security-relevant | Logical components hosting security functions; trust boundaries | Asset Identification List |
| **Threat Agents** | Operational actors with adversarial intent in operational context | N/A (threats map to architecture, not functions directly) | N/A (threat agents are environment, not architecture) | Threat Assessment |
| **Attack Paths** | Operational scenarios showing adversary interaction | System functional chains showing access propagation | Logical exchange paths from external interface to target | Attack Tree / Attack Path Analysis |
| **Security Objectives** | Derived from operational environment and regulatory requirements | Security requirements allocated to system functions with safety reqs | Security requirements on logical components; interface constraints | Security Requirements (Section 5.3) |
| **Mitigations** | N/A (mitigations are design, not operational environment) | System-level controls (auth, encryption, monitoring) on functions | Logical components implementing controls; partitioning/isolation | Security Architecture Description |
| **Residual Risk** | Operational context for risk acceptance (mission phase, exposure) | Risk assessment at system function level | Risk assessment at logical component level with arch justification | Security Risk Assessment Report |

---

## Defense (DoDAF / MIL-STD-882E)

### DoDAF/UAF Viewpoints to Arcadia, SysML, and Tool Mapping

| DoDAF VP | UAF Equivalent | Arcadia | SysML (Cameo/MagicDraw) | Sparx EA | Rhapsody |
|---|---|---|---|---|---|
| **AV-1** | Metadata | Project scope doc | Package overview, stereotyped diagram | Project dashboard | Project browser overview |
| **AV-2** | Taxonomy | Glossary/term definitions in model | Data Dictionary package with stereotyped classes | Glossary element and tagged values | Glossary package |
| **OV-1** | Operational Concept | OAB (Operational Architecture Blank) | Use Case Diagram + rich-picture stereotype | Custom diagram with use case context | Use Case Diagrams with operational context |
| **OV-2** | Operational Connectivity | OAB with Operational Entities and Exchanges | IBD showing operational node interactions | Communication Diagrams between actors | OMD with operational node flows |
| **OV-3** | Resource Flow Matrix | Functional Exchange table export from OA | Allocation Matrix (op node to exchange) | Relationship Matrix (custom) | Table Layout diagram or matrix export |
| **OV-4** | Org Relationships | N/A (external doc) | BDD with organization stereotypes | Org Chart custom diagram | Class Diagram with org stereotypes |
| **OV-5a** | Activity Decomposition | Operational Activity hierarchy in OA | Activity Diagram (decomposition tree) | Activity Diagram hierarchy | Activity Diagram decomposition |
| **OV-5b** | Activity Model | OAIB (Operational Activity Interaction Blank) | Activity Diagram with swimlanes, object flows | Activity Diagrams with ICOM annotations | Activity Diagrams with flows |
| **OV-6a** | Rules Model | Operational constraints on activities | Constraint Blocks, OCL constraints | Constraint elements on activities | Constraint stereotypes on activities |
| **OV-6b** | State Transition | Mode/State machines in OA | State Machine Diagrams (operational context) | State Machine Diagrams | Statechart Diagrams |
| **OV-6c** | Event Trace | Operational Scenario diagrams in OA | Sequence Diagrams (operational lifelines) | Sequence Diagrams | Sequence Diagrams |
| **SV-1** | Resource Connectivity | SAB/LAB (System/Logical Architecture) | IBD showing system interconnections | Component Diagrams with interfaces | Structure Diagrams with ports |
| **SV-2** | Resource Flow | SAB/LAB with functional exchanges | IBD with flow ports and item flows | Component Diagrams with information flows | OMD with directed flows |
| **SV-3** | Systems Matrix | Exchange table export from SA/LA | Allocation/Dependency Matrix | Relationship Matrix | Matrix Layout export |
| **SV-4** | Function Description | System function hierarchy in SA | Activity Diagrams (system-level functions) | Activity Diagrams allocated to components | Activity Diagrams with function allocation |
| **SV-5a** | Activity-Function Map | Traceability from OA activities to SA functions | Allocation Matrix (activity to function) | Traceability Matrix (custom query) | Allocation table or matrix |
| **SV-5b** | Activity-System Map | Traceability from OA activities to SA components | Allocation Matrix (activity to block) | Traceability Matrix | Allocation table |
| **SV-6** | Resource Flow Matrix | Exchange detail table from SA/LA | Tagged values on item flows | Tagged values on information flows | Properties on flow connectors |
| **SV-7** | Measures Matrix | Performance constraints on SA functions | Parametric Diagrams with MOE/MOP | Requirements with performance attributes | Constraint blocks |
| **SV-8** | Evolution Description | N/A (program planning, external doc) | Package per increment with dependencies | Roadmap diagram or Gantt custom | Timeline or external doc |
| **SV-9** | Technology Forecast | N/A (external doc) | External doc linked via package | External doc with element links | External doc |
| **SV-10a** | System Rules | Constraints on system functions in SA | Constraint Blocks on system context | Constraint elements | Constraint stereotypes |
| **SV-10b** | System State Transition | Mode/State machines in SA/LA | State Machine Diagrams (system-level) | State Machine Diagrams | Statechart Diagrams |
| **SV-10c** | System Event Trace | System-level scenarios in SA/LA | Sequence Diagrams (system lifelines) | Sequence Diagrams | Sequence Diagrams |
| **CV-1** | Strategic Vision | N/A (external doc, traces to OA) | Package with strategic context | Custom diagram or external doc | External doc |
| **CV-2** | Capability Taxonomy | Capability hierarchy linked to OA activities | BDD with capability stereotypes | Package hierarchy with capability elements | Class Diagram with capability stereotypes |
| **DIV-1** | Conceptual Data | Data concepts in OA exchange definitions | BDD with data entity stereotypes | Class Diagrams (conceptual) | Class Diagrams (conceptual) |
| **DIV-2** | Logical Data | Data element detail in SA exchanges | BDD/IBD with typed attributes | Class Diagrams (logical, normalized) | Class Diagrams (logical) |
| **DIV-3** | Physical Data | Data format specs in PA exchange detail | BDD with physical data types, Deployment | Class Diagrams (physical, schema-level) | Class Diagrams (physical) |
| **StdV-1** | Standards Profile | Standards references linked to model elements | Stereotyped package with standard references | Tagged values referencing standards | Standard reference elements |
| **StdV-2** | Standards Forecast | N/A (external doc) | External doc linked to standards package | External doc | External doc |
| **PV-1** | Project Relationships | N/A (external doc) | BDD with project stereotypes | Custom diagram | External doc |
| **PV-2** | Project Timelines | N/A (external doc) | Timeline or Gantt custom diagram | Gantt or roadmap custom | External doc |

### DI-SESS/CDRL to Model-Generated Evidence per Tool

| DI-SESS DID | Content | Cameo/MagicDraw | Sparx EA | Capella | DOORS |
|---|---|---|---|---|---|
| **DI-SESS-81495 (SEMP)** | SE processes, org, tools, reviews | External doc; model structure mirrors SEMP sections | External doc; project config references EA packages | External doc; Capella project setup mirrors plan | External doc; module structure aligns to SEMP |
| **DI-SESS-81496 (System Spec)** | Performance, interface, design reqs | Requirement Diagrams + Spec tables exported from model | Requirement elements with spec attributes, HTML/DOCX export | ReqIF export from SA/LA requirements | Native modules; primary generation source for spec content |
| **DI-SESS-81497 (ICD)** | Interface definitions | IBD port/flow exports; interface tables from model | Component interface exports; tagged value tables | PAB component exchange tables; interface detail exports | Interface requirement modules with physical/logical attributes |
| **DI-SESS-81521 (Review Pkg)** | Review evidence, criteria, actions | Dashboard exports, traceability matrices, model reports | HTML reports, relationship matrices, custom templates | Model browser exports, traceability reports | Baseline snapshots, traceability reports, attribute summaries |

**Generation guidance**:
- DI-SESS-81495 (SEMP) is always narrative-dominant. The model informs it but does not generate it directly. Tool and process descriptions in the SEMP should reference model structure and CM practices.
- DI-SESS-81496 (System Spec) is the strongest candidate for model generation. Requirements with typed attributes, traceability, and verification mappings can be exported directly from the model. The export must match the DID format or carry an approved deviation.
- DI-SESS-81497 (ICD) benefits from model extraction but requires curation. Interface details must be complete, versioned, and agreed by both sides of the interface. Model export provides the technical content; the governance wrapper is manual.
- DI-SESS-81521 (Review Pkg) is assembled, not generated. Model exports provide evidence artifacts. The review package structure, entrance/exit criteria assessment, and action item tracking are typically manual or semi-automated.

### Technical Review Criteria to Model Completeness

| Review | Key Criteria | Model Completeness Check |
|---|---|---|
| **ASR** | AoA complete, concept selected, operational requirements validated | OV-1, OV-5b, OV-6c present and reviewed; CV-1/CV-2 linked to operational need; trade study rationale documented |
| **SRR** | System requirements complete, consistent, testable, traceable | System requirements baselined in model or DOORS; SV-5a traceability matrix complete; every OV-5b activity maps to at least one SV-4 function; requirement attributes include verification method |
| **SFR** | Functional architecture satisfies requirements, allocation complete | SA/SV-4 function hierarchy complete; functional allocation to subsystems traced; preliminary hazard analysis linked to functions; interface requirements identified |
| **PDR** | Preliminary design meets allocated baseline, interfaces defined | LA/SV-1 architecture complete; ICDs drafted (DI-SESS-81497); performance budgets allocated; safety analysis updated (SSHA); traceability from requirements through design elements |
| **CDR** | Detailed design complete, ready for build/code | PA complete; all interfaces specified; verification procedures drafted; safety analysis current (SHA); configuration items identified; traceability through to verification planning |
| **TRR** | Test readiness confirmed, procedures approved, environment qualified | Verification cross-reference matrix complete; test procedures linked to requirements; test environment configuration documented; discrepancy reports from development testing dispositioned |
| **FCA** | Performance verified against specification | All verification results captured and traced to requirements; discrepancy reports dispositioned; specification compliance demonstrated per CI |
| **PCA** | As-built matches documentation | Product baseline established; as-built configuration reflected in model; documentation matches delivered configuration; CI identification confirmed |

### MIL-STD-882E Hazard Artifacts to MBSE Elements

| Safety Artifact | MBSE Element | Tool Implementation |
|---|---|---|
| **Hazard** | Stereotyped requirement or custom element with severity/probability attributes | Cameo: Hazard stereotype on Requirement; Sparx: Hazard tagged value profile; Capella: custom property on SystemFunction; DOORS: Hazard module with severity/probability attributes |
| **Causal Factor** | Linked element tracing from hazard to architecture element that produces the causal condition | Cameo: Dependency from Hazard to Block/Activity; Sparx: Trace connector; Capella: traceability link to SA/LA function; DOORS: linked object in causal factor module |
| **Mishap Scenario** | Sequence or activity diagram showing the causal chain from initiating event through hazard to mishap | Cameo: Sequence Diagram with hazard lifeline; Sparx: Activity Diagram with hazard swimlane; Capella: Operational Scenario; DOORS: linked narrative in hazard module |
| **Control Measure** | Requirement allocated to the system function or component that implements the control | Cameo: Requirement with Satisfy relationship to design Block; Sparx: Requirement linked to Component; Capella: constraint on function; DOORS: requirement linked to design element |
| **Verification of Control** | Test case or analysis linked to the control requirement with pass/fail status | Cameo: TestCase with Verify relationship; Sparx: Test element linked to Requirement; Capella: external link; DOORS: verification module with trace to control requirement |
| **Residual Risk** | Risk assessment attribute on hazard element after controls are applied | Cameo: residual severity/probability tagged values; Sparx: risk assessment profile values; Capella: property values; DOORS: residual risk attributes on hazard object |

---

## Automotive (ISO 26262 / ISO 21434 / AUTOSAR)

### ISO 26262 Work Products to Model Elements

| Work Product (Part:Clause) | Arcadia | Cameo/MagicDraw (SysML) | AUTOSAR Tools | DOORS/Polarion | External |
|---|---|---|---|---|---|
| **Item Definition (3:5)** | OA: operational entities, actors, environment context | BDD: system context, actors, external interfaces | N/A (pre-architecture) | Stakeholder requirement module | Item definition document |
| **HARA (3:7)** | OA: operational situations, hazardous event annotations | Custom stereotype: HazardousEvent with S/E/C/ASIL attributes | N/A | HARA module with S/E/C/ASIL attributes per event | HARA worksheet |
| **Safety Goals (3:8)** | OA/SA: safety goal annotations on operational/system functions | Requirement stereotype: SafetyGoal with ASIL, safe state | N/A | Safety goal module, traced to HARA events | Part of FSC document |
| **FSC - FSRs (3:8)** | SA: system functions with FSR allocation, functional chains showing safe state transitions | Requirement Diagrams: FSRs traced to safety goals; Activity Diagrams: functional behavior | N/A | FSR module traced to safety goals | FSC document |
| **TSC - TSRs (4:7)** | LA: logical components with TSR allocation, interface constraints | IBD: allocation of TSRs to logical blocks; Parametric Diagrams for timing | AUTOSAR SWC requirements (ARXML) | TSR module traced to FSRs | TSC document |
| **HSRs (5:6)** | PA: physical components with HW safety attributes | BDD/IBD: hardware elements with SPFM/LFM attributes | ECU resource model | HW safety requirement module | Part 5 verification plan |
| **SSRs (6:6)** | PA: software deployment to physical nodes | SWC stereotypes with ASIL, data flow diagrams | SWC safety annotations in ARXML | SW safety requirement module | Part 6 verification plan |
| **Safety Analyses (9:7-8)** | Cross-view: FTA top events from SA, cut sets resolved to LA/PA elements | FTA/FMEA profiles linked to BDD/IBD elements | N/A (analysis tool: medini, Reliability Workbench) | Analysis linkage attributes on requirement/design modules | FMEA, FTA, FMEDA reports |
| **HW Metrics (5:8)** | PA: annotated failure rates on physical components | Parametric Diagrams: SPFM/LFM/PMHF calculation models | N/A (calculation tool) | Metric values stored as attributes | Part 5 metrics calculation report |
| **Verification Results (4:8, 5:9, 6:10)** | PA: verification linkage from requirements to test evidence | Verify relationships on requirements; test result status | N/A (test management tool) | Verification result attributes; coverage matrices | Test reports, coverage summaries |
| **Safety Case (2:6)** | Cross-view: model provides traceable evidence chain | GSN/SACM safety argument model | N/A | Module hierarchy mirrors safety case structure | Safety case compilation |

**Usage notes**:
- The HARA is rarely modeled natively in the architecture tool. Most programs maintain the HARA in a structured spreadsheet or dedicated safety tool (medini analyze, Ansys medini) and link to the architecture model via safety goal IDs traced to system functions in SA.
- Safety goals and FSRs map to the SA level because they are functional, not implementation-specific. TSRs map to LA because they carry implementation constraints (timing, diagnostic coverage) that drive logical component design.
- Hardware metrics (SPFM, LFM, PMHF) are calculated in dedicated reliability tools (Reliability Workbench, APIS IQ-FMEA, RAM Commander) and linked to the architecture model via component IDs. The architecture model carries the failure rate annotations; the calculation lives in the reliability tool.
- Verification results live in test management tools (DOORS, Polarion, codebeamer) and link to the model via requirement IDs. The model provides the traceability structure; the test tool provides the evidence content.
- The safety case itself is a compilation that references model-derived evidence. The model is not the safety case -- it is the structural backbone that organizes and traces the evidence.

### HARA to FSC to TSC Safety Flow

| Flow Step | Arcadia Representation | SysML (Cameo/MagicDraw) Representation | Traceability Mechanism |
|---|---|---|---|
| **Operational Situation** | OA: Operational Activity with scenario annotations | Activity Diagram: operational scenario with environment context | Scenario ID traced to HARA |
| **Hazardous Event** | OA: Hazardous event annotation on operational activity (S/E/C/ASIL) | HazardousEvent stereotype with S/E/C/ASIL tagged values | Unique HE-ID; HARA row reference |
| **Safety Goal** | SA: Safety goal constraint on system function | Requirement element (SafetyGoal) traced to HazardousEvent | SG-ID derive from HE-ID; bidirectional trace |
| **Functional Safety Requirement** | SA: Allocated requirement on system function; functional chain for safe state transition | Requirement Diagram: FSR satisfy SafetyGoal; Activity Diagram: functional behavior | FSR-ID traced to SG-ID; allocation to system function |
| **Technical Safety Requirement** | LA: Requirement allocated to logical component; interface constraint specification | IBD: TSR allocated to logical block; Parametric: timing/diagnostic constraints | TSR-ID traced to FSR-ID; allocated to logical component |
| **HW/SW Safety Requirement** | PA: Requirement allocated to physical component and deployed software | BDD: HSR/SSR on physical/SW elements; deployment allocation | HSR/SSR-ID traced to TSR-ID; allocated to physical element |
| **Verification Evidence** | PA: Test reference linked to requirement; verification status | Verify relationship: test case to requirement; pass/fail status | Test-ID traced to HSR/SSR-ID; bidirectional closure |

### AUTOSAR Architecture to Arcadia LA/PA and SysML Component Models

| AUTOSAR Element | Arcadia LA | Arcadia PA | SysML (Cameo) | Modeling Notes |
|---|---|---|---|---|
| **SWC (Application)** | Logical Component with functional allocation | Deployed to ECU node in PA | Component (SWC stereotype) with ports and interfaces | ASIL annotation on SWC; one logical component may map to multiple SWCs |
| **RTE** | Logical exchange mechanism (implicit) | Generated configuration on ECU node | Internal Block Diagram: flow ports and connectors | RTE is generated, not modeled as a design element; configuration correctness verified at integration |
| **BSW Module** | Not explicitly modeled (platform service) | ECU platform configuration | Component (BSW stereotype) or deployment annotation | Model BSW modules only when their configuration carries safety requirements (WdgM, E2E, OS scheduling) |
| **Communication (CAN/LIN)** | Logical exchange between components | Physical link in PA with bus attributes (baud rate, load, scheduling) | IBD: flow ports with CAN/LIN protocol attributes | Signal-to-PDU-to-frame mapping lives in AUTOSAR tooling; Arcadia/SysML captures the logical exchange |
| **Communication (Ethernet/SOME/IP)** | Logical service interface (ara::com pattern) | Physical Ethernet link with VLAN, priority, bandwidth | IBD: service ports with SOME/IP contract references | For Adaptive, model service contracts and discovery; deterministic Ethernet (TSN) adds timing constraints |
| **ECU** | N/A (logical view is ECU-agnostic) | Physical Node with processing, memory, I/O attributes | Node in Deployment Diagram with resource constraints | ECU resource constraints (CPU load, memory, I/O) drive feasibility of SWC deployment |
| **Composition** | Logical component hierarchy | Physical component hierarchy within ECU | Composite Structure Diagram: SWC composition tree | AUTOSAR composition hierarchy must match the logical decomposition in the architecture model |
| **E2E Protection** | Logical exchange with E2E annotation | E2E profile configuration per physical link | Stereotype on flow port or connector with E2E profile ID | E2E configuration (profile, data ID, counter) is safety-critical; mismatches cause undetected communication faults |
| **Execution Management** | Logical scheduling constraints | Process deployment on Adaptive platform node | Activity Diagram or State Machine for execution states | For Adaptive Platform: model process startup/shutdown order, resource supervision, deterministic execution |

**Usage notes**:
- The AUTOSAR-to-model mapping is not one-to-one. A single logical component in Arcadia LA may decompose into multiple AUTOSAR SWCs. The mapping rationale must be documented -- the assessor needs to verify that the safety requirement allocated to the logical component is fully covered by the SWCs it maps to.
- RTE and BSW are not modeled as design elements in the architecture model. They are platform configuration. However, when BSW modules carry safety requirements (WdgM alive supervision, E2E protection, OS timing protection), their configuration must be traceable to the TSRs that mandate them.
- The signal-to-PDU-to-frame mapping for CAN/LIN communication lives in the AUTOSAR tooling (e.g., Vector DaVinci, ETAS ISOLAR, EB tresos). The architecture model captures the logical exchange and its safety attributes (E2E profile, timeout, plausibility range). The detailed communication matrix lives in the AUTOSAR configuration database.
- For mixed Classic/Adaptive architectures, the model must show the gateway boundary between the Classic CAN/LIN domain and the Adaptive Ethernet domain, including the protocol translation and the safety/security controls at the gateway.

### Cybersecurity (ISO 21434) and SOTIF (ISO 21448) to Model Structures

| Analysis Element | Arcadia Representation | SysML (Cameo) Representation | Linked ISO Standard | Integration Notes |
|---|---|---|---|---|
| **Asset (21434)** | SA/LA: function or data exchange marked as security-relevant | Component or flow port with SecurityAsset stereotype | 21434 Clause 9 | Assets often overlap with safety-relevant elements; dual annotation required |
| **Threat Scenario (21434)** | OA: adversarial scenario on operational context | Misuse Case or custom ThreatScenario element | 21434 Clause 15 | Threat scenarios should reference the attack surface from the architecture, not generic threats |
| **Damage Scenario (21434)** | OA: impact annotation (safety, financial, operational, privacy) | Tagged values on ThreatScenario: impact ratings per category | 21434 Clause 15 | Safety impact must cross-reference the HARA; a damage scenario affecting a safety function creates an ISO 26262 interaction |
| **Attack Path (21434)** | LA/PA: exchange path from external interface to target asset | Attack Tree Diagram or annotated IBD showing traversal | 21434 Clause 15 | Attack paths through the architecture model verify that security controls are placed on the actual traversal path |
| **Cybersecurity Goal (21434)** | SA: security requirement on system function | Requirement (CybersecurityGoal stereotype) traced to threat/damage | 21434 Clause 15 | Cybersecurity goals that mitigate safety-relevant threats must trace to the safety concept |
| **Triggering Condition (21448)** | OA/SA: scenario annotation on operational activity or system function | Custom stereotype: TriggeringCondition with ODD relevance | 21448 Clause 6 | Triggering conditions link to the ODD definition and the validation strategy |
| **ODD Boundary (21448)** | OA: operational context constraints defining valid operating conditions | Constraint block or parametric diagram defining ODD parameters | 21448 Clause 5 | ODD parameters must be monitorable -- the system must detect when it approaches or exceeds the ODD boundary |
| **SOTIF Validation Scenario** | SA: functional scenario with triggering condition coverage | Test Case element traced to TriggeringCondition | 21448 Clause 10 | Validation evidence must demonstrate scenario coverage against the identified triggering conditions and the residual risk argument |
| **R155 CSMS Evidence** | Cross-view: process evidence referencing model-backed threat analysis | External document with model element references | UNECE R155 | CSMS evidence is organizational; the model provides the technical analysis that the CSMS process governs |
| **R156 SUMS Evidence** | PA: software version identification per ECU, update interface model | Deployment Diagram with version attributes; update channel model | UNECE R156 | Every ECU in the PA must carry a software identification; update paths must be modeled with authentication and rollback |

**Usage notes**:
- ISO 21434 TARA and ISO 26262 HARA are parallel analyses that must cross-reference where they overlap. A threat scenario that can cause a safety goal violation creates a cybersecurity goal with safety implications -- this must appear in both the cybersecurity case and the safety case.
- SOTIF triggering conditions are modeled differently from ISO 26262 failure modes. A triggering condition is not a fault -- it is a specification gap or environmental condition that causes the intended function to behave unsafely. The model must distinguish between these concepts to maintain clarity in the safety argumentation.
- R155 CSMS evidence is primarily organizational (process documentation, incident response plans, supply chain management). The model provides the technical analysis (TARA results, architecture-level controls) that the organizational process governs. The assessor evaluates the CSMS process; the model provides the technical substance.
- For ADAS functions using ML components, the ISO/PAS 8800 requirements for training data quality, model verification, and operational monitoring create additional model elements (training data lineage, model version tracking, performance monitoring architecture) that must be represented in the safety architecture.

---

## Medical Device (IEC 62304 / ISO 14971 / FDA)

### IEC 62304 Lifecycle Activities to Model Artifacts

| IEC 62304 Activity | Class | Capella | Cameo/MagicDraw | Sparx EA | DOORS | MATLAB/Simulink |
|---|---|---|---|---|---|---|
| **Software development planning** | A,B,C | Project config; lifecycle phase diagram | Package structure; profile config; planning stereotypes | Project structure; tagged values on planning packages | Module structure; attribute schemas; lifecycle attributes | Project config; model advisor checks |
| **Software requirements analysis** | A,B,C | System/Logical functions with req trace via ReqIF | Requirement Diagrams; BDD with interface blocks; traceability matrix | Requirement elements with trace to use cases; tagged values | Native requirement modules; attributes for safety class, risk trace, source | Requirements Toolbox; linked Simulink specs |
| **Software architectural design** | B,C | LAB/PAB hierarchy; component exchanges; interface definitions | IBD (logical decomposition); BDD (component hierarchy); Activity Diagrams | Component Diagrams; Composite Structure; allocation tables | Architecture linkage attributes to design tool elements | Subsystem reference models; signal routing |
| **Software detailed design** | C | Detailed PAB; state machines; internal exchanges | State Machine Diagrams; Activity Diagrams (algorithmic); sequence diagrams | Class Diagrams; State Machines; detailed component models | Detailed design linkage attributes | Stateflow charts; algorithm blocks; detailed models |
| **Software unit implementation** | C | External (IDE); traced to PAB elements | External (IDE); traced to design elements via stereotypes | External (IDE); linked via tagged values | Implementation linkage attributes; version references | Auto-generated code (Embedded Coder); manual code linked |
| **Software integration testing** | B,C | External test records; traced to LAB/PAB interfaces | Test Case Diagrams; verification-stereotyped elements | Test Suites linked via Verify relationships | Test modules with pass/fail; bidirectional trace to reqs | Integration test harnesses; back-to-back testing |
| **Software system testing** | B,C | External test records; traced to system requirements | Status attributes on requirements; test coverage dashboards | Test Run results linked to requirements | Verification result attributes; coverage matrices | System-level test suites; HIL test results |
| **Software release** | A,B,C | Baseline tag; export of release configuration | Teamwork Cloud baseline; freeze applied | Project baseline; release package generated | Frozen baseline; release attributes set | Project release; archived configuration |
| **Software maintenance** | A,B,C | Change records traced to impacted elements | Change request stereotypes; impact analysis via dependency | Change proposals linked to affected elements | Change control attributes; delta trace | Model comparison; regression test suites |
| **Software problem resolution** | A,B,C | Anomaly records linked to model elements | Problem report stereotypes with severity and disposition | Defect tracking linked to design/test elements | Anomaly modules with risk impact attributes | Bug tracking linked to model elements and tests |

### ISO 14971 Risk Artifacts to Model Elements

| ISO 14971 Artifact | Capella | Cameo/MagicDraw | Sparx EA | DOORS | Traceability Direction |
|---|---|---|---|---|---|
| **Intended use / user needs** | OA capabilities and actors | Use Case Diagrams; stakeholder BDD | Use Case Diagrams; stakeholder requirements | User needs module; intended use attributes | Forward to hazard identification |
| **Hazard identification** | Hazard elements linked to system functions | Hazard stereotypes on Block elements; custom profile | Hazard elements with tagged values; custom MDG | Risk module; hazard attributes with severity | Forward to hazardous situation |
| **Hazardous situation** | Scenario elements linking hazard to exposure | Activity Diagrams showing exposure path; sequence diagrams | Scenario elements; state machines showing exposure | Hazardous situation records linked to hazards and harms | Bidirectional: hazard + sequence of events |
| **Sequence of events** | Functional chains from cause through failure to exposure | Activity/Sequence Diagrams modeling causal chain | Interaction Diagrams; causal chain elements | Sequence attributes linking cause to hazardous situation | Forward from cause to hazardous situation |
| **Harm and severity** | Harm elements with severity classification | Harm stereotypes with severity tagged values | Harm elements; severity attributes per risk matrix | Harm records; severity classification attributes | Backward from hazardous situation |
| **Risk control measures** | Requirements allocated to logical/physical components | Requirements with risk-control stereotype; trace to design | Requirement elements typed as risk control; Satisfy links | Risk control requirements; bidirectional trace to design outputs | Forward to design input/output; backward to hazard |
| **Residual risk** | Post-control risk assessment linked to controls | Residual risk attributes on hazard elements after control | Risk elements with post-mitigation probability/severity | Residual risk attributes; benefit-risk linkage | Backward from control verification |
| **Verification of risk controls** | Test references linked to control requirements | Verify relationships from test cases to risk controls | Test Cases linked to risk control requirements | Verification records; test-to-control trace | Backward from test result to risk control to hazard |

### FDA Design Controls (21 CFR 820.30) to Arcadia Phases and V-Model

| Design Control Element | Arcadia Phase | V-Model Stage | Model Artifact | DHF Evidence |
|---|---|---|---|---|
| **Design input** | OA → SA | Left arm: requirements | OA capabilities, SA system functions, requirement attributes | Design input document; traceable requirement records |
| **Design output** | SA → LA → PA | Left arm: architecture/design | SA functional chains, LA component hierarchy, PA physical structure | Design output specifications; architecture descriptions |
| **Design review** | All phases (gate reviews) | Horizontal reviews at each level | Review records referencing model baselines | Design review meeting minutes; action item closure |
| **Design verification** | PA (implementation verification) | Right arm: unit/integration/system test | Test references traced to PA elements and requirements | Verification protocols and reports; traceability matrix |
| **Design validation** | Post-PA (user environment) | Right arm: acceptance/validation | Validation plan referencing user needs from OA | Validation protocols and reports; clinical evidence |
| **Design transfer** | PA (production transition) | Bottom of V: transfer | Production specifications derived from PA | Transfer records; manufacturing process validation |
| **Design changes** | Any phase (change control) | Any stage (impact assessment) | Change records with impact trace across phases | Design change orders; re-verification evidence |

### DHF and Technical Documentation Structure to Model-Generated Evidence

| DHF / Technical Doc Section | Model Source | Model-Generated Export | Curated Submission Document |
|---|---|---|---|
| **User needs and intended use** | OA actors, capabilities, operational scenarios | Stakeholder requirements export; use context diagrams | User needs document; indications for use statement |
| **Design input requirements** | SA system functions; requirement attributes with source trace | Requirements list with attributes (safety class, risk trace, source) | Software requirements specification; system requirements |
| **Architecture and design** | LA component hierarchy; PA physical structure; interface definitions | Architecture diagrams; interface control documents; data flow diagrams | Software architecture design chart; system design description |
| **Risk management file** | Hazard/harm/control elements across OA-SA-LA-PA | Risk table export with full trace chain; risk control verification matrix | Risk management report; risk-benefit analysis |
| **Verification evidence** | Test references linked to requirements and PA elements | Traceability matrix (requirement → test → result); coverage report | Verification summary report; test protocols and results |
| **Validation evidence** | Validation plan referencing OA user needs | Validation linkage from user needs to outcomes | Validation summary report; clinical evaluation report |
| **Cybersecurity documentation** | Threat model elements in OA/SA; security controls in LA/PA | Threat model export; SBOM generation from component inventory | Cybersecurity documentation per FDA guidance |
| **GSPR mapping (EU MDR)** | GSPR requirements linked to evidence across all phases | GSPR compliance matrix with cross-references to evidence | GSPR mapping document with harmonized standard references |
| **Post-market surveillance** | Feedback linkage from field data to risk file elements | Updated risk tables; trend analysis from surveillance data | PSUR / PMS report; post-market clinical follow-up report |

---

## Tool Coverage Matrix

Summary of which standards/frameworks are covered by each MBSE tool in the crosswalk tables above.

| Standard / Framework | Capella | Cameo/MagicDraw | Sparx EA | Rhapsody | DOORS | MATLAB/Simulink | AUTOSAR Tools |
|---|---|---|---|---|---|---|---|
| **ARP4754A / ARP4761A** | x | x | x | x | x | x | |
| **DO-178C / DO-254 / DO-331** | x | x | x | x | x | x | |
| **DO-330 (Tool Qualification)** | x | x | x | x | x | x | |
| **DO-326A (Airworthiness Security)** | x | x | | | | | |
| **DoDAF / UAF** | x | x | x | x | | | |
| **DI-SESS / CDRL** | x | x | x | | x | | |
| **MIL-STD-882E** | x | x | x | | x | | |
| **ISO 26262** | x | x | | | x | | x |
| **ISO 21434 (Cybersecurity)** | x | x | | | | | |
| **ISO 21448 (SOTIF)** | x | x | | | | | |
| **AUTOSAR (Classic/Adaptive)** | x | x | | | | | x |
| **UNECE R155 / R156** | x | x | | | | | |
| **IEC 62304** | x | x | x | | x | x | |
| **ISO 14971** | x | x | x | | x | | |
| **FDA 21 CFR 820.30** | x | x | | | | | |
| **EU MDR (GSPR)** | | | | | | | |

**Reading the matrix**: An "x" indicates that the crosswalk tables above include specific implementation guidance for that standard-tool combination. Absence does not mean the tool cannot support the standard -- it means the crosswalk tables above do not include that specific mapping. EU MDR GSPR is referenced in the DHF table but without tool-specific implementation columns. Capella includes Arcadia-native representations. AUTOSAR Tools column covers Vector DaVinci, ETAS ISOLAR, EB tresos, and similar AUTOSAR authoring environments.
