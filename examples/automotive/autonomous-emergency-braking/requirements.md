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
| **Statement**    | The AEB system shall detect and classify pedestrians, cyclists, and motor vehicles within the forward sensing corridor at ranges up to 120 m for vehicles and 60 m for pedestrians using the camera detection path. |
| **Rationale**    | Camera provides classification capability necessary to distinguish vulnerable road users from non-threatening objects per UN R152 test scenarios. |
| **Source**       | UN R152 clause 5.2; CTL-001 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01E, CMP-PER-01B, CMP-CAM-01 |
| **Status**       | Baselined |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The camera detection DNN shall achieve a minimum detection rate of 99% for vehicles and 95% for pedestrians under standard test conditions (ISO 19206-compliant targets, daylight, dry road). |
| **Rationale**    | Detection rate thresholds ensure adequate sensitivity for collision avoidance. |
| **Source**       | CTL-001; UN R152 Annex 3 |
| **Parent**       | REQ-FUN-001 |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01E |
| **Status**       | Baselined |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall detect objects in the forward sensing corridor using the 77 GHz radar at ranges up to 200 m with a range accuracy of +/- 0.5 m and range-rate accuracy of +/- 0.3 m/s. |
| **Rationale**    | Radar provides all-weather range and velocity data independent of lighting conditions. |
| **Source**       | CTL-001; UN R152 clause 5.2 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01F, CMP-PER-01C, CMP-RAD-01 |
| **Status**       | Baselined |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The radar detection algorithm shall filter stationary overhead objects (bridges, signs, gantries) using radar return height estimation and range-rate analysis to prevent false positive triggers. |
| **Rationale**    | Overhead infrastructure returns are a dominant source of false activations on highway. |
| **Source**       | CTL-003; SOTIF TC-006 |
| **Parent**       | REQ-FUN-003 |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01F |
| **Status**       | Baselined |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall fuse camera and radar detections into a unified object list at a rate of not less than 25 Hz, providing 3D position (x, y, z), velocity, object class, and fusion confidence for each tracked object. |
| **Rationale**    | Sensor fusion compensates for individual sensor limitations and provides the decision layer with high-confidence object data. |
| **Source**       | CTL-001; SG-001 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01G |
| **Status**       | Baselined |

### REQ-FUN-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The sensor fusion algorithm shall assign a confidence score (0-100%) to each fused object based on the number of confirming sensor sources, measurement consistency, and track history, and shall not trigger braking for objects with a confidence score below 80%. |
| **Rationale**    | Confidence scoring prevents low-quality detections from causing false braking activations. |
| **Source**       | CTL-002; CTL-003; SG-002 |
| **Parent**       | REQ-FUN-005 |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01G |
| **Status**       | Baselined |

### REQ-FUN-007
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall track each fused object over time and predict its trajectory for a minimum of 2 seconds into the future using a motion model that accounts for constant velocity and constant turn-rate scenarios. |
| **Rationale**    | Trajectory prediction drives accurate TTC computation for crossing and cut-in scenarios. |
| **Source**       | CTL-001; UN R152 clause 5.3 |
| **Parent**       | REQ-FUN-005 |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01G |
| **Status**       | Baselined |

### REQ-FUN-008
| Field        | Value |
|--------------|-------|
| **Statement**    | The object tracking algorithm shall maintain track continuity for objects that are temporarily occluded for up to 500 ms using predicted trajectory coasting. |
| **Rationale**    | Brief occlusions (e.g., passing behind another vehicle) should not cause track drops that could delay braking. |
| **Source**       | Stakeholder need (OEM integration); CTL-001 |
| **Parent**       | REQ-FUN-007 |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01G |
| **Status**       | Baselined |

