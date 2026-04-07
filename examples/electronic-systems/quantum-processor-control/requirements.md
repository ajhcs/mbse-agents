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
| **Statement**    | The QPCS shall execute compiled quantum gate sequences, translating each gate into timed RF pulse parameters and flux bias setpoints dispatched to the appropriate subsystems within the timing window specified by the sequence. |
| **Rationale**    | Core operational capability: translating abstract gate sequences into physical control signals. |
| **Source**       | Stakeholder need (quantum physicist) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RTO-01A |
| **Status**       | Baselined |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall support concurrent execution of gate operations on at least 100 qubits, with independent per-qubit pulse parameters and flux bias setpoints. |
| **Rationale**    | System must scale to the full qubit count of the quantum processor chip. |
| **Source**       | Stakeholder need (quantum physicist); system specification |
| **Parent**       | REQ-FUN-001 |
| **Verification** | Test |
| **Allocation**   | CMP-RTO-01A |
| **Status**       | Baselined |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall formally verify each compiled gate sequence against timing constraints, power limits, and frequency collision rules before permitting execution, completing verification within 100 ms for circuits of up to 10,000 gates. |
| **Rationale**    | Pre-execution verification prevents sequences that could violate safety limits or produce physically invalid control signals. |
| **Source**       | CTL-001; stakeholder need (safety officer) |
| **Parent**       | — |
| **Verification** | Test, Formal verification |
| **Allocation**   | CMP-RTO-01E |
| **Status**       | Baselined |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall accept, prioritize, and queue quantum computation jobs from the cloud job scheduler via IFC-EXT-002, supporting at least 1,000 queued jobs with priority-based scheduling. |
| **Rationale**    | Multi-user quantum computing platforms require job queuing and fair scheduling. |
| **Source**       | Stakeholder need (cloud job scheduler interface) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RTO-01A |
| **Status**       | Baselined |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The RPG shall generate shaped microwave pulses at frequencies between 4 GHz and 8 GHz with an amplitude resolution of 14 bits and a sample rate of not less than 2.4 GSPS per channel. |
| **Rationale**    | Superconducting qubit transition frequencies fall in the 4-8 GHz band; amplitude resolution and sample rate determine gate fidelity. |
| **Source**       | Stakeholder need (control electronics engineer) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RPG-01A, CMP-RPG-01B |
| **Status**       | Baselined |

### REQ-FUN-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The RPG shall produce pulse envelopes with a rise/fall time of not more than 2 ns and a duration programmable from 10 ns to 10 us in 1 ns increments. |
| **Rationale**    | Fast pulse edges and fine duration control are required for high-fidelity single-qubit gates and readout pulses. |
| **Source**       | Stakeholder need (quantum physicist) |
| **Parent**       | REQ-FUN-005 |
| **Verification** | Test |
| **Allocation**   | CMP-RPG-01A, CMP-RPG-01D |
| **Status**       | Baselined |

### REQ-FUN-007
| Field        | Value |
|--------------|-------|
| **Statement**    | The RPG output power limiter shall enforce a maximum output power of -20 dBm at the cryostat input flange, independent of the waveform commanded by the orchestration software. |
| **Rationale**    | RF power exceeding -20 dBm at the chip can damage Josephson junctions. The hardware limiter provides a safety barrier independent of software. |
| **Source**       | HZ-001; CTL-002; IEC 61508 SIL 2 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RPG-01C, CMP-SAF-01B |
| **Status**       | Baselined |

### REQ-FUN-008
| Field        | Value |
|--------------|-------|
| **Statement**    | The CRE shall digitize readout resonator signals at a sample rate of not less than 1 GSPS with 12-bit resolution and shall produce qubit state discrimination results within 500 ns of readout pulse completion. |
| **Rationale**    | High-speed digitization and fast state discrimination are required for mid-circuit measurement and error correction feedback. |
| **Source**       | Stakeholder need (quantum physicist) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CRE-01A, CMP-CRE-01B, CMP-CRE-01D |
| **Status**       | Baselined |

