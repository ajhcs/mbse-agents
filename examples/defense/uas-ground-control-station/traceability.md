# Traceability

## Trace Strategy

This traceability matrix establishes bidirectional linkage across all GCS system engineering artifacts. Forward traces demonstrate that every requirement is allocated, sourced, and verified. Reverse traces confirm that every component, hazard, and verification activity connects back to a requirement. Gaps are first-class entries with disposition, not omissions.

**Traced entities:**
- Requirements (REQ-) to architecture components (CMP-)
- Requirements (REQ-) to hazard/control sources (HZ-, CTL-)
- Requirements (REQ-) to verification activities (VER-)
- Verification activities (VER-) to evidence artifacts (EVD-)
- Components (CMP-) back to requirements
- Hazards (HZ-) through controls (CTL-) to requirements

## Forward Traces

### Requirements to Architecture

| REQ ID       | Statement (short)                              | CMP ID(s)                                    | Allocation Rationale                               |
|--------------|-------------------------------------------------|----------------------------------------------|-----------------------------------------------------|
| REQ-FUN-001  | Create mission plan (500 waypoints)            | CMP-MMC-01B                                  | Mission planning executes on MMC                    |
| REQ-FUN-002  | Validate plan for airspace/terrain/fuel         | CMP-MMC-01B                                  | Plan validation in mission planning application     |
| REQ-FUN-003  | Display AV state at 10 Hz                       | CMP-MMC-01A, CMP-MMC-01D                    | Flight processor computes; display renders          |
| REQ-FUN-004  | Flight command latency ≤ 250 ms                 | CMP-MMC-01A                                  | Flight management processor generates commands      |
| REQ-FUN-005  | Simultaneous control of four AVs                | CMP-MMC-01A, CMP-CLT-01D                    | MMC manages AV state; CLT routes per vehicle        |
| REQ-FUN-006  | Detect C2 link loss within 10 seconds           | CMP-MMC-01F                                  | Lost link manager on MMC                            |
| REQ-FUN-007  | Initiate lost link procedure, ATC notification  | CMP-MMC-01F, CMP-MMC-01C                    | Lost link manager triggers; airspace module notifies|
| REQ-FUN-008  | Flight termination with two-operator auth       | CMP-MMC-01A                                  | Flight management processor handles termination     |
| REQ-FUN-009  | ADS-B Out position reports at 1 Hz              | CMP-MMC-01C                                  | Airspace integration module generates reports       |
| REQ-FUN-010  | ACAS Xu advisory within 2 seconds               | CMP-MMC-01C                                  | Airspace integration module processes advisories    |
| REQ-FUN-011  | C2 link failover within 5 seconds               | CMP-CLT-01D, CMP-CLT-01A, CMP-CLT-01B      | Link controller manages failover between paths      |
| REQ-FUN-012  | Link health metrics at 1 Hz                     | CMP-CLT-01D                                  | Link controller monitors and reports                |
| REQ-FUN-013  | Bandwidth allocation with command priority       | CMP-CLT-01D                                  | Link controller implements QoS                      |
| REQ-FUN-014  | COMSEC key lifecycle management                  | CMP-CLT-01C                                  | COMSEC module manages cryptographic keys            |
| REQ-FUN-015  | Multi-vehicle routing without mis-routing        | CMP-CLT-01D                                  | Link controller validates vehicle IDs               |
| REQ-FUN-016  | Sensor pointing at 5 Hz                          | CMP-SCW-01B                                  | Sensor tasking application on SCW                   |
| REQ-FUN-017  | Geofence enforcement and proximity alerts        | CMP-MMC-01A, CMP-MMC-01B                    | Flight management and planning check boundaries     |
| REQ-FUN-018  | Sensor video display ≤ 500 ms latency            | CMP-SCW-01A                                  | Sensor display processor on SCW                     |
| REQ-FUN-019  | Target mensuration 10 m CEP                      | CMP-SCW-01C                                  | Target mensuration engine on SCW                    |
| REQ-FUN-020  | Power-up BIT within 120 seconds                  | CMP-MMC-01, CMP-CLT-01, CMP-SCW-01          | BIT executes on all subsystems                      |
| REQ-FUN-021  | Crypto hash verification of software loads       | CMP-MMC-01, CMP-CLT-01                      | MMC and CLT validate software integrity             |
| REQ-SAF-001  | Auto lost link within 10 seconds                 | CMP-MMC-01F                                  | Lost link manager initiates without operator input  |
| REQ-SAF-002  | Link degradation annunciation within 3 seconds   | CMP-MMC-01F, CMP-CLT-01D                    | Lost link manager + link controller detect and alert|
| REQ-SAF-003  | Independent flight termination path               | CMP-MMC-01A, CMP-CLT-01D                    | Dedicated message type bypasses normal command path  |
| REQ-SAF-004  | Undetected link loss ≤ 1e-6/FH                   | CMP-MMC-01F, CMP-CLT-01D                    | System-level probability budget                     |
| REQ-SAF-005  | Geofence violation rejection                      | CMP-MMC-01A, CMP-MMC-01B                    | Flight management enforces boundary check           |
| REQ-SAF-006  | Heartbeat monitoring with configurable timeout    | CMP-MMC-01F, CMP-CLT-01D                    | Independent heartbeat mechanism                     |
| REQ-SAF-007  | Vehicle ID validation on every command            | CMP-CLT-01D                                  | Link controller validates per outbound message      |
| REQ-SAF-008  | Mission recorder for flight-critical data         | CMP-MMC-01A                                  | Flight management processor logs to recorder        |
| REQ-IFC-001  | Flight commands at 10 Hz / 200 ms latency        | CMP-CLT-01D, CMP-CLT-01A, CMP-CLT-01B      | Link controller and transceivers                    |
| REQ-IFC-002  | Telemetry forwarding within 20 ms                 | CMP-CLT-01D, CMP-CLT-01A, CMP-CLT-01B      | CLT receives and forwards to MMC                    |
| REQ-IFC-003  | Video forwarding latency ≤ 50 ms                  | CMP-CLT-01D, CMP-SCW-01A                    | CLT forwards; SCW display processor receives        |
| REQ-IFC-004  | ADS-B Out per DO-260C                             | CMP-MMC-01C                                  | Airspace integration formats and transmits          |
| REQ-IFC-005  | GCS LAN 100 Mbps with QoS                        | CMP-MMC-01, CMP-CLT-01, CMP-SCW-01          | All subsystems connect via GCS LAN                  |
| REQ-IFC-006  | SATCOM IP/UDP with DSCP marking                   | CMP-CLT-01B                                  | BLOS modem implements DSCP                          |
| REQ-IFC-007  | LOS via MIL-STD-1553B / RS-422                    | CMP-CLT-01A, CMP-CLT-01E, CMP-CLT-01F      | LOS transceiver + antenna control + PSSS adapter    |
| REQ-PRF-001  | Power-up within 120 seconds at -32C to +49C       | CMP-MMC-01, CMP-CLT-01, CMP-SCW-01          | All subsystems must initialize                      |
| REQ-PRF-002  | 24-hour continuous operations                      | CMP-MMC-01, CMP-CLT-01, CMP-SCW-01          | All subsystems must sustain operations              |
| REQ-PRF-003  | Flight command WCET ≤ 40 ms on 50 ms cycle        | CMP-MMC-01A                                  | Flight management processor timing                  |
| REQ-PRF-004  | Total power ≤ 3000 W at max load                   | CMP-MMC-01, CMP-CLT-01, CMP-SCW-01          | All subsystem power consumption                     |
| REQ-PRF-005  | Mensuration within 2 seconds at 10 m CEP           | CMP-SCW-01C                                  | Target mensuration engine computation time          |

