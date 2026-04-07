# Examples Gallery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create 20 reference system examples across 5 MBSE domains (5 flagships, 15 fleet) with a new Electronic Systems Engineer agent, agent integration, and gallery indexes.

**Architecture:** Each domain is an independent workstream. Flagships are written first (establish IDs and patterns), fleet systems second. A new agent file is written in parallel. Integration tasks (agent updates, indexes, README) depend on content being complete.

**Tech Stack:** Markdown, YAML. No code — pure documentation artifacts.

**Spec:** `docs/superpowers/specs/2026-04-07-examples-gallery-design.md`

---

## Dependency Graph

```
Task 1 (scaffold) ─┬─► Task 2 (aero flagship) ──► Task 3 (aero fleet) ───┐
                    ├─► Task 4 (defense flagship) ► Task 5 (defense fleet) ┤
                    ├─► Task 6 (auto flagship) ──► Task 7 (auto fleet) ────┤
                    ├─► Task 8 (medical flagship) ► Task 9 (medical fleet) ┤
                    ├─► Task 10 (elec flagship) ─► Task 11 (elec fleet) ───┤
                    └─► Task 12 (new agent) ───────────────────────────────┤
                                                                           │
                    Task 13 (agent updates) ◄──────────────────────────────┤
                    Task 14 (indexes) ◄────────────────────────────────────┤
                    Task 15 (README update) ◄──────────────────────────────┘
```

Tasks 2-12 can run in parallel after Task 1. Tasks 13-15 depend on all content being complete.

## Subagent Dispatch Strategy

Each domain flagship (Tasks 2, 4, 6, 8, 10) should use the matching specialist agent:
- Task 2: `subagent_type="Aerospace Systems Engineer"` (existing agent as domain expert)
- Task 4: general-purpose with defense agent context (no matching specialist agent type available)
- Task 6: general-purpose with automotive agent context (no matching specialist agent type available)
- Task 8: general-purpose with medical device agent context (no matching specialist agent type available)
- Task 10, 12: general-purpose with electronic systems spec context

All tasks receive the full spec file path and the artifact templates from the spec.

---

### Task 1: Create Directory Scaffold and system.yaml Files

**Files:**
- Create: 20 directories under `examples/`
- Create: 20 `system.yaml` files
- Create: 5 domain `README.md` placeholder files (will be populated in Task 14)
- Create: `examples/README.md` placeholder (will be populated in Task 14)

- [ ] **Step 1: Create all directories**

```bash
cd "/mnt/d/Coding Projects/MBSE"

# Aerospace
mkdir -p examples/aerospace/flight-management-system
mkdir -p examples/aerospace/cubesat-constellation
mkdir -p examples/aerospace/eva-suit-life-support
mkdir -p examples/aerospace/launch-vehicle-avionics

# Defense
mkdir -p examples/defense/uas-ground-control-station
mkdir -p examples/defense/ballistic-missile-defense
mkdir -p examples/defense/tactical-sdr-radio
mkdir -p examples/defense/naval-combat-management

# Automotive
mkdir -p examples/automotive/autonomous-emergency-braking
mkdir -p examples/automotive/ev-battery-management
mkdir -p examples/automotive/steer-by-wire
mkdir -p examples/automotive/v2x-communication

# Medical Device
mkdir -p examples/medical-device/smart-infusion-pump
mkdir -p examples/medical-device/surgical-robot-platform
mkdir -p examples/medical-device/continuous-glucose-monitor
mkdir -p examples/medical-device/patient-monitoring-network

# Electronic Systems
mkdir -p examples/electronic-systems/quantum-processor-control
mkdir -p examples/electronic-systems/safety-critical-soc
mkdir -p examples/electronic-systems/fpga-radar-signal-processor
mkdir -p examples/electronic-systems/hpc-cluster-orchestration
```

- [ ] **Step 2: Create all system.yaml files**

Write each file using the Write tool. Each system.yaml follows this exact schema:

```yaml
title: {from spec Example Systems table}
domain: {aerospace|defense|automotive|medical-device|electronic-systems}
tier: {flagship|fleet}
status: draft
standards:
  - {extracted from spec description}
assurance_framework: {one-line from spec}
system_class: {from spec}
summary: >
  {2-3 sentences from spec description column}
```

**Aerospace system.yaml files:**

`examples/aerospace/flight-management-system/system.yaml`:
```yaml
title: Integrated Flight Management System
domain: aerospace
tier: flagship
status: draft
standards:
  - ARP4754A
  - ARP4761A
  - DO-178C
  - DO-254
  - DO-326A
  - DO-330
  - DO-331
assurance_framework: FAA development assurance (SOI #1 through SOI #4)
system_class: DAL A airborne system
summary: >
  Multi-channel FMS with flight planning, navigation, and performance
  computation functions. Dual FMC architecture with dissimilar backup.
  DAL A software (DO-178C), DAL A programmable hardware (DO-254),
  cybersecurity assessment (DO-326A).
```

`examples/aerospace/cubesat-constellation/system.yaml`:
```yaml
title: CubeSat Constellation
domain: aerospace
tier: fleet
status: draft
standards:
  - NPR 7123.1
  - CCSDS
  - NASA-STD-8739.8
assurance_framework: NASA mission assurance (Class C)
system_class: Class C mission
summary: >
  12-unit LEO constellation for Earth observation with intersatellite
  links. NASA NPR 7123.1 tailored for Class C mission assurance.
  CCSDS communication protocols.
```

`examples/aerospace/eva-suit-life-support/system.yaml`:
```yaml
title: EVA Suit Life Support System
domain: aerospace
tier: fleet
status: draft
standards:
  - NPR 7123.1
  - NPR 8705.2
  - NASA-STD-5005
  - NASA-STD-5019
assurance_framework: NASA human-rating (NPR 8705.2)
system_class: Human-rated life-critical
summary: >
  Extravehicular activity portable life support system for ISS and
  Artemis missions. Pressure regulation, O2/CO2 management, thermal
  control. NASA-STD-5005 fracture control.
```

