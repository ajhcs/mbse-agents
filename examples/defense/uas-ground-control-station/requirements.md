# Requirements

All requirements are atomic, testable shall-statements.

## Requirement Record Schema

| Field         | Description                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------|
| ID            | Unique identifier (e.g., REQ-FUN-001)                                                            |
| Statement     | Atomic shall-statement                                                                            |
| Rationale     | Why this requirement exists                                                                       |
| Source        | Hazard ID (HZ-), control ID (CTL-), regulatory clause, or stakeholder need                       |
| Parent        | Parent requirement ID (if derived)                                                                |
| Verification  | Method: test, analysis, inspection, demonstration                                                 |
| Allocation    | Target component ID(s) from architecture.md                                                       |
| Status        | Draft, baselined, verified, deferred                                                              |

## Functional Requirements

### REQ-FUN-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall allow the operator to create a mission plan consisting of up to 500 waypoints with defined leg types, loiter patterns, and altitude constraints per STANAG 4586. |
| **Rationale**    | Operational capability for multi-vehicle route definition across extended mission areas. |
| **Source**       | Stakeholder need (unit commander); STANAG 4586 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01B |
| **Status**       | Baselined |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall validate each mission plan leg for airspace deconfliction, terrain clearance, and fuel feasibility before transmitting the plan to the air vehicle. |
| **Rationale**    | Prevents transmission of infeasible plans that could result in airspace violations or fuel exhaustion. |
| **Source**       | Stakeholder need (unit commander); CTL-008 |
| **Parent**       | REQ-FUN-001 |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01B |
| **Status**       | Baselined |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall display air vehicle state (position, altitude, heading, airspeed, engine status, fuel state) on the operator display with a refresh rate of not less than 10 Hz. |
| **Rationale**    | Real-time AV state awareness is required for safe flight management. |
| **Source**       | Stakeholder need (UAS operator crew) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01A, CMP-MMC-01D |
| **Status**       | Baselined |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall transmit flight commands (waypoint changes, heading, altitude, airspeed) to the air vehicle with an end-to-end latency of not more than 250 ms from operator input to C2 link transmission. |
| **Rationale**    | Command latency directly impacts AV flight path response and operator control authority. |
| **Source**       | Stakeholder need (UAS operator crew); MIL-STD-882E risk analysis |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01A |
| **Status**       | Baselined |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall support simultaneous control of up to four Group 4/5 air vehicles with independent mission plans, C2 links, and sensor tasking. |
| **Rationale**    | Multi-vehicle control is the primary operational capability driving the GCS architecture. |
| **Source**       | Stakeholder need (unit commander); ORD |
| **Parent**       | — |
| **Verification** | Test, Demonstration |
| **Allocation**   | CMP-MMC-01A, CMP-CLT-01D |
| **Status**       | Baselined |

### REQ-FUN-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall detect loss of all C2 links to an air vehicle within 10 seconds of the last valid telemetry receipt and shall declare lost link status. |
| **Rationale**    | Timely lost link detection is the initiating event for the safety-critical lost link procedure. |
| **Source**       | HZ-001; CTL-001; MIL-STD-882E |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01F |
| **Status**       | Baselined |

### REQ-FUN-007
| Field        | Value |
|--------------|-------|
| **Statement**    | Upon lost link declaration, the GCS shall initiate the pre-programmed lost link procedure for the affected air vehicle and shall transmit ATC notification within 60 seconds. |
| **Rationale**    | ATC notification is required to deconflict airspace when an unmanned vehicle is flying autonomously without C2. |
| **Source**       | HZ-001; CTL-001; CTL-002; FAA UAS operating procedures |
| **Parent**       | REQ-FUN-006 |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01F, CMP-MMC-01C |
| **Status**       | Baselined |

### REQ-FUN-008
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall provide flight termination command capability requiring two-operator authentication and a confirmation sequence before transmission. |
| **Rationale**    | Flight termination is irreversible; two-operator auth prevents accidental or unauthorized termination. |
| **Source**       | HZ-005; CTL-005; MIL-STD-882E |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01A |
| **Status**       | Baselined |

### REQ-FUN-009
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall generate ADS-B Out position reports for each controlled air vehicle at a rate of 1 Hz with position accuracy derived from AV telemetry. |
| **Rationale**    | ADS-B Out is required for UAS operations in national airspace per FAA UAS policy. |
| **Source**       | Stakeholder need (FAA/ATC); 14 CFR Part 91 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01C |
| **Status**       | Baselined |

