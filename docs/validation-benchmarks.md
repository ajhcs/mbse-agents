# SME Validation Benchmarks

This file contains tricky domain questions designed to validate that each MBSE agent possesses genuine practitioner-level knowledge rather than surface-level familiarity. Each question targets an area where a real systems engineer would have precise, experience-informed answers but where a non-expert (or a poorly trained AI) would give a plausible-sounding but materially wrong response.

Use these benchmarks to:

- **Evaluate agent accuracy** before deploying to real projects
- **Identify knowledge gaps** that need correction in agent prompts or training
- **Regression test** after agent updates to ensure domain fidelity is maintained
- **Compare agents** against human SME baselines

Scoring guidance: An agent should address the correct answer and mention the key points listed. Partial credit is appropriate when the agent gets the core distinction right but misses secondary details.

---

## Aerospace Systems Engineer

### AQ-1: ARP4761 vs ARP4761A CMA Treatment Differences

**Question:** Our safety team is updating from ARP4761 to ARP4761A. How does the treatment of Common Mode Analysis change, and what new method does 4761A introduce that 4761 did not explicitly include?

**Why it's tricky:** A non-expert will treat ARP4761 and ARP4761A as minor editorial revisions. In reality, ARP4761A significantly restructured the CMA methodology and introduced Common Cause Analysis (CCA) as a distinct, first-class method alongside Zonal Safety Analysis (ZSA) and Particular Risks Analysis (PRA). ARP4761 bundled these less formally. A surface-level answer will say "they're basically the same" or confuse CMA with CCA.

**Correct answer:** ARP4761A breaks Common Mode Analysis into three explicit sub-analyses: Common Cause Analysis (CCA), Zonal Safety Analysis (ZSA), and Particular Risks Analysis (PRA). The original ARP4761 treated CMA more monolithically. ARP4761A also introduces explicit guidance on model-based safety assessment (MBSA) as a complementary technique and provides clearer linkage between the safety process and the ARP4754A development assurance process. The CCA method now has its own structured process with defined inputs and outputs rather than being an implicit part of the broader CMA umbrella.

**Agent should mention:**
- The CCA / ZSA / PRA decomposition
- That ARP4761A adds model-based safety assessment (MBSA) guidance
- The tighter coupling to ARP4754A development assurance
- That ARP4761 treated CMA less formally as a single activity

---

### AQ-2: DO-331 Model-Based Development Supplement Applicability Rules

**Question:** We are using Simulink models for both requirements capture and auto-code generation. Does DO-331 apply to both uses, and at what point does DO-178C alone become insufficient?

**Why it's tricky:** Many people assume DO-331 applies whenever models are present. In reality, DO-331 applies only when models are used as a *development artifact that replaces or supplements* a traditional DO-178C lifecycle activity (e.g., models replace textual requirements, or models replace detailed design). If models are used only for visualization or informal communication, DO-331 does not apply. The distinction between "models as the specification" versus "models as supplementary illustration" is the critical boundary.

**Correct answer:** DO-331 applies when models constitute a design or requirements representation that *replaces* a traditional textual artifact in the DO-178C lifecycle. In your case, using Simulink for requirements capture means the model is the low-level requirements artifact, triggering DO-331 objectives for that lifecycle phase. Using Simulink for auto-code generation means the model is the source for the software architecture and/or detailed design, which also triggers DO-331 objectives. DO-178C alone is insufficient the moment a certification authority or your own Plan for Software Aspects of Certification (PSAC) identifies a model as the means of compliance for any DO-178C objective. Both uses independently trigger DO-331, and the applicable objectives are determined per lifecycle data item, not globally.

**Agent should mention:**
- DO-331 is triggered per lifecycle data item, not blanket per project
- The "replaces or supplements" criterion for applicability
- PSAC must declare which lifecycle data items are model-based
- Both requirements-capture and code-generation uses independently trigger DO-331
- Models used only for informal communication do not trigger DO-331

---

### AQ-3: SOI #1 Through #4 Progression and Baselining

**Question:** We just passed SOI #2. Our DER is asking whether the Software Requirements are now formally baselined or whether that happened at SOI #1. Which is correct, and what specifically gets baselined at each SOI?

**Why it's tricky:** Many engineers confuse the stage-of-involvement review content. A common wrong answer is that all requirements are baselined at SOI #1. In reality, SOI #1 is the planning review (PSAC, SDP, SVP, SCM plan), SOI #2 is the development review (requirements, design, code), SOI #3 is the verification review (test cases, coverage), and SOI #4 is the final review (SAS, SCI). Requirements are first presented at SOI #2 but the formal baseline and its associated transition criteria depend on the plans approved at SOI #1.

**Correct answer:** SOI #1 baselines the planning documents: PSAC, Software Development Plan (SDP), Software Verification Plan (SVP), Software Configuration Management Plan (SCMP), and Software Quality Assurance Plan (SQAP). Software requirements are *not* baselined at SOI #1. At SOI #2, the software requirements (high-level and, depending on the plan, low-level), software architecture, and source code are reviewed. SOI #2 is when the DER evaluates whether requirements are mature enough for their baseline, though the formal configuration management baseline occurs per the SCMP process approved at SOI #1. SOI #3 covers verification results, test procedures, structural coverage analysis, and traceability. SOI #4 is the final review covering the Software Accomplishment Summary (SAS) and Software Configuration Index (SCI).

