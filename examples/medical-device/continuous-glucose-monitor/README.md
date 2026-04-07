# Continuous Glucose Monitor

## Overview

The Continuous Glucose Monitor (CGM) is a wearable system that measures interstitial glucose levels every 1-5 minutes via a subcutaneous electrochemical sensor and transmits readings to a companion mobile application over Bluetooth Low Energy (BLE). The mobile display app renders real-time glucose values, trend arrows, and configurable high/low alerts. A cloud analytics platform aggregates historical data, generates trend reports, and provides optional insulin dosing guidance classified as Software as a Medical Device (SaMD) per IMDRF N41. The system comprises three distinct software items: sensor firmware (IEC 62304 Class B), mobile display application (IEC 62304 Class A), and cloud analytics SaMD (IEC 62304 Class B for dosing guidance, Class A for reporting). The system is classified FDA Class II via 510(k) and EU MDR Class IIb. Sensor wear duration is 14 days.

## System Boundary

**Inside the system boundary:**
- Sensor patch: subcutaneous electrochemical glucose sensor, analog front-end, sensor microcontroller with firmware, BLE radio, battery, adhesive housing
- Mobile display application: smartphone app (iOS/Android) for real-time display, alerts, and data relay to cloud
- Cloud analytics platform: data ingestion API, glucose trend analysis engine, insulin dosing guidance algorithm (SaMD), reporting dashboard, data storage

**Outside the system boundary:**
- Smartphone hardware and operating system (commercially available device)
- Cellular/Wi-Fi network infrastructure
- Insulin pump (optional integration partner; separate device)
- Electronic health record system (receives data via cloud API)
- Sensor insertion device (mechanical applicator, not electronic)
- Healthcare provider portal (consumes cloud analytics reports)

## Operational Environment

The sensor patch operates on the patient's body (typically upper arm or abdomen) under conditions of 10C to 45C skin surface temperature, exposure to sweat, water immersion (IP27 rated), and mechanical stress from daily activities. The mobile application runs on consumer smartphones. The cloud analytics platform operates in a HIPAA-compliant cloud environment with 99.9% availability SLA.

## Operating Modes

| Mode ID   | Name              | Description                                                              | Active Functions                                     | Constraints                                       |
|-----------|-------------------|--------------------------------------------------------------------------|------------------------------------------------------|---------------------------------------------------|
| MODE-001  | Continuous Monitor | Sensor active, BLE transmitting, app displaying real-time glucose        | All FUN- functions active                            | Sensor within 14-day wear period; BLE in range     |
| MODE-002  | Warm-Up           | Sensor newly inserted; stabilization period before readings are valid    | FUN-SNS-01 (calibrating), FUN-COM-01 (status only)  | No glucose display; 1-2 hour duration              |
| MODE-003  | Disconnected      | BLE link lost; sensor continues logging; app shows stale data with alert | FUN-SNS-01 (logging locally), FUN-ALT-01 (alert)    | No real-time display; data backfill on reconnect   |
| MODE-004  | End of Life       | Sensor approaching or past 14-day expiration; accuracy degraded          | FUN-ALT-01 (expiration alert), FUN-COM-01            | User prompted to replace sensor                    |

## Key Technical Challenges

1. **SaMD classification boundary.** The system contains three software items with different SaMD classifications per IMDRF N41. The insulin dosing guidance algorithm is SaMD that informs clinical management (IMDRF Category II for serious condition), while the display-only app is not SaMD when it merely renders sensor data without algorithmic interpretation. Maintaining clear boundaries between these software items is essential for proportionate regulatory burden.

2. **Sensor accuracy across wear duration.** Electrochemical sensor accuracy degrades over the 14-day wear period due to biofouling and foreign body response. The system must characterize and compensate for this drift while communicating accuracy limitations to the user through confidence indicators.

3. **Cybersecurity for patient health data.** BLE transmission of glucose data creates a wireless attack surface. The cloud API processes and stores protected health information subject to HIPAA. End-to-end encryption, authentication, and data integrity must be maintained across sensor-to-app BLE, app-to-cloud HTTPS, and cloud-to-EHR API interfaces.

4. **Interoperability with insulin pumps.** Optional closed-loop integration with insulin pumps requires a standardized, safety-qualified communication interface where glucose readings drive automated insulin delivery decisions. The CGM-to-pump interface must address latency, data integrity, and fallback behavior when communication fails.

## Stakeholders

| Stakeholder                    | Role                                                                              |
|--------------------------------|-----------------------------------------------------------------------------------|
| Patient / user                 | Wears sensor, views glucose data on mobile app, makes treatment decisions         |
| Endocrinologist                | Prescribes CGM, reviews trend reports, adjusts therapy based on cloud analytics   |
| FDA (CDRH)                     | Reviews 510(k) submission; evaluates SaMD classification per IMDRF N41            |
| EU Notified Body               | Assesses EU MDR conformity for Class IIb medical device with SaMD component       |
| Insulin pump manufacturer      | Integration partner for optional closed-loop glucose-responsive insulin delivery  |

## Standards Applicability

| Standard            | Applicability                                                                                   |
|---------------------|-------------------------------------------------------------------------------------------------|
| IEC 62304           | Software lifecycle: Class B for sensor firmware and dosing SaMD; Class A for display app        |
| ISO 14971           | Risk management across full product lifecycle including SaMD components                          |
| IEC 62366-1         | Usability engineering for sensor application, mobile app interaction, alert comprehension        |
| IMDRF SaMD N41      | SaMD classification framework for cloud-based insulin dosing guidance algorithm                  |
| FDA SaMD guidance   | Predetermined change control plan for cloud analytics algorithm updates                          |
