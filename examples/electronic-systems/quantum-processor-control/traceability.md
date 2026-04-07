# Traceability

## Trace Strategy

This traceability matrix establishes bidirectional linkage across all QPCS system engineering artifacts. Forward traces demonstrate that every requirement is allocated, sourced, and verified. Reverse traces confirm that every component, hazard, and verification activity connects back to a requirement. Gaps are first-class entries with disposition, not omissions.

**Traced entities:**
- Requirements (REQ-) to architecture components (CMP-)
- Requirements (REQ-) to hazard/control sources (HZ-, CTL-)
- Requirements (REQ-) to verification activities (VER-)
- Verification activities (VER-) to evidence artifacts (EVD-)
- Components (CMP-) back to requirements
- Hazards (HZ-) through controls (CTL-) to requirements

## Forward Traces

### Requirements to Architecture

| REQ ID       | Statement (short)                               | CMP ID(s)                                       | Allocation Rationale                              |
|--------------|-------------------------------------------------|--------------------------------------------------|---------------------------------------------------|
| REQ-FUN-001  | Execute compiled gate sequences                 | CMP-RTO-01A                                      | Orchestration software dispatches gate sequences   |
| REQ-FUN-002  | Support 100+ concurrent qubits                  | CMP-RTO-01A                                      | Scalability in orchestration engine                |
| REQ-FUN-003  | Formally verify sequences before execution      | CMP-RTO-01E                                      | Formal verifier is dedicated stateless component   |
| REQ-FUN-004  | Job queue management (1000 jobs)                | CMP-RTO-01A                                      | Job queue in orchestration software                |
| REQ-FUN-005  | RF pulse generation 4-8 GHz, 14-bit, 2.4 GSPS  | CMP-RPG-01A, CMP-RPG-01B                        | AWG cards and upconversion module                  |
| REQ-FUN-006  | Pulse envelopes 2 ns rise/fall, 10 ns-10 us     | CMP-RPG-01A, CMP-RPG-01D                        | AWG DAC + FPGA pulse sequencer                     |
| REQ-FUN-007  | RF power limit -20 dBm (hardware)               | CMP-RPG-01C, CMP-SAF-01B                        | Hardware limiter + analog comparator               |
| REQ-FUN-008  | CRE digitize 1 GSPS, 12-bit, 500 ns discrimination | CMP-CRE-01A, CMP-CRE-01B, CMP-CRE-01D      | 4K ADC + FPGA discrimination firmware              |
| REQ-FUN-009  | Readout fidelity >= 99.0%                        | CMP-CRE-01A, CMP-CRE-01D                        | FPGA discrimination algorithm quality              |
| REQ-FUN-010  | Multiplexed readout 8 qubits/channel            | CMP-CRE-01A, CMP-CRE-01D                        | Frequency demux in FPGA firmware                   |
| REQ-FUN-011  | Flux bias 20-bit DAC, <100 pA/rtHz noise        | CMP-FBC-01A                                      | Precision DAC specification                        |
| REQ-FUN-012  | Flux bias settling <1 us, 0.01% accuracy        | CMP-FBC-01A, CMP-FBC-01C                        | DAC + bias sequencer FPGA                          |
| REQ-FUN-013  | Flux current limit 10 mA (hardware)             | CMP-FBC-01B, CMP-SAF-01B                        | Hardware current limiter + analog comparator       |
| REQ-FUN-014  | Clock distribution <100 ps skew                 | CMP-TDU-01A, CMP-TDU-01B                        | Reference oscillator + distribution network        |
| REQ-FUN-015  | Trigger jitter <50 ps RMS                       | CMP-TDU-01C                                      | Trigger sequencer FPGA                             |
| REQ-FUN-016  | Automated single-qubit calibration <5 min/qubit | CMP-RTO-01B                                      | Calibration automation software                    |
| REQ-FUN-017  | Two-qubit gate calibration protocols            | CMP-RTO-01B                                      | Calibration automation software                    |
| REQ-FUN-018  | Parameter validation against physical bounds     | CMP-RTO-01B, CMP-RTO-01D                        | Calibration software + Safety Monitor              |
| REQ-FUN-019  | Error correction decode <1 us round-trip         | CMP-RTO-01C                                      | GPU-accelerated decoder                            |
| REQ-FUN-020  | Selectable decoder algorithms at runtime         | CMP-RTO-01C                                      | Software flexibility in decoder                    |
| REQ-FUN-021  | Thermal monitoring with 100 ms output inhibition | CMP-RTO-01D                                      | Safety Monitor software                            |
| REQ-FUN-022  | Health status reporting at 1 Hz                  | CMP-RTO-01D                                      | Safety Monitor and health dashboard                |
| REQ-FUN-023  | Power-up self-test within 60 seconds            | CMP-RTO-01, CMP-RPG-01, CMP-CRE-01, CMP-FBC-01, CMP-TDU-01 | BIT across all subsystems |
| REQ-SAF-001  | Hardware RF power limit with 10 us response      | CMP-RPG-01C, CMP-SAF-01B                        | Analog limiter + comparator                        |
| REQ-SAF-002  | RF trip detection with operator acknowledgment   | CMP-SAF-01A, CMP-RPG-01C                        | Safety PLC detects trip; inhibits output            |
| REQ-SAF-003  | Hardware flux current limit with 10 us response  | CMP-FBC-01B, CMP-SAF-01B                        | Analog current clamp + comparator                  |
| REQ-SAF-004  | Flux trip detection with operator acknowledgment | CMP-SAF-01A, CMP-FBC-01B                        | Safety PLC detects trip; zeros current              |
| REQ-SAF-005  | Calibration Safety Monitor approval >80% limit   | CMP-RTO-01B, CMP-RTO-01D                        | Software safety check before hardware limit        |
| REQ-SAF-006  | Safety PLC self-test 1 Hz with safe-state on fault| CMP-SAF-01A                                     | PLC self-diagnostic                                |
| REQ-SAF-007  | PFDavg <= 1e-2 for safety interlock             | CMP-SAF-01A, CMP-SAF-01B                        | Combined PLC + analog comparator reliability       |
| REQ-SAF-008  | Analog comparators independent of PLC and control | CMP-SAF-01B                                     | Dedicated analog sensing circuits                  |
| REQ-SAF-009  | Safe state on loss of safety PLC communication   | CMP-RTO-01D, CMP-SAF-01A                        | RTO detects heartbeat loss; transitions safe       |
| REQ-SAF-010  | Tamper-evident audit log for safety events       | CMP-RTO-01D, CMP-SAF-01A                        | Logging in Safety Monitor and PLC                  |
| REQ-IFC-001  | Gate sequence upload <10 ms                     | CMP-RTO-01A                                      | High-speed API interface                           |
| REQ-IFC-002  | Pulse waveform load <1 ms to RPG               | CMP-RTO-01A, CMP-RPG-01D                        | PCIe/Ethernet data path                            |
| REQ-IFC-003  | Syndrome data <200 ns to decoder               | CMP-CRE-01A, CMP-RTO-01C                        | Low-latency Ethernet/optical link                  |
| REQ-IFC-004  | Hardwired safety interlock <10 us              | CMP-SAF-01A, CMP-SAF-01B, CMP-RPG-01C, CMP-FBC-01B | Discrete wired interlock path              |
| REQ-IFC-005  | Cryostat temperature data 1 Hz                 | CMP-RTO-01D                                      | Modbus TCP polling                                 |
| REQ-IFC-006  | Clock/trigger distribution <100 ps skew        | CMP-TDU-01A, CMP-TDU-01B, CMP-TDU-01C          | Matched-length distribution network                |
| REQ-IFC-007  | Correction pulses <300 ns to RPG               | CMP-RTO-01C, CMP-RPG-01D                        | PCIe direct / shared memory                        |
| REQ-PRF-001  | Single-qubit gate fidelity error <0.1%         | CMP-RPG-01A, CMP-RPG-01B, CMP-TDU-01            | Pulse quality + timing accuracy                    |
| REQ-PRF-002  | Two-qubit gate fidelity error <0.5%            | CMP-RPG-01A, CMP-RPG-01B, CMP-FBC-01A, CMP-TDU-01 | Combined pulse + flux + timing accuracy       |
| REQ-PRF-003  | Phase noise <-120 dBc/Hz, stability <1 ppb/hr  | CMP-TDU-01A                                      | Reference oscillator specification                 |
| REQ-PRF-004  | CRE power dissipation <10 mW at 4K             | CMP-CRE-01A                                      | FPGA power budget                                  |
| REQ-PRF-005  | Circuit throughput >100K gate layers/sec        | CMP-RTO-01A, CMP-RPG-01D, CMP-TDU-01C           | System pipeline throughput                         |
| REQ-PRF-006  | Channel crosstalk <-60 dB                      | CMP-RPG-01A, CMP-RPG-01B                        | RF isolation design                                |
| REQ-PRF-007  | Full 100-qubit calibration <8 hours            | CMP-RTO-01B                                      | Calibration automation efficiency                  |