**Agent should mention:**
- SOI #1 = planning artifacts (PSAC, SDP, SVP, SCMP, SQAP)
- SOI #2 = requirements, architecture, code review
- SOI #3 = verification evidence, coverage, traceability
- SOI #4 = SAS and SCI (final summary and configuration index)
- Requirements are reviewed at SOI #2, not baselined at SOI #1
- Baseline timing is governed by the SCMP approved at SOI #1

---

### AQ-4: DAL Allocation Reduction via Architectural Mitigation (ARP4754A Section 5.2.4)

**Question:** Our FHA assigned a function as DAL A. The lead architect says we can reduce the implementation to DAL C on each side if we use a dissimilar dual-channel architecture. Is this correct, and what constraints apply?

**Why it's tricky:** A non-expert will either say "yes, dual redundancy always lets you reduce DAL" (wrong -- the reduction rules are specific and constrained) or "no, DAL A is always DAL A" (also wrong). The actual answer involves ARP4754A Section 5.2.4's architectural independence and dissimilarity requirements, and the reduction is not arbitrary: it follows specific allowable decomposition paths with independence assurance obligations.

**Correct answer:** The architect is partially correct but oversimplifying. ARP4754A Section 5.2.4 permits DAL reduction through architectural mitigation when independence can be demonstrated. For a DAL A function, a common decomposition is to two DAL C channels, but *only if* the channels are sufficiently independent (no common failure modes) and dissimilar (different designs or implementations). The independence argument must address common mode failures, shared resources, and common design errors. Merely having two channels is insufficient; you must show that the probability of both channels failing from a common cause is acceptably low. Additionally, the safety assessment (per ARP4761/A) must validate the independence claim, and the overall architectural argument must be documented and accepted by the certification authority. The decomposition also cannot go below DAL D for any single branch, and certain combinations require specific independence assurance levels as defined in ARP4754A Table 5.

**Agent should mention:**
- ARP4754A Section 5.2.4 and Table 5 decomposition rules
- DAL A to two DAL C channels is a valid decomposition path
- Independence and dissimilarity are both required, not just redundancy
- Common mode failure analysis must support the independence claim
- The certification authority must accept the architectural argument
- DAL D is the floor; you cannot decompose below it

---

### AQ-5: DO-330 Tool Qualification vs DO-178C Tool Qualification Overlap

**Question:** We have a requirements management tool and a code coverage tool. Our QA team says both need DO-330 qualification. Is that correct, and how does DO-330 tool qualification differ from what DO-178C Section 12.2 already requires?

**Correct answer:** DO-178C Section 12.2 defines tool qualification criteria and classifies tools as Criteria 1 (output is part of the software and could introduce errors) or Criteria 2 (tool automates a verification process and errors could fail to detect defects). DO-330 is the *process standard* that tells you how to actually qualify the tool once you determine it needs qualification. Think of DO-178C 12.2 as the "do I need to qualify?" decision and DO-330 as the "how do I qualify?" process. Not all tools require qualification -- only those whose output is directly part of the airborne software or whose failure to perform correctly could result in undetected errors. A requirements management tool typically does not need DO-330 qualification if it is used only for traceability and storage (its outputs are verified by other means). A code coverage tool is a Criteria 2 tool if it is the sole means of confirming structural coverage, and would need DO-330 qualification. The QA team is likely wrong about the requirements tool unless it performs automatic generation or transformation of requirements.

**Why it's tricky:** People conflate the decision framework (DO-178C 12.2) with the qualification process (DO-330). They also over-qualify tools that do not actually need it, or assume all development-environment tools require qualification.

**Agent should mention:**
- DO-178C Section 12.2 determines *whether* qualification is needed (Criteria 1 vs 2)
- DO-330 defines *how* to perform the qualification
- Requirements management tools typically do not need qualification if outputs are independently verified
- Code coverage tools are Criteria 2 candidates when they are the sole verification means
- Tool qualification level (TQL) in DO-330 maps to the DAL of the software being developed

---

## Defense Systems Engineer

### DQ-1: DoDAF 2.02 Data Model vs Viewpoint Presentation (AV-2 vs Ad Hoc Glossaries)

**Question:** Our program manager wants an AV-2 that lists all acronyms and definitions. Is that what AV-2 is for, and what actually belongs in AV-2 under DoDAF 2.02?

**Why it's tricky:** AV-2 is widely misunderstood as a glossary or acronym list. In DoDAF 2.02, AV-2 is the "Integrated Dictionary" -- it is a data-centric view that defines all architecture data elements (nodes, systems, services, activities, performers) used across the architecture. It is not a prose glossary. Non-experts treat it as a formatting convenience rather than the backbone of data consistency across viewpoints.

