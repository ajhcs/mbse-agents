# Requirements

All requirements are atomic, testable shall-statements.

## Requirement Record Schema

| Field         | Description                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------|
| ID            | Unique identifier (e.g., REQ-FUN-001)                                                            |
| Statement     | Atomic shall-statement                                                                            |
| Rationale     | Why this requirement exists                                                                       |
| Source        | Regulatory clause, stakeholder need, or safety concern                                            |
| Parent        | Parent requirement ID (if derived)                                                                |
| Verification  | Method: test, analysis, inspection, demonstration                                                 |
| Allocation    | Target component ID(s) from architecture.md                                                       |
| Status        | Draft, baselined, verified, deferred                                                              |

## Functional Requirements

### REQ-FUN-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The CMS shall fuse track data from ship's radars, sonar, EW, and CEC data links into a composite track file of up to 1000 simultaneous tracks with track update latency of not more than 1 second from sensor report receipt to composite track file update. |
| **Rationale**    | Track fusion from all sensor sources provides the tactical picture that drives engagement decisions. |
| **Source**       | Stakeholder need (TAO); combat system performance specification |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CSP-01A |
| **Status**       | Draft |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The CMS shall correlate tracks across sensor types (radar, sonar, EW, CEC) and shall resolve track identity conflicts using a weighted confidence algorithm that accounts for sensor accuracy, update rate, and classification reliability. |
| **Rationale**    | Cross-sensor correlation eliminates duplicate tracks and enriches track quality from multi-phenomenology data. |
| **Source**       | Stakeholder need (CIC watch team); combat system operational architecture |
| **Parent**       | REQ-FUN-001 |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-CSP-01A, CMP-CSP-01B |
| **Status**       | Draft |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The CMS shall perform threat evaluation and weapon assignment (TEWA) by computing threat priority for each classified hostile track and recommending weapon-target pairings based on engagement envelope, weapon inventory, and rules of engagement. |
| **Rationale**    | TEWA provides the TAO with recommended engagement solutions to enable rapid engagement decisions. |
| **Source**       | Stakeholder need (TAO); combat system doctrine |
| **Parent**       | — |
| **Verification** | Test, Demonstration |
| **Allocation**   | CMP-CSP-01C |
| **Status**       | Draft |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The CMS shall process CEC composite track data received via IFC-EXT-004 and shall integrate CEC tracks into the composite track file with quality weighting that reflects off-board sensor accuracy relative to own-ship sensors. |
| **Rationale**    | CEC extends the ship's engagement capability beyond own-ship sensor range; quality weighting prevents degraded off-board tracks from corrupting engagement decisions. |
| **Source**       | Stakeholder need (CIC watch team); CEC operational requirements |
| **Parent**       | REQ-FUN-001 |
| **Verification** | Test |
| **Allocation**   | CMP-DLP-01A, CMP-CSP-01A |
| **Status**       | Draft |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The CMS shall manage the complete engagement sequence from weapon selection through firing authorization, fire control designation, weapon firing, and engagement assessment for each assigned weapon-target pair. |
| **Rationale**    | End-to-end engagement management ensures the kill chain is controlled and that engagement assessment feeds shoot-look-shoot decisions. |
| **Source**       | Stakeholder need (TAO); combat system doctrine |
| **Parent**       | — |
| **Verification** | Test, Demonstration |
| **Allocation**   | CMP-WDS-01A |
| **Status**       | Draft |

### REQ-FUN-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The CMS shall present the composite tactical picture on operator display consoles with a refresh rate of not less than 2 Hz, showing all tracks, weapon status, engagement status, and alert conditions. |
| **Rationale**    | Operator situational awareness of the tactical picture drives engagement and defense decisions. |
| **Source**       | Stakeholder need (CIC watch team) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-DSP-01A |
| **Status**       | Draft |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The CMS weapon direction system shall enforce a positive weapon safety interlock sequence requiring explicit TAO authorization before any weapon firing command is transmitted, with a hardware-backed weapon inhibit that prevents firing commands when weapon safety is set to SAFE. |
| **Rationale**    | Uncommanded or unauthorized weapon firing could endanger own-ship, friendly forces, or civilian shipping and violate rules of engagement. |
| **Source**       | MIL-STD-882E; Navy weapons safety policy |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-WDS-01A, CMP-WDS-01B |
| **Status**       | Draft |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The CMS shall enforce rules of engagement (ROE) constraints by rejecting engagement commands for track classifications or engagement zones that violate the active ROE table, and shall require commanding officer override with logged justification to engage outside ROE parameters. |
| **Rationale**    | ROE enforcement prevents unauthorized engagements; override capability preserves self-defense authority. |
| **Source**       | MIL-STD-882E; Navy ROE policy |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CSP-01C, CMP-WDS-01A |
| **Status**       | Draft |

### REQ-SAF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The CMS shall implement own-ship and friendly force safety zones such that the weapon direction system rejects fire control designations that would direct weapon trajectories through own-ship superstructure or within defined keep-out zones around friendly platforms. |
| **Rationale**    | Weapon firing through own-ship structure or into friendly force positions could cause fratricide or self-inflicted damage. |
| **Source**       | MIL-STD-882E; Navy weapons safety |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-WDS-01A |
| **Status**       | Draft |

### REQ-SAF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The CMS shall log all engagement decisions, weapon firing commands, TAO authorizations, and ROE override events to a tamper-evident combat system recorder with sufficient fidelity to reconstruct the engagement timeline during post-action analysis. |
| **Rationale**    | Post-engagement reconstruction supports accountability, legal review, and lessons learned. |
| **Source**       | MIL-STD-882E; Navy combat system recording requirements |
| **Parent**       | — |
| **Verification** | Test, Inspection |
| **Allocation**   | CMP-CSP-01A |
| **Status**       | Draft |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The CMS shall receive radar track data from the ship's radar suite via IFC-EXT-001 using both MIL-STD-1553B (for legacy radars) and GigE (for modernized radars), with a protocol bridge that presents a unified track format to the track fusion function regardless of source interface type. |
| **Rationale**    | Dual-interface support is required during the multi-year legacy-to-GigE modernization transition. |
| **Source**       | MIL-STD-1553B; combat system modernization plan |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CSN-01A, CMP-CSN-01B |
| **Status**       | Draft |

### REQ-IFC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The CMS shall transmit weapon fire control commands to weapon systems via IFC-EXT-003 using MIL-STD-1553B (for legacy weapons) or GigE (for modernized weapons) with end-to-end fire control command latency of not more than 200 ms from weapon direction to weapon receipt. |
| **Rationale**    | Fire control latency directly impacts engagement timeline for time-critical targets. |
| **Source**       | Combat system performance specification; weapon system ICDs |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-WDS-01A, CMP-CSN-01A, CMP-CSN-01B |
| **Status**       | Draft |

## Performance Requirements

### REQ-PRF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The CMS shall complete the kill chain from initial track detection to weapon firing command for a time-critical air target within 15 seconds, assuming pre-authorized ROE and pre-assigned weapon readiness. |
| **Rationale**    | Kill chain timeline drives ship survivability against anti-ship cruise missiles with short engagement windows. |
| **Source**       | Combat system performance specification |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-CSP-01A, CMP-CSP-01C, CMP-WDS-01A |
| **Status**       | Draft |
