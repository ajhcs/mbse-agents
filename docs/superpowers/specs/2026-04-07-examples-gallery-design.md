# Examples Gallery Design Spec

Reference architecture examples for each MBSE domain agent, providing real artifact structure that demonstrates what has been built and how domain-specific systems engineering artifacts connect.

## Scope

- 5 domains: aerospace, defense, automotive, medical-device, electronic-systems
- 1 flagship system per domain (full artifact set, 6-7 files)
- 3 fleet systems per domain (core artifacts, 4 files each)
- 1 new agent: Electronic Systems Engineer (~600 lines)
- Agent integration: reference systems section added to all 5 agents
- Gallery index + 5 domain indexes

## Directory Structure

```
examples/
├── README.md                                    # Gallery index
├── aerospace/
│   ├── README.md                                # Domain overview
│   ├── flight-management-system/                # FLAGSHIP
│   │   ├── system.yaml
│   │   ├── README.md
│   │   ├── requirements.md
│   │   ├── architecture.md
│   │   ├── hazard-analysis.md
│   │   ├── traceability.md
│   │   ├── assurance-evidence.md
│   │   └── cybersecurity.md
│   ├── cubesat-constellation/                   # Fleet
│   │   ├── system.yaml
│   │   ├── README.md
│   │   ├── requirements.md
│   │   └── architecture.md
│   ├── eva-suit-life-support/                   # Fleet
│   │   ├── system.yaml
│   │   ├── README.md
│   │   ├── requirements.md
│   │   └── architecture.md
│   └── launch-vehicle-avionics/                 # Fleet
│       ├── system.yaml
│       ├── README.md
│       ├── requirements.md
│       └── architecture.md
├── defense/
│   ├── README.md
│   ├── uas-ground-control-station/              # FLAGSHIP
│   │   ├── system.yaml
│   │   ├── README.md
│   │   ├── requirements.md
│   │   ├── architecture.md
│   │   ├── hazard-analysis.md
│   │   ├── traceability.md
│   │   ├── assurance-evidence.md
│   │   └── dodaf-views.md
│   ├── ballistic-missile-defense/               # Fleet
│   │   ├── system.yaml
│   │   ├── README.md
│   │   ├── requirements.md
│   │   └── architecture.md
│   ├── tactical-sdr-radio/                      # Fleet
│   │   ├── system.yaml
│   │   ├── README.md
│   │   ├── requirements.md
│   │   └── architecture.md
│   └── naval-combat-management/                 # Fleet
│       ├── system.yaml
│       ├── README.md
│       ├── requirements.md
│       └── architecture.md
├── automotive/
│   ├── README.md
│   ├── autonomous-emergency-braking/            # FLAGSHIP
│   │   ├── system.yaml
│   │   ├── README.md
│   │   ├── requirements.md
│   │   ├── architecture.md
│   │   ├── hazard-analysis.md
│   │   ├── traceability.md
│   │   ├── assurance-evidence.md
│   │   └── cybersecurity.md
│   ├── ev-battery-management/                   # Fleet
│   │   ├── system.yaml
│   │   ├── README.md
│   │   ├── requirements.md
│   │   └── architecture.md
│   ├── steer-by-wire/                           # Fleet
│   │   ├── system.yaml
│   │   ├── README.md
│   │   ├── requirements.md
│   │   └── architecture.md
│   └── v2x-communication/                       # Fleet
│       ├── system.yaml
│       ├── README.md
│       ├── requirements.md
│       └── architecture.md
├── medical-device/
│   ├── README.md
│   ├── smart-infusion-pump/                     # FLAGSHIP
│   │   ├── system.yaml
│   │   ├── README.md
│   │   ├── requirements.md
│   │   ├── architecture.md
│   │   ├── hazard-analysis.md
│   │   ├── traceability.md
│   │   └── assurance-evidence.md
│   ├── surgical-robot-platform/                 # Fleet
│   │   ├── system.yaml
│   │   ├── README.md
│   │   ├── requirements.md
│   │   └── architecture.md
│   ├── continuous-glucose-monitor/              # Fleet
│   │   ├── system.yaml
│   │   ├── README.md
│   │   ├── requirements.md
│   │   └── architecture.md
│   └── patient-monitoring-network/              # Fleet
│       ├── system.yaml
│       ├── README.md
│       ├── requirements.md
│       └── architecture.md
└── electronic-systems/
    ├── README.md
    ├── quantum-processor-control/               # FLAGSHIP
    │   ├── system.yaml
    │   ├── README.md
    │   ├── requirements.md
    │   ├── architecture.md
    │   ├── hazard-analysis.md
    │   ├── traceability.md
    │   └── assurance-evidence.md
    ├── safety-critical-soc/                     # Fleet
    │   ├── system.yaml
    │   ├── README.md
    │   ├── requirements.md
    │   └── architecture.md
    ├── fpga-radar-signal-processor/             # Fleet
    │   ├── system.yaml
    │   ├── README.md
    │   ├── requirements.md
    │   └── architecture.md
    └── hpc-cluster-orchestration/               # Fleet
        ├── system.yaml
        ├── README.md
        ├── requirements.md
        └── architecture.md
```