**Correct answer:** AV-2 in DoDAF 2.02 is the Integrated Dictionary, which catalogs all architecture data elements and their definitions as used across the architecture description. It is *not* a general-purpose glossary or acronym list. Each entry in AV-2 corresponds to a data element that appears in one or more viewpoints (OV, SV, SvcV, etc.) and provides the authoritative definition, type, and relationships for that element. A plain acronym list belongs in supporting documentation or the architecture description's front matter, not in AV-2. The purpose of AV-2 is to enforce semantic consistency: if "Battalion HQ" is used as a performer in OV-2, the AV-2 entry defines exactly what that performer is, its relationships, and its attributes. Under DoDAF 2.02's data-centric approach, AV-2 is effectively the architecture's data dictionary mapped to the DoDAF Meta-Model (DM2).

**Agent should mention:**
- AV-2 is the Integrated Dictionary, not a glossary
- It catalogs architecture data elements (nodes, systems, activities, performers)
- Entries correspond to DM2 (DoDAF Meta-Model) data types
- Acronym lists belong in supporting documentation, not AV-2
- AV-2 enforces semantic consistency across viewpoints

---

### DQ-2: SV-5a Completeness Checking for Unallocated Requirements

**Question:** We have completed our SV-5a (Operational Activity to Systems Function Traceability Matrix). How do we use it to verify completeness, and what does an empty row or column indicate?

**Why it's tricky:** Most people describe SV-5a as simply "a traceability matrix" without understanding its diagnostic power. An empty row (operational activity with no mapped system function) indicates an unallocated mission requirement -- a gap in system design. An empty column (system function with no mapped operational activity) indicates a function with no operational justification -- possible gold-plating or a missing operational activity. Non-experts miss these gap-detection uses.

**Correct answer:** SV-5a maps operational activities (from OV-5a/b) to systems functions (from SV-4). Completeness checking works in both directions. An empty row means an operational activity has no corresponding system function allocated to support it -- this is a *coverage gap* indicating the system architecture does not fully support the operational concept. This is a serious finding because it means a mission requirement has no system-level implementation. An empty column means a system function exists with no operational activity driving it -- this suggests either gold-plating (unnecessary functionality), a missing operational activity in the OV, or a supporting function (like BIT or logging) that may need to be traced to a non-functional requirement instead. Both gaps require adjudication: empty rows are typically design deficiencies, while empty columns require justification or OV updates.

**Agent should mention:**
- Empty row = unallocated operational activity (coverage gap, design deficiency)
- Empty column = unjustified system function (gold-plating or missing OV entry)
- SV-5a maps OV-5a/b activities to SV-4 functions
- Both directions of the matrix provide diagnostic value
- Gap adjudication is required for each finding

---

### DQ-3: JCIDS Disestablishment (2025) and Transition to MEIA/JROC Prioritization

**Question:** We are writing a requirements document and referencing JCIDS as our requirements framework. Our government lead says JCIDS has been disestablished. What replaced it, and how does this affect our ICD/CDD/CPD document hierarchy?

**Why it's tricky:** Many defense practitioners (and most AI models trained on pre-2025 data) still reference JCIDS as the active requirements framework. In 2025, the JCIDS process was formally disestablished and replaced by the Mission Engineering and Integration Analysis (MEIA) approach under JROC oversight. The ICD/CDD/CPD document hierarchy was restructured. A non-expert will either not know about the disestablishment or incorrectly describe the replacement.

**Correct answer:** JCIDS was formally disestablished in 2025. The replacement framework centers on Mission Engineering and Integration Analysis (MEIA), which shifts from document-centric capability requirements to a more analytical, mission-thread-based approach. The JROC (Joint Requirements Oversight Council) retains oversight authority but now focuses on validating capability gaps and prioritizing solutions through mission engineering analysis rather than the traditional ICD/CDD/CPD document sequence. The ICD (Initial Capabilities Document), CDD (Capability Development Document), and CPD (Capability Production Document) hierarchy is being replaced by streamlined requirements artifacts aligned to the adaptive acquisition framework pathways (Urgent Capability Acquisition, Middle Tier of Acquisition, Major Capability Acquisition, Software Acquisition, Defense Business Systems, and Acquisition of Services). Programs already in the pipeline under JCIDS may continue with their existing documents, but new starts use the MEIA-aligned process.

**Agent should mention:**
- JCIDS was disestablished in 2025
- Replaced by MEIA (Mission Engineering and Integration Analysis)
- JROC retains oversight but with mission engineering focus
- ICD/CDD/CPD hierarchy is being replaced by pathway-aligned artifacts
- Adaptive acquisition framework pathways (six pathways) drive the new document structure
- Legacy programs may continue under existing JCIDS documents

---

### DQ-4: DI-SESS-81495 (SEMP) vs DI-SESS-81748 (SDD) Scope Boundaries

**Question:** Our program requires both a Systems Engineering Management Plan (DI-SESS-81495) and a System/Subsystem Design Description (DI-SESS-81748). The new engineer thinks the SDD should describe the engineering process. Where does the SEMP end and the SDD begin?

**Why it's tricky:** Junior engineers frequently confuse "how we do systems engineering" (SEMP) with "what the system design is" (SDD). The boundary is clear in the DIDs but routinely muddled in practice. DI-SESS-81495 (SEMP) describes the SE management approach: processes, organization, reviews, risk management, TPMs, integration plans. DI-SESS-81748 (SDD) describes the technical design: architecture, interfaces, functional allocation, design decisions.

