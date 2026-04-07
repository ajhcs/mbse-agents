# Assurance Evidence

## Assurance Framework

The Autonomous Emergency Braking system follows the ISO 26262 functional safety lifecycle with an ASIL D safety case. The safety lifecycle spans from concept phase (Part 3) through system development (Parts 4-5), hardware development (Part 5), software development (Part 6), integration and testing (Parts 8-9), and production/operation (Parts 10-12). A third-party functional safety assessment (FSA) is performed per ISO 26262-2 clause 6.4.6 by an independent assessor.

The evidence package supports review by the vehicle OEM safety organization, the third-party functional safety assessor, the type approval authority (UNECE for UN R152), and the Tier-1 supplier's internal functional safety management team.

**Review Progression:**

| Gate       | Gate Name                   | Purpose                                                                                      | Key Evidence                                                             |
|------------|-----------------------------|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Gate 1     | Concept Phase Review        | HARA and safety goals reviewed; safety concept approved                                      | HARA report, Safety Goals, Functional Safety Concept                     |
| Gate 2     | System Design Review        | System architecture, TSR, technical safety concept, cybersecurity concept reviewed            | TSR, Technical Safety Concept, TARA, Architecture Description            |
| Gate 3     | SW/HW Design Review         | Detailed design reviewed; safety analysis updated; verification plans approved                | SW architecture, HW design, FMEA/FTA updates, Verification Plans        |
| Gate 4     | Integration Test Review     | Integration test results reviewed; safety validation evidence collected                       | Integration test reports, Fault injection test results, HW fault metrics |
| Gate 5     | Safety Case Closure / FSA   | Complete safety case reviewed; confirmation measures complete; FSA findings closed            | Safety case, Confirmation review reports, FSA report, Type approval evidence |

## Evidence Lifecycle States

| State     | Meaning                                                    |
|-----------|------------------------------------------------------------|
| Planned   | Artifact identified, not yet started                       |
| Drafted   | Initial content exists, under development                  |
| Reviewed  | Peer or independent review completed                       |
| Approved  | Authority or designated reviewer accepted                  |
| Baselined | Under configuration control in the project CM system       |

## Evidence Index