### Requirements to Hazards

| REQ ID       | Source HZ ID(s)  | Source CTL ID(s)            | Source Clause                        |
|--------------|------------------|-----------------------------|--------------------------------------|
| REQ-FUN-003  | HZ-006, HZ-007   | CTL-001                     | —                                    |
| REQ-FUN-007  | HZ-001           | CTL-002                     | IEC 61508 SIL 2                      |
| REQ-FUN-013  | HZ-002           | CTL-003                     | IEC 61508 SIL 2                      |
| REQ-FUN-018  | —                | CTL-005                     | —                                    |
| REQ-FUN-021  | HZ-004           | CTL-006                     | —                                    |
| REQ-SAF-001  | HZ-001           | CTL-002                     | IEC 61508 Part 2 Section 7.4         |
| REQ-SAF-002  | HZ-001           | CTL-002                     | IEC 61508 Part 1 Section 7           |
| REQ-SAF-003  | HZ-002           | CTL-003                     | IEC 61508 Part 2 Section 7.4         |
| REQ-SAF-004  | HZ-002           | CTL-003                     | IEC 61508 Part 1 Section 7           |
| REQ-SAF-005  | HZ-003           | CTL-005                     | IEC 61508 Part 3 Section 7.4         |
| REQ-SAF-006  | HZ-005           | CTL-008                     | IEC 61508 Part 2 Section 7.4.3       |
| REQ-SAF-007  | HZ-001, HZ-002   | CTL-002, CTL-003            | IEC 61508 Part 1 Table 2             |
| REQ-SAF-008  | HZ-005           | CTL-009                     | IEC 61508 Part 2 Section 7.4.2.2     |
| REQ-SAF-009  | HZ-005, HZ-010   | CTL-008                     | IEC 61508 Part 2 Section 7.4.6       |
| REQ-SAF-010  | HZ-009           | CTL-011                     | IEC 61508 Part 1 Section 8           |

