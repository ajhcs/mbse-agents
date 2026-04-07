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
| **Statement**    | The system shall map surgeon hand controller movements to instrument tip movements with a configurable motion scaling ratio from 1:1 to 5:1, selectable by the surgeon during MODE-001. |
| **Rationale**    | Motion scaling enables fine manipulation beyond unaided human dexterity for microsurgical tasks. |
| **Source**       | Stakeholder need (surgeon); IEC 80601-2-77 Clause 201.12 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CON-01B, CMP-CTR-01A |
| **Status**       | Draft |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The system shall filter physiological hand tremor in the frequency range of 8 Hz to 12 Hz from the surgeon's hand controller input while preserving intentional movements below 4 Hz with less than 5% amplitude attenuation. |
| **Rationale**    | Tremor filtering improves instrument tip stability without degrading intentional surgical gestures. |
| **Source**       | Stakeholder need (surgeon); IEC 80601-2-77 |
| **Parent**       | REQ-FUN-001 |
| **Verification** | Test |
| **Allocation**   | CMP-CTR-01A |
| **Status**       | Draft |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The system shall provide haptic force feedback from the instrument tip to the surgeon's hand controllers with a round-trip latency of not more than 10 ms measured from force/torque sensor sampling to haptic actuator output. |
| **Rationale**    | Transparent haptic feedback below 10 ms preserves the surgeon's force perception and prevents tissue damage from excessive force. |
| **Source**       | IEC 80601-2-77; stakeholder need (surgeon) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PCA-01C, CMP-CON-01C, CMP-CTR-01A |
| **Status**       | Draft |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The system shall render stereoscopic 3D video from the endoscopic camera to the surgeon console display at a minimum of 60 frames per second with a glass-to-glass latency of not more than 100 ms. |
| **Rationale**    | Low-latency high-frame-rate stereo video is essential for depth perception and hand-eye coordination during teleoperation. |
| **Source**       | Stakeholder need (surgeon); IEC 80601-2-77 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-VIS-01A, CMP-VIS-01B, CMP-CON-01D |
| **Status**       | Draft |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The system shall detect the identity and usage count of each attached surgical instrument via the instrument recognition interface and shall prevent use of instruments that have exceeded their maximum usage cycle count. |
| **Rationale**    | Instrument tracking prevents use of worn instruments that may fail during a procedure. |
| **Source**       | Stakeholder need (biomedical engineering); IEC 80601-2-77 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PCA-01D, CMP-CTR-01A |
| **Status**       | Draft |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The system shall halt all instrument arm motion within 50 ms of detecting a joint position, velocity, or torque value outside the predefined safe operating envelope and shall transition to MODE-003 (Fault Hold). |
| **Rationale**    | Runaway arm motion is a critical hazard; immediate halt prevents patient injury. |
| **Source**       | IEC 80601-2-77 Clause 201.12.4; ISO 14971 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CTR-01A, CMP-CTR-01B, CMP-PCA-01B |
| **Status**       | Draft |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The system shall implement collision avoidance that prevents instrument arm-to-arm contact and arm-to-patient contact by enforcing minimum separation distances and reducing arm velocity as separation decreases, without requiring surgeon intervention. |
| **Rationale**    | Multi-arm collision is a foreseeable hazard unique to multi-arm robotic surgical systems. |
| **Source**       | IEC 80601-2-77; ISO 14971 |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-CTR-01A, CMP-PCA-01B |
| **Status**       | Draft |

### REQ-SAF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | Upon loss of the communication link between the surgeon console and the patient-side cart exceeding 100 ms, the system shall transition to MODE-003 (Fault Hold), halt all instrument motion, and annunciate an audible and visual alarm at both the console and the patient-side cart. |
| **Rationale**    | Uncontrolled instrument motion during communication loss can cause patient injury. |
| **Source**       | IEC 80601-2-77 Clause 201.12.4; ISO 14971 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CTR-01A, CMP-CON-01A, CMP-PCA-01A |
| **Status**       | Draft |

### REQ-SAF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The system shall limit the maximum force exertable by any instrument arm to 25 N, enforced by an independent hardware current limiter on each motor driver that is not software-overridable. |
| **Rationale**    | Hardware force limiting provides defense in depth against software faults that could command excessive arm force. |
| **Source**       | IEC 80601-2-77; ISO 14971 |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-PCA-01E |
| **Status**       | Draft |

### REQ-SAF-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The system shall provide a physical emergency stop button accessible from both the surgeon console and the patient-side cart that immediately removes power from all motor drives and engages joint brakes within 100 ms of activation. |
| **Rationale**    | Emergency stop is required as a last-resort safety measure independent of software control. |
| **Source**       | IEC 60601-1 Clause 9.2; IEC 80601-2-77 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CON-01E, CMP-PCA-01F |
| **Status**       | Draft |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The communication link between the surgeon console and the patient-side cart shall maintain a round-trip latency of not more than 2 ms and a packet loss rate of less than 10^-9 during MODE-001 (Teleoperation). |
| **Rationale**    | Deterministic low-latency communication is essential for stable teleoperation control loops and haptic transparency. |
| **Source**       | IEC 80601-2-77; architecture decision AD-01 |
| **Parent**       | REQ-FUN-003 |
| **Verification** | Test |
| **Allocation**   | CMP-CON-01A, CMP-PCA-01A |
| **Status**       | Draft |

### REQ-IFC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The system shall interface with the electrosurgical generator via IFC-EXT-004 to activate and deactivate electrosurgical energy only when the surgeon foot pedal is depressed and the instrument is confirmed engaged, and shall remove energy within 50 ms of foot pedal release. |
| **Rationale**    | Uncontrolled electrosurgical energy application can cause thermal burns to the patient and OR staff. |
| **Source**       | IEC 80601-2-77; ISO 14971 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CON-01E, CMP-PCA-01D |
| **Status**       | Draft |
