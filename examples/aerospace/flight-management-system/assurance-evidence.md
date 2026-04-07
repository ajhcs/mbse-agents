# Assurance Evidence

## Assurance Framework

The Integrated Flight Management System follows the FAA development assurance framework with Stage of Involvement (SOI) progression from SOI #1 (Planning) through SOI #4 (Final). The certification basis is 14 CFR 25.1309 with ARP4754A as the accepted means of compliance for system development assurance per AC 20-174.

The evidence package supports concurrent review by the FAA Aircraft Certification Office (ACO), Designated Engineering Representatives (DERs) for systems, software (DO-178C), and hardware (DO-254), and the applicant's internal design assurance organization.

**SOI Progression:**

| SOI   | Gate Name     | Purpose                                                                     | Key Evidence                                                      |
|-------|---------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------|
| SOI #1| Planning      | Certification basis agreed, plans reviewed, standards and environment defined | PSAC, PHAC, System Dev Plan, Safety Assessment Plan, Security Plan |
| SOI #2| Development   | Requirements and architecture mature, preliminary safety assessment complete | FHA, PSSA, Requirement specs, Architecture description, Allocation tables |
| SOI #3| Verification  | Implementation complete, verification evidence collected, compliance demonstrated | Test reports, Analysis reports, SSA, CMA, Structural coverage, Security assessment |
| SOI #4| Final         | All findings closed, problem reports dispositioned, final compliance determination | Final compliance summary, PR disposition, Configuration index      |

## Evidence Lifecycle States

| State     | Meaning                                                    |
|-----------|------------------------------------------------------------|
| Planned   | Artifact identified, not yet started                       |
| Drafted   | Initial content exists, under development                  |
| Reviewed  | Peer or independent review completed                       |
| Approved  | Authority or designated reviewer accepted                  |
| Baselined | Under configuration control in the project CM system       |

## Evidence Index

