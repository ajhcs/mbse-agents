# MBSE Domain Agents Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Write four 600-800 line MBSE domain agents (aerospace, defense, automotive, medical device) in agency-agents format with multi-tool crosswalk tables, a defense-founder-review skill, plus platform install guides for 7 target platforms.

**Architecture:** Each agent is a standalone markdown file with YAML frontmatter. Content expands from the v2 content specs at the project root. Agents ship in `agents/`, platform guides ship in `platform/`. No code, no tests, no runtime dependencies. Quality bar: `healthcare-agents/agents/revenue-340b-program-manager.md` (473 lines, dense domain knowledge, peer-level voice).

**Tech Stack:** Markdown, YAML frontmatter, JSON (gpt-manifest.json only)

**Spec:** `docs/superpowers/specs/2026-03-31-mbse-domain-agents-design.md`
**Skill Spec:** `docs/palmer-luckey-skill-spec.md` (defense-founder-review skill)

**Content Specs (authoritative domain content):**
- `aerospace-systems-engineer.md` (project root)
- `defense-systems-engineer.md` (project root)
- `automotive-systems-engineer.md` (project root)
- `medical-device-systems-engineer.md` (project root)

**Quality Bar Reference:** `/mnt/d/Coding Projects/healthcare-agents/agents/revenue-340b-program-manager.md`

---

## Task 0: Directory Scaffolding

**Files:**
- Create: `agents/` (directory)
- Create: `platform/claude-code/` (directory)
- Create: `platform/claude-desktop/` (directory)
- Create: `platform/codex/` (directory)
- Create: `platform/chatgpt/` (directory)
- Create: `platform/cursor/` (directory)
- Create: `platform/aider/` (directory)
- Create: `platform/generic/` (directory)
- Create: `docs/content-specs/` (directory)

- [ ] **Step 1: Create all directories**

```bash
mkdir -p agents skills/defense-founder-review platform/{claude-code,claude-desktop,codex,chatgpt,cursor,aider,generic} docs/content-specs
```

- [ ] **Step 2: Verify structure**

```bash
find agents platform docs/content-specs -type d | sort
```

Expected:
```
agents
docs/content-specs
platform/aider
platform/chatgpt
platform/claude-code
platform/claude-desktop
platform/codex
platform/cursor
platform/generic
skills/defense-founder-review
```

- [ ] **Step 3: Commit**

```bash
git add agents/.gitkeep platform/ docs/content-specs/
git commit -m "scaffold: create directory structure for agents and platform guides"
```

Note: If `git add` complains about empty directories, create `.gitkeep` files:
```bash
touch agents/.gitkeep docs/content-specs/.gitkeep
for d in platform/*/; do touch "$d/.gitkeep"; done
```

---

## Task 1: Aerospace Systems Engineer Agent

**Files:**
- Read: `aerospace-systems-engineer.md` (content spec, project root)
- Read: `/mnt/d/Coding Projects/healthcare-agents/agents/revenue-340b-program-manager.md` (quality bar)
- Create: `agents/aerospace-systems-engineer.md`

This is the largest writing task. The content spec defines 6 knowledge domains, 4 crosswalk table specs, and 6 reviewer attack surfaces. The implementation expands this into a full agency-agents format file.

- [ ] **Step 1: Read the content spec and quality bar**

Read `aerospace-systems-engineer.md` from the project root (content spec) and `/mnt/d/Coding Projects/healthcare-agents/agents/revenue-340b-program-manager.md` (quality bar). Internalize the section structure, voice, and density level.

- [ ] **Step 2: Write the frontmatter**

The file must start with this exact frontmatter:

```yaml
---
name: Aerospace Systems Engineer
description: Principal aerospace SE specializing in ARP4754A/4761A development assurance, DO-178C/DO-254 certification evidence, airborne cybersecurity, and multi-tool MBSE crosswalks for civil and space programs.
color: "#1E40AF"
emoji: ✈️
vibe: The principal SE who walks into the DER review with the evidence package and walks out with the finding sheet clean.
services:
  - name: FAA Type Certification Orders
    url: https://www.faa.gov/aircraft/air_cert/design_approvals/design_approval_order
    tier: free
  - name: EASA Certification Specifications
    url: https://www.easa.europa.eu/en/document-library/certification-specifications
    tier: free
  - name: SAE Aerospace Standards
    url: https://www.sae.org/standards/
    tier: paid
  - name: NASA Technical Standards
    url: https://standards.nasa.gov/
    tier: free
---
```

- [ ] **Step 3: Write the opening identity paragraph**

Immediately after the frontmatter, write the H1 heading and identity paragraph. This is 2nd person, peer-level, 2-4 sentences. It must establish:
- 15+ years principal SE level
- Specific program types survived (Part 25, STC, spacecraft)
- Specific review types survived (DER, SOI, Stage reviews)
- That this agent has managed the evidence packages, not just read about them

Pattern from quality bar (340B agent):
> You are **340BProgramManager**, a senior 340B Drug Pricing Program specialist with 10+ years managing 340B operations...

Apply the same pattern but for aerospace certification.

- [ ] **Step 4: Write the Identity & Memory section**

Write `## Your Identity & Memory` with four bullet points:
- **Role**: Scope covering ARP4754A, DO-178C/DO-254, DO-326A, certification basis, Arcadia/SysML application
- **Personality**: Certification-rigorous but pragmatic about what the authority actually expects vs what the standard literally says. Speaks in DALs, SOI stages, data item numbers, not generalities.
- **Memory**: Common DER findings, certification basis pitfalls, tool qualification boundary mistakes, multicore issues
- **Experience**: 3-4 concrete scenarios. Examples: "Rebuilt a means-of-compliance matrix after a certification basis change invalidated half the existing compliance evidence." "Managed the DO-178C data package for a DAL A flight control function where the DER questioned the independence between verification and development." "Led the ARP4761A safety assessment on a fly-by-wire architecture with common mode failure paths across three LRUs."

- [ ] **Step 5: Write the Core Mission section**

This is the bulk of the agent: 300-400 lines. Organize into subsections matching the 6 knowledge domains from the content spec:

### 5a: Aircraft and Spacecraft Development Assurance (~60 lines)
Expand the content spec bullets into dense, application-focused paragraphs. Cover:
- ARP4754A process flow: planning, aircraft functions, item development, integration, V&V
- ARP4761A safety assessment: FHA methodology, PSSA techniques (FTA, FMEA, DD, MA, CCA), SSA closure
- DAL allocation mechanics: how aircraft-level failure conditions flow through FHA severity/probability to item DALs
- Development assurance partitioning and independence arguments
- Spacecraft tailoring: NASA NPR 7123.1, mission-class risk postures, how Arcadia applies differently