Total: 5 flagships (7-8 files each) + 15 fleet systems (4 files each) + 6 indexes = ~105 files.

## Example Systems

### Aerospace

| System | Tier | Description |
|--------|------|-------------|
| Integrated Flight Management System | Flagship | Multi-channel FMS with flight planning, navigation, and performance computation. Dual FMC architecture with dissimilar backup. DAL A software (DO-178C), DAL A programmable hardware (DO-254), cybersecurity (DO-326A). |
| CubeSat Constellation | Fleet | 12-unit LEO constellation for Earth observation with intersatellite links. NASA NPR 7123.1 tailored for Class C mission assurance. CCSDS communication protocols. |
| EVA Suit Life Support | Fleet | Extravehicular activity portable life support system for ISS and Artemis. Pressure regulation, O2/CO2 management, thermal control. NASA-STD-5005 fracture control, human-rating (NPR 8705.2). |
| Launch Vehicle Avionics | Fleet | Upper stage avionics for medium-lift launch vehicle. Flight termination system (FTS), guidance/navigation/control, telemetry. Range safety (EWR 127-1), DO-178C Level A for FTS software. |

### Defense

| System | Tier | Description |
|--------|------|-------------|
| UAS Ground Control Station | Flagship | Multi-vehicle ground control station for Group 4/5 UAS. C2 link management, mission planning, sensor payload control, airspace integration. ACAT II program with MOSA/FACE compliance. DoDAF OV/SV/DIV views, MIL-STD-882E, DI-SESS deliverables. |
| Ballistic Missile Defense Element | Fleet | Engagement coordination element within layered BMDS architecture. Track management, threat assessment, weapon-target pairing. ACAT ID SoS with MDA oversight. |
| Tactical SDR Radio | Fleet | Software-defined radio for JTRS waveform hosting. SCA 4.1 compliant, multi-channel MANET, COMSEC/TRANSEC, NSA Type 1. FACE transport/platform profiles. |
| Naval Combat Management System | Fleet | Surface combatant CMS integrating sensors, weapons, and C2. Track fusion, engagement planning, cooperative engagement. MIL-STD-1553/VME to GigE modernization path. |

### Automotive