| EVD ID   | Artifact Name                                         | Location                                               | Demonstrates                                              | Standard Clause                | Review Milestone | Evidence Consumer      | Status   |
|----------|-------------------------------------------------------|--------------------------------------------------------|-----------------------------------------------------------|-------------------------------|------------------|------------------------|----------|
| EVD-001  | Navigation Position Accuracy Test Report              | evidence/test-reports/nav-position-accuracy.pdf         | Position accuracy meets 0.05 NM (95%); sensor fusion performance | DO-178C Table A-6 (req-based testing) | SOI #3          | DER (Software)         | Planned  |
| EVD-002  | Quantitative Safety Analysis (FTA) Report             | evidence/safety/quantitative-fta-report.pdf             | HZ-001 probability ≤ 1e-9/FH; HZ-007 probability ≤ 1e-7/FH | ARP4761A Section 4.3          | SOI #3           | DER (Systems)          | Planned  |
| EVD-003  | Cross-Channel Comparison Test Report                  | evidence/test-reports/cross-channel-comparison.pdf      | Position and guidance disagree detection, failover timing  | DO-178C Table A-6; ARP4754A 5.2 | SOI #3          | DER (Systems/Software) | Planned  |
| EVD-004  | Sensor FDE Test Report                                | evidence/test-reports/sensor-fde-test.pdf               | Fault detection and exclusion performance; detection probability | DO-178C Table A-6             | SOI #3           | DER (Software)         | Planned  |
| EVD-005  | FDE Detection Probability Analysis                    | evidence/analysis/fde-detection-probability.pdf         | FDE detection probability ≥ 0.999/FH                      | ARP4761A Section 4.3          | SOI #3           | DER (Systems)          | Planned  |
| EVD-006  | Degraded Mode Transition Test Report                  | evidence/test-reports/degraded-mode-transition.pdf      | MODE-002, MODE-003, MODE-004 transitions; crew annunciations | DO-178C Table A-6; ARP4754A 5.2 | SOI #3          | DER (Systems)          | Planned  |
| EVD-007  | ARINC 653 Partition Isolation Test Report             | evidence/test-reports/partition-isolation.pdf            | Spatial and temporal isolation; health monitor response     | ARINC 653 Part 1; DO-178C A-7 | SOI #3           | DER (Software)         | Planned  |
| EVD-008  | Partition Isolation Analysis Report                   | evidence/analysis/partition-isolation-analysis.pdf       | Partition boundary integrity argument; CAST-32A interference assessment | CAST-32A; DO-178C Table A-7  | SOI #3           | DER (Software)         | Planned  |
| EVD-009  | Guidance Command Test Report                          | evidence/test-reports/guidance-command-test.pdf          | Lateral/vertical guidance accuracy, bank angle limits, speed protection | DO-178C Table A-6            | SOI #3           | DER (Software)         | Planned  |
| EVD-010  | VNAV Descent Path Error Analysis                      | evidence/analysis/vnav-path-error-analysis.pdf          | Vertical guidance path accuracy within +/-50 ft            | ARP4754A Section 5.2          | SOI #3           | DER (Systems)          | Planned  |
| EVD-011  | Watchdog Monitoring Test Report                       | evidence/test-reports/watchdog-test.pdf                  | Processor lockup detection within 500 ms; channel failover | DO-178C Table A-6             | SOI #3           | DER (Software)         | Planned  |
| EVD-012  | Security Verification Test Report                     | evidence/test-reports/security-verification.pdf          | Crypto signature, CRC integrity, datalink validation       | DO-326A Section 5.3           | SOI #3           | DER (Systems/Security) | Planned  |
| EVD-013  | Built-In Test Execution Report                        | evidence/test-reports/bit-execution.pdf                  | Power-up BIT coverage, fault detection, reporting           | DO-178C Table A-6; 14 CFR 25.1309 | SOI #3          | DER (Systems)          | Planned  |
| EVD-014  | Flight Plan Management Test Report                    | evidence/test-reports/flight-plan-management.pdf         | Plan creation, modification, datalink amendment, validation | DO-178C Table A-6             | SOI #3           | DER (Software)         | Planned  |
| EVD-015  | RNP/RNAV Monitoring Test Report                       | evidence/test-reports/rnp-monitoring.pdf                 | ANP computation, RNP containment alerting                  | AC 90-105A; DO-178C Table A-6 | SOI #3           | DER (Software), ACO    | Planned  |
| EVD-016  | Performance Computation Test Report                   | evidence/test-reports/performance-computation.pdf        | Fuel prediction accuracy, optimum cruise, low-fuel advisory | DO-178C Table A-6             | SOI #3           | DER (Software)         | Planned  |
| EVD-017  | Display and CDU Test Report                           | evidence/test-reports/display-cdu-test.pdf               | Display refresh rate, CDU response timing                  | DO-178C Table A-6             | SOI #3           | DER (Software)         | Planned  |
| EVD-018  | Security Controls Test Report                         | evidence/test-reports/security-controls.pdf              | Maintenance auth, one-way data flow, AFDX MAC verification | DO-326A Section 5.3           | SOI #3           | DER (Systems/Security) | Planned  |
| EVD-019  | AFDX Virtual Link Directionality Analysis             | evidence/analysis/afdx-directionality-analysis.pdf       | One-way FMC-to-DMC data flow enforcement                   | DO-326A Section 5.3           | SOI #3           | DER (Systems)          | Planned  |
| EVD-020  | Interface Timing Test Report                          | evidence/test-reports/interface-timing.pdf                | IRS forwarding, AFDX bandwidth, datalink latency, TAWS output | DO-178C Table A-6; ICD verification | SOI #3     | DER (Systems)          | Planned  |
| EVD-021  | Environmental Qualification Test Report               | evidence/test-reports/environmental-qualification.pdf    | Power-up timing at temperature extremes; power consumption  | DO-160G; 14 CFR 25.1309      | SOI #3           | DER (Systems), ACO     | Planned  |
| EVD-022  | WCET and CAST-32A Interference Analysis               | evidence/analysis/wcet-cast32a-analysis.pdf              | Guidance WCET ≤ 15 ms; multi-core interference within budget | CAST-32A; DO-178C Table A-7  | SOI #3           | DER (Software)         | Planned  |
| EVD-023  | Navigation Continuity Reliability Analysis            | evidence/analysis/nav-continuity-analysis.pdf            | Navigation output loss probability ≤ 1e-5/FH               | ARP4761A Section 4.3          | SOI #3           | DER (Systems)          | Planned  |
| EVD-024  | Cross-Channel Comparator Independence Evidence Package | evidence/analysis/comparator-independence.pdf           | Hardware independence of comparator from both software channels | ARP4761A CMA; DO-254 Section 5 | SOI #3          | DER (Systems/Hardware) | Planned  |
| EVD-025  | Plan for Software Aspects of Certification (PSAC)     | evidence/plans/psac.pdf                                  | Software lifecycle planning, standards, environment         | DO-178C Section 10.1          | SOI #1           | DER (Software), ACO    | Drafted  |
| EVD-026  | Plan for Hardware Aspects of Certification (PHAC)     | evidence/plans/phac.pdf                                  | Hardware lifecycle planning, standards, environment         | DO-254 Section 10.1           | SOI #1           | DER (Hardware), ACO    | Drafted  |
| EVD-027  | System Development Plan                               | evidence/plans/system-dev-plan.pdf                       | ARP4754A process planning, DAL allocation, review schedule  | ARP4754A Section 5.1          | SOI #1           | DER (Systems), ACO     | Drafted  |
| EVD-028  | Functional Hazard Assessment (FHA)                    | evidence/safety/fha-report.pdf                           | Aircraft/system failure condition identification and classification | ARP4761A Section 4.2     | SOI #2           | DER (Systems), ACO     | Drafted  |
| EVD-029  | Preliminary System Safety Assessment (PSSA)           | evidence/safety/pssa-report.pdf                          | Safety requirement allocation, fault tree construction       | ARP4761A Section 4.3          | SOI #2           | DER (Systems)          | Drafted  |
| EVD-030  | Software Requirements Specification (SRS)             | evidence/development/srs.pdf                             | High-level software requirements                             | DO-178C Table A-3             | SOI #2           | DER (Software)         | Drafted  |
| EVD-031  | Hardware Requirements Specification (HRS)             | evidence/development/hrs.pdf                             | Hardware requirements for FPGA components                    | DO-254 Section 5.1            | SOI #2           | DER (Hardware)         | Drafted  |
| EVD-032  | Software Design Description (SDD)                     | evidence/development/sdd.pdf                             | Software architecture and low-level requirements             | DO-178C Table A-4             | SOI #2           | DER (Software)         | Drafted  |
| EVD-033  | Security Risk Assessment Report                       | evidence/security/security-risk-assessment.pdf           | DO-326A threat assessment, asset identification, security requirements | DO-326A Section 5.2    | SOI #2           | DER (Systems/Security) | Drafted  |
| EVD-034  | Common Mode Analysis (CMA) Report                     | evidence/safety/cma-report.pdf                           | Independence and common-cause analysis for redundancy arguments | ARP4761A CMA             | SOI #3           | DER (Systems)          | Planned  |
| EVD-035  | DO-178C Structural Coverage Analysis (MC/DC)          | evidence/test-reports/structural-coverage.pdf            | MC/DC coverage for Level A software                          | DO-178C Table A-7 Objective 7 | SOI #3          | DER (Software)         | Planned  |
| EVD-036  | Code Generator Tool Qualification Report (DO-330)     | evidence/tool-qualification/code-gen-tqr.pdf             | TQL-1 qualification for auto-code generator                  | DO-330 Section 9              | SOI #2           | DER (Software), ACO    | Planned  |
| EVD-037  | Test Automation Tool Qualification Report (DO-330)    | evidence/tool-qualification/test-automation-tqr.pdf      | TQL-4 qualification for test automation framework            | DO-330 Section 9              | SOI #2           | DER (Software)         | Planned  |
| EVD-038  | Model-Based Development Compliance Summary (DO-331)   | evidence/development/do331-compliance-summary.pdf        | DO-331 MB.6.3 objectives for model-to-code lifecycle         | DO-331 MB.6.3                 | SOI #3           | DER (Software), ACO    | Planned  |
| EVD-039  | System Safety Assessment (SSA)                        | evidence/safety/ssa-report.pdf                           | Confirmation that all PSSA targets are met with implementation evidence | ARP4761A Section 4.4   | SOI #3           | DER (Systems), ACO     | Planned  |
| EVD-040  | Configuration Index                                   | evidence/cm/configuration-index.pdf                      | Complete list of all controlled artifacts with version IDs   | DO-178C Table A-8; DO-254 Section 8 | SOI #4    | DER (Software/Hardware), ACO | Planned |
| EVD-041  | Problem Report Disposition Summary                    | evidence/cm/problem-report-summary.pdf                   | All PRs dispositioned; no open safety-relevant PRs           | DO-178C Table A-9             | SOI #4           | DER (Software), ACO    | Planned  |
| EVD-042  | Final Compliance Summary                              | evidence/compliance/final-compliance-summary.pdf          | Means of compliance complete for all applicable regulations  | ARP4754A Section 5.4; 14 CFR 25.1309 | SOI #4    | ACO                    | Planned  |

