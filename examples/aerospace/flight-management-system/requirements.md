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
| **Statement**    | The FMS shall allow the flight crew to create a lateral flight plan consisting of up to 250 waypoints with defined leg types per ARINC 424. |
| **Rationale**    | Operational capability for route definition across oceanic and continental airspace. |
| **Source**       | Stakeholder need (airline operations); 14 CFR 25.1329 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01A, CMP-FMC-01B |
| **Status**       | Baselined |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall allow modification of the active flight plan during flight without interrupting guidance output for more than one guidance computation cycle (50 ms). |
| **Rationale**    | In-flight plan changes are routine; guidance interruption during modification could cause transient flight path deviations. |
| **Source**       | Stakeholder need (flight crew); CTL-005 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01A, CMP-FMC-01B |
| **Status**       | Baselined |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall accept and process uplinked flight plan amendments received via the FANS datalink interface within 5 seconds of message receipt. |
| **Rationale**    | Supports oceanic and continental datalink operations per FANS-1/A. |
| **Source**       | Stakeholder need (ATC/airline operations); ARINC 702A |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01A, CMP-FMC-01B, CMP-DCU-01B |
| **Status**       | Baselined |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall validate each flight plan leg for performance feasibility before sequencing the leg as active, and shall annunciate to the flight crew if a leg exceeds aircraft performance capabilities. |
| **Rationale**    | Prevents guidance to an infeasible profile that could result in airspeed or altitude deviations. |
| **Source**       | 14 CFR 25.1329; operational integrity |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01A, CMP-FMC-01B |
| **Status**       | Baselined |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall compute aircraft position using multi-sensor fusion of IRS, GNSS, DME, and VOR inputs with a position update rate of not less than 50 Hz. |
| **Rationale**    | Position accuracy and update rate drive guidance quality and RNP containment. |
| **Source**       | 14 CFR 25.1329; AC 90-105A (RNP operations) |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-FMC-01E, CMP-FMC-01F, CMP-DCU-01A |
| **Status**       | Baselined |

### REQ-FUN-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall output the computed position solution to the cross-channel comparator within 20 ms of sensor data receipt. |
| **Rationale**    | Timely cross-channel comparison is necessary to detect position disagreements before they propagate to guidance. |
| **Source**       | CTL-002; ARP4754A Section 5.2 |
| **Parent**       | REQ-FUN-005 |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01E, CMP-FMC-01F, CMP-FMC-01C |
| **Status**       | Baselined |

### REQ-FUN-007
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall weight navigation sensor inputs based on estimated accuracy, integrity, and availability, and shall dynamically adjust weights when sensor quality degrades. |
| **Rationale**    | Sensor weighting drives position accuracy under varying operational conditions. |
| **Source**       | AC 90-105A; RTCA DO-229F (GNSS MOPS) |
| **Parent**       | REQ-FUN-005 |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-FMC-01E, CMP-FMC-01F |
| **Status**       | Baselined |

### REQ-FUN-008
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall detect and exclude faulty navigation sensor inputs within 10 seconds of fault onset with a detection probability of not less than 0.999 per flight hour. |
| **Rationale**    | Fault detection and exclusion prevents erroneous sensor data from corrupting the navigation solution. |
| **Source**       | CTL-003; HZ-003 |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-FMC-01E, CMP-FMC-01F |
| **Status**       | Baselined |

### REQ-FUN-009
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall annunciate to the flight crew when a navigation sensor is excluded, identifying the excluded sensor type, within 2 seconds of exclusion. |
| **Rationale**    | Crew awareness of sensor exclusion is necessary for operational decision-making. |
| **Source**       | CTL-003; 14 CFR 25.1322 (crew alerting) |
| **Parent**       | REQ-FUN-008 |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01E, CMP-FMC-01F, CMP-DMC-01C |
| **Status**       | Baselined |

### REQ-FUN-010
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall continuously compute and display the actual navigation performance (ANP) and shall alert the flight crew when ANP exceeds the required navigation performance (RNP) for the active procedure. |
| **Rationale**    | RNP containment monitoring is a regulatory requirement for RNAV/RNP operations. |
| **Source**       | AC 90-105A; 14 CFR 25.1329 |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-FMC-01E, CMP-FMC-01F, CMP-DMC-01C |
| **Status**       | Baselined |