`examples/aerospace/launch-vehicle-avionics/system.yaml`:
```yaml
title: Launch Vehicle Avionics
domain: aerospace
tier: fleet
status: draft
standards:
  - EWR 127-1
  - DO-178C
  - NASA-STD-8719.24
  - RCC 319
assurance_framework: Range safety (EWR 127-1) + DO-178C Level A (FTS)
system_class: DAL A (FTS), DAL C (GN&C)
summary: >
  Upper stage avionics for medium-lift launch vehicle. Flight
  termination system (FTS), guidance/navigation/control, telemetry.
  Range safety per EWR 127-1.
```

**Defense system.yaml files:**

`examples/defense/uas-ground-control-station/system.yaml`:
```yaml
title: UAS Ground Control Station
domain: defense
tier: flagship
status: draft
standards:
  - DoDAF 2.02
  - MIL-STD-882E
  - MIL-STD-1553
  - DI-SESS-81785A
  - FACE 3.1
  - MOSA
assurance_framework: DoD acquisition (ACAT II) with DAES review
system_class: ACAT II, SIL 4 (safety-critical functions)
summary: >
  Multi-vehicle ground control station for Group 4/5 UAS. C2 link
  management, mission planning, sensor payload control, airspace
  integration. MOSA/FACE compliant open architecture.
```

`examples/defense/ballistic-missile-defense/system.yaml`:
```yaml
title: Ballistic Missile Defense Element
domain: defense
tier: fleet
status: draft
standards:
  - DoDAF 2.02
  - MIL-STD-882E
  - MIL-STD-3022
assurance_framework: MDA acquisition oversight (ACAT ID)
system_class: ACAT ID system-of-systems
summary: >
  Engagement coordination element within layered BMDS architecture.
  Track management, threat assessment, weapon-target pairing.
```

`examples/defense/tactical-sdr-radio/system.yaml`:
```yaml
title: Tactical SDR Radio
domain: defense
tier: fleet
status: draft
standards:
  - SCA 4.1
  - FACE 3.1
  - MIL-STD-882E
  - NSA CNSS
assurance_framework: NSA Type 1 certification + SCA conformance
system_class: NSA Type 1, FACE conformant
summary: >
  Software-defined radio for JTRS waveform hosting. Multi-channel
  MANET, COMSEC/TRANSEC, NSA Type 1. SCA 4.1 compliant with FACE
  transport/platform profiles.
```

`examples/defense/naval-combat-management/system.yaml`:
```yaml
title: Naval Combat Management System
domain: defense
tier: fleet
status: draft
standards:
  - DoDAF 2.02
  - MIL-STD-882E
  - MIL-STD-1553
  - MIL-STD-3022
assurance_framework: Navy PEO IWS acquisition
system_class: ACAT I, mission-critical
summary: >
  Surface combatant CMS integrating sensors, weapons, and C2. Track
  fusion, engagement planning, cooperative engagement capability.
  MIL-STD-1553/VME to GigE modernization path.
```

**Automotive system.yaml files:**

`examples/automotive/autonomous-emergency-braking/system.yaml`:
```yaml
title: Autonomous Emergency Braking System
domain: automotive
tier: flagship
status: draft
standards:
  - ISO 26262
  - ISO 21448
  - ISO 21434
  - AUTOSAR Classic 4.4
  - AUTOSAR Adaptive R22-11
  - UN R152
assurance_framework: ISO 26262 safety lifecycle (ASIL D) + third-party assessment
system_class: ASIL D
summary: >
  Camera + radar fusion AEB for passenger vehicles. ASIL D safety
  case, SOTIF analysis for perception limitations, ISO 21434
  cybersecurity TARA. AUTOSAR Classic/Adaptive split architecture.
```

`examples/automotive/ev-battery-management/system.yaml`:
```yaml
title: EV Battery Management System
domain: automotive
tier: fleet
status: draft
standards:
  - ISO 26262
  - UN R100
  - IEC 62619
  - ISO 6469
assurance_framework: ISO 26262 safety lifecycle (ASIL C/D)
system_class: ASIL D (contactor control), ASIL C (monitoring)
summary: >
  High-voltage lithium-ion BMS for 800V architecture. Cell monitoring,
  thermal management, state estimation (SoC/SoH), contactor control.
```

`examples/automotive/steer-by-wire/system.yaml`:
```yaml
title: Steer-by-Wire System
domain: automotive
tier: fleet
status: draft
standards:
  - ISO 26262
  - ISO 21448
  - UN R79
assurance_framework: ISO 26262 safety lifecycle (ASIL D, fail-operational)
system_class: ASIL D, fail-operational
summary: >
  Full steer-by-wire with no mechanical fallback. Dual-redundant
  steering actuators, torque feedback, rack position control.
  Fail-operational architecture.
```

`examples/automotive/v2x-communication/system.yaml`:
```yaml
title: V2X Communication Unit
domain: automotive
tier: fleet
status: draft
standards:
  - ISO 21434
  - ISO 21448
  - ETSI ITS-G5
  - SAE J3161
  - IEEE 802.11p
assurance_framework: ISO 21434 cybersecurity lifecycle + SOTIF
system_class: QM (communication), ASIL B (safety-relevant messaging)
summary: >
  C-V2X (PC5 + Uu) on-board unit for cooperative perception and
  platooning. ETSI ITS-G5 / SAE J3161 compliant.
```

**Medical Device system.yaml files:**

`examples/medical-device/smart-infusion-pump/system.yaml`:
```yaml
title: Smart Infusion Pump System
domain: medical-device
tier: flagship
status: draft
standards:
  - IEC 62304
  - ISO 14971
  - IEC 60601-1
  - IEC 60601-2-24
  - FDA QMSR
  - EU MDR 2017/745
assurance_framework: FDA premarket (PMA Class III) + EU MDR (Class IIb, Notified Body)
system_class: FDA Class III, EU MDR Class IIb, IEC 62304 Class C
summary: >
  Large-volume infusion pump with dose error reduction software (DERS).
  Drug library, wireless connectivity, EHR integration. IEC 62304
  Class C software with ISO 14971 risk management.
```

`examples/medical-device/surgical-robot-platform/system.yaml`:
```yaml
title: Surgical Robot Platform
domain: medical-device
tier: fleet
status: draft
standards:
  - IEC 62304
  - ISO 14971
  - IEC 60601-1
  - IEC 80601-2-77
  - IEC 62443
assurance_framework: FDA De Novo (Class II) + EU MDR (Class IIb)
system_class: FDA Class II (De Novo), IEC 62304 Class C
summary: >
  Multi-arm teleoperated surgical system for minimally invasive
  procedures. Master-slave architecture, haptic feedback, vision system.
```

