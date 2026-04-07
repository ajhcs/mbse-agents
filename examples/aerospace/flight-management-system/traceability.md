# Traceability

## Trace Strategy

This traceability matrix establishes bidirectional linkage across all FMS system engineering artifacts. Forward traces demonstrate that every requirement is allocated, sourced, and verified. Reverse traces confirm that every component, hazard, and verification activity connects back to a requirement. Gaps are first-class entries with disposition, not omissions.

**Traced entities:**
- Requirements (REQ-) to architecture components (CMP-)
- Requirements (REQ-) to hazard/control/threat sources (HZ-, CTL-, THR-)
- Requirements (REQ-) to verification activities (VER-)
- Verification activities (VER-) to evidence artifacts (EVD-)
- Components (CMP-) back to requirements
- Hazards (HZ-) through controls (CTL-) to requirements

## Forward Traces

### Requirements to Architecture

| REQ ID       | Statement (short)                          | CMP ID(s)                                    | Allocation Rationale                             |
|--------------|--------------------------------------------|----------------------------------------------|--------------------------------------------------|
| REQ-FUN-001  | Create lateral flight plan (250 waypoints) | CMP-FMC-01A, CMP-FMC-01B                    | Flight planning executes on both FMC channels    |
| REQ-FUN-002  | Modify active plan without guidance interruption | CMP-FMC-01A, CMP-FMC-01B               | Plan modification must not disrupt guidance cycle |
| REQ-FUN-003  | Process uplinked flight plan amendments    | CMP-FMC-01A, CMP-FMC-01B, CMP-DCU-01B      | DCU receives datalink; FMC processes plan change |
| REQ-FUN-004  | Validate plan feasibility before sequencing| CMP-FMC-01A, CMP-FMC-01B                    | Performance check runs in FMC                    |
| REQ-FUN-005  | Compute position via multi-sensor fusion   | CMP-FMC-01E, CMP-FMC-01F, CMP-DCU-01A      | Nav algorithms on FMC; sensor data via DCU       |
| REQ-FUN-006  | Output position to comparator within 20 ms | CMP-FMC-01E, CMP-FMC-01F, CMP-FMC-01C      | Position flows to hardware comparator            |
| REQ-FUN-007  | Dynamic sensor weighting                   | CMP-FMC-01E, CMP-FMC-01F                    | Weighting logic in nav application               |
| REQ-FUN-008  | Detect and exclude faulty sensor inputs    | CMP-FMC-01E, CMP-FMC-01F                    | FDE algorithm in nav application                 |
| REQ-FUN-009  | Annunciate sensor exclusion to crew        | CMP-FMC-01E, CMP-FMC-01F, CMP-DMC-01C      | FMC detects; DMC displays annunciation           |
| REQ-FUN-010  | Compute and display ANP vs RNP             | CMP-FMC-01E, CMP-FMC-01F, CMP-DMC-01C      | FMC computes; DMC displays                       |
| REQ-FUN-011  | Fuel prediction accuracy +/-3%             | CMP-FMC-01H                                  | Performance application on FMC                   |
| REQ-FUN-012  | Compute optimum cruise altitude/speed      | CMP-FMC-01H                                  | Performance application on FMC                   |
| REQ-FUN-013  | Low-fuel advisory generation               | CMP-FMC-01H, CMP-DMC-01C                    | FMC computes; DMC displays advisory              |
| REQ-FUN-014  | Lateral guidance roll commands at 20 Hz    | CMP-FMC-01G                                  | Guidance application on FMC                      |
| REQ-FUN-015  | Bank angle limits (25/15 deg)              | CMP-FMC-01G                                  | Limit logic in guidance application              |
| REQ-FUN-016  | Vertical guidance within +/-50 ft          | CMP-FMC-01G                                  | VNAV in guidance application                     |
| REQ-FUN-017  | Speed targets respect operating limits     | CMP-FMC-01G                                  | Speed protection in guidance application         |
| REQ-FUN-018  | Guidance mode management and annunciation  | CMP-FMC-01G, CMP-DMC-01C                    | FMC manages modes; DMC displays                  |
| REQ-FUN-019  | Nav display data at 10 Hz to DMC           | CMP-DMC-01A, CMP-DMC-01C                    | DMC renders display pages                        |
| REQ-FUN-020  | CDU response within 200/500 ms             | CMP-DMC-01B, CMP-DMC-01C                    | CDU interface on DMC                             |
| REQ-FUN-021  | Power-up BIT within 90 seconds             | CMP-FMC-01, CMP-DMC-01, CMP-DCU-01          | BIT executes on all LRUs                         |
| REQ-FUN-022  | Nav database CRC + crypto verification     | CMP-DCU-01C, CMP-DCU-01E                    | Data load validation on DCU                      |
| REQ-SAF-001  | Cross-channel position disagree detection  | CMP-FMC-01C, CMP-FMC-01A, CMP-FMC-01B      | Comparator detects; channels provide data        |
| REQ-SAF-002  | Cross-channel guidance disagree detection  | CMP-FMC-01C, CMP-FMC-01G                    | Comparator detects; guidance inhibits            |
| REQ-SAF-003  | Undetected erroneous guidance ≤ 1e-9/FH    | CMP-FMC-01 (system-level)                   | System-level probability budget                  |
| REQ-SAF-004  | Total nav loss annunciation and MODE-003   | CMP-FMC-01A, CMP-FMC-01B, CMP-DMC-01C      | Both channels detect; DMC annunciates            |
| REQ-SAF-005  | Spatial partition isolation                | CMP-FMC-01D                                  | RTOS enforces partition boundaries               |
| REQ-SAF-006  | Temporal partition isolation               | CMP-FMC-01D                                  | RTOS enforces time windows                       |
| REQ-SAF-007  | DMC loss detection and MODE-004            | CMP-FMC-01, CMP-DMC-01                      | FMC detects DMC loss; drives backup display      |
| REQ-SAF-008  | Total FMS loss ≤ 1e-7/FH                   | CMP-FMC-01 (system-level)                   | System-level probability budget                  |
| REQ-SAF-009  | Watchdog monitoring per FMC channel        | CMP-FMC-01A, CMP-FMC-01B                    | Independent watchdog per channel                 |
| REQ-SAF-010  | Comparator in independent hardware         | CMP-FMC-01C                                  | Design constraint on comparator independence     |
| REQ-SEC-001  | Crypto signature for nav database loads    | CMP-DCU-01C, CMP-DCU-01E                    | Crypto verification on DCU                       |
| REQ-SEC-002  | Role-based auth on maintenance port        | CMP-DCU-01C                                  | Auth logic on DCU maintenance port               |
| REQ-SEC-003  | Datalink message format validation         | CMP-DCU-01B, CMP-DCU-01E                    | Validation logic on DCU                          |
| REQ-SEC-004  | One-way FMC-to-DMC data flow               | CMP-FMC-01, CMP-DMC-01                      | AFDX virtual link configuration                  |
| REQ-SEC-005  | MAC on safety-critical AFDX messages       | CMP-FMC-01, CMP-DMC-01, CMP-DCU-01          | All LRUs participate in MAC                      |
| REQ-IFC-001  | Guidance to AFCS at 20 Hz / 50 ms latency  | CMP-FMC-01G, CMP-FMC-01J                   | Guidance app + FPGA I/O                          |
| REQ-IFC-002  | IRS data forwarding within 5 ms            | CMP-DCU-01A, CMP-DCU-01E                    | DCU sensor interface and aggregation             |
| REQ-IFC-003  | Nav data to DMC at 20 Hz / 2 Mbps AFDX    | CMP-FMC-01, CMP-DMC-01                      | FMC transmits; DMC receives                      |
| REQ-IFC-004  | Datalink message forwarding within 500 ms  | CMP-DCU-01B, CMP-DCU-01E                    | DCU datalink interface                           |
| REQ-IFC-005  | Synchronous comparator operation per frame | CMP-FMC-01C                                  | Comparator receives both channels per frame      |
| REQ-IFC-006  | Position/intent to TAWS at 1 Hz            | CMP-FMC-01, CMP-DCU-01A                     | FMC provides; routed via bus                     |
| REQ-IFC-007  | Maintenance port 10 Mbps / 15 min load     | CMP-DCU-01C                                  | Maintenance port on DCU                          |
| REQ-PRF-001  | Position accuracy 0.05 NM (95%)            | CMP-FMC-01E, CMP-FMC-01F                    | Nav algorithm accuracy                           |
| REQ-PRF-002  | Nav continuity ≤ 1e-5/FH loss probability  | CMP-FMC-01E, CMP-FMC-01F                    | Dual-channel nav availability                    |
| REQ-PRF-003  | Power-up within 90 seconds at -40C to +70C | CMP-FMC-01, CMP-DMC-01, CMP-DCU-01          | All LRUs must initialize                        |
| REQ-PRF-004  | Guidance WCET ≤ 15 ms on 20 ms cycle       | CMP-FMC-01G, CMP-FMC-01D                    | Guidance app timing; RTOS scheduling             |
| REQ-PRF-005  | Total power ≤ 150 W at max load            | CMP-FMC-01, CMP-DMC-01, CMP-DCU-01          | All LRU power consumption                       |

