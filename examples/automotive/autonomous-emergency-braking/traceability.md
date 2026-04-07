# Traceability

## Trace Strategy

This traceability matrix establishes bidirectional linkage across all AEB system engineering artifacts. Forward traces demonstrate that every requirement is allocated, sourced, and verified. Reverse traces confirm that every component, hazard, and verification activity connects back to a requirement. Gaps are first-class entries with disposition, not omissions.

**Traced entities:**
- Requirements (REQ-) to architecture components (CMP-)
- Requirements (REQ-) to hazard/control/threat sources (HZ-, CTL-, THR-)
- Requirements (REQ-) to verification activities (VER-)
- Verification activities (VER-) to evidence artifacts (EVD-)
- Components (CMP-) back to requirements
- Hazards (HZ-) through controls (CTL-) to requirements

## Forward Traces

### Requirements to Architecture

| REQ ID       | Statement (short)                                 | CMP ID(s)                                    | Allocation Rationale                                |
|--------------|---------------------------------------------------|----------------------------------------------|-----------------------------------------------------|
| REQ-FUN-001  | Camera detection: vehicles 120 m, pedestrians 60 m | CMP-PER-01E, CMP-PER-01B, CMP-CAM-01       | Camera detection runs on Perception ECU              |
| REQ-FUN-002  | Camera DNN detection rate: 99% vehicles, 95% peds  | CMP-PER-01E                                  | DNN model quality is Perception ECU SW               |
| REQ-FUN-003  | Radar detection: 200 m range, accuracy specs       | CMP-PER-01F, CMP-PER-01C, CMP-RAD-01       | Radar detection runs on Perception ECU               |
| REQ-FUN-004  | Radar overhead object filtering                    | CMP-PER-01F                                  | Filtering logic in radar detection SW                |
| REQ-FUN-005  | Sensor fusion: 25 Hz, 3D position, confidence      | CMP-PER-01G                                  | Fusion algorithm on Perception ECU                   |
| REQ-FUN-006  | Fusion confidence scoring: 80% threshold            | CMP-PER-01G                                  | Confidence logic in fusion algorithm                 |
| REQ-FUN-007  | Object tracking: 2 second prediction               | CMP-PER-01G                                  | Tracking in fusion application                       |
| REQ-FUN-008  | Track coasting: 500 ms occlusion continuity         | CMP-PER-01G                                  | Tracking algorithm on Perception ECU                 |
| REQ-FUN-009  | TTC computation and braking level determination     | CMP-PER-01H                                  | Decision logic on Perception ECU                     |
| REQ-FUN-010  | Multi-frame confirmation: 3 cycles before braking   | CMP-PER-01H                                  | Confirmation logic in decision application           |
| REQ-FUN-011  | Brake release: within 200 ms of release decision    | CMP-PER-01H, CMP-BRK-01D                    | Decision on PER; release command to BRK              |
| REQ-FUN-012  | Brake force accuracy: +/- 0.5 m/s^2                | CMP-BRK-01D                                  | Brake request manager on Braking ECU                 |
| REQ-FUN-013  | Brake arbitration: higher demand wins               | CMP-BRK-01D                                  | Arbitration logic in brake request manager           |
| REQ-FUN-014  | Closed-loop brake control: 5 ms cycle, ABS coord    | CMP-BRK-01E, CMP-BRK-01B                    | Pressure controller and valve drivers on Braking ECU |
| REQ-FUN-015  | Deceleration limit: 10 m/s^2 max, ESC override      | CMP-BRK-01D, CMP-BRK-01E                    | Limit logic in brake request manager and controller  |
| REQ-FUN-016  | Driver warning: visual + audible, 500 ms before brake| CMP-PER-01H, CMP-GWY-01D                   | Decision app generates; Gateway routes to HMI        |
| REQ-FUN-017  | Sensor health monitoring: 90% diagnostic coverage    | CMP-PER-01D, CMP-PER-01E, CMP-PER-01F      | Health monitoring in Perception platform              |
| REQ-FUN-018  | Degraded mode transition: within 100 ms              | CMP-PER-01D, CMP-GWY-01D                    | Platform manages mode; Gateway notifies HMI          |
| REQ-FUN-019  | Power-up self-test: 5 seconds, readiness report      | CMP-PER-01, CMP-BRK-01, CMP-GWY-01         | All ECUs execute BIT                                 |
| REQ-FUN-020  | Sensor calibration: +/- 0.5 deg accuracy             | CMP-PER-01E, CMP-PER-01F                    | Calibration routines in detection applications       |
| REQ-FUN-021  | Event data recording: 5 s pre-event, NVM             | CMP-PER-01K                                  | EDR application on Perception ECU                    |
| REQ-FUN-022  | OTA validation: ECDSA, SHA-256, rollback             | CMP-PER-01J, CMP-GWY-01E                    | OTA agent on PER; firewall on GWY                    |
| REQ-SAF-001  | 95% detection rate; undetected collision <= 1e-8/h   | CMP-PER-01E, CMP-PER-01F, CMP-PER-01G      | Both detection paths + fusion                        |
| REQ-SAF-002  | Fusion confirmation: 1 sensor + 3 cycles             | CMP-PER-01G                                  | Confirmation logic in fusion algorithm               |
| REQ-SAF-003  | False positive rate: < 1 per 100,000 km              | CMP-PER-01G, CMP-PER-01H                    | Fusion and decision logic                            |
| REQ-SAF-004  | Brake response: 150 ms from command to pressure      | CMP-BRK-01D, CMP-BRK-01E, CMP-BRK-01B      | Braking actuation path                               |
| REQ-SAF-005  | ESC stability override precedence                    | CMP-BRK-01D, CMP-BRK-01E                    | ESC coordination in brake controller                 |
| REQ-SAF-006  | E2E latency: camera to brake <= 300 ms               | CMP-PER-01, CMP-BRK-01, CMP-GWY-01         | System-level timing budget                           |
| REQ-SAF-007  | Brake release timeout: 3 seconds max                 | CMP-PER-01H, CMP-BRK-01D                    | Decision app + brake request manager                 |
| REQ-SAF-008  | Braking path SPFM >= 99%, LFM >= 90%                | CMP-BRK-01A, CMP-BRK-01B, CMP-BRK-01D, CMP-BRK-01E | Hardware fault metrics for braking ECU      |
| REQ-SAF-009  | Degraded mode: extended TTC x1.5, speed <= 80 km/h   | CMP-PER-01H                                  | Decision logic in degraded mode                      |
| REQ-SAF-010  | SOTIF confidence monitoring: MODE-003 at < 60%        | CMP-PER-01G, CMP-PER-01H                    | Fusion confidence monitoring and decision transition  |
| REQ-SEC-001  | OTA crypto signature: ECDSA P-256                     | CMP-PER-01J, CMP-GWY-01E                    | OTA agent and gateway firewall                       |
| REQ-SEC-002  | OTA anti-rollback version check                       | CMP-PER-01J                                  | OTA agent on Perception ECU                          |
| REQ-SEC-003  | CAN FD message allowlist filtering                    | CMP-GWY-01E                                  | Firewall/IDS on Gateway ECU                          |
| REQ-SEC-004  | E2E Profile 7 on safety CAN FD messages               | CMP-GWY-01C, CMP-BRK-01C                    | BSW E2E protection on both ECUs                      |
| REQ-SEC-005  | CAN FD intrusion detection system                     | CMP-GWY-01E                                  | IDS on Gateway ECU                                   |
| REQ-SEC-006  | Diagnostic security access: ISO 14229 0x27             | CMP-GWY-01C, CMP-BRK-01C                    | BSW security on both ECUs                            |
| REQ-SEC-007  | Secure boot with hardware root of trust                | CMP-PER-01A, CMP-PER-01D                    | Hardware root of trust on Perception SoC             |
| REQ-IFC-001  | Perception to Gateway: 50 Hz, 10 ms, SOME/IP E2E      | CMP-PER-01H, CMP-PER-01D                    | Decision app and Adaptive platform                   |
| REQ-IFC-002  | Gateway to Braking: 5 ms translation, E2E continuity   | CMP-GWY-01D, CMP-GWY-01C                    | Gateway message router and BSW                       |
| REQ-IFC-003  | Vehicle dynamics forwarding: 10 ms, 5 ms latency       | CMP-GWY-01D                                  | Gateway message router                               |
| REQ-IFC-004  | Brake status feedback: 100 Hz, E2E Profile 7           | CMP-BRK-01D, CMP-BRK-01C                    | Braking ECU brake manager and BSW                    |
| REQ-IFC-005  | Powertrain torque reduction request                    | CMP-GWY-01D                                  | Gateway routes torque request to PCM                 |
| REQ-PRF-001  | E2E latency <= 300 ms worst case                       | CMP-PER-01, CMP-BRK-01, CMP-GWY-01         | System-level timing                                  |
| REQ-PRF-002  | DNN inference <= 30 ms at 30 fps                       | CMP-PER-01A, CMP-PER-01E                    | NPU timing on Perception SoC                         |
| REQ-PRF-003  | Continuous operation: -40C to +85C, 5 s startup        | CMP-PER-01, CMP-BRK-01, CMP-GWY-01         | All ECUs                                             |
| REQ-PRF-004  | UN R152 test performance thresholds                    | CMP-PER-01, CMP-BRK-01                      | System-level performance                             |
| REQ-PRF-005  | Total power <= 35 W at max load                        | CMP-PER-01, CMP-BRK-01, CMP-GWY-01         | All ECU power consumption                            |