### REQ-FUN-009
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall compute time-to-collision (TTC) for each tracked object and shall determine the braking response level: no action (TTC > 2.5 s), forward collision warning (1.5 s < TTC <= 2.5 s), partial braking (0.8 s < TTC <= 1.5 s), or full emergency braking (TTC <= 0.8 s). |
| **Rationale**    | Graduated response levels provide driver warning before autonomous intervention and comply with UN R152 warning-then-braking sequence. |
| **Source**       | UN R152 clause 5.4; SG-001 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01H |
| **Status**       | Baselined |

### REQ-FUN-010
| Field        | Value |
|--------------|-------|
| **Statement**    | The collision decision logic shall require a minimum of 3 consecutive fusion cycles (120 ms at 25 Hz) of confirmed object presence before triggering partial or full braking, to suppress transient false detections. |
| **Rationale**    | Multi-frame confirmation prevents single-frame false positives from causing unnecessary braking. |
| **Source**       | CTL-003; SG-002 |
| **Parent**       | REQ-FUN-009 |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01H |
| **Status**       | Baselined |

### REQ-FUN-011
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall automatically release braking intervention when the tracked object is no longer in the collision path or when the TTC exceeds the warning threshold, with brake release completing within 200 ms of the release decision. |
| **Rationale**    | Prevents stuck-in-braking condition that could endanger following traffic. |
| **Source**       | CTL-007; SG-002 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01H, CMP-BRK-01D |
| **Status**       | Baselined |

### REQ-FUN-012
| Field        | Value |
|--------------|-------|
| **Statement**    | The Braking Control ECU shall convert the target deceleration command from the Perception ECU into a brake pressure command and shall achieve the commanded deceleration within +/- 0.5 m/s^2 under dry road conditions. |
| **Rationale**    | Brake force accuracy ensures the collision mitigation or avoidance meets the intended stopping distance. |
| **Source**       | CTL-004; SG-003 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-BRK-01D |
| **Status**       | Baselined |

### REQ-FUN-013
| Field        | Value |
|--------------|-------|
| **Statement**    | The Braking Control ECU shall arbitrate between AEB brake requests and driver brake pedal inputs, applying the higher of the two deceleration demands. |
| **Rationale**    | Driver-initiated braking should not be overridden by a lower AEB demand; AEB supplements driver action. |
| **Source**       | UN R152 clause 5.5; stakeholder need (OEM) |
| **Parent**       | REQ-FUN-012 |
| **Verification** | Test |
| **Allocation**   | CMP-BRK-01D |
| **Status**       | Baselined |

### REQ-FUN-014
| Field        | Value |
|--------------|-------|
| **Statement**    | The brake pressure controller shall implement closed-loop control with a control cycle of 5 ms and shall coordinate with the ESC system to prevent wheel lock-up during AEB intervention. |
| **Rationale**    | Closed-loop control with ABS coordination maintains vehicle stability during emergency braking. |
| **Source**       | CTL-004; SG-003 |
| **Parent**       | REQ-FUN-012 |
| **Verification** | Test |
| **Allocation**   | CMP-BRK-01E, CMP-BRK-01B |
| **Status**       | Baselined |

### REQ-FUN-015
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall limit the commanded deceleration to a maximum of 10 m/s^2 during full emergency braking and shall respect ESC stability corrections that reduce brake force on individual wheels. |
| **Rationale**    | Deceleration limit prevents vehicle instability on low-friction surfaces; ESC override maintains directional control. |
| **Source**       | CTL-004; CTL-005; SG-003 |
| **Parent**       | REQ-FUN-012 |
| **Verification** | Test |
| **Allocation**   | CMP-BRK-01D, CMP-BRK-01E |
| **Status**       | Baselined |

### REQ-FUN-016
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall generate a visual collision warning on the instrument cluster and an audible warning tone at the forward collision warning threshold (TTC <= 2.5 s), at least 500 ms before any autonomous braking intervention. |
| **Rationale**    | Driver warning provides opportunity for driver-initiated evasive action before autonomous braking. |
| **Source**       | UN R152 clause 5.4.1; stakeholder need (driver) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01H, CMP-GWY-01D |
| **Status**       | Baselined |