### REQ-FUN-011
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall compute predicted fuel at destination and alternate within an accuracy of +/-3% of actual fuel burn under standard atmospheric conditions. |
| **Rationale**    | Fuel prediction accuracy drives dispatch and diversion decisions. |
| **Source**       | Stakeholder need (airline operations) |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-FMC-01H |
| **Status**       | Baselined |

### REQ-FUN-012
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall compute optimum cruise altitude and speed based on current weight, wind, and temperature data, and shall present the recommended profile to the flight crew. |
| **Rationale**    | Performance optimization reduces fuel consumption and supports operational efficiency. |
| **Source**       | Stakeholder need (airline operations) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01H |
| **Status**       | Baselined |

### REQ-FUN-013
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall generate a low-fuel advisory to the flight crew when predicted fuel at destination falls below the operator-defined minimum fuel threshold. |
| **Rationale**    | Low-fuel awareness enables timely diversion decisions. |
| **Source**       | Stakeholder need (flight crew); 14 CFR 25.1322 |
| **Parent**       | REQ-FUN-011 |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01H, CMP-DMC-01C |
| **Status**       | Baselined |

### REQ-FUN-014
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall compute lateral guidance roll commands to maintain the aircraft within the RNP containment region for the active leg, with a command update rate of not less than 20 Hz. |
| **Rationale**    | Roll command accuracy and rate drive lateral path tracking performance. |
| **Source**       | 14 CFR 25.1329; CTL-004 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01G |
| **Status**       | Baselined |

### REQ-FUN-015
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall limit computed lateral guidance bank angle commands to not exceed 25 degrees in normal operation and 15 degrees below 500 feet AGL. |
| **Rationale**    | Bank angle limits prevent excessive roll that could lead to loss of control at low altitude. |
| **Source**       | 14 CFR 25.1329; CTL-004 |
| **Parent**       | REQ-FUN-014 |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01G |
| **Status**       | Baselined |

### REQ-FUN-016
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall compute vertical guidance pitch and thrust commands to follow the computed vertical profile within +/-50 feet of the target altitude during VNAV descent. |
| **Rationale**    | Vertical path accuracy drives approach precision and terrain clearance margins. |
| **Source**       | 14 CFR 25.1329; CTL-007 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01G |
| **Status**       | Baselined |

### REQ-FUN-017
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall compute speed targets that respect aircraft operating limits (Vmo/Mmo, flap/slat limit speeds, minimum maneuver speed) and shall not command a speed outside these limits. |
| **Rationale**    | Speed limit protection prevents overspeed or low-speed conditions that could result in structural damage or loss of control. |
| **Source**       | 14 CFR 25.1329; CTL-007 |
| **Parent**       | REQ-FUN-016 |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01G |
| **Status**       | Baselined |

### REQ-FUN-018
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall manage transitions between guidance modes (LNAV, VNAV, heading select, altitude hold) and shall annunciate the active guidance mode to the flight crew within 1 second of mode change. |
| **Rationale**    | Crew awareness of active guidance mode is essential for flight path management. |
| **Source**       | 14 CFR 25.1329; 14 CFR 25.1322 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01G, CMP-DMC-01C |
| **Status**       | Baselined |

### REQ-FUN-019
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall provide navigation display data to the DMC at a minimum refresh rate of 10 Hz, including aircraft position, active leg, waypoint sequence, and map overlay data. |
| **Rationale**    | Display refresh rate drives crew situational awareness quality. |
| **Source**       | Stakeholder need (flight crew) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-DMC-01A, CMP-DMC-01C |
| **Status**       | Baselined |

### REQ-FUN-020
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall process crew data entries from the CDU within 200 ms of key press and shall provide visual feedback on the CDU page within 500 ms. |
| **Rationale**    | Responsive CDU interaction prevents crew confusion and data entry errors. |
| **Source**       | Stakeholder need (flight crew) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-DMC-01B, CMP-DMC-01C |
| **Status**       | Baselined |

