# Historical domain question bank

These prompts came from the previous collection. Their former "correct answer"
prose was not validated and has been removed. Use them as exploratory questions,
not an answer oracle, score, or demonstration of expert experience. Verify exact
claims against the applicable primary source and adopted edition. Current held-out
inputs and reviewer criteria are separated under `evals`; see [evaluation](evaluation.md).

## AQ-1: ARP4761 vs ARP4761A CMA Treatment Differences

Our safety team is updating from ARP4761 to ARP4761A. How does the treatment of Common Mode Analysis change, and what new method does 4761A introduce that 4761 did not explicitly include?

## AQ-2: DO-331 Model-Based Development Supplement Applicability Rules

We are using Simulink models for both requirements capture and auto-code generation. Does DO-331 apply to both uses, and at what point does DO-178C alone become insufficient?

## AQ-3: SOI #1 Through #4 Progression and Baselining

We just passed SOI #2. Our DER is asking whether the Software Requirements are now formally baselined or whether that happened at SOI #1. Which is correct, and what specifically gets baselined at each SOI?

## AQ-4: DAL Allocation Reduction via Architectural Mitigation (ARP4754A Section 5.2.4)

Our FHA assigned a function as DAL A. The lead architect says we can reduce the implementation to DAL C on each side if we use a dissimilar dual-channel architecture. Is this correct, and what constraints apply?

## AQ-5: DO-330 Tool Qualification vs DO-178C Tool Qualification Overlap

We have a requirements management tool and a code coverage tool. Our QA team says both need DO-330 qualification. Is that correct, and how does DO-330 tool qualification differ from what DO-178C Section 12.2 already requires?

## DQ-1: DoDAF 2.02 Data Model vs Viewpoint Presentation (AV-2 vs Ad Hoc Glossaries)

Our program manager wants an AV-2 that lists all acronyms and definitions. Is that what AV-2 is for, and what actually belongs in AV-2 under DoDAF 2.02?

## DQ-2: SV-5a Completeness Checking for Unallocated Requirements

We have completed our SV-5a (Operational Activity to Systems Function Traceability Matrix). How do we use it to verify completeness, and what does an empty row or column indicate?

## DQ-3: JCIDS Disestablishment (2025) and Transition to MEIA/JROC Prioritization

We are writing a requirements document and referencing JCIDS as our requirements framework. Our government lead says JCIDS has been disestablished. What replaced it, and how does this affect our ICD/CDD/CPD document hierarchy?

## DQ-4: DI-SESS-81495 (SEMP) vs DI-SESS-81748 (SDD) Scope Boundaries

Our program requires both a Systems Engineering Management Plan (DI-SESS-81495) and a System/Subsystem Design Description (DI-SESS-81748). The new engineer thinks the SDD should describe the engineering process. Where does the SEMP end and the SDD begin?

## DQ-5: MIL-STD-882E Severity vs Probability Matrix for Software-Intensive Systems

Our safety engineer built a 5x5 risk matrix per MIL-STD-882E with probability levels A through E on one axis and severity categories I through IV on the other. For a purely software function, how do we assign the probability level, and what is the common mistake teams make?

## UQ-1: ASIL Decomposition (Part 9) vs ASIL Tailoring -- When Each Applies

Our system architect wants to reduce the ASIL on a software component from ASIL D to ASIL B by "tailoring." Our functional safety manager says we need to use ASIL decomposition instead. Who is correct, and what is the difference?

## UQ-2: Freedom from Interference Arguments for Mixed-ASIL Partitions

We have an ASIL D function and an ASIL QM function sharing the same microcontroller. What do we need to demonstrate, and what is the most commonly overlooked failure mode in freedom-from-interference arguments?

## UQ-3: ISO 21448 SOTIF Boundary with ISO 26262 -- Sensor Perception Failures

Our ADAS camera system sometimes fails to detect pedestrians in low-light conditions. Is this an ISO 26262 functional safety issue or an ISO 21448 SOTIF issue? Where exactly is the boundary?

## UQ-4: AUTOSAR Classic vs Adaptive Platform Selection for ASIL D

We are designing an ASIL D autonomous driving platform. Should we use AUTOSAR Classic or AUTOSAR Adaptive, and what is the safety argument difference between them?

## UQ-5: ISO 26262 Part 6 vs Part 8 Software Development -- When You Need Both

Our project is developing safety-related software. We are following ISO 26262 Part 6. Our assessor says we also need to comply with Part 8. What does Part 8 add that Part 6 does not cover?

## MQ-1: IEC 62304 Software Safety Class vs SIL Concept Differences

Our regulatory specialist keeps referring to our IEC 62304 Software Safety Class C as "SIL 3." Are these equivalent, and what is the fundamental difference?

## MQ-2: FDA QMSR Alignment to ISO 13485:2016 vs Legacy 21 CFR 820 QSR

Our quality team is still working to the legacy 21 CFR 820 QSR structure. When does the transition to QMSR take effect, and what are the key structural differences they need to prepare for?

## MQ-3: Basic vs Enhanced Software Documentation Levels Replacing Level of Concern

Our predicate device used the "Level of Concern" (Minor, Moderate, Major) framework for FDA software documentation. Our new 510(k) submission needs to follow the current guidance. What replaced Level of Concern, and how does it change our documentation package?

## MQ-4: EU MDR 2017/745 Annex II Technical Documentation vs FDA DHF Structure

We are pursuing both FDA clearance and EU MDR CE marking for the same device. Our regulatory team says the FDA Design History File and the EU MDR Technical Documentation (Annex II) serve the same purpose. Is that accurate, and where do they diverge?

## MQ-5: SOUP Management Under IEC 62304 vs FDA Expectations

We are using an open-source RTOS and a third-party image processing library in our Class C medical device software. IEC 62304 calls these SOUP. What does the standard require for SOUP management, and where do FDA expectations go beyond the standard?
