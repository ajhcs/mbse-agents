# Integrated Flight Management System

## Overview

The Integrated Flight Management System (FMS) provides flight planning, navigation, performance computation, and guidance for a Part 25 transport category aircraft. The system computes lateral and vertical flight profiles from an operator-entered flight plan, drives coupled autopilot guidance through the Automatic Flight Control System (AFCS), and presents navigation and performance data to the flight crew via the cockpit display system.

The FMS architecture is a dual-channel design built around two Line Replaceable Units (LRUs): a primary Flight Management Computer (FMC) and a Display Management Computer (DMC), supported by a Data Concentrator Unit (DCU) that aggregates sensor and datalink inputs. The two FMC channels employ dissimilar software to defeat common-mode software faults that could produce misleading navigation or guidance outputs. ARINC 653 partitioning isolates safety-critical navigation functions from lower-criticality advisory functions within each FMC channel.

The system is classified DAL A under ARP4754A, with software developed to DO-178C Level A supplemented by DO-331 for model-based development artifacts. Programmable hardware in the FMC and DCU is developed under DO-254 DAL A. Cybersecurity assessment follows DO-326A, with the threat assessment addressing both ground-facing datalink interfaces and maintenance port access paths.

The target certification basis is 14 CFR 25.1309 (Equipment, Systems, and Installations) with the FMS contributing to compliance with 25.1329 (Flight Guidance System) and AC 20-174 referencing ARP4754A as the development assurance framework.

## System Boundary

**Inside the system boundary:**
- Flight Management Computer (dual-channel, dissimilar)
- Display Management Computer (FMS-specific display processing)
- Data Concentrator Unit (sensor and datalink aggregation)
- FMS application software (flight planning, navigation, performance, guidance)
- FMS-specific wiring and ARINC 429/664 data buses between LRUs
- FMS Control Display Unit (CDU) interface protocol (CDU hardware is external)

**Outside the system boundary:**
- Automatic Flight Control System (receives guidance commands from FMS)
- Navigation sensors (IRS, GNSS, DME, VOR — provide data to DCU)
- Cockpit display system (receives display data from DMC; CDU hardware is display-system-owned)
- Aircraft datalink system (ACARS, FANS — interfaces via DCU)
- Terrain and obstacle databases (loaded via maintenance port, treated as GFE data)
- Engine and fuel system (provides fuel state data via ARINC 429; FMS consumes but does not command)

## Operational Environment

The FMS operates in the cockpit avionics bay of a Part 25 transport aircraft across all phases of flight from pre-departure through post-landing. The operational envelope spans sea level to FL510, temperature extremes from -55C to +70C (equipment bay), and vibration profiles per DO-160G Category S2. The system interfaces with 8+ external aircraft systems via ARINC 429 and ARINC 664 Part 7 (AFDX) data buses.

## Operating Modes

| Mode ID   | Name                | Description                                                  | Active Functions                                      | Constraints                                       |
|-----------|---------------------|--------------------------------------------------------------|-------------------------------------------------------|---------------------------------------------------|
| MODE-001  | Normal              | Dual-channel operation, full navigation and guidance         | All FUN- functions active on both FMC channels        | None                                              |
| MODE-002  | Degraded-Single     | One FMC channel failed; single-channel operation             | FPL, NAV, PERF, GUID on surviving channel             | No cross-channel comparison; crew annunciation required |
| MODE-003  | Nav-Only            | Guidance output inhibited; navigation and display only       | FPL, NAV, PERF active; GUID inhibited                 | AFCS reverts to manual; crew must hand-fly         |
| MODE-004  | Reversionary-Display| DMC failed; FMC drives backup display path                   | All FMC functions; DMC display functions on backup path| Reduced display capability; EICAS page unavailable |
| MODE-005  | Maintenance         | Ground-only mode for data loading and built-in test          | BIT, data load, configuration; no guidance output      | Weight-on-wheels interlock required; no flight use  |

Mode IDs are referenced by hazard-analysis.md, requirements.md, and traceability.md.

## Key Technical Challenges

1. **Dissimilar redundancy verification.** The two FMC channels run dissimilar software implementations of the same navigation and guidance algorithms. Demonstrating equivalence of intended function while confirming independence against common-mode faults requires dual verification campaigns and a rigorous common-mode analysis per ARP4761A.

2. **ARINC 653 partitioning integrity.** Safety-critical navigation functions (DAL A) and advisory performance functions (DAL C) share the same FMC processor under ARINC 653 spatial and temporal partitioning. The partitioning argument must survive SOI #3 scrutiny with evidence of partition testing, health monitoring coverage, and worst-case execution time analysis addressing CAST-32A multi-core interference.

3. **DO-331 model-based development boundary.** The navigation algorithms are developed using model-based methods with auto-generated code. The DO-331 compliance boundary, model-to-code traceability, and DO-330 tool qualification for the code generator must be defined clearly enough that the DER can audit the evidence chain from model requirement to object code.

4. **Cybersecurity-safety interaction.** The DCU's datalink interface creates an attack surface that connects to ACARS and FANS ground networks. A successful integrity attack on the datalink path could corrupt navigation database updates or flight plan modifications, potentially contributing to a Hazardous failure condition. The DO-326A threat assessment must demonstrate that security controls reduce this risk without introducing safety-relevant failure modes of their own.

5. **Multi-sensor navigation integrity.** The FMS fuses data from IRS, GNSS, DME, and VOR with different integrity, accuracy, and availability characteristics. The navigation solution must detect and exclude faulty sensor inputs (FDE) while maintaining RNP containment, and the failure detection logic must be verified against the probability budgets allocated by the PSSA.

## Stakeholders

| Stakeholder              | Role                                                                 |
|--------------------------|----------------------------------------------------------------------|
| Flight crew              | Primary operators; enter flight plans, monitor navigation, manage modes |
| Airline operations       | Define navigation database content, operational procedures, dispatch rules |
| Maintenance organization | Perform data loads, fault isolation, LRU replacement via maintenance mode |
| FAA certification office | Approve type design; conduct SOI reviews; issue TC/STC                |
| Designated Engineering Representative (DER) | Review and recommend approval of compliance evidence |
| EASA certification team  | Parallel validation for dual-certification programs                   |

## Standards Applicability

| Standard      | Applicability                                                                                     |
|---------------|---------------------------------------------------------------------------------------------------|
| ARP4754A      | System development assurance framework; governs FHA-to-SSA lifecycle and DAL allocation            |
| ARP4761A      | Safety assessment methodology; FHA, PSSA, SSA, CMA for all failure conditions                     |
| DO-178C       | Airborne software assurance for FMC, DMC, and DCU application software at Level A                 |
| DO-331        | Model-based development supplement; applies to FMC navigation algorithm development               |
| DO-254        | Programmable hardware assurance for FMC and DCU FPGA/ASIC components at DAL A                     |
| DO-326A       | Airworthiness security process; threat assessment for datalink and maintenance interfaces          |
| DO-356A       | Security methods; TARA methodology for threat identification and risk analysis                     |
| DO-330        | Tool qualification for code generator (TQL-1) and test automation framework (TQL-4)               |
| DO-160G       | Environmental qualification for all LRUs                                                          |
| ARINC 653     | Real-time operating system partitioning standard; governs FMC partition architecture               |
| ARINC 429     | Legacy data bus standard for sensor and display interfaces                                        |
| ARINC 664 P7  | AFDX networking standard for high-bandwidth inter-LRU and external interfaces                     |
| 14 CFR 25.1309| Equipment, systems, and installations; primary airworthiness regulation for FMS                    |
