# Architecture

## System Context

```mermaid
graph TB
    subgraph SBW["Steer-by-Wire System"]
        SWS["CMP-SWS-01<br/>Steering Wheel<br/>Sensor Unit"]
        HFA["CMP-HFA-01<br/>Handwheel Feedback<br/>Actuator"]
        SCC["CMP-SCC-01<br/>SbW Central Controller<br/>(Dual-Channel)"]
        RAA["CMP-RA-A<br/>Rack Actuator A<br/>(Left)"]
        RAB["CMP-RA-B<br/>Rack Actuator B<br/>(Right)"]
    end

    WHEEL["Steering Wheel"]
    RACK["Steering Rack<br/>& Tie Rods"]
    VDC["Vehicle Dynamics<br/>Controller"]
    ADAS["ADAS Lane-Keeping<br/>Assist"]
    PSU["Dual 48V Power<br/>Supply"]
    CLUSTER["Instrument Cluster"]

    WHEEL -->|Mechanical coupling| SWS
    SWS -->|Torque, angle| SCC
    SCC -->|Torque command| HFA
    HFA -->|Road feel torque| WHEEL
    SCC -->|Position command Ch-A| RAA
    SCC -->|Position command Ch-B| RAB
    RAA -->|Rack force (left)| RACK
    RAB -->|Rack force (right)| RACK
    VDC -->|Speed, yaw rate, lat accel| SCC
    ADAS -->|Lane-keeping overlay| SCC
    PSU -->|48V Feed A| SCC
    PSU -->|48V Feed B| SCC
    SCC -->|Rack position, status| VDC
    SCC -->|Status, warnings| CLUSTER
```

## Functional Architecture

| FUN ID       | Function Name                    | Description                                                                   | Inputs                                       | Outputs                                       | Dependencies         |
|--------------|----------------------------------|-------------------------------------------------------------------------------|----------------------------------------------|-----------------------------------------------|----------------------|
| FUN-INP-01   | Steering Input Acquisition       | Read driver torque and angle from redundant steering wheel sensors            | Torque sensor signals, angle sensor signals  | Driver torque, steering angle                 | None                 |
| FUN-CMD-01   | Steering Command Computation     | Convert driver input to target rack position using variable ratio algorithm   | Steering angle, vehicle speed                | Target rack position                          | FUN-INP-01           |
| FUN-ACT-01   | Rack Actuation (Channel A)       | Drive Rack Actuator A to achieve target rack position                         | Target rack position, rack position feedback | Motor current commands (Ch-A)                 | FUN-CMD-01           |
| FUN-ACT-02   | Rack Actuation (Channel B)       | Drive Rack Actuator B to achieve target rack position                         | Target rack position, rack position feedback | Motor current commands (Ch-B)                 | FUN-CMD-01           |
| FUN-FBK-01   | Road-Feel Torque Generation      | Synthesize torque feedback to the handwheel based on road-feel model          | Vehicle speed, rack force estimate, road model | Handwheel torque command                    | FUN-CMD-01           |
| FUN-ARB-01   | ADAS Overlay Arbitration         | Accept and limit ADAS lane-keeping steering overlay commands                  | ADAS overlay request, driver input           | Superimposed rack position offset             | FUN-CMD-01           |
| FUN-FLT-01   | Fault Management and Switchover  | Detect channel faults, manage switchover, force fight detection               | Actuator feedback, channel diagnostics       | Fault flags, mode transitions, channel disable | FUN-ACT-01, FUN-ACT-02 |
| FUN-MON-01   | System Health Monitoring         | Continuous monitoring of sensors, actuators, communication, power supply      | Sensor diagnostics, actuator current, power status | Health status, degradation flags          | None                 |

## Physical Architecture

| CMP ID        | Component Name                           | Type     | Parent        | Description                                                           |
|---------------|------------------------------------------|----------|---------------|-----------------------------------------------------------------------|
| CMP-SWS-01    | Steering Wheel Sensor Unit               | Module   | System        | Redundant torque and angle sensors on the steering column             |
| CMP-SWS-01A   | Torque Sensor (Redundant)                | Hardware | CMP-SWS-01    | Dual-element magnetostrictive torque sensor                           |
| CMP-SWS-01B   | Angle Sensor (Redundant)                 | Hardware | CMP-SWS-01    | Dual-resolver absolute angle sensor                                   |
| CMP-HFA-01    | Handwheel Feedback Actuator              | Module   | System        | BLDC motor providing road-feel torque to the steering column          |
| CMP-SCC-01    | SbW Central Controller                   | ECU      | System        | Dual-channel processing unit for steering command computation         |
| CMP-SCC-01A   | Processing Channel A (MCU-A)             | Hardware | CMP-SCC-01    | Safety MCU with lockstep cores, dedicated power regulator             |
| CMP-SCC-01B   | Processing Channel B (MCU-B)             | Hardware | CMP-SCC-01    | Independent safety MCU (dissimilar silicon), separated power domain   |
| CMP-SCC-01C   | Steering Command Application             | Software | CMP-SCC-01A   | Variable ratio, rack position target computation (runs on both channels) |
| CMP-SCC-01D   | Road-Feel Model Application              | Software | CMP-SCC-01A   | Torque feedback synthesis based on vehicle dynamics and rack force    |
| CMP-SCC-01E   | ADAS Arbitration Application             | Software | CMP-SCC-01A   | ADAS overlay command limiting and superposition                       |
| CMP-SCC-01F   | Fault Manager Application                | Software | CMP-SCC-01A   | Channel health monitoring, force fight detection, switchover logic    |
| CMP-RA-A      | Rack Actuator A (Left)                   | Actuator | System        | BLDC motor with integrated motor controller and rack position sensor  |
| CMP-RA-B      | Rack Actuator B (Right)                  | Actuator | System        | BLDC motor with integrated motor controller and rack position sensor  |

