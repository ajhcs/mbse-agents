# Requirements

All requirements are atomic, testable shall-statements.

## Requirement Record Schema

| Field         | Description                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------|
| ID            | Unique identifier (e.g., REQ-FUN-001)                                                            |
| Statement     | Atomic shall-statement                                                                            |
| Rationale     | Why this requirement exists                                                                       |
| Source        | Hazard ID (HZ-), control ID (CTL-), regulatory clause, or stakeholder need                       |
| Parent        | Parent requirement ID (if derived)                                                                |
| Verification  | Method: test, analysis, inspection, demonstration                                                 |
| Allocation    | Target component ID(s) from architecture.md                                                       |
| Status        | Draft, baselined, verified, deferred                                                              |

## Functional Requirements

### REQ-FUN-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall deliver fluid at a programmable rate from 0.1 mL/hr to 999 mL/hr in increments of 0.1 mL/hr. |
| **Rationale**    | Clinical infusion protocols require a wide rate range with fine granularity for titrated medications. |
| **Source**       | Stakeholder need (clinician); IEC 60601-2-24 Clause 201.12.1 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01B, CMP-PMA-01A, CMP-PMA-01B |
| **Status**       | Baselined |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall maintain flow rate accuracy within +/-5% of the programmed rate at rates >= 1 mL/hr and within +/-15% at rates < 1 mL/hr under standard test conditions per IEC 60601-2-24. |
| **Rationale**    | Flow accuracy requirements are mandated by the infusion pump particular standard. |
| **Source**       | IEC 60601-2-24 Clause 201.12.1.101; CTL-001 |
| **Parent**       | REQ-FUN-001 |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01B, CMP-PMA-01A, CMP-PMA-01B |
| **Status**       | Baselined |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall use closed-loop flow control comparing commanded flow rate against measured flow rate from the flow sensor, with a control loop period of not more than 10 ms. |
| **Rationale**    | Closed-loop control compensates for tubing compliance, viscosity, and mechanical variation. |
| **Source**       | CTL-001; architecture decision AD-04 |
| **Parent**       | REQ-FUN-002 |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01B, CMP-PMA-01B |
| **Status**       | Baselined |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall accumulate delivered volume with an accuracy of +/-5% of the actual volume delivered and shall compare accumulated volume against the programmed VTBI. |
| **Rationale**    | Volume tracking drives KVO transition and dose completion awareness. |
| **Source**       | Stakeholder need (clinician); IEC 60601-2-24 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01B |
| **Status**       | Baselined |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall transition to KVO mode (MODE-003) when the programmed VTBI has been delivered and shall annunciate the transition to the clinician via an audible and visual alarm. |
| **Rationale**    | Automated KVO transition maintains venous access while alerting the clinician that the primary infusion is complete. |
| **Source**       | Stakeholder need (clinician); CTL-008 |
| **Parent**       | REQ-FUN-004 |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01B, CMP-MCB-01D, CMP-UIM-01B |
| **Status**       | Baselined |

### REQ-FUN-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall deliver clinician-initiated bolus volumes from 0.1 mL to 100 mL at rates from 1 mL/hr to 999 mL/hr with DERS hard limit checking applied before bolus delivery begins. |
| **Rationale**    | Bolus delivery must be bounded by drug library hard limits to prevent over-infusion. |
| **Source**       | Stakeholder need (clinician); CTL-003; HZ-002 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01B, CMP-MCB-01C, CMP-PMA-01A |
| **Status**       | Baselined |

### REQ-FUN-007
| Field        | Value |
|--------------|-------|
| **Statement**    | The DERS shall check programmed drug, concentration, dose, and rate against the active drug library before infusion start and shall alert the clinician if any parameter exceeds a soft limit. |
| **Rationale**    | DERS is the primary defense against medication dosing errors. |
| **Source**       | CTL-003; HZ-003; FDA Infusion Pump Improvement Initiative |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01C |
| **Status**       | Baselined |