### Requirements to Hazards

| REQ ID       | Source HZ ID(s) | Source CTL ID(s)          | Source Clause                     |
|--------------|-----------------|---------------------------|-----------------------------------|
| REQ-SAF-001  | HZ-001          | CTL-001                   | —                                 |
| REQ-SAF-002  | HZ-002          | CTL-002                   | —                                 |
| REQ-SAF-003  | HZ-001          | CTL-001, CTL-002          | 14 CFR 25.1309                    |
| REQ-SAF-004  | HZ-004          | CTL-004                   | —                                 |
| REQ-SAF-005  | HZ-005          | CTL-005                   | —                                 |
| REQ-SAF-006  | HZ-005          | CTL-005                   | —                                 |
| REQ-SAF-007  | HZ-006          | CTL-006                   | —                                 |
| REQ-SAF-008  | HZ-007          | CTL-001                   | 14 CFR 25.1309                    |
| REQ-SAF-009  | HZ-008          | CTL-008                   | —                                 |
| REQ-SAF-010  | HZ-001          | CTL-002                   | ARP4761A CMA                      |
| REQ-FUN-008  | HZ-003          | CTL-003                   | —                                 |
| REQ-FUN-022  | HZ-009          | CTL-009                   | —                                 |
| REQ-SEC-001  | —               | CTL-009                   | THR-001                           |
| REQ-SEC-002  | —               | —                         | THR-002                           |
| REQ-SEC-003  | —               | CTL-009                   | THR-003, THR-004                  |
| REQ-SEC-004  | —               | —                         | THR-005                           |
| REQ-SEC-005  | —               | —                         | THR-006                           |