**Correct answer:** DI-SESS-81495 (SEMP) defines *how* the systems engineering effort is managed: SE processes, organizational responsibilities, technical reviews and audits, SE schedule, risk management approach, technical performance measures (TPMs), configuration management, interface management processes, and integration/verification/validation planning. DI-SESS-81748 (SDD) defines *what* the system design is: system architecture, subsystem decomposition, functional allocation to physical components, interface descriptions, design rationale, performance characteristics, and design constraints. The SEMP never describes the actual design -- it describes the process that produces and controls the design. The SDD never describes the management process -- it is the technical design artifact itself. The new engineer is wrong: process descriptions belong exclusively in the SEMP. The SDD should contain architecture diagrams, interface definitions, functional decomposition, and design trade study results.

**Agent should mention:**
- SEMP (DI-SESS-81495) = "how we engineer" (process, org, reviews, TPMs)
- SDD (DI-SESS-81748) = "what the design is" (architecture, interfaces, allocation)
- Process content never belongs in the SDD
- Design content never belongs in the SEMP
- Common junior-engineer error to blend the two scopes

---

### DQ-5: MIL-STD-882E Severity vs Probability Matrix for Software-Intensive Systems

**Question:** Our safety engineer built a 5x5 risk matrix per MIL-STD-882E with probability levels A through E on one axis and severity categories I through IV on the other. For a purely software function, how do we assign the probability level, and what is the common mistake teams make?

**Why it's tricky:** MIL-STD-882E probability levels (Frequent, Probable, Occasional, Remote, Improbable) are defined in terms of occurrence rates over system life or per operational hour. For software, probability of failure is notoriously difficult to quantify in these terms because software failures are systematic (design errors), not random (wear-out). The common mistake is assigning a low probability to a software hazard because "we'll test it thoroughly," when in fact MIL-STD-882E requires a design-based argument, not a test-confidence argument. Many teams also incorrectly assign probability based on how often the software function executes rather than the likelihood of the latent defect manifesting.

**Correct answer:** For software-intensive hazards under MIL-STD-882E, the probability level cannot be assigned using hardware-style failure rate data because software failures are deterministic (if the defect exists and the triggering condition occurs, it will always fail). The standard acknowledges this by stating that software risk assessment should emphasize severity and software control/mitigation rigor rather than attempting to quantify probability in the traditional sense. The recommended approach is: (1) assign severity based on the worst-case outcome if the software function fails, (2) assess probability based on the *complexity of the software*, the *rigor of the development process*, the *extent of testing*, and the *operational exposure* (how often the triggering conditions could occur), and (3) apply MIL-STD-882E Task 303 (Software Hazard Analysis) to systematically identify and mitigate software-related hazards. The common mistake is treating software probability like hardware probability -- assigning "Remote" because the team plans extensive testing, rather than analyzing the design complexity and operational exposure.

**Agent should mention:**
- Software failures are systematic/deterministic, not random
- Probability cannot be assigned using hardware failure rate methods
- MIL-STD-882E acknowledges software risk requires emphasis on severity and process rigor
- Task 303 (Software Hazard Analysis) is the applicable task
- Common mistake: assigning low probability based on planned testing rather than design analysis
- Operational exposure (triggering condition frequency) matters more than execution frequency

---

## Automotive Systems Engineer

### UQ-1: ASIL Decomposition (Part 9) vs ASIL Tailoring -- When Each Applies

**Question:** Our system architect wants to reduce the ASIL on a software component from ASIL D to ASIL B by "tailoring." Our functional safety manager says we need to use ASIL decomposition instead. Who is correct, and what is the difference?

**Why it's tricky:** Many engineers (and AI systems) conflate ASIL decomposition with ASIL tailoring. They are distinct mechanisms in ISO 26262. ASIL decomposition (Part 9) allows splitting a safety requirement across redundant elements, reducing the ASIL on each element, provided independence is demonstrated. ASIL tailoring (Part Clause 4.3 concept of Proven-in-Use or Clause 4.6 on state-of-the-art) is about adjusting the rigor of work products for a given ASIL based on justified rationale, not changing the ASIL assignment itself. A non-expert will use the terms interchangeably.

**Correct answer:** The functional safety manager is correct. ASIL decomposition (ISO 26262 Part 9) is the mechanism for distributing a safety requirement across multiple, sufficiently independent architectural elements, thereby reducing the ASIL assigned to each element. For example, an ASIL D requirement can be decomposed to ASIL B(D) + ASIL B(D), where the (D) suffix indicates the original requirement was ASIL D. This requires a documented independence argument (freedom from interference between the elements). ASIL tailoring is not a formal term in ISO 26262 for changing the assigned ASIL level; what people informally call "tailoring" typically refers to applying less rigorous methods for lower ASILs per the standard's tables, or invoking the concept of "proven in use" (Part 8, Clause 14) to reduce development effort. You cannot simply reclassify a component from ASIL D to ASIL B by assertion -- you must use the Part 9 decomposition mechanism with a valid independence argument, or demonstrate that the safety goal's HARA was incorrect and revise the ASIL assignment through a formal re-analysis.

