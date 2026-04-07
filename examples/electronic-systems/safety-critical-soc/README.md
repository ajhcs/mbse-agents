# Safety-Critical SoC

## Overview

The Safety-Critical SoC (SC-SoC) is an automotive-grade system-on-chip providing ADAS compute for Level 2+ through Level 4 autonomous driving functions. The SoC integrates lockstep ARM Cortex-R52 safety cores, a high-performance application processor cluster, neural network accelerator, and hardware safety mechanisms onto a single 7 nm die. The device targets ASIL D random hardware fault metrics (SPFM >= 99%, LFM >= 90%, PMHF < 10 FIT) per ISO 26262-11 and qualifies through the AEC-Q100 Grade 1 automotive stress test flow. The SoC receives sensor fusion inputs from camera, radar, and lidar interfaces, processes perception and planning algorithms, and outputs actuation commands to the ADAS ECU host over Automotive Ethernet and CAN-FD.

## System Boundary

**Inside the system boundary:**
- Lockstep CPU subsystem (dual Cortex-R52 cores with split-lock comparator)
- Application processor cluster (quad Cortex-A78AE)
- Neural network accelerator (8 TOPS INT8)
- On-chip SRAM (4 MB) with inline ECC and BIST
- Embedded flash (16 MB) with ECC and secure boot ROM
- Hardware safety mechanisms: watchdog timer, voltage monitor, temperature monitor, clock monitor
- On-chip interconnect (NoC) with end-to-end data protection
- Peripheral interfaces: CSI-2 (camera), Automotive Ethernet, CAN-FD, SPI, JTAG/DAP

**Outside the system boundary:**
- ADAS ECU host board (PCB, power supply, external DRAM)
- External sensors (cameras, radar modules, lidar units)
- Vehicle communication networks (CAN bus backbone, Ethernet switch)
- Application software running on the SoC (OEM-developed ADAS stack)
- Package and thermal management (heat sink, TIM, PCB thermal vias)

## Operational Environment

The SC-SoC operates within an ADAS ECU mounted in the vehicle engine bay or passenger compartment, exposed to junction temperatures from -40 C to 150 C (AEC-Q100 Grade 1). The device interfaces with up to 8 camera streams via MIPI CSI-2, radar and lidar preprocessors via Automotive Ethernet, and the vehicle bus via CAN-FD. Power is supplied by the ECU board at 0.8 V core and 1.8 V / 3.3 V I/O, with power management sequencing controlled by the on-chip PMIC interface.

## Operating Modes

| Mode ID   | Name                    | Description                                                             | Active Functions                                              | Constraints                                          |
|-----------|-------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------|------------------------------------------------------|
| MODE-001  | Normal Operation        | Full ADAS compute with all safety mechanisms active                     | All FUN- functions active; lockstep, ECC, monitors enabled    | Junction temp within -40 to 150 C; supply within 5%  |
| MODE-002  | Degraded (Lockstep Fault) | Lockstep comparator detected mismatch; safety core pair offline       | FUN-SAF-01 active; application cores may continue at reduced ASIL | Host ECU notified; affected safety function disabled |
| MODE-003  | Power-On Self-Test      | BIST and safety mechanism verification during startup                   | FUN-BIT-01 active; no ADAS processing                         | Must complete within 100 ms; no actuation output     |
| MODE-004  | Low-Power Standby       | Cores clock-gated; wakeup monitoring active                             | FUN-MON-01 (wake source monitoring) only                      | No processing; CAN wake capability retained          |

## Key Technical Challenges

1. **Lockstep comparison latency vs. fault detection coverage.** The split-lock comparator must detect CPU errors within one clock cycle without introducing pipeline stalls. The comparator operates on instruction-retired signatures rather than cycle-by-cycle state, trading some detection granularity for timing closure at 1.5 GHz.

2. **SRAM single-point fault metric achievement.** Achieving SPFM >= 99% for 4 MB of on-chip SRAM requires inline ECC with single-cycle correction and periodic background scrubbing. The scrub interval must be short enough that latent multi-bit errors remain below the PMHF budget, yet long enough to avoid starving real-time memory accesses.

3. **AEC-Q100 reliability vs. advanced node yield.** Qualifying a 7 nm process for AEC-Q100 Grade 1 requires demonstrating reliability at 150 C junction temperature across HTOL, TC, UHAST, and ESD/LU stresses. Advanced node defect densities and electromigration margins require design-for-reliability techniques (redundant vias, wide metal, guard rings) that increase die area.

4. **Mixed-criticality NoC partitioning.** The on-chip network must provide freedom from interference between ASIL D safety cores and QM application processors. Bandwidth and latency guarantees must be enforced in hardware through time-division or credit-based arbitration, with formal proof that no QM traffic can starve a safety-critical access.

## Stakeholders

| Stakeholder                      | Role                                                                     |
|----------------------------------|--------------------------------------------------------------------------|
| ADAS system integrator (OEM)     | Deploys SoC in ECU; responsible for system-level safety case             |
| Semiconductor design team        | Designs RTL, verifies, and tapes out the SoC                            |
| Functional safety engineer       | Develops FMEDA, performs fault injection, maintains SPFM/LFM budgets    |
| AEC-Q100 qualification engineer  | Executes stress tests and early failure rate analysis                    |
| ECU hardware engineer            | Designs host PCB, power delivery, thermal management                    |
| Certification authority          | Audits ISO 26262 compliance and approves safety case                    |

## Standards Applicability

| Standard       | Applicability                                                                                          |
|----------------|--------------------------------------------------------------------------------------------------------|
| ISO 26262-11   | Semiconductor-specific safety lifecycle: concept, development, production; FMEDA methodology for SPFM/LFM/PMHF |
| AEC-Q100       | Automotive IC qualification: stress test requirements (HTOL, TC, UHAST, ESD), lot sampling, early failure rate screening |
| IEC 61508      | Referenced by ISO 26262 for hardware fault tolerance concepts and SIL/ASIL correspondence               |
| IEEE 1149.1    | JTAG boundary scan for production test and debug access                                                 |
| MIPI CSI-2     | Camera serial interface standard for sensor input                                                       |
