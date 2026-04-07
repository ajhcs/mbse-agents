# Autonomous Emergency Braking System

## Overview

The Autonomous Emergency Braking (AEB) system provides automatic collision avoidance and mitigation for L2+ passenger vehicles by fusing data from a front-facing 8-megapixel camera and a 77 GHz long-range radar. The system continuously monitors the forward driving corridor, detects and classifies objects including vehicles, pedestrians, cyclists, and static obstacles, predicts collision trajectories, and autonomously applies braking force when the driver fails to respond to imminent collision warnings.

The AEB architecture is a distributed three-ECU design spanning AUTOSAR Adaptive and AUTOSAR Classic platforms. The Perception ECU runs AUTOSAR Adaptive R22-11 and executes sensor fusion, object detection, classification, and tracking algorithms on a high-performance SoC with a dedicated neural processing unit. The Braking Control ECU runs AUTOSAR Classic 4.4 and manages the electro-hydraulic brake actuator, ABS interaction, and brake blending with the Electronic Stability Control (ESC) system. The Vehicle Gateway ECU runs AUTOSAR Classic 4.4 and bridges CAN FD and Automotive Ethernet domains, providing the communication backbone between the perception domain and the braking domain while isolating the safety-critical braking path from non-safety vehicle networks.

The system is classified ASIL D under ISO 26262. The safety lifecycle covers concept phase (Part 3), system development (Parts 4-5), and hardware/software integration testing (Parts 8-9). A SOTIF analysis per ISO 21448 addresses perception limitations including false negatives in rain, fog, glare, and tunnel-exit scenarios where the camera or radar may fail to detect valid targets. Cybersecurity threat analysis follows ISO/SAE 21434 with particular focus on OTA update integrity and CAN bus injection threats.

The system targets compliance with UN Regulation No. 152 (Uniform provisions concerning the approval of motor vehicles with regard to the Advanced Emergency Braking System) for type approval in UNECE contracting party markets.

## System Boundary

**Inside the system boundary:**
- Front-facing 8 MP camera module with image signal processor
- 77 GHz long-range radar module (up to 200 m range)
- Perception ECU (AUTOSAR Adaptive, sensor fusion and object detection)
- Braking Control ECU (AUTOSAR Classic, brake actuation commands)
- Vehicle Gateway ECU (AUTOSAR Classic, CAN FD / Ethernet bridging)
- AEB-specific wiring harness (Automotive Ethernet, CAN FD segments)
- AEB application software (perception, decision, actuation)

**Outside the system boundary:**
- Electro-hydraulic brake unit (receives commands from Braking Control ECU)
- Electronic Stability Control system (ESC provides ABS/stability; AEB consumes ESC status and commands brake pressure)
- Vehicle speed and dynamics sensors (wheel speed, yaw rate, steering angle -- consumed via CAN)
- Driver HMI (instrument cluster, head-up display -- receives AEB warnings; HMI hardware is external)
- Powertrain control module (receives torque reduction requests from AEB)
- OTA update infrastructure (cloud backend; AEB receives signed update packages)
- V2X communication unit (optional; provides cooperative awareness data to AEB via gateway)

## Operational Environment

The AEB system operates in a forward-facing vehicle installation on passenger vehicles designed for public road use. The operational design domain (ODD) covers highway and urban driving at speeds from 0 km/h (stationary target approach) to 160 km/h. Environmental conditions span -40C to +85C ambient temperature, direct sunlight and headlight glare, rain up to 50 mm/h, fog with visibility down to 50 m, and night driving. The system interfaces with 5+ vehicle subsystems via CAN FD and Automotive Ethernet. The camera module is mounted at the top of the windshield behind the rearview mirror. The radar module is mounted behind the front bumper fascia.

## Operating Modes

| Mode ID   | Name                    | Description                                                              | Active Functions                                               | Constraints                                          |
|-----------|-------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------|------------------------------------------------------|
| MODE-001  | Normal Driving          | Full AEB capability; camera and radar operational; continuous monitoring  | All FUN- functions active; sensor fusion, tracking, braking    | None                                                 |
| MODE-002  | AEB Active              | Collision imminent; system executing emergency braking intervention       | FUN-DET-01/02, FUN-TRK-01, FUN-DEC-01, FUN-BRK-01/02 active  | Driver override via strong accelerator pedal input    |
| MODE-003  | Degraded Perception     | One sensor failed or performance-limited; reduced detection capability    | Partial sensor fusion; extended braking thresholds applied     | Reduced ODD (speed/range limits); driver warning active |
| MODE-004  | Maintenance/Calibration | Vehicle stationary; sensor alignment and diagnostic functions active      | FUN-BIT-01, FUN-CAL-01 active; no braking intervention        | Ignition on, vehicle stationary; no AEB intervention  |
| MODE-005  | Post-Collision          | AEB intervention has occurred; system in post-event state                 | Event data recording; brake hold; secondary collision monitoring | No new AEB intervention for 3 seconds; driver retains full manual control |

