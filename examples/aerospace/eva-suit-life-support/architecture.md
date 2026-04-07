# Architecture

## System Context

The EVA Suit Life Support System (PLSS) is a self-contained portable unit worn on the crewmember's back during extravehicular activity. It interfaces with the pressure suit garment on the crew side and with the vehicle airlock/umbilical system on the vehicle side. The EVA flight controller monitors PLSS telemetry in real time through the suit communication link relayed via the vehicle communication system.

```
                     ┌──────────────────────┐
                     │  Vehicle Comm System  │
                     │  (ISS / Orion)        │
                     └──────────┬───────────┘
                                │ RF relay
                     ┌──────────▼───────────┐
                     │  EVA Flight           │
                     │  Controller (MCC)     │
                     └──────────────────────┘

      ┌─────────────────────────────────────────────────┐
      │             Suit Pressure Garment                │
      │  (Helmet, HUT, Gloves, LCVG, Boots)             │
      └─────────────────────┬───────────────────────────┘
                            │ Gas, water, data
      ┌─────────────────────▼───────────────────────────┐
      │                    PLSS                          │
      │  ┌──────────┐ ┌──────────┐ ┌──────────┐        │
      │  │ O2 Supply│ │ CDRA     │ │ Thermal  │        │
      │  │ & Reg    │ │ (CO2     │ │ Control  │        │
      │  │          │ │  Removal)│ │ (LCVG +  │        │
      │  └──────────┘ └──────────┘ │ Sublim.) │        │
      │  ┌──────────┐ ┌──────────┐ └──────────┘        │
      │  │ Sec. O2  │ │ C&W /    │                      │
      │  │ Pack     │ │ Avionics │                      │
      │  └──────────┘ └──────────┘                      │
      └─────────────────────┬───────────────────────────┘
                            │ Umbilical (when tethered)
      ┌─────────────────────▼───────────────────────────┐
      │        Vehicle Airlock / EVA Support             │
      │  (O2 recharge, water recharge, power)            │
      └─────────────────────────────────────────────────┘
```

## Functional Architecture

### System Functions

| FUN ID       | Function Name                | Description                                                             | Inputs                             | Outputs                              | Dependencies       |
|--------------|------------------------------|-------------------------------------------------------------------------|-------------------------------------|--------------------------------------|---------------------|
| FUN-PRS-01   | Pressure Regulation          | Maintain suit internal pressure at 4.3 psia; relief valve protection   | O2 supply, suit leak rate           | Regulated suit atmosphere             | FUN-O2-01           |
| FUN-O2-01    | Oxygen Supply                | Provide breathing oxygen from primary tank through regulator            | Primary O2 tank pressure            | Regulated O2 flow                     | None                |
| FUN-O2-02    | Secondary O2 Supply          | Provide emergency O2 from SOP upon primary failure or crew command     | SOP activation signal               | Emergency O2 flow                     | None                |
| FUN-CO2-01   | CO2 Removal                  | Remove CO2 from suit atmosphere using swing-bed CDRA                   | Suit atmosphere, CDRA cycle timing  | Scrubbed atmosphere                   | FUN-PRS-01          |
| FUN-THR-01   | Thermal Control              | Reject metabolic heat via LCVG water loop and sublimator/radiator      | LCVG return water, ice sublimation  | Cooled LCVG supply water              | None                |
| FUN-HUM-01   | Humidity Control             | Remove excess moisture from suit atmosphere                             | Suit atmosphere                     | Dehumidified atmosphere               | FUN-CO2-01          |
| FUN-CW-01    | Caution and Warning          | Monitor PLSS parameters, annunciate off-nominal conditions to crew     | All sensor data                      | Audio/visual alerts, telemetry        | All                 |
| FUN-TLM-01   | Telemetry Transmission       | Transmit PLSS health data to EVA flight controller via suit comm       | C&W sensor data                      | Telemetry data stream                 | FUN-CW-01           |
| FUN-UMB-01   | Umbilical Interface          | Accept vehicle O2, water, power when tethered; manage disconnect       | Vehicle umbilical connection         | Supplemental consumables              | None                |

## Physical Architecture

### Component Hierarchy

