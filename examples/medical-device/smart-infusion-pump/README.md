# Smart Infusion Pump System

## Overview

The Smart Infusion Pump System is a large-volume infusion pump designed for intravenous fluid and medication delivery in acute care settings. The system delivers fluids at programmable rates from 0.1 to 999 mL/hr with dose error reduction software (DERS) that cross-checks programmed infusion parameters against a hospital-customizable drug library containing 2000+ drug entries. The DERS function intercepts dose orders that fall outside institution-defined concentration, dose, and rate limits, requiring clinician override acknowledgment before the pump will deliver outside soft limits and preventing delivery entirely for hard limit violations.

The system connects to hospital networks via Wi-Fi (802.11ac) for electronic health record (EHR) integration, drug library updates, and alarm notification forwarding. The architecture comprises four subsystems: a Pump Mechanism Assembly (PMA) providing the physical fluid delivery mechanism, a Main Control Board (MCB) executing infusion control algorithms and DERS logic, a User Interface Module (UIM) providing touchscreen interaction and alarm annunciation, and a Wireless Communication Module (WCM) managing network connectivity and data exchange with hospital information systems.

The pump is classified as FDA Class III requiring premarket approval (PMA) under 21 CFR 876.5820 and as EU MDR Class IIb under Rule 11 (active therapeutic devices delivering energy or substances). The embedded software is classified IEC 62304 Class C because software failure can contribute to hazardous situations resulting in serious injury or death through over-infusion, under-infusion, or undetected free-flow conditions. Risk management follows ISO 14971 across the full product lifecycle.

## System Boundary

**Inside the system boundary:**
- Pump Mechanism Assembly (PMA): peristaltic pump head, anti-free-flow clamp, flow sensor, occlusion pressure sensor, door latch sensor, air-in-line detector
- Main Control Board (MCB): main processor, infusion control application, DERS engine, alarm management, RTOS, SOUP components (TCP/IP stack, TLS library)
- User Interface Module (UIM): touchscreen display, piezoelectric alarm buzzer, LED status indicators, capacitive touch controller
- Wireless Communication Module (WCM): Wi-Fi radio, antenna, network protocol stack, EHR interface application, drug library update manager
- Internal power management (battery charging, AC/DC conversion, battery monitoring)
- IV administration set interface (tubing cassette engagement mechanism)

**Outside the system boundary:**
- IV administration set and tubing (disposable, supplied separately)
- IV fluid containers and medications (drug products, not device components)
- Hospital network infrastructure (Wi-Fi access points, network switches, firewalls)
- Electronic Health Record system (receives infusion data, sends drug orders; separate system)
- Drug library authoring tool (pharmacy workstation software; creates libraries consumed by pump)
- IV pole and mounting hardware (mechanical support, not electronic)
- Central monitoring station (receives forwarded alarms; separate device)
- Biomedical engineering test equipment (external calibration and service tools)

## Operational Environment

The pump operates in acute care clinical settings including intensive care units, general medical/surgical wards, emergency departments, operating rooms, and ambulatory infusion centers. Environmental conditions span 10C to 40C ambient temperature, 20% to 80% relative humidity (non-condensing), and atmospheric pressure from 57 kPa to 106 kPa (equivalent to sea level through 4000 m altitude). The pump is designed for continuous operation (24/7) on AC mains power with battery backup providing a minimum of 2 hours of infusion at 125 mL/hr.

The pump interfaces with hospital Wi-Fi networks operating on 2.4 GHz and 5 GHz bands. Electromagnetic compatibility is demonstrated per IEC 60601-1-2 for the intended use environment, including immunity to electrostatic discharge, radiated RF fields, and conducted disturbances typical of clinical settings with multiple active medical devices.

## Operating Modes

| Mode ID   | Name               | Description                                                         | Active Functions                                  | Constraints                                          |
|-----------|--------------------|---------------------------------------------------------------------|---------------------------------------------------|------------------------------------------------------|
| MODE-001  | Normal Infusion    | Continuous delivery at programmed rate with DERS active             | All FUN- functions active; DERS checking enabled  | Rate within drug library limits; IV set loaded        |
| MODE-002  | Bolus Mode         | Clinician-initiated bolus delivery at elevated rate                 | FUN-INF-01, FUN-INF-02, FUN-DRS-01, FUN-ALM-01   | Bolus volume and rate within hard limits; time-limited |
| MODE-003  | KVO                | Keep Vein Open at minimum rate after primary infusion completes     | FUN-INF-01, FUN-ALM-01, FUN-MON-01               | Fixed low rate (typically 1-5 mL/hr); alarm annunciated |
| MODE-004  | Alarm/Pause        | Infusion paused due to alarm condition; pump mechanism stopped      | FUN-ALM-01, FUN-MON-01, FUN-COM-01 (alarm forwarding) | No fluid delivery; clinician intervention required    |
| MODE-005  | Standby/Setup      | Pump powered on, no active infusion; programming and configuration  | FUN-DRS-01, FUN-COM-01 (library update), FUN-UIF-01 | No fluid delivery; drug library load permitted        |