## Allocation

| FUN ID       | REQ ID(s)                                    | CMP ID(s)                                    | Assurance Level | Rationale                                                          |
|--------------|----------------------------------------------|----------------------------------------------|-----------------|--------------------------------------------------------------------|
| FUN-INP-01   | REQ-FUN-001                                  | CMP-SWS-01, CMP-SWS-01A, CMP-SWS-01B       | ASIL D          | Steering input is on the critical actuation path; single source of driver intent |
| FUN-CMD-01   | REQ-FUN-002, REQ-FUN-003                     | CMP-SCC-01C                                  | ASIL D          | Incorrect steering command directly causes wrong road wheel angle  |
| FUN-ACT-01   | REQ-FUN-002, REQ-SAF-002                     | CMP-SCC-01A, CMP-RA-A                       | ASIL D          | Primary actuation channel; ASIL D with redundancy via Channel B    |
| FUN-ACT-02   | REQ-FUN-002, REQ-SAF-002                     | CMP-SCC-01B, CMP-RA-B                       | ASIL D          | Redundant actuation channel; ASIL D independent of Channel A       |
| FUN-FBK-01   | REQ-FUN-004                                  | CMP-HFA-01, CMP-SCC-01D                     | ASIL B          | Incorrect road feel is misleading but driver retains visual/vestibular cues |
| FUN-ARB-01   | REQ-FUN-005                                  | CMP-SCC-01C, CMP-SCC-01E                    | ASIL B          | ADAS overlay is authority-limited; driver can always override       |
| FUN-FLT-01   | REQ-SAF-001, REQ-SAF-004                     | CMP-SCC-01F, CMP-RA-A, CMP-RA-B            | ASIL D          | Fault management determines system availability; missed fault leads to loss of steering |
| FUN-MON-01   | REQ-SAF-003                                  | CMP-SCC-01A, CMP-SCC-01B                    | ASIL D          | Health monitoring supports freedom-from-interference argument       |

## Interfaces

### External Interfaces

| IFC ID       | Partner System                       | Data Item                                    | Direction     | Protocol              | Timing                 |
|--------------|--------------------------------------|----------------------------------------------|---------------|-----------------------|------------------------|
| IFC-EXT-001  | Steering Wheel (mechanical)          | Driver torque, steering wheel angle          | In            | Mechanical + sensor   | Continuous (1 kHz)     |
| IFC-EXT-002  | Vehicle Dynamics Controller          | Vehicle speed, yaw rate, lateral acceleration | In           | CAN FD (E2E)          | 10 ms cycle (100 Hz)  |
| IFC-EXT-003  | ADAS Lane-Keeping Assist             | Lane-keeping overlay command, ADAS status    | In            | Automotive Ethernet (SOME/IP) | 20 ms cycle (50 Hz)  |
| IFC-EXT-004  | Vehicle Dynamics Controller / Cluster | Rack position, steering status, fault info   | Out           | CAN FD (E2E)          | 10 ms cycle (100 Hz)  |
| IFC-EXT-005  | Dual 48V Power Supply                | Power feed A, power feed B                   | In            | Hardwired (48V DC)    | Continuous             |

### Internal Interfaces

| IFC ID       | Source CMP ID  | Target CMP ID  | Data Item                                      | Mechanism             | Timing              |
|--------------|----------------|-----------------|------------------------------------------------|-----------------------|---------------------|
| IFC-INT-001  | CMP-SWS-01     | CMP-SCC-01A     | Driver torque, steering angle (Channel A)      | Dedicated analog/digital | 1 ms cycle (1 kHz) |
| IFC-INT-002  | CMP-SWS-01     | CMP-SCC-01B     | Driver torque, steering angle (Channel B)      | Dedicated analog/digital | 1 ms cycle (1 kHz) |
| IFC-INT-003  | CMP-SCC-01A    | CMP-RA-A        | Rack position command, motor current command   | Dedicated CAN FD (E2E) | 1 ms cycle (1 kHz)  |
| IFC-INT-004  | CMP-SCC-01B    | CMP-RA-B        | Rack position command, motor current command   | Dedicated CAN FD (E2E) | 1 ms cycle (1 kHz)  |
| IFC-INT-005  | CMP-RA-A       | CMP-SCC-01A     | Rack position feedback, motor current feedback | Dedicated CAN FD (E2E) | 1 ms cycle (1 kHz)  |
| IFC-INT-006  | CMP-RA-B       | CMP-SCC-01B     | Rack position feedback, motor current feedback | Dedicated CAN FD (E2E) | 1 ms cycle (1 kHz)  |
| IFC-INT-007  | CMP-SCC-01A    | CMP-SCC-01B     | Cross-channel comparison data (position, torque, faults) | Inter-processor link (isolated) | 1 ms cycle |
| IFC-INT-008  | CMP-SCC-01A    | CMP-HFA-01      | Handwheel torque command                       | Dedicated analog/digital | 1 ms cycle (1 kHz) |