| CMP ID        | Component Name                        | Type     | Parent        | Description                                                        |
|---------------|---------------------------------------|----------|---------------|--------------------------------------------------------------------|
| CMP-O2-01     | Primary Oxygen Supply Assembly        | Unit     | PLSS          | High-pressure O2 tank, regulator, check valves, relief valve       |
| CMP-SOP-01    | Secondary Oxygen Pack                 | Unit     | PLSS          | Separate O2 supply with auto-activation valve and manual override  |
| CMP-PREG-01   | Pressure Regulation Assembly          | Unit     | PLSS          | Suit pressure regulator, positive/negative relief valves           |
| CMP-CDRA-01   | CO2 Removal Assembly                  | Unit     | PLSS          | Swing-bed amine sorbent system with cycling valves                 |
| CMP-TCS-01    | Thermal Control Subsystem             | Unit     | PLSS          | LCVG water pump, heat exchanger, sublimator, water reservoir       |
| CMP-TCS-01A   | Sublimator                            | Module   | CMP-TCS-01    | Porous plate sublimator; primary heat rejection to vacuum          |
| CMP-TCS-01B   | LCVG Water Pump                       | Module   | CMP-TCS-01    | Circulates cooling water through the LCVG garment                  |
| CMP-CW-01     | Caution and Warning Electronics       | Unit     | PLSS          | Sensor acquisition, limit checking, alert generation, data logging |
| CMP-CW-01A    | Sensor Suite                          | Module   | CMP-CW-01     | O2 pressure, CO2 PPM, suit pressure, temperatures, humidity        |
| CMP-EPS-01    | Battery and Power Distribution        | Unit     | PLSS          | Lithium-ion battery, power bus, load switches                      |
| CMP-UMB-01    | Umbilical Interface Assembly          | Unit     | PLSS          | Quick-disconnect for O2, water, power, data from vehicle           |
| CMP-COMM-01   | Communication Interface               | Unit     | PLSS          | Data link to suit comm system for telemetry relay                  |

## Allocation

| FUN ID       | REQ ID(s)                              | CMP ID(s)                       | Assurance Level        | Rationale                                                    |
|--------------|----------------------------------------|---------------------------------|------------------------|--------------------------------------------------------------|
| FUN-PRS-01   | REQ-FUN-001, REQ-SAF-001              | CMP-PREG-01, CMP-O2-01         | Human-rated (critical) | Pressure loss is catastrophic; two-fault tolerance required   |
| FUN-O2-01    | REQ-FUN-002, REQ-FUN-006              | CMP-O2-01                       | Human-rated (critical) | O2 depletion is catastrophic                                  |
| FUN-O2-02    | REQ-SAF-002                            | CMP-SOP-01                      | Human-rated (critical) | Emergency O2 is last line of defense                          |
| FUN-CO2-01   | REQ-FUN-003, REQ-SAF-004              | CMP-CDRA-01                     | Human-rated (critical) | CO2 buildup leads to crew incapacitation                      |
| FUN-THR-01   | REQ-FUN-004                            | CMP-TCS-01, CMP-TCS-01A, CMP-TCS-01B | Human-rated (critical) | Thermal runaway leads to hyperthermia             |
| FUN-HUM-01   | REQ-FUN-005                            | CMP-CDRA-01, CMP-TCS-01        | Human-rated             | Humidity is comfort and sensor accuracy concern               |
| FUN-CW-01    | REQ-SAF-003, REQ-SAF-004              | CMP-CW-01, CMP-CW-01A          | Human-rated (critical) | Alerting enables crew-initiated abort                         |
| FUN-TLM-01   | REQ-IFC-002                            | CMP-CW-01, CMP-COMM-01         | Human-rated             | Ground monitoring is defense-in-depth                         |
| FUN-UMB-01   | REQ-IFC-001                            | CMP-UMB-01                      | Human-rated             | Umbilical is not EVA-critical but supports pre/post EVA       |

## Interfaces

### External Interfaces

| IFC ID       | Partner System                  | Data Item                            | Direction      | Protocol          | Timing              |
|--------------|---------------------------------|--------------------------------------|----------------|-------------------|----------------------|
| IFC-EXT-001  | Suit Pressure Garment           | Breathing gas, LCVG water            | Out            | Pneumatic/hydraulic| Continuous          |
| IFC-EXT-002  | Suit Pressure Garment           | Return gas (CO2, humidity, heat)     | In             | Pneumatic          | Continuous           |
| IFC-EXT-003  | Suit Communication System       | Telemetry data, C&W alerts           | Out            | Digital serial     | 1 Hz (TLM), event (alerts) |
| IFC-EXT-004  | Vehicle Umbilical               | O2, cooling water, electrical power  | In             | Pneumatic/electrical| When tethered      |
| IFC-EXT-005  | Vehicle Airlock Support         | Recharge O2, recharge water, battery charge | Bidirectional | Mechanical QD  | Post-EVA             |
| IFC-EXT-006  | Crew (physiological)            | Metabolic O2 consumption, CO2 production, heat | In     | Physiological      | Continuous           |

### Internal Interfaces