### Requirements to Hazards

| REQ ID       | Source HZ ID(s)    | Source CTL ID(s)         | Source Clause                     |
|--------------|--------------------|--------------------------|-----------------------------------|
| REQ-SAF-001  | HZ-001, HZ-002     | CTL-001                  | —                                 |
| REQ-SAF-002  | HZ-001, HZ-012     | CTL-002                  | —                                 |
| REQ-SAF-003  | HZ-003             | CTL-003                  | —                                 |
| REQ-SAF-004  | HZ-004             | CTL-004                  | —                                 |
| REQ-SAF-005  | HZ-005             | CTL-005                  | —                                 |
| REQ-SAF-006  | HZ-006             | CTL-006                  | —                                 |
| REQ-SAF-007  | HZ-007             | CTL-007                  | —                                 |
| REQ-SAF-008  | HZ-008             | —                        | ISO 26262-5 Table 4               |
| REQ-SAF-009  | HZ-011             | CTL-011                  | —                                 |
| REQ-SAF-010  | HZ-011, HZ-012     | CTL-011                  | ISO 21448 clause 6.3              |
| REQ-FUN-005  | —                  | CTL-001                  | SG-001                            |
| REQ-FUN-006  | —                  | CTL-002, CTL-003         | SG-002                            |
| REQ-FUN-010  | —                  | CTL-003                  | SG-002                            |
| REQ-FUN-017  | HZ-008             | CTL-008                  | —                                 |
| REQ-FUN-018  | HZ-008             | CTL-008                  | —                                 |
| REQ-FUN-022  | HZ-009             | CTL-009                  | —                                 |
| REQ-SEC-001  | —                  | CTL-009                  | THR-001, THR-002                  |
| REQ-SEC-002  | —                  | CTL-009                  | THR-002                           |
| REQ-SEC-003  | —                  | CTL-010                  | THR-003, THR-004                  |
| REQ-SEC-004  | —                  | CTL-010                  | THR-003, THR-005                  |
| REQ-SEC-005  | —                  | CTL-010                  | THR-003, THR-004                  |
| REQ-SEC-006  | —                  | —                        | THR-006                           |
| REQ-SEC-007  | —                  | CTL-009                  | THR-001, THR-008                  |