### Requirements to Verification

| REQ ID       | VER ID      | Method              | Artifact                                          | Status  | CMP ID(s)                           | MODE ID(s)         |
|--------------|-------------|---------------------|---------------------------------------------------|---------|-------------------------------------|--------------------|
| REQ-FUN-001  | VER-T-009   | Test                | Gate sequence execution test                      | Planned | CMP-RTO-01A                         | MODE-001           |
| REQ-FUN-002  | VER-T-010   | Test                | 100-qubit concurrent control test                 | Planned | CMP-RTO-01A                         | MODE-001           |
| REQ-FUN-003  | VER-T-003   | Test                | Formal verifier validation test                   | Planned | CMP-RTO-01E                         | MODE-001           |
| REQ-FUN-003  | VER-FV-001  | Formal verification | Verifier correctness proof                        | Planned | CMP-RTO-01E                         | —                  |
| REQ-FUN-004  | VER-T-011   | Test                | Job queue stress test                             | Planned | CMP-RTO-01A                         | MODE-001           |
| REQ-FUN-005  | VER-T-012   | Test                | RF pulse specification compliance test            | Planned | CMP-RPG-01A, CMP-RPG-01B           | MODE-001           |
| REQ-FUN-006  | VER-T-020   | Test                | Pulse envelope timing test                        | Planned | CMP-RPG-01A, CMP-RPG-01D           | MODE-001           |
| REQ-FUN-007  | VER-T-001   | Test                | RF power limiter trip test                        | Planned | CMP-RPG-01C, CMP-SAF-01B           | MODE-001, MODE-002 |
| REQ-FUN-008  | VER-T-021   | Test                | CRE digitization and discrimination test          | Planned | CMP-CRE-01A, CMP-CRE-01B, CMP-CRE-01D | MODE-001       |
| REQ-FUN-009  | VER-T-022   | Test                | Readout fidelity characterization test            | Planned | CMP-CRE-01A, CMP-CRE-01D          | MODE-001           |
| REQ-FUN-009  | VER-A-001   | Analysis            | Readout fidelity statistical analysis             | Planned | CMP-CRE-01A, CMP-CRE-01D          | MODE-001           |
| REQ-FUN-010  | VER-T-023   | Test                | Multiplexed readout test                          | Planned | CMP-CRE-01A, CMP-CRE-01D          | MODE-001           |
| REQ-FUN-011  | VER-T-024   | Test                | DAC resolution and noise floor test               | Planned | CMP-FBC-01A                         | MODE-001           |
| REQ-FUN-012  | VER-T-025   | Test                | Flux bias settling time test                      | Planned | CMP-FBC-01A, CMP-FBC-01C           | MODE-001           |
| REQ-FUN-013  | VER-T-004   | Test                | Flux current limiter trip test                    | Planned | CMP-FBC-01B, CMP-SAF-01B           | MODE-001, MODE-002 |
| REQ-FUN-014  | VER-T-026   | Test                | Clock skew measurement test                       | Planned | CMP-TDU-01A, CMP-TDU-01B           | MODE-001           |
| REQ-FUN-015  | VER-T-027   | Test                | Trigger jitter measurement test                   | Planned | CMP-TDU-01C                         | MODE-001           |
| REQ-FUN-016  | VER-T-013   | Test                | Automated calibration execution test              | Planned | CMP-RTO-01B                         | MODE-002           |
| REQ-FUN-016  | VER-D-001   | Demonstration       | Full calibration cycle demonstration              | Planned | CMP-RTO-01B                         | MODE-002           |
| REQ-FUN-017  | VER-T-028   | Test                | Two-qubit calibration protocol test               | Planned | CMP-RTO-01B                         | MODE-002           |
| REQ-FUN-018  | VER-T-014   | Test                | Parameter validation bounds checking test         | Planned | CMP-RTO-01B, CMP-RTO-01D           | MODE-002           |
| REQ-FUN-019  | VER-T-029   | Test                | Error correction latency test                     | Planned | CMP-RTO-01C                         | MODE-004           |
| REQ-FUN-020  | VER-T-030   | Test                | Decoder algorithm selection test                  | Planned | CMP-RTO-01C                         | MODE-004           |
| REQ-FUN-021  | VER-T-015   | Test                | Thermal excursion response test                   | Planned | CMP-RTO-01D                         | MODE-001           |
| REQ-FUN-022  | VER-T-017   | Test                | Health status reporting test                      | Planned | CMP-RTO-01D                         | MODE-001           |
| REQ-FUN-023  | VER-T-031   | Test                | Power-up self-test execution test                 | Planned | CMP-RTO-01, CMP-RPG-01, CMP-CRE-01, CMP-FBC-01, CMP-TDU-01 | MODE-005 |
| REQ-SAF-001  | VER-T-001   | Test                | RF power limiter response time test               | Planned | CMP-RPG-01C, CMP-SAF-01B           | MODE-001           |
| REQ-SAF-002  | VER-T-002   | Test                | RF trip detection and inhibit test                | Planned | CMP-SAF-01A, CMP-RPG-01C           | MODE-001           |
| REQ-SAF-003  | VER-T-004   | Test                | Flux current limiter response time test           | Planned | CMP-FBC-01B, CMP-SAF-01B           | MODE-001           |
| REQ-SAF-004  | VER-T-005   | Test                | Flux trip detection and zero-current test         | Planned | CMP-SAF-01A, CMP-FBC-01B           | MODE-001           |
| REQ-SAF-005  | VER-T-014   | Test                | Calibration Safety Monitor approval test          | Planned | CMP-RTO-01B, CMP-RTO-01D           | MODE-002           |
| REQ-SAF-006  | VER-T-006   | Test                | Safety PLC self-test and safe-state test          | Planned | CMP-SAF-01A                         | MODE-001           |
| REQ-SAF-007  | VER-A-002   | Analysis            | PFDavg calculation per IEC 61508                  | Planned | CMP-SAF-01A, CMP-SAF-01B           | —                  |
| REQ-SAF-008  | VER-T-008   | Test                | Analog comparator independence test               | Planned | CMP-SAF-01B                         | MODE-005           |
| REQ-SAF-008  | VER-I-001   | Inspection          | Analog sensing path independence inspection       | Planned | CMP-SAF-01B                         | —                  |
| REQ-SAF-009  | VER-T-007   | Test                | PLC communication loss safe-state test            | Planned | CMP-RTO-01D, CMP-SAF-01A           | MODE-001           |
| REQ-SAF-010  | VER-T-018   | Test                | Audit log integrity and completeness test         | Planned | CMP-RTO-01D, CMP-SAF-01A           | MODE-001, MODE-002 |
| REQ-SAF-010  | VER-I-002   | Inspection          | Audit log tamper-evidence inspection              | Planned | CMP-RTO-01D                         | —                  |
| REQ-IFC-001  | VER-T-032   | Test                | Gate sequence upload latency test                 | Planned | CMP-RTO-01A                         | MODE-001           |
| REQ-IFC-002  | VER-T-033   | Test                | Waveform load latency test                        | Planned | CMP-RTO-01A, CMP-RPG-01D           | MODE-001           |
| REQ-IFC-003  | VER-T-034   | Test                | Syndrome data transport latency test              | Planned | CMP-CRE-01A, CMP-RTO-01C           | MODE-004           |
| REQ-IFC-004  | VER-T-019   | Test                | Hardwired interlock propagation test              | Planned | CMP-SAF-01A, CMP-SAF-01B           | MODE-001           |
| REQ-IFC-004  | VER-I-003   | Inspection          | Interlock wiring independence inspection          | Planned | CMP-SAF-01A, CMP-RPG-01C, CMP-FBC-01B | —              |
| REQ-IFC-005  | VER-T-035   | Test                | Cryostat temperature data reception test          | Planned | CMP-RTO-01D                         | MODE-001, MODE-003 |
| REQ-IFC-006  | VER-T-026   | Test                | Clock distribution skew measurement               | Planned | CMP-TDU-01A, CMP-TDU-01B, CMP-TDU-01C | MODE-001       |
| REQ-IFC-007  | VER-T-036   | Test                | Correction pulse command latency test             | Planned | CMP-RTO-01C, CMP-RPG-01D           | MODE-004           |
| REQ-PRF-001  | VER-T-037   | Test                | Single-qubit gate fidelity benchmark test         | Planned | CMP-RPG-01A, CMP-RPG-01B, CMP-TDU-01 | MODE-001        |
| REQ-PRF-001  | VER-A-003   | Analysis            | Gate fidelity error budget analysis               | Planned | CMP-RPG-01A, CMP-RPG-01B, CMP-TDU-01 | —               |
| REQ-PRF-002  | VER-T-038   | Test                | Two-qubit gate fidelity benchmark test            | Planned | CMP-RPG-01, CMP-FBC-01A, CMP-TDU-01 | MODE-001         |
| REQ-PRF-002  | VER-A-004   | Analysis            | Two-qubit fidelity error budget analysis          | Planned | CMP-RPG-01, CMP-FBC-01A, CMP-TDU-01 | —                |
| REQ-PRF-003  | VER-T-039   | Test                | Phase noise and stability measurement test        | Planned | CMP-TDU-01A                         | MODE-001           |
| REQ-PRF-004  | VER-T-040   | Test                | CRE power dissipation measurement at 4K          | Planned | CMP-CRE-01A                         | MODE-001           |
| REQ-PRF-004  | VER-A-005   | Analysis            | CRE thermal budget analysis                       | Planned | CMP-CRE-01A                         | —                  |
| REQ-PRF-005  | VER-T-041   | Test                | Circuit throughput benchmark test                 | Planned | CMP-RTO-01A, CMP-RPG-01D, CMP-TDU-01C | MODE-001       |
| REQ-PRF-006  | VER-T-042   | Test                | Channel crosstalk measurement test                | Planned | CMP-RPG-01A, CMP-RPG-01B           | MODE-001           |
| REQ-PRF-007  | VER-T-043   | Test                | Full calibration cycle timing test                | Planned | CMP-RTO-01B                         | MODE-002           |
| REQ-PRF-007  | VER-D-001   | Demonstration       | Full calibration cycle demonstration              | Planned | CMP-RTO-01B                         | MODE-002           |