### REQ-FUN-021
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall execute power-up BIT on all LRUs within 90 seconds of power application and shall report any detected faults to the flight crew and maintenance system before the system transitions to MODE-001. |
| **Rationale**    | Pre-flight fault detection prevents dispatch with known failures. |
| **Source**       | CTL-010; 14 CFR 25.1309 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01, CMP-DMC-01, CMP-DCU-01 |
| **Status**       | Baselined |

### REQ-FUN-022
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall verify the integrity of navigation database loads using CRC-32 and cryptographic signature verification before accepting the database as valid. |
| **Rationale**    | Corrupt or tampered navigation data could cause erroneous flight plan sequencing. |
| **Source**       | CTL-009; THR-001 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-DCU-01C, CMP-DCU-01E |
| **Status**       | Baselined |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall detect a cross-channel position disagreement exceeding 0.1 NM and shall transition to MODE-002 within 2 seconds of detection. |
| **Rationale**    | Cross-channel disagreement indicates a potential misleading navigation output on one channel. |
| **Source**       | HZ-001; CTL-001 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01C, CMP-FMC-01A, CMP-FMC-01B |
| **Status**       | Baselined |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall detect a cross-channel guidance command disagreement exceeding 2 degrees roll or 1 degree pitch and shall inhibit guidance output to the AFCS within 100 ms of detection. |
| **Rationale**    | Divergent guidance commands, if both applied, could cause uncommanded flight path changes. |
| **Source**       | HZ-002; CTL-002 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01C, CMP-FMC-01G |
| **Status**       | Baselined |

### REQ-SAF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The probability of undetected erroneous FMS guidance output that could cause misleading flight path deviation shall not exceed 1 x 10^-9 per flight hour. |
| **Rationale**    | Quantitative safety target derived from the PSSA for the Catastrophic failure condition of undetected misleading guidance. |
| **Source**       | HZ-001; CTL-001; CTL-002; 14 CFR 25.1309 |
| **Parent**       | — |
| **Verification** | Analysis |
| **Allocation**   | CMP-FMC-01 (system-level) |
| **Status**       | Baselined |

### REQ-SAF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall annunciate loss of all navigation capability to the flight crew within 3 seconds and shall transition to MODE-003 with guidance output inhibited. |
| **Rationale**    | Total navigation loss requires crew awareness and reversion to raw-data navigation. |
| **Source**       | HZ-004; CTL-004 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01A, CMP-FMC-01B, CMP-DMC-01C |
| **Status**       | Baselined |

### REQ-SAF-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The ARINC 653 RTOS shall enforce spatial partition isolation such that a fault in any application partition cannot modify code or data in another partition. |
| **Rationale**    | Partition integrity is the basis for hosting different-DAL functions on shared hardware. |
| **Source**       | HZ-005; CTL-005 |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-FMC-01D |
| **Status**       | Baselined |

### REQ-SAF-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The ARINC 653 RTOS shall enforce temporal partition isolation such that a partition that exceeds its time window allocation is terminated and reported to the health monitor without affecting the scheduling of other partitions. |
| **Rationale**    | Temporal isolation prevents a runaway partition from starving safety-critical functions. |
| **Source**       | HZ-005; CTL-005 |
| **Parent**       | REQ-SAF-005 |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01D |
| **Status**       | Baselined |

### REQ-SAF-007
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall detect loss of the DMC within 5 seconds and shall transition to MODE-004 with FMC-driven backup display capability within 10 seconds. |
| **Rationale**    | Loss of FMS display without backup deprives the crew of navigation situation awareness. |
| **Source**       | HZ-006; CTL-006 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01, CMP-DMC-01 |
| **Status**       | Baselined |

### REQ-SAF-008
| Field        | Value |
|--------------|-------|
| **Statement**    | The probability of loss of all FMS function (both channels failed simultaneously) shall not exceed 1 x 10^-7 per flight hour. |
| **Rationale**    | Quantitative safety target for the Hazardous failure condition of total FMS loss. |
| **Source**       | HZ-007; CTL-001; 14 CFR 25.1309 |
| **Parent**       | — |
| **Verification** | Analysis |
| **Allocation**   | CMP-FMC-01 (system-level) |
| **Status**       | Baselined |

