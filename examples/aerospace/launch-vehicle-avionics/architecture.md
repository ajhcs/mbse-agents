# Architecture

## System Context

The Launch Vehicle Avionics system is the upper stage avionics suite for a medium-lift expendable launch vehicle. It interfaces with the range safety ground system for flight termination, the engine controller for thrust vector control, the ground launch control system for pre-launch checkout, and the tracking network for telemetry. The architecture enforces strict physical and logical separation between the safety-critical FTS and the mission-critical GN&C/telemetry functions.

```
      ┌──────────────────────┐    ┌──────────────────────┐
      │ Range Safety Ground  │    │ Ground Launch Control │
      │ System (Cmd TX)      │    │ System (Umbilical)    │
      └──────────┬───────────┘    └──────────┬───────────┘
                 │ RF cmd                     │ Hardwire
      ┌──────────▼───────────────────────────▼───────────┐
      │            Upper Stage Avionics                   │
      │                                                   │
      │  ┌──────────────┐    ┌──────────────┐            │
      │  │   FTS        │    │   GN&C       │            │
      │  │  (DAL A)     │    │  (DAL C)     │            │
      │  │  Independent │    │              │            │
      │  │  power, proc │    │              │            │
      │  └──────┬───────┘    └──────┬───────┘            │
      │         │                    │                    │
      │  ┌──────▼───────┐    ┌──────▼───────┐            │
      │  │ Ordnance     │    │ Telemetry    │            │
      │  │ Controller   │    │ (DAL D)      │            │
      │  └──────────────┘    └──────┬───────┘            │
      │                             │                    │
      │  ┌──────────────────────────▼───────┐            │
      │  │      Vehicle Management Unit     │            │
      │  │      (Sequencing, Staging)       │            │
      │  └──────────────────────────────────┘            │
      └──────────┬────────────────────┬──────────────────┘
                 │ TVC cmds           │ TLM
      ┌──────────▼───────────┐  ┌────▼──────────────────┐
      │  Engine Controller   │  │ Tracking Network      │
      │  (TVC Actuators)     │  │ (TDRS, Ground Stn)    │
      └──────────────────────┘  └───────────────────────┘
```

## Functional Architecture

### System Functions

| FUN ID       | Function Name                | Description                                                             | Inputs                             | Outputs                              | Dependencies       |
|--------------|------------------------------|-------------------------------------------------------------------------|-------------------------------------|--------------------------------------|---------------------|
| FUN-NAV-01   | Navigation                   | Compute vehicle state (position, velocity, attitude) from IMU data     | IMU measurements                    | Navigation solution (PVT)            | None                |
| FUN-GUD-01   | Guidance                     | Compute steering commands based on navigation state and target orbit   | Navigation solution, target params  | Steering commands                    | FUN-NAV-01          |
| FUN-CTL-01   | Flight Control (TVC)         | Generate TVC actuator commands from steering commands and attitude error| Steering commands, attitude         | TVC gimbal angle commands            | FUN-GUD-01, FUN-NAV-01 |
| FUN-IIP-01   | IIP Computation              | Compute instantaneous impact point for range safety monitoring         | Navigation solution                  | IIP coordinates, corridor status     | FUN-NAV-01          |
| FUN-FT-01    | Flight Termination (Cmd)     | Receive and execute ground-commanded flight termination                 | Range safety RF command              | Ordnance fire commands               | None (independent)  |
| FUN-FT-02    | Autonomous Flight Termination| Detect corridor violation and initiate termination if no ground cmd    | IIP data, corridor boundaries        | Ordnance fire commands               | FUN-IIP-01          |
| FUN-SEQ-01   | Vehicle Sequencing           | Execute flight event timeline (engine start/stop, staging, separation) | Flight timeline, discrete inputs     | Pyro fire, valve commands            | FUN-NAV-01          |
| FUN-TLM-01   | Telemetry Acquisition        | Acquire vehicle health data and format for downlink                    | Sensor data, avionics bus data       | PCM telemetry stream                 | None                |
| FUN-TLM-02   | Telemetry Transmission       | Modulate and transmit telemetry via RF downlink                        | PCM stream                           | RF downlink                          | FUN-TLM-01          |
| FUN-BIT-01   | Pre-Launch BIT               | Execute built-in test of all avionics during pre-launch countdown      | Ground commands, self-test results   | Go/no-go status, fault reports       | None                |