## DO-178C Table A Mapping (DAL A)

This section maps DO-178C Table A objectives to evidence artifacts for the FMS Level A software components (CMP-FMC-01E, CMP-FMC-01F, CMP-FMC-01G, CMP-FMC-01D).

| Table   | Objective Area                        | Key Objectives (Level A)                                              | EVD ID(s)          | Independence Required |
|---------|---------------------------------------|-----------------------------------------------------------------------|--------------------|-----------------------|
| A-1     | Planning Process                      | Plans define lifecycle, standards, environment                        | EVD-025            | No                    |
| A-2     | Development Standards                 | Standards for requirements, design, code are defined and followed      | EVD-025, EVD-030   | No                    |
| A-3     | Software Requirements                 | HLR accuracy, consistency, traceability, conformance to standards     | EVD-030            | Yes                   |
| A-4     | Software Design                       | Architecture verifiable, LLR accurate, data/control coupling analyzed | EVD-032, EVD-038   | Yes                   |
| A-5     | Software Coding                       | Source conforms to architecture, coding standards compliance           | EVD-032, EVD-038   | Yes                   |
| A-6     | Verification (Testing)                | Requirements-based test cases, normal and robustness testing          | EVD-001 through EVD-017 | Yes              |
| A-7     | Verification (Coverage)               | MC/DC structural coverage, data/control coupling coverage             | EVD-035, EVD-022   | Yes                   |
| A-8     | Configuration Management              | Identification, baseline, change control, archival                    | EVD-040            | No                    |
| A-9     | Quality Assurance                     | Process compliance, transition criteria, PR tracking                  | EVD-041            | No                    |
| A-10    | Certification Liaison                 | Plans submitted, SOI reviews conducted, findings resolved             | EVD-042            | No                    |

