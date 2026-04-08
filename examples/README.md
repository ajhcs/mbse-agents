# Example Systems Gallery

Reference architectures demonstrating real artifact structure for each MBSE domain. Flagships include end-to-end traceability matrices from hazard analysis through assurance evidence, with any known gaps called out explicitly in the gap register. Fleet systems provide core artifacts expandable over time.

## ID Conventions

All systems use a shared ID taxonomy:

| Prefix | Scope | Defined In |
|--------|-------|------------|
| `MODE-` | Operating mode | README.md |
| `FUN-` | System/subsystem function | architecture.md |
| `REQ-` | Requirement | requirements.md |
| `HZ-` | Hazard / hazardous situation | hazard-analysis.md |
| `CTL-` | Risk control / mitigation | hazard-analysis.md |
| `THR-` | Cybersecurity threat | cybersecurity.md |
| `AST-` | Cybersecurity asset | cybersecurity.md |
| `CMP-` | Component (HW or SW) | architecture.md |
| `IFC-` | Interface | architecture.md |
| `VER-` | Verification activity | traceability.md |
| `EVD-` | Evidence artifact | assurance-evidence.md |

## Cross-File Integrity

Every flagship is structured to maintain:
- Every HZ has at least one CTL or explicit acceptability rationale
- Every CTL maps to at least one REQ
- Every assurance-relevant REQ maps to at least one CMP and at least one VER
- Every VER maps to at least one EVD
- Every gap is an explicit row in traceability.md

## Systems

### [Aerospace](aerospace/)

| System | Tier | Standards | Status |
|:-------|:-----|:----------|:-------|
| [Integrated Flight Management System](aerospace/flight-management-system/) | Flagship | ARP4754A, DO-178C, DO-254, DO-326A | Complete |
| [CubeSat Constellation](aerospace/cubesat-constellation/) | Fleet | NPR 7123.1, CCSDS | Complete |
| [EVA Suit Life Support](aerospace/eva-suit-life-support/) | Fleet | NPR 8705.2, NASA-STD-5005 | Complete |
| [Launch Vehicle Avionics](aerospace/launch-vehicle-avionics/) | Fleet | EWR 127-1, DO-178C | Complete |

### [Defense](defense/)

| System | Tier | Standards | Status |
|:-------|:-----|:----------|:-------|
| [UAS Ground Control Station](defense/uas-ground-control-station/) | Flagship | DoDAF 2.02, MIL-STD-882E, FACE 3.1 | Complete |
| [Ballistic Missile Defense Element](defense/ballistic-missile-defense/) | Fleet | DoDAF 2.02, MIL-STD-882E | Complete |
| [Tactical SDR Radio](defense/tactical-sdr-radio/) | Fleet | SCA 4.1, FACE 3.1 | Complete |
| [Naval Combat Management System](defense/naval-combat-management/) | Fleet | DoDAF 2.02, MIL-STD-882E | Complete |

### [Automotive](automotive/)

| System | Tier | Standards | Status |
|:-------|:-----|:----------|:-------|
| [Autonomous Emergency Braking](automotive/autonomous-emergency-braking/) | Flagship | ISO 26262, ISO 21448, ISO 21434 | Complete |
| [EV Battery Management System](automotive/ev-battery-management/) | Fleet | ISO 26262, UN R100 | Complete |
| [Steer-by-Wire](automotive/steer-by-wire/) | Fleet | ISO 26262, UN R79 | Complete |
| [V2X Communication Unit](automotive/v2x-communication/) | Fleet | ISO 21434, SAE J3161 | Complete |

### [Medical Device](medical-device/)

| System | Tier | Standards | Status |
|:-------|:-----|:----------|:-------|
| [Smart Infusion Pump](medical-device/smart-infusion-pump/) | Flagship | IEC 62304, ISO 14971, FDA QMSR | Complete |
| [Surgical Robot Platform](medical-device/surgical-robot-platform/) | Fleet | IEC 62304, IEC 80601-2-77 | Complete |
| [Continuous Glucose Monitor](medical-device/continuous-glucose-monitor/) | Fleet | IEC 62304, IMDRF SaMD N41 | Complete |
| [Patient Monitoring Network](medical-device/patient-monitoring-network/) | Fleet | IEC 62304, IEC 60601-1-8 | Complete |

### [Electronic Systems](electronic-systems/)

| System | Tier | Standards | Status |
|:-------|:-----|:----------|:-------|
| [Quantum Processor Control](electronic-systems/quantum-processor-control/) | Flagship | IEC 61508, IEEE 1076/1800 | Complete |
| [Safety-Critical SoC](electronic-systems/safety-critical-soc/) | Fleet | ISO 26262-11, AEC-Q100 | Complete |
| [FPGA Radar Signal Processor](electronic-systems/fpga-radar-signal-processor/) | Fleet | DO-254, MIL-STD-882E | Complete |
| [HPC Cluster Orchestration](electronic-systems/hpc-cluster-orchestration/) | Fleet | IEC 61508 | Complete |
