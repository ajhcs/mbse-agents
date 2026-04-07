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
| **Statement**    | The BMS shall measure individual cell voltages for all 192 cells with an accuracy of +/- 5 mV and a sampling rate of not less than 10 Hz. |
| **Rationale**    | Cell-level voltage monitoring is the primary input for SoC estimation, cell balancing, and over/under-voltage fault detection. |
| **Source**       | IEC 62619 clause 7.2; stakeholder need (OEM energy management) |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-CMU-01, CMP-CMU-01A |
| **Status**       | Baselined |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMS shall measure cell temperatures for each module using at least 2 thermistors per module with an accuracy of +/- 1C and a sampling rate of not less than 5 Hz. |
| **Rationale**    | Temperature monitoring detects thermal anomalies and supports thermal management control decisions. |
| **Source**       | IEC 62619 clause 7.3; ISO 6469 |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-CMU-01, CMP-CMU-01B |
| **Status**       | Baselined |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMS shall estimate pack state-of-charge (SoC) with an accuracy of +/- 3% over the full operating temperature range (-20C to +45C) and across the battery lifetime (0-100% SoH). |
| **Rationale**    | SoC accuracy drives range estimation accuracy and prevents deep discharge or overcharge conditions. |
| **Source**       | Stakeholder need (OEM range estimation); ISO 6469 |
| **Parent**       | -- |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-BMC-01, CMP-BMC-01D |
| **Status**       | Baselined |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMS shall control the thermal management loop to maintain all cell temperatures within 15C to 45C during normal driving and charging modes, by commanding coolant pump speed and valve position. |
| **Rationale**    | Operating cells outside the safe temperature window accelerates degradation and increases thermal runaway risk. |
| **Source**       | IEC 62619 clause 7.3; cell supplier specification |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-BMC-01, CMP-BMC-01E |
| **Status**       | Baselined |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMS shall perform passive cell balancing during MODE-002 (Charging) with a balancing current of 50-200 mA per cell, targeting cell voltage equalization to within 10 mV across the pack. |
| **Rationale**    | Cell balancing maximizes usable pack capacity by compensating for cell-to-cell manufacturing variation and aging differences. |
| **Source**       | Stakeholder need (OEM battery longevity) |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-CMU-01, CMP-CMU-01C |
| **Status**       | Baselined |

### REQ-FUN-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMS shall report pack voltage, pack current, SoC, SoH, maximum available discharge power, and maximum available charge power to the vehicle controller via CAN FD at a rate of 50 Hz. |
| **Rationale**    | The vehicle controller requires real-time pack data for powertrain torque management, regenerative braking coordination, and energy management. |
| **Source**       | Stakeholder need (OEM vehicle controller interface) |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-BMC-01, CMP-BMC-01F |
| **Status**       | Baselined |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMS shall detect thermal runaway onset (cell temperature rise rate exceeding 1C/s concurrent with cell voltage drop exceeding 100 mV/s) and shall command contactor opening within 100 ms of detection. |
| **Rationale**    | Rapid contactor disconnect removes electrical energy from a propagating thermal event, limiting severity. Sub-100 ms response is required because cell-to-cell propagation can occur within 1-5 seconds. |
| **Source**       | IEC 62619 clause 7.7; ISO 6469-1; ISO 26262 HARA (ASIL D hazard) |
| **Parent**       | -- |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-BMC-01C, CMP-HVC-01, CMP-HVC-01A |
| **Status**       | Baselined |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The HV contactor control path shall achieve a single-point fault metric (SPFM) of not less than 99% and a latent fault metric (LFM) of not less than 90%, verified by quantitative hardware fault analysis per ISO 26262-5 for ASIL D. |
| **Rationale**    | The contactor control path is ASIL D because failure to open contactors during a thermal event or crash exposes occupants to sustained high-voltage and thermal hazards. |
| **Source**       | ISO 26262-5 Table 4 (ASIL D); ISO 26262 HARA |
| **Parent**       | -- |
| **Verification** | Analysis |
| **Allocation**   | CMP-HVC-01, CMP-HVC-01A, CMP-HVC-01B |
| **Status**       | Baselined |

### REQ-SAF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMS shall open the HV contactors within 50 ms of receiving a crash signal from the vehicle crash sensor, transitioning to MODE-004 (Emergency Disconnect). |
| **Rationale**    | UN R100 requires HV isolation within a defined time after a crash to prevent electrical shock to occupants and rescue personnel. |
| **Source**       | UN R100 clause 6.4; ISO 6469-3 |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-HVC-01, CMP-HVC-01A, CMP-BMC-01C |
| **Status**       | Baselined |

### REQ-SAF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMS shall detect cell over-voltage (exceeding 4.25V per cell) and cell under-voltage (below 2.5V per cell) and shall derate discharge or charge current within 50 ms of detection. |
| **Rationale**    | Over-voltage during charging can cause lithium plating and thermal instability. Under-voltage during discharge causes irreversible copper dissolution and capacity loss. |
| **Source**       | IEC 62619 clause 7.2; cell supplier specification |
| **Parent**       | REQ-FUN-001 |
| **Verification** | Test |
| **Allocation**   | CMP-CMU-01A, CMP-BMC-01C, CMP-BMC-01D |
| **Status**       | Baselined |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | Each CMU shall communicate cell voltage and temperature data to the BMC via isoSPI daisy-chain with a maximum end-to-end latency of 10 ms for the complete 16-module scan cycle. |
| **Rationale**    | isoSPI provides galvanic isolation between HV cell measurement and LV processing domains while supporting the required 10 Hz minimum sampling rate across all modules. |
| **Source**       | Architecture ICD; ISO 6469 (HV isolation) |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-CMU-01, CMP-BMC-01B |
| **Status**       | Baselined |

### REQ-IFC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMC shall transmit pack status data (voltage, current, SoC, SoH, power limits, fault status) to the vehicle controller via IFC-EXT-001 using CAN FD at a 50 Hz update rate with E2E protection. |
| **Rationale**    | The vehicle controller requires fresh, integrity-protected pack data for torque and energy management decisions. |
| **Source**       | Vehicle controller ICD; stakeholder need (OEM) |
| **Parent**       | REQ-FUN-006 |
| **Verification** | Test |
| **Allocation**   | CMP-BMC-01F |
| **Status**       | Baselined |

## Performance Requirements

### REQ-PRF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMS shall complete a full system power-up self-test and transition to MODE-001 within 3 seconds of ignition-on, including CMU initialization, contactor pre-charge sequence, and isolation check. |
| **Rationale**    | Fast startup is required so that the HV system is available for vehicle launch within the driver's expected wait time. |
| **Source**       | Stakeholder need (OEM vehicle startup timing) |
| **Parent**       | -- |
| **Verification** | Test |
| **Allocation**   | CMP-BMC-01, CMP-CMU-01, CMP-HVC-01 |
| **Status**       | Baselined |