## Physical Architecture

### Component Hierarchy

| CMP ID        | Component Name                        | Type     | Parent        | Description                                                        |
|---------------|---------------------------------------|----------|---------------|--------------------------------------------------------------------|
| CMP-FTS-01    | Flight Termination System Processor   | Unit     | Avionics      | Independent processor for FTS command reception and AFT logic      |
| CMP-FTS-01A   | FTS Command Receiver/Decoder          | Module   | CMP-FTS-01    | Receives and authenticates range safety destruct commands          |
| CMP-FTS-01B   | FTS Software (DO-178C Level A)        | Software | CMP-FTS-01    | AFT algorithm, command processing, safe/arm logic                  |
| CMP-FTS-02    | FTS Ordnance Controller               | Unit     | Avionics      | Safe/arm device, detonation train, shaped charge initiation        |
| CMP-FTS-02A   | Safe/Arm Device                       | Module   | CMP-FTS-02    | Electromechanical device preventing inadvertent ordnance initiation|
| CMP-FTS-03    | FTS Battery                           | Unit     | Avionics      | Independent battery dedicated to FTS (no shared power bus)         |
| CMP-GNC-01    | GN&C Computer                         | Unit     | Avionics      | Navigation, guidance, and flight control processing                |
| CMP-GNC-01A   | Inertial Measurement Unit             | Module   | CMP-GNC-01    | Ring laser gyros and accelerometers for vehicle state sensing      |
| CMP-GNC-01B   | GN&C Software (DO-178C Level C)       | Software | CMP-GNC-01    | Navigation, guidance, control algorithms                           |
| CMP-TLM-01    | Telemetry Processor                   | Unit     | Avionics      | Data acquisition, PCM formatting per IRIG 106                     |
| CMP-TLM-01A   | TLM RF Transmitter                    | Module   | CMP-TLM-01    | S-band FM transmitter for telemetry downlink                       |
| CMP-TLM-01B   | TLM Software (DO-178C Level D)        | Software | CMP-TLM-01    | Data acquisition, formatting, and transmission scheduling          |
| CMP-VMU-01    | Vehicle Management Unit               | Unit     | Avionics      | Sequencing, staging, pyro control for non-FTS ordnance             |
| CMP-PWR-01    | Avionics Power System                 | Unit     | Avionics      | Main battery, power distribution (non-FTS); FTS has CMP-FTS-03    |

## Allocation

| FUN ID       | REQ ID(s)                              | CMP ID(s)                        | Assurance Level | Rationale                                                    |
|--------------|----------------------------------------|----------------------------------|-----------------|--------------------------------------------------------------|
| FUN-NAV-01   | REQ-FUN-001                            | CMP-GNC-01, CMP-GNC-01A         | DAL C           | Navigation error is mission loss, not public safety hazard   |
| FUN-GUD-01   | REQ-FUN-002                            | CMP-GNC-01, CMP-GNC-01B         | DAL C           | Guidance drives mission success; FTS covers safety            |
| FUN-CTL-01   | REQ-FUN-002, REQ-IFC-002              | CMP-GNC-01, CMP-GNC-01B         | DAL C           | TVC control is mission-critical                               |
| FUN-IIP-01   | REQ-FUN-005, REQ-SAF-004              | CMP-GNC-01, CMP-GNC-01B         | DAL C (note)    | IIP feeds AFT; AFT safety is in FTS processor                |
| FUN-FT-01    | REQ-SAF-001, REQ-SAF-002, REQ-IFC-001 | CMP-FTS-01, CMP-FTS-01A         | DAL A           | Ground-commanded FT is the primary range safety function      |
| FUN-FT-02    | REQ-SAF-004, REQ-SAF-005              | CMP-FTS-01, CMP-FTS-01B         | DAL A           | Autonomous FT is backup when ground command is unavailable    |
| FUN-SEQ-01   | REQ-FUN-003                            | CMP-VMU-01                       | DAL C           | Sequencing errors are mission loss                            |
| FUN-TLM-01   | REQ-FUN-004                            | CMP-TLM-01, CMP-TLM-01B         | DAL D           | Telemetry loss is operational inconvenience, not safety       |
| FUN-TLM-02   | REQ-FUN-004                            | CMP-TLM-01, CMP-TLM-01A         | DAL D           | RF transmission supports monitoring only                      |
| FUN-BIT-01   | REQ-IFC-003                            | CMP-FTS-01, CMP-GNC-01, CMP-TLM-01 | Per function | BIT coverage matches the assurance level of each function    |