| System | Tier | Description |
|--------|------|-------------|
| Autonomous Emergency Braking | Flagship | Camera + radar fusion AEB for passenger vehicles. ASIL D safety case, ISO 26262 full lifecycle, SOTIF (ISO 21448) for perception limitations, ISO 21434 cybersecurity, AUTOSAR Classic/Adaptive split architecture. |
| EV Battery Management System | Fleet | High-voltage lithium-ion BMS for 800V architecture. Cell monitoring, thermal management, state estimation (SoC/SoH), contactor control. ASIL C/D, UN R100, IEC 62619. |
| Steer-by-Wire | Fleet | Full steer-by-wire with no mechanical fallback. Dual-redundant steering actuators, torque feedback, rack position control. ASIL D, fail-operational architecture. |
| V2X Communication Unit | Fleet | C-V2X (PC5 + Uu) on-board unit for cooperative perception and platooning. ETSI ITS-G5 / SAE J3161, ISO 21434 cybersecurity, SOTIF interaction with ADAS. |

### Medical Device

| System | Tier | Description |
|--------|------|-------------|
| Smart Infusion Pump | Flagship | Large-volume infusion pump with dose error reduction software (DERS). Drug library, wireless connectivity, EHR integration. Class III (FDA), IEC 62304 Class C software, ISO 14971, IEC 60601-1, FDA QMSR design controls, EU MDR Class IIb. |
| Surgical Robot Platform | Fleet | Multi-arm teleoperated surgical system for minimally invasive procedures. Master-slave architecture, haptic feedback, vision system. Class II De Novo, IEC 62304 Class C, IEC 80601-2-77. |
| Continuous Glucose Monitor | Fleet | Wearable CGM with mobile app and cloud analytics. SaMD component for trend prediction and insulin dosing guidance. Class II 510(k), IEC 62304 Class B (sensor) / Class A (display), IMDRF SaMD N41. |
| Patient Monitoring Network | Fleet | Multi-parameter bedside monitoring with central station aggregation. SpO2, ECG, NIBP, temperature, capnography. IEC 60601-1-8 alarm management, IEC 80001-1 health IT network risk management. |

### Electronic Systems

| System | Tier | Description |
|--------|------|-------------|
| Quantum Processor Control System | Flagship | Cryogenic control electronics and room-temperature orchestration stack for a 100+ qubit superconducting quantum processor. RF pulse generation, qubit readout, error correction feedback loop, calibration automation. Emerging standards landscape, IEC 61508 where applicable to safety-critical calibration, formal verification of control sequences. |
| Safety-Critical SoC | Fleet | Automotive-grade SoC for ADAS compute. Lockstep CPU cores, hardware safety mechanisms (BIST, ECC, watchdog), ASIL D random hardware fault metrics. ISO 26262-11, AEC-Q100 qualification. |
| FPGA Radar Signal Processor | Fleet | FPGA-based real-time signal processor for phased array radar. Pulse compression, Doppler processing, CFAR detection, track-before-detect. DO-254 DAL B, MIL-STD-882E safety. |
| HPC Cluster Orchestration | Fleet | Workload orchestration for a 500-node GPU compute cluster. Job scheduling, resource allocation, fault recovery, power management. IEC 61508 SIL 1 for safety-critical batch processes, data integrity per ALCOA+ principles. |

## ID Taxonomy

Every system uses a shared ID prefix registry. IDs are unique within a system.

| Prefix | Scope | Example | Defined In |
|--------|-------|---------|------------|
| `MODE-` | Operating mode | `MODE-001` | `README.md` |
| `REQ-` | Requirement (all categories) | `REQ-FUN-012` | `requirements.md` |
| `HZ-` | Hazard / hazardous situation | `HZ-003` | `hazard-analysis.md` |
| `CTL-` | Risk control / mitigation | `CTL-007` | `hazard-analysis.md` |
| `CMP-` | Component (HW or SW) | `CMP-FMC-01` | `architecture.md` |
| `IFC-` | Interface | `IFC-EXT-003` | `architecture.md` |
| `VER-` | Verification activity | `VER-T-015` | `traceability.md` |
| `EVD-` | Evidence artifact | `EVD-042` | `assurance-evidence.md` |

### Fleet Systems and IDs

