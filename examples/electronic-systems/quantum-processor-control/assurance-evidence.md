# Assurance Evidence

## Assurance Framework

The Quantum Processor Control System follows the IEC 61508 functional safety lifecycle for the safety-critical calibration and interlock subsystems (SIL 2), supplemented by formal verification of control sequences and EDA tool qualification for the cryogenic FPGA design. The assurance framework adapts IEC 61508 to the emerging quantum computing domain where no industry-specific safety standard exists.

The evidence package supports review by the safety officer (internal), independent functional safety assessor (external per IEC 61508 Part 1 Section 8), and the control electronics design review board.

**Review Progression:**

| Phase     | Gate Name              | Purpose                                                                       | Key Evidence                                                               |
|-----------|------------------------|-------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Phase 1   | Concept & Scope        | System definition, hazard identification, SIL determination                   | Hazard & risk analysis, SIL determination report, safety requirements spec |
| Phase 2   | Design & Development   | Architecture, allocation, safety function design, FMEA/FMECA                  | Safety function specification, FMEA, architecture description, design verification plan |
| Phase 3   | Integration & Validation | Hardware/software integration, safety function testing, formal verification coverage | Test reports, formal verification reports, PFD calculations, safety case   |
| Phase 4   | Operation & Maintenance | Safety function monitoring, periodic proof testing, modification management   | Operation & maintenance manual, proof test procedures, modification log    |

## Evidence Lifecycle States

| State     | Meaning                                                    |
|-----------|------------------------------------------------------------|
| Planned   | Artifact identified, not yet started                       |
| Drafted   | Initial content exists, under development                  |
| Reviewed  | Peer or independent review completed                       |
| Approved  | Authority or designated reviewer accepted                  |
| Baselined | Under configuration control in the project CM system       |

## Evidence Index