### REQ-FUN-017
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall continuously monitor the health of the camera and radar sensors using diagnostic coverage mechanisms with a minimum diagnostic coverage of 90% for each sensor. |
| **Rationale**    | Sensor health monitoring enables detection of degraded perception before it causes hazardous braking decisions. |
| **Source**       | CTL-008; SG-005 |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-PER-01D, CMP-PER-01E, CMP-PER-01F |
| **Status**       | Baselined |

### REQ-FUN-018
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall transition to MODE-003 (Degraded Perception) within 100 ms of detecting a sensor fault, and shall annunciate the degraded state to the driver via the instrument cluster. |
| **Rationale**    | Timely degradation prevents hazardous decisions based on faulty sensor data. |
| **Source**       | CTL-008; HZ-008; SG-005 |
| **Parent**       | REQ-FUN-017 |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01D, CMP-GWY-01D |
| **Status**       | Baselined |

### REQ-FUN-019
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall execute power-up self-test on all ECUs and sensors within 5 seconds of ignition-on and shall report readiness status to the vehicle network before transitioning to MODE-001. |
| **Rationale**    | Pre-drive self-test detects latent faults before the AEB system becomes operational. |
| **Source**       | CTL-008; ISO 26262-5 clause 7.4.4 (latent fault detection) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01, CMP-BRK-01, CMP-GWY-01 |
| **Status**       | Baselined |

### REQ-FUN-020
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall support camera and radar alignment verification using calibration targets, with alignment accuracy of +/- 0.5 degrees in azimuth and elevation, during MODE-004 (Maintenance/Calibration). |
| **Rationale**    | Sensor misalignment causes systematic detection errors; calibration must be verified after installation or windshield replacement. |
| **Source**       | Stakeholder need (maintenance); ISO 21448 clause 10 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01E, CMP-PER-01F |
| **Status**       | Baselined |

### REQ-FUN-021
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall record pre-event data (5 seconds of object tracking, braking commands, vehicle dynamics) and event data (braking activation, duration, deceleration achieved) for each AEB intervention, stored in non-volatile memory. |
| **Rationale**    | Event data recording supports post-collision analysis and regulatory compliance. |
| **Source**       | Stakeholder need (OEM, regulatory); UN R152 clause 6.4 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01K |
| **Status**       | Baselined |

### REQ-FUN-022
| Field        | Value |
|--------------|-------|
| **Statement**    | The Perception ECU OTA update agent shall validate incoming software packages using cryptographic signature verification (ECDSA P-256), verify package integrity using SHA-256 hash, and maintain rollback capability to the previous known-good software version. |
| **Rationale**    | Prevents installation of corrupted or malicious software that could disable or degrade AEB function. |
| **Source**       | CTL-009; THR-001; THR-002 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01J, CMP-GWY-01E |
| **Status**       | Baselined |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall detect at least 95% of relevant obstacles (vehicles, pedestrians, cyclists) within the operational design domain using dual-sensor (camera + radar) fusion, and the probability of undetected obstacle leading to collision shall not exceed 1 x 10^-8 per hour of operation. |
| **Rationale**    | Detection reliability is the primary safety function; dual-sensor fusion provides defense against single-sensor failures. |
| **Source**       | HZ-001; HZ-002; CTL-001; SG-001 |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-PER-01E, CMP-PER-01F, CMP-PER-01G |
| **Status**       | Baselined |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The sensor fusion algorithm shall require confirmation from at least one sensor source (camera or radar) with a track history of at least 3 cycles before accepting an object as valid for braking decisions. |
| **Rationale**    | Confirmation requirement prevents low-quality or transient detections from causing erroneous braking decisions. |
| **Source**       | HZ-001; HZ-012; CTL-002 |
| **Parent**       | REQ-SAF-001 |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01G |
| **Status**       | Baselined |