### REQ-FUN-009
| Field        | Value |
|--------------|-------|
| **Statement**    | The CRE shall achieve a qubit state discrimination fidelity of not less than 99.0% for single-shot readout under standard operating conditions (qubit T1 > 50 us). |
| **Rationale**    | Readout fidelity directly limits quantum error correction performance and experiment quality. |
| **Source**       | Stakeholder need (quantum physicist) |
| **Parent**       | REQ-FUN-008 |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-CRE-01A, CMP-CRE-01D |
| **Status**       | Baselined |

### REQ-FUN-010
| Field        | Value |
|--------------|-------|
| **Statement**    | The CRE shall support simultaneous frequency-multiplexed readout of at least 8 qubits per readout channel with per-qubit state assignment. |
| **Rationale**    | Multiplexed readout reduces the number of physical readout channels required, enabling scaling to 100+ qubits. |
| **Source**       | Stakeholder need (control electronics engineer) |
| **Parent**       | REQ-FUN-008 |
| **Verification** | Test |
| **Allocation**   | CMP-CRE-01A, CMP-CRE-01D |
| **Status**       | Baselined |

### REQ-FUN-011
| Field        | Value |
|--------------|-------|
| **Statement**    | The FBC shall provide per-qubit DC bias current with a resolution of not less than 20 bits and a current noise floor below 100 pA/sqrt(Hz) at 1 Hz. |
| **Rationale**    | Qubit frequency is sensitive to flux bias noise; low-noise DACs are required to maintain coherence. |
| **Source**       | Stakeholder need (control electronics engineer) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FBC-01A |
| **Status**       | Baselined |

### REQ-FUN-012
| Field        | Value |
|--------------|-------|
| **Statement**    | The FBC shall update all flux bias channels simultaneously within a settling time of not more than 1 us to the final value within 0.01% of the target setpoint. |
| **Rationale**    | Fast, accurate flux bias updates are required for two-qubit gate operations that rely on frequency tuning. |
| **Source**       | Stakeholder need (quantum physicist) |
| **Parent**       | REQ-FUN-011 |
| **Verification** | Test |
| **Allocation**   | CMP-FBC-01A, CMP-FBC-01C |
| **Status**       | Baselined |

### REQ-FUN-013
| Field        | Value |
|--------------|-------|
| **Statement**    | The FBC current limiter shall enforce a maximum output current of 10 mA per channel, independent of the setpoint commanded by the orchestration software. |
| **Rationale**    | Flux bias current exceeding 10 mA can permanently damage Josephson junctions. The hardware limiter provides a safety barrier independent of software. |
| **Source**       | HZ-002; CTL-003; IEC 61508 SIL 2 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FBC-01B, CMP-SAF-01B |
| **Status**       | Baselined |

### REQ-FUN-014
| Field        | Value |
|--------------|-------|
| **Statement**    | The TDU shall distribute a phase-coherent reference clock to all subsystems with a channel-to-channel skew of not more than 100 ps. |
| **Rationale**    | Sub-nanosecond synchronization is required for two-qubit gate fidelity across different control channels. |
| **Source**       | Stakeholder need (quantum physicist); system timing budget |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-TDU-01A, CMP-TDU-01B |
| **Status**       | Baselined |

### REQ-FUN-015
| Field        | Value |
|--------------|-------|
| **Statement**    | The TDU shall generate programmable trigger patterns with a trigger-to-trigger jitter of not more than 50 ps RMS. |
| **Rationale**    | Trigger jitter directly contributes to gate timing error and limits achievable gate fidelity. |
| **Source**       | Stakeholder need (control electronics engineer); system timing budget |
| **Parent**       | REQ-FUN-014 |
| **Verification** | Test |
| **Allocation**   | CMP-TDU-01C |
| **Status**       | Baselined |

### REQ-FUN-016
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall execute automated calibration protocols (Rabi oscillation, Ramsey fringe, T1 decay, T2 echo, randomized benchmarking) without manual intervention, completing a full single-qubit calibration cycle in not more than 5 minutes per qubit. |
| **Rationale**    | Daily calibration of 100+ qubits requires automated protocols to maintain operational efficiency. |
| **Source**       | Stakeholder need (hardware calibration engineer) |
| **Parent**       | — |
| **Verification** | Test, Demonstration |
| **Allocation**   | CMP-RTO-01B |
| **Status**       | Baselined |