| EVD ID   | Artifact Name                                          | Location                                                | Demonstrates                                                   | Standard Clause                  | Review Milestone | Evidence Consumer              | Status   |
|----------|--------------------------------------------------------|---------------------------------------------------------|----------------------------------------------------------------|----------------------------------|------------------|--------------------------------|----------|
| EVD-001  | RF Power Limiter Test Report                           | evidence/test-reports/rf-power-limiter-test.pdf          | Hardware limiter trips at -20 dBm; response time <10 us; trip detection and operator acknowledgment | IEC 61508 Part 2 Section 7.4  | Phase 3          | Safety officer, IFS assessor   | Planned  |
| EVD-002  | Formal Verifier Validation Test Report                 | evidence/test-reports/formal-verifier-validation.pdf     | Sequence verification catches timing, power, and frequency violations | IEC 61508 Part 3 Section 7.4  | Phase 3          | Control electronics review board | Planned |
| EVD-003  | Formal Verification Coverage Report                    | evidence/formal-verification/verifier-coverage.pdf       | Model-checked properties cover all hazard-relevant constraints; counterexample analysis | IEC 61508 Part 7 Table A.1    | Phase 3          | Safety officer, IFS assessor   | Planned  |
| EVD-004  | Flux Bias Current Limiter Test Report                  | evidence/test-reports/flux-current-limiter-test.pdf      | Hardware current clamp at 10 mA; response time <10 us; trip detection | IEC 61508 Part 2 Section 7.4  | Phase 3          | Safety officer, IFS assessor   | Planned  |
| EVD-005  | Safety PLC Diagnostic Test Report                      | evidence/test-reports/safety-plc-diagnostic-test.pdf     | Self-test cycle at 1 Hz; fault injection response; safe-state transition on PLC fault and communication loss | IEC 61508 Part 2 Section 7.4.3 | Phase 3       | Safety officer, IFS assessor   | Planned  |
| EVD-006  | Analog Comparator Independence Evidence                | evidence/analysis/analog-comparator-independence.pdf     | Comparator circuits use independent sense points; function with PLC faulted; hardwired interlock propagation | IEC 61508 Part 2 Section 7.4.2.2 | Phase 3     | Safety officer, IFS assessor   | Planned  |
| EVD-007  | System Integration Test Report                         | evidence/test-reports/system-integration-test.pdf        | Gate sequence execution, 100-qubit concurrent control, job queue, waveform load, circuit throughput | System specification           | Phase 3          | Control electronics review board | Planned |
| EVD-008  | RF Pulse Generator Characterization Report             | evidence/test-reports/rpg-characterization.pdf           | Pulse specification compliance (frequency, resolution, rise/fall time), envelope timing, channel crosstalk | System specification           | Phase 3          | Control electronics review board | Planned |
| EVD-009  | Calibration Subsystem Validation Report                | evidence/test-reports/calibration-validation.pdf         | Automated calibration execution, parameter validation, Safety Monitor approval, two-qubit protocols, full cycle timing | IEC 61508 Part 3 Section 7.9 | Phase 3       | Safety officer, IFS assessor   | Planned  |
| EVD-010  | System Health Monitoring Test Report                   | evidence/test-reports/health-monitoring-test.pdf         | Thermal excursion response, TDU lock monitoring, health status reporting, temperature data reception | IEC 61508 Part 2 Section 7.4  | Phase 3          | Safety officer                 | Planned  |
| EVD-011  | Safety Audit Log Integrity Report                      | evidence/test-reports/audit-log-integrity.pdf            | Tamper-evident logging of safety events; role-based access control; completeness verification | IEC 61508 Part 1 Section 8    | Phase 3          | Safety officer, IFS assessor   | Planned  |
| EVD-012  | Cryogenic Readout Electronics Test Report              | evidence/test-reports/cre-test.pdf                       | Digitization performance, state discrimination fidelity, multiplexed readout, latency | System specification           | Phase 3          | Control electronics review board | Planned |
| EVD-013  | Flux Bias Controller Characterization Report           | evidence/test-reports/fbc-characterization.pdf           | DAC resolution, noise floor, settling time, current accuracy | System specification              | Phase 3          | Control electronics review board | Planned |
| EVD-014  | Timing Distribution Performance Report                 | evidence/test-reports/tdu-performance.pdf                | Clock skew, trigger jitter, phase noise, frequency stability | System specification              | Phase 3          | Control electronics review board | Planned |
| EVD-015  | Error Correction Decoder Test Report                   | evidence/test-reports/ec-decoder-test.pdf                | Decode latency, syndrome transport, correction pulse latency, algorithm selection, throughput | System specification           | Phase 3          | Control electronics review board | Planned |
| EVD-016  | Power-Up Self-Test Report                              | evidence/test-reports/power-up-self-test.pdf             | BIT execution within 60 seconds; fault detection and reporting across all subsystems | IEC 61508 diagnostic coverage | Phase 3          | Control electronics review board | Planned |
| EVD-017  | Gate Fidelity Benchmark Report                         | evidence/test-reports/gate-fidelity-benchmark.pdf        | Single-qubit and two-qubit gate fidelity; control electronics error contribution | System specification           | Phase 3          | Control electronics review board | Planned |
| EVD-018  | CRE Thermal Budget Analysis and Test Report            | evidence/analysis/cre-thermal-budget.pdf                 | 4K FPGA power dissipation within 10 mW budget; thermal impact on cryostat | System specification; cryostat thermal model | Phase 2 | Cryogenic engineer, review board | Planned |
| EVD-019  | PFDavg Calculation Report                              | evidence/analysis/pfdavg-calculation.pdf                 | Safety interlock PFDavg <= 1e-2 per IEC 61508; fault tree for SIF | IEC 61508 Part 6 Section 7    | Phase 3          | Safety officer, IFS assessor   | Planned  |
| EVD-020  | Hazard & Risk Analysis Report                          | evidence/safety/hazard-risk-analysis.pdf                 | All hazards identified, risk controls defined, SIL determination justified | IEC 61508 Part 1 Section 7.4  | Phase 1          | Safety officer, IFS assessor   | Drafted  |
| EVD-021  | Safety Requirements Specification                      | evidence/safety/safety-requirements-spec.pdf             | SIL 2 safety requirements derived from hazard analysis; allocated to components | IEC 61508 Part 1 Section 7.10 | Phase 1          | Safety officer                 | Drafted  |
| EVD-022  | System Architecture Description                        | evidence/design/architecture-description.pdf             | Component hierarchy, allocation, interfaces, partitioning, independence arguments | IEC 61508 Part 2 Section 7.2  | Phase 2          | Review board                   | Drafted  |
| EVD-023  | FMEA/FMECA Report                                      | evidence/safety/fmea-fmeca-report.pdf                    | Component-level failure modes, detection coverage, criticality analysis | IEC 60812; IEC 61508 Part 2   | Phase 2          | Safety officer, IFS assessor   | Drafted  |
| EVD-024  | Safety Function Design Specification                   | evidence/design/safety-function-design.pdf               | Safety PLC logic, analog comparator design, interlock architecture, safe states | IEC 61508 Part 2 Section 7.4  | Phase 2          | Safety officer, IFS assessor   | Drafted  |
| EVD-025  | Functional Safety Management Plan                      | evidence/plans/fs-management-plan.pdf                    | Functional safety lifecycle planning, organization, competence, review schedule | IEC 61508 Part 1 Section 6    | Phase 1          | IFS assessor                   | Drafted  |
| EVD-026  | Verification and Validation Plan                       | evidence/plans/v-and-v-plan.pdf                          | Test strategy, formal verification strategy, inspection plan, acceptance criteria | IEC 61508 Part 2 Section 7.7  | Phase 1          | Safety officer, review board   | Drafted  |
| EVD-027  | Configuration Management Plan                          | evidence/plans/cm-plan.pdf                               | Identification, baseline control, change management for safety-related items | IEC 61508 Part 1 Section 6.2  | Phase 1          | Review board                   | Drafted  |
| EVD-028  | CRE FPGA Design Verification Report                    | evidence/test-reports/cre-fpga-verification.pdf          | FPGA functional verification, coverage metrics, timing closure, formal property verification | IEEE 1076; IEEE 1800          | Phase 3          | Control electronics review board | Planned |
| EVD-029  | Independent Functional Safety Assessment Report        | evidence/safety/ifs-assessment-report.pdf                | Independent assessment per IEC 61508 Part 1 Table 5 for SIL 2 | IEC 61508 Part 1 Section 8.2  | Phase 3          | IFS assessor (external)        | Planned  |
| EVD-030  | Safety Case Report                                     | evidence/safety/safety-case-report.pdf                   | Structured argument that all safety requirements are met; residual risk acceptable | IEC 61508 Part 1 Section 7.1  | Phase 3          | Safety officer, IFS assessor   | Planned  |

