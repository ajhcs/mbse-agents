# Assurance Evidence

> Illustrative proposed baseline. Numeric targets, allocations, risk ratings, and evidence paths are teaching assumptions. No executed tests, approved design, or regulatory acceptance is supplied. Verify exact standards claims for the applicable edition before use.

## Assurance Framework

The Smart Infusion Pump System follows a dual regulatory assurance framework:

1. **FDA premarket pathway (510(k) working assumption)**: Current QMSR design/development under 21 CFR 820.10(c) and ISO 13485:2016 with design input, design output, design review, design verification, design validation, and design transfer as the primary lifecycle gates.
2. **EU MDR Class IIb**: Technical documentation per Annex II and Annex III, with conformity assessment by a Notified Body under EU MDR 2017/745.

Both pathways reference ISO 14971 for risk management and IEC 62304 for software lifecycle. The evidence package is structured to serve both regulatory bodies without duplication: each artifact is authored once and mapped to both the FDA design control waterfall and the EU MDR Annex structure.

**Design Control Waterfall (FDA):**

| Gate              | Purpose                                                                | Key Evidence                                                           |
|-------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|
| Design Input      | Requirements established from user needs, risk controls, and regulatory requirements | System requirements, software requirements, risk management plan |
| Design Output     | Architecture and design documents that satisfy design inputs            | Architecture description, software design, SOUP evaluation             |
| Design Review     | Independent review of design artifacts at defined milestones           | Design review meeting records, action item closures                    |
| Design Verification | Objective evidence that design outputs meet design inputs            | Test reports, analysis reports, inspection records                     |
| Design Validation | Objective evidence that the device meets user needs and intended uses  | Usability validation, clinical performance evidence, simulated use test |
| Design Transfer   | Documented procedures for production release                           | Manufacturing specifications, acceptance test procedures, DHF index    |

## Evidence Lifecycle States

| State | Meaning |
| --- | --- |
| Planned | Record/activity identified; no executed result supplied |
| Drafted | Actual draft record exists |
| Executed | Actual procedure result and configuration exist |
| Reviewed | Identified reviewer and disposition recorded |
| Accepted | Authorized acceptance record exists |
| Baselined | Identified configuration is controlled; does not imply execution or acceptance |

All indexed artifact paths below are proposed and absent from this repository.
Their status is Planned. The Markdown teaching baseline is not an accepted QMS record.

## Evidence Index

