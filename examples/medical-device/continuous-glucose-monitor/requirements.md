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
| **Statement**    | The sensor shall measure interstitial glucose concentration in the range of 40 mg/dL to 400 mg/dL with a mean absolute relative difference (MARD) of not more than 10% compared to venous blood glucose reference over the 14-day sensor wear period. |
| **Rationale**    | Glucose measurement accuracy directly impacts treatment decisions and patient safety. |
| **Source**       | FDA 510(k) predicate performance requirements; stakeholder need (patient, endocrinologist) |
| **Parent**       | — |
| **Verification** | Test (clinical study) |
| **Allocation**   | CMP-SNS-01A, CMP-SNS-01B, CMP-SNS-01C |
| **Status**       | Draft |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The sensor shall sample glucose concentration at intervals of not more than 5 minutes during MODE-001 (Continuous Monitor) and shall transmit each reading to the mobile application within 10 seconds of sampling via BLE. |
| **Rationale**    | Frequent sampling with prompt transmission enables real-time glucose trend monitoring. |
| **Source**       | Stakeholder need (patient); FDA 510(k) predicate |
| **Parent**       | REQ-FUN-001 |
| **Verification** | Test |
| **Allocation**   | CMP-SNS-01C, CMP-SNS-01D |
| **Status**       | Draft |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The mobile application shall display the current glucose value, a trend arrow indicating the rate and direction of glucose change, and a time-series graph of the preceding 3 hours of glucose readings, with display updates within 5 seconds of receiving a new BLE transmission. |
| **Rationale**    | Real-time trend visualization supports patient self-management decisions. |
| **Source**       | Stakeholder need (patient); IEC 62366-1 (usability) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-APP-01A |
| **Status**       | Draft |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The mobile application shall generate configurable audible and haptic alerts when the glucose value crosses user-defined high and low thresholds, and shall generate an urgent alarm when glucose falls below 55 mg/dL or exceeds 400 mg/dL. |
| **Rationale**    | Hypoglycemia and severe hyperglycemia alerts are safety-critical notifications. |
| **Source**       | ISO 14971; stakeholder need (patient) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-APP-01A, CMP-APP-01B |
| **Status**       | Draft |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The cloud analytics platform shall compute time-in-range (70-180 mg/dL), glucose management indicator (GMI), and coefficient of variation from aggregated sensor data and shall make these metrics available to the healthcare provider within 15 minutes of data upload. |
| **Rationale**    | Standardized glucose metrics support clinical decision-making per international consensus guidelines. |
| **Source**       | Stakeholder need (endocrinologist); international consensus on CGM reporting |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CLD-01A, CMP-CLD-01B |
| **Status**       | Draft |

### REQ-FUN-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The insulin dosing guidance algorithm (SaMD) shall generate insulin dose adjustment recommendations based on glucose trend patterns over the preceding 14 days and shall present recommendations with the underlying data and rationale to the healthcare provider, not directly to the patient. |
| **Rationale**    | Dosing guidance is classified as SaMD Category II (serious condition, informs clinical management); provider-in-the-loop mitigates risk. |
| **Source**       | IMDRF SaMD N41; FDA SaMD guidance; ISO 14971 |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-CLD-01C |
| **Status**       | Draft |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The sensor firmware shall store the most recent 8 hours of glucose readings in non-volatile memory such that data is preserved through BLE disconnection (MODE-003) and is transmitted to the mobile application upon BLE reconnection. |
| **Rationale**    | Data loss during disconnection creates gaps in glucose history that can mask hypoglycemic episodes. |
| **Source**       | ISO 14971; stakeholder need (patient, endocrinologist) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-SNS-01C |
| **Status**       | Draft |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The system shall suppress glucose display and dosing guidance during MODE-002 (Warm-Up) and shall indicate sensor stabilization status to the user, preventing treatment decisions based on inaccurate readings. |
| **Rationale**    | Sensor readings during warm-up are unreliable; displaying them could lead to inappropriate insulin dosing. |
| **Source**       | ISO 14971; FDA 510(k) predicate labeling |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-SNS-01C, CMP-APP-01A |
| **Status**       | Draft |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The BLE communication between the sensor and the mobile application shall use AES-128 encryption with bonded pairing and shall reject connections from unbonded devices. |
| **Rationale**    | BLE encryption prevents eavesdropping on glucose data and spoofing of sensor readings. |
| **Source**       | FDA premarket cybersecurity guidance; ISO 14971 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-SNS-01D, CMP-APP-01B |
| **Status**       | Draft |

### REQ-IFC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The cloud API shall authenticate all data submissions using OAuth 2.0 with short-lived tokens and shall encrypt data in transit using TLS 1.2 or higher and at rest using AES-256. |
| **Rationale**    | Cloud API security protects patient health information per HIPAA requirements. |
| **Source**       | FDA premarket cybersecurity guidance; HIPAA Security Rule |
| **Parent**       | — |
| **Verification** | Test, Inspection |
| **Allocation**   | CMP-APP-01B, CMP-CLD-01A |
| **Status**       | Draft |

## Performance Requirements

### REQ-PRF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The sensor patch battery shall sustain continuous glucose measurement and BLE transmission for a minimum of 14 days with a sampling interval of 5 minutes and BLE advertisement interval of 5 seconds. |
| **Rationale**    | Battery life must match the sensor wear duration to avoid premature system failure. |
| **Source**       | Stakeholder need (patient); architecture constraint |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-SNS-01E |
| **Status**       | Draft |