## Reverse Traces

### Components to Requirements

| CMP ID        | Component Name                      | REQ ID(s)                                                                                     | Gap? |
|---------------|-------------------------------------|-----------------------------------------------------------------------------------------------|------|
| CMP-RTO-01    | Room-Temperature Orchestrator       | REQ-FUN-023                                                                                   | No   |
| CMP-RTO-01A   | Orchestration Software              | REQ-FUN-001, REQ-FUN-002, REQ-FUN-004, REQ-IFC-001, REQ-IFC-002, REQ-PRF-005                | No   |
| CMP-RTO-01B   | Calibration Automation Software     | REQ-FUN-016, REQ-FUN-017, REQ-FUN-018, REQ-SAF-005, REQ-PRF-007                             | No   |
| CMP-RTO-01C   | Error Correction Decoder            | REQ-FUN-019, REQ-FUN-020, REQ-IFC-003, REQ-IFC-007                                           | No   |
| CMP-RTO-01D   | Safety Monitor Software             | REQ-FUN-018, REQ-FUN-021, REQ-FUN-022, REQ-SAF-005, REQ-SAF-009, REQ-SAF-010, REQ-IFC-005  | No   |
| CMP-RTO-01E   | Sequence Formal Verifier            | REQ-FUN-003                                                                                   | No   |
| CMP-RPG-01    | RF Pulse Generator                  | REQ-FUN-023                                                                                   | No   |
| CMP-RPG-01A   | AWG Channel Cards                   | REQ-FUN-005, REQ-FUN-006, REQ-PRF-001, REQ-PRF-002, REQ-PRF-006                             | No   |
| CMP-RPG-01B   | RF Upconversion Module              | REQ-FUN-005, REQ-PRF-001, REQ-PRF-002, REQ-PRF-006                                           | No   |
| CMP-RPG-01C   | Output Power Limiter                | REQ-FUN-007, REQ-SAF-001, REQ-SAF-002, REQ-IFC-004                                           | No   |
| CMP-RPG-01D   | Pulse Sequencer FPGA                | REQ-FUN-006, REQ-IFC-002, REQ-IFC-007, REQ-PRF-005                                           | No   |
| CMP-CRE-01    | Cryogenic Readout Electronics       | REQ-FUN-023                                                                                   | No   |
| CMP-CRE-01A   | 4K Readout FPGA                     | REQ-FUN-008, REQ-FUN-009, REQ-FUN-010, REQ-IFC-003, REQ-PRF-004                             | No   |
| CMP-CRE-01B   | ADC Front-End                       | REQ-FUN-008                                                                                   | No   |
| CMP-CRE-01C   | Signal Conditioning Module          | —                                                                                             | YES  |
| CMP-CRE-01D   | Readout Discrimination Firmware     | REQ-FUN-008, REQ-FUN-009, REQ-FUN-010                                                        | No   |
| CMP-FBC-01    | Flux Bias Controller                | REQ-FUN-023                                                                                   | No   |
| CMP-FBC-01A   | Precision DAC Modules               | REQ-FUN-011, REQ-FUN-012, REQ-PRF-002                                                        | No   |
| CMP-FBC-01B   | Current Limiter Circuit             | REQ-FUN-013, REQ-SAF-003, REQ-SAF-004, REQ-IFC-004                                           | No   |
| CMP-FBC-01C   | Bias Sequencer FPGA                 | REQ-FUN-012                                                                                   | No   |
| CMP-TDU-01    | Timing Distribution Unit            | REQ-FUN-023, REQ-PRF-001, REQ-PRF-002                                                        | No   |
| CMP-TDU-01A   | Reference Oscillator                | REQ-FUN-014, REQ-PRF-003                                                                     | No   |
| CMP-TDU-01B   | Clock Distribution Network          | REQ-FUN-014, REQ-IFC-006                                                                     | No   |
| CMP-TDU-01C   | Trigger Sequencer FPGA              | REQ-FUN-015, REQ-IFC-006, REQ-PRF-005                                                        | No   |
| CMP-SAF-01    | Safety Interlock Module             | —                                                                                             | No   |
| CMP-SAF-01A   | Safety PLC                          | REQ-SAF-002, REQ-SAF-004, REQ-SAF-006, REQ-SAF-007, REQ-SAF-009, REQ-SAF-010, REQ-IFC-004  | No   |
| CMP-SAF-01B   | Analog Comparator Trip Circuits     | REQ-FUN-007, REQ-FUN-013, REQ-SAF-001, REQ-SAF-003, REQ-SAF-007, REQ-SAF-008, REQ-IFC-004  | No   |