| EVD ID   | Artifact Name                                         | Location                                               | Demonstrates                                                         | Standard Clause                     | Review Milestone       | Evidence Consumer              | Status   |
|----------|-------------------------------------------------------|--------------------------------------------------------|----------------------------------------------------------------------|-------------------------------------|------------------------|--------------------------------|----------|
| EVD-001  | Infusion Delivery Verification Test Report            | evidence/test-reports/infusion-delivery-verification.pdf | Flow rate accuracy, volume tracking, closed-loop control, trumpet curve compliance | IEC 60601-2-24 (exact applicability to verify); IEC 62304 (exact applicability to verify) | Design Verification | FDA reviewer; Notified Body | Planned |
| EVD-002  | Safety Mechanism Test Report                          | evidence/test-reports/safety-mechanism-test.pdf         | Anti-free-flow clamp engagement, hardware rate limiter, door sensor, safe state transition | IEC 60601-2-24 (exact applicability to verify); ISO 14971 (exact applicability to verify) | Design Verification | FDA reviewer; Notified Body | Planned |
| EVD-003  | DERS Verification Test Report                         | evidence/test-reports/ders-verification.pdf             | Soft limit alerting, hard limit enforcement, bolus checking, override logging, UI workflow DERS gate | IEC 62304 (exact applicability to verify); FDA DERS guidance | Design Verification | FDA reviewer; Notified Body | Planned |
| EVD-004  | Alarm System Test Report                              | evidence/test-reports/alarm-system-test.pdf             | Occlusion detection timing, air-in-line detection, alarm signal characteristics, upstream occlusion | IEC 60601-1-8; IEC 60601-2-24 (exact applicability to verify) | Design Verification | FDA reviewer; Notified Body | Planned |
| EVD-005  | Processor Safety Mechanism Test Report                | evidence/test-reports/processor-safety-test.pdf         | Watchdog timeout and reset, safe state transition timing, fault injection results | IEC 62304 (exact applicability to verify); ISO 14971 (exact applicability to verify) | Design Verification | FDA reviewer; Notified Body | Planned |
| EVD-006  | Alarm Annunciator Independence Test Report            | evidence/test-reports/alarm-independence-test.pdf       | Alarm function during display failure, alarm signal compliance per IEC 60601-1-8 | IEC 60601-1-8 (exact applicability to verify) | Design Verification | FDA reviewer; Notified Body | Planned |
| EVD-007  | Drug Library Management Test Report                   | evidence/test-reports/drug-library-management.pdf       | Library integrity verification, library activation control, library capacity | IEC 62304 (exact applicability to verify); FDA premarket cybersecurity | Design Verification | FDA reviewer; Notified Body | Planned |
| EVD-008  | Degraded Mode and Display Test Report                 | evidence/test-reports/degraded-mode-display.pdf         | Flow sensor loss fallback, display content verification, data integrity | IEC 62304 (exact applicability to verify) | Design Verification | FDA reviewer; Notified Body | Planned |
| EVD-009  | Self-Test and Power-Up Verification Report            | evidence/test-reports/self-test-powerup.pdf             | Self-test coverage, power-up timing, sensor verification completeness | IEC 60601-1 (exact applicability to verify); IEC 62304 (exact applicability to verify) | Design Verification | FDA reviewer; Notified Body | Planned |
| EVD-010  | Cybersecurity Verification Test Report                | evidence/test-reports/cybersecurity-verification.pdf    | TLS encryption, Wi-Fi authentication, RTOS partition isolation, MCB input validation, network independence | FDA premarket cybersecurity guidance; IEC 62443-4-1 | Design Verification | FDA reviewer; Notified Body | Planned |
| EVD-011  | Battery and Power Management Test Report              | evidence/test-reports/battery-power-test.pdf            | Battery runtime endurance, power interruption recovery, battery alarm thresholds | IEC 60601-1 (exact applicability to verify) | Design Verification | FDA reviewer; Notified Body | Planned |
| EVD-012  | Usability Validation Test Report                      | evidence/test-reports/usability-validation.pdf          | Touch response, infusion programming workflow, alarm response, use-related risk analysis | IEC 62366-1; FDA human factors guidance | Design Validation | FDA reviewer; Notified Body | Planned |
| EVD-013  | EHR Integration and Communication Test Report         | evidence/test-reports/ehr-integration-test.pdf          | HL7/FHIR message exchange, drug order reception, alarm forwarding latency | IEC 80001-1; HL7 conformance | Design Verification | FDA reviewer; Notified Body | Planned |
| EVD-014  | Environmental and EMC Test Report                     | evidence/test-reports/environmental-emc.pdf             | Power consumption, temperature operating range, EMC per IEC 60601-1-2 | IEC 60601-1-2; IEC 60601-1 (exact applicability to verify) | Design Verification | FDA reviewer; Notified Body | Planned |
| EVD-015  | Risk Management Report                                | evidence/safety/risk-management-report.pdf              | ISO 14971 risk management process completion, residual risk acceptability, overall residual risk evaluation | ISO 14971 (exact applicability to verify) | Design Review | FDA reviewer; Notified Body | Planned |
| EVD-016  | Software Development Plan                             | evidence/plans/software-development-plan.pdf            | IEC 62304 lifecycle planning, Table A.1 applicability, SOUP identification, safety classification | IEC 62304 (exact applicability to verify) | Design Input | FDA reviewer; Notified Body | Planned |
| EVD-017  | Software Requirements Specification                   | evidence/development/software-requirements.pdf          | Software requirements derived from system requirements and risk controls | IEC 62304 (exact applicability to verify) | Design Input | FDA reviewer; Notified Body | Planned |
| EVD-018  | Software Architecture Description                     | evidence/development/software-architecture.pdf          | Software architecture, partition design, SOUP integration, safety class allocation | IEC 62304 (exact applicability to verify) | Design Output | FDA reviewer; Notified Body | Planned |
| EVD-019  | Software Detailed Design                              | evidence/development/software-detailed-design.pdf       | Unit-level design for Class C components (infusion control, DERS, alarm management) | IEC 62304 (exact applicability to verify) | Design Output | FDA reviewer; Notified Body | Planned |
| EVD-020  | SOUP Evaluation Report                                | evidence/development/soup-evaluation.pdf                | SOUP identification, functional requirements, known anomaly evaluation, risk impact assessment | IEC 62304 (exact applicability to verify) | Design Review | FDA reviewer; Notified Body | Planned |
| EVD-021  | Design History File (DHF) Index                       | evidence/dhf/dhf-index.pdf                              | Complete index of all design control artifacts with version, date, and review status | 21 CFR 820.10(c) / ISO 13485 (exact applicability to verify); QMSR | Design Transfer | FDA reviewer | Planned |
| EVD-022  | System Requirements Specification                     | evidence/development/system-requirements.pdf            | System-level requirements with full record schema (this document is the controlled version) | 21 CFR 820.10(c) / ISO 13485 (exact applicability to verify); IEC 62304 (exact applicability to verify) | Design Input | FDA reviewer; Notified Body | Planned |
| EVD-023  | Simulated Use Validation Report                       | evidence/test-reports/simulated-use-validation.pdf      | Device meets user needs under simulated clinical conditions; use-related risk mitigation confirmed | IEC 62366-1; 21 CFR 820.10(c) / ISO 13485 (exact applicability to verify) | Design Validation | FDA reviewer; Notified Body | Planned |
| EVD-024  | Post-Market Surveillance Plan                         | evidence/plans/post-market-surveillance-plan.pdf        | DERS override trend monitoring, MAUDE complaint review, SOUP anomaly monitoring, field safety corrective action process | EU MDR Article 83; 21 CFR 803 | Design Transfer | Notified Body; FDA | Planned |
| EVD-025  | Configuration Management Plan                         | evidence/plans/configuration-management-plan.pdf        | CM procedures for software, hardware, SOUP, drug library, and documentation baselines | IEC 62304 (exact applicability to verify); ISO 13485 (exact applicability to verify) | Design Input | FDA reviewer; Notified Body | Planned |

