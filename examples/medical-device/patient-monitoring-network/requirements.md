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
| **Statement**    | The bedside monitor shall continuously acquire and display SpO2, ECG (heart rate, rhythm), NIBP, body temperature, and EtCO2 parameters with parameter-specific update rates: ECG waveform at 250 Hz, SpO2 at 1 Hz, NIBP on demand or at configurable intervals (1-240 min), temperature at 0.1 Hz, and EtCO2 waveform at 25 Hz. |
| **Rationale**    | Multi-parameter monitoring provides comprehensive physiological assessment for acute care patients. |
| **Source**       | Stakeholder need (bedside nurse); FDA 510(k) predicate |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-BED-01A, CMP-BED-01B, CMP-BED-01C |
| **Status**       | Draft |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The bedside monitor shall generate alarms conforming to IEC 60601-1-8 alarm priority categories (high, medium, low) based on parameter-specific alarm limits configurable by the clinician within manufacturer-defined safety ranges. |
| **Rationale**    | Standardized alarm priorities ensure consistent clinician recognition and response across monitoring parameters. |
| **Source**       | IEC 60601-1-8 Clause 6.3; stakeholder need (bedside nurse) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-BED-01D, CMP-BED-01E |
| **Status**       | Draft |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The bedside monitor shall implement configurable alarm delay (0 to 30 seconds) per parameter to suppress transient threshold crossings caused by patient motion artifacts, and shall not delay high-priority alarms for asystole, ventricular fibrillation, or apnea conditions. |
| **Rationale**    | Alarm delay reduces nuisance alarms from motion artifact while preserving immediate notification for life-threatening arrhythmias. |
| **Source**       | IEC 60601-1-8; stakeholder need (bedside nurse); ISO 14971 |
| **Parent**       | REQ-FUN-002 |
| **Verification** | Test |
| **Allocation**   | CMP-BED-01D |
| **Status**       | Draft |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The bedside monitor shall transmit physiological data and alarm events to the central station over the dedicated monitoring network with an end-to-end latency from alarm condition detection to central station alarm annunciation of not more than 5 seconds. |
| **Rationale**    | Bounded alarm latency ensures the central station provides timely backup notification when the bedside nurse is unavailable. |
| **Source**       | IEC 60601-1-8 (distributed alarm systems); stakeholder need (monitor technician) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-BED-01F, CMP-NET-01, CMP-CEN-01A |
| **Status**       | Draft |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The central station shall simultaneously display physiological waveforms, numeric parameters, and alarm status for up to 32 patients with a display refresh rate of not less than 1 Hz for numeric values and 50 Hz for ECG waveforms. |
| **Rationale**    | Central station capacity must match the patient-to-nurse ratio in acute care units. |
| **Source**       | Stakeholder need (monitor technician); FDA 510(k) predicate |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CEN-01A, CMP-CEN-01B |
| **Status**       | Draft |

### REQ-FUN-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The central station shall escalate unacknowledged high-priority alarms to the nurse call system via IFC-EXT-003 within 30 seconds of initial alarm annunciation if neither the bedside nurse nor the central station technician acknowledges the alarm. |
| **Rationale**    | Alarm escalation to nurse call provides a secondary notification pathway when primary responders are unavailable. |
| **Source**       | IEC 60601-1-8 (alarm escalation); stakeholder need (patient safety) |
| **Parent**       | REQ-FUN-004 |
| **Verification** | Test |
| **Allocation**   | CMP-CEN-01C, CMP-GW-01 |
| **Status**       | Draft |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | Upon loss of network connectivity between a bedside monitor and the central station (MODE-004), the bedside monitor shall continue all local physiological monitoring and alarm annunciation functions without degradation, and shall display a visible network status indicator to the bedside clinician. |
| **Rationale**    | Network failure must not degrade bedside patient safety; central station is a supplementary monitoring layer. |
| **Source**       | IEC 80001-1; ISO 14971 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-BED-01, CMP-BED-01F |
| **Status**       | Draft |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The bedside monitor shall generate a high-priority alarm within 10 seconds of detecting asystole (no QRS complex for 4 seconds) and within 5 seconds of detecting ventricular fibrillation, and these alarms shall not be subject to alarm delay or clinician-configurable suppression. |
| **Rationale**    | Lethal arrhythmia detection is the most time-critical alarm function; delay or suppression could result in patient death. |
| **Source**       | IEC 60601-1-8; IEC 60601-2-27 (ECG particular standard); ISO 14971 |
| **Parent**       | REQ-FUN-002 |
| **Verification** | Test |
| **Allocation**   | CMP-BED-01D, CMP-BED-01E |
| **Status**       | Draft |

### REQ-SAF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The dedicated monitoring network shall provide electrical isolation between each bedside monitor and the network infrastructure conforming to IEC 60601-1 Clause 8.5 MOPP (2 MOPP for patient-connected devices), and shall not create an electrical path between patients connected to different bedside monitors. |
| **Rationale**    | Network cabling must not create patient-to-patient leakage current paths or compromise the means of patient protection. |
| **Source**       | IEC 60601-1 Clause 8.5; IEC 80001-1 |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-BED-01F, CMP-NET-01 |
| **Status**       | Draft |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The gateway server shall transmit patient physiological data and alarm events to the EMR via IFC-EXT-002 using HL7 v2 ADT/ORU messages or FHIR Observation resources within 60 seconds of the triggering event. |
| **Rationale**    | EMR integration automates clinical documentation and supports retrospective analysis. |
| **Source**       | Stakeholder need (bedside nurse, hospital IT); IEC 80001-1 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-GW-01 |
| **Status**       | Draft |

### REQ-IFC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The gateway server shall receive ADT messages from the hospital ADT system via IFC-EXT-004 and shall automatically associate patient demographics with the bedside monitor assigned to the corresponding bed location. |
| **Rationale**    | Automated patient-monitor association reduces manual data entry errors and supports correct alarm routing. |
| **Source**       | Stakeholder need (bedside nurse); IEC 80001-1 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-GW-01, CMP-CEN-01A |
| **Status**       | Draft |

## Performance Requirements

### REQ-PRF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The dedicated monitoring network shall sustain a maximum network utilization of 50% under full patient load (32 bedside monitors transmitting continuously) to ensure deterministic alarm delivery within the 5-second latency budget under worst-case traffic conditions. |
| **Rationale**    | Network congestion beyond 50% utilization introduces non-deterministic queuing delays that can violate the alarm latency requirement. |
| **Source**       | IEC 80001-1; architecture decision AD-02 |
| **Parent**       | REQ-FUN-004 |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-NET-01 |
| **Status**       | Draft |