### Requirements to Hazards

| REQ ID       | Source HZ ID(s) | Source CTL ID(s)         | Source Clause                     |
|--------------|-----------------|---------------------------|-----------------------------------|
| REQ-FUN-002  | HZ-008          | CTL-008                   | —                                 |
| REQ-FUN-006  | HZ-001          | CTL-001                   | MIL-STD-882E                      |
| REQ-FUN-007  | HZ-001, HZ-002  | CTL-001, CTL-002          | FAA UAS operating procedures      |
| REQ-FUN-008  | HZ-005          | CTL-005                   | MIL-STD-882E                      |
| REQ-FUN-010  | HZ-003          | CTL-003                   | RTCA DO-386                       |
| REQ-FUN-013  | HZ-004          | CTL-006                   | —                                 |
| REQ-FUN-015  | HZ-006          | CTL-007                   | —                                 |
| REQ-FUN-017  | HZ-007          | CTL-008                   | FAA UAS operating procedures      |
| REQ-FUN-020  | HZ-009          | CTL-009                   | —                                 |
| REQ-FUN-021  | HZ-010          | CTL-010                   | DI-SESS-81785A                    |
| REQ-SAF-001  | HZ-001          | CTL-001                   | —                                 |
| REQ-SAF-002  | HZ-002          | CTL-002, CTL-004          | —                                 |
| REQ-SAF-003  | HZ-005          | CTL-005                   | —                                 |
| REQ-SAF-004  | HZ-001          | CTL-001                   | MIL-STD-882E                      |
| REQ-SAF-005  | HZ-007          | CTL-008                   | —                                 |
| REQ-SAF-006  | HZ-001          | CTL-001                   | —                                 |
| REQ-SAF-007  | HZ-006          | CTL-007                   | —                                 |
| REQ-SAF-008  | HZ-009          | CTL-009                   | DI-SESS-81785A                    |