## FDA Design Control Mapping

This section maps the evidence artifacts to the proposed design/development record structure. Current design/development requirements are in 21 CFR 820.10(c), incorporating ISO 13485 (exact applicability to verify); the old 820.30 phases below are historical labels, not current clause citations.

| Design Control Phase | Current design/development basis | Required Evidence                                            | EVD ID(s)                          | Status    |
|----------------------|----------------------|--------------------------------------------------------------|------------------------------------|-----------|
| Design Input         | 21 CFR 820.10(c) / ISO 13485 (exact applicability to verify)            | System and software requirements, risk management plan       | EVD-016, EVD-017, EVD-022          | Planned |
| Design Output        | 21 CFR 820.10(c) / ISO 13485 (exact applicability to verify)            | Architecture, detailed design, SOUP evaluation               | EVD-018, EVD-019, EVD-020          | Planned |
| Design Review        | 21 CFR 820.10(c) / ISO 13485 (exact applicability to verify)            | Risk management report, design review records                | EVD-015                            | Planned |
| Design Verification  | 21 CFR 820.10(c) / ISO 13485 (exact applicability to verify)            | Test reports demonstrating outputs meet inputs               | EVD-001 through EVD-014            | Planned   |
| Design Validation    | 21 CFR 820.10(c) / ISO 13485 (exact applicability to verify)            | Usability validation, simulated use testing                  | EVD-012, EVD-023                   | Planned   |
| Design Transfer      | 21 CFR 820.10(c) / ISO 13485 (exact applicability to verify)            | DHF index, manufacturing specs, post-market plan             | EVD-021, EVD-024, EVD-025          | Planned |

## EU MDR Annex II / Annex III Mapping

This section maps the evidence artifacts to the EU MDR 2017/745 technical documentation requirements.

