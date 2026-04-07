# Architecture

## System Context

The CubeSat Constellation operates as a distributed system of 12 spacecraft in LEO, coordinated by a ground-based mission operations center. Each spacecraft is an autonomous node that images, processes, stores, and relays data through the intersatellite link mesh. The ground segment provides orbit determination updates, imaging campaign commands, and constellation health monitoring.

```
                     ┌─────────────────────┐
                     │  Ground Segment      │
                     │  (Mission Ops Center)│
                     └────────┬────────────┘
                              │ CCSDS TM/TC
                     ┌────────▼────────────┐
                     │  Ground Station      │
                     │  Network (SLE)       │
                     └────────┬────────────┘
                              │ S-band
            ┌─────────────────┼─────────────────┐
            │                 │                 │
      ┌─────▼─────┐    ┌─────▼─────┐    ┌─────▼─────┐
      │   SC-01    │◄──►│   SC-02    │◄──►│   SC-12    │
      │  (6U Bus)  │ ISL│  (6U Bus)  │ ISL│  (6U Bus)  │
      └────────────┘    └────────────┘    └────────────┘
            │                 │                 │
      ┌─────▼─────┐    ┌─────▼─────┐    ┌─────▼─────┐
      │  Payload   │    │  Payload   │    │  Payload   │
      │ (Imaging)  │    │ (Imaging)  │    │ (Imaging)  │
      └────────────┘    └────────────┘    └────────────┘
```

## Functional Architecture

### System Functions

| FUN ID       | Function Name                    | Description                                                             | Inputs                             | Outputs                              | Dependencies       |
|--------------|----------------------------------|-------------------------------------------------------------------------|-------------------------------------|--------------------------------------|---------------------|
| FUN-IMG-01   | Payload Imaging                  | Acquire multispectral Earth observation imagery per scheduling commands | Imaging commands, attitude data      | Raw image frames, metadata           | FUN-ATT-01          |
| FUN-IMG-02   | On-Board Image Processing        | Compress, quality-check, and packetize imagery for downlink            | Raw image frames                     | Compressed image packets             | FUN-IMG-01          |
| FUN-NAV-01   | Orbit Determination              | Compute spacecraft state using GPS and propagated ephemeris            | GPS data, clock                      | Position/velocity solution           | None                |
| FUN-NAV-02   | Orbit Maintenance                | Plan and execute station-keeping maneuvers                              | Orbit state, constellation geometry  | Maneuver commands                    | FUN-NAV-01          |
| FUN-ATT-01   | Attitude Determination & Control | Three-axis stabilized pointing for imaging and comm                    | Star tracker, gyro, magnetometer     | Attitude solution, actuator commands | None                |
| FUN-COM-01   | Ground Communication             | TM/TC via CCSDS protocol stack over S-band                            | TM packets, TC packets               | RF uplink/downlink                   | None                |
| FUN-COM-02   | Intersatellite Link              | Data relay between spacecraft in the constellation mesh                | Data packets, routing table           | Relayed data packets                 | FUN-COM-01          |
| FUN-CON-01   | Constellation Management         | Coordinate imaging schedules, mesh routing, and health across fleet    | Spacecraft health, orbit states       | Schedule commands, routing updates   | FUN-NAV-01          |
| FUN-PWR-01   | Power Management                 | Solar array regulation, battery charge/discharge, load shedding        | Solar array current, battery SOC      | Regulated bus power, load shed cmds  | None                |
| FUN-FDIR-01  | Fault Detection and Recovery     | Detect anomalies and execute autonomous recovery or safe-hold          | Health telemetry, watchdog timers     | Recovery actions, mode transitions   | All                 |

## Physical Architecture

### Component Hierarchy (per spacecraft)