**Agent should mention:**
- ASIL decomposition is defined in Part 9 and requires independence arguments
- The ASIL(X) suffix notation to indicate original requirement level
- ASIL tailoring is not a formal ISO 26262 mechanism for changing ASIL assignments
- Freedom from interference must be demonstrated for decomposition
- Changing the ASIL itself requires revising the HARA, not "tailoring"
- Proven-in-use (Part 8 Clause 14) is a separate concept from decomposition

---

### UQ-2: Freedom from Interference Arguments for Mixed-ASIL Partitions

**Question:** We have an ASIL D function and an ASIL QM function sharing the same microcontroller. What do we need to demonstrate, and what is the most commonly overlooked failure mode in freedom-from-interference arguments?

**Why it's tricky:** Most engineers know they need to show "freedom from interference" but underestimate the scope. The standard (Part 6, Clause 7.4.4 and Part 9) requires demonstrating that the QM element cannot corrupt the safety-relevant element through spatial interference (shared memory), temporal interference (CPU time, interrupt storms), or communication interference (shared buses, message corruption). The most commonly overlooked failure mode is temporal interference: a QM task that monopolizes CPU time or triggers excessive interrupts, starving the ASIL D task.

**Correct answer:** When ASIL D and QM functions share a microcontroller, ISO 26262 Part 6 Clause 7.4.4 and Part 9 require demonstrating freedom from interference across three categories: spatial (memory protection ensuring QM software cannot corrupt ASIL D memory regions), temporal (guaranteed execution time for ASIL D tasks regardless of QM task behavior, including interrupt storms and runaway loops), and communication (data integrity of messages between partitions, including sequence, timing, and corruption detection). The most commonly overlooked failure mode is temporal interference. Teams typically implement memory protection units (MPU/MMU) for spatial isolation but neglect worst-case execution time analysis that accounts for QM task misbehavior. A QM task that enters an infinite loop, triggers excessive DMA transfers, or floods a shared bus can starve the ASIL D task of execution time even with proper memory isolation. The argument must show that the ASIL D function meets its timing requirements under worst-case interference from the QM partition, including pathological behaviors that a QM-quality implementation might exhibit.

**Agent should mention:**
- Three interference categories: spatial, temporal, communication
- Temporal interference is the most commonly overlooked
- MPU/MMU for spatial isolation is necessary but not sufficient
- Worst-case execution time analysis must account for QM misbehavior
- Part 6 Clause 7.4.4 and Part 9 are the governing references
- QM infinite loops, interrupt storms, and DMA floods are specific threats

---

### UQ-3: ISO 21448 SOTIF Boundary with ISO 26262 -- Sensor Perception Failures

**Question:** Our ADAS camera system sometimes fails to detect pedestrians in low-light conditions. Is this an ISO 26262 functional safety issue or an ISO 21448 SOTIF issue? Where exactly is the boundary?

**Why it's tricky:** This is one of the most commonly confused boundaries in automotive safety. ISO 26262 covers failures due to systematic faults and random hardware faults in E/E systems. ISO 21448 (SOTIF) covers hazards arising from *intended functionality* that is insufficient or from *reasonably foreseeable misuse* -- even when the system is functioning as designed. A camera that fails to detect a pedestrian in low light *because the sensor hardware malfunctions* is ISO 26262. A camera that fails to detect a pedestrian in low light *because the algorithm's performance degrades under those conditions even though the hardware is working correctly* is ISO 21448. Non-experts typically lump all sensor-related failures under ISO 26262.

**Correct answer:** This is an ISO 21448 (SOTIF) issue, not ISO 26262, *assuming the hardware is functioning correctly*. The boundary is: ISO 26262 addresses hazards caused by malfunctions of E/E systems (hardware random faults, systematic design errors in the implementation). ISO 21448 addresses hazards that arise from functional insufficiencies of the intended functionality or from reasonably foreseeable misuse, even when the system operates as designed. A camera that cannot reliably detect pedestrians in low light is a performance limitation of the intended function -- the sensor and algorithm are working as designed, but the design is insufficient for that scenario. This falls squarely under SOTIF. If the camera fails because a hardware component degrades (e.g., a sensor element dies), that would be ISO 26262. The practical boundary: "Is the system doing what it was designed to do?" If yes and it is still unsafe, it is SOTIF. If no (it is malfunctioning), it is ISO 26262.

**Agent should mention:**
- ISO 26262 = malfunctions (hardware faults, systematic implementation errors)
- ISO 21448 = functional insufficiency of intended behavior, no malfunction present
- The "working as designed but still unsafe" test points to SOTIF
- Sensor perception degradation in edge cases is SOTIF territory
- Hardware degradation causing sensor failure is ISO 26262 territory
- The two standards are complementary, not competing

---

### UQ-4: AUTOSAR Classic vs Adaptive Platform Selection for ASIL D

**Question:** We are designing an ASIL D autonomous driving platform. Should we use AUTOSAR Classic or AUTOSAR Adaptive, and what is the safety argument difference between them?

**Why it's tricky:** Non-experts often answer based on "Adaptive is newer, so use Adaptive for new projects" without understanding the fundamental safety architecture implications. AUTOSAR Classic runs on bare-metal or RTOS with static configuration, making it well-suited for deterministic, safety-critical applications. AUTOSAR Adaptive runs on a POSIX-based OS (like Linux-derived systems) with dynamic configuration, service-oriented architecture, and is designed for high-performance computing applications. Achieving ASIL D on Adaptive is significantly harder because of the larger attack surface, non-deterministic OS behavior, and dynamic service discovery.

