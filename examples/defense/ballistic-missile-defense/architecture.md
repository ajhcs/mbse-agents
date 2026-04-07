# Architecture

## System Context

```mermaid
graph TB
    subgraph BMDE["Ballistic Missile Defense Element"]
        TMS["CMP-TMS-01<br/>Track Management Subsystem"]
        ECP["CMP-ECP-01<br/>Engagement Coordination Processor"]
        BDS["CMP-BDS-01<br/>Battle Management Display Suite"]
        CGW["CMP-CGW-01<br/>C2 Communications Gateway"]
    end

    SBIRS["SBIRS / OPIR<br/>(Space-Based Sensors)"]
    RADAR_FWD["Forward Radar<br/>(AN/TPY-2)"]
    RADAR_SEA["Sea-Based Radar<br/>(SPY-7 / Aegis)"]
    INTERCEPT_GBI["GBI Launch System"]
    INTERCEPT_SM3["SM-3 / Aegis BMD"]
    INTERCEPT_THAAD["THAAD Battery"]
    NCA["National Command Authority"]
    ADJ_BMDE["Adjacent BMDS Elements"]
    COCOM["COCOM C2 Network"]

    SBIRS -->|Track data (OPIR)| CGW
    RADAR_FWD -->|Radar tracks| CGW
    RADAR_SEA -->|Radar tracks| CGW
    CGW -->|Fused track data| TMS
    TMS -->|Correlated tracks| ECP
    ECP -->|Fire control commands| CGW
    CGW -->|Fire control| INTERCEPT_GBI
    CGW -->|Fire control| INTERCEPT_SM3
    CGW -->|Fire control| INTERCEPT_THAAD
    NCA -->|Engagement authority| ECP
    ECP -->|Engagement status| BDS
    ADJ_BMDE <-->|Coordination messages| CGW
    COCOM -->|Defended asset priorities| ECP
    ECP -->|Engagement reports| COCOM
```

## Functional Architecture

### System Functions

| FUN ID       | Function Name                      | Description                                                                      | Inputs                                      | Outputs                                     | Dependencies         |
|--------------|------------------------------------|----------------------------------------------------------------------------------|---------------------------------------------|---------------------------------------------|----------------------|
| FUN-TRK-01   | Multi-Source Track Fusion           | Receive, correlate, and fuse track data from multiple sensor sources             | Sensor track messages via CGW               | Composite track file, correlation confidence | None                 |
| FUN-TRK-02   | Track Classification               | Classify correlated tracks as ballistic threat, cruise threat, debris, or unknown | Correlated track kinematics, sensor phenomenology | Track classification, discrimination confidence | FUN-TRK-01           |
| FUN-TRK-03   | Track State Prediction             | Predict threat trajectory for engagement planning and interceptor guidance       | Correlated track state, atmospheric model   | Predicted impact point, trajectory state vector | FUN-TRK-01           |
| FUN-ENG-01   | Weapon-Target Pairing              | Assign interceptors to threats based on defended asset priority and Pk optimization | Classified tracks, interceptor inventory, defended asset list | Weapon-target assignments, engagement sequence | FUN-TRK-02, FUN-TRK-03 |
| FUN-ENG-02   | Engagement Authority Enforcement   | Enforce positive fire control and engagement authority chain                     | Operator authorization, NCA delegation      | Authorized engagement commands               | FUN-ENG-01           |
| FUN-ENG-03   | Engagement Coordination            | Coordinate shoot-look-shoot and deconfliction with adjacent BMDS elements       | Adjacent element status, engagement assignments | Coordination messages, deconfliction results | FUN-ENG-01           |
| FUN-CMD-01   | Fire Control Command Generation    | Generate and transmit fire control commands to interceptor launch systems        | Authorized engagement, interceptor interface data | Fire control messages via CGW               | FUN-ENG-02           |
| FUN-BIT-01   | Built-In Test                      | Power-up and continuous BIT for all BMDE subsystems                              | BIT commands, health data                   | Fault reports, subsystem status              | None                 |
| FUN-SIM-01   | Training Simulation                | Inject simulated threat tracks for operator training                            | Scenario data, training parameters          | Simulated track feed                         | FUN-TRK-01           |

## Physical Architecture

### Component Hierarchy