Mode IDs are referenced by hazard-analysis.md, requirements.md, and traceability.md.

## Key Technical Challenges

1. **SOTIF perception limitations.** The camera and radar sensors have complementary but individually limited detection capabilities. The camera is degraded by rain, fog, direct glare, and low light. The radar has poor lateral resolution, cannot distinguish between a pedestrian and a signpost, and suffers from multipath reflections in urban canyons. The sensor fusion algorithm must compensate for these limitations, but residual SOTIF scenarios (ISO 21448 triggering conditions) where both sensors fail simultaneously for the same object remain the primary safety concern.

2. **ASIL D braking path integrity.** The brake actuation path from collision decision to hydraulic brake pressure application must meet ASIL D random hardware fault metrics. The Braking Control ECU requires hardware fault detection coverage exceeding 99% (single-point fault metric) and diagnostic test intervals short enough to detect latent faults before they combine with active faults. The AUTOSAR Classic safety mechanisms (program flow monitoring, memory protection, watchdog) must be configured to achieve the required diagnostic coverage.

3. **AUTOSAR Adaptive and Classic coexistence.** The Perception ECU (Adaptive) and Braking Control ECU (Classic) have fundamentally different execution models, timing characteristics, and safety mechanisms. The end-to-end communication path from perception output to brake command must maintain ASIL D integrity across the Adaptive/Classic boundary, which requires careful E2E protection (AUTOSAR E2E Profile 7), timing monitoring, and freedom-from-interference arguments at the network interface.

4. **Real-time decision latency budget.** The total system latency from object detection to brake pressure rise must not exceed 300 ms for the system to achieve the required stopping distances under UN R152. This budget spans camera exposure and ISP processing (~50 ms), neural network inference (~30 ms), sensor fusion and tracking (~20 ms), decision logic (~10 ms), CAN/Ethernet communication (~10 ms), and brake hydraulic response (~100 ms), leaving minimal margin for retries or extended processing.

5. **Cybersecurity of OTA and CAN interfaces.** The Perception ECU receives OTA software updates for the neural network model and fusion parameters. A compromised update could disable AEB or cause false activations. The CAN FD interface to the braking domain is susceptible to message injection attacks. The ISO 21434 TARA must demonstrate that security controls mitigate these threats without introducing unacceptable safety impact (e.g., security mechanisms that delay brake commands).

## Stakeholders

| Stakeholder                    | Role                                                                          |
|--------------------------------|-------------------------------------------------------------------------------|
| Vehicle driver                 | Primary beneficiary; receives warnings; can override AEB intervention         |
| Vehicle OEM integration team   | Integrates AEB into vehicle platform; responsible for vehicle-level safety case |
| Tier-1 AEB system supplier     | Designs and delivers AEB system; holds SEooC safety case                     |
| Type approval authority (UNECE)| Approves vehicle type against UN R152; reviews test evidence                  |
| Third-party assessor           | Performs functional safety assessment per ISO 26262 Part 2, clause 6.4.6     |
| Maintenance technician         | Performs sensor calibration, ECU replacement, diagnostic readout              |
| Vulnerable road users          | Pedestrians, cyclists -- ultimate safety beneficiaries of AEB intervention    |

## Standards Applicability

| Standard            | Applicability                                                                                           |
|---------------------|---------------------------------------------------------------------------------------------------------|
| ISO 26262           | Functional safety lifecycle; ASIL D for braking path; governs concept, system, HW, SW, integration      |
| ISO 21448 (SOTIF)   | Safety of the Intended Functionality; addresses perception limitations and triggering conditions          |
| ISO 21434           | Cybersecurity engineering; TARA for OTA, CAN, and V2X interfaces                                        |
| AUTOSAR Classic 4.4 | Software architecture for Braking Control ECU and Vehicle Gateway ECU                                   |
| AUTOSAR Adaptive R22-11 | Software architecture for Perception ECU; ara::com, ara::exec services                              |
| UN R152             | Type approval regulation for AEBS; test scenarios, stopping distance requirements                        |
| ISO 11898           | CAN and CAN FD physical and data link layer; applies to in-vehicle communication                        |
| IEEE 802.3 (100BASE-T1) | Automotive Ethernet physical layer for Perception ECU to Gateway communication                     |
