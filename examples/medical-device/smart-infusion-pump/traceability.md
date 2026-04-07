# Traceability

## Trace Strategy

This traceability matrix establishes bidirectional linkage across all Smart Infusion Pump system engineering artifacts. Forward traces demonstrate that every requirement is allocated, sourced, and verified. Reverse traces confirm that every component, hazard, and verification activity connects back to a requirement. Gaps are first-class entries with disposition, not omissions.

**Traced entities:**
- Requirements (REQ-) to architecture components (CMP-)
- Requirements (REQ-) to hazard/control sources (HZ-, CTL-)
- Requirements (REQ-) to verification activities (VER-)
- Verification activities (VER-) to evidence artifacts (EVD-)
- Components (CMP-) back to requirements
- Hazards (HZ-) through controls (CTL-) to requirements

## Forward Traces

### Requirements to Architecture

| REQ ID       | Statement (short)                               | CMP ID(s)                                           | Allocation Rationale                                    |
|--------------|-------------------------------------------------|-----------------------------------------------------|---------------------------------------------------------|
| REQ-FUN-001  | Programmable rate 0.1-999 mL/hr                 | CMP-MCB-01B, CMP-PMA-01A, CMP-PMA-01B              | MCB controls; PMA delivers; flow sensor confirms        |
| REQ-FUN-002  | Flow rate accuracy +/-5% / +/-15%               | CMP-MCB-01B, CMP-PMA-01A, CMP-PMA-01B              | Closed-loop control drives accuracy                     |
| REQ-FUN-003  | Closed-loop flow control at 10 ms               | CMP-MCB-01B, CMP-PMA-01B                            | MCB executes control loop; sensor provides feedback     |
| REQ-FUN-004  | Volume tracking +/-5% accuracy                  | CMP-MCB-01B                                          | Volume accumulation in infusion control software        |
| REQ-FUN-005  | KVO transition on VTBI complete                 | CMP-MCB-01B, CMP-MCB-01D, CMP-UIM-01B              | MCB transitions; alarm app notifies; buzzer annunciates |
| REQ-FUN-006  | Bolus delivery with DERS hard limit check       | CMP-MCB-01B, CMP-MCB-01C, CMP-PMA-01A              | DERS checks before MCB commands bolus                   |
| REQ-FUN-007  | DERS soft limit alert before infusion start     | CMP-MCB-01C                                          | DERS engine on MCB                                      |
| REQ-FUN-008  | DERS hard limit non-overridable                 | CMP-MCB-01C                                          | DERS engine enforces absolute limits                    |
| REQ-FUN-009  | DERS override logging to NVM                    | CMP-MCB-01C                                          | Logging in DERS engine; NVM on MCB                      |
| REQ-FUN-010  | Drug library 2000+ entries                      | CMP-MCB-01C                                          | Library storage on MCB flash                            |
| REQ-FUN-011  | Drug library CRC + signature verification       | CMP-MCB-01C, CMP-WCM-01C                            | WCM receives; MCB validates                             |
| REQ-FUN-012  | Occlusion alarm within 5 seconds                | CMP-MCB-01D, CMP-PMA-01E, CMP-UIM-01B              | Pressure sensor detects; alarm app triggers; buzzer annunciates |
| REQ-FUN-013  | Air-in-line alarm within 2 seconds; pause       | CMP-MCB-01D, CMP-PMA-01D, CMP-UIM-01B              | Air detector triggers; alarm app pauses; buzzer annunciates |
| REQ-FUN-014  | Alarm signals per IEC 60601-1-8                 | CMP-MCB-01D, CMP-UIM-01B                            | Alarm app controls; buzzer/LED annunciates              |
| REQ-FUN-015  | Flow deviation alarm > 15% for 30s              | CMP-MCB-01D, CMP-PMA-01B                            | Alarm app monitors flow sensor vs. commanded rate       |
| REQ-FUN-016  | Upstream occlusion alarm within 5s              | CMP-MCB-01D, CMP-PMA-01E                            | Pressure sensor detects; alarm app triggers             |
| REQ-FUN-017  | Door-open detection; MODE-004 within 500 ms     | CMP-MCB-01D, CMP-PMA-01F                            | Door sensor triggers; alarm app transitions             |
| REQ-FUN-018  | Flow sensor loss; open-loop fallback            | CMP-MCB-01B, CMP-MCB-01D                            | Control app switches mode; alarm app notifies           |
| REQ-FUN-019  | Battery monitoring; low/critical alarms         | CMP-MCB-01K                                          | Power management monitors; alarms at thresholds         |
| REQ-FUN-020  | Display infusion parameters at 2 Hz             | CMP-UIM-01A, CMP-UIM-01C                            | Display app renders; touchscreen displays               |
| REQ-FUN-021  | Touch response within 200/500 ms                | CMP-UIM-01A, CMP-UIM-01C                            | Touch controller and display app                        |
| REQ-FUN-022  | Programming workflow enforces DERS check        | CMP-UIM-01C, CMP-MCB-01C                            | UI workflow gates on DERS completion                    |
| REQ-FUN-023  | Power-up self-test within 30 seconds            | CMP-MCB-01, CMP-MCB-01J                             | MCB runs test; watchdog verified                        |
| REQ-SAF-001  | Mechanical anti-free-flow within 500 ms         | CMP-PMA-01C                                          | Passive mechanical clamp; independent of electronics    |
| REQ-SAF-002  | Watchdog reset to safe state within 200 ms      | CMP-MCB-01J, CMP-MCB-01A                            | Hardware watchdog monitors processor                    |
| REQ-SAF-003  | Hardware motor current limiter at 999 mL/hr     | CMP-MCB-01H                                          | Independent hardware circuit on motor driver            |
| REQ-SAF-004  | Gross flow discrepancy alarm; MODE-004          | CMP-MCB-01B, CMP-MCB-01D                            | Infusion control detects; alarm app transitions         |
| REQ-SAF-005  | RTOS MPU isolation: P1 from P4                  | CMP-MCB-01E                                          | RTOS memory protection configuration                    |
| REQ-SAF-006  | Non-recoverable fault to safe state < 1s        | CMP-MCB-01B, CMP-MCB-01D, CMP-PMA-01C, CMP-UIM-01B | MCB stops pump; clamp engages; alarm activates          |
| REQ-SAF-007  | Alarm independent of display                    | CMP-MCB-01D, CMP-UIM-01B                            | Alarm hardware driven directly; not via display app     |
| REQ-SAF-008  | Battery backup 2 hours at 125 mL/hr            | CMP-MCB-01K                                          | Battery capacity in power management unit               |
| REQ-SAF-009  | DERS independent of network                     | CMP-MCB-01C                                          | Local drug library; no network dependency               |
| REQ-SAF-010  | No library update during active infusion        | CMP-MCB-01C, CMP-WCM-01C                            | MCB and WCM enforce standby-only activation             |
| REQ-IFC-001  | Infusion status to EHR within 30 seconds        | CMP-WCM-01B                                          | EHR interface application                               |
| REQ-IFC-002  | Drug orders from EHR; clinician confirmation    | CMP-WCM-01B, CMP-MCB-01C                            | WCM receives; MCB processes with DERS                   |
| REQ-IFC-003  | TLS 1.2+ with mutual authentication            | CMP-MCB-01G, CMP-WCM-01A                            | TLS library + Wi-Fi radio                               |
| REQ-IFC-004  | WPA2/WPA3 with 802.1X; no WEP                  | CMP-WCM-01A                                          | Wi-Fi radio configuration                               |
| REQ-IFC-005  | Alarm forwarding within 10 seconds              | CMP-WCM-01B, CMP-MCB-01D                            | Alarm app sends; EHR interface forwards                 |
| REQ-IFC-006  | MCB validates all WCM data; reject malformed    | CMP-MCB-01B                                          | Input validation at MCB-WCM boundary                    |
| REQ-PRF-001  | Trumpet curve compliance per IEC 60601-2-24     | CMP-MCB-01B, CMP-PMA-01A                            | Control algorithm and pump mechanism uniformity         |
| REQ-PRF-002  | Power-up ready within 30 seconds                | CMP-MCB-01, CMP-UIM-01, CMP-WCM-01                  | All subsystems initialize                               |
| REQ-PRF-003  | Power consumption 25W AC / 15W battery          | CMP-MCB-01K                                          | Power management design                                 |
| REQ-PRF-004  | Auto-resume after < 5s power interruption       | CMP-MCB-01K, CMP-MCB-01B                            | Battery backup and infusion state persistence           |