## DO-254 Evidence (DAL A)

Hardware evidence for programmable components CMP-FMC-01J (FMC FPGA) and CMP-DCU-01D (DCU FPGA).

| DO-254 Section | Activity                              | Evidence                                              | EVD ID(s)          | Status   |
|----------------|---------------------------------------|-------------------------------------------------------|--------------------| ---------|
| Section 5.1    | Hardware Requirements                 | Hardware Requirements Specification                   | EVD-031            | Drafted  |
| Section 5.2    | Conceptual Design                     | FPGA architecture description and block diagrams      | EVD-032            | Drafted  |
| Section 5.3    | Detailed Design                       | HDL source, synthesis reports, timing analysis         | (internal to EVD-032) | Planned |
| Section 5.4    | Implementation                        | FPGA place-and-route results, bitstream               | (build artifacts)  | Planned  |
| Section 5.5    | Verification                          | FPGA functional verification, timing verification     | EVD-003, EVD-020   | Planned  |
| Section 8      | Configuration Management              | FPGA configuration index, HDL baseline                | EVD-040            | Planned  |
| Section 10.1   | Planning                              | PHAC                                                  | EVD-026            | Drafted  |

## DO-326A Security Evidence

| DO-326A Section | Activity                              | Evidence                                              | EVD ID(s)          | Status   |
|-----------------|---------------------------------------|-------------------------------------------------------|--------------------| ---------|
| Section 5.1     | Security Planning                     | Airworthiness Security Plan (within System Dev Plan)  | EVD-027            | Drafted  |
| Section 5.2     | Security Risk Assessment              | Threat assessment, asset identification, risk analysis | EVD-033            | Drafted  |
| Section 5.3     | Security Verification                 | Security controls test results                        | EVD-012, EVD-018   | Planned  |
| Section 5.4     | Security Compliance Summary           | Security requirements trace, residual risk acceptance | EVD-042            | Planned  |