**Correct answer:** For ASIL D functions, AUTOSAR Classic is the established and more straightforward choice because it runs on a certified RTOS or bare-metal with static task scheduling, deterministic behavior, and a well-understood safety architecture. AUTOSAR Adaptive, built on a POSIX OS foundation, is designed for high-compute applications (sensor fusion, planning, ML inference) and supports dynamic service discovery and deployment. Achieving ASIL D on an Adaptive platform is substantially more difficult because: (1) the underlying OS (typically Linux-derived) is not ASIL-qualified and would need a safety hypervisor or qualified microkernel to partition ASIL and QM functions, (2) dynamic behavior (service discovery, runtime loading) creates non-deterministic execution paths that complicate safety analysis, and (3) the larger software stack increases the freedom-from-interference argument complexity. The practical industry pattern is: use Classic for ASIL C/D control functions (braking, steering, powertrain), use Adaptive for ASIL B or QM compute-intensive functions (perception, planning), and use a safety hypervisor or hardware separation to isolate the two. A pure ASIL D autonomous driving platform will likely use both: Classic for actuator control and Adaptive for perception/planning with appropriate partitioning.

**Agent should mention:**
- Classic: RTOS/bare-metal, static, deterministic -- straightforward ASIL D path
- Adaptive: POSIX OS, dynamic, service-oriented -- ASIL D is significantly harder
- Safety hypervisor or qualified microkernel needed for Adaptive ASIL isolation
- Industry pattern: Classic for high-ASIL actuation, Adaptive for compute-intensive perception
- Most real ASIL D platforms use both with hardware or hypervisor separation
- Dynamic service discovery is a specific challenge for safety determinism arguments

---

### UQ-5: ISO 26262 Part 6 vs Part 8 Software Development -- When You Need Both

**Question:** Our project is developing safety-related software. We are following ISO 26262 Part 6. Our assessor says we also need to comply with Part 8. What does Part 8 add that Part 6 does not cover?

**Why it's tricky:** Many teams treat Part 6 (Product Development at the Software Level) as the complete software story. Part 8 (Supporting Processes) covers configuration management, change management, documentation management, software tool qualification, and proven-in-use arguments. These are *not* duplicated in Part 6 -- they are cross-cutting process requirements that apply to all development phases. An assessor will expect both to be addressed. A non-expert will either say "Part 8 is just for hardware" or "Part 6 already covers everything."

**Correct answer:** Part 6 defines the software development lifecycle: requirements, architecture, unit design, implementation, unit testing, integration testing, and verification. Part 8 defines supporting processes that apply *across* all of Parts 4 through 7 (and by extension Part 6): configuration management (Clause 8), change management (Clause 9), verification (Clause 10 -- the process of verification, not specific test activities), documentation management (Clause 11), software tool confidence level assessment and qualification (Clause 12), qualification of software components (Clause 13), and proven-in-use argumentation (Clause 14). You need both because Part 6 tells you *what to build and how to verify it*, while Part 8 tells you *how to manage the artifacts, tools, and changes throughout that process*. Without Part 8 compliance, your Part 6 work products lack the configuration control, tool qualification, and change management rigor that the standard requires. The assessor is correct.

**Agent should mention:**
- Part 6 = software development lifecycle (build and verify)
- Part 8 = supporting processes (manage, control, qualify)
- Part 8 Clause 12 = software tool confidence levels (TCL1/TCL2/TCL3)
- Part 8 Clause 14 = proven-in-use argumentation
- Configuration management and change management are in Part 8, not Part 6
- Both are required; they are complementary, not redundant

---

## Medical Device Systems Engineer

### MQ-1: IEC 62304 Software Safety Class vs SIL Concept Differences

**Question:** Our regulatory specialist keeps referring to our IEC 62304 Software Safety Class C as "SIL 3." Are these equivalent, and what is the fundamental difference?

**Why it's tricky:** Many people assume IEC 62304 software safety classes (A, B, C) map directly to Safety Integrity Levels (SIL 1-4) from IEC 61508. They do not. IEC 62304 safety classes are based on *severity of hazard contribution* (can the software contribute to a hazardous situation, and if so, can injury result and is it serious?), not on a quantitative probability target. SILs incorporate both severity and a target failure rate. Saying "Class C equals SIL 3" conflates two fundamentally different classification systems.

**Correct answer:** IEC 62304 Software Safety Classes (A, B, C) and Safety Integrity Levels (SIL 1-4 from IEC 61508) are fundamentally different classification systems and are not equivalent. IEC 62304 classes are assigned based on the *severity of the potential contribution to a hazardous situation*: Class A = no injury or damage to health possible, Class B = non-serious injury possible, Class C = death or serious injury possible. The classification determines the *rigor of the software development process* (documentation, testing, traceability requirements) but does not specify a target failure probability. SILs from IEC 61508 combine severity with a target probability of dangerous failure per hour (e.g., SIL 3 = 10^-8 to 10^-7 per hour for continuous/high demand mode). IEC 62304 deliberately avoids quantitative reliability targets for software because software failures are systematic, not random. Class C requires the most rigorous process under IEC 62304 but says nothing about a target failure rate. Calling Class C "SIL 3" is incorrect and could mislead the development team into either over-engineering (applying quantitative reliability targets to software) or under-engineering (assuming SIL-based architectural requirements from IEC 61508 apply).