### Requirements to Verification

| REQ ID       | VER ID     | Method       | Artifact                                        | Status  | CMP ID(s)                  | MODE ID(s)          |
|--------------|------------|--------------|--------------------------------------------------|---------|----------------------------|----------------------|
| REQ-FUN-001  | VER-T-013  | Test         | Flight plan entry test procedure                 | Planned | CMP-FMC-01A, CMP-FMC-01B  | MODE-001             |
| REQ-FUN-002  | VER-T-014  | Test         | In-flight plan modification test                 | Planned | CMP-FMC-01A, CMP-FMC-01B  | MODE-001             |
| REQ-FUN-003  | VER-T-015  | Test         | Datalink plan amendment test                     | Planned | CMP-FMC-01A/B, CMP-DCU-01B| MODE-001             |
| REQ-FUN-004  | VER-T-016  | Test         | Plan feasibility validation test                 | Planned | CMP-FMC-01A, CMP-FMC-01B  | MODE-001             |
| REQ-FUN-005  | VER-T-017  | Test         | Multi-sensor position computation test           | Planned | CMP-FMC-01E/F, CMP-DCU-01A| MODE-001             |
| REQ-FUN-006  | VER-T-018  | Test         | Position output timing test                      | Planned | CMP-FMC-01E/F, CMP-FMC-01C| MODE-001             |
| REQ-FUN-007  | VER-T-019  | Test         | Sensor weighting adaptation test                 | Planned | CMP-FMC-01E, CMP-FMC-01F  | MODE-001, MODE-002   |
| REQ-FUN-008  | VER-T-004  | Test         | Sensor FDE test with fault injection             | Planned | CMP-FMC-01E, CMP-FMC-01F  | MODE-001             |
| REQ-FUN-008  | VER-A-002  | Analysis     | FDE detection probability analysis               | Planned | CMP-FMC-01E, CMP-FMC-01F  | MODE-001             |
| REQ-FUN-009  | VER-T-020  | Test         | Sensor exclusion annunciation test               | Planned | CMP-FMC-01E/F, CMP-DMC-01C| MODE-001             |
| REQ-FUN-010  | VER-T-021  | Test         | ANP/RNP monitoring and alerting test             | Planned | CMP-FMC-01E/F, CMP-DMC-01C| MODE-001             |
| REQ-FUN-011  | VER-T-022  | Test         | Fuel prediction accuracy test                    | Planned | CMP-FMC-01H               | MODE-001             |
| REQ-FUN-011  | VER-A-005  | Analysis     | Fuel prediction statistical analysis             | Planned | CMP-FMC-01H               | MODE-001             |
| REQ-FUN-012  | VER-T-023  | Test         | Optimum cruise computation test                  | Planned | CMP-FMC-01H               | MODE-001             |
| REQ-FUN-013  | VER-T-024  | Test         | Low-fuel advisory test                           | Planned | CMP-FMC-01H, CMP-DMC-01C  | MODE-001             |
| REQ-FUN-014  | VER-T-025  | Test         | Lateral guidance roll command test               | Planned | CMP-FMC-01G               | MODE-001             |
| REQ-FUN-015  | VER-T-026  | Test         | Bank angle limit test                            | Planned | CMP-FMC-01G               | MODE-001             |
| REQ-FUN-016  | VER-T-008  | Test         | Vertical guidance path accuracy test             | Planned | CMP-FMC-01G               | MODE-001             |
| REQ-FUN-016  | VER-A-004  | Analysis     | VNAV descent path error analysis                 | Planned | CMP-FMC-01G               | MODE-001             |
| REQ-FUN-017  | VER-T-027  | Test         | Speed limit protection test                      | Planned | CMP-FMC-01G               | MODE-001             |
| REQ-FUN-018  | VER-T-028  | Test         | Guidance mode transition test                    | Planned | CMP-FMC-01G, CMP-DMC-01C  | MODE-001             |
| REQ-FUN-019  | VER-T-029  | Test         | Navigation display refresh rate test             | Planned | CMP-DMC-01A, CMP-DMC-01C  | MODE-001             |
| REQ-FUN-020  | VER-T-030  | Test         | CDU response timing test                         | Planned | CMP-DMC-01B, CMP-DMC-01C  | MODE-001             |
| REQ-FUN-021  | VER-T-012  | Test         | Power-up BIT execution test                      | Planned | CMP-FMC-01, CMP-DMC-01, CMP-DCU-01 | MODE-005   |
| REQ-FUN-022  | VER-T-010  | Test         | Nav database integrity verification test         | Planned | CMP-DCU-01C, CMP-DCU-01E  | MODE-005             |
| REQ-SAF-001  | VER-T-002  | Test         | Cross-channel position disagree test             | Planned | CMP-FMC-01C, CMP-FMC-01A/B| MODE-001             |
| REQ-SAF-002  | VER-T-003  | Test         | Cross-channel guidance disagree test             | Planned | CMP-FMC-01C, CMP-FMC-01G  | MODE-001             |
| REQ-SAF-003  | VER-A-001  | Analysis     | Quantitative safety analysis (FTA)               | Planned | CMP-FMC-01 (system)       | MODE-001             |
| REQ-SAF-004  | VER-T-005  | Test         | Total nav loss annunciation and mode transition  | Planned | CMP-FMC-01A/B, CMP-DMC-01C| MODE-001 → MODE-003  |
| REQ-SAF-005  | VER-T-006  | Test         | Spatial partition isolation test                 | Planned | CMP-FMC-01D               | MODE-001             |
| REQ-SAF-005  | VER-A-003  | Analysis     | Partition isolation analysis                     | Planned | CMP-FMC-01D               | MODE-001             |
| REQ-SAF-006  | VER-T-031  | Test         | Temporal partition overrun test                  | Planned | CMP-FMC-01D               | MODE-001             |
| REQ-SAF-007  | VER-T-007  | Test         | DMC loss detection and backup display test       | Planned | CMP-FMC-01, CMP-DMC-01    | MODE-001 → MODE-004  |
| REQ-SAF-008  | VER-A-006  | Analysis     | Dual-channel reliability analysis                | Planned | CMP-FMC-01 (system)       | MODE-001             |
| REQ-SAF-009  | VER-T-009  | Test         | Watchdog lockup detection test                   | Planned | CMP-FMC-01A, CMP-FMC-01B  | MODE-001             |
| REQ-SAF-010  | VER-I-001  | Inspection   | Comparator hardware independence inspection      | Planned | CMP-FMC-01C               | —                    |
| REQ-SAF-010  | VER-A-007  | Analysis     | Comparator independence analysis                 | Planned | CMP-FMC-01C               | —                    |
| REQ-SEC-001  | VER-T-010  | Test         | Crypto signature verification test               | Planned | CMP-DCU-01C, CMP-DCU-01E  | MODE-005             |
| REQ-SEC-002  | VER-T-032  | Test         | Maintenance port authentication test             | Planned | CMP-DCU-01C               | MODE-005             |
| REQ-SEC-003  | VER-T-011  | Test         | Datalink message validation and rejection test   | Planned | CMP-DCU-01B, CMP-DCU-01E  | MODE-001             |
| REQ-SEC-004  | VER-T-033  | Test         | FMC-to-DMC one-way data flow test                | Planned | CMP-FMC-01, CMP-DMC-01    | MODE-001             |
| REQ-SEC-004  | VER-A-008  | Analysis     | AFDX virtual link directionality analysis        | Planned | CMP-FMC-01, CMP-DMC-01    | —                    |
| REQ-SEC-005  | VER-T-034  | Test         | AFDX MAC verification test                       | Planned | CMP-FMC-01, CMP-DMC-01, CMP-DCU-01 | MODE-001   |
| REQ-IFC-001  | VER-T-035  | Test         | Guidance command timing and rate test             | Planned | CMP-FMC-01G, CMP-FMC-01J  | MODE-001             |
| REQ-IFC-002  | VER-T-036  | Test         | IRS data forwarding latency test                 | Planned | CMP-DCU-01A, CMP-DCU-01E  | MODE-001             |
| REQ-IFC-003  | VER-T-037  | Test         | FMC-to-DMC bandwidth and rate test               | Planned | CMP-FMC-01, CMP-DMC-01    | MODE-001             |
| REQ-IFC-004  | VER-T-038  | Test         | Datalink forwarding latency test                 | Planned | CMP-DCU-01B, CMP-DCU-01E  | MODE-001             |
| REQ-IFC-005  | VER-T-039  | Test         | Comparator synchronous frame test                | Planned | CMP-FMC-01C               | MODE-001             |
| REQ-IFC-006  | VER-T-040  | Test         | TAWS data output rate test                       | Planned | CMP-FMC-01, CMP-DCU-01A   | MODE-001             |
| REQ-IFC-007  | VER-T-041  | Test         | Maintenance port throughput and load time test    | Planned | CMP-DCU-01C               | MODE-005             |
| REQ-PRF-001  | VER-T-001  | Test         | Position accuracy test campaign                  | Planned | CMP-FMC-01E, CMP-FMC-01F  | MODE-001             |
| REQ-PRF-001  | VER-A-009  | Analysis     | Navigation accuracy Monte Carlo analysis         | Planned | CMP-FMC-01E, CMP-FMC-01F  | MODE-001             |
| REQ-PRF-002  | VER-A-010  | Analysis     | Navigation continuity reliability analysis       | Planned | CMP-FMC-01E, CMP-FMC-01F  | MODE-001             |
| REQ-PRF-003  | VER-T-042  | Test         | Power-up timing test at temperature extremes     | Planned | CMP-FMC-01, CMP-DMC-01, CMP-DCU-01 | MODE-005   |
| REQ-PRF-004  | VER-T-043  | Test         | Guidance WCET measurement test                   | Planned | CMP-FMC-01G, CMP-FMC-01D  | MODE-001             |
| REQ-PRF-004  | VER-A-011  | Analysis     | CAST-32A interference analysis for guidance WCET | Planned | CMP-FMC-01G, CMP-FMC-01D  | MODE-001             |
| REQ-PRF-005  | VER-T-044  | Test         | LRU power consumption test                       | Planned | CMP-FMC-01, CMP-DMC-01, CMP-DCU-01 | MODE-001   |