## IEC 61508 SIL Evidence Mapping

This section maps IEC 61508 lifecycle activities to evidence artifacts for the SIL 2 safety instrumented functions.

### Part 1: General Requirements

| Clause   | Activity                                                | Evidence                                           | EVD ID(s)     | Status   |
|----------|---------------------------------------------------------|----------------------------------------------------|---------------|----------|
| Section 6 | Functional safety management                           | Functional Safety Management Plan                  | EVD-025       | Drafted  |
| Section 7.4 | Hazard and risk analysis                             | Hazard & Risk Analysis Report                      | EVD-020       | Drafted  |
| Section 7.10 | Safety requirements specification                    | Safety Requirements Specification                  | EVD-021       | Drafted  |
| Section 7.15 | Safety validation                                    | Safety Case Report                                 | EVD-030       | Planned  |
| Section 8 | Functional safety assessment                            | IFS Assessment Report                              | EVD-029       | Planned  |
| Section 8 | Management of safety audit trail                        | Safety Audit Log Integrity Report                  | EVD-011       | Planned  |

### Part 2: Hardware Requirements

| Clause       | Activity                                              | Evidence                                           | EVD ID(s)           | Status   |
|--------------|-------------------------------------------------------|----------------------------------------------------|---------------------|----------|
| Section 7.2  | Hardware safety function design                       | Safety Function Design Specification               | EVD-024             | Drafted  |
| Section 7.4  | Hardware safety function implementation               | RF Power Limiter Test, Flux Current Limiter Test   | EVD-001, EVD-004    | Planned  |
| Section 7.4.2.2 | Independence of hardware protection layers          | Analog Comparator Independence Evidence            | EVD-006             | Planned  |
| Section 7.4.3 | Diagnostic coverage                                  | Safety PLC Diagnostic Test Report                  | EVD-005             | Planned  |
| Section 7.4.6 | Communication safety                                 | Safety PLC Diagnostic Test (comm loss test)         | EVD-005             | Planned  |
| Section 7.7  | Hardware integration testing                          | System Integration Test Report                     | EVD-007             | Planned  |