### Requirements to Hazards

| REQ ID       | Source HZ ID(s)     | Source CTL ID(s)          | Source Clause                        |
|--------------|---------------------|---------------------------|--------------------------------------|
| REQ-FUN-002  | —                   | CTL-001                   | IEC 60601-2-24 Clause 201.12.1.101  |
| REQ-FUN-003  | —                   | CTL-001                   | —                                    |
| REQ-FUN-005  | —                   | CTL-008                   | —                                    |
| REQ-FUN-006  | HZ-002              | CTL-003                   | —                                    |
| REQ-FUN-007  | HZ-003              | CTL-003                   | —                                    |
| REQ-FUN-008  | HZ-003              | CTL-003                   | —                                    |
| REQ-FUN-011  | HZ-009              | CTL-009                   | —                                    |
| REQ-FUN-012  | —                   | CTL-005                   | IEC 60601-2-24 Clause 201.12.4.101  |
| REQ-FUN-013  | HZ-004              | CTL-004                   | IEC 60601-2-24 Clause 201.12.4.103  |
| REQ-FUN-015  | HZ-001              | CTL-001                   | —                                    |
| REQ-FUN-016  | —                   | CTL-005                   | IEC 60601-2-24 Clause 201.12.4.101  |
| REQ-FUN-017  | HZ-005              | CTL-006                   | —                                    |
| REQ-FUN-022  | HZ-003              | CTL-003                   | —                                    |
| REQ-FUN-023  | —                   | CTL-011                   | IEC 60601-1 Clause 15.4.4           |
| REQ-SAF-001  | HZ-005              | CTL-006                   | IEC 60601-2-24 Clause 201.12.4.104  |
| REQ-SAF-002  | HZ-006              | CTL-007                   | —                                    |
| REQ-SAF-003  | HZ-001              | CTL-002                   | —                                    |
| REQ-SAF-004  | HZ-001, HZ-005      | CTL-001                   | —                                    |
| REQ-SAF-005  | HZ-008              | CTL-012                   | —                                    |
| REQ-SAF-006  | HZ-006              | CTL-007                   | IEC 60601-1 Clause 13.1             |
| REQ-SAF-007  | HZ-007              | CTL-008                   | IEC 60601-1-8                        |
| REQ-SAF-009  | HZ-008              | CTL-012                   | —                                    |
| REQ-SAF-010  | HZ-009              | CTL-009                   | —                                    |
| REQ-IFC-003  | HZ-008              | CTL-012                   | —                                    |
| REQ-IFC-004  | HZ-008              | CTL-012                   | —                                    |
| REQ-IFC-006  | HZ-008              | CTL-012                   | —                                    |