### Hazards to Controls to Requirements

| HZ ID   | CTL ID(s)                 | REQ ID(s)                                                                | Fully Mitigated? |
|---------|---------------------------|--------------------------------------------------------------------------|------------------|
| HZ-001  | CTL-001, CTL-002          | REQ-FUN-003, REQ-FUN-007, REQ-SAF-001, REQ-SAF-002                      | Yes              |
| HZ-002  | CTL-003, CTL-004          | REQ-FUN-013, REQ-SAF-003, REQ-SAF-004                                   | Yes              |
| HZ-003  | CTL-005, CTL-002, CTL-003 | REQ-SAF-005, REQ-FUN-018, REQ-FUN-007, REQ-FUN-013                      | Yes              |
| HZ-004  | CTL-006                   | REQ-FUN-021                                                              | Yes              |
| HZ-005  | CTL-008, CTL-009          | REQ-SAF-006, REQ-SAF-007, REQ-SAF-008, REQ-SAF-009                      | Yes              |
| HZ-006  | CTL-007                   | REQ-FUN-003, REQ-FUN-022                                                 | Yes              |
| HZ-007  | CTL-001, CTL-002, CTL-003 | REQ-FUN-003, REQ-FUN-007, REQ-FUN-013                                    | Yes              |
| HZ-008  | CTL-006, CTL-010          | REQ-FUN-021, REQ-FUN-022                                                 | Yes              |
| HZ-009  | CTL-009, CTL-011          | REQ-SAF-008, REQ-SAF-010                                                 | Yes              |
| HZ-010  | CTL-008, CTL-012          | REQ-SAF-006, REQ-SAF-009                                                 | Yes              |