### REQ-FUN-017
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall execute two-qubit calibration protocols (cross-resonance, CZ gate, iSWAP) and shall update coupling parameters in the calibration database upon successful completion. |
| **Rationale**    | Two-qubit gate calibration is essential for entangling operations on the processor. |
| **Source**       | Stakeholder need (hardware calibration engineer) |
| **Parent**       | REQ-FUN-016 |
| **Verification** | Test, Demonstration |
| **Allocation**   | CMP-RTO-01B |
| **Status**       | Baselined |

### REQ-FUN-018
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall validate all calibrated parameters against physically plausible bounds (qubit frequency 4-8 GHz, T1 1-500 us, T2 1-500 us, gate fidelity 0.90-1.00) before accepting them into the active parameter database. |
| **Rationale**    | Prevents calibration artifacts or measurement errors from corrupting the parameter database with physically implausible values. |
| **Source**       | CTL-005; stakeholder need (hardware calibration engineer) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RTO-01B, CMP-RTO-01D |
| **Status**       | Baselined |

### REQ-FUN-019
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall decode quantum error correction syndromes and compute correction operations with a round-trip latency (readout completion to correction pulse start) of not more than 1 us for surface codes up to distance d=7. |
| **Rationale**    | Error correction must complete within the qubit coherence time to suppress logical error rates. |
| **Source**       | Stakeholder need (quantum physicist); error correction performance specification |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RTO-01C |
| **Status**       | Baselined |

### REQ-FUN-020
| Field        | Value |
|--------------|-------|
| **Statement**    | The error correction decoder shall support minimum-weight perfect matching (MWPM) and union-find decoding algorithms, selectable at runtime without firmware or hardware changes. |
| **Rationale**    | Decoder algorithm research is active; runtime selectability enables performance comparison without system downtime. |
| **Source**       | Stakeholder need (quantum physicist) |
| **Parent**       | REQ-FUN-019 |
| **Verification** | Test |
| **Allocation**   | CMP-RTO-01C |
| **Status**       | Baselined |

### REQ-FUN-021
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall continuously monitor cryostat temperature at the 4 K and 20 mK stages and shall inhibit all RF output and flux bias output within 100 ms if the 20 mK stage temperature exceeds 100 mK. |
| **Rationale**    | Thermal excursion above 100 mK at the mixing chamber indicates a cryostat fault; qubit operations are meaningless and control signals could damage thermally stressed components. |
| **Source**       | HZ-004; CTL-006; stakeholder need (cryogenic engineer) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RTO-01D |
| **Status**       | Baselined |

### REQ-FUN-022
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall report subsystem health status (RPG channel status, CRE readout quality, FBC noise levels, TDU lock status) to the operator interface at a rate of not less than 1 Hz. |
| **Rationale**    | Continuous health monitoring enables operators to detect degradation before it impacts experiment quality. |
| **Source**       | Stakeholder need (quantum physicist) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RTO-01D |
| **Status**       | Baselined |

### REQ-FUN-023
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall execute power-up self-test on all subsystems within 60 seconds of power application and shall report any detected faults to the operator before the system transitions to MODE-001 or MODE-002. |
| **Rationale**    | Self-test detects latent faults before they affect qubit operations or compromise safety functions. |
| **Source**       | Stakeholder need (control electronics engineer); IEC 61508 diagnostic coverage |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RTO-01, CMP-RPG-01, CMP-CRE-01, CMP-FBC-01, CMP-TDU-01 |
| **Status**       | Baselined |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall enforce a maximum RF output power of -20 dBm at the cryostat input flange via a hardware power limiter that operates independently of all software, with a response time of not more than 10 us from limit exceedance to output suppression. |
| **Rationale**    | Hardware-enforced RF power limit prevents qubit damage regardless of software state. |
| **Source**       | HZ-001; CTL-002; IEC 61508 Part 2 Section 7.4 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RPG-01C, CMP-SAF-01B |
| **Status**       | Baselined |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall detect RF power limiter trip events and shall inhibit all RPG output channels within 100 ms of trip detection, requiring explicit operator acknowledgment before resuming RF output. |
| **Rationale**    | A limiter trip indicates a potentially unsafe condition that requires operator assessment before resuming operations. |
| **Source**       | HZ-001; CTL-002; IEC 61508 Part 1 Section 7 |
| **Parent**       | REQ-SAF-001 |
| **Verification** | Test |
| **Allocation**   | CMP-SAF-01A, CMP-RPG-01C |
| **Status**       | Baselined |