### REQ-FUN-010
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall process ACAS Xu resolution advisories and shall present deconfliction guidance to the operator within 2 seconds of advisory receipt. |
| **Rationale**    | ACAS Xu advisories must be presented with minimum latency to allow operator response within the collision avoidance time window. |
| **Source**       | HZ-003; CTL-003; RTCA DO-386 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01C |
| **Status**       | Baselined |

### REQ-FUN-011
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall manage LOS and BLOS C2 data link sessions with automatic failover from the active link to the backup link within 5 seconds of active link loss detection. |
| **Rationale**    | Rapid link failover minimizes the C2 link interruption during single-path failure. |
| **Source**       | HZ-002; CTL-004 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CLT-01D, CMP-CLT-01A, CMP-CLT-01B |
| **Status**       | Baselined |

### REQ-FUN-012
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall monitor C2 link health for each active link path (LOS and BLOS) and shall report link quality metrics (BER, signal strength, latency) to the operator at 1 Hz. |
| **Rationale**    | Link health monitoring supports proactive operator management before link loss occurs. |
| **Source**       | Stakeholder need (UAS operator crew) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CLT-01D |
| **Status**       | Baselined |

### REQ-FUN-013
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall dynamically allocate C2 link bandwidth between telemetry, sensor video, and command channels such that flight-safety-critical commands are guaranteed a minimum reserved bandwidth regardless of sensor data load. |
| **Rationale**    | Bandwidth starvation of flight commands by sensor video is a safety-relevant failure mode. |
| **Source**       | HZ-004; CTL-006 |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-CLT-01D |
| **Status**       | Baselined |

### REQ-FUN-014
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall manage COMSEC key lifecycle including key fill, OTAR, key update, and zeroization for all C2 link cryptographic contexts. |
| **Rationale**    | COMSEC key management is essential for maintaining encrypted C2 link integrity. |
| **Source**       | Stakeholder need (maintenance organization); NSA COMSEC policy |
| **Parent**       | — |
| **Verification** | Test, Demonstration |
| **Allocation**   | CMP-CLT-01C |
| **Status**       | Baselined |

### REQ-FUN-015
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall route C2 data streams for up to four air vehicles simultaneously, ensuring that commands destined for one air vehicle are not transmitted to another. |
| **Rationale**    | Mis-routing a command to the wrong AV could cause unintended flight maneuvers. |
| **Source**       | HZ-006; CTL-007 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CLT-01D |
| **Status**       | Baselined |

### REQ-FUN-016
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall command sensor payload pointing (azimuth, elevation) and mode selection (EO, IR, SAR) with a command update rate of not less than 5 Hz. |
| **Rationale**    | Sensor pointing responsiveness drives operator effectiveness for target tracking. |
| **Source**       | Stakeholder need (sensor operator) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-SCW-01B |
| **Status**       | Baselined |

### REQ-FUN-017
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall support geofence enforcement by transmitting geofence boundary data to the air vehicle and by annunciating geofence proximity warnings to the operator at 500 m and 100 m from the boundary. |
| **Rationale**    | Geofence enforcement prevents unauthorized airspace penetration and supports lost link containment. |
| **Source**       | HZ-007; CTL-008; FAA UAS operating procedures |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01A, CMP-MMC-01B |
| **Status**       | Baselined |

### REQ-FUN-018
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall receive, decode, and display sensor video at up to 1080p resolution with an end-to-end display latency of not more than 500 ms from AV sensor to operator display. |
| **Rationale**    | Video latency affects operator situational awareness and target tracking effectiveness. |
| **Source**       | Stakeholder need (sensor operator) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-SCW-01A |
| **Status**       | Baselined |

### REQ-FUN-019
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall compute target coordinates from sensor pointing data and air vehicle position with a circular error probable (CEP) of not more than 10 meters. |
| **Rationale**    | Target mensuration accuracy drives downstream PED and engagement decision quality. |
| **Source**       | Stakeholder need (intelligence community); operational performance requirement |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-SCW-01C |
| **Status**       | Baselined |

### REQ-FUN-020
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall execute power-up BIT on all subsystems within 120 seconds of power application and shall report detected faults to the operator before the system transitions to MODE-001. |
| **Rationale**    | Pre-mission fault detection prevents operations with known subsystem failures. |
| **Source**       | CTL-009; MIL-STD-882E |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01, CMP-CLT-01, CMP-SCW-01 |
| **Status**       | Baselined |