### Requirements to Verification

| REQ ID       | VER ID     | Method        | Artifact                                            | Status  | CMP ID(s)                           | MODE ID(s)       |
|--------------|------------|---------------|------------------------------------------------------|---------|-------------------------------------|------------------|
| REQ-FUN-001  | VER-T-001  | Test          | Camera detection range and classification test       | Planned | CMP-PER-01E, CMP-CAM-01            | MODE-001         |
| REQ-FUN-002  | VER-T-002  | Test          | DNN detection rate test (ISO 19206 targets)          | Planned | CMP-PER-01E                         | MODE-001         |
| REQ-FUN-003  | VER-T-003  | Test          | Radar detection range and accuracy test              | Planned | CMP-PER-01F, CMP-RAD-01            | MODE-001         |
| REQ-FUN-004  | VER-T-004  | Test          | Overhead object filtering test                       | Planned | CMP-PER-01F                         | MODE-001         |
| REQ-FUN-005  | VER-T-005  | Test          | Sensor fusion output rate and content test           | Planned | CMP-PER-01G                         | MODE-001         |
| REQ-FUN-006  | VER-T-006  | Test          | Fusion confidence scoring and threshold test         | Planned | CMP-PER-01G                         | MODE-001         |
| REQ-FUN-007  | VER-T-007  | Test          | Object tracking and trajectory prediction test       | Planned | CMP-PER-01G                         | MODE-001         |
| REQ-FUN-008  | VER-T-008  | Test          | Track coasting under occlusion test                  | Planned | CMP-PER-01G                         | MODE-001         |
| REQ-FUN-009  | VER-T-009  | Test          | TTC computation and braking level test               | Planned | CMP-PER-01H                         | MODE-001         |
| REQ-FUN-010  | VER-T-010  | Test          | Multi-frame confirmation test                        | Planned | CMP-PER-01H                         | MODE-001         |
| REQ-FUN-011  | VER-T-011  | Test          | Brake release timing and condition test              | Planned | CMP-PER-01H, CMP-BRK-01D           | MODE-002         |
| REQ-FUN-012  | VER-T-012  | Test          | Brake force accuracy test                            | Planned | CMP-BRK-01D                         | MODE-002         |
| REQ-FUN-013  | VER-T-013  | Test          | Brake arbitration test (AEB vs driver)               | Planned | CMP-BRK-01D                         | MODE-002         |
| REQ-FUN-014  | VER-T-014  | Test          | Closed-loop brake control and ABS coordination test  | Planned | CMP-BRK-01E, CMP-BRK-01B           | MODE-002         |
| REQ-FUN-015  | VER-T-015  | Test          | Deceleration limit and ESC override test             | Planned | CMP-BRK-01D, CMP-BRK-01E           | MODE-002         |
| REQ-FUN-016  | VER-T-016  | Test          | Driver warning timing and content test               | Planned | CMP-PER-01H, CMP-GWY-01D           | MODE-001         |
| REQ-FUN-017  | VER-T-017  | Test          | Sensor health monitoring diagnostic coverage test    | Planned | CMP-PER-01D, CMP-PER-01E, CMP-PER-01F | MODE-001      |
| REQ-FUN-017  | VER-A-001  | Analysis      | Sensor diagnostic coverage analysis                  | Planned | CMP-PER-01E, CMP-PER-01F           | MODE-001         |
| REQ-FUN-018  | VER-T-018  | Test          | Degraded mode transition timing test                 | Planned | CMP-PER-01D, CMP-GWY-01D           | MODE-001 -> MODE-003 |
| REQ-FUN-019  | VER-T-019  | Test          | Power-up self-test execution and timing test         | Planned | CMP-PER-01, CMP-BRK-01, CMP-GWY-01| MODE-004         |
| REQ-FUN-020  | VER-T-020  | Test          | Sensor calibration accuracy test                     | Planned | CMP-PER-01E, CMP-PER-01F           | MODE-004         |
| REQ-FUN-021  | VER-T-021  | Test          | Event data recording content and storage test        | Planned | CMP-PER-01K                         | MODE-005         |
| REQ-FUN-022  | VER-T-022  | Test          | OTA update validation and rollback test              | Planned | CMP-PER-01J, CMP-GWY-01E           | MODE-004         |
| REQ-SAF-001  | VER-T-023  | Test          | Dual-sensor detection rate test campaign             | Planned | CMP-PER-01E, CMP-PER-01F, CMP-PER-01G | MODE-001      |
| REQ-SAF-001  | VER-A-002  | Analysis      | Undetected collision probability analysis            | Planned | CMP-PER-01 (system)                 | MODE-001         |
| REQ-SAF-002  | VER-T-024  | Test          | Fusion confirmation logic test                       | Planned | CMP-PER-01G                         | MODE-001         |
| REQ-SAF-003  | VER-T-025  | Test          | False positive rate measurement test (100k+ km)      | Planned | CMP-PER-01G, CMP-PER-01H           | MODE-001         |
| REQ-SAF-003  | VER-A-003  | Analysis      | False positive rate statistical analysis             | Planned | CMP-PER-01G, CMP-PER-01H           | MODE-001         |
| REQ-SAF-004  | VER-T-026  | Test          | Brake response latency test                          | Planned | CMP-BRK-01D, CMP-BRK-01E           | MODE-002         |
| REQ-SAF-005  | VER-T-027  | Test          | ESC stability override test                          | Planned | CMP-BRK-01D, CMP-BRK-01E           | MODE-002         |
| REQ-SAF-006  | VER-T-028  | Test          | End-to-end latency measurement test                  | Planned | CMP-PER-01, CMP-BRK-01, CMP-GWY-01| MODE-001 -> MODE-002 |
| REQ-SAF-006  | VER-A-004  | Analysis      | Latency budget analysis (component breakdown)        | Planned | CMP-PER-01, CMP-BRK-01, CMP-GWY-01| MODE-001         |
| REQ-SAF-007  | VER-T-029  | Test          | Brake release timeout test                           | Planned | CMP-PER-01H, CMP-BRK-01D           | MODE-002 -> MODE-005 |
| REQ-SAF-008  | VER-A-005  | Analysis      | Hardware fault metric analysis (SPFM, LFM, PMHF)    | Planned | CMP-BRK-01A, CMP-BRK-01B           | —                |
| REQ-SAF-009  | VER-T-030  | Test          | Degraded mode TTC extension and speed limit test     | Planned | CMP-PER-01H                         | MODE-003         |
| REQ-SAF-010  | VER-T-031  | Test          | SOTIF confidence monitoring and MODE-003 transition  | Planned | CMP-PER-01G, CMP-PER-01H           | MODE-001 -> MODE-003 |
| REQ-SAF-010  | VER-A-006  | Analysis      | SOTIF triggering condition coverage analysis         | Planned | CMP-PER-01G                         | MODE-001         |
| REQ-SEC-001  | VER-T-032  | Test          | OTA crypto signature verification test               | Planned | CMP-PER-01J                         | MODE-004         |
| REQ-SEC-002  | VER-T-033  | Test          | OTA anti-rollback test                               | Planned | CMP-PER-01J                         | MODE-004         |
| REQ-SEC-003  | VER-T-034  | Test          | CAN FD message allowlist filtering test              | Planned | CMP-GWY-01E                         | MODE-001         |
| REQ-SEC-004  | VER-T-035  | Test          | E2E Profile 7 protection test                        | Planned | CMP-GWY-01C, CMP-BRK-01C           | MODE-001         |
| REQ-SEC-005  | VER-T-036  | Test          | CAN FD intrusion detection test                      | Planned | CMP-GWY-01E                         | MODE-001         |
| REQ-SEC-006  | VER-T-037  | Test          | Diagnostic security access test                      | Planned | CMP-GWY-01C, CMP-BRK-01C           | MODE-004         |
| REQ-SEC-007  | VER-T-038  | Test          | Secure boot integrity verification test              | Planned | CMP-PER-01A, CMP-PER-01D           | MODE-004         |
| REQ-IFC-001  | VER-T-039  | Test          | Perception-to-Gateway rate and latency test          | Planned | CMP-PER-01H, CMP-PER-01D           | MODE-001         |
| REQ-IFC-002  | VER-T-040  | Test          | Gateway translation latency test                     | Planned | CMP-GWY-01D, CMP-GWY-01C           | MODE-001         |
| REQ-IFC-003  | VER-T-041  | Test          | Vehicle dynamics forwarding latency test             | Planned | CMP-GWY-01D                         | MODE-001         |
| REQ-IFC-004  | VER-T-042  | Test          | Brake status feedback rate and E2E test              | Planned | CMP-BRK-01D, CMP-BRK-01C           | MODE-002         |
| REQ-IFC-005  | VER-T-043  | Test          | Powertrain torque reduction request test             | Planned | CMP-GWY-01D                         | MODE-002         |
| REQ-PRF-001  | VER-T-044  | Test          | End-to-end latency stress test                       | Planned | CMP-PER-01, CMP-BRK-01, CMP-GWY-01| MODE-001         |
| REQ-PRF-001  | VER-A-007  | Analysis      | Worst-case latency analysis                          | Planned | CMP-PER-01, CMP-BRK-01, CMP-GWY-01| MODE-001         |
| REQ-PRF-002  | VER-T-045  | Test          | DNN inference timing test at thermal extremes        | Planned | CMP-PER-01A, CMP-PER-01E           | MODE-001         |
| REQ-PRF-002  | VER-A-008  | Analysis      | NPU WCET and thermal analysis                        | Planned | CMP-PER-01A                         | MODE-001         |
| REQ-PRF-003  | VER-T-046  | Test          | Temperature range and startup timing test            | Planned | CMP-PER-01, CMP-BRK-01, CMP-GWY-01| MODE-004 -> MODE-001 |
| REQ-PRF-004  | VER-T-047  | Test          | UN R152 type approval test campaign                  | Planned | CMP-PER-01, CMP-BRK-01             | MODE-001 -> MODE-002 |
| REQ-PRF-005  | VER-T-048  | Test          | Total power consumption measurement test             | Planned | CMP-PER-01, CMP-BRK-01, CMP-GWY-01| MODE-001         |