### REQ-SAF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall enforce a maximum flux bias current of 10 mA per channel via a hardware current limiter that operates independently of all software, with a response time of not more than 10 us from limit exceedance to current clamping. |
| **Rationale**    | Hardware-enforced current limit prevents Josephson junction damage regardless of software state. |
| **Source**       | HZ-002; CTL-003; IEC 61508 Part 2 Section 7.4 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-FBC-01B, CMP-SAF-01B |
| **Status**       | Baselined |

### REQ-SAF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall detect flux bias current limiter trip events and shall set all FBC channels to zero current within 100 ms of trip detection, requiring explicit operator acknowledgment before resuming flux bias output. |
| **Rationale**    | A current limiter trip indicates a potentially unsafe condition requiring operator review. |
| **Source**       | HZ-002; CTL-003; IEC 61508 Part 1 Section 7 |
| **Parent**       | REQ-SAF-003 |
| **Verification** | Test |
| **Allocation**   | CMP-SAF-01A, CMP-FBC-01B |
| **Status**       | Baselined |

### REQ-SAF-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The calibration automation software shall request Safety Monitor approval before setting any RF power or flux bias parameter that exceeds 80% of the hardware limit, and the Safety Monitor shall validate the requested parameter against the authorized calibration range before granting approval. |
| **Rationale**    | Software-enforced pre-check provides defense-in-depth before reaching the hardware safety limit. |
| **Source**       | HZ-003; CTL-005; IEC 61508 Part 3 Section 7.4 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RTO-01B, CMP-RTO-01D |
| **Status**       | Baselined |

### REQ-SAF-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The safety PLC shall execute a diagnostic self-test cycle at least once per second and shall transition the system to a safe state (all RF output inhibited, all flux bias set to zero) if the self-test detects any internal fault. |
| **Rationale**    | Continuous self-test ensures the safety function remains available; IEC 61508 SIL 2 requires diagnostic test interval commensurate with the dangerous failure rate. |
| **Source**       | HZ-005; CTL-008; IEC 61508 Part 2 Section 7.4.3 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-SAF-01A |
| **Status**       | Baselined |

### REQ-SAF-007
| Field        | Value |
|--------------|-------|
| **Statement**    | The safety interlock module shall achieve a probability of dangerous failure on demand (PFDavg) of not more than 1 x 10^-2, consistent with IEC 61508 SIL 2 for a low-demand safety function. |
| **Rationale**    | Quantitative safety target for the interlock function per IEC 61508 Table 2. |
| **Source**       | HZ-001; HZ-002; CTL-002; CTL-003; IEC 61508 Part 1 Table 2 |
| **Parent**       | — |
| **Verification** | Analysis |
| **Allocation**   | CMP-SAF-01A, CMP-SAF-01B |
| **Status**       | Baselined |

### REQ-SAF-008
| Field        | Value |
|--------------|-------|
| **Statement**    | The analog comparator trip circuits shall operate on independent analog sense points, with no shared sensing path with the control system measurements, and shall function correctly with the safety PLC in a faulted state. |
| **Rationale**    | Independence of the analog trip from both the control system and the digital safety PLC provides a third layer of defense. |
| **Source**       | HZ-005; CTL-009; IEC 61508 Part 2 Section 7.4.2.2 |
| **Parent**       | REQ-SAF-007 |
| **Verification** | Inspection, Analysis |
| **Allocation**   | CMP-SAF-01B |
| **Status**       | Baselined |