### REQ-SAF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall limit false positive braking activations (braking when no collision threat exists) to fewer than 1 event per 100,000 km of driving under representative traffic conditions. |
| **Rationale**    | False activations are hazardous to following traffic and erode driver trust. |
| **Source**       | HZ-003; CTL-003; SG-002 |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-PER-01G, CMP-PER-01H |
| **Status**       | Baselined |

### REQ-SAF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The Braking Control ECU shall achieve the commanded deceleration within 150 ms of brake command receipt for full emergency braking (TTC <= 0.8 s). |
| **Rationale**    | Brake actuation latency directly impacts collision avoidance effectiveness; 150 ms brake system response is within the 300 ms total system latency budget. |
| **Source**       | HZ-004; CTL-004; SG-003 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-BRK-01D, CMP-BRK-01E, CMP-BRK-01B |
| **Status**       | Baselined |

### REQ-SAF-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall coordinate with the ESC system such that ESC stability corrections take precedence over AEB deceleration commands when the ESC detects loss of vehicle stability. |
| **Rationale**    | Vehicle stability takes precedence over collision mitigation to prevent secondary loss-of-control accidents. |
| **Source**       | HZ-005; CTL-005 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-BRK-01D, CMP-BRK-01E |
| **Status**       | Baselined |

### REQ-SAF-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The end-to-end latency from camera frame capture to brake pressure rise initiation shall not exceed 300 ms under worst-case processing conditions. |
| **Rationale**    | Total system latency budget determines minimum collision avoidance capability per UN R152 stopping distance requirements. |
| **Source**       | HZ-006; CTL-006; SG-004 |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-PER-01 (system-level), CMP-BRK-01, CMP-GWY-01 |
| **Status**       | Baselined |

### REQ-SAF-007
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall automatically release braking intervention within 3 seconds of the braking trigger, or when the object tracker confirms the collision threat has cleared, whichever occurs first. |
| **Rationale**    | Prevents stuck-in-braking condition that could endanger following vehicles. |
| **Source**       | HZ-007; CTL-007 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01H, CMP-BRK-01D |
| **Status**       | Baselined |

### REQ-SAF-008
| Field        | Value |
|--------------|-------|
| **Statement**    | The Braking Control ECU shall achieve a single-point fault metric (SPFM) of not less than 99% and a latent fault metric (LFM) of not less than 90% for the braking actuation path, verified by quantitative hardware fault analysis per ISO 26262-5. |
| **Rationale**    | ASIL D hardware fault metrics for the braking path require the highest diagnostic coverage. |
| **Source**       | HZ-008; ISO 26262-5 Table 4 (ASIL D) |
| **Parent**       | — |
| **Verification** | Analysis |
| **Allocation**   | CMP-BRK-01A, CMP-BRK-01B, CMP-BRK-01D, CMP-BRK-01E |
| **Status**       | Baselined |

### REQ-SAF-009
| Field        | Value |
|--------------|-------|
| **Statement**    | When the AEB system operates in MODE-003 (Degraded Perception), the system shall extend TTC warning and braking thresholds by a factor of 1.5 and shall limit AEB operating speed to 80 km/h. |
| **Rationale**    | Extended thresholds compensate for reduced detection capability in degraded mode, limiting AEB operation to scenarios where the remaining sensor can still provide adequate detection. |
| **Source**       | HZ-011; CTL-011; SG-005 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01H |
| **Status**       | Baselined |

### REQ-SAF-010
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall monitor sensor fusion confidence continuously and shall transition to MODE-003 when the aggregate fusion confidence drops below 60% for more than 500 ms, indicating a SOTIF triggering condition. |
| **Rationale**    | SOTIF-aware degradation ensures the system does not make braking decisions when perception quality is insufficient. |
| **Source**       | HZ-011; HZ-012; CTL-011; ISO 21448 clause 6.3 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01G, CMP-PER-01H |
| **Status**       | Baselined |