Mode IDs are referenced by hazard-analysis.md, requirements.md, and traceability.md.

## Key Technical Challenges

1. **Dose error reduction effectiveness vs. alert fatigue.** The DERS must intercept clinically significant dose errors while maintaining an override rate low enough that clinicians do not develop alert fatigue and begin overriding all warnings reflexively. Drug library tuning must balance sensitivity (catching errors) against specificity (minimizing false positives), and the system must log override patterns to support post-market surveillance of library effectiveness.

2. **Free-flow prevention across all failure modes.** Uncontrolled gravity-driven free-flow is the single most dangerous failure mode of an infusion pump, capable of delivering a fatal bolus within minutes. The anti-free-flow mechanism must engage reliably when the IV set is removed from the pump, when the pump door is opened during infusion, and when the pump mechanism itself fails. The safety argument must address mechanical, electrical, and software failure paths to free-flow.

3. **Software safety classification and SOUP risk management.** The infusion control software is IEC 62304 Class C, requiring full lifecycle evidence including detailed design and unit verification. The system uses three SOUP components (RTOS, TCP/IP stack, TLS library) that must each be evaluated for known anomalies, and the risk management process must demonstrate that SOUP failures cannot lead to unmitigated hazardous situations. SOUP anomaly monitoring must be maintained through the product lifetime.

4. **Cybersecurity integration with safety.** The Wi-Fi interface creates an attack surface that connects the pump to hospital networks. Per FDA premarket cybersecurity guidance, the threat model must address unauthorized drug library modification, infusion parameter manipulation, and denial-of-service attacks that could delay alarm notification. Security controls must be evaluated for their own potential to introduce safety risks (e.g., authentication lockout preventing emergency drug delivery).

5. **Dual regulatory pathway alignment.** The system must simultaneously satisfy FDA PMA design control requirements (21 CFR 820.30 / QMSR) and EU MDR Annex II/III technical documentation requirements. The evidence package structure must serve both regulatory bodies without duplication, and the risk management file must satisfy both ISO 14971 (referenced by both pathways) and the specific expectations of FDA premarket reviewers regarding benefit-risk determination.

## Stakeholders

| Stakeholder                    | Role                                                                                 |
|--------------------------------|--------------------------------------------------------------------------------------|
| Clinician (nurse, physician)   | Primary operator; programs infusions, responds to alarms, manages drug delivery      |
| Patient                        | Receives infused medication; subject to harm from device malfunction                 |
| Pharmacist                     | Configures drug library parameters; reviews override logs for safety improvement     |
| Biomedical engineering         | Installs, maintains, calibrates, and services the pump; manages fleet configuration  |
| Hospital IT / network admin    | Manages Wi-Fi infrastructure, EHR integration, and network security for pump fleet   |
| FDA (CDRH)                     | Reviews PMA submission; conducts premarket inspections of the design history file     |
| EU Notified Body               | Assesses EU MDR conformity; audits technical documentation per Annex II/III          |
| Quality/Regulatory affairs     | Maintains QMS, manages design controls, coordinates submissions and audits           |

## Standards Applicability

| Standard            | Applicability                                                                                          |
|---------------------|--------------------------------------------------------------------------------------------------------|
| IEC 62304           | Software lifecycle for Class C safety-classified embedded software (MCB, UIM, WCM applications)        |
| ISO 14971           | Risk management process across full product lifecycle; risk file maintained as living document          |
| IEC 60601-1         | General safety and essential performance for medical electrical equipment; Type BF applied part         |
| IEC 60601-1-2       | Electromagnetic compatibility for intended use environment (acute care clinical setting)                |
| IEC 60601-2-24      | Particular requirements for infusion pumps and controllers; flow accuracy, alarm conditions             |
| FDA 21 CFR 820.30   | Design controls (design input, output, review, verification, validation, transfer); QMSR alignment    |
| EU MDR 2017/745     | Essential requirements (Annex I GSPRs); technical documentation (Annex II/III); Class IIb Rule 11     |
| IEC 62443-4-1       | Secure development lifecycle (referenced by FDA premarket cybersecurity guidance)                       |
| IEC 60601-1-8       | Alarm systems for medical electrical equipment; alarm priority and signal characteristics               |
| IEC 62366-1         | Usability engineering; use-related risk analysis and usability validation                               |
