# Cybersecurity Analysis

## Applicable Framework

This cybersecurity analysis follows ISO/SAE 21434 (Road Vehicles -- Cybersecurity Engineering). The Threat Analysis and Risk Assessment (TARA) identifies cybersecurity-relevant assets within the AEB system boundary, characterizes attack paths, assesses attack feasibility using the attack potential approach (elapsed time, expertise, knowledge, window of opportunity, equipment), and allocates security requirements alongside safety requirements per ISO 26262.

The analysis scope covers all operating modes (MODE-001 through MODE-005) with emphasis on the OTA update interface (IFC-EXT-007), the CAN FD braking domain (IFC-INT-004/005), the Automotive Ethernet domain (IFC-INT-003/006), and the diagnostic interface (IFC-EXT-009).

## Asset Identification

| AST ID   | Asset Name                                 | CMP ID(s)                           | C   | I   | A   | Safety Relevance (HZ ID)        |
|----------|--------------------------------------------|-------------------------------------|-----|-----|-----|---------------------------------|
| AST-001  | Perception DNN Model and Fusion Parameters | CMP-PER-01E, CMP-PER-01G           | Low | High| High| HZ-001, HZ-002 (missed detection if model corrupted) |
| AST-002  | Braking Command Messages (CAN FD)          | CMP-BRK-01D, CMP-GWY-01D           | Low | High| High| HZ-010 (unauthorized braking via injection) |
| AST-003  | OTA Update Packages                        | CMP-PER-01J, CMP-GWY-01E           | Low | High| High| HZ-009 (disabled AEB via corrupted update) |
| AST-004  | Perception ECU Application Software        | CMP-PER-01D/E/F/G/H                | Low | High| High| HZ-001, HZ-009 (all perception failures from SW tampering) |
| AST-005  | E2E Protection Keys and Counters           | CMP-BRK-01C, CMP-GWY-01C           | High| High| Medium | HZ-010 (E2E bypass enables injection) |
| AST-006  | Sensor Calibration Parameters              | CMP-PER-01E, CMP-PER-01F           | Low | High| Low | HZ-001 (incorrect calibration degrades detection) |
| AST-007  | Event Data Records                         | CMP-PER-01K                         | High| High| Low | No direct safety impact; forensic/legal relevance |
| AST-008  | Diagnostic Session Credentials             | CMP-GWY-01C, CMP-BRK-01C           | High| High| Low | HZ-009, HZ-010 (unauthorized diagnostic access) |

**C/I/A Rating Scale**: High = compromise directly enables a safety-relevant failure condition; Medium = compromise enables a precondition for a safety-relevant failure; Low = compromise has operational but not direct safety impact.

## Threat Analysis

### ISO 21434 TARA

| THR ID   | Threat Scenario                                                         | Attack Path                                                                    | AST ID(s)        | Feasibility     | Impact   | Risk   | HZ ID(s)        |
|----------|-------------------------------------------------------------------------|--------------------------------------------------------------------------------|------------------|-----------------|----------|--------|-----------------|
| THR-001  | Malicious OTA update replaces DNN model with adversarial model          | Compromise OTA backend or MITM on TCU-to-ECU path; deliver signed package with attacker's signing key or exploit key compromise | AST-003, AST-004 | Low (High effort) | High    | Medium | HZ-009, HZ-001  |
| THR-002  | OTA update replay attack installs outdated vulnerable software          | Capture legitimate update package; replay after rollback vulnerability patched  | AST-003          | Medium          | High     | Medium | HZ-009           |
| THR-003  | CAN FD message injection: forged brake command                          | Physical access to CAN FD bus (OBD-II port, aftermarket device); inject spoofed brake command frame | AST-002          | Medium          | High     | High   | HZ-010           |
| THR-004  | CAN FD message injection: disable AEB by spoofing sensor status         | Inject fault-status messages for camera/radar on CAN FD; trigger MODE-003 transition | AST-002      | Medium          | Medium   | Medium | HZ-008           |
| THR-005  | Automotive Ethernet SOME/IP injection between Perception and Gateway    | Compromise a device on the Ethernet domain; inject SOME/IP service messages mimicking Perception ECU output | AST-002, AST-005 | Low (High effort) | High | Medium | HZ-010, HZ-003  |
| THR-006  | Diagnostic session hijacking via UDS over CAN                           | Physical access to OBD-II; initiate diagnostic session; write calibration or disable DTC | AST-008, AST-006 | Medium      | Medium   | Medium | HZ-001, HZ-008  |
| THR-007  | Sensor spoofing: radar jamming or GPS relay attack                      | Dedicated RF equipment in proximity to vehicle; jam 77 GHz radar or spoof GPS signals | AST-001      | Low (specialized equipment) | Medium | Low  | HZ-011           |
| THR-008  | Supply chain attack: malicious code in Perception ECU firmware          | Compromise supplier build environment or component supply chain               | AST-004          | Low (nation-state) | High   | Medium | HZ-001, HZ-009  |

