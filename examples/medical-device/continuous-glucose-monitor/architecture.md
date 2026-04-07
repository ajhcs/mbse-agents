# Architecture

## System Context

```mermaid
graph TB
    subgraph CGM["Continuous Glucose Monitor System"]
        SNS["CMP-SNS-01<br/>Sensor Patch"]
        APP["CMP-APP-01<br/>Mobile Display App"]
        CLD["CMP-CLD-01<br/>Cloud Analytics"]
    end

    PATIENT["Patient"]
    HCP["Healthcare<br/>Provider"]
    PUMP["Insulin Pump<br/>(Optional)"]
    EHR["Electronic Health<br/>Record"]
    PHONE["Smartphone<br/>(Platform)"]

    PATIENT -->|Interstitial fluid| SNS
    SNS -->|BLE glucose data| APP
    APP -->|Display, alerts| PATIENT
    APP -->|HTTPS upload| CLD
    CLD -->|Trend reports, dosing guidance| HCP
    CLD -->|FHIR glucose data| EHR
    SNS -.->|BLE (optional)| PUMP
    PHONE -->|OS services| APP
```

## Functional Architecture

| FUN ID       | Function Name                   | Description                                                                 | Inputs                                  | Outputs                                    | Dependencies      |
|--------------|---------------------------------|-----------------------------------------------------------------------------|-----------------------------------------|--------------------------------------------|--------------------|
| FUN-SNS-01   | Glucose Measurement             | Sample electrochemical sensor, apply calibration, produce glucose value     | Raw sensor current, calibration model   | Calibrated glucose reading (mg/dL)         | None               |
| FUN-COM-01   | BLE Data Transmission           | Transmit glucose readings and sensor status to mobile app via BLE          | Glucose readings, sensor status         | BLE packets (encrypted)                    | FUN-SNS-01         |
| FUN-DSP-01   | Glucose Display and Trending    | Render real-time glucose, trend arrows, and historical graph on mobile     | BLE glucose data                        | Display content, trend indicators          | FUN-COM-01         |
| FUN-ALT-01   | Alert Management                | Generate high/low glucose alerts and urgent alarms on mobile device        | Glucose value, user thresholds          | Audible/haptic alerts                      | FUN-DSP-01         |
| FUN-UPL-01   | Cloud Data Upload               | Transmit glucose history from mobile app to cloud analytics platform       | Glucose history, session metadata       | HTTPS data upload                          | FUN-DSP-01         |
| FUN-ANL-01   | Glucose Analytics and Reporting | Compute time-in-range, GMI, variability metrics from aggregated data       | Uploaded glucose history                | Provider reports, standardized metrics     | FUN-UPL-01         |
| FUN-DOS-01   | Insulin Dosing Guidance (SaMD)  | Generate insulin dose adjustment recommendations from trend analysis       | 14-day glucose patterns                 | Dosing recommendations (provider-facing)   | FUN-ANL-01         |

## Physical Architecture