## Reverse Traces

### Components to Requirements

| CMP ID        | Component Name                     | REQ ID(s)                                                                    | Gap? |
|---------------|------------------------------------|------------------------------------------------------------------------------|------|
| CMP-FMC-01    | Flight Management Computer         | REQ-SAF-003, REQ-SAF-008, REQ-FUN-021, REQ-SAF-007, REQ-SEC-004, REQ-SEC-005, REQ-IFC-003, REQ-IFC-006, REQ-PRF-003, REQ-PRF-005 | No |
| CMP-FMC-01A   | FMC Channel A Processor            | REQ-FUN-001, REQ-FUN-002, REQ-FUN-003, REQ-FUN-004, REQ-SAF-001, REQ-SAF-004, REQ-SAF-009 | No |
| CMP-FMC-01B   | FMC Channel B Processor            | REQ-FUN-001, REQ-FUN-002, REQ-FUN-003, REQ-FUN-004, REQ-SAF-001, REQ-SAF-004, REQ-SAF-009 | No |
| CMP-FMC-01C   | Cross-Channel Comparator           | REQ-FUN-006, REQ-SAF-001, REQ-SAF-002, REQ-SAF-010, REQ-IFC-005            | No   |
| CMP-FMC-01D   | ARINC 653 RTOS                     | REQ-SAF-005, REQ-SAF-006, REQ-PRF-004                                       | No   |
| CMP-FMC-01E   | Nav Application (Ch A)             | REQ-FUN-005, REQ-FUN-006, REQ-FUN-007, REQ-FUN-008, REQ-FUN-009, REQ-FUN-010, REQ-PRF-001, REQ-PRF-002 | No |
| CMP-FMC-01F   | Nav Application (Ch B)             | REQ-FUN-005, REQ-FUN-006, REQ-FUN-007, REQ-FUN-008, REQ-FUN-009, REQ-FUN-010, REQ-PRF-001, REQ-PRF-002 | No |
| CMP-FMC-01G   | Guidance Application               | REQ-FUN-014, REQ-FUN-015, REQ-FUN-016, REQ-FUN-017, REQ-FUN-018, REQ-SAF-002, REQ-IFC-001, REQ-PRF-004 | No |
| CMP-FMC-01H   | Performance Application            | REQ-FUN-011, REQ-FUN-012, REQ-FUN-013                                       | No   |
| CMP-FMC-01J   | FMC FPGA Subsystem                 | REQ-IFC-001                                                                  | No   |
| CMP-DMC-01    | Display Management Computer        | REQ-FUN-021, REQ-SAF-007, REQ-SEC-004, REQ-SEC-005, REQ-IFC-003, REQ-PRF-003, REQ-PRF-005 | No |
| CMP-DMC-01A   | DMC Display Processor              | REQ-FUN-019                                                                  | No   |
| CMP-DMC-01B   | DMC CDU Interface                  | REQ-FUN-020                                                                  | No   |
| CMP-DMC-01C   | DMC Display Application            | REQ-FUN-009, REQ-FUN-010, REQ-FUN-013, REQ-FUN-018, REQ-FUN-019, REQ-FUN-020, REQ-SAF-004, REQ-SAF-007 | No |
| CMP-DCU-01    | Data Concentrator Unit             | REQ-FUN-021, REQ-SEC-005, REQ-PRF-003, REQ-PRF-005                          | No   |
| CMP-DCU-01A   | DCU Sensor Interface               | REQ-FUN-005, REQ-IFC-002, REQ-IFC-006                                       | No   |
| CMP-DCU-01B   | DCU Datalink Interface             | REQ-FUN-003, REQ-SEC-003, REQ-IFC-004                                       | No   |
| CMP-DCU-01C   | DCU Maintenance Port               | REQ-FUN-022, REQ-SEC-001, REQ-SEC-002, REQ-IFC-007                          | No   |
| CMP-DCU-01D   | DCU FPGA Subsystem                 | —                                                                            | YES  |
| CMP-DCU-01E   | DCU Aggregation Application        | REQ-FUN-022, REQ-SEC-001, REQ-SEC-003, REQ-IFC-002, REQ-IFC-004            | No   |