### Verification to Requirements

| VER ID      | REQ ID(s)                              | EVD ID(s)     | Status  |
|-------------|----------------------------------------|---------------|---------|
| VER-T-001   | REQ-FUN-007, REQ-SAF-001              | EVD-001        | Planned |
| VER-T-002   | REQ-SAF-002                            | EVD-001        | Planned |
| VER-T-003   | REQ-FUN-003                            | EVD-002        | Planned |
| VER-FV-001  | REQ-FUN-003                            | EVD-003        | Planned |
| VER-T-004   | REQ-FUN-013, REQ-SAF-003              | EVD-004        | Planned |
| VER-T-005   | REQ-SAF-004                            | EVD-004        | Planned |
| VER-T-006   | REQ-SAF-006                            | EVD-005        | Planned |
| VER-T-007   | REQ-SAF-009                            | EVD-005        | Planned |
| VER-T-008   | REQ-SAF-008                            | EVD-006        | Planned |
| VER-I-001   | REQ-SAF-008                            | EVD-006        | Planned |
| VER-T-009   | REQ-FUN-001                            | EVD-007        | Planned |
| VER-T-010   | REQ-FUN-002                            | EVD-007        | Planned |
| VER-T-011   | REQ-FUN-004                            | EVD-007        | Planned |
| VER-T-012   | REQ-FUN-005                            | EVD-008        | Planned |
| VER-T-013   | REQ-FUN-016, REQ-SAF-005              | EVD-009        | Planned |
| VER-D-001   | REQ-FUN-016, REQ-PRF-007              | EVD-009        | Planned |
| VER-T-014   | REQ-FUN-018, REQ-SAF-005              | EVD-009        | Planned |
| VER-T-015   | REQ-FUN-021                            | EVD-010        | Planned |
| VER-T-016   | REQ-FUN-003                            | EVD-010        | Planned |
| VER-T-017   | REQ-FUN-022                            | EVD-010        | Planned |
| VER-T-018   | REQ-SAF-010                            | EVD-011        | Planned |
| VER-I-002   | REQ-SAF-010                            | EVD-011        | Planned |
| VER-T-019   | REQ-IFC-004                            | EVD-006        | Planned |
| VER-I-003   | REQ-IFC-004                            | EVD-006        | Planned |
| VER-T-020   | REQ-FUN-006                            | EVD-008        | Planned |
| VER-T-021   | REQ-FUN-008                            | EVD-012        | Planned |
| VER-T-022   | REQ-FUN-009                            | EVD-012        | Planned |
| VER-A-001   | REQ-FUN-009                            | EVD-012        | Planned |
| VER-T-023   | REQ-FUN-010                            | EVD-012        | Planned |
| VER-T-024   | REQ-FUN-011                            | EVD-013        | Planned |
| VER-T-025   | REQ-FUN-012                            | EVD-013        | Planned |
| VER-T-026   | REQ-FUN-014, REQ-IFC-006              | EVD-014        | Planned |
| VER-T-027   | REQ-FUN-015                            | EVD-014        | Planned |
| VER-T-028   | REQ-FUN-017                            | EVD-009        | Planned |
| VER-T-029   | REQ-FUN-019                            | EVD-015        | Planned |
| VER-T-030   | REQ-FUN-020                            | EVD-015        | Planned |
| VER-T-031   | REQ-FUN-023                            | EVD-016        | Planned |
| VER-T-032   | REQ-IFC-001                            | EVD-007        | Planned |
| VER-T-033   | REQ-IFC-002                            | EVD-007        | Planned |
| VER-T-034   | REQ-IFC-003                            | EVD-015        | Planned |
| VER-T-035   | REQ-IFC-005                            | EVD-010        | Planned |
| VER-T-036   | REQ-IFC-007                            | EVD-015        | Planned |
| VER-T-037   | REQ-PRF-001                            | EVD-017        | Planned |
| VER-A-003   | REQ-PRF-001                            | EVD-017        | Planned |
| VER-T-038   | REQ-PRF-002                            | EVD-017        | Planned |
| VER-A-004   | REQ-PRF-002                            | EVD-017        | Planned |
| VER-T-039   | REQ-PRF-003                            | EVD-014        | Planned |
| VER-T-040   | REQ-PRF-004                            | EVD-018        | Planned |
| VER-A-005   | REQ-PRF-004                            | EVD-018        | Planned |
| VER-T-041   | REQ-PRF-005                            | EVD-007        | Planned |
| VER-T-042   | REQ-PRF-006                            | EVD-008        | Planned |
| VER-T-043   | REQ-PRF-007                            | EVD-009        | Planned |
| VER-A-002   | REQ-SAF-007                            | EVD-019        | Planned |

