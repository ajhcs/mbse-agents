# Medical-device analysis and review

Use the sections relevant to the device and decision. Verify exact obligations against the jurisdiction, current regulatory text, intended use, and applicable standards editions. A publication listing can identify a standard. Check the actual text for a clause-level claim.

## Intended use and classification

Establish indication, patient population, user, use environment, therapeutic/diagnostic role, connectivity, accessories, and degree of automation. These facts drive classification and evidence strategy. FDA product class, EU MDR class, IEC 62304 software class, and FDA software documentation level are different classifications and do not map automatically.

Identify the actual product code, regulatory pathway, intended-use boundaries, and applicable classification rules. [Pump classification](pump-classification.md) illustrates why product, software, and submission classifications must remain separate; it is a narrow example, not a classification rule for the whole domain.

## Risk and software lifecycle

Keep hazard, sequence of events, hazardous situation, and harm distinct. Trace each risk control into an implemented design or operational measure and its effectiveness evidence. Do not substitute a risk-priority number for the adopted risk acceptability and residual-risk process. Consider new risks caused by a control, use error, and overall residual risk.

Determine software safety classification from the software's possible contribution to harm, supported by risk analysis and the applicable IEC 62304 edition. Partitioning or external controls need a documented rationale; regulatory Class II does not imply software Class B.

For SOUP/OTS and suppliers, identify exact component/version/configuration, function, application requirements, known anomalies, risk impact, controls, and maintenance/monitoring responsibilities. A dependency list is insufficient. Distinguish IEC SOUP obligations and FDA documentation expectations; verify exact clauses and current guidance rather than guessing a lifecycle section number.

Tie software problem reports to changes, risk reassessment, regression verification, configuration, and release disposition. Trace critical behavior across HW/SW boundaries, including sensing, delivery control, alarms, degraded states, power loss, network failure, and update behavior.

## Quality, submission, and human use

FDA's [QMSR page](https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr) states that QMSR became effective on February 2, 2026 and incorporates ISO 13485:2016 into Part 820. Use current Part 820 and its retained FDA requirements. References to old 820.30 belong in historical crosswalks, not as current clause citations. ISO certification alone does not establish all FDA obligations.

Define controlled design/development, risk, verification, validation, transfer, change, supplier, and postmarket records. The model is a source for evidence only with identifiable configuration and extraction/review procedures. A mutable diagram is not an approved design record.

Select the current FDA software documentation framework and substantiate the choice. For EU MDR, connect GSPR applicability, Annex II technical documentation, Annex III postmarket work, clinical evaluation, and the conformity route to the device. Avoid treating an FDA record index and EU technical documentation as interchangeable.

Consider electrical safety, essential performance, EMC, particular device requirements, alarms, usability, and representative use validation. Choose IEC 60601/62366 and other applicability from the actual device and environment. Specify alarm priority, response timing, operator interpretation, and recovery, without inventing clinical thresholds.

Integrate cybersecurity with safety and lifecycle work: unauthorized configuration, malicious inputs, denial of service, authenticity of libraries/updates, monitoring, SBOM, vulnerability handling, and recovery. Determine current statutory and guidance applicability for the actual device; security measures can create a use or availability risk themselves.

## Artifact mappings and review

| Engineering thread | Proposed model content | Controlled evidence |
| --- | --- | --- |
| User need / intended use | Context and operational scenario | Confirmed use statement and validation |
| Risk-control requirement | Requirement and functional allocation | Implemented control and effectiveness test |
| SW behavior / SOUP | Components and HW/SW interfaces | Configuration, anomaly evaluation, verification |
| Human-system interaction | Mode, display/alarm, recovery flow | Use-related risk and usability evidence |
| Submission obligation | Applicability and record index | Current basis and controlled records |
| Change / field issue | Affected elements and trace | Risk reassessment, regression, release decision |

Use the project's Capella/SysML profile, requirements tool, and analysis tools to maintain consistent IDs and exports. Mappings are engineering proposals, not vendor-approved equivalences.

Before handoff, check whether the intended use supports each classification rationale. Trace the consequential hazardous situation through the implemented control, actual configuration, and test or use observation. Identify planned or incomplete records and any unverified alarm, delivery, or isolation assumptions that affect the conclusion.