| CMP ID        | Component Name                        | Type       | Parent       | Description                                                          |
|---------------|---------------------------------------|------------|--------------|----------------------------------------------------------------------|
| CMP-SNS-01    | Sensor Patch                          | Assembly   | System       | Wearable patch with subcutaneous sensor, electronics, and BLE radio  |
| CMP-SNS-01A   | Electrochemical Sensor Element        | Module     | CMP-SNS-01   | Enzyme-coated electrode for glucose oxidation current measurement    |
| CMP-SNS-01B   | Analog Front-End                      | Hardware   | CMP-SNS-01   | Potentiostat, ADC, signal conditioning for sensor current            |
| CMP-SNS-01C   | Sensor Microcontroller + Firmware     | HW/SW      | CMP-SNS-01   | ARM Cortex-M0 running glucose measurement and calibration firmware   |
| CMP-SNS-01D   | BLE Radio                             | Hardware   | CMP-SNS-01   | Bluetooth Low Energy 5.0 transceiver with AES-128 encryption         |
| CMP-SNS-01E   | Sensor Battery                        | Hardware   | CMP-SNS-01   | Non-rechargeable coin cell sized for 14-day operation                |
| CMP-APP-01    | Mobile Display Application            | Software   | System       | Smartphone application for glucose display, alerts, and cloud relay  |
| CMP-APP-01A   | Display and Alerting Module           | Software   | CMP-APP-01   | UI rendering, trend computation, configurable alert management       |
| CMP-APP-01B   | Communication Module                  | Software   | CMP-APP-01   | BLE stack integration, cloud API client, authentication              |
| CMP-CLD-01    | Cloud Analytics Platform              | Software   | System       | Server-side glucose analytics, reporting, and dosing guidance        |
| CMP-CLD-01A   | Data Ingestion API                    | Software   | CMP-CLD-01   | REST API for glucose data upload with OAuth 2.0 authentication       |
| CMP-CLD-01B   | Analytics Engine                      | Software   | CMP-CLD-01   | Time-in-range, GMI, variability computation, report generation       |
| CMP-CLD-01C   | Insulin Dosing Guidance Algorithm     | Software   | CMP-CLD-01   | SaMD component: pattern-based insulin dose adjustment recommendations |

## Allocation

| FUN ID       | REQ ID(s)                           | CMP ID(s)                              | Assurance Level      | Rationale                                                     |
|--------------|--------------------------------------|----------------------------------------|----------------------|---------------------------------------------------------------|
| FUN-SNS-01   | REQ-FUN-001                         | CMP-SNS-01A, CMP-SNS-01B, CMP-SNS-01C | IEC 62304 Class B    | Sensor measurement error can lead to incorrect treatment      |
| FUN-COM-01   | REQ-FUN-002, REQ-IFC-001           | CMP-SNS-01C, CMP-SNS-01D              | IEC 62304 Class B    | BLE failure causes data gap; encrypted to prevent spoofing    |
| FUN-DSP-01   | REQ-FUN-003                         | CMP-APP-01A                            | IEC 62304 Class A    | Display renders sensor data without algorithmic transformation |
| FUN-ALT-01   | REQ-FUN-004                         | CMP-APP-01A, CMP-APP-01B              | IEC 62304 Class A    | Alerts depend on smartphone OS notification; patient can check manually |
| FUN-UPL-01   | REQ-IFC-002                         | CMP-APP-01B, CMP-CLD-01A              | IEC 62304 Class A    | Upload failure delays analytics; does not affect real-time display |
| FUN-ANL-01   | REQ-FUN-005                         | CMP-CLD-01A, CMP-CLD-01B              | IEC 62304 Class A    | Reporting metrics are retrospective; reviewed by provider      |
| FUN-DOS-01   | REQ-FUN-006                         | CMP-CLD-01C                            | IEC 62304 Class B    | SaMD dosing guidance informs clinical management (IMDRF Cat II) |

## Interfaces

### External Interfaces

| IFC ID       | Partner System              | Data Item                                | Direction     | Protocol             | Timing                    |
|--------------|-----------------------------|------------------------------------------|---------------|----------------------|---------------------------|
| IFC-EXT-001  | Patient (interstitial fluid)| Glucose-proportional electrochemical current | In         | Electrochemical      | Continuous (sensor element) |
| IFC-EXT-002  | Smartphone (OS)             | BLE stack, notifications, storage        | Bidirectional | OS APIs              | Event-driven               |
| IFC-EXT-003  | Electronic Health Record    | Glucose history, trend reports (FHIR)    | Out           | FHIR R4 / REST API   | On demand                  |
| IFC-EXT-004  | Insulin Pump (optional)     | Real-time glucose value, trend           | Out           | BLE (standardized)   | Per glucose sample         |

### Internal Interfaces