`examples/medical-device/continuous-glucose-monitor/system.yaml`:
```yaml
title: Continuous Glucose Monitor
domain: medical-device
tier: fleet
status: draft
standards:
  - IEC 62304
  - ISO 14971
  - IEC 62366-1
  - IMDRF SaMD N41
  - FDA SaMD guidance
assurance_framework: FDA 510(k) (Class II) + EU MDR (Class IIb)
system_class: FDA Class II, IEC 62304 Class B/A (SaMD component)
summary: >
  Wearable CGM with mobile app and cloud analytics. SaMD component
  for trend prediction and insulin dosing guidance.
```

`examples/medical-device/patient-monitoring-network/system.yaml`:
```yaml
title: Patient Monitoring Network
domain: medical-device
tier: fleet
status: draft
standards:
  - IEC 62304
  - ISO 14971
  - IEC 60601-1
  - IEC 60601-1-8
  - IEC 80001-1
assurance_framework: FDA 510(k) (Class II) + EU MDR (Class IIa)
system_class: FDA Class II, IEC 62304 Class B
summary: >
  Multi-parameter bedside monitoring with central station aggregation.
  SpO2, ECG, NIBP, temperature, capnography. IEC 60601-1-8 alarm
  management.
```

**Electronic Systems system.yaml files:**

`examples/electronic-systems/quantum-processor-control/system.yaml`:
```yaml
title: Quantum Processor Control System
domain: electronic-systems
tier: flagship
status: draft
standards:
  - IEC 61508
  - IEEE 1076
  - IEEE 1800
assurance_framework: IEC 61508 (safety-critical calibration) + formal verification
system_class: SIL 2 (safety-critical calibration subsystem)
summary: >
  Cryogenic control electronics and room-temperature orchestration
  stack for a 100+ qubit superconducting quantum processor. RF pulse
  generation, qubit readout, error correction feedback loop,
  calibration automation.
```

`examples/electronic-systems/safety-critical-soc/system.yaml`:
```yaml
title: Safety-Critical SoC
domain: electronic-systems
tier: fleet
status: draft
standards:
  - ISO 26262-11
  - AEC-Q100
  - IEC 61508
assurance_framework: ISO 26262-11 (semiconductor) + AEC-Q100 qualification
system_class: ASIL D (random HW fault metrics)
summary: >
  Automotive-grade SoC for ADAS compute. Lockstep CPU cores, hardware
  safety mechanisms (BIST, ECC, watchdog). ASIL D random hardware
  fault metrics per ISO 26262-11.
```

`examples/electronic-systems/fpga-radar-signal-processor/system.yaml`:
```yaml
title: FPGA Radar Signal Processor
domain: electronic-systems
tier: fleet
status: draft
standards:
  - DO-254
  - MIL-STD-882E
  - MIL-HDBK-217
assurance_framework: DO-254 DAL B + MIL-STD-882E safety
system_class: DO-254 DAL B
summary: >
  FPGA-based real-time signal processor for phased array radar. Pulse
  compression, Doppler processing, CFAR detection, track-before-detect.
```

`examples/electronic-systems/hpc-cluster-orchestration/system.yaml`:
```yaml
title: HPC Cluster Orchestration System
domain: electronic-systems
tier: fleet
status: draft
standards:
  - IEC 61508
  - ALCOA+
assurance_framework: IEC 61508 SIL 1 (safety-critical batch processes)
system_class: SIL 1
summary: >
  Workload orchestration for a 500-node GPU compute cluster. Job
  scheduling, resource allocation, fault recovery, power management.
  Data integrity per ALCOA+ principles.
```

- [ ] **Step 3: Create placeholder index files**

Create minimal placeholder files that will be fully populated in Task 14:

`examples/README.md`:
```markdown
# Example Systems Gallery

> This index will be populated after all example systems are complete.
```

One per domain (`examples/{domain}/README.md`):
```markdown
# {Domain} Examples

> This index will be populated after all example systems are complete.
```

- [ ] **Step 4: Commit scaffold**

```bash
git add examples/
git commit -m "feat: scaffold examples gallery directories and system.yaml files"
```

---

### Task 2: Aerospace Flagship — Integrated Flight Management System

**Files:**
- Create: `examples/aerospace/flight-management-system/README.md`
- Create: `examples/aerospace/flight-management-system/requirements.md`
- Create: `examples/aerospace/flight-management-system/architecture.md`
- Create: `examples/aerospace/flight-management-system/hazard-analysis.md`
- Create: `examples/aerospace/flight-management-system/traceability.md`
- Create: `examples/aerospace/flight-management-system/assurance-evidence.md`
- Create: `examples/aerospace/flight-management-system/cybersecurity.md`

**Dispatch:** Use `subagent_type="Aerospace Systems Engineer"` for domain expertise.

**Context for subagent:** You are writing the flagship reference system for the aerospace domain. Read the full design spec at `docs/superpowers/specs/2026-04-07-examples-gallery-design.md` for artifact templates, ID taxonomy, and cross-file integrity rules. Read `examples/aerospace/flight-management-system/system.yaml` for system metadata. Read the existing aerospace agent at `agents/aerospace-systems-engineer.md` for domain knowledge and tone.

**Quality criteria:**
- README.md: 200-400 word overview, system boundary, 4-5 operating modes (MODE-001 through MODE-005), 4-5 key technical challenges, stakeholders, standards applicability with rationale
- requirements.md: 30-50 requirements using the uniform record schema (ID, Statement, Rationale, Source, Parent, Verification, Allocation, Status). Must include functional (REQ-FUN-), safety (REQ-SAF-), security (REQ-SEC-), interface (REQ-IFC-), and performance (REQ-PRF-) categories. Safety requirement sources must be HZ-xxx or CTL-xxx IDs. Security requirement sources must be THR-xxx IDs.
- architecture.md: System context, functional architecture with FUN- IDs, physical architecture with CMP- IDs, allocation table (FUN ID → REQ IDs → CMP ID → DAL), external interfaces (IFC-EXT-) and internal interfaces (IFC-INT-), failure containment/partitioning (ARINC 653, dissimilar redundancy), 3-5 architecture decisions
- hazard-analysis.md: ARP4761A methodology, aerospace terminology table, 3-5 assumptions (ASM-), 8-12 hazards (HZ-) with failure condition classification (catastrophic through NSE), initial and residual risk, risk controls (CTL-), at least one worked fault tree in mermaid, PSSA/SSA section
- traceability.md: Forward traces (req→arch, req→hazard, req→verification), reverse traces (component→req, hazard→control→req, verification→req), gap register with explicit gaps, coverage summary with real numbers matching the requirements and hazards
- assurance-evidence.md: FAA SOI framework, evidence lifecycle states, evidence index (EVD-) with Location column, SOI progression checklist, DO-178C Table A mapping for DAL A, DO-254 evidence, DO-326A evidence, DO-330 tool qualification
- cybersecurity.md: DO-326A framework, assets (AST-) mapped to CMP- IDs, threats (THR-) with attack vectors, security requirements (REQ-SEC-) cross-referenced to requirements.md, security-safety interaction table linking THR- to HZ- IDs