### Requirements to Verification

| REQ ID       | VER ID     | Method       | Artifact                                       | Status  | CMP ID(s)                             | MODE ID(s)          |
|--------------|------------|--------------|------------------------------------------------|---------|---------------------------------------|----------------------|
| REQ-FUN-001  | VER-T-015  | Test         | Mission plan creation test                     | Planned | CMP-MMC-01B                           | MODE-001             |
| REQ-FUN-002  | VER-T-010  | Test         | Plan validation test                           | Planned | CMP-MMC-01B                           | MODE-001             |
| REQ-FUN-003  | VER-T-016  | Test         | AV state display refresh rate test             | Planned | CMP-MMC-01A, CMP-MMC-01D             | MODE-001             |
| REQ-FUN-004  | VER-T-017  | Test         | Flight command latency test                    | Planned | CMP-MMC-01A                           | MODE-001             |
| REQ-FUN-005  | VER-T-018  | Test         | Multi-vehicle simultaneous control test        | Planned | CMP-MMC-01A, CMP-CLT-01D             | MODE-001             |
| REQ-FUN-005  | VER-D-001  | Demonstration| Four-vehicle operational demonstration         | Planned | CMP-MMC-01A, CMP-CLT-01D             | MODE-001             |
| REQ-FUN-006  | VER-T-001  | Test         | C2 link loss detection timing test             | Planned | CMP-MMC-01F                           | MODE-001             |
| REQ-FUN-007  | VER-T-003  | Test         | Lost link procedure execution test             | Planned | CMP-MMC-01F, CMP-MMC-01C             | MODE-001 -> MODE-003 |
| REQ-FUN-008  | VER-T-006  | Test         | Flight termination authentication test         | Planned | CMP-MMC-01A                           | MODE-001, MODE-005   |
| REQ-FUN-009  | VER-T-019  | Test         | ADS-B Out generation test                      | Planned | CMP-MMC-01C                           | MODE-001             |
| REQ-FUN-010  | VER-T-004  | Test         | ACAS advisory processing latency test          | Planned | CMP-MMC-01C                           | MODE-001             |
| REQ-FUN-011  | VER-T-005  | Test         | C2 link failover timing test                   | Planned | CMP-CLT-01D, CMP-CLT-01A/B           | MODE-001 -> MODE-002 |
| REQ-FUN-012  | VER-T-020  | Test         | Link health metrics reporting test             | Planned | CMP-CLT-01D                           | MODE-001             |
| REQ-FUN-013  | VER-T-007  | Test         | Bandwidth reservation under load test          | Planned | CMP-CLT-01D                           | MODE-001             |
| REQ-FUN-013  | VER-A-002  | Analysis     | Bandwidth allocation analysis                  | Planned | CMP-CLT-01D                           | MODE-001             |
| REQ-FUN-014  | VER-T-013  | Test         | COMSEC key management test                     | Planned | CMP-CLT-01C                           | MODE-004             |
| REQ-FUN-015  | VER-T-008  | Test         | Vehicle ID routing validation test             | Planned | CMP-CLT-01D                           | MODE-001             |
| REQ-FUN-016  | VER-T-021  | Test         | Sensor pointing command rate test              | Planned | CMP-SCW-01B                           | MODE-001             |
| REQ-FUN-017  | VER-T-009  | Test         | Geofence enforcement and alerting test         | Planned | CMP-MMC-01A, CMP-MMC-01B             | MODE-001             |
| REQ-FUN-018  | VER-T-022  | Test         | Sensor video display latency test              | Planned | CMP-SCW-01A                           | MODE-001             |
| REQ-FUN-019  | VER-T-014  | Test         | Target mensuration accuracy test               | Planned | CMP-SCW-01C                           | MODE-001             |
| REQ-FUN-019  | VER-A-003  | Analysis     | Mensuration error budget analysis              | Planned | CMP-SCW-01C                           | MODE-001             |
| REQ-FUN-020  | VER-T-011  | Test         | Power-up BIT execution test                    | Planned | CMP-MMC-01, CMP-CLT-01, CMP-SCW-01   | MODE-004             |
| REQ-FUN-021  | VER-T-012  | Test         | Software load integrity verification test      | Planned | CMP-MMC-01, CMP-CLT-01               | MODE-004             |
| REQ-SAF-001  | VER-T-002  | Test         | Automatic lost link initiation test            | Planned | CMP-MMC-01F                           | MODE-001 -> MODE-003 |
| REQ-SAF-002  | VER-T-023  | Test         | Link degradation annunciation test             | Planned | CMP-MMC-01F, CMP-CLT-01D             | MODE-001 -> MODE-002 |
| REQ-SAF-003  | VER-T-024  | Test         | Independent termination path test              | Planned | CMP-MMC-01A, CMP-CLT-01D             | MODE-001             |
| REQ-SAF-003  | VER-A-004  | Analysis     | Termination path independence analysis         | Planned | CMP-MMC-01A, CMP-CLT-01D             | —                    |
| REQ-SAF-004  | VER-A-001  | Analysis     | Undetected link loss probability analysis      | Planned | CMP-MMC-01F, CMP-CLT-01D             | MODE-001             |
| REQ-SAF-005  | VER-T-025  | Test         | Geofence violation rejection test              | Planned | CMP-MMC-01A, CMP-MMC-01B             | MODE-001             |
| REQ-SAF-006  | VER-T-026  | Test         | Heartbeat monitoring timeout test              | Planned | CMP-MMC-01F, CMP-CLT-01D             | MODE-001             |
| REQ-SAF-007  | VER-T-027  | Test         | Vehicle ID validation per-message test         | Planned | CMP-CLT-01D                           | MODE-001             |
| REQ-SAF-008  | VER-T-028  | Test         | Mission recorder fidelity test                 | Planned | CMP-MMC-01A                           | MODE-001             |
| REQ-SAF-008  | VER-I-001  | Inspection   | Mission recorder data completeness inspection  | Planned | CMP-MMC-01A                           | —                    |
| REQ-IFC-001  | VER-T-029  | Test         | Flight command rate and latency test           | Planned | CMP-CLT-01D, CMP-CLT-01A/B           | MODE-001             |
| REQ-IFC-002  | VER-T-030  | Test         | Telemetry forwarding latency test              | Planned | CMP-CLT-01D, CMP-CLT-01A/B           | MODE-001             |
| REQ-IFC-003  | VER-T-031  | Test         | Video forwarding latency test                  | Planned | CMP-CLT-01D, CMP-SCW-01A             | MODE-001             |
| REQ-IFC-004  | VER-T-032  | Test         | ADS-B Out format compliance test               | Planned | CMP-MMC-01C                           | MODE-001             |
| REQ-IFC-005  | VER-T-033  | Test         | GCS LAN bandwidth and QoS test                 | Planned | CMP-MMC-01, CMP-CLT-01, CMP-SCW-01   | MODE-001             |
| REQ-IFC-006  | VER-T-034  | Test         | SATCOM DSCP marking test                       | Planned | CMP-CLT-01B                           | MODE-001             |
| REQ-IFC-007  | VER-T-035  | Test         | LOS MIL-STD-1553B / RS-422 interface test      | Planned | CMP-CLT-01A, CMP-CLT-01E, CMP-CLT-01F| MODE-001             |
| REQ-PRF-001  | VER-T-036  | Test         | Power-up timing at temperature extremes test   | Planned | CMP-MMC-01, CMP-CLT-01, CMP-SCW-01   | MODE-004             |
| REQ-PRF-002  | VER-T-037  | Test         | 24-hour endurance test                         | Planned | CMP-MMC-01, CMP-CLT-01, CMP-SCW-01   | MODE-001             |
| REQ-PRF-003  | VER-T-038  | Test         | Flight command WCET measurement test           | Planned | CMP-MMC-01A                           | MODE-001             |
| REQ-PRF-003  | VER-A-005  | Analysis     | WCET timing margin analysis                    | Planned | CMP-MMC-01A                           | MODE-001             |
| REQ-PRF-004  | VER-T-039  | Test         | Total power consumption test                   | Planned | CMP-MMC-01, CMP-CLT-01, CMP-SCW-01   | MODE-001             |
| REQ-PRF-005  | VER-T-040  | Test         | Mensuration response time test                 | Planned | CMP-SCW-01C                           | MODE-001             |