## Security Requirements

### REQ-SEC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall verify the cryptographic signature of all OTA update packages using ECDSA P-256 or equivalent before installation, and shall reject packages that fail signature verification. |
| **Rationale**    | Prevents installation of tampered or malicious software that could disable AEB. |
| **Source**       | THR-001; THR-002; CTL-009 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01J, CMP-GWY-01E |
| **Status**       | Baselined |

### REQ-SEC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The OTA update agent shall reject update packages with a version number equal to or lower than the currently installed version to prevent rollback attacks. |
| **Rationale**    | Prevents replay of outdated software that may contain known vulnerabilities. |
| **Source**       | THR-002; CTL-009 |
| **Parent**       | REQ-SEC-001 |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01J |
| **Status**       | Baselined |

### REQ-SEC-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The Vehicle Gateway ECU shall filter all CAN FD messages crossing domain boundaries against a static allowlist of permitted message IDs and source addresses, and shall drop messages not on the allowlist. |
| **Rationale**    | Prevents unauthorized message injection from reaching the safety-critical braking domain. |
| **Source**       | THR-003; THR-004; CTL-010 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-GWY-01E |
| **Status**       | Baselined |

### REQ-SEC-004
| Field        | Value |
|--------------|-------|
| **Statement**    | All safety-relevant CAN FD messages between the Vehicle Gateway ECU and Braking Control ECU shall be protected with AUTOSAR E2E Profile 7 (CRC-64, rolling counter, data ID), and the receiving ECU shall reject messages with invalid E2E checks. |
| **Rationale**    | E2E protection detects message corruption, loss, repetition, and injection on the safety-critical communication path. |
| **Source**       | THR-003; THR-005; CTL-010 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-GWY-01C, CMP-BRK-01C |
| **Status**       | Baselined |

### REQ-SEC-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The Vehicle Gateway ECU shall implement an intrusion detection system that monitors CAN FD bus traffic for anomalous message rates, unexpected message IDs, and timing violations, and shall log detected anomalies as security events. |
| **Rationale**    | Intrusion detection provides defense-in-depth beyond the static allowlist filter. |
| **Source**       | THR-003; THR-004; CTL-010 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-GWY-01E |
| **Status**       | Baselined |

### REQ-SEC-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall require ISO 14229 security access (service 0x27) with challenge-response authentication before allowing diagnostic write operations to safety-relevant calibration parameters. |
| **Rationale**    | Prevents unauthorized modification of safety-relevant parameters via the diagnostic interface. |
| **Source**       | THR-006 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-GWY-01C, CMP-BRK-01C |
| **Status**       | Baselined |

### REQ-SEC-007
| Field        | Value |
|--------------|-------|
| **Statement**    | The Perception ECU shall verify the integrity of the DNN model and fusion parameter files on each power cycle using hardware-enforced secure boot with a hardware root of trust. |
| **Rationale**    | Secure boot prevents execution of tampered perception software that could cause systematic missed detections. |
| **Source**       | THR-001; THR-008; CTL-009 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01A, CMP-PER-01D |
| **Status**       | Baselined |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The Perception ECU shall transmit braking request messages to the Vehicle Gateway ECU via IFC-INT-003 at a rate of 50 Hz with a maximum latency of 10 ms from decision computation to Ethernet frame transmission, using SOME/IP with E2E protection. |
| **Rationale**    | Braking request freshness drives collision avoidance timing; 50 Hz update rate supports the 20 ms decision cycle. |
| **Source**       | Gateway ICD; CTL-006 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01H, CMP-PER-01D |
| **Status**       | Baselined |

### REQ-IFC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The Vehicle Gateway ECU shall translate SOME/IP braking commands from Ethernet to CAN FD messages and forward them to the Braking Control ECU via IFC-INT-004 within 5 ms of Ethernet frame receipt, maintaining E2E protection continuity. |
| **Rationale**    | Gateway translation latency is part of the 300 ms total system latency budget. |
| **Source**       | Braking ECU ICD; CTL-006 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-GWY-01D, CMP-GWY-01C |
| **Status**       | Baselined |