### Part 3: Software Requirements

| Clause       | Activity                                              | Evidence                                           | EVD ID(s)           | Status   |
|--------------|-------------------------------------------------------|----------------------------------------------------|---------------------|----------|
| Section 7.2  | Software safety requirements specification            | Safety Requirements Specification (software)       | EVD-021             | Drafted  |
| Section 7.4  | Software architecture design                          | System Architecture Description                    | EVD-022             | Drafted  |
| Section 7.9  | Software safety validation                            | Calibration Subsystem Validation Report            | EVD-009             | Planned  |

### Part 6: SIL Calculation

| Clause       | Activity                                              | Evidence                                           | EVD ID(s)     | Status   |
|--------------|-------------------------------------------------------|----------------------------------------------------|---------------|----------|
| Section 7    | PFDavg/PFH calculation                                | PFDavg Calculation Report                          | EVD-019       | Planned  |

### Part 7: Techniques and Measures

| Technique                          | Recommendation for SIL 2 | Applied? | Evidence                              | EVD ID(s)     |
|------------------------------------|---------------------------|----------|---------------------------------------|---------------|
| Fault detection and diagnosis      | Highly Recommended        | Yes      | Safety PLC Diagnostic Test Report     | EVD-005       |
| Redundancy (diverse)               | Recommended               | Yes      | Analog Comparator Independence Evidence| EVD-006      |
| Formal methods (safety-related SW) | Recommended               | Yes      | Formal Verification Coverage Report   | EVD-003       |
| Static analysis                    | Highly Recommended        | Yes      | CRE FPGA Design Verification Report  | EVD-028       |
| FMEA/FMECA                         | Highly Recommended        | Yes      | FMEA/FMECA Report                     | EVD-023       |
| Safety manual                      | Required                  | Planned  | Operation & Maintenance Manual         | (not indexed) |

## Formal Verification Coverage Metrics

The QPCS uses formal verification at two levels: control sequence verification (CMP-RTO-01E) and FPGA design verification (CMP-CRE-01A).

### Sequence Formal Verifier (CMP-RTO-01E)

| Property Category                 | Number of Properties | Coverage Metric                         | Tool                | EVD ID   |
|-----------------------------------|---------------------|-----------------------------------------|---------------------|----------|
| Timing constraint satisfaction    | 12                  | All pairwise qubit timing constraints for 100 qubits | SMT solver (Z3)    | EVD-003  |
| RF power budget per qubit         | 100                 | Per-qubit power envelope over full sequence duration | Bounded model checker | EVD-003 |
| Frequency collision avoidance     | 4950                | All qubit pairs checked for frequency proximity during simultaneous operations | SAT solver  | EVD-003 |
| Flux bias current limits          | 100                 | Per-qubit current setpoint within safe range for all time steps | SMT solver (Z3) | EVD-003  |
| Pulse overlap violations          | 100                 | No overlapping pulses on the same channel | SAT solver           | EVD-003  |

**Verification completeness argument:** The verifier checks all 5 categories of constraint for every gate sequence before execution. The set of properties was derived systematically from the hazard analysis (HZ-001 through HZ-007) and maps to CTL-001. The verifier model was independently reviewed for completeness (GAP-002 in traceability.md notes the residual risk of model incompleteness).

### CRE FPGA Design Verification (CMP-CRE-01A)

| Verification Method                | Coverage Target     | Metric                                  | Tool                     | EVD ID   |
|------------------------------------|--------------------|-----------------------------------------|--------------------------|----------|
| RTL simulation (UVM testbench)     | 100% code coverage | Statement, branch, condition, toggle    | Siemens Questa           | EVD-028  |
| Formal property verification       | 42 properties      | All safety-relevant state machine properties proven | Cadence JasperGold | EVD-028  |
| Equivalence checking (RTL vs. gate)| 100%               | Combinational and sequential equivalence | Synopsys Formality       | EVD-028  |
| Timing closure                     | 100%               | All paths meet setup and hold constraints at 4K operating temperature | Cadence Innovus | EVD-028 |

## EDA Tool Qualification Argument