### Requirements to Verification

| REQ ID       | VER ID     | Method        | Artifact                                              | Status  | CMP ID(s)                              | MODE ID(s)           |
|--------------|------------|---------------|-------------------------------------------------------|---------|----------------------------------------|----------------------|
| REQ-FUN-001  | VER-T-001  | Test          | Flow rate range and increment test                    | Planned | CMP-MCB-01B, CMP-PMA-01A/B            | MODE-001             |
| REQ-FUN-002  | VER-T-002  | Test          | Flow rate accuracy test per IEC 60601-2-24            | Planned | CMP-MCB-01B, CMP-PMA-01A/B            | MODE-001             |
| REQ-FUN-003  | VER-T-003  | Test          | Closed-loop control loop timing test                  | Planned | CMP-MCB-01B, CMP-PMA-01B              | MODE-001             |
| REQ-FUN-004  | VER-T-024  | Test          | Volume tracking accuracy test                         | Planned | CMP-MCB-01B                            | MODE-001             |
| REQ-FUN-005  | VER-T-025  | Test          | KVO transition and alarm test                         | Planned | CMP-MCB-01B/D, CMP-UIM-01B            | MODE-001 -> MODE-003 |
| REQ-FUN-006  | VER-T-005  | Test          | Bolus delivery with DERS hard limit test              | Planned | CMP-MCB-01B/C, CMP-PMA-01A            | MODE-002             |
| REQ-FUN-007  | VER-T-006  | Test          | DERS soft limit alert test                            | Planned | CMP-MCB-01C                            | MODE-005, MODE-001   |
| REQ-FUN-008  | VER-T-007  | Test          | DERS hard limit enforcement test                      | Planned | CMP-MCB-01C                            | MODE-005             |
| REQ-FUN-009  | VER-T-026  | Test          | DERS override logging test                            | Planned | CMP-MCB-01C                            | MODE-001             |
| REQ-FUN-010  | VER-T-027  | Test          | Drug library capacity and structure test              | Planned | CMP-MCB-01C                            | MODE-005             |
| REQ-FUN-011  | VER-T-015  | Test          | Drug library integrity verification test              | Planned | CMP-MCB-01C, CMP-WCM-01C              | MODE-005             |
| REQ-FUN-012  | VER-T-009  | Test          | Downstream occlusion alarm timing test                | Planned | CMP-MCB-01D, CMP-PMA-01E, CMP-UIM-01B | MODE-001            |
| REQ-FUN-013  | VER-T-008  | Test          | Air-in-line detection and pause test                  | Planned | CMP-MCB-01D, CMP-PMA-01D, CMP-UIM-01B | MODE-001            |
| REQ-FUN-014  | VER-T-014  | Test          | Alarm signal characteristics test (IEC 60601-1-8)    | Planned | CMP-MCB-01D, CMP-UIM-01B              | MODE-001, MODE-004   |
| REQ-FUN-015  | VER-T-028  | Test          | Flow deviation alarm threshold and timing test        | Planned | CMP-MCB-01D, CMP-PMA-01B              | MODE-001             |
| REQ-FUN-016  | VER-T-010  | Test          | Upstream occlusion alarm timing test                  | Planned | CMP-MCB-01D, CMP-PMA-01E              | MODE-001             |
| REQ-FUN-017  | VER-T-011  | Test          | Door-open detection and mode transition test          | Planned | CMP-MCB-01D, CMP-PMA-01F              | MODE-001 -> MODE-004 |
| REQ-FUN-018  | VER-T-017  | Test          | Flow sensor loss fallback test                        | Planned | CMP-MCB-01B, CMP-MCB-01D              | MODE-001             |
| REQ-FUN-019  | VER-T-029  | Test          | Battery monitoring and alarm threshold test           | Planned | CMP-MCB-01K                            | MODE-001             |
| REQ-FUN-020  | VER-T-018  | Test          | Display refresh rate and content test                 | Planned | CMP-UIM-01A, CMP-UIM-01C              | MODE-001             |
| REQ-FUN-021  | VER-T-030  | Test          | Touch response latency test                           | Planned | CMP-UIM-01A, CMP-UIM-01C              | MODE-001, MODE-005   |
| REQ-FUN-022  | VER-T-007  | Test          | Programming workflow DERS enforcement test            | Planned | CMP-UIM-01C, CMP-MCB-01C              | MODE-005             |
| REQ-FUN-022  | VER-I-001  | Inspection    | UI workflow code path inspection for DERS bypass      | Planned | CMP-UIM-01C                            | —                    |
| REQ-FUN-023  | VER-T-019  | Test          | Power-up self-test coverage and timing test           | Planned | CMP-MCB-01, CMP-MCB-01J               | MODE-005             |
| REQ-SAF-001  | VER-T-004  | Test          | Anti-free-flow clamp engagement test (mechanical)     | Planned | CMP-PMA-01C                            | MODE-001, MODE-004   |
| REQ-SAF-001  | VER-A-001  | Analysis      | Anti-free-flow clamp endurance analysis (100K cycles) | Planned | CMP-PMA-01C                            | —                    |
| REQ-SAF-002  | VER-T-012  | Test          | Watchdog timeout and processor reset test             | Planned | CMP-MCB-01J, CMP-MCB-01A              | MODE-001             |
| REQ-SAF-003  | VER-T-004  | Test          | Hardware motor current limiter test                   | Planned | CMP-MCB-01H                            | MODE-001             |
| REQ-SAF-003  | VER-A-001  | Analysis      | Motor current limiter circuit analysis                | Planned | CMP-MCB-01H                            | —                    |
| REQ-SAF-004  | VER-T-013  | Test          | Gross flow discrepancy alarm and mode transition test | Planned | CMP-MCB-01B, CMP-MCB-01D              | MODE-001 -> MODE-004 |
| REQ-SAF-005  | VER-T-020  | Test          | RTOS MPU partition isolation test                     | Planned | CMP-MCB-01E                            | MODE-001             |
| REQ-SAF-005  | VER-A-002  | Analysis      | RTOS MPU configuration review                         | Planned | CMP-MCB-01E                            | —                    |
| REQ-SAF-006  | VER-T-013  | Test          | Safe state transition timing test                     | Planned | CMP-MCB-01B/D, CMP-PMA-01C, CMP-UIM-01B | MODE-001          |
| REQ-SAF-007  | VER-T-014  | Test          | Alarm independence from display test                  | Planned | CMP-MCB-01D, CMP-UIM-01B              | MODE-001             |
| REQ-SAF-008  | VER-T-031  | Test          | Battery runtime endurance test at 125 mL/hr          | Planned | CMP-MCB-01K                            | MODE-001             |
| REQ-SAF-009  | VER-T-022  | Test          | DERS operation during network disconnection test      | Planned | CMP-MCB-01C                            | MODE-001             |
| REQ-SAF-010  | VER-T-016  | Test          | Library update rejection during active infusion test  | Planned | CMP-MCB-01C, CMP-WCM-01C              | MODE-001             |
| REQ-IFC-001  | VER-T-032  | Test          | EHR status message timing and content test            | Planned | CMP-WCM-01B                            | MODE-001             |
| REQ-IFC-002  | VER-T-033  | Test          | Drug order reception and pre-population test          | Planned | CMP-WCM-01B, CMP-MCB-01C              | MODE-005             |
| REQ-IFC-003  | VER-T-020  | Test          | TLS encryption and mutual authentication test         | Planned | CMP-MCB-01G, CMP-WCM-01A              | MODE-001, MODE-005   |
| REQ-IFC-004  | VER-T-021  | Test          | Wi-Fi authentication protocol test                    | Planned | CMP-WCM-01A                            | MODE-005             |
| REQ-IFC-005  | VER-T-034  | Test          | Alarm forwarding latency test                         | Planned | CMP-WCM-01B, CMP-MCB-01D              | MODE-004             |
| REQ-IFC-006  | VER-T-022  | Test          | MCB input validation and malformed message rejection  | Planned | CMP-MCB-01B                            | MODE-001             |
| REQ-PRF-001  | VER-T-035  | Test          | Trumpet curve compliance test                         | Planned | CMP-MCB-01B, CMP-PMA-01A              | MODE-001             |
| REQ-PRF-002  | VER-T-036  | Test          | Power-up timing test at temperature extremes          | Planned | CMP-MCB-01, CMP-UIM-01, CMP-WCM-01    | MODE-005             |
| REQ-PRF-003  | VER-T-037  | Test          | Power consumption measurement test                    | Planned | CMP-MCB-01K                            | MODE-001             |
| REQ-PRF-004  | VER-T-038  | Test          | Power interruption auto-resume test                   | Planned | CMP-MCB-01K, CMP-MCB-01B              | MODE-001             |

