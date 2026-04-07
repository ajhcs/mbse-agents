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
| **Statement**    | The constellation shall provide multispectral Earth observation imagery with a ground sample distance of 5 m or better at nadir from the operational orbit altitude. |
| **Rationale**    | Minimum spatial resolution to satisfy the mission's Earth observation objectives. |
| **Source**       | Stakeholder need (end-user community); mission requirements document |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-PAY-01 |
| **Status**       | Draft |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The constellation shall achieve 24-hour global revisit at latitudes between 60 degrees N and 60 degrees S with at least 10 of 12 spacecraft operational. |
| **Rationale**    | Revisit cadence drives the operational utility of the constellation for change detection applications. |
| **Source**       | Stakeholder need (end-user community); constellation design trade study |
| **Parent**       | — |
| **Verification** | Analysis |
| **Allocation**   | CMP-CON-01 |
| **Status**       | Draft |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | Each spacecraft shall establish and maintain intersatellite links with at least 2 neighboring spacecraft whenever line-of-sight geometry permits. |
| **Rationale**    | ISL mesh connectivity enables data relay to ground without requiring each spacecraft to have a direct ground contact. |
| **Source**       | Constellation architecture trade study; CCSDS 211.0-B |
| **Parent**       | — |
| **Verification** | Test, Demonstration |
| **Allocation**   | CMP-SDR-01 |
| **Status**       | Draft |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | Each spacecraft shall transmit telemetry and receive telecommands using CCSDS Space Packet Protocol (CCSDS 133.0-B) over a TM/TC Space Data Link layer. |
| **Rationale**    | CCSDS protocol compliance ensures interoperability with the multi-provider ground station network. |
| **Source**       | CCSDS 133.0-B; CCSDS 132.0-B; CCSDS 231.0-B |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-SDR-01, CMP-OBC-01 |
| **Status**       | Draft |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | Each spacecraft shall perform autonomous orbit maintenance maneuvers to maintain the constellation phasing within +/-0.5 degrees of the nominal mean anomaly separation. |
| **Rationale**    | Constellation geometry maintenance ensures the revisit guarantee is met without requiring continuous ground commanding. |
| **Source**       | REQ-FUN-002; mission operations concept |
| **Parent**       | REQ-FUN-002 |
| **Verification** | Analysis, Demonstration |
| **Allocation**   | CMP-OBC-01, CMP-PROP-01 |
| **Status**       | Draft |

### REQ-FUN-006
| Field        | Value |
|--------------|-------|
| **Statement**    | Each spacecraft on-board computer shall implement error detection and correction (EDAC) on all critical memory, correcting single-bit errors and detecting double-bit errors. |
| **Rationale**    | Radiation-induced single-event upsets in LEO require memory protection to prevent silent data corruption on COTS processors. |
| **Source**       | NASA-STD-8739.8; radiation environment analysis |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-OBC-01 |
| **Status**       | Draft |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | Each spacecraft shall comply with NASA-STD-8719.14 requirements for orbital debris mitigation, including a 25-year post-mission deorbit timeline. |
| **Rationale**    | Orbital debris mitigation is a mandatory compliance requirement for all NASA-affiliated LEO missions. |
| **Source**       | NASA-STD-8719.14; U.S. Government Orbital Debris Mitigation Standard Practices |
| **Parent**       | — |
| **Verification** | Analysis |
| **Allocation**   | CMP-PROP-01, CMP-OBC-01 |
| **Status**       | Draft |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | Each spacecraft shall execute an autonomous collision avoidance maneuver within 4 hours of receiving a conjunction data message (CDM) indicating a probability of collision exceeding 1 x 10^-4, if ground confirmation is not received within 2 hours. |
| **Rationale**    | Limited ground contact windows require on-board collision avoidance capability to protect the constellation and the debris environment. |
| **Source**       | NASA Conjunction Assessment guidelines; stakeholder need (mission operations) |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-OBC-01, CMP-PROP-01 |
| **Status**       | Draft |

### REQ-SAF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | Each spacecraft shall transition to MODE-002 (Safe-Hold) within 60 seconds of detecting a fault condition that could result in uncontrolled attitude or unintended propulsive maneuver. |
| **Rationale**    | Safe-hold prevents a faulted spacecraft from becoming a collision hazard or depleting resources uncontrollably. |
| **Source**       | Mission safety requirements; CLASS C mission assurance |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-OBC-01, CMP-ADCS-01 |
| **Status**       | Draft |

### REQ-SAF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The constellation management software shall detect loss of contact with any spacecraft within 3 consecutive missed contact windows and shall initiate MODE-003 (Constellation-Reconfig) mesh re-routing within 1 orbit period. |
| **Rationale**    | Timely detection of spacecraft loss enables the constellation to reconfigure data routing and imaging schedules to minimize coverage degradation. |
| **Source**       | Mission operations concept; REQ-FUN-002 |
| **Parent**       | REQ-FUN-002 |
| **Verification** | Demonstration |
| **Allocation**   | CMP-CON-01, CMP-SDR-01 |
| **Status**       | Draft |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | Each spacecraft shall support CCSDS Space Link Extension (SLE) transfer services for ground station interoperability, including RAF and RCF service types. |
| **Rationale**    | SLE interoperability enables the use of multiple third-party ground station providers without custom protocol adaptation. |
| **Source**       | CCSDS 913.1-B (SLE); stakeholder need (mission operations) |
| **Parent**       | REQ-FUN-004 |
| **Verification** | Test |
| **Allocation**   | CMP-SDR-01, CMP-OBC-01 |
| **Status**       | Draft |

### REQ-IFC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The intersatellite link shall operate at a minimum data rate of 1 Mbps per link with a bit error rate not exceeding 1 x 10^-6 at the maximum inter-spacecraft range within the constellation geometry. |
| **Rationale**    | ISL data rate must support imagery relay from spacecraft without direct ground contact within the orbital period. |
| **Source**       | CCSDS 211.0-B; constellation data budget analysis |
| **Parent**       | REQ-FUN-003 |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-SDR-01 |
| **Status**       | Draft |