## Reverse Traces

### Components to Requirements

| CMP ID        | Component Name                     | REQ ID(s)                                                                                          | Gap? |
|---------------|------------------------------------|-----------------------------------------------------------------------------------------------------|------|
| CMP-PER-01    | Perception ECU                     | REQ-FUN-019, REQ-SAF-006, REQ-PRF-001, REQ-PRF-003, REQ-PRF-004, REQ-PRF-005                     | No   |
| CMP-PER-01A   | Perception SoC                     | REQ-PRF-002, REQ-SEC-007                                                                           | No   |
| CMP-PER-01B   | Camera Interface Module            | REQ-FUN-001                                                                                        | No   |
| CMP-PER-01C   | Radar Interface Module             | REQ-FUN-003                                                                                        | No   |
| CMP-PER-01D   | Perception Adaptive Platform       | REQ-FUN-017, REQ-FUN-018, REQ-FUN-019, REQ-IFC-001, REQ-SEC-007                                  | No   |
| CMP-PER-01E   | Camera Detection Application       | REQ-FUN-001, REQ-FUN-002, REQ-FUN-017, REQ-FUN-020, REQ-SAF-001                                  | No   |
| CMP-PER-01F   | Radar Detection Application        | REQ-FUN-003, REQ-FUN-004, REQ-FUN-017, REQ-FUN-020, REQ-SAF-001                                  | No   |
| CMP-PER-01G   | Sensor Fusion Application          | REQ-FUN-005, REQ-FUN-006, REQ-FUN-007, REQ-FUN-008, REQ-SAF-001, REQ-SAF-002, REQ-SAF-003, REQ-SAF-010 | No |
| CMP-PER-01H   | Collision Decision Application     | REQ-FUN-009, REQ-FUN-010, REQ-FUN-011, REQ-FUN-016, REQ-SAF-003, REQ-SAF-007, REQ-SAF-009, REQ-SAF-010, REQ-IFC-001 | No |
| CMP-PER-01J   | OTA Update Agent                   | REQ-FUN-022, REQ-SEC-001, REQ-SEC-002                                                             | No   |
| CMP-PER-01K   | Event Data Recorder Application    | REQ-FUN-021                                                                                        | No   |
| CMP-BRK-01    | Braking Control ECU                | REQ-FUN-019, REQ-SAF-006, REQ-PRF-001, REQ-PRF-003, REQ-PRF-004, REQ-PRF-005                     | No   |
| CMP-BRK-01A   | Braking Microcontroller            | REQ-SAF-008                                                                                        | No   |
| CMP-BRK-01B   | Brake Valve Driver Stage           | REQ-FUN-014, REQ-SAF-004, REQ-SAF-008                                                             | No   |
| CMP-BRK-01C   | Braking Classic Platform           | REQ-SEC-004, REQ-SEC-006, REQ-IFC-004                                                             | No   |
| CMP-BRK-01D   | Brake Request Manager              | REQ-FUN-011, REQ-FUN-012, REQ-FUN-013, REQ-FUN-015, REQ-SAF-004, REQ-SAF-005, REQ-SAF-007, REQ-SAF-008, REQ-IFC-004 | No |
| CMP-BRK-01E   | Brake Pressure Controller          | REQ-FUN-014, REQ-FUN-015, REQ-SAF-004, REQ-SAF-005, REQ-SAF-008                                  | No   |
| CMP-BRK-01F   | Safety Monitoring Function         | —                                                                                                  | YES  |
| CMP-GWY-01    | Vehicle Gateway ECU                | REQ-FUN-019, REQ-SAF-006, REQ-PRF-001, REQ-PRF-003, REQ-PRF-005                                  | No   |
| CMP-GWY-01A   | Gateway Microcontroller            | —                                                                                                  | YES  |
| CMP-GWY-01B   | Ethernet Switch Module             | —                                                                                                  | YES  |
| CMP-GWY-01C   | Gateway Classic Platform           | REQ-SEC-004, REQ-SEC-006, REQ-IFC-002                                                             | No   |
| CMP-GWY-01D   | Message Router Application         | REQ-FUN-016, REQ-FUN-018, REQ-IFC-002, REQ-IFC-003, REQ-IFC-005                                  | No   |
| CMP-GWY-01E   | Network Firewall / IDS             | REQ-FUN-022, REQ-SEC-001, REQ-SEC-003, REQ-SEC-005                                                | No   |
| CMP-CAM-01    | Front Camera Module                | REQ-FUN-001, REQ-FUN-003                                                                           | No   |
| CMP-RAD-01    | Front Radar Module                 | REQ-FUN-003                                                                                        | No   |