### REQ-SAF-009
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall implement independent watchdog monitoring on each FMC channel such that a processor lockup is detected and the channel is declared failed within 500 ms. |
| **Rationale**    | Watchdog monitoring detects processor failures that the application software cannot self-detect. |
| **Source**       | HZ-008; CTL-008 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01A, CMP-FMC-01B |
| **Status**       | Baselined |

### REQ-SAF-010
| Field        | Value |
|--------------|-------|
| **Statement**    | The cross-channel comparator shall be implemented in dedicated hardware independent of both FMC software channels, with no shared processing resources. |
| **Rationale**    | Comparator independence ensures that a common-mode software fault cannot defeat both the computation and the comparison. |
| **Source**       | HZ-001; CTL-002; ARP4761A CMA |
| **Parent**       | — |
| **Verification** | Inspection, Analysis |
| **Allocation**   | CMP-FMC-01C |
| **Status**       | Baselined |

## Security Requirements

### REQ-SEC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall authenticate all navigation database loads using a cryptographic signature verification mechanism before accepting the database into the active navigation data store. |
| **Rationale**    | Prevents installation of tampered navigation data that could corrupt flight plan sequencing. |
| **Source**       | THR-001; CTL-009 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-DCU-01C, CMP-DCU-01E |
| **Status**       | Baselined |

### REQ-SEC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The DCU maintenance port shall require role-based authentication before granting access to data load or configuration functions. |
| **Rationale**    | Prevents unauthorized access to the maintenance interface that could enable malicious data loading or configuration changes. |
| **Source**       | THR-002 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-DCU-01C |
| **Status**       | Baselined |

### REQ-SEC-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The DCU shall validate all ACARS/FANS datalink messages against the expected message format and shall reject messages that fail format validation, logging the rejection event. |
| **Rationale**    | Prevents malformed or malicious datalink messages from reaching the FMC. |
| **Source**       | THR-003; THR-004 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-DCU-01B, CMP-DCU-01E |
| **Status**       | Baselined |

### REQ-SEC-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall enforce one-way data flow from the FMC to the DMC for display data, preventing any DMC-originated command from modifying FMC navigation or guidance state. |
| **Rationale**    | Prevents a compromised DMC from injecting commands into the safety-critical FMC. |
| **Source**       | THR-005 |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-FMC-01, CMP-DMC-01 |
| **Status**       | Baselined |

### REQ-SEC-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall apply message authentication codes (MAC) to all safety-critical AFDX messages transmitted between LRUs, and shall reject messages with invalid MACs. |
| **Rationale**    | Protects inter-LRU communication integrity against message injection or modification. |
| **Source**       | THR-006 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01, CMP-DMC-01, CMP-DCU-01 |
| **Status**       | Baselined |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall transmit lateral and vertical guidance commands to the AFCS via IFC-EXT-001 at a rate of 20 Hz with a maximum latency of 50 ms from computation to ARINC 429 bus transmission. |
| **Rationale**    | Guidance command freshness is critical to AFCS control loop stability. |
| **Source**       | AFCS ICD; 14 CFR 25.1329 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01G, CMP-FMC-01J |
| **Status**       | Baselined |

### REQ-IFC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The DCU shall receive IRS data via IFC-EXT-004 at the IRS output rate (50 Hz) and shall forward validated IRS data to the FMC via IFC-INT-001 within 5 ms of receipt. |
| **Rationale**    | IRS latency directly impacts navigation solution timeliness. |
| **Source**       | IRS ICD; ARP4754A Section 5.2 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-DCU-01A, CMP-DCU-01E |
| **Status**       | Baselined |

### REQ-IFC-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMC shall transmit navigation and performance display data to the DMC via IFC-INT-002 at a rate of not less than 20 Hz using AFDX virtual links with a guaranteed bandwidth of 2 Mbps. |
| **Rationale**    | Display data bandwidth and rate support the 10 Hz display refresh requirement. |
| **Source**       | DMC ICD |
| **Parent**       | REQ-FUN-019 |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01, CMP-DMC-01 |
| **Status**       | Baselined |

