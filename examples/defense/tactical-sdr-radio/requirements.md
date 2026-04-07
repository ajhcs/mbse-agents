# Requirements

All requirements are atomic, testable shall-statements.

## Requirement Record Schema

| Field         | Description                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------|
| ID            | Unique identifier (e.g., REQ-FUN-001)                                                            |
| Statement     | Atomic shall-statement                                                                            |
| Rationale     | Why this requirement exists                                                                       |
| Source        | Regulatory clause, stakeholder need, or safety concern                                            |
| Parent        | Parent requirement ID (if derived)                                                                |
| Verification  | Method: test, analysis, inspection, demonstration                                                 |
| Allocation    | Target component ID(s) from architecture.md                                                       |
| Status        | Draft, baselined, verified, deferred                                                              |

## Functional Requirements

### REQ-FUN-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The radio shall host and simultaneously execute up to four SCA 4.1 conformant waveform applications across independent RF channels. |
| **Rationale**    | Multi-channel operation enables simultaneous voice, data, and networking on different waveforms. |
| **Source**       | Stakeholder need (signal/communications officer); SCA 4.1 |
| **Parent**       | — |
| **Verification** | Test, Demonstration |
| **Allocation**   | CMP-SDP-01A, CMP-SDP-01B |
| **Status**       | Draft |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The radio shall load, verify, and deploy waveform application software from external media within 60 seconds per waveform, with cryptographic integrity verification before deployment to the SCA execution environment. |
| **Rationale**    | Waveform loading must be fast for tactical responsiveness; integrity verification prevents deployment of compromised waveform code. |
| **Source**       | SCA 4.1; NSA CNSS policy |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-SDP-01A, CMP-SDP-01C |
| **Status**       | Draft |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The radio shall provide MANET networking capability supporting up to 30 network nodes with self-forming, self-healing mesh topology and a minimum sustained data throughput of 2 Mbps per channel. |
| **Rationale**    | MANET enables infrastructure-free communications essential for dismounted and mobile tactical operations. |
| **Source**       | Stakeholder need (tactical radio operator); operational requirements document |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-SDP-01B |
| **Status**       | Draft |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The radio shall encrypt all transmitted data using the embedded NSA Type 1 cryptographic module with COMSEC key loaded via SKL or OTAR, and shall not transmit plaintext on any operational channel unless the operator explicitly selects MODE-002 (COMSEC Bypass). |
| **Rationale**    | COMSEC protection of all tactical communications is the default operational posture; bypass is an emergency exception. |
| **Source**       | NSA CNSS / CNSSP 11; stakeholder need (COMSEC custodian) |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-CRM-01A |
| **Status**       | Draft |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The radio shall provide TRANSEC (transmission security) including low probability of intercept (LPI) and low probability of detection (LPD) modes with frequency hopping rates of at least 200 hops per second on applicable waveforms. |
| **Rationale**    | TRANSEC protects against adversary detection and direction-finding of tactical radio emissions. |
| **Source**       | NSA CNSS; operational requirements document |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-CRM-01A, CMP-RFT-01A |
| **Status**       | Draft |

### REQ-FUN-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The radio shall interface with the host platform antenna subsystem via IFC-EXT-001 across HF (2-30 MHz), VHF (30-88 MHz), UHF (225-512 MHz), and L-band (1350-1850 MHz) frequency ranges with automatic antenna tuning. |
| **Rationale**    | Multi-band coverage supports the range of JTRS waveforms required for joint/coalition interoperability. |
| **Source**       | Stakeholder need (signal/communications officer); JTRS frequency plan |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RFT-01A, CMP-RFT-01B |
| **Status**       | Draft |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The radio shall execute emergency cryptographic zeroization of all key material within 10 seconds of operator initiation, rendering all keys unrecoverable. |
| **Rationale**    | Zeroization prevents key compromise when the radio is at risk of capture. Failure to zeroize could compromise the entire COMSEC net. |
| **Source**       | MIL-STD-882E; NSA CNSS / CNSSP 11 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CRM-01A |
| **Status**       | Draft |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The radio shall enforce hardware-level separation between red (plaintext) and black (ciphertext) data paths such that no single software fault can cause plaintext data to appear on the black side of the crypto boundary. |
| **Rationale**    | Software-only red/black separation is insufficient for Type 1 certification; hardware enforcement is required to prevent plaintext leakage under fault conditions. |
| **Source**       | NSA CNSS; NSA Type 1 certification requirements |
| **Parent**       | — |
| **Verification** | Analysis, Inspection |
| **Allocation**   | CMP-CRM-01A, CMP-SDP-01A |
| **Status**       | Draft |

### REQ-SAF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The radio shall limit RF output power to the configured maximum for the selected waveform and band, and shall inhibit RF transmission when no antenna is connected or when a fault is detected in the RF output path. |
| **Rationale**    | Unterminated RF output can damage the transceiver; excessive power can cause harmful interference or violate spectrum allocation. |
| **Source**       | MIL-STD-882E; MIL-STD-461G |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RFT-01A |
| **Status**       | Draft |

### REQ-SAF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The radio shall prevent waveform application software from directly accessing the cryptographic module key storage, crypto algorithms, or red-side data paths; all crypto operations shall be mediated through the SCA security service API. |
| **Rationale**    | Untrusted or compromised waveform code must not be able to extract key material or bypass encryption. |
| **Source**       | SCA 4.1 security model; NSA Type 1 certification requirements |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-SDP-01C, CMP-CRM-01A |
| **Status**       | Draft |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The radio shall interface with the antenna subsystem via IFC-EXT-001 providing RF signal input/output across all supported frequency bands with a maximum VSWR of 2.0:1 at the antenna port. |
| **Rationale**    | Antenna interface specification ensures RF performance across all waveform operating bands. |
| **Source**       | Host platform ICD; MIL-STD-461G |
| **Parent**       | REQ-FUN-006 |
| **Verification** | Test |
| **Allocation**   | CMP-RFT-01B |
| **Status**       | Draft |

### REQ-IFC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The radio shall provide a host platform data interface via IFC-EXT-003 using Gigabit Ethernet with FACE 3.1 TSS data transport APIs for C2 and mission system connectivity. |
| **Rationale**    | FACE-conformant host interface enables portability of host platform applications across radio platforms. |
| **Source**       | FACE 3.1; stakeholder need (host platform integrator) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-SDP-01D |
| **Status**       | Draft |

## Performance Requirements

### REQ-PRF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The radio shall achieve full operational status (MODE-001) within 30 seconds of power application, including SCA framework initialization, waveform deployment from stored configuration, and crypto key activation. |
| **Rationale**    | Rapid startup supports tactical responsiveness for dismounted operations. |
| **Source**       | Stakeholder need (tactical radio operator); operational requirements document |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-SDP-01A, CMP-CRM-01A, CMP-RFT-01A |
| **Status**       | Draft |