### REQ-FUN-008
| Field        | Value |
|--------------|-------|
| **Statement**    | The DERS shall prevent infusion start if any programmed parameter exceeds a hard limit, and the hard limit shall not be overridable by the clinician. |
| **Rationale**    | Hard limits represent absolute safety boundaries that should never be exceeded. |
| **Source**       | CTL-003; HZ-003; FDA Infusion Pump Improvement Initiative |
| **Parent**       | REQ-FUN-007 |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01C |
| **Status**       | Baselined |

### REQ-FUN-009
| Field        | Value |
|--------------|-------|
| **Statement**    | The DERS shall log all soft limit alerts and clinician override decisions, including drug name, programmed parameters, limit values, and clinician response, to non-volatile memory. |
| **Rationale**    | Override logging supports pharmacovigilance and drug library tuning to reduce alert fatigue. |
| **Source**       | Stakeholder need (pharmacist); FDA premarket cybersecurity guidance (data integrity) |
| **Parent**       | REQ-FUN-007 |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01C |
| **Status**       | Baselined |

### REQ-FUN-010
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall store a drug library containing a minimum of 2000 drug entries with per-drug soft and hard limits for concentration, dose, rate, and VTBI, organized by clinical care area. |
| **Rationale**    | Hospital drug libraries require large capacity with care-area-specific limit profiles. |
| **Source**       | Stakeholder need (pharmacist) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01C |
| **Status**       | Baselined |

### REQ-FUN-011
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall validate the integrity of drug library files using CRC-32 and digital signature verification before activating a new drug library. |
| **Rationale**    | Corrupted or tampered drug libraries can defeat DERS protection. |
| **Source**       | CTL-009; HZ-009; FDA premarket cybersecurity guidance |
| **Parent**       | REQ-FUN-010 |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01C, CMP-WCM-01C |
| **Status**       | Baselined |

### REQ-FUN-012
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall generate a high-priority alarm per IEC 60601-1-8 within 5 seconds of detecting an occlusion condition exceeding the configurable occlusion pressure threshold. |
| **Rationale**    | Prompt occlusion detection prevents under-infusion and upstream line rupture. |
| **Source**       | IEC 60601-2-24 Clause 201.12.4.101; CTL-005 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01D, CMP-PMA-01E, CMP-UIM-01B |
| **Status**       | Baselined |

### REQ-FUN-013
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall generate a high-priority alarm per IEC 60601-1-8 within 2 seconds of detecting air-in-line volume exceeding 50 microliters and shall pause the infusion (MODE-004). |
| **Rationale**    | Air embolism prevention requires rapid detection and infusion stoppage. |
| **Source**       | IEC 60601-2-24 Clause 201.12.4.103; CTL-004; HZ-004 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01D, CMP-PMA-01D, CMP-UIM-01B |
| **Status**       | Baselined |

### REQ-FUN-014
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall generate alarm signals conforming to IEC 60601-1-8 alarm priorities: high-priority (pulse pattern, >= 75 dBA), medium-priority (>= 65 dBA), and low-priority (>= 55 dBA), measured at 1 meter. |
| **Rationale**    | Standardized alarm characteristics ensure clinical audibility and recognition. |
| **Source**       | IEC 60601-1-8 Clause 6.3; IEC 60601-2-24 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01D, CMP-UIM-01B |
| **Status**       | Baselined |

### REQ-FUN-015
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall continuously monitor the flow sensor output and shall generate a medium-priority alarm if the measured flow rate deviates from the commanded rate by more than 15% for more than 30 seconds. |
| **Rationale**    | Flow deviation detection catches partial occlusions and pump mechanism failures. |
| **Source**       | CTL-001; HZ-001 |
| **Parent**       | REQ-FUN-003 |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01D, CMP-PMA-01B |
| **Status**       | Baselined |

### REQ-FUN-016
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall detect an upstream occlusion (container empty) when upstream pressure drops below the configurable threshold and shall generate a high-priority alarm within 5 seconds. |
| **Rationale**    | Upstream occlusion indicates fluid source exhaustion requiring clinician intervention. |
| **Source**       | IEC 60601-2-24 Clause 201.12.4.101; CTL-005 |
| **Parent**       | REQ-FUN-012 |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01D, CMP-PMA-01E |
| **Status**       | Baselined |