### Hazards to Controls to Requirements

| HZ ID   | CTL ID(s)                | REQ ID(s)                                                                       | Fully Mitigated? |
|---------|--------------------------|---------------------------------------------------------------------------------|------------------|
| HZ-001  | CTL-001, CTL-002         | REQ-FUN-005, REQ-SAF-001, REQ-SAF-002                                          | Yes              |
| HZ-002  | CTL-001, CTL-002         | REQ-FUN-001, REQ-FUN-005, REQ-SAF-001                                          | Yes              |
| HZ-003  | CTL-003                  | REQ-SAF-003, REQ-FUN-010                                                       | Yes              |
| HZ-004  | CTL-004                  | REQ-FUN-012, REQ-FUN-014, REQ-SAF-004                                          | Yes              |
| HZ-005  | CTL-004, CTL-005         | REQ-FUN-015, REQ-SAF-005                                                       | Yes              |
| HZ-006  | CTL-006                  | REQ-PRF-001, REQ-PRF-002, REQ-SAF-006                                          | Yes              |
| HZ-007  | CTL-007                  | REQ-FUN-011, REQ-SAF-007                                                       | Yes              |
| HZ-008  | CTL-008                  | REQ-FUN-017, REQ-FUN-018, REQ-SAF-008                                          | Yes              |
| HZ-009  | CTL-009                  | REQ-FUN-022, REQ-SEC-001, REQ-SEC-002                                          | Yes              |
| HZ-010  | CTL-010                  | REQ-SEC-003, REQ-SEC-004, REQ-SEC-005                                          | Yes              |
| HZ-011  | CTL-001, CTL-011         | REQ-SAF-001, REQ-SAF-009, REQ-SAF-010                                          | Yes              |
| HZ-012  | CTL-002, CTL-011         | REQ-SAF-002, REQ-SAF-010                                                       | Yes              |