### Attack Feasibility Assessment (Attack Potential Approach)

| THR ID | Elapsed Time | Expertise    | Knowledge of Item | Window of Opportunity | Equipment     | Total AP | Feasibility |
|--------|-------------|--------------|-------------------|-----------------------|---------------|----------|-------------|
| THR-001| > 6 months  | Expert       | Critical          | Difficult             | Bespoke       | 31+      | Low         |
| THR-002| < 1 month   | Proficient   | Restricted        | Easy                  | Standard      | 14       | Medium      |
| THR-003| < 1 week    | Proficient   | Public            | Easy (OBD-II)         | Standard      | 10       | Medium      |
| THR-004| < 1 week    | Proficient   | Restricted        | Easy (OBD-II)         | Standard      | 12       | Medium      |
| THR-005| > 6 months  | Expert       | Critical          | Difficult             | Specialized   | 28       | Low         |
| THR-006| < 1 month   | Competent    | Restricted        | Easy (OBD-II)         | Standard      | 11       | Medium      |
| THR-007| < 1 month   | Expert       | Public            | Moderate              | Bespoke       | 22       | Low         |
| THR-008| > 6 months  | Multiple experts | Critical      | Difficult             | Bespoke       | 35+      | Low         |

## Security Requirements

Security requirements are listed here for context with their threat linkage. The canonical record for all requirements is in requirements.md.

| REQ ID       | Statement                                                                                              | THR ID(s)          | CTL ID(s) | Verification |
|--------------|--------------------------------------------------------------------------------------------------------|--------------------|-----------|--------------|
| REQ-SEC-001  | The AEB system shall verify the cryptographic signature of all OTA update packages before installation using asymmetric key verification (ECDSA P-256 or equivalent). | THR-001, THR-002 | CTL-009  | Test         |
| REQ-SEC-002  | The OTA update agent shall reject update packages with a version number equal to or lower than the currently installed version (anti-rollback). | THR-002            | CTL-009   | Test         |
| REQ-SEC-003  | The Vehicle Gateway ECU shall implement CAN FD message filtering based on a static allowlist of permitted message IDs, source addresses, and message rates. | THR-003, THR-004 | CTL-010  | Test         |
| REQ-SEC-004  | All safety-relevant CAN FD messages between the Vehicle Gateway ECU and Braking Control ECU shall be protected with AUTOSAR E2E Profile 7 (CRC-64 + rolling counter). | THR-003, THR-005 | CTL-010  | Test         |
| REQ-SEC-005  | The Vehicle Gateway ECU shall implement an intrusion detection system (IDS) that detects anomalous CAN FD message patterns and logs security events. | THR-003, THR-004 | CTL-010  | Test         |
| REQ-SEC-006  | The AEB system shall require security access (ISO 14229 service 0x27) with challenge-response authentication before allowing diagnostic write operations to safety-relevant parameters. | THR-006 | —       | Test         |
| REQ-SEC-007  | The Perception ECU shall store the DNN model and fusion parameters in a secure boot partition with hardware-enforced integrity verification on each power cycle. | THR-001, THR-008 | CTL-009  | Test         |

### Additional Security Controls (not in requirements.md scope)

These controls are procedural or environmental and are documented here for the security evidence package:

| Control ID (Security) | Description                                                                         | THR ID(s)      |
|-----------------------|-------------------------------------------------------------------------------------|----------------|
| SC-001                | OTA update backend uses HSM-protected signing keys with dual-control access         | THR-001        |
| SC-002                | Supply chain integrity: signed firmware images from Tier-1 supplier with certificate chain | THR-008  |
| SC-003                | OBD-II port access restricted to authorized personnel in service environments       | THR-003, THR-006 |
| SC-004                | Ethernet domain uses MACsec (IEEE 802.1AE) for link-layer encryption between Perception ECU and Gateway | THR-005 |
| SC-005                | Secure debug ports (JTAG) are permanently disabled on production ECUs via hardware fuses | THR-008   |

## Security-Safety Interaction

| THR ID   | Attack Consequence                                                 | HZ ID   | Combined Risk | Mitigation Strategy                                                                         |
|----------|--------------------------------------------------------------------|---------|---------------|---------------------------------------------------------------------------------------------|
| THR-001  | Replaced DNN model causes systematic missed detections              | HZ-009  | High          | Cryptographic signature verification (REQ-SEC-001) + secure boot (REQ-SEC-007) + rollback (REQ-SEC-002) |
| THR-002  | Outdated software reintroduces patched SOTIF vulnerability          | HZ-009  | Medium        | Anti-rollback version check (REQ-SEC-002) + cryptographic verification (REQ-SEC-001)        |
| THR-003  | Injected brake command causes unauthorized deceleration             | HZ-010  | High          | E2E protection (REQ-SEC-004) + CAN firewall (REQ-SEC-003) + IDS (REQ-SEC-005)              |
| THR-004  | Spoofed sensor fault status disables AEB unnecessarily              | HZ-008  | Medium        | CAN firewall (REQ-SEC-003) + E2E protection (REQ-SEC-004) + sensor-level health monitoring (CTL-008) |
| THR-005  | SOME/IP injection modifies perception output on Ethernet domain     | HZ-010  | Medium        | MACsec link-layer encryption (SC-004) + E2E protection across gateway (REQ-SEC-004)         |
| THR-006  | Diagnostic session used to disable AEB or modify calibration        | HZ-001  | Medium        | Security access authentication (REQ-SEC-006) + OBD-II physical access restriction (SC-003)  |
| THR-007  | Radar jamming causes SOTIF-like degradation                         | HZ-011  | Low           | Sensor health monitoring (CTL-008) + SOTIF-aware degradation (CTL-011) + camera compensation (CTL-001) |
| THR-008  | Supply chain compromise embeds malicious code in production firmware | HZ-001  | Medium        | Secure boot (REQ-SEC-007) + supply chain signing (SC-002) + JTAG disable (SC-005)           |

### Security-Safety Boundary Analysis

The primary security-safety boundary is at the **Vehicle Gateway ECU** (CMP-GWY-01), which separates:

1. **Ethernet domain** (Perception ECU, OTA path) from **CAN FD safety domain** (Braking Control ECU, ESC, powertrain).
2. **External interfaces** (OTA via TCU, diagnostic via OBD-II, V2X) from **internal safety-critical communication**.

The Gateway enforces:
- **CAN FD message allowlist** (CMP-GWY-01E) filtering all messages crossing from Ethernet to CAN FD domain.
- **E2E protection continuity** across protocol translation: SOME/IP E2E on Ethernet is verified and re-wrapped as CAN FD E2E Profile 7.
- **Rate limiting** on diagnostic and V2X message paths to prevent denial-of-service propagation to the braking domain.
- **VLAN isolation** of OTA update traffic from safety-critical SOME/IP traffic on the Ethernet domain.

The secondary security boundary is at the **Perception ECU secure boot chain**, which ensures:
- Application software integrity is verified on each power cycle using hardware root of trust.
- DNN model integrity is verified before loading into NPU memory.
- OTA updates are cryptographically validated before replacing the active software partition.

These boundaries map directly to the freedom-from-interference arguments in the architecture (architecture.md) and the sensor health monitoring controls in the hazard analysis (hazard-analysis.md).