### REQ-FUN-021
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall verify the integrity of all software loads using cryptographic hash verification before accepting the software as valid for operational use. |
| **Rationale**    | Corrupted or tampered software could compromise flight-critical functions. |
| **Source**       | CTL-010; DI-SESS-81785A |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01, CMP-CLT-01 |
| **Status**       | Baselined |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall detect loss of all C2 links to a controlled air vehicle within 10 seconds and shall initiate the lost link procedure without operator intervention. |
| **Rationale**    | Automatic lost link initiation ensures timely AV recovery even if the operator is task-saturated. |
| **Source**       | HZ-001; CTL-001 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01F |
| **Status**       | Baselined |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall annunciate C2 link degradation (single-path loss) to the operator within 3 seconds with an audio and visual alert, and shall automatically transition to MODE-002. |
| **Rationale**    | Operator awareness of degraded C2 enables proactive mission adjustment before total link loss. |
| **Source**       | HZ-002; CTL-002; CTL-004 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01F, CMP-CLT-01D |
| **Status**       | Baselined |

### REQ-SAF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The flight termination command path shall be independent of the normal mission command path, using a dedicated message type and authentication mechanism, such that a software fault in mission command processing cannot prevent flight termination. |
| **Rationale**    | Flight termination is the last-resort safety function; it must remain available even during mission software failures. |
| **Source**       | HZ-005; CTL-005 |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-MMC-01A, CMP-CLT-01D |
| **Status**       | Baselined |

### REQ-SAF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The probability of undetected C2 link loss (GCS believes link is active when it is not) shall not exceed 1 x 10^-6 per flight hour. |
| **Rationale**    | Undetected link loss prevents timely initiation of lost link procedures; AV may deviate without recovery. |
| **Source**       | HZ-001; CTL-001; MIL-STD-882E |
| **Parent**       | — |
| **Verification** | Analysis |
| **Allocation**   | CMP-MMC-01F, CMP-CLT-01D |
| **Status**       | Baselined |

### REQ-SAF-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall enforce geofence containment such that a geofence violation command (operator commanding AV outside approved boundaries) is rejected with an operator alert. |
| **Rationale**    | Geofence enforcement prevents unauthorized airspace penetration and potential mid-air collision. |
| **Source**       | HZ-007; CTL-008 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01A, CMP-MMC-01B |
| **Status**       | Baselined |

### REQ-SAF-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall implement continuous C2 link heartbeat monitoring with a configurable timeout (default 10 seconds) and shall declare link loss when heartbeat responses are not received within the timeout period. |
| **Rationale**    | Heartbeat monitoring provides a definitive link loss detection mechanism independent of telemetry data content. |
| **Source**       | HZ-001; CTL-001 |
| **Parent**       | REQ-SAF-001 |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01F, CMP-CLT-01D |
| **Status**       | Baselined |

### REQ-SAF-007
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall prevent transmission of flight commands to the wrong air vehicle by validating vehicle ID in every outbound command message against the registered vehicle routing table. |
| **Rationale**    | Mis-routed commands could cause an unintended AV to execute a maneuver meant for a different vehicle. |
| **Source**       | HZ-006; CTL-007 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CLT-01D |
| **Status**       | Baselined |

### REQ-SAF-008
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall log all flight-critical commands, operator inputs, and C2 link status changes to a non-volatile mission recorder with sufficient fidelity to reconstruct the command timeline during post-mission analysis. |
| **Rationale**    | Mission recording supports mishap investigation and safety assessment validation. |
| **Source**       | CTL-009; DI-SESS-81785A |
| **Parent**       | — |
| **Verification** | Test, Inspection |
| **Allocation**   | CMP-MMC-01A |
| **Status**       | Baselined |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall transmit flight commands to the air vehicle via IFC-EXT-001 at a rate of 10 Hz with a maximum C2 link uplink latency of 200 ms per STANAG 4586 Level 3 interoperability. |
| **Rationale**    | Command rate and latency drive AV responsiveness to operator inputs. |
| **Source**       | STANAG 4586; AV ICD |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CLT-01D, CMP-CLT-01A, CMP-CLT-01B |
| **Status**       | Baselined |

### REQ-IFC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall receive AV telemetry via IFC-EXT-002 at the AV output rate (10 Hz) and shall forward validated telemetry to the MMC via IFC-INT-002 within 20 ms of receipt. |
| **Rationale**    | Telemetry timeliness drives operator situational awareness and lost link detection accuracy. |
| **Source**       | AV ICD; STANAG 4586 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CLT-01D, CMP-CLT-01A, CMP-CLT-01B |
| **Status**       | Baselined |