**Cross-file integrity:** After writing all files, verify:
- Every HZ- has at least one CTL- or acceptability rationale
- Every CTL- maps to at least one REQ-
- Every REQ-SAF- and REQ-SEC- maps to at least one CMP- and one VER-
- Every VER- maps to at least one EVD-
- IDs used across files match (no typos, no orphans except in gap register)

- [ ] **Step 1: Write README.md** — system identity, boundary, modes, challenges, stakeholders, standards
- [ ] **Step 2: Write architecture.md** — establishes FUN-, CMP-, IFC- IDs that other files reference
- [ ] **Step 3: Write requirements.md** — references CMP- IDs in allocation column, will reference HZ-/CTL-/THR- IDs in source column (use planned IDs)
- [ ] **Step 4: Write hazard-analysis.md** — establishes HZ-, CTL- IDs, references MODE- and REQ- IDs
- [ ] **Step 5: Write cybersecurity.md** — establishes AST-, THR- IDs, references CMP- and HZ- IDs
- [ ] **Step 6: Backfill requirements.md** — update safety/security requirement sources with actual HZ-/CTL-/THR- IDs from steps 4-5
- [ ] **Step 7: Write traceability.md** — references all IDs from all other files
- [ ] **Step 8: Write assurance-evidence.md** — references VER- IDs from traceability.md
- [ ] **Step 9: Cross-file integrity check** — grep for every ID prefix across all 7 files, verify no orphans except in gap register
- [ ] **Step 10: Commit**

```bash
git add examples/aerospace/flight-management-system/
git commit -m "feat: add aerospace flagship — Integrated Flight Management System"
```

---

### Task 3: Aerospace Fleet Systems

**Files:**
- Create: 3 files each for `cubesat-constellation/`, `eva-suit-life-support/`, `launch-vehicle-avionics/`

**Dispatch:** Use `subagent_type="Aerospace Systems Engineer"`.

**Context for subagent:** You are writing 3 fleet-tier reference systems for the aerospace domain. Read the spec at `docs/superpowers/specs/2026-04-07-examples-gallery-design.md` for templates. Read the flagship at `examples/aerospace/flight-management-system/` for the established pattern and tone. Read each system's `system.yaml` for metadata.

