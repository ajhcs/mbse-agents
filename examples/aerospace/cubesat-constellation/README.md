# CubeSat Constellation

## Overview

The CubeSat Constellation is a 12-unit low Earth orbit (LEO) formation providing multispectral Earth observation with 24-hour global revisit. Each 6U spacecraft carries an optical payload and a software-defined radio supporting intersatellite links (ISL) and CCSDS-compliant ground communication. The constellation operates autonomously between ground contacts, performing on-board orbit maintenance, data routing through the ISL mesh, and payload scheduling coordinated by a ground-based mission operations center.

The system is classified NASA Class C under NPR 7150.2 with mission assurance tailored per NPR 7123.1. Class C tailoring accepts higher risk for cost-constrained missions: formal independent verification is reduced, and heritage hardware with existing radiation characterization replaces full qualification testing for non-safety-critical components.

## System Boundary

**Inside the system boundary:**
- 12 spacecraft bus avionics (OBC, EPS, ADCS, propulsion)
- Software-defined radio (ISL + ground link)
- Optical payload instrument and on-board processing
- Constellation management software (on-board and ground segment)
- Intersatellite link mesh network

**Outside the system boundary:**
- Ground segment infrastructure (antenna network, mission control center)
- Launch vehicle and deployment system
- Third-party relay satellites (if used for emergency communication)
- End-user data distribution and processing systems
- Space weather monitoring services (consumed data only)

## Operational Environment

The constellation operates in a 500 km sun-synchronous orbit with an orbital lifetime target of 5 years. Each spacecraft experiences approximately 5,500 thermal cycles per year, total ionizing dose of approximately 10 krad(Si) over mission life, and single-event upset rates requiring EDAC on all critical memory. Ground contacts occur via polar ground stations with an average contact window of 8 minutes per pass, 4-6 passes per day per spacecraft.

## Operating Modes

| Mode ID   | Name              | Description                                                    | Active Functions                                | Constraints                                        |
|-----------|-------------------|----------------------------------------------------------------|-------------------------------------------------|----------------------------------------------------|
| MODE-001  | Normal-Ops        | Nominal imaging, data relay, and orbit maintenance             | All FUN- functions active                       | None                                               |
| MODE-002  | Safe-Hold         | Spacecraft-level safe mode after fault detection               | EPS, thermal, coarse attitude only              | Payload off; ISL beacon only; awaiting ground cmd   |
| MODE-003  | Constellation-Reconfig | One or more spacecraft lost; mesh re-routing active       | ISL re-routing, revised scheduling              | Degraded revisit time; coverage gaps possible       |
| MODE-004  | Eclipse-Management| Reduced operations during extended eclipse sequences           | Payload duty-cycled; ISL maintained             | Power-positive budget enforced; non-essential loads shed |

## Key Technical Challenges

1. **Radiation tolerance on COTS hardware.** Class C tailoring permits commercial-grade processors with radiation characterization rather than full rad-hard parts. Demonstrating acceptable single-event effects mitigation through software FDIR and EDAC requires mission-specific radiation analysis and test data.

2. **Autonomous orbit maintenance.** With limited ground contact windows, each spacecraft must execute autonomous station-keeping maneuvers to maintain the constellation geometry. Collision avoidance using TLE/CDM data must be performed on-board with ground override capability.

3. **ISL mesh routing under dynamic topology.** The intersatellite link network topology changes as spacecraft enter and exit mutual visibility. The routing algorithm must converge within one orbit period and handle single-link failures without data loss.

4. **Ground segment interface standardization.** CCSDS Space Link Extension (SLE) services must interface with multiple ground station providers, each with different SLE implementation profiles, requiring robust protocol negotiation and fallback mechanisms.

## Stakeholders

| Stakeholder                  | Role                                                                  |
|------------------------------|-----------------------------------------------------------------------|
| Mission operations center    | Constellation command, scheduling, orbit maintenance planning         |
| Payload operations team      | Imaging campaign planning, data quality assessment                    |
| NASA mission assurance       | Class C mission assurance oversight, waiver authority                  |
| Launch services provider     | Deployment interface, orbit insertion accuracy                        |
| End-user community           | Earth observation data consumers; drive revisit and resolution needs   |

## Standards Applicability

| Standard          | Applicability                                                                              |
|-------------------|--------------------------------------------------------------------------------------------|
| NPR 7123.1        | Systems engineering processes; tailored for Class C mission risk posture                   |
| NPR 7150.2        | Software engineering; Class C software classification drives V&V depth                     |
| CCSDS 133.0-B     | Space Packet Protocol for telemetry and telecommand framing                                |
| CCSDS 132.0-B     | TM Space Data Link Protocol for ground downlink                                            |
| CCSDS 231.0-B     | TC Space Data Link Protocol for ground uplink                                              |
| CCSDS 211.0-B     | Proximity-1 Space Link Protocol for intersatellite link                                    |
| NASA-STD-8739.8   | Software assurance and safety for Class C missions                                         |