### Verification to Requirements

| VER ID     | REQ ID(s)                        | EVD ID(s)     | Status  |
|------------|----------------------------------|---------------|---------|
| VER-T-001  | REQ-FUN-001                      | EVD-001       | Planned |
| VER-T-002  | REQ-FUN-002                      | EVD-001       | Planned |
| VER-T-003  | REQ-FUN-003                      | EVD-002       | Planned |
| VER-T-004  | REQ-FUN-004                      | EVD-002       | Planned |
| VER-T-005  | REQ-FUN-005                      | EVD-003       | Planned |
| VER-T-006  | REQ-FUN-006                      | EVD-003       | Planned |
| VER-T-007  | REQ-FUN-007                      | EVD-003       | Planned |
| VER-T-008  | REQ-FUN-008                      | EVD-003       | Planned |
| VER-T-009  | REQ-FUN-009                      | EVD-004       | Planned |
| VER-T-010  | REQ-FUN-010                      | EVD-004       | Planned |
| VER-T-011  | REQ-FUN-011                      | EVD-005       | Planned |
| VER-T-012  | REQ-FUN-012                      | EVD-006       | Planned |
| VER-T-013  | REQ-FUN-013                      | EVD-006       | Planned |
| VER-T-014  | REQ-FUN-014                      | EVD-006       | Planned |
| VER-T-015  | REQ-FUN-015                      | EVD-006       | Planned |
| VER-T-016  | REQ-FUN-016                      | EVD-007       | Planned |
| VER-T-017  | REQ-FUN-017                      | EVD-008       | Planned |
| VER-A-001  | REQ-FUN-017                      | EVD-008       | Planned |
| VER-T-018  | REQ-FUN-018                      | EVD-008       | Planned |
| VER-T-019  | REQ-FUN-019                      | EVD-009       | Planned |
| VER-T-020  | REQ-FUN-020                      | EVD-010       | Planned |
| VER-T-021  | REQ-FUN-021                      | EVD-011       | Planned |
| VER-T-022  | REQ-FUN-022                      | EVD-012       | Planned |
| VER-T-023  | REQ-SAF-001                      | EVD-013       | Planned |
| VER-A-002  | REQ-SAF-001                      | EVD-014       | Planned |
| VER-T-024  | REQ-SAF-002                      | EVD-013       | Planned |
| VER-T-025  | REQ-SAF-003                      | EVD-015       | Planned |
| VER-A-003  | REQ-SAF-003                      | EVD-015       | Planned |
| VER-T-026  | REQ-SAF-004                      | EVD-006       | Planned |
| VER-T-027  | REQ-SAF-005                      | EVD-006       | Planned |
| VER-T-028  | REQ-SAF-006                      | EVD-016       | Planned |
| VER-A-004  | REQ-SAF-006                      | EVD-016       | Planned |
| VER-T-029  | REQ-SAF-007                      | EVD-005       | Planned |
| VER-A-005  | REQ-SAF-008                      | EVD-017       | Planned |
| VER-T-030  | REQ-SAF-009                      | EVD-018       | Planned |
| VER-T-031  | REQ-SAF-010                      | EVD-018       | Planned |
| VER-A-006  | REQ-SAF-010                      | EVD-019       | Planned |
| VER-T-032  | REQ-SEC-001                      | EVD-012       | Planned |
| VER-T-033  | REQ-SEC-002                      | EVD-012       | Planned |
| VER-T-034  | REQ-SEC-003                      | EVD-020       | Planned |
| VER-T-035  | REQ-SEC-004                      | EVD-020       | Planned |
| VER-T-036  | REQ-SEC-005                      | EVD-020       | Planned |
| VER-T-037  | REQ-SEC-006                      | EVD-020       | Planned |
| VER-T-038  | REQ-SEC-007                      | EVD-012       | Planned |
| VER-T-039  | REQ-IFC-001                      | EVD-021       | Planned |
| VER-T-040  | REQ-IFC-002                      | EVD-021       | Planned |
| VER-T-041  | REQ-IFC-003                      | EVD-021       | Planned |
| VER-T-042  | REQ-IFC-004                      | EVD-021       | Planned |
| VER-T-043  | REQ-IFC-005                      | EVD-021       | Planned |
| VER-T-044  | REQ-PRF-001                      | EVD-016       | Planned |
| VER-A-007  | REQ-PRF-001                      | EVD-016       | Planned |
| VER-T-045  | REQ-PRF-002                      | EVD-022       | Planned |
| VER-A-008  | REQ-PRF-002                      | EVD-022       | Planned |
| VER-T-046  | REQ-PRF-003                      | EVD-023       | Planned |
| VER-T-047  | REQ-PRF-004                      | EVD-024       | Planned |
| VER-T-048  | REQ-PRF-005                      | EVD-023       | Planned |