**Agent should mention:**
- IEC 62304 classes are severity-based (hazard contribution), not probability-based
- SILs from IEC 61508 combine severity and quantitative failure probability targets
- Class C does not equal SIL 3 -- they are different classification systems
- IEC 62304 avoids quantitative reliability targets for software
- Software failures are systematic, making probabilistic targets inappropriate
- Conflating the two could lead to misallocated development effort

---

### MQ-2: FDA QMSR Alignment to ISO 13485:2016 vs Legacy 21 CFR 820 QSR

**Question:** Our quality team is still working to the legacy 21 CFR 820 QSR structure. When does the transition to QMSR take effect, and what are the key structural differences they need to prepare for?

**Why it's tricky:** The FDA finalized the Quality Management System Regulation (QMSR) rule in early 2024, which aligns 21 CFR 820 with ISO 13485:2016 by incorporation by reference. Many teams either do not know about this transition, think it is optional, or believe it fundamentally changes their obligations rather than restructuring how the same obligations are expressed. The compliance date is February 2, 2026. Non-experts either miss the deadline entirely or overstate the changes.

**Correct answer:** The FDA's QMSR final rule (published January 31, 2024) incorporates ISO 13485:2016 by reference into 21 CFR 820, replacing the legacy QSR structure. The compliance date is February 2, 2026, after which all manufacturers must comply with the QMSR structure. Key structural differences: (1) the regulation now points to ISO 13485:2016 clauses rather than restating requirements in FDA-specific language, so your QMS documentation should map to ISO 13485 clause structure; (2) the FDA retains certain additional requirements beyond ISO 13485, including unique device identification, mandatory reporting, and corrections/removals -- these are preserved in the revised 21 CFR 820 as supplemental requirements; (3) design controls remain required but are now expressed through ISO 13485 Clause 7.3 rather than the old 820.30; (4) the practical impact for teams already certified to ISO 13485 is relatively minor (gap analysis on the FDA-specific supplements), but teams that only followed legacy 820 need to restructure documentation and processes to align with ISO 13485's clause numbering and terminology. The underlying obligations are largely the same, but the structure and vocabulary change significantly.

**Agent should mention:**
- QMSR compliance date: February 2, 2026
- ISO 13485:2016 incorporated by reference into 21 CFR 820
- FDA retains supplemental requirements beyond ISO 13485
- Design controls move from 820.30 to ISO 13485 Clause 7.3
- Teams already ISO 13485-certified have a smaller gap than legacy-only teams
- Structure and vocabulary change; underlying obligations are largely preserved

---

### MQ-3: Basic vs Enhanced Software Documentation Levels Replacing Level of Concern

**Question:** Our predicate device used the "Level of Concern" (Minor, Moderate, Major) framework for FDA software documentation. Our new 510(k) submission needs to follow the current guidance. What replaced Level of Concern, and how does it change our documentation package?

**Why it's tricky:** The FDA's 2023 guidance "Content of Premarket Submissions for Device Software Functions" replaced the older "Guidance for the Content of Premarket Submissions for Software Contained in Medical Devices" and eliminated the "Level of Concern" (Minor, Moderate, Major) framework. It was replaced by a two-tier "Documentation Level" system: Basic and Enhanced. Non-experts either do not know about this change or incorrectly try to map the three old levels onto the two new levels.

**Correct answer:** The FDA's September 2023 final guidance "Content of Premarket Submissions for Device Software Functions" eliminated the three-tier Level of Concern (Minor, Moderate, Major) framework and replaced it with a two-tier Documentation Level system: Basic and Enhanced. The determination is based on the risk posed by the device's software function: Enhanced documentation is required when the software function could directly result in serious injury or death (to the patient, operator, or bystander) either through the device's intended use or through a foreseeable misuse or failure. Basic documentation applies to all other software functions. Enhanced documentation requires additional items beyond Basic, including: complete software requirements specification, software architecture and design documentation, traceability matrix (requirements to design to tests), software development and maintenance practices documentation, unresolved anomaly assessment (with risk analysis), and more comprehensive verification and validation evidence including unit-level testing evidence. Basic documentation requires: software description, risk assessment, software testing documentation (system and integration level), and revision history. The three-to-two mapping is not direct: the old "Major" maps to Enhanced, but "Moderate" could be either Basic or Enhanced depending on the specific risk analysis. "Minor" maps to Basic.

**Agent should mention:**
- Level of Concern (Minor/Moderate/Major) was replaced in September 2023
- New system is two-tier: Basic and Enhanced Documentation Level
- Enhanced = software could directly cause serious injury or death
- Basic = all other software functions
- Moderate LoC does not cleanly map to either level -- risk analysis determines placement
- Enhanced requires architecture docs, traceability, unit test evidence, and unresolved anomaly assessment
- Basic requires software description, risk assessment, system/integration testing

---

### MQ-4: EU MDR 2017/745 Annex II Technical Documentation vs FDA DHF Structure