### Hazards to Controls to Requirements

| HZ ID   | CTL ID(s)            | REQ ID(s)                                                                      | Fully Mitigated? |
|---------|----------------------|--------------------------------------------------------------------------------|------------------|
| HZ-001  | CTL-001, CTL-002, CTL-010 | REQ-SAF-001, REQ-SAF-002, REQ-SAF-003, REQ-SAF-010, REQ-FUN-021          | Yes              |
| HZ-002  | CTL-002, CTL-004     | REQ-SAF-001, REQ-SAF-002, REQ-SAF-004, REQ-FUN-014                            | Yes              |
| HZ-003  | CTL-003              | REQ-FUN-008, REQ-FUN-009, REQ-SEC-003                                          | Yes              |
| HZ-004  | CTL-004              | REQ-SAF-004                                                                    | Yes              |
| HZ-005  | CTL-005              | REQ-SAF-005, REQ-SAF-006                                                       | Yes              |
| HZ-006  | CTL-006              | REQ-SAF-007                                                                    | Yes              |
| HZ-007  | CTL-001, CTL-008     | REQ-SAF-003, REQ-SAF-008, REQ-SAF-009                                          | Yes              |
| HZ-008  | CTL-008              | REQ-SAF-009                                                                    | Yes              |
| HZ-009  | CTL-009              | REQ-FUN-022, REQ-SEC-001                                                       | Yes              |
| HZ-010  | CTL-009, CTL-003     | REQ-SEC-003, REQ-FUN-008                                                       | Yes              |
| HZ-011  | CTL-007              | REQ-FUN-016, REQ-FUN-017                                                       | Yes              |
| HZ-012  | CTL-006              | REQ-SAF-007                                                                    | Yes              |

