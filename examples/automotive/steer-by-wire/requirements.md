# Requirements

All requirements are atomic, testable shall-statements.

## Requirement Record Schema

| Field         | Description                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------|
| ID            | Unique identifier (e.g., REQ-FUN-001)                                                            |
| Statement     | Atomic shall-statement                                                                            |
| Rationale     | Why this requirement exists                                                                       |
| Source        | Hazard ID (HZ-), control ID (CTL-), threat ID (THR-), regulatory clause, or stakeholder need     |
| Parent        | Parent requirement ID (if derived)                                                                |
| Verification  | Method: test, analysis, inspection, demonstration                                                 |
| Allocation    | Target component ID(s) from architecture.md                                                       |
| Status        | Draft, baselined, verified, deferred                                                              |

## Functional Requirements

### REQ-FUN-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The SbW system shall read driver steering torque and steering wheel angle from the steering wheel sensor unit with a torque accuracy of +/- 0.1 Nm and angle accuracy of +/- 0.5 degrees, at a sampling rate of not less than 1 kHz. |
| **Rationale**    | High-resolution, high-rate steering input is necessary for responsive rack position control and accurate torque feedback generation. |
| **Source**       | UN R79 clause 5.1.4; stakeholder need (OEM steering feel) |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-SWS-01, CMP-SWS-01A, CMP-SWS-01B |
| **Status**       | Baselined |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The SbW system shall convert driver steering input into a target rack position and shall command the rack actuators to achieve the target position within +/- 0.5 mm accuracy under normal driving conditions. |
| **Rationale**    | Rack position accuracy translates directly to vehicle directional accuracy; 0.5 mm corresponds to approximately 0.05 degrees of road wheel angle. |
| **Source**       | Stakeholder need (OEM vehicle dynamics); UN R79 |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-SCC-01, CMP-SCC-01C, CMP-RA-A, CMP-RA-B |
| **Status**       | Baselined |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The SbW system shall implement a variable steering ratio that adjusts from 12:1 at highway speeds (above 80 km/h) to 8:1 at low speeds (below 30 km/h), with smooth interpolation between ratio endpoints. |
| **Rationale**    | Variable ratio improves low-speed maneuverability while providing stability at highway speeds, a key advantage of SbW over fixed-ratio mechanical steering. |
| **Source**       | Stakeholder need (OEM vehicle dynamics tuning) |
| **Parent**       | REQ-FUN-002 |
| **Verification** | Test |
| **Allocation**   | CMP-SCC-01C |
| **Status**       | Baselined |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The handwheel feedback actuator shall generate road-feel torque proportional to estimated tire-road interaction forces, with a torque bandwidth of not less than 20 Hz and maximum torque capability of 8 Nm. |
| **Rationale**    | Road-feel torque provides the driver with steering feedback essential for vehicle control and driver confidence. The 20 Hz bandwidth ensures the driver perceives road surface changes and limit conditions. |
| **Source**       | Stakeholder need (OEM steering feel); ISO 21448 (SOTIF -- incorrect feel could mislead driver) |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-HFA-01, CMP-SCC-01D |
| **Status**       | Baselined |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The SbW system shall accept steering overlay commands from the ADAS lane-keeping assist function via IFC-EXT-003 and shall superimpose the ADAS rack position offset onto the driver-commanded position, limited to a maximum overlay authority of +/- 3 degrees of road wheel angle. |
| **Rationale**    | ADAS integration requires the SbW system to accept external steering inputs while limiting ADAS authority to prevent unintended large steering interventions. |
| **Source**       | Stakeholder need (ADAS integration); ISO 21448 (SOTIF -- ADAS overlay limits) |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-SCC-01C, CMP-SCC-01E |
| **Status**       | Baselined |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The SbW system shall maintain steering functionality after any single fault, with a maximum interruption of 50 ms during fault detection and switchover to the surviving channel. |
| **Rationale**    | With no mechanical fallback, loss of steering is ASIL D. Fail-operational behavior after a single fault is mandatory per UN R79 and the HARA. |
| **Source**       | UN R79 clause 5.1.6 (single-fault performance); ISO 26262 HARA (ASIL D) |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-SCC-01, CMP-RA-A, CMP-RA-B, CMP-SCC-01B |
| **Status**       | Baselined |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | Rack Actuator A and Rack Actuator B shall be capable of independently providing full steering rack travel with a minimum assist torque of 50% of nominal, such that either actuator alone can maintain vehicle directional control. |
| **Rationale**    | Each actuator must be independently sufficient for safe vehicle operation after failure of the other, supporting the fail-operational architecture. |
| **Source**       | UN R79 clause 5.1.6; ISO 26262 HARA (ASIL D) |
| **Parent**       | REQ-SAF-001 |
| **Verification** | Test |
| **Allocation**   | CMP-RA-A, CMP-RA-B |
| **Status**       | Baselined |

