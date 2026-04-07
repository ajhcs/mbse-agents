# EV Battery Management System

## Overview

The EV Battery Management System (BMS) manages a 800V lithium-ion battery pack consisting of 192 series-connected cells organized in 16 modules of 12 cells each. The BMS monitors individual cell voltages and temperatures, estimates state-of-charge (SoC) and state-of-health (SoH), controls high-voltage contactors for pack connect/disconnect, and manages the thermal regulation loop to maintain cells within safe operating limits. The system provides the vehicle controller with pack-level data for energy management, regenerative braking coordination, and charging control. Thermal runaway detection and propagation prevention is the primary safety function, requiring sub-second isolation of a faulting module from the pack.

## System Boundary

**Inside the system boundary:**
- Cell Monitoring Units (CMU) -- one per module, measuring cell voltage and temperature
- Battery Management Controller (BMC) -- central processing unit for pack-level management
- HV Contactor Driver -- controls main positive, main negative, and pre-charge contactors
- Current sensor interface -- pack-level current measurement
- Thermal management interface -- controls coolant pump and valve actuators
- Isolation monitoring device (IMD) interface
- BMS application software (state estimation, contactor sequencing, thermal control, fault management)

**Outside the system boundary:**
- Battery cells and modules (electrochemical components; BMS monitors but does not manufacture)
- HV contactors (electromechanical devices; BMS controls but does not contain)
- Coolant pump and thermal loop (BMS commands flow rate; pump hardware is external)
- Vehicle controller (receives pack data; commands charge/discharge limits)
- Charging inlet and on-board charger (BMS manages charging profile; charger hardware is external)
- Instrument cluster (displays SoC, range, warnings; HMI hardware is external)
- Crash sensor (vehicle-level; provides crash signal to BMS for emergency disconnect)

## Operational Environment

The BMS operates within an automotive battery enclosure mounted on the vehicle underbody. The HV domain operates at nominal 800V DC (range 580V--920V depending on SoC). Ambient temperature range is -40C to +60C, with cell operating temperature managed to 15C--45C by the thermal loop. The BMS interfaces with the vehicle controller via CAN FD and with the CMUs via daisy-chained isoSPI. The system must withstand crash loads per UN R100 and maintain HV isolation integrity under single-fault conditions.

## Operating Modes

| Mode ID   | Name                    | Description                                                              | Active Functions                                                | Constraints                                                |
|-----------|-------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------|------------------------------------------------------------|
| MODE-001  | Normal Driving          | Pack connected; continuous cell monitoring, SoC/SoH estimation, thermal regulation active | All FUN- functions active                                      | None                                                       |
| MODE-002  | Charging                | Pack connected to external charger; BMS manages charge profile, balancing active | Cell balancing, charge current limiting, thermal regulation    | Maximum charge rate limited by cell temperature and SoH    |
| MODE-003  | Degraded                | One or more CMU faults or thermal anomaly detected; reduced power output | Monitoring active; contactor control active; power derated     | Reduced discharge/charge current limits; driver warning     |
| MODE-004  | Emergency Disconnect    | Thermal runaway detected or crash signal received; contactors opened immediately | Contactor open, isolation monitoring, fault logging             | No HV power available; vehicle enters limp/stop mode       |

## Key Technical Challenges

1. **Thermal runaway propagation prevention.** A single cell thermal runaway can propagate to adjacent cells within seconds. The BMS must detect the onset (rapid voltage drop + temperature spike) and open contactors before propagation can energize the full pack, while the mechanical design provides propagation barriers between modules.

2. **ASIL decomposition between monitoring and actuation.** Cell monitoring (ASIL C) and contactor control (ASIL D) have different integrity requirements. The contactor driver path must achieve ASIL D hardware fault metrics independently of the monitoring path, requiring dedicated safety mechanisms on the contactor control circuit.

3. **State estimation accuracy across aging.** SoC and SoH estimation must remain accurate across the battery lifetime (1,000+ charge cycles, 8+ years) as cell impedance and capacity change. Model-based estimators (extended Kalman filter or equivalent) require periodic recalibration against actual capacity measurements.

4. **800V isolation integrity.** The BMS straddles the HV and LV domains. Galvanic isolation between the CMU measurement circuits (HV side) and the BMC processing circuits (LV side) must be maintained under all fault conditions, including creepage/clearance requirements per IEC 62619.

## Stakeholders

| Stakeholder                    | Role                                                                            |
|--------------------------------|---------------------------------------------------------------------------------|
| Vehicle driver                 | Relies on accurate SoC for range estimation; receives battery warnings          |
| Vehicle OEM integration team   | Integrates BMS into vehicle energy management; responsible for vehicle safety case |
| Tier-1 BMS supplier            | Designs and delivers BMS; holds SEooC safety case for battery management        |
| Type approval authority        | Approves vehicle against UN R100; reviews crash safety and HV isolation evidence |
| Battery cell supplier          | Provides cell specifications and abuse tolerance data consumed by BMS design    |
| Maintenance technician         | Performs HV system service; relies on BMS interlock and diagnostic functions     |

## Standards Applicability

| Standard       | Applicability                                                                                     |
|----------------|---------------------------------------------------------------------------------------------------|
| ISO 26262      | Functional safety lifecycle; ASIL D for contactor control, ASIL C for monitoring; governs HW, SW  |
| UN R100        | Crash safety of electric powertrain; HV isolation post-crash, contactor behavior during impact     |
| IEC 62619      | Safety requirements for secondary lithium cells in industrial applications; abuse testing          |
| ISO 6469       | Safety of electrically propelled road vehicles; HV protection, isolation monitoring               |
| ISO 11898      | CAN and CAN FD physical/data link layer for vehicle communication                                |