## Failure Containment / Partitioning

### Dual-Channel Independence (Freedom from Interference)

The SbW architecture achieves fail-operational behavior through two fully independent actuation channels. Each channel consists of an independent processing path (MCU) in the SCC and an independent rack actuator.

| Partition             | Channel A                              | Channel B                              | Independence Evidence                  |
|-----------------------|----------------------------------------|----------------------------------------|----------------------------------------|
| Processing            | CMP-SCC-01A (MCU-A, lockstep)         | CMP-SCC-01B (MCU-B, dissimilar silicon) | Separate die, separate supply, separate clock |
| Power regulation      | Dedicated 48V-to-5V regulator (Feed A) | Dedicated 48V-to-5V regulator (Feed B)  | Separate power domains from vehicle dual feed |
| Sensor input          | Dedicated sensor signal path to MCU-A  | Dedicated sensor signal path to MCU-B   | Separated PCB traces, separate ADCs     |
| Actuator              | CMP-RA-A (left-mounted)               | CMP-RA-B (right-mounted)              | Physically separated, independent motor controllers |
| Communication         | Dedicated CAN FD to RA-A              | Dedicated CAN FD to RA-B              | Separate CAN transceivers and bus segments |

**Common-cause failure mitigation:**
- Dissimilar silicon: MCU-A and MCU-B use different processor architectures from different vendors.
- Separated power: Each channel is powered from a separate vehicle power feed with independent voltage regulation. A single power supply failure disables only one channel.
- Cross-channel comparison: IFC-INT-007 provides a comparison link for force fight detection without creating a common execution dependency. The link uses a simple point-to-point protocol with hardware timeout; loss of the link triggers conservative single-channel operation, not simultaneous shutdown.

### Force Fight Detection and Resolution

Both actuators drive the same steering rack. If one channel computes an incorrect position command, the two actuators can fight against each other, creating a locked-steering condition. The fault manager (CMP-SCC-01F) on each channel monitors:
- Torque output vs. commanded torque (per-channel)
- Cross-channel position command comparison (via IFC-INT-007)
- Rack position error vs. commanded position

If opposing torques exceeding 20% of commanded value persist for >50 ms, the fault manager disables the suspected faulting channel by cutting motor power to that actuator, transitioning to MODE-002.

## Architecture Decisions

### AD-01: Dual-Redundant Actuators over Single Actuator with Mechanical Fallback

**Decision:** Use two independent rack actuators (RA-A, RA-B) with no mechanical steering column fallback.

**Rationale:** A mechanical fallback column defeats the primary benefits of SbW: variable steering ratio, packaging flexibility, and decoupled cabin layout. Dual-redundant actuators provide fail-operational steering that meets UN R79 single-fault requirements without the weight, packaging, and performance compromises of a mechanical backup. Each actuator independently provides sufficient force for vehicle directional control.

**Trade-off:** Higher cost and complexity than single actuator + mechanical fallback. Requires rigorous freedom-from-interference argument for ASIL D. Accepted because the SbW value proposition depends on eliminating the mechanical column.

### AD-02: Dissimilar Silicon for Processing Channels

**Decision:** Use processor architectures from different vendors for MCU-A and MCU-B.

**Rationale:** Common-cause failures due to silicon design defects (errata) are a primary concern for dual-channel safety architectures. Using dissimilar silicon from different vendors ensures that a systematic design defect in one processor does not affect the other channel. This strengthens the freedom-from-interference argument per ISO 26262-9 clause 7 and satisfies assessor expectations for ASIL D fail-operational systems.

**Trade-off:** Dissimilar silicon increases software development effort (two toolchains, two sets of drivers) and complicates hardware qualification. Accepted because the common-cause failure argument is the linchpin of the fail-operational safety case, and assessors will scrutinize it intensively.

### AD-03: 1 kHz Control Loop Rate

**Decision:** Run the steering control loop at 1 kHz (1 ms cycle) on both processing channels.

**Rationale:** The 10 ms end-to-end latency requirement (REQ-PRF-001) and the need for crisp steering response mandate a high-rate control loop. 1 kHz provides multiple control iterations within the latency budget, supports high-bandwidth road-feel torque generation (20 Hz bandwidth requirement in REQ-FUN-004), and enables rapid fault detection (force fight detection within 50 ms requires many comparison samples). This rate is standard practice for safety-critical EPS and SbW systems.

**Trade-off:** 1 kHz demands significant MCU processing capacity and constrains the software execution budget per cycle. Accepted because steering responsiveness is the primary user experience metric and safety-critical fault detection depends on high-rate monitoring.