## Reverse Traces

### Components to Requirements

| CMP ID        | Component Name                     | REQ ID(s)                                                                    | Gap? |
|---------------|------------------------------------|------------------------------------------------------------------------------|------|
| CMP-MMC-01    | Mission Management Computer        | REQ-FUN-020, REQ-FUN-021, REQ-IFC-005, REQ-PRF-001, REQ-PRF-002, REQ-PRF-004 | No |
| CMP-MMC-01A   | MMC Flight Management Processor    | REQ-FUN-003, REQ-FUN-004, REQ-FUN-005, REQ-FUN-008, REQ-FUN-017, REQ-SAF-003, REQ-SAF-005, REQ-SAF-008, REQ-PRF-003 | No |
| CMP-MMC-01B   | MMC Mission Planning Application   | REQ-FUN-001, REQ-FUN-002, REQ-FUN-017, REQ-SAF-005                          | No   |
| CMP-MMC-01C   | MMC Airspace Integration Module    | REQ-FUN-007, REQ-FUN-009, REQ-FUN-010, REQ-IFC-004                          | No   |
| CMP-MMC-01D   | MMC Operator Display Unit          | REQ-FUN-003                                                                  | No   |
| CMP-MMC-01E   | MMC FACE TSS Runtime               | —                                                                            | YES  |
| CMP-MMC-01F   | MMC Lost Link Manager              | REQ-FUN-006, REQ-FUN-007, REQ-SAF-001, REQ-SAF-002, REQ-SAF-004, REQ-SAF-006 | No |
| CMP-CLT-01    | C2 Link Terminal                   | REQ-FUN-020, REQ-FUN-021, REQ-IFC-005, REQ-PRF-001, REQ-PRF-002, REQ-PRF-004 | No |
| CMP-CLT-01A   | CLT LOS Transceiver                | REQ-FUN-011, REQ-IFC-001, REQ-IFC-002, REQ-IFC-007                          | No   |
| CMP-CLT-01B   | CLT BLOS Modem                     | REQ-FUN-011, REQ-IFC-001, REQ-IFC-002, REQ-IFC-006                          | No   |
| CMP-CLT-01C   | CLT COMSEC Module                  | REQ-FUN-014                                                                  | No   |
| CMP-CLT-01D   | CLT Link Controller                | REQ-FUN-005, REQ-FUN-011, REQ-FUN-012, REQ-FUN-013, REQ-FUN-015, REQ-SAF-002, REQ-SAF-003, REQ-SAF-004, REQ-SAF-006, REQ-SAF-007, REQ-IFC-001, REQ-IFC-002 | No |
| CMP-CLT-01E   | CLT Antenna Control Unit           | REQ-IFC-007                                                                  | No   |
| CMP-CLT-01F   | CLT FACE PSSS Adapter              | REQ-IFC-007                                                                  | No   |
| CMP-SCW-01    | Sensor Control Workstation         | REQ-FUN-020, REQ-IFC-005, REQ-PRF-001, REQ-PRF-002, REQ-PRF-004            | No   |
| CMP-SCW-01A   | SCW Sensor Display Processor       | REQ-FUN-018, REQ-IFC-003                                                     | No   |
| CMP-SCW-01B   | SCW Sensor Tasking Application     | REQ-FUN-016                                                                  | No   |
| CMP-SCW-01C   | SCW Target Mensuration Engine      | REQ-FUN-019, REQ-PRF-005                                                     | No   |
| CMP-SCW-01D   | SCW Operator Display Unit          | —                                                                            | YES  |