| EVD ID   | Artifact Name                                           | Location                                                   | Demonstrates                                                         | Standard Clause                         | Review Milestone | Evidence Consumer              | Status   |
|----------|---------------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------|-----------------------------------------|------------------|--------------------------------|----------|
| EVD-001  | Camera Detection Range and Classification Test Report   | evidence/test-reports/camera-detection-test.pdf             | Camera detection range (120 m vehicle, 60 m pedestrian) and DNN classification accuracy (99%/95%) | ISO 26262-4 clause 7; UN R152 Annex 3  | Gate 4          | OEM Safety, Type Approval      | Planned  |
| EVD-002  | Radar Detection Range and Accuracy Test Report          | evidence/test-reports/radar-detection-test.pdf              | Radar detection range (200 m), accuracy (+/- 0.5 m, +/- 0.3 m/s), overhead filtering | ISO 26262-4 clause 7                   | Gate 4          | OEM Safety                     | Planned  |
| EVD-003  | Sensor Fusion Performance Test Report                   | evidence/test-reports/sensor-fusion-test.pdf                | Fusion rate (25 Hz), confidence scoring, tracking, trajectory prediction | ISO 26262-4 clause 7; ISO 21448 clause 10 | Gate 4       | OEM Safety, FSA Assessor       | Planned  |
| EVD-004  | Collision Decision Logic Test Report                    | evidence/test-reports/collision-decision-test.pdf           | TTC computation accuracy, graduated braking levels, multi-frame confirmation | ISO 26262-4 clause 7                   | Gate 4          | OEM Safety                     | Planned  |
| EVD-005  | Brake Release and Timeout Test Report                   | evidence/test-reports/brake-release-test.pdf                | Brake release timing (200 ms), 3-second timeout, post-collision behavior | ISO 26262-4 clause 7                   | Gate 4          | OEM Safety                     | Planned  |
| EVD-006  | Braking Actuation Performance Test Report               | evidence/test-reports/braking-actuation-test.pdf            | Brake force accuracy, response latency (150 ms), ABS coordination, ESC override, deceleration limits | ISO 26262-4 clause 7; UN R152 Annex 3 | Gate 4 | OEM Safety, Type Approval      | Planned  |
| EVD-007  | Driver Warning System Test Report                       | evidence/test-reports/driver-warning-test.pdf               | Warning timing (500 ms before braking), visual and audible warning content | UN R152 clause 5.4.1                   | Gate 4          | Type Approval                  | Planned  |
| EVD-008  | Sensor Health Monitoring Test Report                    | evidence/test-reports/sensor-health-monitoring-test.pdf     | Diagnostic coverage (90%), degraded mode transition (100 ms), sensor fault injection results | ISO 26262-5 clause 7.4.4; ISO 26262-4 clause 7 | Gate 4 | OEM Safety, FSA Assessor | Planned  |
| EVD-009  | Power-Up Self-Test Report                               | evidence/test-reports/power-up-self-test.pdf                | BIT execution within 5 seconds, readiness reporting, latent fault detection | ISO 26262-5 clause 7.4.4              | Gate 4          | OEM Safety                     | Planned  |
| EVD-010  | Sensor Calibration Verification Report                  | evidence/test-reports/calibration-verification.pdf          | Calibration accuracy (+/- 0.5 deg), alignment procedure validation    | ISO 21448 clause 10                     | Gate 4          | OEM Safety                     | Planned  |
| EVD-011  | Event Data Recording Verification Report                | evidence/test-reports/edr-verification.pdf                  | Pre-event data capture (5 seconds), NVM storage integrity, data completeness | UN R152 clause 6.4                     | Gate 4          | Type Approval                  | Planned  |
| EVD-012  | OTA Update Security Test Report                         | evidence/test-reports/ota-security-test.pdf                 | Crypto signature verification, anti-rollback, secure boot, rollback capability | ISO 21434 clause 15; ISO 26262-4 clause 7 | Gate 4      | OEM Safety, Cybersecurity Assessor | Planned |
| EVD-013  | Dual-Sensor Detection Rate Test Campaign Report         | evidence/test-reports/dual-sensor-detection-campaign.pdf    | Combined camera+radar detection rate (>= 95%), UN R152 target scenarios | ISO 26262-4 clause 7; UN R152 Annex 3  | Gate 4          | OEM Safety, Type Approval      | Planned  |
| EVD-014  | Undetected Collision Probability Analysis               | evidence/analysis/undetected-collision-probability.pdf      | Probability analysis demonstrating <= 1e-8/h for undetected collision | ISO 26262-5 clause 7.4; ARP4761A methodology adapted | Gate 5 | FSA Assessor                   | Planned  |
| EVD-015  | False Positive Rate Statistical Analysis and Test       | evidence/test-reports/false-positive-rate-test.pdf          | False activation rate < 1 per 100,000 km under representative conditions | ISO 26262-4 clause 7; ISO 21448 clause 10 | Gate 4      | OEM Safety, Type Approval      | Planned  |
| EVD-016  | End-to-End Latency Test and Analysis Report             | evidence/test-reports/e2e-latency-test.pdf                  | Total latency <= 300 ms worst case; component-level breakdown         | ISO 26262-4 clause 7                   | Gate 4          | OEM Safety, FSA Assessor       | Planned  |
| EVD-017  | Hardware Fault Metric Analysis (FMEDA)                  | evidence/analysis/hardware-fault-metrics.pdf                | SPFM >= 99%, LFM >= 90%, PMHF within ASIL D budget for braking path  | ISO 26262-5 clause 8; Annex C          | Gate 4          | FSA Assessor                   | Planned  |
| EVD-018  | SOTIF Degraded Mode Test Report                         | evidence/test-reports/sotif-degraded-mode-test.pdf          | TTC extension (x1.5), speed limit (80 km/h), confidence monitoring, MODE-003 transitions | ISO 21448 clause 10                    | Gate 4          | OEM Safety, FSA Assessor       | Planned  |
| EVD-019  | SOTIF Triggering Condition Analysis                     | evidence/analysis/sotif-triggering-condition-analysis.pdf   | Coverage of triggering conditions TC-001 through TC-007; residual risk evaluation | ISO 21448 clause 6.3                  | Gate 5          | FSA Assessor                   | Planned  |
| EVD-020  | Cybersecurity Controls Test Report                      | evidence/test-reports/cybersecurity-controls-test.pdf       | CAN firewall, IDS, E2E protection, diagnostic security access testing  | ISO 21434 clause 15                    | Gate 4          | Cybersecurity Assessor         | Planned  |
| EVD-021  | Interface Timing and Protocol Test Report               | evidence/test-reports/interface-timing-test.pdf             | SOME/IP latency, CAN FD E2E, gateway translation, brake feedback rate  | ISO 26262-4 clause 7                   | Gate 4          | OEM Safety                     | Planned  |
| EVD-022  | DNN Inference Timing and Thermal Analysis               | evidence/analysis/dnn-inference-timing.pdf                  | DNN WCET <= 30 ms; thermal derating analysis                          | ISO 26262-6 clause 7; ISO 26262-11     | Gate 3          | OEM Safety                     | Planned  |
| EVD-023  | Environmental and Startup Test Report                   | evidence/test-reports/environmental-startup-test.pdf        | Operation -40C to +85C; startup within 5 seconds; power consumption   | ISO 26262-4 clause 7; ISO 16750        | Gate 4          | OEM Safety, Type Approval      | Planned  |
| EVD-024  | UN R152 Type Approval Test Report                       | evidence/test-reports/un-r152-type-approval.pdf             | Speed reduction for stationary target, full stop for pedestrian crossing | UN R152 Annex 3                        | Gate 5          | Type Approval Authority        | Planned  |
| EVD-025  | HARA Report                                             | evidence/safety/hara-report.pdf                             | Hazardous event identification and ASIL classification                 | ISO 26262-3 clause 7                   | Gate 1          | OEM Safety, FSA Assessor       | Drafted  |
| EVD-026  | Safety Goals and Functional Safety Concept              | evidence/safety/fsc-report.pdf                              | Safety goals SG-001 through SG-005; functional safety concept          | ISO 26262-3 clauses 8-9               | Gate 1          | OEM Safety, FSA Assessor       | Drafted  |
| EVD-027  | Technical Safety Requirements (TSR)                     | evidence/safety/tsr-report.pdf                              | System-level safety requirements derived from safety goals             | ISO 26262-4 clause 6                   | Gate 2          | OEM Safety, FSA Assessor       | Drafted  |
| EVD-028  | Technical Safety Concept                                | evidence/safety/tsc-report.pdf                              | Architecture-level safety concept with allocation and safety mechanisms | ISO 26262-4 clause 7                  | Gate 2          | OEM Safety, FSA Assessor       | Drafted  |
| EVD-029  | Cybersecurity TARA Report                               | evidence/security/tara-report.pdf                           | ISO 21434 threat analysis, asset identification, risk assessment       | ISO 21434 clauses 8-9                 | Gate 2          | Cybersecurity Assessor         | Drafted  |
| EVD-030  | System Architecture Description                         | evidence/development/system-architecture.pdf                | Component hierarchy, interfaces, allocation, partitioning rationale    | ISO 26262-4 clause 7                   | Gate 2          | OEM Safety                     | Drafted  |
| EVD-031  | Software Architecture and Design Document               | evidence/development/sw-architecture.pdf                    | AUTOSAR Adaptive/Classic SW architecture, process groups, safety mechanisms | ISO 26262-6 clause 7                | Gate 3          | OEM Safety                     | Planned  |
| EVD-032  | Hardware Design Document (Braking ECU)                  | evidence/development/hw-design-braking.pdf                  | Lockstep MCU, ECC, watchdog, valve driver safety design                | ISO 26262-5 clauses 6-7               | Gate 3          | OEM Safety, FSA Assessor       | Planned  |
| EVD-033  | Common Cause Analysis (DFA)                             | evidence/safety/common-cause-analysis.pdf                   | Dependent failure analysis for ASIL decomposition; sensor independence evidence | ISO 26262-9 clause 7              | Gate 4          | FSA Assessor                   | Planned  |
| EVD-034  | Freedom from Interference Analysis                      | evidence/safety/ffi-analysis.pdf                            | Spatial, temporal, communication protection between ASIL levels on Perception ECU | ISO 26262-6 Annex D; ISO 26262-9 clause 6 | Gate 3   | FSA Assessor                   | Planned  |
| EVD-035  | Safety Case Report                                      | evidence/safety/safety-case-report.pdf                      | Complete safety argument with GSN structure; links all evidence         | ISO 26262-2 clause 6.4.3              | Gate 5          | OEM Safety, FSA Assessor       | Planned  |
| EVD-036  | Confirmation Review Report (Verification Review)        | evidence/safety/confirmation-review-report.pdf              | Independent verification review per ISO 26262-2 clause 6.4.4          | ISO 26262-2 clause 6.4.4              | Gate 5          | FSA Assessor                   | Planned  |
| EVD-037  | Functional Safety Assessment (FSA) Report               | evidence/safety/fsa-report.pdf                              | Third-party assessment findings and closure                            | ISO 26262-2 clause 6.4.6              | Gate 5          | OEM Safety, Type Approval      | Planned  |
| EVD-038  | Functional Safety Audit Report                          | evidence/safety/fs-audit-report.pdf                         | Process audit confirming safety lifecycle compliance                    | ISO 26262-2 clause 6.4.5              | Gate 5          | OEM Safety                     | Planned  |

