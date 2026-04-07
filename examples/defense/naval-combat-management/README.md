# Naval Combat Management System

## Overview

The Naval Combat Management System (CMS) is the central C2 system for a surface combatant warship, integrating sensors, weapons, and external data links into a unified tactical picture for engagement planning and execution. The CMS fuses track data from the ship's radar suite (air search, surface search, fire control), sonar, electronic warfare, and cooperative engagement capability (CEC) data links to produce a composite track picture. Operators use the CMS for threat evaluation and weapon assignment (TEWA), engagement planning, and weapon direction against air, surface, and subsurface threats. The system manages the sensor-to-weapon kill chain from initial detection through engagement assessment. The CMS interfaces with legacy MIL-STD-1553 weapons and sensors while supporting a GigE modernization path for new installations. This is an ACAT I program under Navy PEO Integrated Warfare Systems (IWS) acquisition oversight.

## System Boundary

**Inside the system boundary:**
- Combat System Processor (track fusion, TEWA, engagement planning)
- Weapon Direction System (weapon assignment, fire control interface, engagement sequencing)
- Display System (tactical plot, operator consoles, alert management)
- Data Link Processor (Link 16, CEC, coalition data links)
- Combat System Network (internal GigE backbone with 1553 bridge)

**Outside the system boundary:**
- Ship's radar suite (AN/SPY-series, fire control radars -- provide track data, receive designation)
- Sonar suite (hull-mounted, towed array -- provide underwater tracks)
- Weapon systems (missiles, guns, CIWS, torpedoes -- receive fire control commands, manage own terminal guidance)
- CEC network (ship-to-ship cooperative engagement -- CMS interfaces but does not own the CEC hardware)
- Navigation system (provides own-ship position and kinematics)
- Ship's combat direction center (CDC) physical infrastructure

## Operational Environment

The CMS operates within the ship's combat information center (CIC). Environmental conditions per MIL-STD-810H for shipboard equipment including salt fog, vibration, and shock (per MIL-S-901 for grade A shock). The system interfaces with shipboard power (60 Hz, 440V 3-phase through UPS) and cooling (chilled water). Electromagnetic environment per MIL-STD-461G for shipboard above-deck and below-deck classifications.

## Operating Modes

| Mode ID   | Name                   | Description                                                        | Active Functions                            | Constraints                                    |
|-----------|------------------------|--------------------------------------------------------------------|---------------------------------------------|------------------------------------------------|
| MODE-001  | Full Combat            | All sensors, weapons, and data links integrated; full engagement capability | All FUN- functions active                   | None                                           |
| MODE-002  | Degraded Sensor        | One or more sensor feeds lost; track fusion operates on reduced inputs | FUN-TRK-01 degraded; FUN-WPN-01 active with reduced track quality | Engagement confidence thresholds raised      |
| MODE-003  | Emissions Control      | Radar emissions restricted (EMCON); passive sensors and CEC data only | FUN-TRK-01 passive only; FUN-DL-01 receive only | No active radar designation; CEC-dependent engagement |
| MODE-004  | Port / Maintenance     | Pierside maintenance, software updates, BIT, no weapon functions   | FUN-BIT-01, FUN-DLD-01 active              | Weapon interfaces inhibited                    |

Mode IDs are referenced by requirements.md.

## Key Technical Challenges

1. **Multi-sensor track fusion with diverse phenomenology.** The CMS fuses tracks from radar (air and surface), sonar (subsurface), EW (emitter), and CEC (off-board) sources with different update rates, coordinate frames, measurement accuracies, and target classification taxonomies. Track correlation must handle the air-surface-subsurface dimensional overlap (a helicopter is both an air track and a radar track) and must not create false correlations that would generate phantom threats.

2. **Legacy MIL-STD-1553 to GigE migration.** Existing weapon and sensor interfaces use MIL-STD-1553 bus protocols designed in the 1970s with 1 Mbps bandwidth. New sensors and weapons use GigE. The CMS must bridge both interface types simultaneously during the multi-year modernization transition without degrading engagement timelines on either interface generation.

3. **Cooperative Engagement Capability (CEC) integration.** CEC enables ships to engage threats using another ship's sensor data. The CMS must treat CEC tracks with appropriate quality weighting (off-board sensor accuracy may differ from own-ship sensors) and must manage engagement authority when the firing ship does not hold the target on its own sensors.

4. **Weapon safety interlocks.** The CMS must enforce weapon safety at every stage of the kill chain: weapon selection, arming, fire control designation, and firing authority. An erroneous weapon release could endanger own-ship, friendly forces, or civilian shipping. The weapon direction system must prevent uncommanded weapon firing and enforce rules of engagement (ROE) constraints.

## Stakeholders

| Stakeholder                        | Role                                                            |
|------------------------------------|-----------------------------------------------------------------|
| CIC watch team                     | Operate CMS, manage tracks, authorize engagements               |
| Commanding officer                 | Weapons release authority; approves ROE implementation          |
| Tactical action officer (TAO)      | Primary CMS engagement authority in CIC                         |
| PEO IWS                            | Acquisition oversight for combat system programs                |
| Ship's electronics technicians     | Maintain CMS hardware and software, perform BIT                 |
| Type commander (TYCOM)             | Fleet readiness and combat system certification                 |

## Standards Applicability

| Standard        | Applicability                                                                             |
|-----------------|-------------------------------------------------------------------------------------------|
| DoDAF 2.02      | Architecture framework for combat system integration views                                |
| MIL-STD-882E    | System safety; weapon safety interlocks, uncommanded weapon firing prevention              |
| MIL-STD-1553B   | Legacy data bus for weapon and sensor interfaces during modernization transition           |
| MIL-STD-3022    | System-of-systems engineering for combat system integration                               |
| MIL-STD-461G    | EMI/EMC for shipboard electronic equipment                                                |
| MIL-S-901D      | Shock qualification for shipboard equipment                                               |