Fleet systems use the same ID prefixes for `MODE-`, `REQ-`, and `CMP-` in their core files. They do not have `HZ-`, `CTL-`, `VER-`, or `EVD-` IDs since those are defined in flagship-only assurance files. If a fleet system is later promoted to flagship, the assurance files add IDs that reference the existing `REQ-` and `CMP-` IDs without renumbering.

### Cross-File Integrity Rules (flagships)

- Every `HZ-` has at least one `CTL-` or an explicit acceptability rationale
- Every `CTL-` maps to at least one `REQ-`
- Every assurance-relevant `REQ-` maps to at least one `CMP-` and one `VER-`
- Every `VER-` maps to at least one `EVD-`
- Every gap is an explicit row in `traceability.md`, not an omission

## File Conventions

### Mandatory Core (every system, fleet or flagship)

| File | Purpose |
|------|---------|
| `system.yaml` | Machine-readable metadata |
| `README.md` | ConOps, system boundary, operating modes, stakeholders, standards |
| `requirements.md` | Structured requirements with uniform record schema |
| `architecture.md` | Decomposition, allocation, interfaces, partitioning |

### Flagship Assurance Layer (common filenames, domain-specific content)

| File | Role |
|------|------|
| `hazard-analysis.md` | Risk/hazard identification, fault analysis, risk controls |
| `traceability.md` | Forward and reverse traces, gap register |
| `assurance-evidence.md` | Evidence index, review gates, lifecycle status |

### Domain-Specific Extras

| File | Domains | Purpose |
|------|---------|---------|
| `dodaf-views.md` | Defense | DoDAF/UAF viewpoint products |
| `cybersecurity.md` | Aerospace, Automotive | Threat analysis (DO-326A, ISO 21434 TARA) |

## Artifact Templates

### system.yaml

```yaml
title: {System Name}
domain: {aerospace|defense|automotive|medical-device|electronic-systems}
tier: {flagship|fleet}
status: {complete|draft|planned}
standards:
  - {Standard 1}
  - {Standard 2}
assurance_framework: {One-line description of certification/assurance regime}
system_class: {Domain-specific classification, e.g., DAL A, ASIL D, Class III}
summary: >
  {2-3 sentence system description}
```

### README.md

```markdown
# {System Name}

## Overview
What this system is, what problem it solves, who operates it.
Flagship: 200-400 words. Fleet: 100-150 words.

## System Boundary
What is inside the system, what is outside. Physical and logical
boundaries. Explicitly name what is excluded and why.

## Operational Environment
Where it operates, environmental conditions, installation context,
interfacing systems at the boundary.

## Operating Modes

| Mode ID   | Name        | Description                    | Active Functions | Constraints        |
|-----------|-------------|--------------------------------|------------------|--------------------|
| MODE-001  | Normal      | Full operational capability    | All              | None               |
| MODE-002  | Degraded    | Partial function after fault   | {subset}         | {restrictions}     |
| ...       | ...         | ...                            | ...              | ...                |

Mode IDs are referenced by hazard-analysis.md, requirements.md,
and traceability.md.

## Key Technical Challenges
3-5 things that make this system hard from an SE perspective.

## Stakeholders
Operator, maintainer, certifying authority, patient/end-user.

## Standards Applicability
Which standards apply and the rationale for applicability.
```

### requirements.md

```markdown
# Requirements

All requirements are atomic, testable shall-statements.

## Requirement Record Schema

| Field         | Description                                                          |
|---------------|----------------------------------------------------------------------|
| ID            | Unique identifier (e.g., REQ-FUN-001)                               |
| Statement     | Atomic shall-statement                                               |
| Rationale     | Why this requirement exists                                          |
| Source        | Hazard ID, risk control ID, regulatory clause, or stakeholder need   |
| Parent        | Parent requirement ID (if derived)                                   |
| Verification  | Method: test, analysis, inspection, demonstration                    |
| Allocation    | Target component ID(s) from architecture.md                          |
| Status        | Draft, baselined, verified, deferred                                 |

## Functional Requirements
REQ-FUN-001 through REQ-FUN-0xx

## Safety / Assurance Requirements
Source must reference a hazard ID (HZ-xxx), risk control ID (CTL-xxx),
or regulatory clause. No prose-only sourcing.

## Interface Requirements
Each entry includes: data item, direction (in/out/bidirectional),
interface partner, protocol/standard, timing/latency constraint.

## Performance Requirements
Each entry includes: threshold value, operating condition under which
the threshold applies, and measurement method.
```