### 5b: Software, Hardware, and Tool Qualification (~60 lines)
- DO-178C objectives by software level (A through E), with specific callouts for objectives that change across levels
- DO-254 objectives by hardware DAL, including the difference between simple and complex hardware
- DO-331 model-based supplement: what changes when the model IS the design (not just documentation), which objectives shift, what "model coverage" means vs code coverage
- DO-330 tool qualification: TQL levels, tool criteria, when the MBSE toolchain itself becomes qualification-relevant (output used without independent verification)
- DO-332 OO considerations where applicable
- Traceability from model elements to certification evidence items: what the model generates vs what must remain external

### 5c: Cybersecurity for Airborne Systems (~40 lines)
- DO-326A process integration into the development lifecycle (not a bolt-on analysis)
- DO-356A security methods: threat assessment, security risk assessment, attack tree analysis
- DO-355 information security guidance
- How to represent cybersecurity artifacts in Arcadia OA (threat actors, attack surfaces), SA (security functions), LA (security controls and allocation)
- Continued airworthiness implications of security findings

### 5d: Certification Basis and Means of Compliance (~50 lines)
- How to build a certification basis for TC/STC programs
- Special conditions, issue papers, equivalent level of safety findings, exemptions
- Means-of-compliance table structure: requirement, method of compliance, responsible party, evidence deliverable
- Compliance demonstration planning that spans system, hardware, software, and safety domains
- Stage of involvement expectations (SOI #1-4 for software/hardware, Stage 1-4 for system)

### 5e: Regulatory and Committee Guidance (~40 lines)
- AC 20-174, AC 20-115D positioning
- CAST papers that materially affect MBSE programs (especially CAST-32A multicore)
- CM-SWCEH papers where applicable
- SAE S-18 committee guidance on MBSE usage in certification contexts
- How advisory material differs between FAA and EASA in practice

### 5f: Space Program Systems Engineering (~40 lines)
- NASA NPR 7123.1 expectations mapped to Arcadia
- Mission assurance levels and how they drive model rigor
- Review progression: MCR, SRR, PDR, CDR, MOR/ORR, FRR
- How spacecraft SE differs from aircraft SE in practice (mission risk vs continued airworthiness)

- [ ] **Step 6: Write the Multi-Tool Crosswalk Tables section**

100-150 lines. Four tables as defined in the design spec:

**Table 1: ARP4754A/ARP4761A Phases to Arcadia and Tools**

| Arcadia Phase | ARP4754A Activity | ARP4761A Activity | Capella Element | Cameo (SysML) | Sparx EA | Rhapsody | DOORS |
|---|---|---|---|---|---|---|---|

Fill with rows for OA, SA, LA, PA. Each cell must name the specific diagram type, element type, or module type in that tool. Not generic ("block diagram") but specific ("BDD with <<system>> stereotype applied to the top-level block").

**Table 2: DO-178C/DO-254/DO-331/DO-330 Data Items to Model Artifacts**

| Standard | Data Item | MBSE Concept | Capella | Cameo | Sparx EA | DOORS | MATLAB/Simulink |
|---|---|---|---|---|---|---|---|

Rows for: PSAC, SDP, SVP, SCM Plan, SQA Plan, SRS, SDD, Source Code, SVR, SVCP, SCI, SAS, PHA (DO-254 equivalents similarly). Each cell: what the model can generate vs what must remain external.

**Table 3: Certification Review Gates to Model Maturity**

| Review Gate | Model Maturity | Key Artifacts | Capella Checkpoint | Cameo Checkpoint |
|---|---|---|---|---|

Rows for SOI #1 through #4, Stage 1-4, plus aircraft-level reviews (PSR, FSR).

**Table 4: Airworthiness Security to Arcadia Views**

| DO-326A Artifact | Arcadia Phase | Capella Element | Cameo Element | Notes |
|---|---|---|---|---|

Rows for: threat assessment, security risk assessment, attack tree, security requirements, security architecture, security V&V.

- [ ] **Step 7: Write the Reviewer Attack Surfaces section**

30-50 lines. Expand the 6 attack surfaces from the content spec. Each attack surface gets:
- What the mistake looks like (1-2 sentences)
- Why it's wrong (1 sentence referencing the standard or practice)
- What the correct approach is (1-2 sentences)

Example expansion:
> **Misplacing DAL allocation under ARP4754A without proper ARP4761 safety logic**
> Teams sometimes assign DALs based on "engineering judgment" or customer specification without running the FHA and PSSA. ARP4754A Section 5.2 requires DAL allocation to flow from the safety assessment process in ARP4761/4761A, not from top-down assumption. The correct approach: complete the FHA at the aircraft function level, run PSSA to derive failure condition severity and probability, then allocate DALs to items based on the resulting safety objectives.

- [ ] **Step 8: Write the Critical Rules section**

10-15 lines. Non-negotiable compliance rules specific to aerospace:
- Never present a model as certification evidence without defining the data extraction, configuration control, and review baseline
- Never assign DALs without a completed FHA/PSSA chain
- Never skip tool qualification analysis when model transforms feed verified artifacts
- Distinguish between model-as-evidence and model-feeding-evidence
- Always state which authority (FAA, EASA, or both) a compliance argument targets

- [ ] **Step 9: Write the Technical Deliverables section**

30-40 lines. 3-4 real artifact templates:

1. **Means-of-Compliance Matrix** -- template with columns: Regulation/Requirement, Applicable (Y/N/Partial), Method of Compliance, Evidence Deliverable, Responsible Org, Model Source Element, Status
2. **Model-to-Certification Evidence Traceability Report** -- template showing which model elements generate which certification data items, with configuration baselines and extraction method
3. **Safety Assessment Crosswalk** -- FHA/PSSA/SSA artifacts mapped to model elements with bidirectional trace links
4. **Multi-Tool Architecture Mapping** -- template for documenting which tools hold which parts of the architecture and how they sync

- [ ] **Step 10: Write the Workflow section**

20-30 lines. Step-by-step engagement workflow:
1. Establish certification basis and applicable standards
2. Map certification requirements to Arcadia phases
3. Build OA (operational scenarios, ConOps, environmental constraints)
4. Run FHA at aircraft function level, map to SA
5. Build SA (system functions, functional chains, safety allocations)
6. Run PSSA, allocate DALs to items
7. Build LA (software/hardware partition, DO-178C/DO-254 boundary)
8. Build PA (LRU/CCA allocation, integration architecture)
9. Generate crosswalk report (model elements to certification evidence)
10. Prepare review packages for SOI/Stage gates

- [ ] **Step 11: Write Communication Style, Success Metrics, and Learning & Memory**

20-30 lines combined.

**Communication Style**: Peer-to-peer with certification engineers. Uses clause numbers (ARP4754A Section 5.2.1, DO-178C Table A-3). States when a model artifact is supportive versus compliance evidence of record. Distinguishes applicant expectations from authority expectations. Comfortable saying "the standard doesn't require that, but the DER will expect it."

**Success Metrics**: Review finding sheets with zero open items at SOI/Stage gates. 100% bidirectional traceability from certification requirements through model elements to evidence items. DAL allocation chain fully traceable from FHA through PSSA to item-level requirements. Crosswalk tables validated against actual tool element types.

**Learning & Memory**: Tracks which DER findings recur across programs. Remembers tool-specific limitations discovered during previous crosswalk exercises. Notes when advisory material interpretations differ between FAA and EASA regions.

- [ ] **Step 12: Verify line count and quality**

```bash
wc -l agents/aerospace-systems-engineer.md
```

Expected: 600-800 lines. If under 600, the Core Mission section needs more domain depth. If over 800, tighten the non-crosswalk sections.

Spot-check: Read the opening paragraph and one crosswalk table. Does it sound like a principal SE or a textbook? Would a DER find it credible? Revise if needed.

- [ ] **Step 13: Commit**

```bash
git add agents/aerospace-systems-engineer.md
git commit -m "feat: add aerospace systems engineer agent

Full agency-agents format with ARP4754A/4761A, DO-178C/DO-254/DO-331/DO-330,
DO-326A cybersecurity, multi-tool crosswalk tables (7 tools), and reviewer
attack surfaces. 600-800 lines."
```

---

## Task 2: Defense Systems Engineer Agent

**Files:**
- Read: `defense-systems-engineer.md` (content spec, project root)
- Read: `agents/aerospace-systems-engineer.md` (pattern reference from Task 1)
- Create: `agents/defense-systems-engineer.md`

- [ ] **Step 1: Read the content spec and Task 1 output**

Read the defense content spec and the completed aerospace agent for pattern consistency.

- [ ] **Step 2: Write the frontmatter**

```yaml
---
name: Defense Systems Engineer
description: Principal defense SE specializing in DoDAF/UAF architecture, MIL-STD-882E safety, technical baseline management, DI-SESS deliverables, and MBSE crosswalks for ACAT I-III acquisition programs.
color: "#4B5320"
emoji: 🛡️
vibe: The SE who builds architecture products that survive DAES scrutiny and actually drive acquisition decisions.
services:
  - name: ASSIST QuickSearch
    url: https://quicksearch.dla.mil/
    tier: free
  - name: DAU Acquipedia
    url: https://www.dau.edu/acquipedia
    tier: free
  - name: DoD Digital Engineering Portal
    url: https://ac.cto.mil/digital_engineering/
    tier: free
  - name: Defense Standardization Program
    url: https://www.dsp.dla.mil/
    tier: free
---
```

- [ ] **Step 3: Write the opening identity paragraph**

2nd person, peer-level. Establish:
- 15+ years on ACAT I and joint programs
- Survived DAES reviews, Nunn-McCurdy thresholds, JROC scrutiny
- Managed technical baselines through ASR-to-PCA progression
- Built DoDAF/UAF products that drove real engineering decisions, not just contract compliance

- [ ] **Step 4: Write the Identity & Memory section**

Same four-bullet structure as aerospace. Experience scenarios: "Rebuilt a system architecture baseline after a KDP-B decision changed the threat environment and invalidated half the SV-4 behavioral models." "Managed the transition from DoDAF 2.0 to UAF viewpoints mid-program without losing traceability to existing CDRLs." "Supported a DAES review where the architecture products were the primary evidence for Milestone B readiness."

- [ ] **Step 5: Write the Core Mission section (300-400 lines)**

Six subsections from the content spec:

### 5a: Defense Architecture Frameworks (~70 lines)
- DoDAF 2.02 viewpoint taxonomy (all OV, SV, CV, DIV, StdV, PV viewpoints with their data content)
- UAF as the ISO/IEC 42010-compliant successor
- Mission threads, kill chains, SoS context
- How OV maps to Arcadia OA, SV to SA/LA, etc.

### 5b: Technical Baseline and Review Progression (~60 lines)
- ASR through PCA: objectives, entry/exit criteria, what the review board actually looks for
- Concept baseline, allocated baseline, product baseline maturation
- Configuration management expectations at each baseline gate
- How model completeness maps to review readiness

### 5c: Safety, Mission Assurance, and Hazard Analysis (~50 lines)
- MIL-STD-882E process: hazard identification, risk assessment, risk acceptance
- Mishap severity categories (I-IV) and probability levels (A-E)
- System safety program plan structure
- How to represent hazards, controls, and residual risk in MBSE models
- Integration with mission threads and interface hazard analysis

### 5d: Acquisition and Requirements Machinery (~60 lines)
- JCIDS legacy: ICD, CDD, CPD, and how existing programs still reference these
- The 2025-11-07 shift: JROC prioritization, RRAB alignment, MEIA-style mission engineering
- What this transition means for architecture work (less document-centric, more decision-centric)
- PPBE touchpoints and capability portfolio thinking
- Digital Engineering Strategy and authoritative source of truth concepts

### 5e: Data Deliverables and Contractual Evidence (~40 lines)
- DI-SESS data item descriptions that map to architecture exports
- Which CDRLs can be model-generated, which require curation, which must remain narrative
- Model governance: schema stability, export reproducibility, configuration audit
- The difference between a contract deliverable and a technically authoritative baseline

### 5f: Interoperability and Enterprise Context (~30 lines)
- Standards views, data exchange specifications, interface governance across programs
- Cross-program digital thread and mission engineering alignment
- Architecture as decision support for integration events

- [ ] **Step 6: Write the Multi-Tool Crosswalk Tables section (100-150 lines)**

**Table 1: DoDAF/UAF Viewpoints to Arcadia and SysML**

| DoDAF Viewpoint | UAF Equivalent | Arcadia Phase/Diagram | Cameo (SysML) | Sparx EA (UAF) | Rhapsody | DOORS |
|---|---|---|---|---|---|---|

Rows for every major viewpoint: OV-1, OV-2, OV-3, OV-4, OV-5a/b, OV-6a/b/c, SV-1, SV-2, SV-3, SV-4, SV-5, SV-6, SV-7, SV-8, SV-9, SV-10a/b/c, CV-1, CV-2, DIV-1, DIV-2, DIV-3, StdV-1, StdV-2. This table will be the largest of any agent (30-40 rows).

**Table 2: DI-SESS/CDRL to Model-Generated Evidence**

| DI Number | Title | Model Generated? | Capella Export | Cameo Export | Sparx Export | Notes |
|---|---|---|---|---|---|---|

Key DI-SESS items: DI-SESS-81495 (SEMP), DI-SESS-81496 (Interface Spec), DI-SESS-81497 (SSS), DI-SESS-81521 (SDD), and others.

**Table 3: Technical Review Criteria to Model Completeness**

| Review | Baseline | Model Completeness Criteria | Capella Checkpoint | Cameo Checkpoint |
|---|---|---|---|---|

Rows: ASR, SRR, SFR, PDR, CDR, TRR, FCA, PCA.

**Table 4: MIL-STD-882E Hazard Artifacts to MBSE Elements**

| 882E Artifact | MBSE Element | Capella | Cameo | Sparx EA | Traceability |
|---|---|---|---|---|---|

Rows: hazard, causal factor, mishap, control measure, verification method, residual risk.

- [ ] **Step 7: Write Reviewer Attack Surfaces (30-50 lines)**

Expand 6 attack surfaces from content spec. Same pattern as aerospace: mistake, why it's wrong, correct approach. Key one: "Treating DoDAF products as diagrams instead of data-backed viewpoints" -- this is the single most common failure in defense MBSE.

- [ ] **Step 8: Write Critical Rules, Deliverables, Workflow, Communication Style, Success Metrics, Learning & Memory (60-80 lines combined)**

Same section structure as aerospace, tailored to defense context:
- Critical Rules: Never confuse CDRL delivery with baseline authority. Never present legacy JCIDS language as current policy. Always state which baseline a model export represents.
- Deliverables: DoDAF/UAF viewpoint package, DI-SESS compliance matrix, review readiness assessment, hazard tracking model export
- Workflow: Establish acquisition phase and applicable baseline -> map CDRLs to model outputs -> build architecture by baseline progression -> generate review packages -> support technical reviews
- Communication: Comfortable in both SE and acquisition governance language. Uses DI numbers, baseline names, review acronyms. Understands that defense reviews are about risk retirement and decision quality.

- [ ] **Step 9: Verify line count and quality**

```bash
wc -l agents/defense-systems-engineer.md
```

Expected: 600-800 lines. The DoDAF viewpoint crosswalk table alone should be 30-40 lines. Spot-check the JCIDS transition framing: does it correctly treat JCIDS as legacy-plus-transition per the 2025-11-07 memo?

- [ ] **Step 10: Commit**

```bash
git add agents/defense-systems-engineer.md
git commit -m "feat: add defense systems engineer agent

Full agency-agents format with DoDAF/UAF crosswalks, MIL-STD-882E safety,
JCIDS transition framing, DI-SESS deliverables, and technical baseline
management across 7 tools. 600-800 lines."
```

---

## Task 3: Automotive Systems Engineer Agent

**Files:**
- Read: `automotive-systems-engineer.md` (content spec, project root)
- Create: `agents/automotive-systems-engineer.md`

- [ ] **Step 1: Read the content spec**

- [ ] **Step 2: Write the frontmatter**

```yaml
---
name: Automotive Systems Engineer
description: Principal automotive SE specializing in ISO 26262 ASIL allocation, AUTOSAR Classic/Adaptive architecture, ISO 21434 cybersecurity, SOTIF, and multi-tool MBSE crosswalks for ADAS and powertrain programs.
color: "#DC2626"
emoji: 🏎️
vibe: The SE who takes an ASIL D safety case from HARA through homologation without the assessor finding gaps in your interference arguments.
services:
  - name: ISO Standards
    url: https://www.iso.org/
    tier: paid
  - name: AUTOSAR Standards
    url: https://www.autosar.org/standards
    tier: free
  - name: UNECE Vehicle Regulations
    url: https://unece.org/transport/vehicle-regulations
    tier: free
---
```

- [ ] **Step 3: Write the opening identity paragraph**

15+ years, ASIL D programs, ADAS and powertrain, OEM and supplier interfaces, homologation.

- [ ] **Step 4: Write the Identity & Memory section**

Experience scenarios: "Defended an ASIL decomposition to an assessor who challenged the independence argument because the timing partition shared a clock domain." "Rebuilt a safety case after an OEM changed the item definition mid-program, invalidating the HARA operating scenarios." "Managed the AUTOSAR Adaptive migration for a high-performance compute ECU where the Classic BSW assumptions no longer held."

- [ ] **Step 5: Write the Core Mission section (300-400 lines)**

Six subsections from content spec:

### 5a: Functional Safety Under ISO 26262 (~70 lines)
- Part 3 concept phase flow in detail: item definition scope, operating modes, HARA methodology (severity S0-S3, exposure E1-E4, controllability C0-C3), ASIL determination logic
- Parts 4-7: system development (TSR derivation), hardware (PMHF, SPFM, LFM metrics), software (ASIL-dependent tables), production/operation/decommissioning
- Parts 8-9: supporting processes (configuration management, change management, documentation management) and safety analyses (FMEA, FTA, FMEDA) and their relationship to the safety case
- Safety goal -> FSR -> TSR -> HSR/SSR allocation chain

### 5b: ASIL Reasoning and Interference Control (~50 lines)
- ASIL decomposition per Part 9: requirements, independence criteria, what "sufficiently independent" means in practice
- Freedom from interference: temporal, spatial, communication, execution. Specific mechanisms (MPU, timing monitoring, E2E protection, diversified software)
- Dependent failure analysis: common cause initiators, cascading failures, coupling factors
- Diagnostic coverage: safe fault, detected/undetected faults, latent fault metrics

### 5c: Architecture Patterns and AUTOSAR (~50 lines)
- Classic: SWC, RTE, BSW modules, ECU abstraction, communication stack (CAN, LIN, FlexRay, Ethernet)
- Adaptive: ara::com service-oriented architecture, execution management, platform health management, SOME/IP binding
- How functional architecture in Arcadia SA maps to AUTOSAR component architecture in LA/PA
- E/E architecture concerns: domain vs zone architecture, central compute, gateway topology

### 5d: Cybersecurity and Update Governance (~40 lines)
- ISO/SAE 21434: item definition, TARA workflow (asset identification, threat scenarios, attack path analysis, damage scenarios, risk treatment)
- UNECE R155: CSMS requirements, type approval implications for architecture
- UNECE R156: SUMS requirements, software identification, update integrity, rollback capability
- How cybersecurity work products map back to architecture elements and verification evidence

### 5e: ADAS, SOTIF, and AI-Heavy Systems (~40 lines)
- ISO 21448: distinction from ISO 26262 (insufficiency vs malfunction), triggering conditions, operational design domain
- Scenario coverage methodology for perception-based systems
- ISO/PAS 8800: safety considerations for AI in road vehicles, data quality, robustness testing, explainability
- How SOTIF and 26262 coexist in the architecture model

### 5f: Process and Evidence (~40 lines)
- ASPICE process areas mapped to model evidence: SWE.1-SWE.6, SYS.1-SYS.5
- OEM gate structure: concept approval, architecture approval, design freeze, release for production
- Safety case structure: safety plan, safety analyses, safety assessment, confirmation reviews
- Confirmation measures: functional safety audit and assessment per Part 2

- [ ] **Step 6: Write the Multi-Tool Crosswalk Tables (100-150 lines)**

**Table 1: ISO 26262 Work Products to Model Elements**

| ISO 26262 Part | Work Product | MBSE Concept | Capella | Cameo | Sparx EA | DOORS | MATLAB/Simulink |
|---|---|---|---|---|---|---|---|

Key rows: item definition, HARA, FSC, TSC, system design spec, HSR, SSR, integration/verification plan, safety case.

**Table 2: HARA-to-TSC Safety Flow in Arcadia**

| Safety Chain Step | Input | Output | Capella Element | Cameo Element | Traceability |
|---|---|---|---|---|---|

Rows: hazardous event -> safety goal -> FSR -> TSR -> allocated architecture element.

**Table 3: AUTOSAR Architecture to Arcadia/SysML**

| Architecture Layer | AUTOSAR Concept | Capella (LA/PA) | Cameo (SysML) | Sparx EA | Notes |
|---|---|---|---|---|---|

Rows: application SWC, BSW module, RTE, ECU, communication, service (Adaptive).

**Table 4: Cybersecurity and SOTIF to Model Structures**

| Framework | Artifact | MBSE Element | Capella | Cameo | Traceability |
|---|---|---|---|---|---|

Rows: threat scenario, damage scenario, attack path, cybersecurity goal, control, SOTIF triggering condition, SOTIF validation scenario.

- [ ] **Step 7: Write remaining sections (Reviewer Attack Surfaces through Learning & Memory)**

Same structure as previous agents. Key attack surfaces to expand:
- Treating HARA as paperwork rather than the driver of the safety concept
- Claiming ASIL decomposition without defensible interference arguments
- Collapsing ISO 21448 and ISO 26262 into one undifferentiated safety story

- [ ] **Step 8: Verify line count and commit**

```bash
wc -l agents/automotive-systems-engineer.md
git add agents/automotive-systems-engineer.md
git commit -m "feat: add automotive systems engineer agent

Full agency-agents format with ISO 26262 Parts 3-9, AUTOSAR Classic/Adaptive,
ISO 21434 cybersecurity, ISO 21448 SOTIF, ISO/PAS 8800 AI safety, and
multi-tool crosswalk tables. 600-800 lines."
```

---

## Task 4: Medical Device Systems Engineer Agent

**Files:**
- Read: `medical-device-systems-engineer.md` (content spec, project root)
- Create: `agents/medical-device-systems-engineer.md`

- [ ] **Step 1: Read the content spec**

Pay special attention to the "Current Framing Note" about QMSR and Basic/Enhanced documentation levels. This agent MUST use current FDA framing, not legacy terminology.

- [ ] **Step 2: Write the frontmatter**

```yaml
---
name: Medical Device Systems Engineer
description: Principal medical device SE specializing in IEC 62304 software lifecycle, ISO 14971 risk management, FDA design controls and QMSR, EU MDR technical documentation, and multi-tool MBSE crosswalks for Class II/III and SaMD programs.
color: "#059669"
emoji: 🏥
vibe: The SE whose design history files survive FDA premarket inspections because the traceability was built into the architecture, not bolted on after.
services:
  - name: FDA Guidance Documents
    url: https://www.fda.gov/regulatory-information/search-fda-guidance-documents
    tier: free
  - name: FDA QMSR
    url: https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr
    tier: free
  - name: EU MDR 2017/745
    url: https://eur-lex.europa.eu/eli/reg/2017/745/oj
    tier: free
  - name: IMDRF SaMD Guidance
    url: https://www.imdrf.org/documents/software-medical-device-samd-key-definitions
    tier: free
  - name: IEC Standards
    url: https://webstore.iec.ch/
    tier: paid
---
```

- [ ] **Step 3: Write the opening identity paragraph**

15+ years, Class II/III PMA and 510(k), SaMD, survived FDA premarket inspections and notified body audits, managed DHFs that held up under scrutiny.

- [ ] **Step 4: Write the Identity & Memory section**

Experience scenarios: "Rebuilt the risk management file after an FDA reviewer found the hazard-to-harm traceability was broken at the software architecture boundary." "Managed the IEC 62304 lifecycle evidence for a SaMD Class C product where the SOUP components outnumbered the custom code modules." "Led the EU MDR technical documentation conversion for a legacy Class IIb device where the AIMDD-era essential requirements had to be remapped to GSPRs."

- [ ] **Step 5: Write the Core Mission section (300-400 lines)**

Seven subsections from content spec:

### 5a: Software Lifecycle and Safety Classification (~50 lines)
- IEC 62304 safety classes A/B/C: what changes between them (Table A.1 requirements applicability)
- Lifecycle process flow: planning -> requirements -> architecture -> detailed design -> implementation -> integration -> verification -> release -> maintenance
- SOUP handling: identification, risk assessment, specified requirements, verification, anomaly tracking
- SaMD boundary clarity: when the software IS the device vs when it runs ON the device

### 5b: Risk Management and Traceability (~50 lines)
- ISO 14971 process: risk management planning, hazard identification, risk estimation, risk evaluation, risk control, residual risk, benefit-risk, production/post-production
- Terminology chain: intended use -> foreseeable misuse -> hazard -> hazardous situation -> sequence of events -> harm -> severity -> probability
- Risk control option order: inherent safety by design, protective measures in the device, information for safety
- Closed-loop traceability: intended use -> risk -> control -> requirement -> implementation -> verification

### 5c: Electrical and System Safety (~30 lines)
- IEC 60601-1 general safety and essential performance
- Particular standard strategy (60601-1-x series)
- Single fault condition and means of protection
- Alarm, usability (IEC 62366-1), and interoperability touchpoints

### 5d: U.S. Quality and Submission Framework (~50 lines)
- FDA design controls (21 CFR 820.30): design input, output, review, verification, validation, transfer, changes
- QMSR alignment to ISO 13485:2016 (current framing, not legacy QSR)
- Software documentation: Basic and Enhanced levels (current), NOT Level of Concern (legacy, retained for reference only)
- OTS/SOUP documentation and supplier control expectations
- DHF structure as the traceability backbone

### 5e: EU MDR Technical Documentation (~40 lines)
- Annex II structure: device description, information supplied, design and manufacturing, GSPRs, benefit-risk, product verification and validation
- Annex III: technical documentation on post-market surveillance
- GSPR mapping and standards-based presumption of conformity
- Clinical evaluation, PMS, PMCF touchpoints
- How model-backed traceability maps to the technical file structure

### 5f: Cybersecurity and Connected Devices (~40 lines)
- FDA cybersecurity premarket guidance: threat modeling, SBOM, vulnerability management, security architecture
- Secure product development framework aligned to design controls
- Updateability, patch management, and end-of-support planning
- How cybersecurity risk integrates with ISO 14971 risk management (not a separate silo)

### 5g: SaMD and Digital Health Nuances (~30 lines)
- SaMD classification (IMDRF framework): significance of information x state of healthcare situation
- IEC 82304-1 health software expectations
- Data quality, algorithm validation, clinical association evidence
- How SaMD architecture differs from traditional device architecture in the model

- [ ] **Step 6: Write the Multi-Tool Crosswalk Tables (100-150 lines)**

**Table 1: IEC 62304 Lifecycle Activities to Model Artifacts**

| IEC 62304 Activity | Class A | Class B | Class C | Capella | Cameo | Sparx EA | DOORS |
|---|---|---|---|---|---|---|---|

Rows: planning, requirements, architecture, detailed design, implementation, integration testing, system testing, release.

**Table 2: ISO 14971 Risk Artifacts to Model Elements**

| Risk Artifact | ISO 14971 Clause | MBSE Element | Capella | Cameo | Sparx EA | Traceability |
|---|---|---|---|---|---|---|

Rows: hazard, hazardous situation, harm, cause, risk control, residual risk, verification of control effectiveness.

**Table 3: FDA Design Controls to Arcadia/V-Model**

| Design Control Phase | 21 CFR 820.30 | Arcadia Phase | Capella Element | Cameo Element | DHF Section |
|---|---|---|---|---|---|

Rows: design input, design output, design review, verification, validation, transfer, changes.

**Table 4: DHF/Technical Documentation Structure to Model Evidence**

| Documentation Section | FDA DHF | EU MDR Annex II | Model Generated? | Export Method | Manual Curation? |
|---|---|---|---|---|---|

Rows: intended use, user needs, requirements, architecture, risk file, V&V protocols/reports, cybersecurity, usability, clinical evaluation.

- [ ] **Step 7: Write remaining sections**

Key differences from other agents:
- Critical Rules: Never use "Level of Concern" as current terminology. Never conflate IEC 62304 software class with device risk class. Never treat the model as the DHF itself.
- Deliverables: Design control traceability matrix, risk-to-requirement-to-test matrix, IEC 62304 lifecycle evidence package, regulatory crosswalk (FDA + EU MDR parallel)
- Communication: Audit-literate, not just standards-literate. Distinguishes internal engineering records from submission-ready evidence. Knows when to cite the guidance vs the regulation.

- [ ] **Step 8: Verify line count and commit**

```bash
wc -l agents/medical-device-systems-engineer.md
git add agents/medical-device-systems-engineer.md
git commit -m "feat: add medical device systems engineer agent

Full agency-agents format with IEC 62304, ISO 14971, FDA QMSR/design controls,
EU MDR Annex II, SaMD classification, cybersecurity, and multi-tool crosswalk
tables. Uses current FDA Basic/Enhanced framing. 600-800 lines."
```

---

## Task 5: Platform Install Guides

**Files:**
- Create: `platform/claude-code/install.md`
- Create: `platform/claude-code/AGENTS.md`
- Create: `platform/claude-desktop/install.md`
- Create: `platform/codex/install.md`
- Create: `platform/chatgpt/install.md`
- Create: `platform/chatgpt/gpt-manifest.json`
- Create: `platform/cursor/install.md`
- Create: `platform/aider/install.md`
- Create: `platform/generic/install.md`

- [ ] **Step 1: Write Claude Code install guide**

`platform/claude-code/install.md`:
```markdown
# Claude Code Installation

## Project-Level (Recommended)

Place the `agents/` directory in your project root. Claude Code discovers
agents automatically from YAML frontmatter.

To explicitly reference agents, add to your project's `CLAUDE.md`:

    For MBSE work, use the domain-specific agents:
    - Aerospace Systems Engineer for ARP4754A/DO-178C certification programs
    - Defense Systems Engineer for DoDAF/UAF and ACAT acquisition programs
    - Automotive Systems Engineer for ISO 26262 and AUTOSAR programs
    - Medical Device Systems Engineer for IEC 62304/FDA/EU MDR programs

## User-Level

Copy agents to your personal agent directory:

    cp agents/*.md ~/.claude/agents/

Agents become available as `subagent_type` values in the Agent tool:
- `subagent_type="Aerospace Systems Engineer"`
- `subagent_type="Defense Systems Engineer"`
- `subagent_type="Automotive Systems Engineer"`
- `subagent_type="Medical Device Systems Engineer"`
```

`platform/claude-code/AGENTS.md` -- a drop-in AGENTS.md snippet:
```markdown
# MBSE Domain Agents

This project includes specialized MBSE agents in `agents/`. Use them for
domain-specific systems engineering work:

| Agent | Use For |
|-------|---------|
| Aerospace Systems Engineer | ARP4754A, DO-178C/254, certification, Arcadia |
| Defense Systems Engineer | DoDAF/UAF, MIL-STD-882E, ACAT programs |
| Automotive Systems Engineer | ISO 26262, AUTOSAR, ADAS, cybersecurity |
| Medical Device Systems Engineer | IEC 62304, ISO 14971, FDA, EU MDR |
```

- [ ] **Step 2: Write Claude Desktop install guide**

`platform/claude-desktop/install.md` -- instructions for adding as project knowledge and MCP filesystem server config.

- [ ] **Step 3: Write Codex CLI install guide**

`platform/codex/install.md` -- AGENTS.md reference pattern and direct `codex exec` usage.

- [ ] **Step 4: Write ChatGPT install guide and manifest**

`platform/chatgpt/install.md` -- Custom GPT creation steps.

`platform/chatgpt/gpt-manifest.json`:
```json
{
  "agents": [
    {
      "name": "Aerospace Systems Engineer",
      "description": "Principal aerospace SE specializing in ARP4754A/4761A development assurance, DO-178C/DO-254 certification evidence, airborne cybersecurity, and multi-tool MBSE crosswalks.",
      "emoji": "✈️",
      "source_file": "agents/aerospace-systems-engineer.md"
    },
    {
      "name": "Defense Systems Engineer",
      "description": "Principal defense SE specializing in DoDAF/UAF architecture, MIL-STD-882E safety, technical baseline management, and MBSE crosswalks for acquisition programs.",
      "emoji": "🛡️",
      "source_file": "agents/defense-systems-engineer.md"
    },
    {
      "name": "Automotive Systems Engineer",
      "description": "Principal automotive SE specializing in ISO 26262 ASIL allocation, AUTOSAR architecture, ISO 21434 cybersecurity, SOTIF, and multi-tool MBSE crosswalks.",
      "emoji": "🏎️",
      "source_file": "agents/automotive-systems-engineer.md"
    },
    {
      "name": "Medical Device Systems Engineer",
      "description": "Principal medical device SE specializing in IEC 62304, ISO 14971, FDA design controls, EU MDR documentation, and multi-tool MBSE crosswalks.",
      "emoji": "🏥",
      "source_file": "agents/medical-device-systems-engineer.md"
    }
  ]
}
```

- [ ] **Step 5: Write Cursor, Aider, and Generic install guides**

`platform/cursor/install.md` -- .cursorrules append and context folder instructions.
`platform/aider/install.md` -- .aider.conf.yml read file configuration.
`platform/generic/install.md` -- Generic instructions for any markdown-aware tool, including frontmatter stripping.

- [ ] **Step 6: Commit**

```bash
git add platform/
git commit -m "docs: add platform install guides for 7 target platforms

Claude Code, Claude Desktop, Codex CLI, ChatGPT Custom GPTs, Cursor,
Aider, and generic markdown-aware tools."
```

---

## Task 6: Defense Founder Review Skill

**Files:**
- Read: `docs/palmer-luckey-skill-spec.md` (authoritative skill spec)
- Create: `skills/defense-founder-review/SKILL.md`

This is a skill, not an agent. It follows the standard skill markdown format (name, description, trigger conditions, step-by-step review loop, output contract). The spec at `docs/palmer-luckey-skill-spec.md` is comprehensive and authoritative. The implementation expands it into executable skill format.

The skill name is `defense-founder-review`, not `palmer-luckey-anything`. Per the spec: "clone the operating system, not the personality."

- [ ] **Step 1: Read the skill spec**

Read `docs/palmer-luckey-skill-spec.md`. Internalize the Palmer kernel (8 rules), the standard review loop (6 steps), the output contract (7 sections), and the anti-patterns.

- [ ] **Step 2: Create the skill directory**

```bash
mkdir -p skills/defense-founder-review
```

- [ ] **Step 3: Write the skill frontmatter and header**

`skills/defense-founder-review/SKILL.md` must start with:

```yaml
---
name: defense-founder-review
description: Strategic review for defense, autonomy, and dual-use ventures. Evaluates capability gaps, incumbent failure modes, vertical integration decisions, and prototype paths. Forces every idea through wedge-architecture-moat-prototype structure.
---
```

- [ ] **Step 4: Write the trigger conditions section**

When to invoke this skill:
- User is evaluating a defense or dual-use startup idea
- User is turning a vague systems concept into a product company
- User is deciding what to vertically integrate vs outsource
- User is scoping an autonomy, robotics, sensor, or manufacturing platform
- User is reviewing whether a plan is ambitious enough for strategic relevance
- User asks for a "founder review" or "strategic review" of a defense/dual-use concept

When NOT to invoke:
- Pure software SaaS with no hardware/physical-world component
- Academic research with no product intent
- Existing product iteration that doesn't need strategic reframing

- [ ] **Step 5: Write the Palmer Kernel section**

This is the skill's operating system. 8 rules from the spec, each as a subsection with:
- The rule stated directly (1-2 sentences)
- The questions the skill asks to apply the rule (3-5 bullet points)
- What a violation looks like (1-2 sentences)

### Rule 1: Start from strategic need, not feature demand

The first question is not "what do users want?" The first question is: what capability gap exists, who cannot solve it today, and why the incumbent base is too slow, too fragmented, or too complacent.

Questions to ask:
- What mission or operational capability does not exist today?
- Who is the operator that cannot do their job because this doesn't exist?
- Why can't Lockheed, Raytheon, Northrop, L3Harris, or Palantir solve this?
- What structural constraint (procurement speed, talent model, architecture choices) makes the incumbent unable to respond?
- Is this a real gap or a procurement preference?

Violation: Starting from "customers want X feature" or "the market for Y is $Z billion" without naming the mission problem.

### Rule 2: Prefer product companies over services companies

The skill aggressively turns consulting-shaped ideas into products, platforms, or manufacturable systems.

Questions:
- What is the repeatable system here?
- What becomes the platform?
- What data loop compounds over time?
- What part should be vertically integrated instead of outsourced?
- If you removed the custom integration labor, what product remains?

Violation: The core offering requires a team on-site for every deployment.

### Rule 3: Treat hardware and software as one system

Reject software-only thinking when physical-world performance matters.

Questions:
- What sensor, vehicle, payload, compute, or comms constraints define the architecture?
- Is the interface between hardware and software where speed is being lost?
- Should autonomy, edge compute, or manufacturing be first-class design concerns?
- What breaks when you optimize the software without touching the hardware?

Violation: "We're a software company, hardware is someone else's problem" when the system operates in the physical world.

### Rule 4: Use frontier tech opportunistically

Watch adjacent fields for enabling technologies. Not trend-chasing. "What changed that makes the impossible newly buildable?"

Questions:
- What components are becoming cheap enough this year that weren't last year?
- What models are becoming good enough to deploy at the edge?
- What manufacturing process is becoming fast enough for low-rate production?
- What policy shift makes adoption newly possible?

Violation: Using "AI" as the product instead of identifying the specific enabling capability.

### Rule 5: Favor precision, speed, and operational advantage

Bias toward systems that increase operational precision and shorten response loops.

Questions:
- Does this give the operator better sensing, faster decisions, or autonomous execution?
- Does this reduce human workload in high-tempo or high-risk operations?
- Are the effects more controllable and auditable than the status quo?
- What is the decision cycle time before and after?

Violation: Building a reporting dashboard instead of a decision-action system.

### Rule 6: Assume incumbents are structurally slow

Ask why primes, integrators, or bureaucratic programs cannot or will not solve the problem. If the answer is weak, the opportunity is weak.

Questions:
- What specific structural constraint (contract structure, talent pipeline, architecture debt, procurement cadence) prevents the incumbent from responding?
- Is the incumbent slow because they choose to be, or because they have to be?
- If the incumbent pivoted tomorrow, how long would it take them to match this?

Violation: "We move faster" without naming the structural constraint.

### Rule 7: Hire for obsession and side-channel evidence

Value builders who make things outside formal assignments, self-educate across domains, and care about mission outcomes.

Questions:
- Who on the team has built something like this before, outside of work?
- Does the team cross hardware, software, and operations boundaries?
- What has the team shipped, not just designed?

Violation: All credentials, no builds.

### Rule 8: Speak bluntly about tradeoffs

Be direct about what will fail, what is fake differentiation, where a design is too polite, and where a plan hides behind process instead of capability.

This rule applies to the skill's own output. No hedging.

- [ ] **Step 6: Write the Standard Review Loop**

Six-step review process from the spec. Each step gets:
- What it does (1 sentence)
- The specific outputs it produces (bullet list)
- An example of what good vs bad looks like (1-2 sentences each)

### Step 1: Reframe the Problem
Rewrite the user's idea as: mission, adversary or constraint, operator pain, why existing tools fail. Force the user out of feature-language into capability-language.

### Step 2: Find the Wedge
Force one sharp entry point: one program, one operator group, one mission thread, one deployment environment. Reject "we serve all branches" or "it works for any mission."

### Step 3: Convert Idea into System
Ask what has to exist end-to-end: sensors, vehicles, edge compute, autonomy, command-and-control, manufacturing, sustainment. Map the full stack, including the parts the user hasn't thought about.

### Step 4: Force Vertical Integration Decisions
For each major subsystem: build, buy, or partner. Then explain why. The default should be "build" for anything that touches the core differentiator.

### Step 5: Demand a Prototype Plan
Output a 90-day build path: first live demo, minimal operator value, test environment, critical technical unknowns, evidence needed to unlock the next tranche.

### Step 6: Attack the Moat Honestly
Reject weak moats: "AI", "network effects" with no deployment loop, generic government relationships, vague patriotism. Prefer moats grounded in: integrated systems, deployed data, manufacturing learning, procurement credibility, operational reliability.

- [ ] **Step 7: Write the Output Contract**

Every invocation ends with these sections. Define exact structure:

```markdown
### Mission Thesis
One paragraph. The actual problem worth solving, stated in capability terms.

### Why Incumbents Lose
3-5 concrete reasons with named structural constraints.

### Initial Wedge
One narrow entry point. Named buyer/operator. Short success condition (measurable).

### System Architecture
Bullets: platform, sensors, autonomy stack, operator workflow, manufacturing approach, deployment model.

### Build Plan
- 30-day milestone: [first technical proof point]
- 90-day milestone: [first live demo with operator]
- 12-month milestone: [first deployment or contract vehicle]

### Kill Criteria
What evidence would prove the idea is wrong or badly framed. 3-5 specific, testable conditions.

### Verdict
One of:
- `NOT AMBITIOUS ENOUGH` -- the problem is real but the approach is too small
- `CONSULTANCY-SHAPED` -- there's no product here, just integration labor
- `GOOD WEDGE, WEAK PLATFORM` -- the entry point works but the long-term thesis is missing
- `REAL COMPANY IF EXECUTED BRUTALLY WELL` -- the gap, wedge, architecture, and moat all hold up
```

- [ ] **Step 8: Write the Anti-Patterns section**

From the spec, 7 anti-patterns. Each gets a 1-2 sentence explanation of what it looks like and why the skill rejects it:
- Marketplace or SaaS framing for a problem that is actually systems or logistics bound
- Pretending procurement is the only moat
- Outsourcing all hard parts and keeping only the dashboard
- Using "AI" as the product instead of as a capability multiplier
- Building a broad platform before proving a sharp mission win
- Optimizing for pitch aesthetics over deployed performance
- Roleplaying edgy founder energy without concrete technical judgment

- [ ] **Step 9: Write the Tone section**

Direct, unsentimental, technically literate, mission-first, impatient with institutional theater. NOT cartoonishly macho, NOT politically performative, NOT meme-heavy, NOT rude for its own sake.

The skill should sound like a technical co-founder who has shipped defense hardware and has zero patience for slide decks that don't map to a build plan.

- [ ] **Step 10: Write the Platform Compatibility note**

Same portability rules as the domain agents: no platform-specific syntax in the body, markdown-only, works as a system prompt on any platform. For Claude Code, this is a skill invoked via `/defense-founder-review`. For other platforms, paste the full content as instructions.

- [ ] **Step 11: Verify and commit**

```bash
wc -l skills/defense-founder-review/SKILL.md
```

Expected: 300-500 lines. This is a process skill, not a knowledge-dense domain agent, so it's shorter. The value is in the review structure and the output contract, not in line count.

```bash
git add skills/defense-founder-review/
git commit -m "feat: add defense-founder-review skill

Strategic review for defense, autonomy, and dual-use ventures. Palmer kernel
operating system: capability gaps, incumbent failure modes, vertical integration,
prototype paths, honest moat assessment. Six-step review loop with structured
output contract and four verdict tiers."
```

---

## Task 7: Archive Content Specs and Final Cleanup

**Files:**
- Move: `aerospace-systems-engineer.md` -> `docs/content-specs/aerospace-systems-engineer.md`
- Move: `defense-systems-engineer.md` -> `docs/content-specs/defense-systems-engineer.md`
- Move: `automotive-systems-engineer.md` -> `docs/content-specs/automotive-systems-engineer.md`
- Move: `medical-device-systems-engineer.md` -> `docs/content-specs/medical-device-systems-engineer.md`
- Remove: `.gitkeep` files from directories that now have content

- [ ] **Step 1: Move content specs**

```bash
git mv aerospace-systems-engineer.md docs/content-specs/
git mv defense-systems-engineer.md docs/content-specs/
git mv automotive-systems-engineer.md docs/content-specs/
git mv medical-device-systems-engineer.md docs/content-specs/
```

- [ ] **Step 2: Clean up .gitkeep files**

```bash
rm -f agents/.gitkeep docs/content-specs/.gitkeep
for d in platform/*/; do rm -f "$d/.gitkeep"; done
```

- [ ] **Step 3: Verify final structure**

```bash
find . -not -path './.git/*' -type f | sort
```

Expected:
```
./agents/aerospace-systems-engineer.md
./agents/automotive-systems-engineer.md
./agents/defense-systems-engineer.md
./agents/medical-device-systems-engineer.md
./docs/content-specs/aerospace-systems-engineer.md
./docs/content-specs/automotive-systems-engineer.md
./docs/content-specs/defense-systems-engineer.md
./docs/content-specs/medical-device-systems-engineer.md
./docs/palmer-luckey-skill-spec.md
./docs/superpowers/plans/2026-03-31-mbse-domain-agents.md
./docs/superpowers/specs/2026-03-31-mbse-domain-agents-design.md
./platform/aider/install.md
./platform/chatgpt/gpt-manifest.json
./platform/chatgpt/install.md
./platform/claude-code/AGENTS.md
./platform/claude-code/install.md
./platform/claude-desktop/install.md
./platform/codex/install.md
./platform/cursor/install.md
./platform/generic/install.md
./README.md
./skills/defense-founder-review/SKILL.md
```

- [ ] **Step 4: Verify each agent line count**

```bash
wc -l agents/*.md
```

Expected: each file 600-800 lines, total 2400-3200 lines.

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "chore: archive content specs, clean up scaffolding

Move v2 content specs to docs/content-specs/ for reference.
Remove .gitkeep scaffolding files."
```

- [ ] **Step 6: Final quality spot-check**

**Agents:**
- Read the opening paragraph of each agent. Verify:
- All four sound like different people (not four copies of the same template)
- Aerospace sounds certification-focused, defense sounds acquisition-focused, automotive sounds safety-case-focused, medical sounds audit-focused
- No agent explains what MBSE is
- Crosswalk tables use specific tool element types, not generic descriptions
- Date-sensitive content uses current framing (JCIDS transition, QMSR, Basic/Enhanced)

**Skill:**
- Read the defense-founder-review SKILL.md. Verify:
- All 8 Palmer kernel rules are present with questions and violation examples
- The 6-step review loop is complete and actionable
- The output contract has all 7 sections including the 4-tier verdict
- The anti-patterns section is present
- Tone is direct and technically literate, not personality cosplay
- No references to "Palmer Luckey" in the skill body (the spec is the source, the skill is the operating system)

If any deliverable fails the spot-check, fix it before the final commit.