## DO-330 Tool Qualification

| Tool                          | Criteria | TQL   | Hosted SW Level | Justification                                                  | EVD ID   | Status   |
|-------------------------------|----------|-------|-----------------|----------------------------------------------------------------|----------|----------|
| Code Generator (Embedded Coder) | 1      | TQL-1 | Level A         | Generates code from navigation models; output enters airborne SW baseline. Model-to-code traceability verified but tool output is relied upon without independent code review of every generated line. | EVD-036 | Planned |
| Test Automation Framework     | 2        | TQL-4 | Level A         | Automates test execution and result comparison; output is trusted for verification credit without manual re-execution of every test case. | EVD-037 | Planned |
| Requirements Management Tool  | 3        | —     | Level A         | Used for requirement storage and traceability; output is independently reviewed. No qualification required (Criteria 3 tool). | —       | N/A      |
| Static Analysis Tool          | 2        | TQL-4 | Level A         | Automates coding standards compliance checking; findings are reviewed but the tool is relied upon for completeness of checks. | EVD-037 | Planned |
| Model Coverage Tool           | 2        | TQL-4 | Level A         | Measures model coverage for DO-331 MB.6.4 credit; coverage results are trusted for verification completeness assessment. | EVD-037 | Planned |

## DO-331 Model-Based Development Evidence

The FMC navigation algorithms (CMP-FMC-01E, CMP-FMC-01F) are developed using model-based methods invoking DO-331 MB.6.3 (model used to generate code). The following evidence chain supports DO-331 compliance:

| DO-331 Objective | Activity                                                | Evidence                                      | EVD ID   |
|------------------|---------------------------------------------------------|-----------------------------------------------|----------|
| MB.6.1           | Model standards and modeling guidelines defined          | Model Standards Document (in PSAC)            | EVD-025  |
| MB.6.3.1         | Model developed per model standards                      | Model review records                          | EVD-038  |
| MB.6.3.2         | Model reviewed against standards                         | Model review checklist and findings           | EVD-038  |
| MB.6.3.3         | Model-to-code transformation verified                    | Auto-generated code review samples            | EVD-038  |
| MB.6.3.4         | Model under configuration management                     | Model baseline in CM system                   | EVD-040  |
| MB.6.3.5         | Model-to-code traceability established                   | Traceability matrix (model element to code)   | EVD-038  |
| MB.6.4.4         | Model coverage analysis (if model used for verification) | Model coverage report                         | EVD-035  |