| IFC ID       | Source CMP ID   | Target CMP ID   | Data Item                              | Mechanism           | Timing                |
|--------------|-----------------|------------------|----------------------------------------|---------------------|-----------------------|
| IFC-INT-001  | CMP-SNS-01A     | CMP-SNS-01B      | Raw sensor current                     | Analog trace        | Continuous             |
| IFC-INT-002  | CMP-SNS-01B     | CMP-SNS-01C      | Digitized sensor signal                | SPI                 | Per sample (1-5 min)   |
| IFC-INT-003  | CMP-SNS-01C     | CMP-SNS-01D      | Calibrated glucose + status            | UART                | Per sample             |
| IFC-INT-004  | CMP-SNS-01D     | CMP-APP-01B      | Encrypted BLE glucose packet           | BLE 5.0 GATT       | Per sample (1-5 min)   |
| IFC-INT-005  | CMP-APP-01B     | CMP-CLD-01A      | Glucose history batch upload           | HTTPS / REST        | Periodic (5-15 min)    |

## Failure Containment / Partitioning

The three-tier architecture (sensor, app, cloud) provides inherent physical and logical separation.

**Sensor independence:** The sensor patch operates autonomously with local data logging. BLE failure causes MODE-003 (Disconnected) but does not affect measurement or local storage. The sensor firmware is safety-classified (Class B) independently of the app.

**App-cloud separation:** The mobile display application provides real-time glucose monitoring independent of cloud availability. Cloud analytics failure does not affect real-time display or alerting. The dosing guidance SaMD (CMP-CLD-01C) runs in an isolated compute environment with independent deployment and validation cycles from the analytics engine (CMP-CLD-01B).

**SaMD boundary enforcement:** The insulin dosing guidance algorithm (FUN-DOS-01) is deployed as a separate microservice with defined API boundaries. Its inputs and outputs are versioned. Algorithm updates follow the predetermined change control plan filed with FDA, allowing certain updates without new 510(k) submissions.

## Architecture Decisions

### AD-01: Three Distinct Software Items over Monolithic Design

**Decision:** Architect the system as three independently classified software items (sensor firmware, mobile app, cloud SaMD) rather than a single integrated software system.

**Rationale:** IMDRF N41 and IEC 62304 classify software based on the severity of harm that a software failure can contribute to. The display-only app (Class A) and the dosing guidance algorithm (Class B SaMD) have fundamentally different risk profiles. Separating them allows proportionate development rigor: Class B lifecycle for the sensor firmware and dosing algorithm, Class A for the display app. This reduces development cost for the lower-risk component without compromising safety for the higher-risk components.

**Trade-off:** Three separate software items require three independent verification and release processes. Accepted because the regulatory efficiency and risk proportionality outweigh the process overhead.

### AD-02: Provider-Facing Dosing Guidance over Patient-Facing

**Decision:** Route insulin dosing guidance recommendations to the healthcare provider rather than directly to the patient.

**Rationale:** Presenting dosing recommendations directly to the patient would elevate the SaMD classification from IMDRF Category II (informs clinical management) toward Category III (drives clinical management), significantly increasing the regulatory burden and clinical evidence requirements. Provider-in-the-loop maintains a human clinical judgment step in the dosing decision chain.

**Trade-off:** Patients do not receive real-time dosing suggestions; they must wait for provider review. Accepted because the regulatory pathway is more achievable and the safety argument is stronger with a clinician intermediary.

### AD-03: BLE 5.0 with AES-128 Bonded Pairing

**Decision:** Use BLE 5.0 with AES-128 encryption and bonded pairing for sensor-to-app communication rather than unencrypted BLE or Wi-Fi.

**Rationale:** BLE 5.0 provides sufficient bandwidth for glucose data (small payload, low frequency) with significantly lower power consumption than Wi-Fi, enabling a 14-day battery life from a coin cell. AES-128 bonded pairing prevents eavesdropping and device spoofing without the key exchange complexity of higher-security protocols that would exceed the sensor's compute budget.

**Trade-off:** BLE range (typically 10-30 m) limits the sensor-to-phone distance. Accepted because the patient carries the phone, and MODE-003 handles temporary disconnections with local data buffering and backfill.
