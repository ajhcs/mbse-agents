# Steer-by-Wire System

## Overview

The Steer-by-Wire (SbW) system replaces the conventional mechanical steering column with an electrically actuated steering architecture providing no mechanical fallback between the steering wheel and the road wheels. The system reads driver torque and angle inputs from the steering wheel sensor unit, transmits steering commands electronically to dual-redundant rack actuators, and synthesizes road-feel torque feedback to the driver through a handwheel actuator. Because there is no physical coupling between the steering wheel and the rack, the system is classified fail-operational under ISO 26262: a single fault must not result in loss of steering, and the system must maintain directional control until the driver can safely stop the vehicle.

## System Boundary

**Inside the system boundary:**
- Steering Wheel Sensor Unit (SWS) -- redundant torque and angle sensors on the steering column
- Handwheel Feedback Actuator (HFA) -- motor providing road-feel torque to the driver
- SbW Central Controller (SCC) -- dual-channel processing unit for steering command computation
- Rack Actuator A (RA-A) -- primary electromechanical rack actuator (left-side mounting)
- Rack Actuator B (RA-B) -- secondary electromechanical rack actuator (right-side mounting)
- Rack position sensor (redundant, integrated into each actuator)
- SbW power supply management (dual-feed from vehicle electrical system)
- SbW application software (steering ratio, torque feedback model, fault management)

**Outside the system boundary:**
- Steering wheel (mechanical input device; SbW reads torque/angle from it)
- Steering rack and tie rods (mechanical output; actuators drive the rack)
- Vehicle dynamics controller (provides yaw rate, lateral acceleration; SbW consumes for feedback)
- ADAS lane-keeping assist (sends steering overlay commands to SbW; SbW arbitrates)
- Vehicle power supply (dual 48V feeds; SbW consumes power but does not manage the supply)
- Instrument cluster (displays SbW status, warnings; HMI hardware is external)

## Operational Environment

The SbW system operates in passenger vehicles designed for public road use at speeds from 0 km/h to the vehicle's maximum speed. The system must function across -40C to +85C ambient temperature. The rack actuators are exposed to road spray, vibration, and impact loads. The SCC is cabin-mounted. The system interfaces with the vehicle dynamics domain via CAN FD and with ADAS via Automotive Ethernet. UN R79 requires that steering functionality be maintained after any single fault, with a maximum 50 ms interruption in steering assist during fault switchover.

## Operating Modes

| Mode ID   | Name                    | Description                                                              | Active Functions                                                | Constraints                                                |
|-----------|-------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------|------------------------------------------------------------|
| MODE-001  | Normal Steering         | Both actuator channels active; full torque feedback; variable ratio      | All FUN- functions active on both channels                     | None                                                       |
| MODE-002  | Degraded Single-Channel | One actuator channel failed; remaining channel provides full steering    | Single-channel actuation; reduced torque feedback fidelity     | Reduced maximum assist torque; driver warning active; speed limited to 130 km/h |
| MODE-003  | Limp-Home               | Multiple faults detected; minimum steering capability maintained         | Basic rack position control on surviving channel               | Fixed steering ratio; no variable assist; speed limited to 30 km/h |
| MODE-004  | Maintenance/Calibration | Vehicle stationary; sensor calibration and diagnostic functions active   | Sensor self-test, actuator alignment, fault readout            | No steering actuation; vehicle must be stationary           |

## Key Technical Challenges

1. **Fail-operational without mechanical fallback.** Unlike conventional EPS, SbW has no mechanical column to fall back on. The system must guarantee steering availability after any single fault, requiring fully redundant actuators, sensors, processing, and power supply with deterministic fault switchover.

2. **Freedom-from-interference between redundant channels.** The two actuator channels (RA-A, RA-B) and the dual processing channels in the SCC must be provably independent per ISO 26262-9. A common-cause fault affecting both channels simultaneously must be demonstrated as sufficiently unlikely through dissimilar hardware, separated power domains, and diversity in sensor technology.

3. **Road-feel torque feedback synthesis.** Without a mechanical connection, the driver receives no natural steering feel. The handwheel feedback actuator must synthesize realistic road-feel torque that varies with speed, road surface, and steering angle, using a model-based approach that avoids instability or oscillation.

4. **UN R79 single-fault performance.** UN R79 mandates that after a single fault the system must still provide steering capability meeting defined minimum performance criteria, including a maximum 50 ms interruption during switchover and continued steering at reduced capability.

## Stakeholders

| Stakeholder                    | Role                                                                            |
|--------------------------------|---------------------------------------------------------------------------------|
| Vehicle driver                 | Relies on steering responsiveness and road feel; safety-critical interaction    |
| Vehicle OEM integration team   | Integrates SbW into vehicle dynamics; responsible for vehicle-level safety case |
| Tier-1 SbW system supplier     | Designs and delivers SbW system; holds ASIL D safety case                      |
| Type approval authority        | Approves vehicle against UN R79; reviews single-fault steering performance     |
| Third-party assessor           | Performs functional safety assessment per ISO 26262 Part 2                      |
| ADAS integration team          | Integrates lane-keeping overlay commands with SbW actuation path               |

## Standards Applicability

| Standard       | Applicability                                                                                     |
|----------------|---------------------------------------------------------------------------------------------------|
| ISO 26262      | Functional safety lifecycle; ASIL D for entire steering actuation path; fail-operational argument  |
| ISO 21448      | SOTIF analysis for steering feel anomalies and ADAS overlay interaction                           |
| UN R79         | Steering equipment type approval; single-fault steering performance requirements                  |
| ISO 11898      | CAN and CAN FD physical/data link layer for vehicle communication                                |