### REQ-SAF-009
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall transition to a safe state (MODE-003 equivalent: all RF inhibited, all flux bias zeroed) within 200 ms of detecting loss of communication with the safety PLC. |
| **Rationale**    | Communication loss with the safety system must be treated as a potentially unsafe condition. |
| **Source**       | HZ-005; CTL-008; IEC 61508 Part 2 Section 7.4.6 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RTO-01D, CMP-SAF-01A |
| **Status**       | Baselined |

### REQ-SAF-010
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall log all safety interlock trip events, calibration parameter changes, and safety limit modifications in a tamper-evident audit log with timestamps traceable to the system clock. |
| **Rationale**    | Audit trail supports post-incident investigation and demonstrates compliance with IEC 61508 management of functional safety. |
| **Source**       | IEC 61508 Part 1 Section 8 (management of functional safety) |
| **Parent**       | — |
| **Verification** | Inspection, Test |
| **Allocation**   | CMP-RTO-01D, CMP-SAF-01A |
| **Status**       | Baselined |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall accept compiled gate sequences from the quantum circuit compiler via IFC-EXT-001 in a defined binary format, with sequence uploads completing within 10 ms for circuits of up to 10,000 gates. |
| **Rationale**    | Fast sequence upload minimizes job pipeline latency. |
| **Source**       | Stakeholder need (quantum software developer) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RTO-01A |
| **Status**       | Baselined |

### REQ-IFC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The RTO shall transmit pulse waveform parameters to the RPG via IFC-INT-001 with a latency of not more than 1 ms from sequence dispatch to RPG memory load confirmation. |
| **Rationale**    | Waveform loading latency is part of the job startup overhead and affects throughput. |
| **Source**       | Stakeholder need (quantum physicist); system timing budget |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RTO-01A, CMP-RPG-01D |
| **Status**       | Baselined |

### REQ-IFC-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The CRE shall transmit syndrome measurement results to the RTO error correction decoder via IFC-INT-003 within 200 ns of state discrimination completion. |
| **Rationale**    | Syndrome data transport latency directly consumes the error correction latency budget. |
| **Source**       | REQ-FUN-019; system timing budget |
| **Parent**       | REQ-FUN-019 |
| **Verification** | Test |
| **Allocation**   | CMP-CRE-01A, CMP-RTO-01C |
| **Status**       | Baselined |

### REQ-IFC-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The safety interlock signals (IFC-INT-009, IFC-INT-010) shall be implemented as hardwired discrete signals with a propagation delay of not more than 10 us from trip detection to output suppression, with no software in the signal path. |
| **Rationale**    | Hardwired safety signals ensure interlock response time is independent of any software or firmware execution. |
| **Source**       | CTL-002; CTL-003; IEC 61508 Part 2 Section 7.4 |
| **Parent**       | — |
| **Verification** | Test, Inspection |
| **Allocation**   | CMP-SAF-01A, CMP-SAF-01B, CMP-RPG-01C, CMP-FBC-01B |
| **Status**       | Baselined |

### REQ-IFC-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall receive cryostat temperature data from the dilution refrigerator control system via IFC-EXT-003 at a rate of not less than 1 Hz, and shall detect loss of temperature data within 5 seconds. |
| **Rationale**    | Temperature monitoring supports cryogenic thermal excursion detection (HZ-004). |
| **Source**       | HZ-004; CTL-006; stakeholder need (cryogenic engineer) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RTO-01D |
| **Status**       | Baselined |

### REQ-IFC-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The TDU shall distribute clock and trigger signals to the RPG, CRE, and FBC via IFC-INT-005 through IFC-INT-008 with matched electrical lengths such that channel-to-channel skew does not exceed 100 ps. |
| **Rationale**    | Timing distribution accuracy is critical for multi-qubit gate operations. |
| **Source**       | REQ-FUN-014; system timing budget |
| **Parent**       | REQ-FUN-014 |
| **Verification** | Test |
| **Allocation**   | CMP-TDU-01A, CMP-TDU-01B, CMP-TDU-01C |
| **Status**       | Baselined |

