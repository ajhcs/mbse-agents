# Requirements

All requirements are atomic, testable shall-statements.

## Requirement Record Schema

| Field         | Description                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------|
| ID            | Unique identifier (e.g., REQ-FUN-001)                                                            |
| Statement     | Atomic shall-statement                                                                            |
| Rationale     | Why this requirement exists                                                                       |
| Source        | Regulatory clause, stakeholder need, or parent requirement                                        |
| Parent        | Parent requirement ID (if derived)                                                                |
| Verification  | Method: test, analysis, inspection, demonstration                                                 |
| Allocation    | Target component ID(s) from architecture.md                                                       |
| Status        | Draft, baselined, verified, deferred                                                              |

## Functional Requirements

### REQ-FUN-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The GN&C computer shall compute vehicle state (position, velocity, attitude) using IMU data at a navigation update rate of not less than 50 Hz. |
| **Rationale**    | Navigation update rate drives guidance accuracy and thrust vector control loop stability during powered flight. |
| **Source**       | Vehicle trajectory requirements; GN&C performance specification |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-GNC-01 |
| **Status**       | Draft |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The GN&C computer shall generate thrust vector control (TVC) commands to maintain vehicle attitude within +/-0.5 degrees of the commanded trajectory during powered flight. |
| **Rationale**    | Attitude accuracy during powered flight directly determines orbit insertion accuracy and prevents trajectory violation that could trigger flight termination. |
| **Source**       | Vehicle trajectory requirements; payload orbit insertion specification |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-GNC-01 |
| **Status**       | Draft |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The vehicle management unit shall execute the flight sequence timeline including engine start, engine cutoff, staging separation, payload fairing jettison, and payload separation, with command timing accuracy within +/-10 ms of the planned timeline. |
| **Rationale**    | Sequence timing accuracy prevents premature or late separation events that could damage the vehicle or payload. |
| **Source**       | Vehicle integration ICD; mission timeline specification |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-VMU-01 |
| **Status**       | Draft |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The telemetry system shall acquire, format, and transmit vehicle telemetry data at a minimum aggregate rate of 2 Mbps using PCM/FM modulation per IRIG 106 Chapter 4. |
| **Rationale**    | Telemetry data rate supports real-time vehicle health monitoring and post-flight reconstruction for mission success and anomaly investigation. |
| **Source**       | IRIG 106; range telemetry requirements |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-TLM-01 |
| **Status**       | Draft |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The GN&C computer shall compute and downlink the predicted instantaneous impact point (IIP) at a rate of not less than 1 Hz throughout powered flight. |
| **Rationale**    | IIP is used by range safety and by the autonomous FT algorithm to determine whether the vehicle trajectory remains within the approved flight corridor. |
| **Source**       | EWR 127-1 Section 3.5; NASA-STD-8719.24 |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-GNC-01, CMP-TLM-01 |
| **Status**       | Draft |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The FTS shall terminate vehicle flight within 500 ms of receiving a valid destruct command from the range safety command system via IFC-EXT-001. |
| **Rationale**    | Response time budget ensures that a vehicle deviating from its approved corridor can be terminated before the IIP reaches a populated area. |
| **Source**       | EWR 127-1 Section 3.2; RCC 319 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FTS-01 |
| **Status**       | Draft |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The FTS shall operate independently of the GN&C computer, with no shared processors, software, power buses, or communication paths between FTS and GN&C. |
| **Rationale**    | FTS independence ensures that a GN&C failure that causes the trajectory violation cannot simultaneously prevent flight termination. |
| **Source**       | EWR 127-1 Section 3.1; range safety independence requirement |
| **Parent**       | — |
| **Verification** | Inspection, Analysis |
| **Allocation**   | CMP-FTS-01, CMP-GNC-01 |
| **Status**       | Draft |

### REQ-SAF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The FTS ordnance system shall demonstrate a reliability of not less than 0.999 at a 95% confidence level per EWR 127-1, verified through lot acceptance testing and bridgewire continuity monitoring. |
| **Rationale**    | Ordnance reliability ensures that an FTS activation command results in actual vehicle termination. |
| **Source**       | EWR 127-1 Section 3.6; RCC 319 |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-FTS-02 |
| **Status**       | Draft |

### REQ-SAF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The FTS shall implement an autonomous flight termination (AFT) function that initiates vehicle termination when the computed IIP exits the approved flight corridor boundaries and ground-commanded termination has not been received within 5 seconds of the violation. |
| **Rationale**    | Autonomous termination provides a backup to ground-commanded termination for cases where the ground command link is interrupted or latent. |
| **Source**       | NASA-STD-8719.24; EWR 127-1 Section 3.5 |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-FTS-01, CMP-GNC-01 |
| **Status**       | Draft |

### REQ-SAF-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The FTS software shall be developed to DO-178C Level A, satisfying all objectives of Tables A-1 through A-10 with independence per the Level A column. |
| **Rationale**    | FTS software failure is catastrophic (failure to terminate when commanded). DO-178C Level A provides the highest assurance level for airborne software. |
| **Source**       | EWR 127-1; DO-178C; range safety certification requirements |
| **Parent**       | — |
| **Verification** | Inspection, Analysis |
| **Allocation**   | CMP-FTS-01 |
| **Status**       | Draft |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The FTS command receiver shall receive and decode range safety destruct commands via IFC-EXT-001 on the assigned frequency with a command signal detection threshold of -110 dBm and a maximum false-command probability of 1 x 10^-9 per flight. |
| **Rationale**    | Receiver sensitivity ensures command reception throughout the flight envelope. False-command probability prevents inadvertent termination from noise or interference. |
| **Source**       | EWR 127-1 Section 3.3; RCC 319 |
| **Parent**       | REQ-SAF-001 |
| **Verification** | Test |
| **Allocation**   | CMP-FTS-01 |
| **Status**       | Draft |

### REQ-IFC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The GN&C computer shall transmit TVC commands to the engine controller via IFC-EXT-003 at a rate of 50 Hz with a maximum latency of 10 ms from command computation to serial bus transmission. |
| **Rationale**    | TVC command freshness is critical to engine gimbal control loop stability during powered flight. |
| **Source**       | Engine controller ICD; GN&C control loop analysis |
| **Parent**       | REQ-FUN-002 |
| **Verification** | Test |
| **Allocation**   | CMP-GNC-01 |
| **Status**       | Draft |

### REQ-IFC-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The avionics shall receive pre-launch configuration data and FTS arm commands from the ground launch control system via IFC-EXT-005 over a hardwired umbilical, with the umbilical disconnecting at T-0 without affecting FTS armed status. |
| **Rationale**    | Pre-launch ground interface supports final configuration and FTS arming. Post-disconnect FTS retention ensures termination capability is maintained through liftoff. |
| **Source**       | Ground operations ICD; EWR 127-1 |
| **Parent**       | — |
| **Verification** | Test, Demonstration |
| **Allocation**   | CMP-FTS-01, CMP-VMU-01 |
| **Status**       | Draft |
