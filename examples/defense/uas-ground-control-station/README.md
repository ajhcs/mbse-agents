# UAS Ground Control Station

## Overview

The UAS Ground Control Station (GCS) is a multi-vehicle ground control station for Group 4/5 unmanned aircraft systems of the MQ-9 class. The GCS provides command and control (C2) link management, mission planning and execution, electro-optical/infrared/synthetic aperture radar (EO/IR/SAR) sensor payload control, and airspace integration through ADS-B and ACAS Xu interfaces. A single GCS station supports simultaneous control of up to four air vehicles across beyond-line-of-sight (BLOS) satellite and line-of-sight (LOS) data links.

The system is an ACAT II major defense acquisition program with a Modular Open Systems Approach (MOSA) mandate per 10 USC 4401. The architecture conforms to FACE Technical Standard 3.1 for software portability and reuse across the Transport Services Segment (TSS) and Platform-Specific Services Segment (PSSS). Three subsystems compose the GCS: a Mission Management Computer (MMC) for flight management, mission planning, and C2 orchestration; a C2 Link Terminal (CLT) for LOS/BLOS data link operations and COMSEC; and a Sensor Control Workstation (SCW) for multi-sensor payload tasking, exploitation, and dissemination.

Safety assessment follows MIL-STD-882E with SIL 4 rigor applied to flight-safety-critical functions including lost link procedures, geofence enforcement, and emergency flight termination. System safety deliverables are structured as DI-SESS CDRLs mapped to technical review gates (SRR, PDR, CDR, TRR). DoDAF 2.02 views provide the architecture products required by the DoD Architecture Framework for milestone decision reviews.

## System Boundary

**Inside the system boundary:**
- Mission Management Computer (flight management, mission planning, C2 orchestration)
- C2 Link Terminal (LOS/BLOS transceiver, COMSEC module, antenna control)
- Sensor Control Workstation (EO/IR/SAR display, sensor tasking, PED functions)
- GCS application software (FACE 3.1 conformant)
- Internal Ethernet backbone (GCS LAN) connecting MMC, CLT, and SCW
- Operator interface hardware (displays, input devices, alert panels) integrated into MMC and SCW

**Outside the system boundary:**
- Air vehicle flight control system (receives commands from GCS via C2 link; flight dynamics are AV-resident)
- Sensor payloads (EO/IR turret, SAR pod -- GCS commands but does not host sensor processing hardware)
- SATCOM ground terminal (provides BLOS transport; CLT interfaces to the terminal but does not own it)
- ATC/FAA systems (GCS provides ADS-B and ACAS data but does not control airspace management)
- Intelligence processing exploitation and dissemination (PED) enterprise (GCS feeds sensor products but downstream analysis is external)
- Launch and recovery element (LRE) for taxi/takeoff/landing phases (separate ground station)

## Operational Environment

The GCS operates from fixed ground sites, containerized shelters (SICPS-type), or deployable HMMWV-mounted configurations. Operating temperature range is -32C to +49C per MIL-STD-810H Method 501/502. The system interfaces with theater C2 networks via SIPR/NIPR connectivity, satellite communication ground terminals for BLOS operations, and local LOS antenna systems for operations within 150 NM. Electromagnetic environment per MIL-STD-461G applies to all GCS subsystems.

## Operating Modes

| Mode ID   | Name                | Description                                                              | Active Functions                                           | Constraints                                              |
|-----------|---------------------|--------------------------------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------|
| MODE-001  | Normal Mission      | Full multi-vehicle C2 with all sensor and link functions operational     | All FUN- functions active across MMC, CLT, SCW             | None                                                     |
| MODE-002  | Degraded C2         | One C2 link path lost; remaining path supports reduced data rate         | FUN-C2-01 on surviving link; FUN-MSN-01, FUN-SNS-01 at reduced bandwidth | Sensor video downgraded to keyframes; telemetry rate halved |
| MODE-003  | Lost Link           | All C2 links to one or more air vehicles lost                            | FUN-MSN-03 (lost link procedure) active; FUN-C2-01 attempts reconnect | AV executes pre-programmed lost link profile; GCS monitors only |
| MODE-004  | Ground Maintenance  | Ground-only mode for software loading, BIT, and configuration            | FUN-BIT-01, FUN-DLD-01 active; no flight commands transmitted | Weight-on-wheels interlock equivalent (ground power only) |
| MODE-005  | Emergency           | Flight termination command authority activated                           | FUN-MSN-04 (emergency flight termination) takes priority over all other functions | Requires two-operator authentication; irreversible once initiated |