### Verification to Requirements

| VER ID     | REQ ID(s)                   | EVD ID(s)        | Status  |
|------------|------------------------------|------------------|---------|
| VER-T-001  | REQ-PRF-001                  | EVD-001          | Planned |
| VER-A-001  | REQ-SAF-003                  | EVD-002          | Planned |
| VER-T-002  | REQ-SAF-001                  | EVD-003          | Planned |
| VER-T-003  | REQ-SAF-002                  | EVD-003          | Planned |
| VER-T-004  | REQ-FUN-008                  | EVD-004          | Planned |
| VER-A-002  | REQ-FUN-008                  | EVD-005          | Planned |
| VER-T-005  | REQ-SAF-004                  | EVD-006          | Planned |
| VER-T-006  | REQ-SAF-005                  | EVD-007          | Planned |
| VER-A-003  | REQ-SAF-005                  | EVD-008          | Planned |
| VER-T-007  | REQ-SAF-007                  | EVD-006          | Planned |
| VER-T-008  | REQ-FUN-016                  | EVD-009          | Planned |
| VER-A-004  | REQ-FUN-016                  | EVD-010          | Planned |
| VER-T-009  | REQ-SAF-009                  | EVD-011          | Planned |
| VER-T-010  | REQ-FUN-022, REQ-SEC-001     | EVD-012          | Planned |
| VER-T-011  | REQ-SEC-003                  | EVD-012          | Planned |
| VER-T-012  | REQ-FUN-021                  | EVD-013          | Planned |
| VER-T-013  | REQ-FUN-001                  | EVD-014          | Planned |
| VER-T-014  | REQ-FUN-002                  | EVD-014          | Planned |
| VER-T-015  | REQ-FUN-003                  | EVD-014          | Planned |
| VER-T-016  | REQ-FUN-004                  | EVD-014          | Planned |
| VER-T-017  | REQ-FUN-005                  | EVD-001          | Planned |
| VER-T-018  | REQ-FUN-006                  | EVD-003          | Planned |
| VER-T-019  | REQ-FUN-007                  | EVD-001          | Planned |
| VER-T-020  | REQ-FUN-009                  | EVD-004          | Planned |
| VER-T-021  | REQ-FUN-010                  | EVD-015          | Planned |
| VER-T-022  | REQ-FUN-011                  | EVD-016          | Planned |
| VER-A-005  | REQ-FUN-011                  | EVD-016          | Planned |
| VER-T-023  | REQ-FUN-012                  | EVD-016          | Planned |
| VER-T-024  | REQ-FUN-013                  | EVD-016          | Planned |
| VER-T-025  | REQ-FUN-014                  | EVD-009          | Planned |
| VER-T-026  | REQ-FUN-015                  | EVD-009          | Planned |
| VER-T-027  | REQ-FUN-017                  | EVD-009          | Planned |
| VER-T-028  | REQ-FUN-018                  | EVD-009          | Planned |
| VER-T-029  | REQ-FUN-019                  | EVD-017          | Planned |
| VER-T-030  | REQ-FUN-020                  | EVD-017          | Planned |
| VER-T-031  | REQ-SAF-006                  | EVD-007          | Planned |
| VER-T-032  | REQ-SEC-002                  | EVD-018          | Planned |
| VER-T-033  | REQ-SEC-004                  | EVD-018          | Planned |
| VER-A-008  | REQ-SEC-004                  | EVD-019          | Planned |
| VER-T-034  | REQ-SEC-005                  | EVD-018          | Planned |
| VER-T-035  | REQ-IFC-001                  | EVD-009          | Planned |
| VER-T-036  | REQ-IFC-002                  | EVD-020          | Planned |
| VER-T-037  | REQ-IFC-003                  | EVD-020          | Planned |
| VER-T-038  | REQ-IFC-004                  | EVD-020          | Planned |
| VER-T-039  | REQ-IFC-005                  | EVD-003          | Planned |
| VER-T-040  | REQ-IFC-006                  | EVD-020          | Planned |
| VER-T-041  | REQ-IFC-007                  | EVD-020          | Planned |
| VER-T-042  | REQ-PRF-003                  | EVD-021          | Planned |
| VER-T-043  | REQ-PRF-004                  | EVD-022          | Planned |
| VER-A-011  | REQ-PRF-004                  | EVD-022          | Planned |
| VER-T-044  | REQ-PRF-005                  | EVD-021          | Planned |
| VER-A-009  | REQ-PRF-001                  | EVD-001          | Planned |
| VER-A-010  | REQ-PRF-002                  | EVD-023          | Planned |
| VER-I-001  | REQ-SAF-010                  | EVD-024          | Planned |
| VER-A-006  | REQ-SAF-008                  | EVD-002          | Planned |
| VER-A-007  | REQ-SAF-010                  | EVD-024          | Planned |

