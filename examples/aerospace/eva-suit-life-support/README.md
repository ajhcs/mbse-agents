# EVA Suit Life Support System

## Overview

The EVA Suit Life Support System is a portable life support system (PLSS) providing atmospheric pressure, oxygen supply, carbon dioxide removal, thermal regulation, and humidity control for a single crewmember during extravehicular activity. The system supports both ISS-based EVA and Artemis lunar surface operations with a nominal 8-hour sortie duration and a 30-minute emergency reserve.

The PLSS is human-rated per NPR 8705.2, with fracture control per NASA-STD-5005 for all pressure-containing structure. The system is designed to two-fault tolerant for catastrophic hazards (loss of crew) and single-fault tolerant for critical hazards, consistent with NASA-STD-8719.13 hazard classification.

## System Boundary

**Inside the system boundary:**
- Primary oxygen supply and regulation
- Carbon dioxide removal assembly (CDRA swing-bed)
- Thermal control loop (LCVG water circuit and sublimator)
- Suit pressure garment interface (pressure regulation valves, relief valves)
- PLSS avionics (caution and warning, sensor suite, data logging)
- Secondary oxygen pack (emergency supply)
- Battery and power distribution

**Outside the system boundary:**
- Suit pressure garment (helmet, gloves, HUT, boots)
- Helmet-mounted display and communication system
- Umbilical system (when tethered to vehicle)
- Vehicle airlock and EVA support equipment
- Crew physiological state (consumed O2, produced CO2 and heat are boundary inputs)

## Operational Environment

The PLSS operates in the vacuum of space during ISS EVA and on the lunar surface during Artemis missions. Thermal environment ranges from -157C (shadow) to +121C (direct solar), with transitions as rapid as 45 minutes per orbit on ISS. Lunar dust presents contamination and seal degradation challenges. The system must function in microgravity (ISS) and partial gravity (1/6 g lunar) with identical crew interfaces.

## Operating Modes

| Mode ID   | Name              | Description                                                    | Active Functions                                | Constraints                                        |
|-----------|-------------------|----------------------------------------------------------------|-------------------------------------------------|----------------------------------------------------|
| MODE-001  | Nominal-EVA       | Full life support during normal sortie operations              | All FUN- functions active                       | None                                               |
| MODE-002  | Degraded-Thermal  | Primary thermal loop impaired; backup sublimator active        | O2/CO2 nominal; thermal on backup               | Reduced metabolic rate required; sortie time limited |
| MODE-003  | Emergency-O2      | Primary O2 depleted or regulator failed; secondary O2 active  | Secondary O2, CO2 removal, minimal thermal      | 30-minute reserve; crew abort to airlock required    |
| MODE-004  | Crew-Abort        | Immediate return to airlock initiated                          | Emergency O2, suit pressure hold, comm active   | All non-essential systems shed; minimum safe config  |

## Key Technical Challenges

1. **Two-fault tolerance for catastrophic hazards.** Loss of suit pressure or oxygen is catastrophic. The architecture must demonstrate two independent inhibits for each catastrophic failure path, verified through fault tree analysis per NASA-STD-8719.13.

2. **Thermal balance across extreme environments.** The sublimator-based thermal control must maintain crew comfort from the metabolic heat load range of 70W (rest) to 470W (maximum exertion) across the full thermal environment. Water consumption rate directly limits sortie duration.

3. **CO2 washout in the helmet.** CO2 must be swept from the helmet volume to prevent localized CO2 buildup near the crew's breathing zone, even at low ventilation flow rates. This requires validated CFD analysis of the helmet ventilation flow field.

4. **Fracture control for pressure vessels.** All pressure-containing structure must satisfy NASA-STD-5005 fracture control, including proof-of-concept testing, NDE inspection intervals, and safe-life or leak-before-burst demonstration for each pressure vessel and fitting.

## Stakeholders

| Stakeholder                      | Role                                                              |
|----------------------------------|-------------------------------------------------------------------|
| EVA crew                         | Primary user; depends on system for survival during sortie        |
| EVA flight controller            | Real-time monitoring of PLSS telemetry during EVA                 |
| Crew equipment integration team  | PLSS-to-suit and PLSS-to-vehicle interface management             |
| NASA Safety and Mission Assurance | Human-rating certification authority per NPR 8705.2              |
| Artemis program office           | Lunar EVA requirements, sortie duration, dust mitigation needs    |

## Standards Applicability

| Standard          | Applicability                                                                              |
|-------------------|--------------------------------------------------------------------------------------------|
| NPR 7123.1        | Systems engineering processes for human spaceflight systems                                |
| NPR 8705.2        | Human-rating requirements; drives two-fault tolerance and crew safety                      |
| NASA-STD-5005     | Fracture control for pressure vessels, fittings, and structural elements                   |
| NASA-STD-5019     | Fracture control for composite and bonded structures (PLSS enclosure)                      |
| NASA-STD-8719.13  | Safety standard for hazard classification and risk acceptance                              |
| AIAA S-080-1998   | Space systems metallic pressure vessels (PLSS O2 tanks)                                    |