### REQ-IFC-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The DCU shall receive ACARS/FANS messages via IFC-EXT-008 and shall forward validated messages to the FMC via IFC-INT-001 within 500 ms of receipt. |
| **Rationale**    | Datalink message delivery timeliness supports ATC communication requirements. |
| **Source**       | ACARS ICD; FANS-1/A |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-DCU-01B, CMP-DCU-01E |
| **Status**       | Baselined |

### REQ-IFC-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMC cross-channel comparator shall receive computed outputs from both channels via IFC-INT-003 and IFC-INT-004 within the same 20 ms computation frame and shall output the comparison result via IFC-INT-005 before the next frame begins. |
| **Rationale**    | Synchronous comparison is necessary to detect divergent outputs within a single computation cycle. |
| **Source**       | CTL-002; ARP4754A Section 5.2 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01C |
| **Status**       | Baselined |

### REQ-IFC-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The DCU shall transmit FMS position and intent data to TAWS via IFC-EXT-010 at 1 Hz per ARINC 429 label assignments defined in the TAWS ICD. |
| **Rationale**    | TAWS requires FMS position and intent for predictive terrain alerting. |
| **Source**       | TAWS ICD |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01, CMP-DCU-01A |
| **Status**       | Baselined |

### REQ-IFC-007
| Field        | Value |
|--------------|-------|
| **Statement**    | The maintenance port (IFC-EXT-012) shall support Ethernet-based data loading at a minimum throughput of 10 Mbps and shall complete a full navigation database load within 15 minutes. |
| **Rationale**    | Maintenance efficiency requires acceptable data load times for line operations. |
| **Source**       | Stakeholder need (maintenance organization) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-DCU-01C |
| **Status**       | Baselined |

## Performance Requirements

### REQ-PRF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS navigation solution shall achieve a horizontal position accuracy of 0.05 NM (95%) or better when GNSS and IRS are both available. |
| **Rationale**    | Position accuracy drives RNP 0.1 and RNP 0.3 approach capability. |
| **Source**       | AC 90-105A; operational performance requirement |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-FMC-01E, CMP-FMC-01F |
| **Status**       | Baselined |

### REQ-PRF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall maintain navigation solution continuity such that the probability of unscheduled loss of navigation output does not exceed 1 x 10^-5 per flight hour in MODE-001 (Normal). |
| **Rationale**    | Navigation continuity supports RNP containment and operational approval. |
| **Source**       | AC 90-105A; DO-229F |
| **Parent**       | — |
| **Verification** | Analysis |
| **Allocation**   | CMP-FMC-01E, CMP-FMC-01F |
| **Status**       | Baselined |

### REQ-PRF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall complete power-up initialization, including BIT, database verification, and system self-test, within 90 seconds of power application at ambient temperatures between -40C and +70C. |
| **Rationale**    | Rapid power-up supports operational turnaround and dispatch requirements. |
| **Source**       | Stakeholder need (airline operations) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01, CMP-DMC-01, CMP-DCU-01 |
| **Status**       | Baselined |

### REQ-PRF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS guidance computation loop shall execute with a worst-case execution time (WCET) of not more than 15 ms on a 20 ms cycle, providing a minimum 25% timing margin under all partition scheduling scenarios. |
| **Rationale**    | WCET margin ensures guidance computation completes within its ARINC 653 time window under worst-case multi-core interference conditions per CAST-32A. |
| **Source**       | CAST-32A; ARP4754A Section 5.2 |
| **Parent**       | — |
| **Verification** | Analysis, Test |
| **Allocation**   | CMP-FMC-01G, CMP-FMC-01D |
| **Status**       | Baselined |

### REQ-PRF-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The FMS shall operate within a total power consumption of 150 watts across all three LRUs under maximum computational load conditions. |
| **Rationale**    | Power budget constraint for aircraft electrical load analysis. |
| **Source**       | Aircraft electrical load analysis; 14 CFR 25.1351 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FMC-01, CMP-DMC-01, CMP-DCU-01 |
| **Status**       | Baselined |
