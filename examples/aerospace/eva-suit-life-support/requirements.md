# Requirements

All requirements are atomic, testable shall-statements.

## Requirement Record Schema

| Field         | Description                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------|
| ID            | Unique identifier (e.g., REQ-FUN-001)                                                            |
| Statement     | Atomic shall-statement                                                                            |
| Rationale     | Why this requirement exists                                                                       |
| Source        | Regulatory clause, stakeholder need, or parent requirement                                        |
| Parent        | Parent requirement ID (if derived)                                                                |
| Verification  | Method: test, analysis, inspection, demonstration                                                 |
| Allocation    | Target component ID(s) from architecture.md                                                       |
| Status        | Draft, baselined, verified, deferred                                                              |

## Functional Requirements

### REQ-FUN-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The PLSS shall maintain suit internal pressure at 4.3 +/-0.1 psia during all EVA operating modes. |
| **Rationale**    | 4.3 psia is the established EVA suit operating pressure for ISS and Artemis, providing adequate oxygen partial pressure for crew respiration while permitting acceptable suit mobility. |
| **Source**       | NPR 8705.2; EVA suit pressure garment ICD |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-PREG-01 |
| **Status**       | Draft |

### REQ-FUN-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The PLSS shall supply breathing-quality oxygen at a flow rate sufficient to maintain an inspired O2 partial pressure between 2.8 and 3.3 psia at metabolic rates from 70 W to 470 W. |
| **Rationale**    | Oxygen partial pressure range ensures crew physiological safety across the full metabolic work rate range encountered during EVA. |
| **Source**       | NASA-STD-3001 Vol. 2; crew health requirements |
| **Parent**       | — |
| **Verification** | Test, Analysis |
| **Allocation**   | CMP-O2-01 |
| **Status**       | Draft |

### REQ-FUN-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The PLSS shall remove carbon dioxide from the suit atmosphere to maintain inspired CO2 partial pressure below 7.6 mmHg at metabolic rates up to 470 W. |
| **Rationale**    | CO2 above 7.6 mmHg impairs crew cognitive performance and above 15 mmHg presents an acute health hazard. |
| **Source**       | NASA-STD-3001 Vol. 2; SMAC limits for CO2 |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CDRA-01 |
| **Status**       | Draft |

### REQ-FUN-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The PLSS thermal control loop shall reject crew metabolic heat from 70 W (rest) to 470 W (maximum exertion) while maintaining the liquid cooling and ventilation garment (LCVG) inlet temperature between 45F and 65F. |
| **Rationale**    | LCVG inlet temperature range ensures crew thermal comfort and prevents hypothermia or hyperthermia during EVA. |
| **Source**       | NASA-STD-3001 Vol. 2; thermal comfort guidelines |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-TCS-01 |
| **Status**       | Draft |

### REQ-FUN-005
| Field        | Value |
|--------------|-------|
| **Statement**    | The PLSS shall remove humidity from the suit atmosphere to maintain relative humidity below 85% at the ventilation inlet. |
| **Rationale**    | Excessive humidity causes visor fogging and crew discomfort, and can degrade CO2 sensor accuracy. |
| **Source**       | EVA crew health requirements; heritage PLSS design data |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CDRA-01, CMP-TCS-01 |
| **Status**       | Draft |

### REQ-FUN-006
| Field        | Value |
|--------------|-------|
| **Statement**    | The PLSS shall support a nominal sortie duration of 8 hours at an average metabolic rate of 250 W, with consumables (O2, battery, water) sized for this duration plus a 30-minute emergency reserve. |
| **Rationale**    | 8-hour sortie with 30-minute reserve is the baseline EVA timeline for Artemis lunar surface operations. |
| **Source**       | Artemis EVA requirements; stakeholder need (EVA flight controller) |
| **Parent**       | — |
| **Verification** | Analysis, Test |
| **Allocation**   | CMP-O2-01, CMP-EPS-01, CMP-TCS-01 |
| **Status**       | Draft |

## Safety Requirements

### REQ-SAF-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The PLSS shall provide two-fault tolerance against catastrophic loss of suit pressure, such that no combination of two failures can result in suit depressurization below 3.5 psia within the time required for crew to reach the airlock. |
| **Rationale**    | Two-fault tolerance for catastrophic hazards is mandated by NPR 8705.2 for human-rated systems. Loss of suit pressure in vacuum is immediately life-threatening. |
| **Source**       | NPR 8705.2 Section 4.2; NASA-STD-8719.13 |
| **Parent**       | — |
| **Verification** | Analysis, Test |
| **Allocation**   | CMP-PREG-01 |
| **Status**       | Draft |