| CMP ID        | Component Name                          | Type     | Parent        | Description                                                          |
|---------------|-----------------------------------------|----------|---------------|----------------------------------------------------------------------|
| CMP-TMS-01    | Track Management Subsystem              | Subsystem| System        | Multi-source track fusion, correlation, classification, prediction   |
| CMP-TMS-01A   | Track Fusion Processor                  | Module   | CMP-TMS-01    | Real-time track correlation and fusion from multiple sensor feeds    |
| CMP-TMS-01B   | Track Discrimination Engine             | Software | CMP-TMS-01    | Kinematic and phenomenology-based threat discrimination              |
| CMP-ECP-01    | Engagement Coordination Processor       | Subsystem| System        | Weapon-target pairing, engagement authority, fire control            |
| CMP-ECP-01A   | Fire Control Processor                  | Module   | CMP-ECP-01    | Fire control command generation and positive control enforcement     |
| CMP-ECP-01B   | Threat Assessment Engine                | Software | CMP-ECP-01    | Threat classification and engagement priority computation            |
| CMP-ECP-01C   | Weapon-Target Pairing Optimizer         | Software | CMP-ECP-01    | Optimal interceptor assignment against defended asset priorities     |
| CMP-BDS-01    | Battle Management Display Suite         | Subsystem| System        | Operator situational awareness and engagement authorization display |
| CMP-BDS-01A   | Battle Management Display Processor     | Module   | CMP-BDS-01    | Track display, engagement status rendering, operator input           |
| CMP-CGW-01    | C2 Communications Gateway               | Subsystem| System        | BMDS data link management, message routing, COMSEC                   |
| CMP-CGW-01A   | BMDS Link Processor                     | Module   | CMP-CGW-01    | Multi-link message handling, source authentication, routing          |
| CMP-CGW-01B   | COMSEC Module                           | Hardware | CMP-CGW-01    | Type 1 cryptographic processing for all classified data links        |

## Allocation

| FUN ID       | REQ ID(s)                          | CMP ID(s)                         | Assurance Level | Rationale                                                       |
|--------------|------------------------------------|-----------------------------------|-----------------|------------------------------------------------------------------|
| FUN-TRK-01   | REQ-FUN-001, REQ-FUN-002          | CMP-TMS-01A, CMP-TMS-01B         | SIL 3           | Track data quality drives engagement decision accuracy           |
| FUN-TRK-02   | REQ-FUN-003                        | CMP-ECP-01B                       | SIL 3           | Misclassification directly impacts engagement effectiveness      |
| FUN-TRK-03   | REQ-PRF-001                        | CMP-TMS-01A, CMP-TMS-01B         | SIL 3           | Trajectory prediction accuracy drives interceptor guidance       |
| FUN-ENG-01   | REQ-FUN-004                        | CMP-ECP-01C                       | SIL 3           | Pairing optimization directly affects defended asset coverage    |
| FUN-ENG-02   | REQ-SAF-001, REQ-SAF-002, REQ-SAF-003 | CMP-ECP-01A, CMP-BDS-01A    | SIL 4           | Engagement authority enforcement is highest safety criticality   |
| FUN-ENG-03   | REQ-IFC-002                        | CMP-CGW-01A, CMP-ECP-01C         | SIL 3           | Uncoordinated engagement wastes interceptor inventory            |
| FUN-CMD-01   | REQ-FUN-005                        | CMP-ECP-01A, CMP-CGW-01A         | SIL 4           | Fire control commands directly cause interceptor launch          |
| FUN-BIT-01   | —                                  | All CMP-                          | SIL 2           | BIT supports fault detection before engagement                   |
| FUN-SIM-01   | —                                  | CMP-TMS-01A                       | SIL 1           | Training function; no live engagement capability                 |

## Interfaces

### External Interfaces

| IFC ID       | Partner System                   | Data Item                             | Direction     | Protocol            | Timing              |
|--------------|----------------------------------|---------------------------------------|---------------|---------------------|----------------------|
| IFC-EXT-001  | SBIRS / OPIR Sensors             | Space-based IR track data             | In            | BMDS OPIR datalink  | 2 s update rate      |
| IFC-EXT-002  | Forward/Sea-Based Radars         | Radar track data                      | In            | BMDS radar datalink | 1 s update rate      |
| IFC-EXT-003  | Interceptor Launch Systems       | Fire control commands, status replies | Bidirectional | BMDS fire control link | 500 ms command rate |
| IFC-EXT-004  | Adjacent BMDS Elements           | Engagement coordination messages      | Bidirectional | BMDS C2 network     | Event-driven         |
| IFC-EXT-005  | COCOM C2 Network                 | Defended asset priorities, engagement reports | Bidirectional | TCP/IP (SIPR) | On demand            |
| IFC-EXT-006  | NCA Authority Chain              | Engagement authorization directives   | In            | Secure voice / data | Event-driven         |