### REQ-SAF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The dual processing channels within the SCC shall execute independently with freedom from interference enforced by separate processor cores, separated memory spaces, and independent power regulation, per ISO 26262-9 clause 7 (freedom from interference). |
| **Rationale**    | A common-cause fault affecting both processing channels would eliminate steering, violating the fail-operational requirement. Independence must be demonstrated at the hardware level. |
| **Source**       | ISO 26262-9 clause 7; ISO 26262 HARA (ASIL D) |
| **Parent**       | REQ-SAF-001 |
| **Verification** | Analysis, Inspection |
| **Allocation**   | CMP-SCC-01A, CMP-SCC-01B |
| **Status**       | Baselined |

### REQ-SAF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The SbW system shall detect actuator force fight between RA-A and RA-B (opposing torque exceeding 20% of commanded torque for more than 50 ms) and shall disable the faulting actuator within 100 ms. |
| **Rationale**    | Both actuators driving the same rack can produce opposing forces if one channel has a command error, creating a locked-steering hazard. Force fight detection is a critical safety mechanism. |
| **Source**       | ISO 26262 HARA (ASIL D -- unintended steering); UN R79 |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-SCC-01B, CMP-RA-A, CMP-RA-B |
| **Status**       | Baselined |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The SCC shall receive vehicle dynamics data (vehicle speed, yaw rate, lateral acceleration) from the vehicle dynamics controller via IFC-EXT-002 at a rate of 100 Hz with E2E protection, with a maximum age of 15 ms at point of use. |
| **Rationale**    | Vehicle dynamics data is required for variable steering ratio computation and road-feel torque model input. Data freshness is critical for stability at highway speeds. |
| **Source**       | Vehicle dynamics controller ICD; architecture timing budget |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-SCC-01, CMP-SCC-01C, CMP-SCC-01D |
| **Status**       | Baselined |

### REQ-IFC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The SbW system shall provide rack position, steering status, and fault information to the vehicle dynamics controller and instrument cluster via IFC-EXT-004 at a rate of 100 Hz with E2E protection. |
| **Rationale**    | Vehicle dynamics controller requires current rack position for stability control functions; instrument cluster displays SbW status to the driver. |
| **Source**       | Vehicle dynamics controller ICD; stakeholder need (OEM) |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-SCC-01, CMP-SCC-01C |
| **Status**       | Baselined |

## Performance Requirements

### REQ-PRF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The end-to-end latency from driver steering input to rack actuator force application shall not exceed 10 ms under worst-case processing and communication conditions. |
| **Rationale**    | Steering responsiveness directly impacts vehicle stability and driver control feel. 10 ms total latency ensures imperceptible delay from the driver's perspective. |
| **Source**       | Stakeholder need (OEM steering dynamics); UN R79 response time |
| **Parent**       | -- |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-SWS-01, CMP-SCC-01, CMP-RA-A, CMP-RA-B |
| **Status**       | Baselined |