### Hazards to Controls to Requirements

| HZ ID   | CTL ID(s)       | REQ ID(s)                                                                        | Fully Mitigated? |
|---------|-----------------|----------------------------------------------------------------------------------|------------------|
| HZ-001  | CTL-001         | REQ-FUN-006, REQ-SAF-001, REQ-SAF-004, REQ-SAF-006                              | Yes              |
| HZ-002  | CTL-001, CTL-002, CTL-004 | REQ-FUN-007, REQ-SAF-001, REQ-SAF-002, REQ-FUN-011                     | Yes              |
| HZ-003  | CTL-003         | REQ-FUN-010                                                                      | Yes              |
| HZ-004  | CTL-006         | REQ-FUN-013                                                                      | Yes              |
| HZ-005  | CTL-005         | REQ-FUN-008, REQ-SAF-003                                                         | Yes              |
| HZ-006  | CTL-007         | REQ-FUN-015, REQ-SAF-007                                                         | Yes              |
| HZ-007  | CTL-008         | REQ-FUN-002, REQ-FUN-017, REQ-SAF-005                                            | Yes              |
| HZ-008  | CTL-008         | REQ-FUN-002                                                                      | Yes              |
| HZ-009  | CTL-009         | REQ-FUN-020, REQ-SAF-008                                                         | Yes              |
| HZ-010  | CTL-010         | REQ-FUN-021                                                                      | Yes              |
| HZ-011  | CTL-011         | REQ-FUN-014                                                                      | Yes              |
| HZ-012  | CTL-012         | REQ-FUN-019                                                                      | Yes              |