### REQ-FUN-017
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall detect the door-open condition via the door latch sensor and shall transition to MODE-004 (Alarm/Pause) within 500 ms of detection. |
| **Rationale**    | Door open during infusion requires immediate stoppage; anti-free-flow clamp engages mechanically. |
| **Source**       | CTL-006; HZ-005 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01D, CMP-PMA-01F |
| **Status**       | Baselined |

### REQ-FUN-018
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall detect loss of flow sensor input and shall transition to open-loop delivery with a medium-priority alarm within 5 seconds, using motor step counting as the backup flow estimation method. |
| **Rationale**    | Flow sensor failure should not halt infusion but requires clinician awareness of reduced accuracy. |
| **Source**       | CTL-010; IEC 60601-2-24 |
| **Parent**       | REQ-FUN-003 |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01B, CMP-MCB-01D |
| **Status**       | Baselined |

### REQ-FUN-019
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall monitor battery state of charge and shall generate a low-priority alarm when remaining battery runtime falls below 30 minutes and a high-priority alarm when runtime falls below 10 minutes. |
| **Rationale**    | Battery depletion warning gives clinician time to connect AC power before infusion is interrupted. |
| **Source**       | IEC 60601-1 Clause 11.8; stakeholder need (clinician) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01K |
| **Status**       | Baselined |

### REQ-FUN-020
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall display the current infusion parameters (drug name, rate, VTBI, volume infused, time remaining) on the main screen with a refresh rate of not less than 2 Hz. |
| **Rationale**    | Clinician situational awareness requires continuously visible infusion status. |
| **Source**       | Stakeholder need (clinician); IEC 62366-1 (usability) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-UIM-01A, CMP-UIM-01C |
| **Status**       | Baselined |

### REQ-FUN-021
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall respond to clinician touch inputs within 200 ms of contact and shall provide visual feedback on the display within 500 ms. |
| **Rationale**    | Responsive interface prevents data entry errors and clinician frustration. |
| **Source**       | IEC 62366-1 (usability); stakeholder need (clinician) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-UIM-01A, CMP-UIM-01C |
| **Status**       | Baselined |

### REQ-FUN-022
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump infusion programming workflow shall require DERS limit checking to complete before the pump permits infusion start, and shall not provide a user interface path that bypasses DERS checking. |
| **Rationale**    | DERS bypass would defeat the dose error reduction safety function. |
| **Source**       | CTL-003; HZ-003; FDA Infusion Pump Improvement Initiative |
| **Parent**       | REQ-FUN-007 |
| **Verification** | Test, Inspection |
| **Allocation**   | CMP-UIM-01C, CMP-MCB-01C |
| **Status**       | Baselined |

### REQ-FUN-023
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall execute a power-up self-test verifying processor, memory, flow sensor, pressure sensor, air detector, door sensor, display, alarm annunciator, and watchdog within 30 seconds of power application and shall not permit infusion start until self-test passes. |
| **Rationale**    | Pre-use self-test detects latent faults before they combine with active faults during infusion. |
| **Source**       | CTL-011; IEC 60601-1 Clause 15.4.4 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01, CMP-MCB-01J |
| **Status**       | Baselined |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The anti-free-flow clamp shall engage mechanically to occlude the IV tubing within 500 ms of door opening, independent of processor, software, or electrical power state. |
| **Rationale**    | Free-flow is the highest-severity hazard; the primary control must be independent of electronics. |
| **Source**       | HZ-005; CTL-006; IEC 60601-2-24 Clause 201.12.4.104 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PMA-01C |
| **Status**       | Baselined |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The hardware watchdog timer shall reset the main processor within 200 ms if the processor fails to service the watchdog, and the reset shall place the pump in a safe state (infusion stopped, anti-free-flow engaged, alarm activated). |
| **Rationale**    | Processor lockup or software hang must result in a safe state, not continued uncontrolled delivery. |
| **Source**       | HZ-006; CTL-007 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01J, CMP-MCB-01A |
| **Status**       | Baselined |