## ISO 26262 Work Product Mapping by Part

### Part 3: Concept Phase

| Part 3 Clause | Work Product                            | EVD ID(s) | ASIL   | Status  |
|---------------|-----------------------------------------|-----------|--------|---------|
| Clause 5      | Item Definition                         | (README.md, system.yaml) | ASIL D | Drafted |
| Clause 7      | Hazard Analysis and Risk Assessment     | EVD-025   | ASIL D | Drafted |
| Clause 8      | Safety Goals                            | EVD-026   | ASIL D | Drafted |
| Clause 9      | Functional Safety Concept               | EVD-026   | ASIL D | Drafted |

### Part 4: Product Development at the System Level

| Part 4 Clause | Work Product                            | EVD ID(s)        | ASIL   | Status  |
|---------------|-----------------------------------------|------------------|--------|---------|
| Clause 6      | Technical Safety Requirements (TSR)     | EVD-027          | ASIL D | Drafted |
| Clause 7      | System Design / Technical Safety Concept | EVD-028, EVD-030 | ASIL D | Drafted |
| Clause 7      | Integration and Testing Evidence         | EVD-001 through EVD-024 | ASIL D | Planned |

### Part 5: Product Development at the Hardware Level

| Part 5 Clause | Work Product                            | EVD ID(s) | ASIL   | Status  |
|---------------|-----------------------------------------|-----------|--------|---------|
| Clause 6      | Hardware Design Specification           | EVD-032   | ASIL D | Planned |
| Clause 7      | Hardware Safety Mechanisms              | EVD-032   | ASIL D | Planned |
| Clause 7.4.4  | Evaluation of Safety Goal Violations (FMEDA) | EVD-017 | ASIL D | Planned |
| Clause 8      | Hardware Architectural Metrics (SPFM, LFM, PMHF) | EVD-017 | ASIL D | Planned |