Flagship: 30-50 requirements. Fleet: 8-12 covering functional + safety.

### architecture.md

```markdown
# Architecture

## System Context
The system in its environment. Neighboring systems, external actors,
data/control flows crossing the system boundary.

## Functional Architecture
Function decomposition from system-level down. Each function:
inputs, outputs, functional dependencies, owning subsystem.

## Physical Architecture
Hardware/software component breakdown. What runs where.
Redundancy and dissimilarity decisions.

## Allocation

| Function ID | REQ ID(s) | CMP ID | Assurance Level | Rationale |

## Interfaces

### External Interfaces
| IFC ID | Partner System | Data Item | Direction | Protocol | Timing |

### Internal Interfaces
| IFC ID | Source CMP ID | Target CMP ID | Data Item | Mechanism | Timing |

## Failure Containment / Partitioning
Partitioning strategy, independence arguments, monitoring mechanisms.
For each partition boundary: what it isolates, how isolation is
enforced (spatial, temporal, electrical), what evidence supports it.

## Architecture Decisions
3-5 major design decisions with rationale.
```

### hazard-analysis.md (flagship only)

```markdown
# Hazard Analysis

## Methodology
Applicable standard clause. Scope: system boundary and modes analyzed.

## Terminology

| Term                | Definition (this system)                | Standard Reference |
|---------------------|-----------------------------------------|--------------------|
| Hazard              | {domain-appropriate}                    | {clause}           |
| Cause               | ...                                     | ...                |
| Failure Mode        | ...                                     | ...                |
| Hazardous Situation | ...                                     | ...                |
| Harm                | ...                                     | ...                |

## Assumptions and Preconditions

| Assumption ID | Statement                              | Validity Basis     |
|---------------|----------------------------------------|--------------------|
| ASM-001       | {text}                                 | {evidence/source}  |

## Hazard Log

| HZ ID | Description | Cause(s) | Effect | MODE ID(s) | Severity | Likelihood | Initial Risk | CTL ID(s) | Residual Risk | Owner / Acceptance Authority | REQ ID(s) |

- Initial Risk: before controls
- Residual Risk: after controls, with rationale
- Every HZ references at least one MODE-xxx
- Every HZ traces to REQ ID(s) via CTL ID(s), or carries acceptability rationale

## Risk Controls

| CTL ID | HZ ID(s) | Description | Type | REQ ID(s) | VER ID(s) | Residual Risk Contribution |

Type: elimination, reduction, protective measure, information for safety.

## Fault Analysis
At least one worked fault tree, dependency diagram, or FMEA excerpt.

## Domain-Specific Sections

### Aerospace: PSSA/SSA
Fault tree excerpts with cut sets, PSSA-to-SSA progression,
quantitative probability budgets.

### Defense: Risk Acceptance
MIL-STD-882E risk matrix, risk acceptance authority chain.

### Automotive: HARA & Safety Goals
HARA table (S/E/C to ASIL), safety goals, ASIL decomposition rationale.

### Medical: Risk Management (ISO 14971)
Full risk management scope: estimation, evaluation, risk-benefit,
overall residual risk evaluation.

### Electronic: FMEA/FMECA
Component/gate-level FMEA, detection coverage, formal verification fault model.
```

### traceability.md (flagship only)