### REQ-IFC-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall receive sensor video via IFC-EXT-004 and shall forward the video stream to the SCW via IFC-INT-003 with a forwarding latency of not more than 50 ms. |
| **Rationale**    | Video forwarding latency directly contributes to the end-to-end sensor display latency budget. |
| **Source**       | MISB ST 0601; sensor payload ICD |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CLT-01D, CMP-SCW-01A |
| **Status**       | Baselined |

### REQ-IFC-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall transmit ADS-B Out position reports via IFC-EXT-007 at 1 Hz per DO-260C format with aircraft identification, position, altitude, and velocity fields populated from AV telemetry. |
| **Rationale**    | ADS-B format compliance is required for airspace integration. |
| **Source**       | 14 CFR Part 91; RTCA DO-260C |
| **Parent**       | REQ-FUN-009 |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01C |
| **Status**       | Baselined |

### REQ-IFC-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS internal Ethernet backbone (IFC-INT-001 through IFC-INT-007) shall provide a guaranteed minimum bandwidth of 100 Mbps between subsystems with QoS prioritization for flight-critical traffic classes. |
| **Rationale**    | Internal bandwidth and QoS ensure flight-critical data is not delayed by sensor video bulk transfers. |
| **Source**       | System architecture decision AD-03 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01, CMP-CLT-01, CMP-SCW-01 |
| **Status**       | Baselined |

### REQ-IFC-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall interface with the SATCOM ground terminal via IFC-EXT-005 using IP/UDP transport with DSCP marking for traffic class differentiation between command, telemetry, and sensor streams. |
| **Rationale**    | DSCP marking enables the SATCOM terminal to prioritize flight-critical traffic over sensor data. |
| **Source**       | SATCOM terminal ICD |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CLT-01B |
| **Status**       | Baselined |

### REQ-IFC-007
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall interface with the LOS antenna system via IFC-EXT-006 using MIL-STD-1553B for C2 data and RS-422 for antenna pointing commands. |
| **Rationale**    | Legacy LOS equipment uses MIL-STD-1553B; RS-422 provides the antenna servo interface. |
| **Source**       | LOS antenna ICD |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CLT-01A, CMP-CLT-01E, CMP-CLT-01F |
| **Status**       | Baselined |

## Performance Requirements

### REQ-PRF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall complete power-up initialization, including BIT and COMSEC key verification, within 120 seconds of power application at operating temperatures between -32C and +49C. |
| **Rationale**    | Rapid power-up supports tactical deployment and operational readiness timelines. |
| **Source**       | Stakeholder need (unit commander); MIL-STD-810H |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01, CMP-CLT-01, CMP-SCW-01 |
| **Status**       | Baselined |

### REQ-PRF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall sustain continuous mission operations for a minimum of 24 hours without operator-initiated restart or system degradation. |
| **Rationale**    | Extended mission duration supports persistent surveillance operations. |
| **Source**       | Stakeholder need (unit commander); ORD |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01, CMP-CLT-01, CMP-SCW-01 |
| **Status**       | Baselined |

### REQ-PRF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS mission management processor shall execute the flight command computation loop with a worst-case execution time (WCET) of not more than 40 ms on a 50 ms cycle, providing a minimum 20% timing margin. |
| **Rationale**    | WCET margin ensures flight command computation completes within the required update cycle. |
| **Source**       | System architecture; REQ-FUN-004 |
| **Parent**       | REQ-FUN-004 |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-MMC-01A |
| **Status**       | Baselined |

### REQ-PRF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS shall operate within a total power consumption of 3000 watts across all three subsystems under maximum computational and C2 link load. |
| **Rationale**    | Power budget constraint for deployable shelter and vehicle-mounted configurations. |
| **Source**       | Stakeholder need (maintenance organization); shelter power capacity |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MMC-01, CMP-CLT-01, CMP-SCW-01 |
| **Status**       | Baselined |

### REQ-PRF-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The GCS target mensuration engine shall compute target coordinates within 2 seconds of operator designation at the required 10 m CEP accuracy. |
| **Rationale**    | Mensuration response time supports time-sensitive targeting workflows. |
| **Source**       | Stakeholder need (intelligence community) |
| **Parent**       | REQ-FUN-019 |
| **Verification** | Test |
| **Allocation**   | CMP-SCW-01C |
| **Status**       | Baselined |