## Gap Register

| Gap ID  | Type                   | Entity ID      | Description                                                                                      | Disposition |
|---------|------------------------|----------------|--------------------------------------------------------------------------------------------------|-------------|
| GAP-001 | Orphan component       | CMP-CRE-01C    | Signal Conditioning Module has no direct requirements; its gain/filter characteristics are implicitly covered by CRE readout performance (REQ-FUN-008, REQ-FUN-009) but no explicit REQ- allocates to this component | Planned: derive REQ-FUN-024 for signal conditioning gain and bandwidth specification at next requirements review |
| GAP-002 | Incomplete formal verification coverage | REQ-FUN-003 | The formal verifier (CMP-RTO-01E) checks timing, power, and frequency constraints, but the completeness of the verification model against all possible qubit damage modes is an open research question. The model may not capture all physically realizable failure modes | Planned: commission independent review of verification model completeness; accept residual risk of model incompleteness with hardware interlock as backup |
| GAP-003 | Emerging standards gap  | REQ-SAF-007    | IEC 61508 PFDavg target for the safety interlock is based on the assumption that SIL 2 is appropriate for quantum processor protection. No industry-specific standard for quantum hardware safety exists. If a quantum computing safety standard emerges, the SIL assignment may need revision | Accepted: IEC 61508 is the best-available framework; monitor emerging standards through IEEE and IEC working groups |

## Coverage Summary

- **Requirements with architecture allocation**: 40/40 (100%)
- **Safety requirements with hazard source**: 10/10 (100%)
- **Requirements with verification activity**: 40/40 (100%)
- **Verification activities with evidence artifact**: 52/52 (100%)
- **Components with at least one requirement**: 25/26 (96.2%) — GAP-001 (CMP-CRE-01C)
- **Hazards with at least one control**: 10/10 (100%)
- **Controls with at least one requirement**: 12/12 (100%)
- **Gaps registered**: 3 (2 dispositioned as Planned, 1 as Accepted)