### Verification to Requirements

| VER ID     | REQ ID(s)                    | EVD ID(s)        | Status  |
|------------|------------------------------|------------------|---------|
| VER-T-001  | REQ-FUN-006                  | EVD-001          | Planned |
| VER-T-002  | REQ-SAF-001                  | EVD-001          | Planned |
| VER-T-003  | REQ-FUN-007                  | EVD-002          | Planned |
| VER-T-004  | REQ-FUN-010                  | EVD-003          | Planned |
| VER-T-005  | REQ-FUN-011, REQ-SAF-002     | EVD-004          | Planned |
| VER-T-006  | REQ-FUN-008, REQ-SAF-003     | EVD-005          | Planned |
| VER-T-007  | REQ-FUN-013                  | EVD-006          | Planned |
| VER-A-002  | REQ-FUN-013                  | EVD-006          | Planned |
| VER-T-008  | REQ-FUN-015, REQ-SAF-007     | EVD-007          | Planned |
| VER-T-009  | REQ-FUN-017, REQ-SAF-005     | EVD-008          | Planned |
| VER-T-010  | REQ-FUN-002                  | EVD-008          | Planned |
| VER-T-011  | REQ-FUN-020                  | EVD-009          | Planned |
| VER-T-012  | REQ-FUN-021                  | EVD-010          | Planned |
| VER-T-013  | REQ-FUN-014                  | EVD-011          | Planned |
| VER-T-014  | REQ-FUN-019                  | EVD-012          | Planned |
| VER-A-003  | REQ-FUN-019                  | EVD-012          | Planned |
| VER-T-015  | REQ-FUN-001                  | EVD-013          | Planned |
| VER-T-016  | REQ-FUN-003                  | EVD-013          | Planned |
| VER-T-017  | REQ-FUN-004                  | EVD-013          | Planned |
| VER-T-018  | REQ-FUN-005                  | EVD-013          | Planned |
| VER-D-001  | REQ-FUN-005                  | EVD-014          | Planned |
| VER-T-019  | REQ-FUN-009                  | EVD-003          | Planned |
| VER-T-020  | REQ-FUN-012                  | EVD-004          | Planned |
| VER-T-021  | REQ-FUN-016                  | EVD-015          | Planned |
| VER-T-022  | REQ-FUN-018                  | EVD-015          | Planned |
| VER-T-023  | REQ-SAF-002                  | EVD-004          | Planned |
| VER-T-024  | REQ-SAF-003                  | EVD-005          | Planned |
| VER-A-004  | REQ-SAF-003                  | EVD-005          | Planned |
| VER-A-001  | REQ-SAF-004                  | EVD-016          | Planned |
| VER-T-025  | REQ-SAF-005                  | EVD-008          | Planned |
| VER-T-026  | REQ-SAF-006                  | EVD-001          | Planned |
| VER-T-027  | REQ-SAF-007                  | EVD-007          | Planned |
| VER-T-028  | REQ-SAF-008                  | EVD-017          | Planned |
| VER-I-001  | REQ-SAF-008                  | EVD-017          | Planned |
| VER-T-029  | REQ-IFC-001                  | EVD-018          | Planned |
| VER-T-030  | REQ-IFC-002                  | EVD-018          | Planned |
| VER-T-031  | REQ-IFC-003                  | EVD-018          | Planned |
| VER-T-032  | REQ-IFC-004                  | EVD-003          | Planned |
| VER-T-033  | REQ-IFC-005                  | EVD-018          | Planned |
| VER-T-034  | REQ-IFC-006                  | EVD-018          | Planned |
| VER-T-035  | REQ-IFC-007                  | EVD-018          | Planned |
| VER-T-036  | REQ-PRF-001                  | EVD-019          | Planned |
| VER-T-037  | REQ-PRF-002                  | EVD-019          | Planned |
| VER-T-038  | REQ-PRF-003                  | EVD-020          | Planned |
| VER-A-005  | REQ-PRF-003                  | EVD-020          | Planned |
| VER-T-039  | REQ-PRF-004                  | EVD-019          | Planned |
| VER-T-040  | REQ-PRF-005                  | EVD-012          | Planned |