## Reverse Traces

### Components to Requirements

| CMP ID        | Component Name                     | REQ ID(s)                                                                        | Gap? |
|---------------|------------------------------------|----------------------------------------------------------------------------------|------|
| CMP-PMA-01    | Pump Mechanism Assembly            | REQ-FUN-001 (via children)                                                       | No   |
| CMP-PMA-01A   | Peristaltic Pump Drive             | REQ-FUN-001, REQ-FUN-002, REQ-FUN-006, REQ-PRF-001                              | No   |
| CMP-PMA-01B   | Flow Sensor                        | REQ-FUN-001, REQ-FUN-002, REQ-FUN-003, REQ-FUN-015                              | No   |
| CMP-PMA-01C   | Anti-Free-Flow Clamp               | REQ-SAF-001, REQ-SAF-006                                                         | No   |
| CMP-PMA-01D   | Air-in-Line Detector               | REQ-FUN-013                                                                      | No   |
| CMP-PMA-01E   | Occlusion Pressure Sensor          | REQ-FUN-012, REQ-FUN-016                                                         | No   |
| CMP-PMA-01F   | Door Latch Sensor                  | REQ-FUN-017                                                                      | No   |
| CMP-MCB-01    | Main Control Board                 | REQ-FUN-023, REQ-PRF-002 (system-level)                                          | No   |
| CMP-MCB-01A   | Main Processor                     | REQ-SAF-002                                                                      | No   |
| CMP-MCB-01B   | Infusion Control Application       | REQ-FUN-001, REQ-FUN-002, REQ-FUN-003, REQ-FUN-004, REQ-FUN-018, REQ-SAF-004, REQ-IFC-006, REQ-PRF-001, REQ-PRF-004 | No |
| CMP-MCB-01C   | DERS Engine                        | REQ-FUN-007, REQ-FUN-008, REQ-FUN-009, REQ-FUN-010, REQ-FUN-011, REQ-FUN-022, REQ-SAF-009, REQ-SAF-010, REQ-IFC-002 | No |
| CMP-MCB-01D   | Alarm Management Application       | REQ-FUN-005, REQ-FUN-012, REQ-FUN-013, REQ-FUN-014, REQ-FUN-015, REQ-FUN-016, REQ-FUN-017, REQ-SAF-004, REQ-SAF-006, REQ-SAF-007, REQ-IFC-005 | No |
| CMP-MCB-01E   | RTOS (SOUP)                        | REQ-SAF-005                                                                      | No   |
| CMP-MCB-01F   | TCP/IP Stack (SOUP)                | REQ-IFC-003 (via network stack)                                                  | No   |
| CMP-MCB-01G   | TLS Library (SOUP)                 | REQ-IFC-003                                                                      | No   |
| CMP-MCB-01H   | Motor Driver Circuit               | REQ-SAF-003                                                                      | No   |
| CMP-MCB-01J   | Safety Watchdog                    | REQ-SAF-002, REQ-FUN-023                                                         | No   |
| CMP-MCB-01K   | Power Management Unit              | REQ-FUN-019, REQ-SAF-008, REQ-PRF-003, REQ-PRF-004                              | No   |
| CMP-UIM-01    | User Interface Module              | REQ-PRF-002 (via children)                                                       | No   |
| CMP-UIM-01A   | Touchscreen Display                | REQ-FUN-020, REQ-FUN-021                                                         | No   |
| CMP-UIM-01B   | Alarm Annunciator                  | REQ-FUN-005, REQ-FUN-012, REQ-FUN-013, REQ-FUN-014, REQ-SAF-006, REQ-SAF-007   | No   |
| CMP-UIM-01C   | Display Application Software       | REQ-FUN-020, REQ-FUN-021, REQ-FUN-022                                            | No   |
| CMP-WCM-01    | Wireless Communication Module      | REQ-PRF-002 (via children)                                                       | No   |
| CMP-WCM-01A   | Wi-Fi Radio                        | REQ-IFC-003, REQ-IFC-004                                                         | No   |
| CMP-WCM-01B   | EHR Interface Application          | REQ-IFC-001, REQ-IFC-002, REQ-IFC-005                                            | No   |
| CMP-WCM-01C   | Drug Library Update Manager        | REQ-FUN-011, REQ-SAF-010                                                         | No   |