## Gap Register

| Gap ID  | Type               | Entity ID     | Description                                                                                        | Disposition          |
|---------|--------------------|---------------|----------------------------------------------------------------------------------------------------|----------------------|
| GAP-001 | Orphan component   | CMP-BRK-01F  | Safety Monitoring Function has no explicit requirements allocated; monitoring behavior is derived from REQ-SAF-008 and ISO 26262-5 clause 7.4.4 but no REQ- directly targets this component | Planned: derive REQ-SAF-011 for independent safety monitoring at next requirements review |
| GAP-002 | Orphan component   | CMP-GWY-01A  | Gateway Microcontroller has no direct requirements; hardware requirements are derived from gateway-level REQ-IFC-002 and REQ-IFC-003 but not explicitly allocated to the MCU | Planned: derive hardware-level requirements at detailed design phase |
| GAP-003 | Orphan component   | CMP-GWY-01B  | Ethernet Switch Module has no direct requirements; switch configuration is an implementation detail of IFC-INT-003 and IFC-INT-006 | Accepted: switch configuration is a design artifact, not a separate requirement |
| GAP-004 | Incomplete verification | REQ-SAF-001 | Undetected collision probability (1e-8/h) verified by analysis only (VER-A-002); requires validated field data for sensor detection rates and fusion performance that is not yet available | Planned: complete field data collection before FSA; analysis contingent on data availability |

## Coverage Summary

- **Requirements with architecture allocation**: 49/49 (100%)
- **Safety requirements with hazard source**: 10/10 (100%)
- **Security requirements with threat source**: 7/7 (100%)
- **Requirements with verification activity**: 49/49 (100%)
- **Verification activities with evidence artifact**: 58/58 (100%)
- **Components with at least one requirement**: 22/25 (88.0%) -- GAP-001 (CMP-BRK-01F), GAP-002 (CMP-GWY-01A), GAP-003 (CMP-GWY-01B)
- **Hazards with at least one control**: 12/12 (100%)
- **Controls with at least one requirement**: 11/11 (100%)
- **Gaps registered**: 4 (3 Planned, 1 Accepted)