## Gap Register

| Gap ID  | Type                   | Entity ID     | Description                                                                              | Disposition |
|---------|------------------------|---------------|------------------------------------------------------------------------------------------|-------------|
| GAP-001 | Orphan component       | CMP-DCU-01D   | DCU FPGA Subsystem has no direct requirements; bus arbitration function is derived from interface requirements but no explicit REQ- allocates to this component | Planned: derive REQ-FUN-023 for DCU FPGA bus arbitration at next requirements review |
| GAP-002 | Derived requirement without full verification | REQ-FUN-006 | Derived from REQ-FUN-005 (position computation); 20 ms timing constraint is a design choice, not a safety assessment output. Verification test (VER-T-018) is planned but the derivation rationale needs formal review and feedback to safety assessment per DO-178C 5.1.2 | Planned: complete derived requirement review at SOI #2 |
| GAP-003 | Incomplete verification coverage | REQ-SAF-003 | Quantitative probability target (1e-9/FH) is verified by analysis only (VER-A-001); no test can directly demonstrate this probability. SSA closure depends on FTA with validated failure rate data, which is not yet available for all basic events | Planned: obtain vendor failure rate data before SOI #3; SSA closure contingent on data availability |

## Coverage Summary

- **Requirements with architecture allocation**: 49/49 (100%)
- **Safety requirements with hazard source**: 10/10 (100%)
- **Security requirements with threat source**: 5/5 (100%)
- **Requirements with verification activity**: 49/49 (100%)
- **Verification activities with evidence artifact**: 54/54 (100%)
- **Components with at least one requirement**: 18/19 (94.7%) — GAP-001 (CMP-DCU-01D)
- **Hazards with at least one control**: 12/12 (100%)
- **Controls with at least one requirement**: 10/10 (100%)
- **Gaps registered**: 3 (all dispositioned as Planned)