## Interfaces

### External Interfaces

| IFC ID       | Partner System                  | Data Item                            | Direction      | Protocol          | Timing              |
|--------------|---------------------------------|--------------------------------------|----------------|-------------------|----------------------|
| IFC-EXT-001  | Range Safety Command System     | FTS destruct command (encrypted)     | In             | UHF cmd link      | Event-driven         |
| IFC-EXT-002  | Range Safety Command System     | FTS status telemetry (arm/safe, health) | Out         | Dedicated TLM link| 1 Hz                |
| IFC-EXT-003  | Engine Controller               | TVC gimbal angle commands            | Out            | Serial (MIL-STD-1553 or RS-422) | 50 Hz      |
| IFC-EXT-004  | Engine Controller               | Engine health data (chamber P, temps)| In             | Serial (MIL-STD-1553 or RS-422) | 10 Hz      |
| IFC-EXT-005  | Ground Launch Control System    | Pre-launch config, FTS arm commands  | In             | Hardwire umbilical| Pre-launch only      |
| IFC-EXT-006  | Tracking Network (TDRS/Ground)  | Telemetry downlink (PCM/FM)          | Out            | S-band FM (IRIG 106)| Continuous         |
| IFC-EXT-007  | Payload Adapter                 | Separation command, payload status   | Bidirectional  | Discrete/serial    | Event-driven         |

### Internal Interfaces

| IFC ID       | Source CMP ID  | Target CMP ID  | Data Item                           | Mechanism         | Timing              |
|--------------|----------------|-----------------|-------------------------------------|-------------------|----------------------|
| IFC-INT-001  | CMP-GNC-01     | CMP-FTS-01      | IIP data for AFT algorithm          | One-way serial    | 1 Hz                 |
| IFC-INT-002  | CMP-GNC-01     | CMP-VMU-01      | Sequencing triggers (nav-derived)   | Discrete/serial   | Event-driven         |
| IFC-INT-003  | CMP-GNC-01     | CMP-TLM-01      | GN&C telemetry parameters           | Internal bus      | 50 Hz                |
| IFC-INT-004  | CMP-FTS-01     | CMP-FTS-02      | Ordnance fire command               | Dedicated hardwire| Event-driven         |
| IFC-INT-005  | CMP-FTS-01     | CMP-TLM-01      | FTS health telemetry                | One-way serial    | 1 Hz                 |
| IFC-INT-006  | CMP-VMU-01     | CMP-TLM-01      | Sequencing event status             | Internal bus      | Event-driven         |
| IFC-INT-007  | CMP-FTS-03     | CMP-FTS-01      | Independent FTS power               | Dedicated harness | Continuous           |
| IFC-INT-008  | CMP-PWR-01     | CMP-GNC-01, CMP-TLM-01, CMP-VMU-01 | Main avionics power | Power harness | Continuous       |

## Failure Containment / Partitioning

### FTS-GN&C Independence

The fundamental safety architecture is the physical and logical independence of the FTS from all other avionics functions. This independence is enforced at every level:

**Processing independence:** CMP-FTS-01 is a separate processor board with its own firmware ROM, RAM, and clock. No shared code, no shared memory, no common-mode software.

**Power independence:** CMP-FTS-03 is a dedicated battery connected only to FTS components. Total failure of CMP-PWR-01 (main avionics power) does not affect FTS operation.

