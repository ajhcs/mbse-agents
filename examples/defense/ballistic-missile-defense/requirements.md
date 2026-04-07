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
| **Statement**    | The BMDE shall receive and process sensor track data from up to 12 concurrent sensor feeds with a track update processing latency of not more than 500 ms from receipt to track file update. |
| **Rationale**    | Multiple sensor feeds are required for layered defense; processing latency directly impacts engagement timeline. |
| **Source**       | Stakeholder need (COCOM staff); BMDS system performance specification |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-TMS-01A |
| **Status**       | Draft |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMDE shall correlate tracks from multiple sensor sources into a composite track file, resolving duplicate tracks with a correlation confidence threshold of 95% or greater. |
| **Rationale**    | Track correlation across sensor types eliminates duplicate threat entries and provides a single engagement-quality track picture. |
| **Source**       | Stakeholder need (BMDS operator crew); BMDS operational architecture |
| **Parent**       | REQ-FUN-001 |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-TMS-01A, CMP-TMS-01B |
| **Status**       | Draft |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMDE shall classify each correlated track as ballistic threat, cruise threat, debris, or unknown within 10 seconds of initial track establishment using kinematic discrimination and sensor phenomenology data. |
| **Rationale**    | Threat classification drives engagement priority; misclassification wastes interceptor inventory or fails to engage real threats. |
| **Source**       | Stakeholder need (BMDS operator crew); MDA system performance specification |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-ECP-01B |
| **Status**       | Draft |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMDE shall compute weapon-target pairing assignments for all classified ballistic threats against available interceptor inventory, optimizing for maximum defended asset coverage with a pairing computation time of not more than 5 seconds. |
| **Rationale**    | Weapon-target pairing must complete within the engagement timeline; optimal assignment maximizes Pk across the defended area. |
| **Source**       | Stakeholder need (COCOM staff); BMDS engagement doctrine |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-ECP-01C |
| **Status**       | Draft |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMDE shall transmit fire control commands to designated interceptor launch systems via IFC-EXT-003 with end-to-end command latency of not more than 2 seconds from operator authorization to interceptor receipt. |
| **Rationale**    | Fire control command latency directly reduces available engagement time for interceptor fly-out. |
| **Source**       | BMDS system performance specification; engagement timeline analysis |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-ECP-01A, CMP-CGW-01A |
| **Status**       | Draft |

### REQ-FUN-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMDE shall provide the operator with an engagement status display showing all active tracks, weapon-target pairings, interceptor status, and defended asset coverage updated at not less than 1 Hz. |
| **Rationale**    | Operator situational awareness is essential for engagement authorization decisions. |
| **Source**       | Stakeholder need (BMDS operator crew) |
| **Parent**       | — |
| **Verification** | Test, Demonstration |
| **Allocation**   | CMP-BDS-01A |
| **Status**       | Draft |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMDE shall implement a positive fire control sequence requiring explicit operator authorization before any fire control command is transmitted to an interceptor launch system, with a two-person authentication mechanism for strategic interceptor classes. |
| **Rationale**    | Inadvertent launch of an interceptor could escalate a crisis, waste limited inventory, or result in interceptor impact in unintended areas. |
| **Source**       | MIL-STD-882E; NCA engagement authority doctrine |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-ECP-01A, CMP-BDS-01A |
| **Status**       | Draft |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMDE shall reject fire control commands that target tracks classified as debris or unknown, and shall require operator override with logged justification to engage tracks classified as unknown. |
| **Rationale**    | Engaging non-threat tracks wastes interceptor inventory and may engage friendly or neutral objects. |
| **Source**       | MIL-STD-882E; BMDS rules of engagement |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-ECP-01A, CMP-ECP-01C |
| **Status**       | Draft |

### REQ-SAF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMDE shall enforce engagement authority boundaries such that fire control commands are transmitted only for threat tracks within the BMDE's assigned engagement zone and authorized threat classes. |
| **Rationale**    | Engagement outside the assigned zone could interfere with adjacent BMDS elements or violate NCA engagement authority delegation. |
| **Source**       | MIL-STD-882E; BMDS C2 architecture |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-ECP-01A |
| **Status**       | Draft |

### REQ-SAF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMDE shall log all engagement decisions, operator authorizations, fire control commands, and track classifications to a tamper-evident mission recorder with sufficient fidelity to reconstruct the engagement timeline during post-event analysis. |
| **Rationale**    | Post-engagement reconstruction supports accountability, lessons learned, and safety investigation. |
| **Source**       | MIL-STD-882E; MDA test and evaluation requirements |
| **Parent**       | — |
| **Verification** | Test, Inspection |
| **Allocation**   | CMP-ECP-01A |
| **Status**       | Draft |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMDE shall receive sensor track data via IFC-EXT-001 and IFC-EXT-002 in BMDS standard track message format with message validation including source authentication and sequence number verification. |
| **Rationale**    | Track message integrity is essential; corrupted or spoofed track data could cause incorrect engagement decisions. |
| **Source**       | BMDS interface control document; MIL-STD-3022 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-TMS-01A, CMP-CGW-01A |
| **Status**       | Draft |

### REQ-IFC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMDE shall exchange engagement coordination messages with adjacent BMDS elements via IFC-EXT-004 to prevent dual engagement of a single threat and to coordinate shoot-look-shoot sequences. |
| **Rationale**    | Uncoordinated engagement wastes interceptor inventory by assigning multiple interceptors from different elements to the same threat. |
| **Source**       | BMDS operational architecture; MIL-STD-3022 |
| **Parent**       | — |
| **Verification** | Test, Demonstration |
| **Allocation**   | CMP-CGW-01A, CMP-ECP-01C |
| **Status**       | Draft |

## Performance Requirements

### REQ-PRF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The BMDE shall maintain a composite track file of up to 500 simultaneous tracks with track state prediction accuracy sufficient to support interceptor midcourse guidance updates. |
| **Rationale**    | Track file capacity and prediction accuracy directly determine the number of threats that can be engaged simultaneously. |
| **Source**       | BMDS system performance specification |
| **Parent**       | REQ-FUN-001 |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-TMS-01A, CMP-TMS-01B |
| **Status**       | Draft |