### REQ-SAF-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The PLSS shall provide a secondary oxygen supply (SOP) capable of sustaining crew respiration for a minimum of 30 minutes at a metabolic rate of 250 W, activated automatically upon primary O2 supply failure or manually by crew command. |
| **Rationale**    | SOP provides the emergency reserve for crew abort to the airlock when the primary O2 system fails. Automatic activation prevents delay if crew is incapacitated. |
| **Source**       | NPR 8705.2; REQ-FUN-006 |
| **Parent**       | REQ-FUN-006 |
| **Verification** | Test |
| **Allocation**   | CMP-SOP-01 |
| **Status**       | Draft |

### REQ-SAF-003
| Field        | Value |
|--------------|-------|
| **Statement**    | The PLSS caution and warning system shall annunciate a suit pressure low warning to the crew and EVA flight controller within 5 seconds of suit pressure dropping below 4.0 psia. |
| **Rationale**    | Early warning of pressure loss enables crew-initiated abort before the condition becomes critical. |
| **Source**       | NASA-STD-8719.13; NPR 8705.2 |
| **Parent**       | REQ-SAF-001 |
| **Verification** | Test |
| **Allocation**   | CMP-CW-01 |
| **Status**       | Draft |

### REQ-SAF-004
| Field        | Value |
|--------------|-------|
| **Statement**    | The PLSS shall annunciate a CO2 high warning when inspired CO2 partial pressure exceeds 5.3 mmHg, and shall annunciate a CO2 critical alarm when inspired CO2 exceeds 7.6 mmHg. |
| **Rationale**    | Tiered alerting for CO2 gives the crew time to reduce metabolic rate or initiate abort before cognitive impairment onset. |
| **Source**       | NASA-STD-3001 Vol. 2; crew health requirements |
| **Parent**       | REQ-FUN-003 |
| **Verification** | Test |
| **Allocation**   | CMP-CW-01 |
| **Status**       | Draft |

### REQ-SAF-005
| Field        | Value |
|--------------|-------|
| **Statement**    | All PLSS pressure vessels and fittings shall satisfy NASA-STD-5005 fracture control requirements, including safe-life demonstration or leak-before-burst verification for each pressure-containing component. |
| **Rationale**    | Fracture control prevents catastrophic failure of pressure vessels due to undetected cracks or material defects. |
| **Source**       | NASA-STD-5005; NPR 8705.2 |
| **Parent**       | — |
| **Verification** | Inspection, Analysis, Test |
| **Allocation**   | CMP-O2-01, CMP-PREG-01, CMP-TCS-01 |
| **Status**       | Draft |

## Interface Requirements

### REQ-IFC-001
| Field        | Value |
|--------------|-------|
| **Statement**    | The PLSS shall interface with the vehicle umbilical to receive supplemental O2 and cooling water during pre-EVA checkout and post-EVA recharge, with disconnect accomplished by crew single-handed operation within 10 seconds. |
| **Rationale**    | Umbilical interface supports pre-EVA resource conservation and post-EVA recharge. Quick disconnect supports crew egress in contingency scenarios. |
| **Source**       | EVA suit ICD; stakeholder need (crew equipment integration) |
| **Parent**       | — |
| **Verification** | Test, Demonstration |
| **Allocation**   | CMP-UMB-01 |
| **Status**       | Draft |

### REQ-IFC-002
| Field        | Value |
|--------------|-------|
| **Statement**    | The PLSS shall transmit real-time telemetry (suit pressure, O2 flow rate, CO2 partial pressure, LCVG inlet/outlet temperature, battery state of charge) to the EVA flight controller at a minimum rate of 1 Hz via the suit communication system. |
| **Rationale**    | Real-time telemetry enables ground monitoring of PLSS health and crew physiological status during EVA. |
| **Source**       | EVA operations requirements; stakeholder need (EVA flight controller) |
| **Parent**       | — |
| **Verification** | Test |
| **Allocation**   | CMP-CW-01, CMP-COMM-01 |
| **Status**       | Draft |
