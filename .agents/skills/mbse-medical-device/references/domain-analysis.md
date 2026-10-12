# Medical-device analysis and review

This reference is engineering guidance. Exact requirements depend on jurisdiction, device intended use, applicable standards editions, and current regulatory text. Identify sources at the precision used and do not present a standard catalog as verification of its clauses.

## Intended use and classification

Establish indication, patient population, user, use environment, therapeutic/diagnostic role, connectivity, accessories, and degree of automation. These facts drive classification and evidence strategy. FDA product class, EU MDR class, IEC 62304 software class, and FDA software documentation level are different classifications and do not map automatically.

For an ordinary healthcare-facility infusion pump, [21 CFR 880.5725](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-880/subpart-F/section-880.5725) specifies Class II. [21 CFR 876.5820](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-876/subpart-F/section-876.5820) concerns hemodialysis, not general infusion pumps. Do not infer a PMA solely from patient risk or embedded software Class C. Confirm product code, system context, predicate and pathway for the actual device. Pumps submitted as part of a Class III system can differ: see FDA's [infusion-pump guidance](https://www.fda.gov/media/78369/download), section 3.

For EU classification, Rule 12 covers active administration/removal of substances; Rule 11 concerns software. MDCG 2021-24 Rev.1's Rule 12 table lists infusion pumps under IIb when administration is potentially hazardous. Software driving or influencing a device also needs implementing rule 3.3 considered. Check all applicable rules and exceptions against intended use; the example's class is a provisional rationale, not a notified-body decision. See [MDCG classification guidance](https://health.ec.europa.eu/system/files/2021-10/mdcg_2021-24_en_0.pdf), printed pages 47-48.

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

Review pressure points: incorrect intended-use classification; software/product class conflation; missing hazardous situation; SOUP without risk assessment; outdated clause citation; unverified control; unsupported alarm/flow claims; network isolation stated without resource evidence; planned records called accepted evidence.