### Hazards to Controls to Requirements

| HZ ID   | CTL ID(s)              | REQ ID(s)                                                                              | Fully Mitigated? |
|---------|------------------------|----------------------------------------------------------------------------------------|------------------|
| HZ-001  | CTL-001, CTL-002       | REQ-FUN-002, REQ-FUN-003, REQ-FUN-015, REQ-SAF-003, REQ-SAF-004                       | Yes              |
| HZ-002  | CTL-003                | REQ-FUN-006, REQ-FUN-007, REQ-FUN-008                                                  | Yes              |
| HZ-003  | CTL-003, CTL-009       | REQ-FUN-007, REQ-FUN-008, REQ-FUN-011, REQ-FUN-022, REQ-SAF-010                       | Yes              |
| HZ-004  | CTL-004                | REQ-FUN-013                                                                            | Yes              |
| HZ-005  | CTL-006                | REQ-SAF-001, REQ-FUN-017                                                               | Yes              |
| HZ-006  | CTL-007                | REQ-SAF-002, REQ-SAF-006                                                               | Yes              |
| HZ-007  | CTL-008                | REQ-FUN-014, REQ-SAF-007                                                               | Yes              |
| HZ-008  | CTL-012, CTL-009       | REQ-IFC-003, REQ-IFC-004, REQ-IFC-006, REQ-SAF-005, REQ-SAF-009, REQ-FUN-011          | Yes              |
| HZ-009  | CTL-009                | REQ-FUN-011, REQ-SAF-010                                                               | Yes              |
| HZ-010  | CTL-005, CTL-001       | REQ-FUN-012, REQ-FUN-015, REQ-FUN-016                                                  | Yes              |
| HZ-011  | CTL-010                | REQ-FUN-018, REQ-FUN-020                                                               | Yes              |
| HZ-012  | CTL-007, CTL-011       | REQ-SAF-002, REQ-SAF-006, REQ-FUN-023                                                  | Yes              |