```markdown
# Traceability

## Trace Strategy
What is traced, in which direction, and why.

## Forward Traces

### Requirements to Architecture
| REQ ID | Statement (short) | CMP ID(s) | Allocation Rationale |

### Requirements to Hazards
| REQ ID | Source HZ ID(s) | Source CTL ID(s) | Source Clause |

### Requirements to Verification
| REQ ID | VER ID | Method | Artifact | Status | CMP ID | MODE ID(s) |

Status: planned, executed, passed, failed, waived.

## Reverse Traces

### Components to Requirements
| CMP ID | Component Name | REQ ID(s) | Gap? |

Orphan components are explicit rows with Gap = YES.

### Hazards to Controls to Requirements
| HZ ID | CTL ID(s) | REQ ID(s) | Fully Mitigated? |

Orphan hazards are explicit rows.

### Verification to Requirements
| VER ID | REQ ID(s) | EVD ID(s) | Status |

## Gap Register

| Gap ID  | Type                   | Entity ID | Description             | Disposition         |
|---------|------------------------|-----------|-------------------------|---------------------|
| GAP-001 | Orphan requirement     | REQ-xxx   | No component allocation | {accepted/planned}  |
| GAP-002 | Orphan hazard          | HZ-xxx    | No mitigating control   | {accepted/planned}  |

Gaps are first-class rows with disposition: accepted, planned, or escalated.

## Coverage Summary
- Requirements with architecture allocation: x/y (z%)
- Safety requirements with hazard source: x/y (z%)
- Requirements with verification evidence: x/y (z%)
- Components with at least one requirement: x/y (z%)
- Hazards with at least one control: x/y (z%)
- Controls with at least one requirement: x/y (z%)
```

### assurance-evidence.md (flagship only)

```markdown
# Assurance Evidence

## Assurance Framework
Regulatory/certification regime and review progression.

## Evidence Lifecycle States

| State     | Meaning                                  |
|-----------|------------------------------------------|
| Planned   | Artifact identified, not yet started     |
| Drafted   | Initial content exists                   |
| Reviewed  | Peer or independent review completed     |
| Approved  | Authority or designated reviewer accepted|
| Baselined | Under configuration control              |

## Evidence Index

| EVD ID | Artifact Name | Demonstrates | Standard Clause | Review Milestone | Evidence Consumer | Status |

- Review Milestone: which gate this evidence supports
- Evidence Consumer: who reviews/accepts this evidence

## Domain-Specific Evidence Mapping

### Aerospace
SOI progression checklist, DO-178C Table A objective-to-evidence mapping,
DO-254 evidence, DO-326A security evidence, DO-330 tool qualification.

### Defense
DI-SESS CDRL mapping, technical review gate evidence (SRR/PDR/CDR/TRR),
T&E master plan traceability, MIL-STD-882E risk acceptance chain.

### Automotive
ISO 26262 work product mapping by part and ASIL, safety case structure,
confirmation measures, homologation evidence.

### Medical Device
FDA design control mapping (input/output/verification/validation/transfer),
DHF index, EU MDR Annex II/III structure, IEC 62304 evidence by class.

### Electronic Systems
DO-254 evidence by DAL, IEC 61508 SIL mapping, formal verification
coverage metrics, EDA tool qualification, HW/SW interface evidence.
```

### dodaf-views.md (defense flagship only)

```markdown
# DoDAF / UAF Architecture Views

## Viewpoint Selection Rationale
Which viewpoints, why selected, which review gates consume them.

## Operational Viewpoint (OV)

### OV-1: High-Level Operational Concept
Diagram: operational nodes, activities, information exchanges.

### OV-5b: Operational Activity Model
| Activity ID | Activity Name | Input(s) | Output(s) | Performer | REQ ID(s) |

## Systems Viewpoint (SV)

### SV-1: Systems Interface Description
| System Node | CMP ID | Interface Partner | IFC ID | Data Item | Protocol |

### SV-4: Systems Functionality Description
Function-to-system allocation referencing architecture.md.

## Data and Information Viewpoint (DIV)

### DIV-2: Logical Data Model

## View-to-Deliverable Mapping
| View | DI-SESS CDRL | Review Gate | Consumer |

## Traceability to Architecture
| DoDAF Element | architecture.md Entity | ID |
```