### Internal Interfaces

| IFC ID       | Source CMP ID  | Target CMP ID  | Data Item                              | Mechanism           | Timing              |
|--------------|----------------|-----------------|----------------------------------------|---------------------|----------------------|
| IFC-INT-001  | CMP-CGW-01     | CMP-TMS-01      | Validated sensor track messages        | Internal Ethernet   | Per sensor rate      |
| IFC-INT-002  | CMP-TMS-01     | CMP-ECP-01      | Correlated track file updates          | Internal Ethernet   | 500 ms               |
| IFC-INT-003  | CMP-ECP-01     | CMP-CGW-01      | Fire control commands                  | Internal Ethernet   | Event-driven         |
| IFC-INT-004  | CMP-ECP-01     | CMP-BDS-01      | Engagement status, track display data  | Internal Ethernet   | 1 Hz                 |
| IFC-INT-005  | CMP-BDS-01     | CMP-ECP-01      | Operator authorization inputs          | Internal Ethernet   | Event-driven         |

## Failure Containment / Partitioning

### SoS Boundary Containment

The BMDE's primary partitioning strategy exploits the system-of-systems architecture: sensors, the BMDE, and interceptor launch systems are independently operated systems connected by defined datalinks. A failure within the BMDE cannot directly cause an interceptor to launch because the interceptor launch system enforces its own positive fire control sequence. The BMDE transmits fire control commands, but the interceptor system independently verifies command authentication before executing launch. This provides a two-level positive control barrier.

**Internal partitioning:**
- Track Management and Engagement Coordination are separate subsystems on independent processors. A TMS fault (track corruption) does not propagate to ECP except through the validated track interface.
- The Fire Control Processor (CMP-ECP-01A) runs on a dedicated processor partition isolated from the Weapon-Target Pairing Optimizer (CMP-ECP-01C). A pairing algorithm fault does not affect fire control command integrity.
- The COMSEC module (CMP-CGW-01B) enforces a cryptographic boundary between the BMDE internal network and all external datalinks.

**Evidence**: MIL-STD-882E safety assessment verifies that no single BMDE failure can result in an inadvertent interceptor launch.

## Architecture Decisions

### AD-01: Centralized Track Fusion over Distributed Sensor-Level Fusion

**Decision:** Perform track correlation and fusion centrally within the BMDE rather than relying on sensor-level fused tracks.

**Rationale:** Individual sensors provide single-phenomenology data (IR only from SBIRS, radar-only from AN/TPY-2). Central fusion within the BMDE enables cross-phenomenology correlation that improves discrimination confidence beyond what any single sensor can achieve. The SoS architecture means sensor systems are acquired independently and do not share a common track fusion implementation.

**Trade-off:** Central fusion requires high-bandwidth, low-latency sensor feeds to the BMDE. Accepted because the discrimination improvement from multi-phenomenology fusion is essential for countermeasure-resistant engagement decisions.

### AD-02: Two-Level Positive Fire Control

**Decision:** Implement positive fire control enforcement at both the BMDE (operator authorization) and the interceptor launch system (independent command authentication), rather than relying on BMDE-only control.

**Rationale:** MIL-STD-882E severity analysis rates inadvertent interceptor launch as Catastrophic. A single-level control creates a single point of failure for the highest-severity hazard. The two-level approach ensures that neither a BMDE software fault nor a datalink corruption can independently cause an inadvertent launch.

**Trade-off:** Two-level authentication adds latency to the fire control command path. Accepted because the safety argument for inadvertent launch prevention outweighs the engagement timeline cost.

### AD-03: Separated Track Management and Engagement Subsystems

**Decision:** Implement Track Management and Engagement Coordination as physically separate subsystems with a defined track interface rather than a single integrated processor.

**Rationale:** Track fusion is a computationally intensive real-time signal processing function. Engagement coordination is an optimization and decision-support function. Separating them prevents track processing load from starving engagement computation and provides a clean failure containment boundary: a TMS fault degrades the track picture but does not corrupt active engagement state.

**Trade-off:** Separation increases system complexity and inter-subsystem interface overhead. Accepted because the failure containment and computational isolation benefits justify the additional integration cost.