### Verification to Requirements

| VER ID     | REQ ID(s)                                   | EVD ID(s)       | Status  |
|------------|---------------------------------------------|-----------------|---------|
| VER-T-001  | REQ-FUN-001                                 | EVD-001         | Planned |
| VER-T-002  | REQ-FUN-002                                 | EVD-001         | Planned |
| VER-T-003  | REQ-FUN-003                                 | EVD-001         | Planned |
| VER-T-004  | REQ-SAF-001, REQ-SAF-003                    | EVD-002         | Planned |
| VER-T-005  | REQ-FUN-006                                 | EVD-003         | Planned |
| VER-T-006  | REQ-FUN-007                                 | EVD-003         | Planned |
| VER-T-007  | REQ-FUN-008, REQ-FUN-022                    | EVD-003         | Planned |
| VER-T-008  | REQ-FUN-013                                 | EVD-004         | Planned |
| VER-T-009  | REQ-FUN-012                                 | EVD-004         | Planned |
| VER-T-010  | REQ-FUN-016                                 | EVD-004         | Planned |
| VER-T-011  | REQ-SAF-001, REQ-FUN-017                    | EVD-002         | Planned |
| VER-T-012  | REQ-SAF-002                                 | EVD-005         | Planned |
| VER-T-013  | REQ-SAF-004, REQ-SAF-006                    | EVD-005         | Planned |
| VER-T-014  | REQ-FUN-014, REQ-SAF-007                    | EVD-006         | Planned |
| VER-T-015  | REQ-FUN-011                                 | EVD-007         | Planned |
| VER-T-016  | REQ-SAF-010                                 | EVD-007         | Planned |
| VER-T-017  | REQ-FUN-018                                 | EVD-008         | Planned |
| VER-T-018  | REQ-FUN-020                                 | EVD-008         | Planned |
| VER-T-019  | REQ-FUN-023                                 | EVD-009         | Planned |
| VER-T-020  | REQ-SAF-005, REQ-IFC-003                    | EVD-010         | Planned |
| VER-T-021  | REQ-IFC-004                                 | EVD-010         | Planned |
| VER-T-022  | REQ-SAF-009, REQ-IFC-006                    | EVD-010         | Planned |
| VER-T-024  | REQ-FUN-004                                 | EVD-001         | Planned |
| VER-T-025  | REQ-FUN-005                                 | EVD-001         | Planned |
| VER-T-026  | REQ-FUN-009                                 | EVD-003         | Planned |
| VER-T-027  | REQ-FUN-010                                 | EVD-003         | Planned |
| VER-T-028  | REQ-FUN-015                                 | EVD-001         | Planned |
| VER-T-029  | REQ-FUN-019                                 | EVD-011         | Planned |
| VER-T-030  | REQ-FUN-021                                 | EVD-012         | Planned |
| VER-T-031  | REQ-SAF-008                                 | EVD-011         | Planned |
| VER-T-032  | REQ-IFC-001                                 | EVD-013         | Planned |
| VER-T-033  | REQ-IFC-002                                 | EVD-013         | Planned |
| VER-T-034  | REQ-IFC-005                                 | EVD-013         | Planned |
| VER-T-035  | REQ-PRF-001                                 | EVD-001         | Planned |
| VER-T-036  | REQ-PRF-002                                 | EVD-009         | Planned |
| VER-T-037  | REQ-PRF-003                                 | EVD-014         | Planned |
| VER-T-038  | REQ-PRF-004                                 | EVD-011         | Planned |
| VER-A-001  | REQ-SAF-001, REQ-SAF-003                    | EVD-002         | Planned |
| VER-A-002  | REQ-SAF-005                                 | EVD-010         | Planned |
| VER-I-001  | REQ-FUN-022                                 | EVD-003         | Planned |

## Gap Register

| Gap ID  | Type                   | Entity ID     | Description                                    | Disposition |
|---------|------------------------|---------------|------------------------------------------------|-------------|
| GAP-001 | Deferred verification  | REQ-PRF-001   | Trumpet curve test requires final production pump mechanism; cannot verify on prototype | Planned (design transfer) |

## Coverage Summary

- Requirements with architecture allocation: 42/42 (100%)
- Safety requirements with hazard/control source: 16/16 (100%) (10 REQ-SAF + 6 REQ-FUN with HZ/CTL source)
- Requirements with verification evidence: 42/42 (100%)
- Components with at least one requirement: 26/27 (96%) — CMP-PMA-01 is parent-level only (covered by children)
- Hazards with at least one control: 12/12 (100%)
- Controls with at least one requirement: 12/12 (100%)
- Verification activities with evidence artifact: 40/40 (100%)
- Gaps registered: 1 (planned disposition)
