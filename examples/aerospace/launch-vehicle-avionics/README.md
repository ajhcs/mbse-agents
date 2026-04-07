# Launch Vehicle Avionics

## Overview

The Launch Vehicle Avionics system provides guidance, navigation, and control (GN&C), flight termination, telemetry, and vehicle management for the upper stage of a medium-lift expendable launch vehicle. The avionics architecture partitions safety-critical flight termination functions from mission-critical GN&C and telemetry through physically separate processing units with independent power paths.

The Flight Termination System (FTS) is classified DAL A under DO-178C, driven by range safety requirements per EWR 127-1 and RCC 319. FTS software is the sole DO-178C-scoped element; GN&C software is classified DAL C based on mission loss consequence, and telemetry processing is DAL D. Range safety certification requires independent assessment by the launch range authority prior to each campaign.

## System Boundary

**Inside the system boundary:**
- Flight Termination System (FTS receiver, safe/arm, ordnance controller)
- GN&C computer (IMU processing, guidance algorithms, TVC commands)
- Telemetry processor and RF transmitter
- Vehicle management unit (sequencing, staging, separation)
- Avionics power distribution and battery
- Flight harness and ordnance cabling

**Outside the system boundary:**
- Range safety ground system (command transmitters, tracking radar)
- Engine controller and thrust vector control actuators (receive commands)
- First stage avionics (separated at staging)
- Payload adapter and payload avionics
- Ground launch control system (pre-flight checkout and arming)
- Tracking and data relay satellite (TDRS) network

## Operational Environment

The avionics operate from pre-launch countdown through upper stage mission completion, a timeline of approximately 2 hours. The environment progresses from ground-level ambient through maximum aerodynamic pressure (Max-Q), stage separation shock (100g pyroshock), upper stage engine ignition vibration, and sustained acceleration up to 6g. Thermal environment transitions from ground conditioning through aerodynamic heating to free-space radiation. All avionics must survive ordnance shock from separation events.

## Operating Modes

| Mode ID   | Name                | Description                                                    | Active Functions                                | Constraints                                        |
|-----------|---------------------|----------------------------------------------------------------|-------------------------------------------------|----------------------------------------------------|
| MODE-001  | Pre-Launch          | Ground checkout, FTS arm sequence, final countdown             | BIT, FTS arm, GN&C alignment, TLM active        | Umbilical connected; ground power available         |
| MODE-002  | Ascent              | Powered flight with active GN&C and range safety monitoring    | All FUN- functions active                       | None                                               |
| MODE-003  | Coast               | Unpowered coast phase between burns                            | GN&C (attitude hold), TLM, FTS armed            | Reduced power mode; thermal management active       |
| MODE-004  | Flight-Termination  | FTS activation upon range safety command or autonomous trigger | FTS ordnance fire; all other functions cease     | Irreversible; terminates mission                    |

## Key Technical Challenges

1. **FTS independence from GN&C.** The FTS must function even if the GN&C computer has failed catastrophically, requiring physically separate processors, independent power, and dedicated RF command reception. The independence argument must satisfy range safety review per EWR 127-1 Section 3.

2. **DO-178C Level A for FTS software.** FTS software is the highest-criticality airborne software on the vehicle, with no credit for operational procedures or crew intervention. The full DO-178C Level A objective set applies, including MC/DC coverage, and the verification evidence is reviewed by the range safety authority, not a traditional DER.

3. **Autonomous flight termination criteria.** In addition to ground-commanded termination, the FTS must implement autonomous termination criteria (instantaneous impact point prediction) that detect trajectory violations without ground intervention, with an acceptable false-positive rate to avoid unnecessary mission loss.

4. **Ordnance system reliability.** The FTS ordnance chain (safe/arm device, detonation train, shaped charges) must achieve a reliability of 0.999 at 95% confidence per EWR 127-1, demonstrated through lot acceptance testing, bridgewire continuity monitoring, and safe/arm status telemetry.

## Stakeholders

| Stakeholder                    | Role                                                                  |
|--------------------------------|-----------------------------------------------------------------------|
| Launch range safety officer    | FTS certification authority; mission flight safety approval           |
| Vehicle program office         | GN&C performance, mission success, vehicle integration                |
| Engine contractor              | TVC command interface, engine controller integration                  |
| Payload customer               | Orbit insertion accuracy, payload separation interface                |
| Ground operations team         | Pre-launch checkout, countdown, FTS arming sequence                   |

## Standards Applicability

| Standard          | Applicability                                                                              |
|-------------------|--------------------------------------------------------------------------------------------|
| EWR 127-1         | Eastern/Western Range safety requirements; governs FTS design, test, and certification      |
| RCC 319           | Flight termination system commonality standard; FTS component requirements                  |
| DO-178C           | Airborne software assurance; Level A for FTS, Level C for GN&C, Level D for telemetry       |
| NASA-STD-8719.24  | Expendable launch vehicle range safety; autonomous FT criteria                              |
| MIL-STD-1576      | Electroexplosive subsystem safety; ordnance design and test                                 |
| IRIG 106          | Telemetry standards; PCM formatting and RF transmission                                     |