**Communication independence:** The only data path from GN&C to FTS is IFC-INT-001, a one-way serial link carrying IIP data. This link is unidirectional at the physical layer (transmit-only on GN&C side, receive-only on FTS side). FTS cannot be commanded, inhibited, or influenced by GN&C software. If IFC-INT-001 fails, the FTS falls back to ground-commanded termination only (FUN-FT-01), which does not require IIP data.

**RF independence:** FTS command reception (CMP-FTS-01A) operates on a dedicated UHF frequency separate from the S-band telemetry downlink. RF interference on the telemetry link cannot affect FTS command reception.

### DAL Partitioning

The three DO-178C software components are developed under different DALs with no shared development artifacts:

| CMP ID        | DAL   | Rationale                                                      |
|---------------|-------|----------------------------------------------------------------|
| CMP-FTS-01B   | DAL A | FTS software failure is catastrophic (failure to terminate)    |
| CMP-GNC-01B   | DAL C | GN&C failure is mission loss; FTS provides safety backup       |
| CMP-TLM-01B   | DAL D | Telemetry loss is an operational inconvenience                 |

No credit is taken for GN&C or telemetry in the FTS safety argument. The FTS safety case stands alone.

### Ordnance Safety

The FTS ordnance chain (CMP-FTS-02) implements a two-stage safety architecture:
1. **Safe/Arm Device (CMP-FTS-02A):** Electromechanical device that physically interrupts the detonation train. Armed only by ground command via IFC-EXT-005 during the terminal countdown. Status is telemetered via IFC-EXT-002.
2. **Fire Command:** Requires both safe/arm in armed state AND a valid fire command from CMP-FTS-01. Inadvertent ordnance initiation requires simultaneous failure of the safe/arm device AND spurious fire command generation, a combination analyzed as extremely improbable per EWR 127-1.

## Architecture Decisions

### AD-01: Physically Separate FTS Processor over Partitioned Software

**Decision:** Implement the FTS on a physically separate processor (CMP-FTS-01) rather than a software partition on the GN&C computer.

**Rationale:** EWR 127-1 requires that the FTS be independent of the vehicle guidance system. While software partitioning (e.g., ARINC 653) can provide logical independence, range safety authorities have historically required physical separation for launch vehicle FTS, and the independence argument for a separate processor is unambiguous. A software partition on the GN&C computer would introduce common-mode concerns (shared processor, shared power, shared clock) that would require extensive additional evidence for range safety certification.

**Trade-off:** Additional hardware mass, volume, and power for a separate processor. Accepted because the certification path is significantly cleaner and range safety review risk is lower.

### AD-02: One-Way IIP Data Link from GN&C to FTS

**Decision:** Provide IIP data to the FTS autonomous flight termination algorithm via a one-way serial link (IFC-INT-001) rather than a bidirectional bus.

**Rationale:** The one-way link ensures that FTS cannot be influenced by GN&C software beyond receiving IIP position data. If the link fails or transmits erroneous data, the AFT algorithm cannot determine corridor status and will not autonomously terminate; ground-commanded termination remains fully functional via IFC-EXT-001. The failure mode of a broken IIP link is conservative (no autonomous termination, ground takes over) rather than hazardous.

**Trade-off:** FTS cannot receive GN&C health status or supplementary navigation data. Accepted because the safety benefit of enforced one-way data flow outweighs the loss of supplementary information.

### AD-03: DO-178C Level A for FTS Software, Level C for GN&C

**Decision:** Apply DO-178C Level A only to FTS software (CMP-FTS-01B) and Level C to GN&C software (CMP-GNC-01B), rather than Level A for all flight software.

**Rationale:** The consequence of FTS software failure is catastrophic (failure to terminate a hazardous vehicle), warranting Level A. GN&C software failure results in mission loss (incorrect trajectory) but not public safety hazard, because the FTS provides an independent safety net. Applying Level A to GN&C would approximately triple the GN&C verification effort without improving public safety, since the safety argument does not take credit for GN&C correctness.

**Trade-off:** GN&C software has higher residual defect risk at Level C than at Level A. Accepted because the FTS safety case is independent of GN&C correctness, and the cost/schedule impact of Level A for GN&C is not justified by safety benefit.