### REQ-SAF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall limit the maximum deliverable flow rate to 999 mL/hr under all software and hardware fault conditions, enforced by an independent hardware current limiter on the pump motor driver that prevents motor speed from exceeding the rate corresponding to 999 mL/hr. |
| **Rationale**    | Hardware rate limiting provides defense in depth against software faults that could command excessive pump speed. |
| **Source**       | HZ-001; CTL-002; IEC 60601-2-24 |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-MCB-01H |
| **Status**       | Baselined |

### REQ-SAF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall detect a discrepancy between the commanded flow rate and the measured flow rate exceeding 25% of the commanded rate for more than 10 seconds and shall transition to MODE-004 (Alarm/Pause) with a high-priority alarm. |
| **Rationale**    | Gross flow discrepancy indicates pump mechanism failure, tubing displacement, or free-flow condition. |
| **Source**       | HZ-001; HZ-005; CTL-001 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01B, CMP-MCB-01D |
| **Status**       | Baselined |

### REQ-SAF-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The RTOS memory protection unit shall enforce spatial isolation between the infusion control partition (P1) and the communication partition (P4) such that a fault in the communication task cannot modify infusion control memory. |
| **Rationale**    | Communication failures and network attacks must not propagate to safety-critical infusion control. |
| **Source**       | HZ-008; CTL-012; FDA premarket cybersecurity guidance |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-MCB-01E |
| **Status**       | Baselined |

### REQ-SAF-006
| Field        | Value |
|--------------|-------|
| **Statement**    | Upon detection of a non-recoverable software fault, the pump shall transition to a safe state within 1 second. The safe state shall consist of: infusion stopped, anti-free-flow clamp engaged, high-priority alarm activated, and fault code displayed. |
| **Rationale**    | Non-recoverable faults must result in a defined safe state that prevents patient harm and alerts the clinician. |
| **Source**       | HZ-006; CTL-007; IEC 60601-1 Clause 13.1 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01B, CMP-MCB-01D, CMP-PMA-01C, CMP-UIM-01B |
| **Status**       | Baselined |

### REQ-SAF-007
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall maintain alarm annunciation capability (audible and visual) independent of the touchscreen display, such that alarm signals are generated even if the display application crashes or the touchscreen fails. |
| **Rationale**    | Alarm annunciation is the last line of defense; it must function when the display has failed. |
| **Source**       | HZ-007; CTL-008; IEC 60601-1-8 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01D, CMP-UIM-01B |
| **Status**       | Baselined |

### REQ-SAF-008
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall provide battery backup sufficient to maintain infusion delivery and alarm capability for a minimum of 2 hours at a rate of 125 mL/hr. |
| **Rationale**    | AC power interruptions in hospital settings must not immediately halt treatment. |
| **Source**       | IEC 60601-1 Clause 11.8; stakeholder need (clinician) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01K |
| **Status**       | Baselined |

### REQ-SAF-009
| Field        | Value |
|--------------|-------|
| **Statement**    | The DERS engine shall operate independently from the network communication functions such that a loss of Wi-Fi connectivity does not degrade DERS checking capability for infusions programmed using the locally stored drug library. |
| **Rationale**    | DERS protection must not depend on network availability. |
| **Source**       | HZ-008; CTL-012; FDA premarket cybersecurity guidance |
| **Parent**       | REQ-FUN-007 |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01C |
| **Status**       | Baselined |

### REQ-SAF-010
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall not accept drug library updates during an active infusion. Drug library activation shall require the pump to be in MODE-005 (Standby/Setup) with no active infusion. |
| **Rationale**    | Mid-infusion library changes could alter DERS limits for the active drug, creating an inconsistent safety state. |
| **Source**       | HZ-009; CTL-009 |
| **Parent**       | REQ-FUN-011 |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01C, CMP-WCM-01C |
| **Status**       | Baselined |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall transmit infusion status data (drug, rate, volume infused, alarm state) to the EHR via IFC-EXT-001 using HL7 v2 or FHIR messaging within 30 seconds of a status change event. |
| **Rationale**    | Timely auto-documentation reduces manual charting burden and supports clinical decision-making. |
| **Source**       | Stakeholder need (clinician, hospital IT); IEC 80001-1 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-WCM-01B |
| **Status**       | Baselined |