| CMP ID        | Component Name                        | Type     | Parent        | Description                                                        |
|---------------|---------------------------------------|----------|---------------|--------------------------------------------------------------------|
| CMP-OBC-01    | On-Board Computer                     | Unit     | Spacecraft    | Radiation-tolerant processor; runs FSW for all on-board functions   |
| CMP-OBC-01A   | OBC Flight Software                   | Software | CMP-OBC-01    | RTOS, C&DH, FDIR, orbit maintenance, scheduling                   |
| CMP-SDR-01    | Software-Defined Radio                | Unit     | Spacecraft    | S-band ground link and UHF/S-band ISL transceiver                  |
| CMP-SDR-01A   | SDR Ground Link Firmware              | Software | CMP-SDR-01    | CCSDS TM/TC framing, modulation/demodulation                       |
| CMP-SDR-01B   | SDR ISL Firmware                      | Software | CMP-SDR-01    | Proximity-1 protocol, mesh routing                                  |
| CMP-PAY-01    | Optical Payload                       | Unit     | Spacecraft    | Multispectral imager, focal plane, on-board processing             |
| CMP-ADCS-01   | ADCS Assembly                         | Unit     | Spacecraft    | Star tracker, gyro, magnetometer, reaction wheels, magnetorquers   |
| CMP-EPS-01    | Electrical Power System               | Unit     | Spacecraft    | Solar panels, battery, power distribution, battery charge regulator|
| CMP-PROP-01   | Propulsion System                     | Unit     | Spacecraft    | Cold-gas or electric propulsion for orbit maintenance               |
| CMP-CON-01    | Constellation Manager (Ground)        | Software | Ground Segment| Scheduling, fleet health monitoring, mesh routing coordination     |

## Allocation

| FUN ID       | REQ ID(s)                              | CMP ID(s)                   | Assurance Level   | Rationale                                                    |
|--------------|----------------------------------------|-----------------------------|-------------------|--------------------------------------------------------------|
| FUN-IMG-01   | REQ-FUN-001                            | CMP-PAY-01, CMP-ADCS-01    | Class C           | Imaging is the primary mission function                      |
| FUN-IMG-02   | REQ-FUN-001                            | CMP-PAY-01, CMP-OBC-01     | Class C           | On-board processing supports data volume management           |
| FUN-NAV-01   | REQ-FUN-005                            | CMP-OBC-01                  | Class C           | Orbit knowledge drives station-keeping accuracy               |
| FUN-NAV-02   | REQ-FUN-005, REQ-SAF-002              | CMP-OBC-01, CMP-PROP-01    | Class C (elevated)| Collision avoidance has safety relevance                      |
| FUN-ATT-01   | REQ-FUN-001                            | CMP-ADCS-01                 | Class C           | Pointing drives image quality                                 |
| FUN-COM-01   | REQ-FUN-004, REQ-IFC-001              | CMP-SDR-01, CMP-SDR-01A    | Class C           | Ground communication is mission-essential                     |
| FUN-COM-02   | REQ-FUN-003, REQ-IFC-002              | CMP-SDR-01, CMP-SDR-01B    | Class C           | ISL is a constellation-enabling capability                    |
| FUN-CON-01   | REQ-FUN-002, REQ-SAF-004              | CMP-CON-01                  | Class C           | Constellation coordination drives revisit guarantee           |
| FUN-PWR-01   | REQ-FUN-006                            | CMP-EPS-01                  | Class C           | Power management enables all other functions                  |
| FUN-FDIR-01  | REQ-SAF-001, REQ-SAF-003              | CMP-OBC-01, CMP-OBC-01A    | Class C (elevated)| FDIR prevents hazardous spacecraft behavior                   |

## Interfaces

### External Interfaces

| IFC ID       | Partner System                  | Data Item                            | Direction      | Protocol          | Timing              |
|--------------|---------------------------------|--------------------------------------|----------------|-------------------|----------------------|
| IFC-EXT-001  | Ground Station Network          | Telemetry frames                     | Out            | CCSDS TM (132.0-B)| Per contact pass    |
| IFC-EXT-002  | Ground Station Network          | Telecommand packets                  | In             | CCSDS TC (231.0-B)| Per contact pass    |
| IFC-EXT-003  | Adjacent Spacecraft (ISL)       | Data relay packets, routing updates  | Bidirectional  | CCSDS Prox-1 (211.0-B)| Continuous       |
| IFC-EXT-004  | GPS Constellation               | PVT solution, time                   | In             | L1 C/A             | 1 Hz               |
| IFC-EXT-005  | Mission Operations Center       | Scheduling commands, orbit updates   | Bidirectional  | CCSDS SLE (913.1-B)| Per contact pass   |
| IFC-EXT-006  | Space Weather Service           | Radiation alerts, geomagnetic data   | In             | CCSDS message      | Event-driven        |

### Internal Interfaces (per spacecraft)