The QPCS uses commercial EDA tools for FPGA design (CRE at 4K) and for safety PLC programming. IEC 61508 Part 3 Section 7.4.4 requires confidence in tools used in the safety lifecycle.

| Tool                               | Vendor             | Use                                     | Qualification Approach          | EVD ID   | Status   |
|------------------------------------|--------------------|----------------------------------------|--------------------------------|----------|----------|
| Questa Sim                         | Siemens EDA        | RTL simulation and UVM testbench execution for CRE FPGA | Tool validation per IEC 61508 Part 3 Table B.3: tool output verified by independent analysis | EVD-028 | Planned |
| JasperGold                         | Cadence            | Formal property verification for CRE FPGA | Tool output cross-checked against simulation results; proven properties independently reviewed | EVD-028 | Planned |
| Formality                          | Synopsys           | Equivalence checking (RTL to gate-level) for CRE FPGA | Tool output checked by sampling gate-level simulation against RTL simulation | EVD-028 | Planned |
| Innovus                            | Cadence            | Place-and-route and timing closure for CRE FPGA | Static timing analysis output verified by timing simulation at corners | EVD-028 | Planned |
| Safety PLC Programming Environment | PLC vendor          | Safety PLC application programming (IEC 61131-3) | Pre-certified tool per IEC 61508 Part 3; vendor provides T/TUV certification | EVD-024 | Planned |
| Z3 SMT Solver                      | Microsoft Research | Formal verification of gate sequences in CMP-RTO-01E | Open-source tool with extensive community validation; verification results cross-checked against brute-force simulation for small circuits | EVD-003 | Planned |

**Tool qualification rationale:** For SIL 2, IEC 61508 Part 3 Table B.3 permits tool validation approaches ranging from increased confidence from use to formal tool certification. The QPCS approach uses independent verification of tool outputs (simulation results checked against formal properties, and vice versa) to achieve the required tool confidence without requiring full tool certification, which is impractical for commercial EDA tools not specifically designed for IEC 61508 environments.

## HW/SW Interface Evidence

The HW/SW interface is critical for the QPCS because the safety function spans both hardware (analog limiters, comparators, safety PLC) and software (Safety Monitor, Calibration Engine) components.

| Interface                          | Hardware Component | Software Component | Critical Parameters                           | Verification Approach                     | EVD ID(s)          |
|------------------------------------|--------------------|--------------------|-----------------------------------------------|-------------------------------------------|--------------------|
| Safety interlock → RPG limiter     | CMP-SAF-01A/B      | —                  | Trip threshold (-20 dBm), response time (<10 us) | Hardware-in-loop test with calibrated RF source | EVD-001, EVD-006  |
| Safety interlock → FBC limiter     | CMP-SAF-01A/B      | —                  | Trip threshold (10 mA), response time (<10 us) | Hardware-in-loop test with calibrated current source | EVD-004, EVD-006 |
| Safety PLC → RTO Safety Monitor    | CMP-SAF-01A        | CMP-RTO-01D        | Heartbeat interval, safe-state trigger, status data | Communication failure injection test    | EVD-005            |
| Calibration SW → Safety Monitor    | —                  | CMP-RTO-01B/D      | Parameter approval request/grant, limit validation | Software integration test with boundary values | EVD-009          |
| CRE FPGA firmware → ADC hardware   | CMP-CRE-01B        | CMP-CRE-01D        | Sample rate, bit depth, timing alignment       | Hardware-in-loop test with calibrated signal source | EVD-012, EVD-028 |
| TDU FPGA → Clock distribution HW   | CMP-TDU-01B        | CMP-TDU-01C        | Clock frequency, jitter, skew                  | Oscilloscope measurement with calibrated probes | EVD-014          |
| RPG FPGA → AWG DAC hardware        | CMP-RPG-01A        | CMP-RPG-01D        | Sample rate, resolution, waveform integrity    | Spectrum analyzer and oscilloscope measurement | EVD-008          |

**Interface evidence completeness:** Every interface where a safety function crosses a HW/SW boundary has a defined verification approach with both hardware-in-loop testing and independent measurement instrumentation. The most critical interface (safety interlock to RPG/FBC limiters) uses hardwired discrete signals with no software in the path, eliminating HW/SW interface complexity for the primary safety barrier.