Mode IDs are referenced by hazard-analysis.md, requirements.md, and traceability.md.

## Key Technical Challenges

1. **Lost link procedural safety.** When all C2 links to an air vehicle are lost, the AV executes a pre-programmed lost link profile (orbit, return to base, or controlled flight into terrain avoidance). The GCS must detect link loss within defined timelines, initiate recovery procedures, and coordinate with ATC. The lost link detection and response sequence is the single highest-risk failure mode in the system and drives the MIL-STD-882E severity/probability budget.

2. **Multi-vehicle C2 under bandwidth constraints.** Simultaneous control of four Group 4/5 UAS across shared BLOS SATCOM bandwidth requires dynamic bandwidth allocation between telemetry, sensor video, and command uplink channels. Prioritization algorithms must ensure flight-safety-critical commands are never starved by sensor data traffic, while maintaining sufficient situational awareness for operators.

3. **MOSA/FACE conformance with legacy interfaces.** The FACE 3.1 mandate requires a layered architecture with defined portability profiles, but the system must interface with legacy MIL-STD-1553 and RS-422 C2 link equipment. The PSSS must bridge FACE-conformant application software to non-conformant legacy transports without compromising portability goals or introducing unverified interface wrappers.

4. **COMSEC key management across classification domains.** The CLT handles both LOS and BLOS links at different classification levels. Cryptographic key management must support over-the-air rekeying (OTAR), key fill, and zeroization while maintaining Type 1 COMSEC integrity. The COMSEC boundary is a critical security domain that intersects with the safety domain when encrypted C2 links fail.

5. **Airspace integration for non-cooperative targets.** The GCS must provide ACAS Xu deconfliction advisories and ADS-B Out position reports for UAS operating in national airspace. Latency in the ground-to-air C2 loop means that time-critical avoidance maneuvers must account for C2 link delay, creating a unique challenge that does not exist for manned aircraft TCAS implementations.

## Stakeholders

| Stakeholder                        | Role                                                                              |
|------------------------------------|-----------------------------------------------------------------------------------|
| UAS operator crew (pilot, sensor operator) | Primary operators; execute mission, manage C2 links, control sensor payloads |
| Unit commander                     | Mission authority; approves mission plans, lost link profiles, ROE                |
| Program Executive Office (PEO)     | Acquisition oversight; milestone decision authority for ACAT II program           |
| DASD(SE)                           | Systems engineering policy oversight; MOSA compliance assessment                  |
| DT&E / OT&E organizations          | Developmental and operational test planning and execution                         |
| FAA / ATC                          | Airspace integration authority; UAS airspace access coordination                  |
| Maintenance organization           | Perform software loads, BIT, COMSEC key fill, hardware maintenance               |
| Intelligence community (IC)        | Consumer of sensor products; defines PED requirements                             |

## Standards Applicability

| Standard        | Applicability                                                                                        |
|-----------------|------------------------------------------------------------------------------------------------------|
| MIL-STD-882E    | System safety; hazard identification, risk assessment, risk acceptance authority chain                |
| DoDAF 2.02      | Architecture framework; OV, SV, DIV viewpoints for milestone reviews                                 |
| FACE 3.1        | Software architecture standard; portability profiles for TSS and PSSS segments                       |
| MOSA (10 USC 4401) | Modular open systems approach mandate for major defense acquisition programs                       |
| DI-SESS-81785A  | CDRL data item description for system safety deliverables                                            |
| MIL-STD-1553B   | Legacy data bus standard for C2 link terminal interfaces                                             |
| MIL-STD-461G    | Electromagnetic interference requirements for all GCS subsystems                                     |
| MIL-STD-810H    | Environmental engineering considerations and laboratory tests                                        |
| DO-178C         | Software assurance for airborne-equivalent safety-critical GCS functions (applied by analogy)         |
| STANAG 4586     | NATO standard for UAS control system interoperability                                                |
