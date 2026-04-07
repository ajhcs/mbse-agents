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
| **Statement**    | The SC-SoC shall execute ADAS application software on the Cortex-A78AE cluster with a sustained throughput of not less than 200 KDMIPS at 2.0 GHz clock frequency. |
| **Rationale**    | ADAS perception and planning algorithms require high-performance general-purpose compute. |
| **Source**       | Stakeholder need (ADAS system integrator) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-APP-01 |
| **Status**       | Draft |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The SC-SoC shall execute the lockstep CPU pair in split-lock mode, comparing instruction-retired signatures every clock cycle and asserting a lockstep fault signal within 2 clock cycles of a mismatch detection. |
| **Rationale**    | Lockstep execution with rapid fault detection is the primary mechanism for achieving ASIL D CPU diagnostic coverage. |
| **Source**       | ISO 26262-11 Clause 7 (hardware architectural metrics); stakeholder need (functional safety engineer) |
| **Parent**       | — |
| **Verification** | Test, Formal verification |
| **Allocation**   | CMP-LSC-01 |
| **Status**       | Draft |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The SC-SoC shall perform inline ECC on all on-chip SRAM accesses, correcting single-bit errors and detecting double-bit errors with a correction latency of not more than 1 clock cycle. |
| **Rationale**    | SRAM is the largest contributor to the random hardware fault budget; inline ECC achieves the required SPFM. |
| **Source**       | ISO 26262-11 Clause 7; stakeholder need (functional safety engineer) |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-MEM-01 |
| **Status**       | Draft |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The SC-SoC shall execute a background SRAM scrub cycle across all 4 MB of on-chip SRAM within a period of not more than 100 ms, correcting latent single-bit errors before they accumulate into uncorrectable multi-bit errors. |
| **Rationale**    | Background scrubbing limits latent fault accumulation within the PMHF budget. |
| **Source**       | ISO 26262-11 Annex D (latent fault analysis); stakeholder need (functional safety engineer) |
| **Parent**       | REQ-FUN-003 |
| **Verification** | Test |
| **Allocation**   | CMP-MEM-01 |
| **Status**       | Draft |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The SC-SoC shall provide a neural network accelerator delivering not less than 8 TOPS at INT8 precision for DNN inference workloads with a power efficiency of not less than 4 TOPS/W. |
| **Rationale**    | Object detection and classification networks for ADAS require dedicated hardware acceleration to meet real-time latency targets. |
| **Source**       | Stakeholder need (ADAS system integrator) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-NNA-01 |
| **Status**       | Draft |

### REQ-FUN-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The SC-SoC shall accept up to 8 MIPI CSI-2 camera streams at up to 2.5 Gbps per lane with 4-lane support per port, totaling a maximum aggregate input bandwidth of 80 Gbps. |
| **Rationale**    | Surround-view and multi-camera ADAS configurations require high aggregate sensor input bandwidth. |
| **Source**       | Stakeholder need (ADAS system integrator) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01 |
| **Status**       | Draft |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The SC-SoC shall achieve a single-point fault metric (SPFM) of not less than 99% across all safety-relevant logic, computed per ISO 26262-11 Annex C FMEDA methodology. |
| **Rationale**    | ASIL D hardware architectural metric target per ISO 26262-5 Table 4. |
| **Source**       | ISO 26262-5 Table 4; ISO 26262-11 Clause 7 |
| **Parent**       | — |
| **Verification** | Analysis |
| **Allocation**   | CMP-LSC-01, CMP-MEM-01, CMP-SAF-01 |
| **Status**       | Draft |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The SC-SoC shall achieve a latent fault metric (LFM) of not less than 90% across all safety-relevant logic, computed per ISO 26262-11 Annex C FMEDA methodology. |
| **Rationale**    | ASIL D hardware architectural metric target per ISO 26262-5 Table 4. |
| **Source**       | ISO 26262-5 Table 4; ISO 26262-11 Clause 7 |
| **Parent**       | — |
| **Verification** | Analysis |
| **Allocation**   | CMP-LSC-01, CMP-MEM-01, CMP-SAF-01 |
| **Status**       | Draft |

### REQ-SAF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The SC-SoC shall achieve a probabilistic metric for random hardware failures (PMHF) of less than 10 FIT for the safety-critical subsystem, computed over a vehicle lifetime of 15 years. |
| **Rationale**    | ASIL D PMHF target per ISO 26262-5 Table 5. |
| **Source**       | ISO 26262-5 Table 5; ISO 26262-11 Clause 7 |
| **Parent**       | — |
| **Verification** | Analysis |
| **Allocation**   | CMP-LSC-01, CMP-MEM-01, CMP-SAF-01, CMP-NOC-01 |
| **Status**       | Draft |

### REQ-SAF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The SC-SoC watchdog timer shall detect software execution faults within the lockstep CPU and shall assert a system reset if the watchdog is not serviced within 10 ms of the programmed timeout. |
| **Rationale**    | Watchdog provides a diverse diagnostic for software hangs and infinite loops not detected by lockstep comparison. |
| **Source**       | ISO 26262-11 Clause 8 (on-chip safety mechanisms); stakeholder need (functional safety engineer) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-SAF-01 |
| **Status**       | Draft |

### REQ-SAF-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The SC-SoC voltage monitor shall detect supply voltage excursions exceeding +/- 5% of nominal within 10 us and shall assert a safe-state signal to the ADAS ECU host. |
| **Rationale**    | Out-of-range supply voltage can cause logic malfunction; rapid detection ensures the host ECU can transition to a safe state. |
| **Source**       | ISO 26262-11 Clause 8; stakeholder need (ECU hardware engineer) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-SAF-01 |
| **Status**       | Draft |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The SC-SoC shall communicate with the ADAS ECU host processor via Automotive Ethernet (100BASE-T1) with a link-level latency of not more than 5 us and shall support TCP/IP and SOME/IP service discovery. |
| **Rationale**    | Automotive Ethernet is the standard interconnect for high-bandwidth ADAS data exchange within the ECU. |
| **Source**       | Stakeholder need (ADAS system integrator) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01 |
| **Status**       | Draft |

### REQ-IFC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The SC-SoC shall provide CAN-FD interface(s) supporting bit rates up to 5 Mbit/s for vehicle network communication, with hardware message filtering and at least 64 receive message buffers. |
| **Rationale**    | CAN-FD is required for integration with the vehicle communication backbone and safety-critical actuation commands. |
| **Source**       | Stakeholder need (ADAS system integrator) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PER-01 |
| **Status**       | Draft |