### REQ-IFC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall receive drug orders from the EHR via IFC-EXT-002 and shall pre-populate infusion programming fields, requiring clinician confirmation before infusion start. |
| **Rationale**    | EHR-to-pump order transfer reduces transcription errors; clinician confirmation prevents automation complacency. |
| **Source**       | Stakeholder need (clinician); CTL-003 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-WCM-01B, CMP-MCB-01C |
| **Status**       | Baselined |

### REQ-IFC-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall encrypt all network communications using TLS 1.2 or higher with certificate-based mutual authentication per the hospital PKI infrastructure. |
| **Rationale**    | Network encryption prevents eavesdropping and man-in-the-middle attacks on infusion data and drug library transfers. |
| **Source**       | CTL-012; FDA premarket cybersecurity guidance; IEC 62443-4-1 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01G, CMP-WCM-01A |
| **Status**       | Baselined |

### REQ-IFC-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall authenticate to the hospital Wi-Fi network using WPA2-Enterprise or WPA3 with 802.1X and shall not support open or WEP-encrypted networks. |
| **Rationale**    | Weak or absent Wi-Fi authentication exposes the pump to network-based attacks. |
| **Source**       | CTL-012; FDA premarket cybersecurity guidance |
| **Parent**       | REQ-IFC-003 |
| **Verification** | Test |
| **Allocation**   | CMP-WCM-01A |
| **Status**       | Baselined |

### REQ-IFC-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall forward active alarm notifications to the central monitoring station via IFC-EXT-004 within 10 seconds of alarm activation, including alarm priority, alarm condition, and pump identifier. |
| **Rationale**    | Remote alarm notification enables centralized monitoring of pump fleets in large clinical areas. |
| **Source**       | Stakeholder need (clinician, hospital administration); IEC 60601-1-8 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-WCM-01B, CMP-MCB-01D |
| **Status**       | Baselined |

### REQ-IFC-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The MCB shall validate all data received from the WCM via IFC-INT-009 against expected message format and value ranges before acting on the data, and shall reject malformed messages with an error log entry. |
| **Rationale**    | Input validation at the MCB-WCM boundary prevents network-originated data from corrupting safety-critical functions. |
| **Source**       | CTL-012; HZ-008; FDA premarket cybersecurity guidance |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01B |
| **Status**       | Baselined |

## Performance Requirements

### REQ-PRF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall achieve trumpet curve compliance per IEC 60601-2-24 Clause 201.12.1.103 for observation windows of 2, 5, 11, 19, and 31 minutes at the reference rate of 25 mL/hr. |
| **Rationale**    | Trumpet curve compliance demonstrates short-term and long-term flow uniformity. |
| **Source**       | IEC 60601-2-24 Clause 201.12.1.103 |
| **Parent**       | REQ-FUN-002 |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01B, CMP-PMA-01A |
| **Status**       | Baselined |

### REQ-PRF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall complete power-up self-test and be ready for infusion programming within 30 seconds of power application at ambient temperatures between 10C and 40C. |
| **Rationale**    | Rapid startup supports clinical workflow in emergency and routine settings. |
| **Source**       | Stakeholder need (clinician); IEC 60601-1 |
| **Parent**       | REQ-FUN-023 |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01, CMP-UIM-01, CMP-WCM-01 |
| **Status**       | Baselined |

### REQ-PRF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall operate within a total power consumption of 25 watts on AC mains and shall consume not more than 15 watts from battery during infusion at 125 mL/hr. |
| **Rationale**    | Power budget constrains thermal design and battery runtime requirements. |
| **Source**       | IEC 60601-1 Clause 11; architecture constraint |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01K |
| **Status**       | Baselined |

### REQ-PRF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The pump shall resume infusion delivery within 5 seconds of AC power restoration following a power interruption of less than 5 seconds, without clinician intervention, and shall alarm if the interruption exceeds 5 seconds. |
| **Rationale**    | Brief power interruptions from outlet disconnects during patient transport should not halt treatment. |
| **Source**       | IEC 60601-1 Clause 11.8; stakeholder need (clinician) |
| **Parent**       | REQ-SAF-008 |
| **Verification** | Test |
| **Allocation**   | CMP-MCB-01K, CMP-MCB-01B |
| **Status**       | Baselined |