### Part 6: Product Development at the Software Level

| Part 6 Clause | Work Product                            | EVD ID(s) | ASIL   | Status  |
|---------------|-----------------------------------------|-----------|--------|---------|
| Clause 7      | Software Architectural Design           | EVD-031   | ASIL D | Planned |
| Clause 8      | Software Unit Design and Implementation | EVD-031   | ASIL D | Planned |
| Clause 9      | Software Unit Verification              | EVD-031   | ASIL D | Planned |
| Clause 10     | Software Integration and Verification   | (various test reports) | ASIL D | Planned |
| Annex D       | Freedom from Interference               | EVD-034   | ASIL D | Planned |

### Part 9: ASIL-Oriented and Safety-Oriented Analysis

| Part 9 Clause | Work Product                            | EVD ID(s) | ASIL   | Status  |
|---------------|-----------------------------------------|-----------|--------|---------|
| Clause 5      | ASIL Decomposition Justification        | EVD-033   | ASIL D | Planned |
| Clause 6      | Freedom from Interference               | EVD-034   | ASIL D | Planned |
| Clause 7      | Dependent Failure Analysis (DFA)        | EVD-033   | ASIL D | Planned |

### Part 2: Management of Functional Safety

| Part 2 Clause | Work Product                            | EVD ID(s) | ASIL   | Status  |
|---------------|-----------------------------------------|-----------|--------|---------|
| Clause 6.4.3  | Safety Case                             | EVD-035   | ASIL D | Planned |
| Clause 6.4.4  | Confirmation Review (Verification)      | EVD-036   | ASIL D | Planned |
| Clause 6.4.5  | Functional Safety Audit                 | EVD-038   | ASIL D | Planned |
| Clause 6.4.6  | Functional Safety Assessment (FSA)      | EVD-037   | ASIL D | Planned |

## Safety Case Structure (GSN)

The safety case follows a Goal Structuring Notation (GSN) pattern:

```
G1: AEB system is acceptably safe for public road deployment [ASIL D]
|
+-- S1: Argument over hazardous events identified in HARA
|   |
|   +-- G1.1: All hazardous events are identified and classified [EVD-025]
|   +-- G1.2: Safety goals are complete and correct [EVD-026]
|   +-- G1.3: Safety goals are allocated to system design [EVD-027, EVD-028]
|
+-- S2: Argument over safety requirements implementation
|   |
|   +-- G2.1: Safety requirements are derived from safety goals [EVD-027]
|   +-- G2.2: Safety requirements are allocated to architecture [EVD-030, traceability.md]
|   +-- G2.3: Safety requirements are verified [EVD-001 through EVD-024]
|
+-- S3: Argument over ASIL D hardware integrity
|   |
|   +-- G3.1: Hardware fault metrics meet ASIL D targets [EVD-017]
|   +-- G3.2: Safety mechanisms provide required diagnostic coverage [EVD-008, EVD-032]
|   +-- G3.3: ASIL decomposition is justified [EVD-033]
|
+-- S4: Argument over SOTIF perception adequacy
|   |
|   +-- G4.1: Triggering conditions are identified and analyzed [EVD-019]
|   +-- G4.2: Residual SOTIF risk is acceptable [EVD-018, EVD-019]
|   +-- G4.3: SOTIF-aware degradation limits AEB to safe operating region [EVD-018]
|
+-- S5: Argument over cybersecurity adequacy
|   |
|   +-- G5.1: Threats are identified and assessed [EVD-029]
|   +-- G5.2: Security controls mitigate identified threats [EVD-012, EVD-020]
|   +-- G5.3: Security-safety interaction is managed [EVD-029, cybersecurity.md]
|
+-- S6: Argument over process compliance
    |
    +-- G6.1: Safety lifecycle followed per ISO 26262 [EVD-038]
    +-- G6.2: Confirmation measures completed [EVD-036, EVD-037, EVD-038]
    +-- G6.3: Type approval evidence complete [EVD-024]
```

## Confirmation Measures

### Verification Review (ISO 26262-2 clause 6.4.4)

| Review Area                      | Scope                                                    | Method                  | Evidence Required                    | Status  |
|----------------------------------|----------------------------------------------------------|-------------------------|--------------------------------------|---------|
| HARA completeness                | All operational situations considered; ASIL classification correct | Independent review     | EVD-025 reviewed by assessor        | Planned |
| Safety concept correctness       | Safety goals correctly decomposed to TSR and TSC          | Independent review      | EVD-026, EVD-027, EVD-028           | Planned |
| Architecture safety adequacy     | ASIL decomposition valid; freedom from interference demonstrated | Independent review    | EVD-033, EVD-034                     | Planned |
| Hardware fault metric validity   | FMEDA assumptions valid; failure rates justified          | Independent review      | EVD-017                              | Planned |
| Verification completeness        | All safety requirements verified; traceability complete   | Audit                   | traceability.md, EVD-001 to EVD-024 | Planned |

### Functional Safety Assessment (ISO 26262-2 clause 6.4.6)

The third-party FSA is performed by an assessor independent of the development organization, examining:

1. Whether the safety lifecycle processes were followed correctly.
2. Whether the safety case is complete, consistent, and convincing.
3. Whether the evidence supports the safety claims made.
4. Whether the SOTIF analysis adequately addresses perception limitations.
5. Whether the cybersecurity measures adequately protect safety-relevant functions.

### Functional Safety Audit (ISO 26262-2 clause 6.4.5)

Process audit confirming that the development organization followed the safety management procedures defined in the safety plan, including:
- Configuration management of safety-relevant artifacts.
- Change management process for safety requirements and design.
- Problem report and anomaly management for safety-relevant findings.
- Tool confidence level assessment per ISO 26262-8 clause 11.

## Homologation Evidence

| UN R152 Clause | Requirement                                         | Evidence                              | EVD ID   | Status  |
|----------------|------------------------------------------------------|---------------------------------------|----------|---------|
| Clause 5.1     | AEB operational speed range                          | System specification and test          | EVD-024  | Planned |
| Clause 5.2     | Forward detection capability                         | Camera and radar detection tests       | EVD-001, EVD-002, EVD-013 | Planned |
| Clause 5.3     | Object tracking and collision assessment             | Fusion and decision logic tests        | EVD-003, EVD-004 | Planned |
| Clause 5.4     | Warning-then-braking sequence                        | Driver warning and braking tests       | EVD-007, EVD-006 | Planned |
| Clause 5.4.1   | Forward collision warning before braking              | Warning timing test (500 ms)           | EVD-007  | Planned |
| Clause 5.5     | Driver override capability                           | Accelerator override test              | EVD-006  | Planned |
| Clause 6.4     | Event data recording                                 | EDR verification                       | EVD-011  | Planned |
| Annex 3        | Test scenario performance thresholds                 | UN R152 type approval test campaign    | EVD-024  | Planned |
