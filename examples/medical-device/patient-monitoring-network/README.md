# Patient Monitoring Network

## Overview

The Patient Monitoring Network is a multi-parameter bedside monitoring system with central station aggregation for acute care environments. Each bedside monitor acquires physiological signals including pulse oximetry (SpO2), electrocardiography (ECG, 3/5/12-lead), non-invasive blood pressure (NIBP), body temperature, and sidestream capnography (EtCO2). Bedside monitors transmit physiological data and alarm events over a dedicated medical-grade network to a central station that displays up to 32 patients simultaneously, manages alarm escalation, and interfaces with the hospital EMR and nurse call systems. The system implements IEC 60601-1-8 alarm management with configurable alarm limits, alarm delay, and alarm escalation to reduce alarm fatigue while preserving clinically significant notifications. Network risk management follows IEC 80001-1. The system is classified FDA Class II (510(k)) and EU MDR Class IIa.

## System Boundary

**Inside the system boundary:**
- Bedside monitors: parameter acquisition modules (SpO2, ECG, NIBP, temp, EtCO2), bedside display, local alarm annunciator, bedside processor, network interface
- Central station: multi-patient display, alarm aggregation and escalation engine, nurse assignment management, trending and event review, network server
- Medical-grade network: dedicated Ethernet switches, cabling, and network infrastructure connecting bedside monitors to the central station
- Gateway server: protocol translation between the monitoring network and hospital systems (EMR, nurse call, ADT)

**Outside the system boundary:**
- Patient sensors and accessories (SpO2 finger clips, ECG leads, NIBP cuffs, temperature probes, EtCO2 sampling lines — disposable/reusable, supplied separately)
- Hospital IT network infrastructure (beyond the dedicated monitoring network segment)
- Electronic Medical Record system (receives data via gateway)
- Nurse call system (receives alarm escalation via gateway)
- ADT (Admission-Discharge-Transfer) system (provides patient demographics)
- Bedside mount / rail clamp hardware

## Operational Environment

The system operates in acute care settings including intensive care units, step-down units, telemetry floors, and post-anesthesia care units. Bedside monitors operate at 10C to 40C, 20% to 80% RH (non-condensing). The dedicated monitoring network uses shielded Ethernet cabling with medical-grade isolation transformers. The central station is located in a nursing station with continuous staff presence. Network latency between any bedside monitor and the central station must not exceed the alarm notification budget.

## Operating Modes

| Mode ID   | Name               | Description                                                                    | Active Functions                                         | Constraints                                          |
|-----------|--------------------|--------------------------------------------------------------------------------|----------------------------------------------------------|------------------------------------------------------|
| MODE-001  | Full Monitoring    | All parameters active, central station connected, alarms enabled               | All FUN- functions active                                | All sensors connected; network operational            |
| MODE-002  | Transport          | Bedside monitor operating on battery during patient transport; local alarms only | FUN-ACQ-01, FUN-ALM-01 (local), FUN-LOG-01             | No central station link; battery limited (2 hr min)   |
| MODE-003  | Standby            | Monitor powered on, no patient connected; awaiting sensor attachment            | FUN-NET-01 (network presence), FUN-ADT-01               | No physiological monitoring; no alarms                |
| MODE-004  | Network Degraded   | Bedside monitoring continues; central station link impaired or lost            | FUN-ACQ-01, FUN-ALM-01 (local), FUN-LOG-01              | Local alarms only; no central alarm forwarding        |

## Key Technical Challenges

1. **Alarm fatigue reduction without missing clinically significant events.** Studies report that over 85% of clinical alarms are non-actionable, causing alarm fatigue that leads clinicians to silence, ignore, or disable alarms — including genuine emergencies. The alarm management system must implement intelligent alarm delay, adaptive thresholds, and multi-parameter correlation to reduce nuisance alarms while maintaining sensitivity for true clinical deterioration events per IEC 60601-1-8 alarm priority categories.

2. **Alarm latency budget from bedside to central station.** IEC 60601-1-8 defines alarm signal generation timing requirements. The end-to-end latency from physiological event detection at the bedside to alarm annunciation at the central station must be bounded and verifiable. The latency budget must account for sensor processing time, bedside alarm detection, network transmission, central station alarm aggregation, and display rendering.

3. **Network risk management per IEC 80001-1.** Incorporating medical devices into a health IT network introduces risks not present in standalone operation. The dedicated monitoring network must be analyzed per IEC 80001-1 for safety, effectiveness, and data security risks introduced by network connectivity, including network failure, congestion, unauthorized access, and data corruption.

4. **Multi-parameter correlation for clinical decision support.** Combining SpO2 desaturation with heart rate, respiratory rate (derived from ECG and EtCO2), and blood pressure trends enables early warning scores that detect patient deterioration before single-parameter alarms trigger. The correlation algorithms must be validated against clinical outcomes data.

## Stakeholders

| Stakeholder                    | Role                                                                              |
|--------------------------------|-----------------------------------------------------------------------------------|
| Bedside nurse                  | Primary clinical user; responds to alarms, interprets trends, adjusts parameters  |
| Central station monitor tech   | Monitors multi-patient display; escalates alarms when bedside response is delayed |
| Patient                        | Subject of monitoring; affected by missed alarms or alarm fatigue consequences    |
| Biomedical engineering          | Installs, configures, and maintains the monitoring network and devices            |
| Hospital IT / network admin    | Manages network infrastructure; responsible for IEC 80001-1 network risk management |
| FDA (CDRH)                     | Reviews 510(k) for multi-parameter monitoring system                              |

## Standards Applicability

| Standard            | Applicability                                                                                   |
|---------------------|-------------------------------------------------------------------------------------------------|
| IEC 62304           | Software lifecycle for Class B embedded software (bedside and central station)                  |
| ISO 14971           | Risk management across full product lifecycle including networked operation                      |
| IEC 60601-1         | General safety and essential performance; Type BF/CF applied parts (ECG, SpO2)                  |
| IEC 60601-1-8       | Alarm systems: alarm priority assignment, alarm signal characteristics, distributed alarm management |
| IEC 80001-1         | Health IT network risk management for the dedicated monitoring network segment                   |