### cybersecurity.md (aerospace + automotive flagships)

```markdown
# Cybersecurity Analysis

## Applicable Framework
- Aerospace: DO-326A / DO-356A
- Automotive: ISO/SAE 21434

## Asset Identification
| Asset ID | Asset Name | CMP ID | C | I | A | Safety Relevance (HZ ID) |

## Threat Analysis

### Aerospace (DO-326A)
| Threat ID | Threat Condition | Attack Vector | Asset ID(s) | Security Risk | HZ ID(s) |

### Automotive (ISO 21434 TARA)
| Threat ID | Threat Scenario | Attack Path | Asset ID(s) | Feasibility | Impact | Risk | HZ ID(s) |

## Security Requirements
| REQ-SEC-xxx | Statement | Threat ID(s) | CTL ID(s) | Verification |

Must also appear in requirements.md with source = Threat ID.

## Security-Safety Interaction
| Threat ID | Attack Consequence | HZ ID | Combined Risk | Mitigation Strategy |
```

## Agent Integration

### Existing Agents (4 updates)

Each agent file gets a new `## Reference Systems` section (~30-50 lines):

```markdown
## Reference Systems

This agent has domain knowledge grounded in the following example
systems. Each demonstrates real artifact structure, ID conventions,
and cross-file traceability.

### Flagship
- **[{Name}](../../examples/{domain}/{dir}/)** — {one-line description}.
  Full artifact set: system definition, requirements, architecture,
  hazard analysis, traceability, assurance evidence.

### Fleet
- **[{Name}](../../examples/{domain}/{dir}/)** — {one-line description}.
  Core artifacts: system definition, requirements, architecture.
- ...

### How to Use These Examples
- When asked about artifact structure, reference the applicable
  example file as a concrete illustration.
- When asked about traceability, walk the ID chain through the
  flagship files.
- When helping a user build their own system, use the example as
  a starting template adapted to their context.
- Always frame as "the reference {system} example shows..." rather
  than presenting example content as the user's system.
```

### New Agent: Electronic Systems Engineer

~600 lines following the pattern of the existing 4 agents:

- **Domain**: ASIC/FPGA/SoC design, hardware verification, safety-critical electronics, quantum computing hardware
- **Standards**: DO-254, IEC 61508, IEC 61131, AEC-Q100, IEEE 1076/1364/1800 (VHDL/Verilog/SystemVerilog)
- **Methodologies**: UVM, formal verification, coverage-driven verification, equivalence checking
- **EDA Toolchains**: Cadence (Genus, Innovus, Xcelium, JasperGold), Synopsys (Design Compiler, VCS, Formality), Siemens EDA (Questa, Calibre)
- **MBSE Crosswalk**: Mapping electronic design artifacts to SysML/Capella/Cameo model elements
- **Quantum section**: Emerging standards landscape, qubit control architecture, error correction verification
- **Reviewer attack surfaces**: What assessors challenge in electronic systems certification

### README.md Updates

The project README.md gets a new section pointing to the examples gallery, and the badge count updates to reflect 5 agents.

## Deliverable Summary

| Deliverable | Count | Depth |
|-------------|-------|-------|
| Flagship systems (7-8 files each) | 5 | Full artifact set with cross-file traceability |
| Fleet systems (4 files each) | 15 | Core: system.yaml, README, requirements, architecture |
| New agent: Electronic Systems Engineer | 1 | ~600 lines |
| Agent updates (reference systems section) | 4 | ~30-50 lines each |
| Gallery index | 1 | Generated from system.yaml |
| Domain indexes | 5 | Domain context + system table |
| README.md update | 1 | New section + badge update |

Total new files: ~105
Total new agent file: 1
Total agent file updates: 4