## Gap Register

| Gap ID  | Type                   | Entity ID     | Description                                                                                  | Disposition |
|---------|------------------------|---------------|----------------------------------------------------------------------------------------------|-------------|
| GAP-001 | Orphan component       | CMP-MMC-01E   | FACE TSS Runtime has no direct requirements; transport services are infrastructure supporting all PCS applications but no explicit REQ- allocates to this component | Planned: derive REQ-FUN-022 for FACE TSS data transport performance at next requirements review |
| GAP-002 | Orphan component       | CMP-SCW-01D   | SCW Operator Display Unit has no direct requirements; display hardware is presentation-only with requirements allocated to the display processor software (CMP-SCW-01A) | Accepted: hardware display is COTS with no safety-critical requirements; SCW-01A requirements cover display function |
| GAP-003 | Incomplete verification | REQ-SAF-004   | Quantitative probability target (1e-6/FH) is verified by analysis only (VER-A-001); no test can directly demonstrate this probability. SSAR closure depends on FTA with validated failure rate data | Planned: obtain vendor failure rate data before CDR; SSAR closure contingent on data availability |

## Coverage Summary

- **Requirements with architecture allocation**: 42/42 (100%)
- **Safety requirements with hazard source**: 8/8 (100%)
- **Requirements with verification activity**: 42/42 (100%)
- **Verification activities with evidence artifact**: 46/46 (100%)
- **Components with at least one requirement**: 17/19 (89.5%) -- GAP-001 (CMP-MMC-01E), GAP-002 (CMP-SCW-01D)
- **Hazards with at least one control**: 12/12 (100%)
- **Controls with at least one requirement**: 12/12 (100%)
- **Gaps registered**: 3 (2 planned, 1 accepted)