| Annex Section        | Requirement                                                    | EVD ID(s)                               | Status    |
|----------------------|----------------------------------------------------------------|-----------------------------------------|-----------|
| Annex II, Section 1  | Device description and specification                           | EVD-022 (system requirements), README.md | Planned |
| Annex II, Section 2  | Information supplied by the manufacturer (labeling, IFU)       | (external to this evidence set)         | Planned   |
| Annex II, Section 3  | Design and manufacturing information                           | EVD-018, EVD-019, EVD-025              | Planned |
| Annex II, Section 4  | General safety and performance requirements (GSPRs)            | EVD-015 (risk), EVD-001-014 (verification) | Planned |
| Annex II, Section 5  | Benefit-risk analysis and risk management                      | EVD-015                                 | Planned |
| Annex II, Section 6  | Product verification and validation                            | EVD-001-014 (verification), EVD-012/023 (validation) | Planned |
| Annex III, Section 1 | Post-market surveillance plan                                  | EVD-024                                 | Planned |
| Annex III, Section 3 | Post-market clinical follow-up plan                            | (external to this evidence set)         | Planned   |

## Software Lifecycle Evidence Plan

The overall software Class C is a teaching assumption. Any proposed lower-class
subsystem needs risk and segregation rationale against the adopted IEC 62304 edition;
no class reduction is established by this example. Exact clauses and class-specific
obligations require a licensed-source review.

| Proposed work | Evidence IDs | Scope / open decision |
| --- | --- | --- |
| Development planning | EVD-016 | Process, resources, configuration, and classification rationale |
| Requirements and architecture | EVD-017, EVD-018 | Risk-control allocation and interface behavior |
| Detailed design and unit verification | EVD-019 and associated procedures | Infusion control, DERS, alarm, display; exact applicability to verify |
| Integration/system verification | EVD-001 through EVD-014 | Normal, boundary, fault, and recovery conditions |
| SOUP assessment | EVD-020 | RTOS, TCP/IP, TLS; versions/supplier/anomalies not established |
| Configuration/change/problem resolution | EVD-024, EVD-025 | Actual records, regression scope, and release disposition are planned |

## SOUP Evidence Requirements

The proposed SOUP evidence plan covers these application-specific records. Verify exact requirements in the applicable IEC 62304 edition and current FDA guidance:

| SOUP ID  | CMP ID      | Evidence Required                                                          | EVD ID   | Status  |
|----------|-------------|----------------------------------------------------------------------------|----------|---------|
| SOUP-001 | CMP-MCB-01E | Functional requirements, known anomaly evaluation, risk impact assessment  | EVD-020  | Planned |
| SOUP-002 | CMP-MCB-01F | Functional requirements, known anomaly evaluation (CVE review), risk impact | EVD-020  | Planned |
| SOUP-003 | CMP-MCB-01G | Functional requirements, known anomaly evaluation (CVE review), risk impact | EVD-020  | Planned |

**SOUP anomaly monitoring process:**
The proposed post-market plan (EVD-024) would include periodic review of the following; cadence is a project decision needing justification:
- Vendor errata lists for SOUP-001 (RTOS)
- CVE databases (NVD, vendor-specific) for SOUP-002 (TCP/IP) and SOUP-003 (TLS)
- Impact assessment of new anomalies on the device risk profile
- Patch/update evaluation and deployment timeline

## Post-Market Surveillance Evidence

| Activity                          | Data Source                           | Frequency    | EVD ID   |
|-----------------------------------|---------------------------------------|--------------|----------|
| DERS override trend monitoring    | Pump fleet override logs (aggregated) | Monthly      | EVD-024  |
| MAUDE complaint review            | FDA MAUDE database                    | Quarterly    | EVD-024  |
| SOUP anomaly monitoring           | Vendor errata, CVE databases          | Quarterly    | EVD-024  |
| Field safety corrective actions   | Quality system CAPA process           | As needed    | EVD-024  |
| Post-market clinical follow-up    | Clinical literature review            | Annually     | EVD-024  |
| Drug library effectiveness review | Override data + pharmacy feedback     | Semi-annually | EVD-024  |