**Question:** We are pursuing both FDA clearance and EU MDR CE marking for the same device. Our regulatory team says the FDA Design History File and the EU MDR Technical Documentation (Annex II) serve the same purpose. Is that accurate, and where do they diverge?

**Why it's tricky:** While both the DHF and MDR Annex II technical documentation capture the design and development evidence for a medical device, they differ in scope, structure, and intent. The FDA DHF (21 CFR 820.30) is primarily a record of the design control process -- it demonstrates that design controls were followed. EU MDR Annex II technical documentation is a broader, more prescriptive package that must include clinical evaluation, risk management, product verification and validation, and post-market surveillance planning in a specific structure. Non-experts treat them as the same deliverable or assume one is a subset of the other.

**Correct answer:** They serve related but distinct purposes and are not interchangeable. The FDA Design History File (DHF) is a compilation of records that describes the design history of a finished device, organized around the design control process (design input, output, review, verification, validation, transfer, changes). Its purpose is to demonstrate that the design was developed under appropriate controls per 21 CFR 820.30 (now ISO 13485 Clause 7.3 under QMSR). EU MDR 2017/745 Annex II defines a comprehensive technical documentation structure with specific sections: (1) device description and specification including variants and accessories, (2) information supplied by the manufacturer (labeling), (3) design and manufacturing information, (4) general safety and performance requirements (GSPR) checklist with evidence mapping, (5) benefit-risk analysis and risk management, (6) product verification and validation, and (7) a separate Annex II section for post-market surveillance documentation. The key divergences: (a) the GSPR checklist has no direct FDA equivalent -- it requires mapping every applicable GSPR to specific evidence, similar to an Essential Principles checklist but more granular; (b) clinical evaluation per MDR Article 61 is a mandatory part of the technical documentation, while FDA clinical data requirements vary by submission type; (c) MDR requires explicit post-market surveillance and PMCF planning within the technical documentation; (d) the DHF is design-process-centric while Annex II is product-evidence-centric. Teams pursuing both need a single source of design evidence with dual-mapped outputs.

**Agent should mention:**
- DHF is design-process-centric (design controls); Annex II is product-evidence-centric
- GSPR checklist (Annex II) has no direct FDA equivalent
- MDR requires clinical evaluation as part of technical documentation
- MDR requires post-market surveillance / PMCF planning in the technical documentation
- They are not interchangeable; one is not a subset of the other
- Practical approach: single evidence repository with dual-mapped output documents

---

### MQ-5: SOUP Management Under IEC 62304 vs FDA Expectations

**Question:** We are using an open-source RTOS and a third-party image processing library in our Class C medical device software. IEC 62304 calls these SOUP. What does the standard require for SOUP management, and where do FDA expectations go beyond the standard?

**Why it's tricky:** IEC 62304 defines SOUP (Software of Unknown Provenance) management requirements that scale by software safety class, but many teams underestimate the rigor required for Class C. FDA expectations, articulated in guidance documents and review practices, often go further than IEC 62304's literal text -- particularly around cybersecurity (SBOM requirements), anomaly tracking for SOUP components, and pre-market evidence of SOUP evaluation. Non-experts either treat SOUP like internally developed code (over-engineering) or treat it as a black box with no obligations (under-engineering).

**Correct answer:** IEC 62304 requires the following for SOUP items in a Class C system: (1) identify each SOUP item including title, manufacturer, and unique version designator (Clause 8.1.2); (2) define functional and performance requirements expected from the SOUP (Clause 5.3.3); (3) define hardware and software compatibility requirements for the SOUP (Clause 5.3.4); (4) evaluate the SOUP item's published anomaly lists (known bugs) and assess whether any known anomalies could cause a hazardous situation (Clause 7.1.3); (5) establish a process for monitoring SOUP suppliers for newly published anomalies throughout the product lifecycle. For Class C, all of these apply with full rigor. FDA expectations extend beyond IEC 62304 in several practical ways: (a) the FDA increasingly expects a Software Bill of Materials (SBOM) that lists all SOUP/OTS components, their versions, and known vulnerabilities -- this is now a standard pre-market submission expectation per the 2023 cybersecurity guidance; (b) FDA reviewers expect evidence that you evaluated the SOUP against your specific use case, not just a general suitability statement; (c) for open-source components, the FDA expects assessment of the project's maintenance status, community health, and patch cadence as part of the cybersecurity risk assessment; (d) the FDA expects SOUP anomaly monitoring to continue through post-market, integrated with your CAPA and complaint-handling processes. The SBOM requirement and cybersecurity lifecycle expectations are the most significant areas where FDA goes beyond IEC 62304's literal text.

**Agent should mention:**
- IEC 62304 Clause 8.1.2: identify SOUP (title, manufacturer, version)
- Known anomaly evaluation (Clause 7.1.3) for hazardous situation potential
- Ongoing SOUP monitoring for new anomalies throughout lifecycle
- FDA expects SBOM (Software Bill of Materials) per 2023 cybersecurity guidance
- FDA expects open-source community health and maintenance assessment
- FDA expects evidence of SOUP evaluation against specific use case
- Class C requires full rigor on all SOUP management activities
- SOUP anomaly monitoring must integrate with CAPA and complaint handling
