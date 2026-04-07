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
| **Statement**    | The VCU shall transmit Cooperative Awareness Messages (CAM) containing ego vehicle position, speed, heading, and dimensions at a rate between 1 Hz and 10 Hz, dynamically adjusted based on vehicle dynamics changes per ETSI EN 302 637-2. |
| **Rationale**    | CAM broadcast enables other V2X participants to be aware of the ego vehicle's presence and trajectory for collision avoidance and cooperative maneuvers. |
| **Source**       | ETSI EN 302 637-2 clause 6.1.3; SAE J3161 |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-APP-01, CMP-APP-01B, CMP-PC5-01 |
| **Status**       | Baselined |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The VCU shall receive and decode CAM, DENM, and CPM messages from other V2X participants via PC5 and Uu interfaces, supporting a combined message throughput of not less than 1,000 messages per second. |
| **Rationale**    | In dense traffic scenarios (intersections, highway merging) the VCU must process messages from up to 100+ surrounding vehicles and RSUs simultaneously. |
| **Source**       | ETSI EN 302 637-2; ETSI EN 302 637-3; ETSI TS 103 324 |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-APP-01, CMP-APP-01A, CMP-PC5-01, CMP-UU-01 |
| **Status**       | Baselined |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The VCU shall determine ego vehicle position using GNSS with dead-reckoning augmentation, achieving a horizontal position accuracy of 1.5 m (CEP 95%) under open-sky conditions and 5 m under urban canyon conditions. |
| **Rationale**    | Position accuracy directly impacts the usefulness of transmitted CAM messages for cooperative perception by receiving vehicles. |
| **Source**       | ETSI TS 102 894-2 (position accuracy); SAE J2945/1 |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-GNSS-01 |
| **Status**       | Baselined |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The VCU shall format received V2X object data (remote vehicle positions, velocities, hazard notifications) into a standardized cooperative perception output and deliver it to the ADAS fusion ECU via IFC-EXT-001 at a rate of 10 Hz. |
| **Rationale**    | The ADAS fusion ECU requires a consistent, time-stamped data format to integrate V2X data with onboard sensor data for extended perception. |
| **Source**       | Stakeholder need (ADAS integration); ETSI TS 103 324 (CPM) |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-APP-01, CMP-APP-01C |
| **Status**       | Baselined |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The VCU shall manage pseudonym certificate rotation, switching the active signing certificate at intervals between 5 and 10 minutes during normal operation, without interrupting message transmission for more than 100 ms during certificate change. |
| **Rationale**    | Pseudonym rotation protects driver privacy by preventing long-term vehicle tracking through V2X messages, while minimizing service interruption. |
| **Source**       | IEEE 1609.2 clause 6.3; ETSI TS 103 097 |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-HSM-01, CMP-APP-01D |
| **Status**       | Baselined |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The VCU shall perform plausibility checking on all received V2X messages by cross-referencing reported remote vehicle positions and velocities against ego sensor data (radar, camera via ADAS feedback) and shall assign a plausibility confidence score (0-100%) to each V2X object. |
| **Rationale**    | SOTIF analysis (ISO 21448) identifies that false or spoofed V2X data could cause the ADAS system to make hazardous decisions. Plausibility checking provides defense-in-depth against incorrect cooperative perception data. |
| **Source**       | ISO 21448 clause 6 (SOTIF triggering conditions); ISO 26262 HARA (ASIL B) |
| **Parent**       | -- |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-APP-01C |
| **Status**       | Baselined |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The VCU shall tag all V2X data delivered to the ADAS fusion ECU with a trust level indicator (authenticated/plausibility-checked/unverified), and shall transition to MODE-003 (Degraded Trust) when the HSM reports certificate validation failure, ensuring no unauthenticated data is tagged as authenticated. |
| **Rationale**    | The ADAS fusion ECU must be able to weight V2X data appropriately based on its authentication and plausibility status, degrading V2X influence on safety decisions when trust is compromised. |
| **Source**       | ISO 21448 clause 6; ISO 21434 (cybersecurity) |
| **Parent**       | REQ-SAF-001 |
| **Verification** | Test |
| **Allocation**   | CMP-APP-01C, CMP-HSM-01 |
| **Status**       | Baselined |

### REQ-SAF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The safety-relevant data path from V2X message decode to ADAS fusion output shall be protected with E2E protection (CRC + sequence counter) meeting ASIL B diagnostic coverage requirements per ISO 26262-5. |
| **Rationale**    | The QM protocol stack and ASIL B message processing share a data path. E2E protection on the safety-relevant segment ensures data integrity across the QM/ASIL boundary. |
| **Source**       | ISO 26262-5 (ASIL B communication); architecture QM/ASIL split |
| **Parent**       | -- |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-APP-01A, CMP-APP-01C |
| **Status**       | Baselined |

## Security Requirements

### REQ-SEC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The VCU shall verify the ECDSA P-256 digital signature on every received V2X message using the HSM, completing signature verification within 5 ms per message to sustain the 1,000 messages/second throughput requirement. |
| **Rationale**    | Message authentication prevents acceptance of spoofed V2X messages that could inject false objects into the cooperative perception pipeline. |
| **Source**       | IEEE 1609.2 clause 5.3; ETSI TS 103 097; ISO 21434 TARA |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-HSM-01 |
| **Status**       | Baselined |

### REQ-SEC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The VCU shall maintain a Certificate Revocation List (CRL) and shall reject messages signed by revoked certificates, with CRL updates received via Uu interface at least once per hour when cellular connectivity is available. |
| **Rationale**    | Revoked certificates may indicate compromised vehicles or misbehaving participants whose V2X data should not be trusted. |
| **Source**       | IEEE 1609.2 clause 6.4; ETSI TS 103 097; ISO 21434 TARA |
| **Parent**       | REQ-SEC-001 |
| **Verification** | Test |
| **Allocation**   | CMP-HSM-01, CMP-APP-01D, CMP-UU-01 |
| **Status**       | Baselined |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The VCU shall deliver cooperative perception data to the ADAS fusion ECU via IFC-EXT-001 using CAN FD at a 10 Hz update rate with E2E protection, with a maximum end-to-end latency of 50 ms from PC5 message reception to ADAS output. |
| **Rationale**    | V2X data value degrades rapidly with latency; 50 ms ensures the data is usable for ADAS decision-making at vehicle speeds up to 130 km/h. |
| **Source**       | ADAS fusion ECU ICD; architecture timing budget |
| **Parent**       | REQ-FUN-004 |
| **Verification** | Test |
| **Allocation**   | CMP-APP-01C |
| **Status**       | Baselined |

## Performance Requirements

### REQ-PRF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The VCU shall achieve PC5 direct communication range of not less than 300 m in line-of-sight conditions and not less than 150 m in urban non-line-of-sight (single building obstruction) at the minimum required message reception rate of 90%. |
| **Rationale**    | Communication range determines the time available for cooperative perception to extend the vehicle's sensing horizon for intersection and merging scenarios. |
| **Source**       | ETSI TS 103 723 (V2X performance requirements); SAE J3161 |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-PC5-01 |
| **Status**       | Baselined |
