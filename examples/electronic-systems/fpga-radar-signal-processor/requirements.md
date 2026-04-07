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
| Verification  | Method: test, analysis, inspection, demonstration, formal verification                            |
| Allocation    | Target component ID(s) from architecture.md                                                       |
| Status        | Draft, baselined, verified, deferred                                                              |

## Functional Requirements

### REQ-FUN-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The FRSP shall accept 16 simultaneous ADC input channels at 14-bit resolution and 250 MSPS sample rate per channel via LVDS interfaces, and shall align all channels to within 1 sample period (4 ns) of a common time reference. |
| **Rationale**    | Phased array beamforming requires time-aligned samples from all receive channels. |
| **Source**       | Stakeholder need (radar system engineer) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-ADC-01 |
| **Status**       | Draft |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The FRSP shall perform digital pulse compression on each receive channel using a programmable matched filter with a processing gain of not less than 30 dB for waveform bandwidths up to 10 MHz. |
| **Rationale**    | Pulse compression improves range resolution and SNR, enabling detection of small targets at long range. |
| **Source**       | Stakeholder need (radar system engineer) |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-PC-01 |
| **Status**       | Draft |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The FRSP shall perform Doppler processing via range-gated FFT with a minimum of 64 pulse integration and a velocity resolution of not greater than 5 m/s at X-band (9.5 GHz). |
| **Rationale**    | Doppler resolution determines the ability to separate targets from clutter and to resolve closely spaced movers. |
| **Source**       | Stakeholder need (radar system engineer) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-DOP-01 |
| **Status**       | Draft |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The FRSP shall execute CFAR detection using selectable cell-averaging (CA-CFAR) and ordered-statistic (OS-CFAR) algorithms, maintaining a false alarm rate of not more than 10^-6 per range-Doppler cell under Swerling I target models. |
| **Rationale**    | Adaptive detection thresholding is required to maintain constant false alarm probability across varying clutter environments. |
| **Source**       | Stakeholder need (radar system engineer) |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-DET-01 |
| **Status**       | Draft |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The FRSP shall format detected target reports containing range, Doppler velocity, azimuth angle, elevation angle, and signal-to-noise ratio, and shall transmit reports to the track processor via IFC-EXT-003 within 2 ms of detection completion per radar dwell. |
| **Rationale**    | Timely delivery of target reports to the track processor is required to maintain track update rate. |
| **Source**       | Stakeholder need (radar system engineer) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RPT-01 |
| **Status**       | Draft |

### REQ-FUN-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The FRSP shall complete the full processing chain (pulse compression, Doppler FFT, CFAR detection, report generation) within a single pulse repetition interval at a maximum PRF of 20 kHz (50 us processing budget). |
| **Rationale**    | Real-time processing without pipeline stalls is required to avoid data loss at the maximum operating PRF. |
| **Source**       | Stakeholder need (radar system engineer); system timing budget |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-PC-01, CMP-DOP-01, CMP-DET-01, CMP-RPT-01 |
| **Status**       | Draft |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The FRSP shall inhibit all output data that could command radar transmission within 10 us of detecting a BIT failure, and shall assert an RF inhibit signal on IFC-EXT-005 to the radar controller. |
| **Rationale**    | A processing fault could produce erroneous beam steering commands that direct the radar beam toward personnel or restricted zones. |
| **Source**       | MIL-STD-882E hazard analysis (unintended radiation); stakeholder need (safety engineer) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-BIT-01, CMP-RPT-01 |
| **Status**       | Draft |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The FRSP shall detect single-event upset (SEU) corruption in FPGA configuration memory via continuous frame-level CRC scrubbing, completing a full configuration memory scan in not more than 100 ms, and shall initiate partial reconfiguration of the affected region upon CRC mismatch. |
| **Rationale**    | SEU in configuration memory can silently alter processing logic, producing undetected erroneous target reports or unintended RF control outputs. |
| **Source**       | MIL-STD-882E hazard analysis (data integrity); DO-254 Section 11.4 (SEU considerations) |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-CFG-01 |
| **Status**       | Draft |

### REQ-SAF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The FRSP shall validate all clock domain crossing (CDC) paths using formal CDC verification during RTL design, with zero unresolved asynchronous crossings in the final design. |
| **Rationale**    | Unverified CDC paths risk metastability-induced data corruption that could produce spurious target detections or missed real targets. |
| **Source**       | DO-254 Appendix B (design assurance considerations for PLDs); stakeholder need (DO-254 DER) |
| **Parent**       | — |
| **Verification** | Formal verification, Inspection |
| **Allocation**   | CMP-ADC-01, CMP-PC-01, CMP-DOP-01, CMP-RPT-01 |
| **Status**       | Draft |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The FRSP shall receive waveform parameters and beam steering commands from the radar controller via IFC-EXT-002 (SpaceWire) with a command latency of not more than 50 us from command receipt to processing pipeline reconfiguration. |
| **Rationale**    | Waveform agility requires rapid reconfiguration of matched filter coefficients and processing chain parameters between radar dwells. |
| **Source**       | Stakeholder need (radar system engineer) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RPT-01, CMP-PC-01 |
| **Status**       | Draft |

### REQ-IFC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The FRSP shall transmit radar status words and BIT results to the aircraft mission computer via MIL-STD-1553B (IFC-EXT-004) at a message rate of not less than 20 Hz. |
| **Rationale**    | The mission computer requires timely health status for operational decisions and maintenance logging. |
| **Source**       | Stakeholder need (aircraft integrator); MIL-STD-1553B |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-BUS-01 |
| **Status**       | Draft |