### REQ-IFC-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The Vehicle Gateway ECU shall forward vehicle dynamics data (wheel speed, yaw rate, steering angle, ESC status) from the CAN domain to the Perception ECU via IFC-INT-006 at the source sensor rate (10 ms cycle) with a forwarding latency of not more than 5 ms. |
| **Rationale**    | Vehicle dynamics data is required for ego motion estimation and TTC computation accuracy. |
| **Source**       | Perception ECU ICD |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-GWY-01D |
| **Status**       | Baselined |

### REQ-IFC-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The Braking Control ECU shall report brake status (actual brake pressure, actual deceleration, fault status) to the Vehicle Gateway ECU via IFC-INT-005 at a rate of 100 Hz with E2E Profile 7 protection. |
| **Rationale**    | Brake feedback enables the Perception ECU to verify that commanded braking is being achieved. |
| **Source**       | Braking ECU ICD; CTL-004 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-BRK-01D, CMP-BRK-01C |
| **Status**       | Baselined |

### REQ-IFC-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall transmit a torque reduction request to the Powertrain Control Module via IFC-EXT-004 simultaneously with any AEB braking command, to reduce engine torque and avoid powertrain-brake conflict. |
| **Rationale**    | Engine torque reduction during AEB braking prevents brake fade and improves stopping distance. |
| **Source**       | Powertrain ICD; stakeholder need (OEM) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-GWY-01D |
| **Status**       | Baselined |

## Performance Requirements

### REQ-PRF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The total end-to-end latency from camera frame capture to brake pressure rise initiation shall not exceed 300 ms under worst-case processing and communication conditions. |
| **Rationale**    | 300 ms total latency budget is derived from UN R152 stopping distance requirements at maximum AEB operating speed. |
| **Source**       | CTL-006; SG-004; UN R152 Annex 3 |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-PER-01 (system-level), CMP-BRK-01, CMP-GWY-01 |
| **Status**       | Baselined |

### REQ-PRF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The DNN inference on the Perception ECU NPU shall complete within 30 ms per camera frame at 30 fps, providing a minimum 10% timing margin under worst-case thermal and power conditions. |
| **Rationale**    | DNN inference timing is the largest single contributor to the perception pipeline latency. |
| **Source**       | CTL-006; architecture timing budget |
| **Parent**       | REQ-PRF-001 |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-PER-01A, CMP-PER-01E |
| **Status**       | Baselined |

### REQ-PRF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall operate continuously from vehicle ignition-on to ignition-off without performance degradation, across the full ambient temperature range of -40C to +85C, and shall enter MODE-001 within 5 seconds of ignition-on. |
| **Rationale**    | AEB must be operational throughout every drive cycle; startup time must be minimized for safety. |
| **Source**       | Stakeholder need (OEM); UN R152 clause 5.1 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01, CMP-BRK-01, CMP-GWY-01 |
| **Status**       | Baselined |

### REQ-PRF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall achieve the following UN R152 test performance: reduce speed by at least 20 km/h for stationary vehicle target approach at 50 km/h, and achieve full stop for pedestrian crossing at 40 km/h. |
| **Rationale**    | Minimum performance thresholds required for UN R152 type approval. |
| **Source**       | UN R152 Annex 3 Table 1; SG-001 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01 (system-level), CMP-BRK-01 |
| **Status**       | Baselined |

### REQ-PRF-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The AEB system shall consume no more than 35 watts total across all three ECUs under maximum processing load conditions. |
| **Rationale**    | Power budget constraint for vehicle electrical load analysis and thermal management. |
| **Source**       | Vehicle electrical specification; stakeholder need (OEM) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01, CMP-BRK-01, CMP-GWY-01 |
| **Status**       | Baselined |