**Quality criteria per fleet system:**
- README.md: 100-150 word overview, system boundary, 3-4 operating modes (MODE-), key technical challenges, stakeholders, standards applicability
- requirements.md: 8-12 requirements using uniform record schema. At least functional + safety categories. Sources can reference regulatory clauses (fleet systems don't have hazard-analysis.md).
- architecture.md: System context, functional architecture with FUN- IDs, physical architecture with CMP- IDs, allocation table, key external and internal interfaces (IFC-), failure containment/partitioning summary, 2-3 architecture decisions

**CubeSat Constellation** — emphasize constellation-level vs spacecraft-level boundary, intersatellite link interfaces, NASA Class C tailoring rationale, CCSDS protocol stack.

**EVA Suit Life Support** — emphasize human-rating requirements, life-critical failure modes, pressure/thermal/O2 management architecture, crew abort as operating mode.

**Launch Vehicle Avionics** — emphasize FTS safety (DAL A) vs GN&C (DAL C) split, range safety requirements, flight termination as operating mode, DO-178C applicability for FTS software.

- [ ] **Step 1: Write CubeSat Constellation files** (README.md, requirements.md, architecture.md)
- [ ] **Step 2: Write EVA Suit Life Support files** (README.md, requirements.md, architecture.md)
- [ ] **Step 3: Write Launch Vehicle Avionics files** (README.md, requirements.md, architecture.md)
- [ ] **Step 4: Verify ID consistency** — each system uses unique IDs, no collisions
- [ ] **Step 5: Commit**

```bash
git add examples/aerospace/cubesat-constellation/ examples/aerospace/eva-suit-life-support/ examples/aerospace/launch-vehicle-avionics/
git commit -m "feat: add aerospace fleet systems — CubeSat, EVA suit, launch vehicle"
```

---

### Task 4: Defense Flagship — UAS Ground Control Station

**Files:**
- Create: 7 files in `examples/defense/uas-ground-control-station/`
  - README.md, requirements.md, architecture.md, hazard-analysis.md, traceability.md, assurance-evidence.md, dodaf-views.md

**Dispatch:** general-purpose agent with defense SE spec context.

**Context for subagent:** You are writing the flagship reference system for the defense domain. Read the spec at `docs/superpowers/specs/2026-04-07-examples-gallery-design.md`. Read the defense agent at `agents/defense-systems-engineer.md` for domain knowledge, tone, and standards depth. Read `examples/defense/uas-ground-control-station/system.yaml` for metadata. Follow the same cross-file integrity rules as the aerospace flagship (Task 2).

**Quality criteria:** Same structure as Task 2, with these defense-specific differences:
- hazard-analysis.md: MIL-STD-882E methodology, hazard severity (I-IV) × probability (A-E) matrix, risk acceptance authority chain (PM → PEO → DASD), mishap terminology
- assurance-evidence.md: DI-SESS CDRL mapping, technical review gates (SRR/PDR/CDR/TRR), T&E master plan
- dodaf-views.md: OV-1 (operational concept in mermaid), OV-5b (operational activity model with REQ- traces), SV-1 (system interfaces with CMP-/IFC- traces), SV-4 (function allocation), DIV-2 (logical data model), view-to-deliverable mapping (CDRL numbers), traceability to architecture.md entities
- requirements.md: 30-50 requirements. No security requirements section (defense handles security through classification/COMSEC, not a separate cybersecurity artifact).

- [ ] **Step 1: Write README.md**
- [ ] **Step 2: Write architecture.md** — MOSA/FACE layered architecture, CMP- and IFC- IDs
- [ ] **Step 3: Write requirements.md** — references architecture CMP- IDs
- [ ] **Step 4: Write hazard-analysis.md** — MIL-STD-882E, HZ- and CTL- IDs
- [ ] **Step 5: Write dodaf-views.md** — references FUN-, CMP-, IFC-, REQ- IDs from other files
- [ ] **Step 6: Backfill requirements.md** — update safety requirement sources with HZ-/CTL- IDs
- [ ] **Step 7: Write traceability.md**
- [ ] **Step 8: Write assurance-evidence.md**
- [ ] **Step 9: Cross-file integrity check**
- [ ] **Step 10: Commit**

```bash
git add examples/defense/uas-ground-control-station/
git commit -m "feat: add defense flagship — UAS Ground Control Station"
```

---

### Task 5: Defense Fleet Systems

**Files:**
- Create: 3 files each for `ballistic-missile-defense/`, `tactical-sdr-radio/`, `naval-combat-management/`

**Dispatch:** general-purpose with defense agent context.

**Context for subagent:** Read spec, read defense agent, read defense flagship for pattern. Read each system's `system.yaml`.

**System-specific emphasis:**
- **Ballistic Missile Defense**: SoS architecture boundary, engagement coordination vs interceptor boundary, ACAT ID oversight, MDA-specific review gates
- **Tactical SDR Radio**: SCA 4.1 architecture (waveform/platform), FACE profiles, COMSEC/TRANSEC boundary, NSA certification modes
- **Naval Combat Management**: Sensor-to-weapon kill chain, cooperative engagement, MIL-STD-1553 legacy interfaces, modernization architecture decisions

- [ ] **Step 1: Write Ballistic Missile Defense files**
- [ ] **Step 2: Write Tactical SDR Radio files**
- [ ] **Step 3: Write Naval Combat Management files**
- [ ] **Step 4: Verify ID consistency**
- [ ] **Step 5: Commit**

```bash
git add examples/defense/ballistic-missile-defense/ examples/defense/tactical-sdr-radio/ examples/defense/naval-combat-management/
git commit -m "feat: add defense fleet systems — BMD, SDR radio, naval CMS"
```

---

### Task 6: Automotive Flagship — Autonomous Emergency Braking

**Files:**
- Create: 7 files in `examples/automotive/autonomous-emergency-braking/`
  - README.md, requirements.md, architecture.md, hazard-analysis.md, traceability.md, assurance-evidence.md, cybersecurity.md

**Dispatch:** general-purpose with automotive agent context.

**Context for subagent:** Read spec, read automotive agent at `agents/automotive-systems-engineer.md`, read `system.yaml`.

**Quality criteria:** Same cross-file structure, with these automotive-specific differences:
- hazard-analysis.md: ISO 26262-3 HARA methodology, hazardous event classification (severity S0-S3 × exposure E0-E4 × controllability C0-C3 → ASIL QM/A/B/C/D), safety goals derived from hazardous events, ASIL decomposition rationale for redundant paths
- cybersecurity.md: ISO/SAE 21434 TARA methodology, attack feasibility rating (elapsed time, specialist expertise, knowledge, window of opportunity, equipment), security-safety interaction for sensor spoofing and CAN bus attacks
- assurance-evidence.md: ISO 26262 work product mapping by part (Part 3-11), safety case structure (GSN notation), confirmation measures (verification review, FSA, FS audit), homologation evidence outline
- requirements.md: Include SOTIF-related requirements (ISO 21448) alongside safety requirements

- [ ] **Step 1: Write README.md**
- [ ] **Step 2: Write architecture.md** — AUTOSAR Classic (braking ECU) + Adaptive (sensor fusion) split
- [ ] **Step 3: Write requirements.md**
- [ ] **Step 4: Write hazard-analysis.md** — HARA with ASIL determination
- [ ] **Step 5: Write cybersecurity.md** — TARA for sensor/CAN attack surfaces
- [ ] **Step 6: Backfill requirements.md** — HZ-/CTL-/THR- sources
- [ ] **Step 7: Write traceability.md**
- [ ] **Step 8: Write assurance-evidence.md**
- [ ] **Step 9: Cross-file integrity check**
- [ ] **Step 10: Commit**

```bash
git add examples/automotive/autonomous-emergency-braking/
git commit -m "feat: add automotive flagship — Autonomous Emergency Braking"
```

---

### Task 7: Automotive Fleet Systems

**Files:**
- Create: 3 files each for `ev-battery-management/`, `steer-by-wire/`, `v2x-communication/`

**Dispatch:** general-purpose with automotive agent context.

**System-specific emphasis:**
- **EV BMS**: 800V high-voltage boundary, cell-to-pack architecture, thermal runaway as hazard, ASIL decomposition between monitoring (C) and contactor control (D), UN R100 crash safety
- **Steer-by-Wire**: Fail-operational vs fail-safe distinction, dual-redundant actuator architecture, no mechanical fallback mode, ASIL D with freedom-from-interference argument, UN R79 steering requirements
- **V2X Communication**: QM (communication) vs ASIL B (safety messages) split, V2X message authentication, SOTIF for cooperative perception, C-V2X PC5 vs Uu mode architecture

- [ ] **Step 1: Write EV Battery Management files**
- [ ] **Step 2: Write Steer-by-Wire files**
- [ ] **Step 3: Write V2X Communication files**
- [ ] **Step 4: Verify ID consistency**
- [ ] **Step 5: Commit**

```bash
git add examples/automotive/ev-battery-management/ examples/automotive/steer-by-wire/ examples/automotive/v2x-communication/
git commit -m "feat: add automotive fleet systems — BMS, steer-by-wire, V2X"
```

---

### Task 8: Medical Device Flagship — Smart Infusion Pump

**Files:**
- Create: 6 files in `examples/medical-device/smart-infusion-pump/`
  - README.md, requirements.md, architecture.md, hazard-analysis.md, traceability.md, assurance-evidence.md

**Dispatch:** general-purpose with medical device agent context.

**Context for subagent:** Read spec, read medical device agent at `agents/medical-device-systems-engineer.md`, read `system.yaml`.

**Quality criteria:** Same cross-file structure, with these medical-specific differences:
- hazard-analysis.md: ISO 14971 risk management methodology (this file IS the risk management file), hazardous situation → harm chain terminology, risk estimation (severity × probability), risk evaluation against acceptability matrix, risk-benefit analysis section, overall residual risk evaluation, risk controls mapped to IEC 62304 software safety classification
- assurance-evidence.md: FDA design control waterfall (design input → output → verification → validation → transfer), Design History File (DHF) index, EU MDR Annex II/III technical documentation structure, IEC 62304 software lifecycle evidence by safety class (A/B/C), post-market surveillance plan reference
- requirements.md: 30-50 requirements. No security requirements section (infusion pump cybersecurity handled through FDA premarket guidance, folded into safety requirements). Include IEC 60601-1 essential performance requirements and IEC 60601-2-24 infusion-specific requirements.

- [ ] **Step 1: Write README.md**
- [ ] **Step 2: Write architecture.md** — pump mechanism, DERS software, drug library, wireless/EHR interface
- [ ] **Step 3: Write requirements.md**
- [ ] **Step 4: Write hazard-analysis.md** — ISO 14971 full risk management
- [ ] **Step 5: Backfill requirements.md** — HZ-/CTL- sources
- [ ] **Step 6: Write traceability.md**
- [ ] **Step 7: Write assurance-evidence.md** — FDA design controls + EU MDR
- [ ] **Step 8: Cross-file integrity check**
- [ ] **Step 9: Commit**

```bash
git add examples/medical-device/smart-infusion-pump/
git commit -m "feat: add medical device flagship — Smart Infusion Pump"
```

---

### Task 9: Medical Device Fleet Systems

**Files:**
- Create: 3 files each for `surgical-robot-platform/`, `continuous-glucose-monitor/`, `patient-monitoring-network/`

**Dispatch:** general-purpose with medical device agent context.

**System-specific emphasis:**
- **Surgical Robot**: Master-slave teleoperation boundary, haptic feedback latency requirements, IEC 80601-2-77 surgical robot standard, De Novo classification rationale, mechanical + software + electrical failure modes
- **CGM**: SaMD classification (IMDRF N41), sensor vs display vs cloud analytics boundary, IEC 62304 Class B (sensor firmware) vs Class A (display app) split, interoperability with insulin pumps, cybersecurity for patient data
- **Patient Monitoring**: Multi-parameter alarm management (IEC 60601-1-8), central station aggregation architecture, IEC 80001-1 health IT network risk, bedside-to-central interface timing, alarm fatigue as a design challenge

- [ ] **Step 1: Write Surgical Robot Platform files**
- [ ] **Step 2: Write Continuous Glucose Monitor files**
- [ ] **Step 3: Write Patient Monitoring Network files**
- [ ] **Step 4: Verify ID consistency**
- [ ] **Step 5: Commit**

```bash
git add examples/medical-device/surgical-robot-platform/ examples/medical-device/continuous-glucose-monitor/ examples/medical-device/patient-monitoring-network/
git commit -m "feat: add medical device fleet systems — surgical robot, CGM, patient monitoring"
```

---

### Task 10: Electronic Systems Flagship — Quantum Processor Control

**Files:**
- Create: 6 files in `examples/electronic-systems/quantum-processor-control/`
  - README.md, requirements.md, architecture.md, hazard-analysis.md, traceability.md, assurance-evidence.md

**Dispatch:** general-purpose with electronic systems spec context.

**Context for subagent:** Read spec. This is a new domain without an existing agent file. Use the spec's Electronic Systems sections for guidance. The quantum processor control system bridges traditional electronic design (FPGA/ASIC for control electronics) with emerging quantum computing (qubit control, error correction).

**Quality criteria:** Same cross-file structure, with these electronic-specific differences:
- hazard-analysis.md: FMEA/FMECA methodology at component/gate level, failure mode → system effect mapping, detection coverage metrics, formal verification fault model, IEC 61508 where applicable to safety-critical calibration subsystem
- assurance-evidence.md: IEC 61508 SIL evidence mapping (for calibration subsystem), formal verification coverage metrics, EDA tool qualification argument, HW/SW interface evidence
- architecture.md: Cryogenic (4K) vs room-temperature boundary, RF pulse generation chain, qubit readout digitization, error correction feedback loop timing, calibration automation software, FPGA vs ASIC partitioning decisions
- requirements.md: 30-50 requirements. Include formal verification requirements, timing/jitter requirements for qubit control, calibration accuracy requirements tied to IEC 61508

- [ ] **Step 1: Write README.md** — quantum control system context, cryogenic/room-temp boundary
- [ ] **Step 2: Write architecture.md** — control electronics chain, FUN-/CMP-/IFC- IDs
- [ ] **Step 3: Write requirements.md**
- [ ] **Step 4: Write hazard-analysis.md** — FMEA approach, HZ-/CTL- IDs
- [ ] **Step 5: Backfill requirements.md** — HZ-/CTL- sources
- [ ] **Step 6: Write traceability.md**
- [ ] **Step 7: Write assurance-evidence.md**
- [ ] **Step 8: Cross-file integrity check**
- [ ] **Step 9: Commit**

```bash
git add examples/electronic-systems/quantum-processor-control/
git commit -m "feat: add electronic systems flagship — Quantum Processor Control"
```

---

### Task 11: Electronic Systems Fleet Systems

**Files:**
- Create: 3 files each for `safety-critical-soc/`, `fpga-radar-signal-processor/`, `hpc-cluster-orchestration/`

**Dispatch:** general-purpose with electronic systems spec context.

**System-specific emphasis:**
- **Safety-Critical SoC**: ISO 26262-11 semiconductor process, lockstep CPU architecture, hardware safety mechanisms (BIST, ECC, watchdog), ASIL D random HW fault metrics (SPFM, LFM, PMHF), AEC-Q100 qualification flow
- **FPGA Radar Signal Processor**: DO-254 DAL B lifecycle, FPGA design assurance (synthesis, P&R, timing closure), signal processing chain (pulse compression → Doppler → CFAR → detection), MIL-STD-882E for radar safety
- **HPC Cluster Orchestration**: IEC 61508 SIL 1 for safety-critical batch processes, job scheduling fault tolerance, GPU node failure recovery, power management safety, ALCOA+ data integrity for regulated workloads

- [ ] **Step 1: Write Safety-Critical SoC files**
- [ ] **Step 2: Write FPGA Radar Signal Processor files**
- [ ] **Step 3: Write HPC Cluster Orchestration files**
- [ ] **Step 4: Verify ID consistency**
- [ ] **Step 5: Commit**

```bash
git add examples/electronic-systems/safety-critical-soc/ examples/electronic-systems/fpga-radar-signal-processor/ examples/electronic-systems/hpc-cluster-orchestration/
git commit -m "feat: add electronic systems fleet — SoC, FPGA radar, HPC cluster"
```

---

### Task 12: New Agent — Electronic Systems Engineer

**Files:**
- Create: `agents/electronic-systems-engineer.md`

**Dispatch:** general-purpose, using existing agents as structural reference.

**Context for subagent:** Read the spec's "New Agent: Electronic Systems Engineer" section. Read all 4 existing agent files for structure, tone, and depth calibration: `agents/aerospace-systems-engineer.md`, `agents/defense-systems-engineer.md`, `agents/automotive-systems-engineer.md`, `agents/medical-device-systems-engineer.md`. Each is ~650 lines. The new agent must match that depth.

**Structure (match existing agents):**
1. YAML frontmatter: name, description, color, emoji, vibe, services, last_verified
2. `# Electronic Systems Engineer` — identity paragraph
3. `## Your Identity & Memory` — role, personality, memory, experience (4 bullet narratives)
4. `## Core Mission` — electronic design assurance deep dive:
   - DO-254 lifecycle (planning, design, verification, configuration management)
   - IEC 61508 systematic capability and random hardware integrity
   - Formal verification methodology (model checking, equivalence checking, property checking)
   - Coverage-driven verification (UVM, constrained random, functional coverage)
   - ASIC/FPGA/SoC design flow (RTL → synthesis → P&R → timing closure → signoff)
   - Quantum computing hardware (emerging section)
5. `## Multi-Tool Crosswalk Tables` — mapping electronic design artifacts to SysML/Capella/Cameo/Sparx/DOORS/MATLAB elements
6. `## Reviewer Attack Surfaces` — what DO-254 DERs, IEC 61508 assessors, and ISO 26262-11 auditors challenge
7. `## Critical Rules` — never conflate RTL simulation with formal proof, tool qualification boundaries for EDA tools, etc.
8. `## Technical Deliverables` — design assurance plan, verification plan, HW/SW interface document
9. `## Workflow` — review preparation steps
10. `## Reference Systems` — links to electronic-systems examples (from spec agent integration template)
11. `## Communication Style`
12. `## Success Metrics`
13. `## Learning & Memory`

- [ ] **Step 1: Read all 4 existing agent files** for structure and tone
- [ ] **Step 2: Write frontmatter and identity** (~lines 1-50)
- [ ] **Step 3: Write Core Mission** (~lines 50-350, deepest section)
- [ ] **Step 4: Write Multi-Tool Crosswalk Tables** (~lines 350-430)
- [ ] **Step 5: Write Reviewer Attack Surfaces** (~lines 430-490)
- [ ] **Step 6: Write remaining sections** (Critical Rules, Deliverables, Workflow, Reference Systems, Communication Style, Success Metrics, Learning & Memory, ~lines 490-650)
- [ ] **Step 7: Verify line count** — target ~650 lines, matching existing agents
- [ ] **Step 8: Commit**

```bash
git add agents/electronic-systems-engineer.md
git commit -m "feat: add Electronic Systems Engineer agent"
```

---

### Task 13: Agent Integration — Add Reference Systems Sections

**Files:**
- Modify: `agents/aerospace-systems-engineer.md`
- Modify: `agents/defense-systems-engineer.md`
- Modify: `agents/automotive-systems-engineer.md`
- Modify: `agents/medical-device-systems-engineer.md`
- Verify: `agents/electronic-systems-engineer.md` (should already have Reference Systems from Task 12)

**Depends on:** Tasks 2-12 (all content must exist for links to be valid)

**Context:** Add the `## Reference Systems` section to each existing agent file, using the template from the spec. Insert it before `## Communication Style` (which is the last behavioral section in each agent).

- [ ] **Step 1: Read each agent file** to find the insertion point (before `## Communication Style`)

- [ ] **Step 2: Add Reference Systems to aerospace agent**

Insert before `## Communication Style` in `agents/aerospace-systems-engineer.md`:

```markdown
## Reference Systems

This agent has domain knowledge grounded in the following example systems. Each demonstrates real artifact structure, ID conventions, and cross-file traceability.

### Flagship
- **[Integrated Flight Management System](../examples/aerospace/flight-management-system/)** — Dual FMC architecture, DAL A, DO-178C/DO-254/DO-326A. Full artifact set: system definition, requirements, architecture, hazard analysis, traceability, assurance evidence, cybersecurity.

### Fleet
- **[CubeSat Constellation](../examples/aerospace/cubesat-constellation/)** — 12-unit LEO constellation, NPR 7123.1 Class C. Core artifacts.
- **[EVA Suit Life Support](../examples/aerospace/eva-suit-life-support/)** — Portable life support for ISS/Artemis, human-rated. Core artifacts.
- **[Launch Vehicle Avionics](../examples/aerospace/launch-vehicle-avionics/)** — Upper stage avionics, FTS DAL A, range safety. Core artifacts.

### How to Use These Examples
- When asked about artifact structure, reference the applicable example file as a concrete illustration.
- When asked about traceability, walk the ID chain through the flagship system's files.
- When helping a user build their own system, use the example as a starting template adapted to their context.
- Always frame as "the reference FMS example shows..." rather than presenting example content as the user's system.
```

- [ ] **Step 3: Add Reference Systems to defense agent**

Same pattern, referencing defense systems (UAS GCS flagship, BMD/SDR/naval fleet).

- [ ] **Step 4: Add Reference Systems to automotive agent**

Same pattern, referencing automotive systems (AEB flagship, BMS/SbW/V2X fleet).

- [ ] **Step 5: Add Reference Systems to medical device agent**

Same pattern, referencing medical device systems (infusion pump flagship, surgical robot/CGM/patient monitoring fleet).

- [ ] **Step 6: Verify electronic systems agent** already has Reference Systems section from Task 12

- [ ] **Step 7: Verify all links** — confirm every `../examples/{domain}/{system}/` path resolves to an existing directory

```bash
cd "/mnt/d/Coding Projects/MBSE"
grep -roh '\.\./examples/[^ )]*' agents/*.md | while read path; do
  [ -d "$path" ] || echo "BROKEN: $path"
done
```

- [ ] **Step 8: Commit**

```bash
git add agents/
git commit -m "feat: add Reference Systems sections to all agent files"
```

---

### Task 14: Gallery Index and Domain Indexes

**Files:**
- Modify: `examples/README.md`
- Modify: `examples/aerospace/README.md`
- Modify: `examples/defense/README.md`
- Modify: `examples/automotive/README.md`
- Modify: `examples/medical-device/README.md`
- Modify: `examples/electronic-systems/README.md`

**Depends on:** Tasks 2-11 (all example content must exist)

- [ ] **Step 1: Write gallery index** (`examples/README.md`)

Content structure:
```markdown
# Example Systems Gallery

Reference architectures demonstrating real artifact structure for each
MBSE domain. Flagships include full traceability from hazard analysis
through assurance evidence. Fleet systems provide core artifacts
expandable over time.

## ID Conventions

All systems use a shared ID taxonomy:

| Prefix | Scope | Defined In |
|--------|-------|------------|
| MODE-  | Operating mode | README.md |
| FUN-   | System/subsystem function | architecture.md |
| REQ-   | Requirement | requirements.md |
| HZ-    | Hazard | hazard-analysis.md |
| CTL-   | Risk control | hazard-analysis.md |
| THR-   | Cybersecurity threat | cybersecurity.md |
| AST-   | Cybersecurity asset | cybersecurity.md |
| CMP-   | Component | architecture.md |
| IFC-   | Interface | architecture.md |
| VER-   | Verification activity | traceability.md |
| EVD-   | Evidence artifact | assurance-evidence.md |

## Cross-File Integrity

Every flagship maintains:
- Every HZ has ≥1 CTL or explicit acceptability rationale
- Every CTL maps to ≥1 REQ
- Every assurance-relevant REQ maps to ≥1 CMP and ≥1 VER
- Every VER maps to ≥1 EVD
- Every gap is an explicit row in traceability.md

## Systems

### Aerospace
{table generated from system.yaml files}

### Defense
{table}

### Automotive
{table}

### Medical Device
{table}

### Electronic Systems
{table}
```

Each domain table: `| System | Tier | Standards | Status |` with links to system directories.

- [ ] **Step 2: Write aerospace domain index** (`examples/aerospace/README.md`)

Domain context paragraph about what these systems demonstrate for aerospace SE. System table with links. Brief explanation of aerospace-specific artifact types (PSSA/SSA, SOI progression, DO-178C Table A).

- [ ] **Step 3: Write defense domain index**
- [ ] **Step 4: Write automotive domain index**
- [ ] **Step 5: Write medical device domain index**
- [ ] **Step 6: Write electronic systems domain index**
- [ ] **Step 7: Verify all internal links resolve**
- [ ] **Step 8: Commit**

```bash
git add examples/README.md examples/aerospace/README.md examples/defense/README.md examples/automotive/README.md examples/medical-device/README.md examples/electronic-systems/README.md
git commit -m "feat: add gallery index and domain indexes"
```

---

### Task 15: Project README.md Update

**Files:**
- Modify: `README.md`

**Depends on:** Tasks 12-14

- [ ] **Step 1: Read current README.md**

- [ ] **Step 2: Update badge counts**

Change:
```
![Agents](https://img.shields.io/badge/agents-4-blue?style=flat)
```
To:
```
![Agents](https://img.shields.io/badge/agents-5-blue?style=flat)
```

- [ ] **Step 3: Add Electronic Systems Engineer to Agents table**

Add row after Medical Device:
```markdown
| [Electronic Systems Engineer](agents/electronic-systems-engineer.md) | ASIC, FPGA, SoC, quantum | DO-254, IEC 61508, IEEE 1800, AEC-Q100 | 600+ |
```

- [ ] **Step 4: Add Examples Gallery section**

Insert after the Agents section (before "Supported MBSE Tools"):

```markdown
## Example Systems

Each agent is grounded in reference architectures with real artifact structure — requirements, architecture decomposition, hazard analysis, traceability matrices, and assurance evidence packages.

| Domain | Flagship | Fleet Systems |
|:-------|:---------|:--------------|
| Aerospace | [Integrated FMS](examples/aerospace/flight-management-system/) | CubeSat constellation, EVA suit life support, launch vehicle avionics |
| Defense | [UAS Ground Control Station](examples/defense/uas-ground-control-station/) | Ballistic missile defense, tactical SDR radio, naval combat management |
| Automotive | [Autonomous Emergency Braking](examples/automotive/autonomous-emergency-braking/) | EV battery management, steer-by-wire, V2X communication |
| Medical Device | [Smart Infusion Pump](examples/medical-device/smart-infusion-pump/) | Surgical robot, continuous glucose monitor, patient monitoring |
| Electronic Systems | [Quantum Processor Control](examples/electronic-systems/quantum-processor-control/) | Safety-critical SoC, FPGA radar signal processor, HPC cluster |

Full gallery: [examples/](examples/)
```

- [ ] **Step 5: Update "Wanted agents" in Contributing section**

Remove "Nuclear, naval, space, railway, industrial control systems" if electronic systems is now covered. Update to reflect remaining gaps.

- [ ] **Step 6: Verify all links**

```bash
cd "/mnt/d/Coding Projects/MBSE"
grep -oh 'examples/[^ )]*' README.md | while read path; do
  [ -d "$path" ] || [ -f "$path" ] || echo "BROKEN: $path"
done
```

- [ ] **Step 7: Commit**

```bash
git add README.md
git commit -m "feat: update README with examples gallery and Electronic Systems agent"
```

- [ ] **Step 8: Update system.yaml status fields**

After all content is written, update every `system.yaml` from `status: draft` to `status: complete`.

```bash
find examples/ -name "system.yaml" -exec sed -i 's/status: draft/status: complete/' {} \;
git add examples/
git commit -m "chore: mark all example systems as complete"
```