| IFC ID       | Source CMP ID  | Target CMP ID  | Data Item                           | Mechanism         | Timing              |
|--------------|----------------|-----------------|-------------------------------------|-------------------|----------------------|
| IFC-INT-001  | CMP-OBC-01     | CMP-SDR-01      | TM packets, TC routing              | SpaceWire / UART  | Continuous           |
| IFC-INT-002  | CMP-OBC-01     | CMP-PAY-01      | Imaging commands, timing sync       | SpaceWire         | Per imaging event    |
| IFC-INT-003  | CMP-PAY-01     | CMP-OBC-01      | Image data packets                  | SpaceWire         | During imaging       |
| IFC-INT-004  | CMP-ADCS-01    | CMP-OBC-01      | Attitude solution, sensor data      | I2C / SPI         | 10 Hz                |
| IFC-INT-005  | CMP-OBC-01     | CMP-ADCS-01     | Attitude commands, mode commands    | I2C / SPI         | 10 Hz                |
| IFC-INT-006  | CMP-EPS-01     | CMP-OBC-01      | Battery SOC, bus voltage, power status | I2C            | 1 Hz                 |
| IFC-INT-007  | CMP-OBC-01     | CMP-PROP-01     | Maneuver commands, valve commands   | GPIO / serial     | Event-driven         |

## Failure Containment / Partitioning

### Spacecraft-Level FDIR

Each spacecraft implements a three-tier FDIR hierarchy:
1. **Component-level:** Hardware watchdog timers on OBC, SDR, and payload processors detect lockups and trigger local resets.
2. **Subsystem-level:** OBC flight software monitors health telemetry from each subsystem against predefined limits. Out-of-limit conditions trigger subsystem-level recovery (e.g., payload power cycle, ADCS mode reversion).
3. **System-level:** Persistent faults or multiple simultaneous anomalies trigger transition to MODE-002 (Safe-Hold), which powers off non-essential loads, maintains coarse sun-pointing for power-positive operation, and broadcasts a beacon on the ISL for ground notification.

### Constellation-Level Fault Handling

The ground-based constellation manager (CMP-CON-01) monitors fleet health and detects spacecraft loss. Upon detecting a lost spacecraft (3 consecutive missed contacts per REQ-SAF-004), the constellation manager recalculates ISL mesh routes and imaging schedules for the remaining spacecraft, entering MODE-003 (Constellation-Reconfig). This reconfiguration accepts degraded revisit performance rather than risking constellation stability.

### Radiation Mitigation (Class C Tailoring)

Class C tailoring accepts COTS processors with radiation characterization rather than full rad-hard qualification. Mitigation relies on:
- EDAC (SECDED) on all OBC memory (REQ-FUN-006)
- Periodic memory scrubbing (every 60 seconds)
- Software-based watchdog and heartbeat monitoring
- Safe-hold mode as the ultimate recovery for uncorrectable SEU accumulation

## Architecture Decisions

### AD-01: CCSDS Protocol Stack over Proprietary Protocols

**Decision:** Use the CCSDS protocol stack (Space Packet, TM/TC Data Link, Proximity-1) for all communication links rather than a proprietary protocol.

**Rationale:** CCSDS compliance enables ground station interoperability across the multi-provider polar ground station network without custom protocol adaptation at each site. The ISL uses CCSDS Proximity-1, which is designed for short-range spacecraft-to-spacecraft links and provides the store-and-forward capability needed for mesh routing.

**Trade-off:** CCSDS framing overhead is higher than a minimal proprietary protocol. Accepted because the interoperability benefit outweighs the bandwidth cost on the already-constrained S-band link.

### AD-02: Ground-Based Constellation Management over Fully Autonomous

**Decision:** Place the constellation management function (scheduling, mesh routing coordination, orbit maintenance planning) in the ground segment rather than distributing it fully across the spacecraft.

**Rationale:** Ground-based management simplifies on-board software complexity, reduces OBC processing requirements, and keeps the human-in-the-loop for safety-relevant decisions (collision avoidance override, constellation reconfiguration). On-board autonomy is limited to safe-hold (MODE-002) and time-critical collision avoidance (REQ-SAF-002).

**Trade-off:** Requires sufficient ground contact for timely commanding. Mitigated by the ISL mesh, which allows ground commands to reach any spacecraft through relay even when only one spacecraft is in direct ground contact.

### AD-03: Cold-Gas Propulsion over Electric Propulsion

**Decision:** Use cold-gas propulsion for orbit maintenance rather than electric propulsion.

**Rationale:** Cold-gas provides immediate thrust (no warm-up or duty cycle constraints), simplifying autonomous collision avoidance maneuver execution within the 4-hour timeline required by REQ-SAF-002. The delta-V budget for a 5-year mission in 500 km SSO is within cold-gas capability for a 6U form factor. Electric propulsion would provide higher specific impulse but requires extended thruster firing periods that complicate attitude control and imaging scheduling.

**Trade-off:** Lower Isp reduces total delta-V margin. Accepted because the operational simplicity and collision avoidance response time are higher priorities for a Class C mission.