### REQ-IFC-007
| Field        | Value |
|--------------|-------|
| **Statement**    | The error correction decoder shall transmit correction pulse commands to the RPG via IFC-INT-004 within 300 ns of decode completion, using a deterministic low-latency interface (PCIe direct or shared memory). |
| **Rationale**    | Correction pulse command transport latency is part of the 1 us error correction round-trip budget. |
| **Source**       | REQ-FUN-019; system timing budget |
| **Parent**       | REQ-FUN-019 |
| **Verification** | Test |
| **Allocation**   | CMP-RTO-01C, CMP-RPG-01D |
| **Status**       | Baselined |

## Performance Requirements

### REQ-PRF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall achieve a single-qubit gate fidelity contribution (control electronics error) of not more than 0.1%, such that the total single-qubit gate fidelity exceeds 99.9% when combined with the qubit coherence-limited fidelity. |
| **Rationale**    | Control electronics error must be a small fraction of the total gate error budget. |
| **Source**       | Stakeholder need (quantum physicist); system performance specification |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-RPG-01A, CMP-RPG-01B, CMP-TDU-01 |
| **Status**       | Baselined |

### REQ-PRF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall achieve a two-qubit gate fidelity contribution (control electronics error) of not more than 0.5%, such that the total two-qubit gate fidelity exceeds 99.5% when combined with the qubit coherence-limited fidelity. |
| **Rationale**    | Two-qubit gate fidelity is the primary bottleneck for quantum error correction threshold. |
| **Source**       | Stakeholder need (quantum physicist); system performance specification |
| **Parent**       | REQ-PRF-001 |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-RPG-01A, CMP-RPG-01B, CMP-FBC-01A, CMP-TDU-01 |
| **Status**       | Baselined |

### REQ-PRF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The TDU reference oscillator shall exhibit a phase noise of not more than -120 dBc/Hz at 10 kHz offset from the 10 GHz carrier, and the oscillator frequency stability shall be within 1 ppb over any 1-hour interval. |
| **Rationale**    | Phase noise and frequency stability directly limit achievable gate fidelity through timing jitter and frequency drift. |
| **Source**       | Stakeholder need (control electronics engineer); system timing budget |
| **Parent**       | REQ-FUN-014 |
| **Verification** | Test |
| **Allocation**   | CMP-TDU-01A |
| **Status**       | Baselined |

### REQ-PRF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The CRE 4 K FPGA shall dissipate not more than 10 mW total power, including all readout channels and communication interfaces. |
| **Rationale**    | Power dissipation at the 4 K stage is limited by cryocooler capacity; exceeding the thermal budget raises the base temperature and degrades qubit coherence. |
| **Source**       | Stakeholder need (cryogenic engineer); cryostat thermal budget |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-CRE-01A |
| **Status**       | Baselined |

### REQ-PRF-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall sustain a quantum circuit execution throughput of not less than 100,000 single-qubit gate layers per second in MODE-001, measured as the number of parallel gate layers executed across all qubits per unit time. |
| **Rationale**    | Execution throughput determines the practical speed of quantum algorithms and the value of the quantum computing platform. |
| **Source**       | Stakeholder need (quantum physicist); system performance specification |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RTO-01A, CMP-RPG-01D, CMP-TDU-01C |
| **Status**       | Baselined |

### REQ-PRF-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The RPG channel-to-channel crosstalk shall be not more than -60 dB between any two output channels measured at the cryostat input flange. |
| **Rationale**    | Crosstalk between control channels causes unintended qubit rotations, limiting gate fidelity. |
| **Source**       | Stakeholder need (control electronics engineer) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-RPG-01A, CMP-RPG-01B |
| **Status**       | Baselined |

### REQ-PRF-007
| Field        | Value |
|--------------|-------|
| **Statement**    | The QPCS shall complete a full 100-qubit calibration cycle (single-qubit characterization for all qubits plus two-qubit gate calibration for all coupled pairs) in not more than 8 hours. |
| **Rationale**    | Calibration must complete within a daily maintenance window to maximize processor availability. |
| **Source**       | Stakeholder need (hardware calibration engineer) |
| **Parent**       | REQ-FUN-016 |
| **Verification** | Test, Demonstration |
| **Allocation**   | CMP-RTO-01B |
| **Status**       | Baselined |