| IFC ID       | Source CMP ID  | Target CMP ID  | Data Item                           | Mechanism         | Timing              |
|--------------|----------------|-----------------|-------------------------------------|-------------------|----------------------|
| IFC-INT-001  | CMP-O2-01      | CMP-PREG-01     | Regulated O2 supply                 | Pneumatic tubing  | Continuous           |
| IFC-INT-002  | CMP-SOP-01     | CMP-PREG-01     | Emergency O2 supply                 | Pneumatic tubing  | On activation        |
| IFC-INT-003  | CMP-PREG-01    | CMP-CDRA-01     | Pressurized suit atmosphere         | Pneumatic duct    | Continuous           |
| IFC-INT-004  | CMP-CDRA-01    | CMP-TCS-01      | Scrubbed atmosphere (for cooling)   | Pneumatic duct    | Continuous           |
| IFC-INT-005  | CMP-CW-01A     | CMP-CW-01       | Sensor readings (P, T, ppCO2, RH)  | Analog/digital    | 1 Hz sample rate     |
| IFC-INT-006  | CMP-EPS-01     | All CMPs         | Regulated power bus                 | Electrical harness| Continuous           |
| IFC-INT-007  | CMP-CW-01      | CMP-COMM-01     | Telemetry packets                   | Digital serial    | 1 Hz                 |

## Failure Containment / Partitioning

### Two-Fault Tolerance Architecture

For catastrophic hazards (loss of suit pressure, loss of O2), the PLSS architecture provides two independent inhibits per failure path:

**Pressure loss path:**
1. Primary pressure regulator maintains suit pressure (CMP-PREG-01 active regulation)
2. Positive relief valve prevents overpressure; check valves prevent reverse flow (CMP-PREG-01 passive protection)
3. Secondary O2 pack provides independent pressure source if primary regulator fails (CMP-SOP-01)

**O2 depletion path:**
1. Primary O2 supply with regulated flow (CMP-O2-01)
2. Flow sensor and low-O2 alarm triggers crew abort (CMP-CW-01)
3. Secondary O2 pack auto-activates on primary supply failure (CMP-SOP-01)

**CO2 buildup path:**
1. CDRA actively scrubs CO2 (CMP-CDRA-01)
2. CO2 sensor with tiered alerting enables crew to reduce metabolic rate (CMP-CW-01)
3. Emergency purge valve allows direct suit atmosphere venting and O2 replenishment as a last resort (CMP-PREG-01)

### Independence of Secondary O2 Pack

CMP-SOP-01 is physically and functionally independent from CMP-O2-01. It has its own pressure vessel, regulator, and activation mechanism. The auto-activation valve senses downstream pressure loss and opens without requiring electrical power or C&W software command, providing mechanical independence from the avionics chain.

### Thermal Subsystem Redundancy

The thermal control subsystem provides a backup sublimator feed path (CMP-TCS-01A backup mode) that bypasses the primary water pump (CMP-TCS-01B) using a manual crew-operated valve. This supports MODE-002 (Degraded-Thermal) operation with reduced but survivable thermal rejection until crew abort is complete.

## Architecture Decisions

### AD-01: Swing-Bed CDRA over Lithium Hydroxide (LiOH) Canisters

**Decision:** Use a regenerable amine swing-bed CO2 removal system rather than expendable LiOH canisters.

**Rationale:** Swing-bed CDRA provides continuous CO2 removal without consumable replacement during the sortie. LiOH canisters would require either mid-sortie canister swap (operational burden) or oversized canisters (mass penalty) for the 8-hour sortie duration. The swing-bed design regenerates by vacuum-desorbing CO2 to space in alternating beds, providing indefinite operation as long as power is available.

**Trade-off:** Higher mechanical complexity (cycling valves, two sorbent beds) compared to passive LiOH. The cycling valves are a potential failure mode mitigated by the emergency purge capability. Accepted because the mass and operational advantages outweigh the mechanical complexity for Artemis lunar surface operations requiring long sortie durations.

### AD-02: Sublimator-Based Heat Rejection over Radiator-Only

**Decision:** Use a porous plate sublimator as the primary heat rejection device rather than a body-mounted radiator alone.

**Rationale:** The thermal environment varies dramatically between ISS (cyclic eclipse) and lunar surface (continuous solar exposure on the sunlit side). A sublimator provides heat rejection that is largely independent of the external thermal environment, as it relies on water ice sublimation to vacuum rather than radiative cooling. This provides consistent thermal control across both ISS and Artemis operational environments.

**Trade-off:** Sublimator consumes feedwater, which is a mass-limited consumable that directly constrains sortie duration. Accepted because the thermal environment independence is essential for a dual-mission PLSS design. Water consumption rate is the primary factor in the 8-hour sortie duration limit.

### AD-03: Dedicated Secondary O2 Pack over Shared Primary Tank with Redundant Regulators

**Decision:** Provide a physically separate secondary O2 pack (CMP-SOP-01) rather than a second regulator on the primary O2 tank.

**Rationale:** A separate pressure vessel with its own regulator provides true independence for the second inhibit against O2 loss. If the primary tank fails (leak, structural failure), a second regulator on the same tank provides no protection. The SOP is a self-contained unit with mechanical auto-activation that operates without electrical power, ensuring that the emergency O2 supply is available even in a total avionics failure scenario.

**Trade-off:** Additional mass and volume for a separate pressure vessel. Accepted because the independence argument for the second catastrophic hazard inhibit is significantly stronger with a separate pressure source.
