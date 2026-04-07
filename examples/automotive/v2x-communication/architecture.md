# Architecture

## System Context

```mermaid
graph TB
    subgraph VCU["V2X Communication Unit"]
        PC5["CMP-PC5-01<br/>PC5 Radio Module"]
        UU["CMP-UU-01<br/>Cellular Modem"]
        GNSS["CMP-GNSS-01<br/>GNSS Receiver"]
        HSM["CMP-HSM-01<br/>Hardware Security<br/>Module"]
        APP["CMP-APP-01<br/>VCU Application<br/>Processor"]
    end

    VEHICLES["Other Vehicles<br/>(V2V)"]
    RSU["Roadside Units<br/>(V2I)"]
    CELL_NET["Cellular Network<br/>(V2N)"]
    PKI["V2X PKI Backend"]
    ADAS["ADAS Fusion ECU"]
    GWY["Vehicle CAN Gateway"]
    VEH_DYN["Vehicle Dynamics<br/>Sensors (via CAN)"]
    ANT_PC5["PC5 Antenna<br/>(5.9 GHz)"]
    ANT_UU["Uu Antenna<br/>(Cellular)"]
    ANT_GNSS["GNSS Antenna<br/>(Roof-mounted)"]

    VEHICLES <-->|PC5 direct (CAM, DENM)| PC5
    RSU <-->|PC5 direct (CPM, SPAT)| PC5
    CELL_NET <-->|LTE-V2X / 5G NR-V2X| UU
    PKI -->|Certificates, CRL| UU
    ANT_PC5 --- PC5
    ANT_UU --- UU
    ANT_GNSS --- GNSS
    APP -->|CAN FD| ADAS
    GWY -->|Vehicle data (speed, heading)| APP
    VEH_DYN -->|CAN| GWY
```

## Functional Architecture

| FUN ID       | Function Name                    | Description                                                                   | Inputs                                       | Outputs                                       | Dependencies         |
|--------------|----------------------------------|-------------------------------------------------------------------------------|----------------------------------------------|-----------------------------------------------|----------------------|
| FUN-TX-01    | V2X Message Transmission         | Encode and transmit CAM/DENM messages via PC5 and/or Uu                       | Ego vehicle position, speed, heading, events | Transmitted V2X messages                      | FUN-POS-01           |
| FUN-RX-01    | V2X Message Reception            | Receive and decode CAM/DENM/CPM messages from PC5 and Uu interfaces          | Raw RF signals                               | Decoded V2X message content                   | None                 |
| FUN-POS-01   | Position Determination           | Compute ego vehicle position using GNSS + dead-reckoning fusion               | GNSS signals, vehicle speed, heading         | Ego position (lat, lon, altitude, heading)    | None                 |
| FUN-AUTH-01  | Message Authentication           | Verify digital signatures on received messages; sign outgoing messages        | Messages, certificates, HSM keys             | Authentication status per message             | FUN-RX-01            |
| FUN-PLB-01   | Plausibility Checking            | Cross-check received V2X data against ego sensor context for consistency     | Decoded messages, ego sensor feedback        | Plausibility confidence per V2X object         | FUN-RX-01, FUN-AUTH-01 |
| FUN-FMT-01   | ADAS Output Formatting           | Format authenticated, plausibility-checked V2X data for ADAS fusion ECU      | Plausibility-checked objects, trust levels   | Cooperative perception output (CAN FD)        | FUN-PLB-01           |
| FUN-CRT-01   | Certificate Management           | Manage pseudonym rotation, enrollment, CRL updates, and credential storage   | PKI responses, timers                        | Active signing certificate, CRL state         | FUN-AUTH-01          |
| FUN-MOD-01   | PC5/Uu Mode Management           | Select and switch between PC5 direct and Uu cellular modes based on availability | Radio status, congestion metrics            | Active radio mode, channel assignments        | None                 |

## Physical Architecture

| CMP ID        | Component Name                           | Type     | Parent        | Description                                                           |
|---------------|------------------------------------------|----------|---------------|-----------------------------------------------------------------------|
| CMP-PC5-01    | C-V2X PC5 Radio Module                   | Module   | System        | 5.9 GHz ITS-band sidelink transceiver for direct V2X communication    |
| CMP-UU-01     | C-V2X Uu Cellular Modem                  | Module   | System        | LTE-V2X / 5G NR-V2X modem for network-based V2X communication        |
| CMP-GNSS-01   | GNSS Receiver                            | Module   | System        | Multi-constellation (GPS, Galileo, GLONASS) receiver with dead-reckoning |
| CMP-HSM-01    | Hardware Security Module                 | Module   | System        | Tamper-resistant crypto engine for ECDSA signing/verification and key storage |
| CMP-APP-01    | VCU Application Processor               | ECU      | System        | Central processor running V2X protocol stack, plausibility, and ADAS formatting |
| CMP-APP-01A   | V2X Protocol Stack                       | Software | CMP-APP-01    | ETSI ITS-G5 / SAE J3161 message encoding/decoding (QM)               |
| CMP-APP-01B   | CAM/DENM Transmission Manager            | Software | CMP-APP-01    | Message generation, rate adaptation, channel selection (QM)           |
| CMP-APP-01C   | Plausibility and ADAS Formatter          | Software | CMP-APP-01    | Safety-relevant message processing, confidence scoring, E2E output (ASIL B) |
| CMP-APP-01D   | Certificate Lifecycle Manager            | Software | CMP-APP-01    | Pseudonym rotation, enrollment, CRL management (QM)                   |

## Allocation

| FUN ID       | REQ ID(s)                                    | CMP ID(s)                                    | Assurance Level | Rationale                                                          |
|--------------|----------------------------------------------|----------------------------------------------|-----------------|--------------------------------------------------------------------|
| FUN-TX-01    | REQ-FUN-001                                  | CMP-APP-01B, CMP-PC5-01, CMP-UU-01          | QM              | Transmission is a communication function with no direct safety impact |
| FUN-RX-01    | REQ-FUN-002                                  | CMP-APP-01A, CMP-PC5-01, CMP-UU-01          | QM              | Reception and decoding is protocol processing; safety handled downstream |
| FUN-POS-01   | REQ-FUN-003                                  | CMP-GNSS-01                                  | QM              | Position accuracy is a performance concern for transmitted CAM quality |
| FUN-AUTH-01  | REQ-SEC-001, REQ-SEC-002                     | CMP-HSM-01, CMP-APP-01A                     | QM              | Authentication is a security function; contributes to trust level for ADAS |
| FUN-PLB-01   | REQ-SAF-001                                  | CMP-APP-01C                                  | ASIL B          | Plausibility checking prevents false V2X data from reaching safety decisions |
| FUN-FMT-01   | REQ-FUN-004, REQ-SAF-002, REQ-SAF-003       | CMP-APP-01C                                  | ASIL B          | ADAS output formatting is the QM/ASIL boundary; E2E protection enforced here |
| FUN-CRT-01   | REQ-FUN-005, REQ-SEC-002                     | CMP-HSM-01, CMP-APP-01D                     | QM              | Certificate management is a security lifecycle function, not safety-rated |
| FUN-MOD-01   | REQ-FUN-002                                  | CMP-APP-01B, CMP-PC5-01, CMP-UU-01          | QM              | Mode selection is a communication optimization function              |

## Interfaces

### External Interfaces

| IFC ID       | Partner System                       | Data Item                                    | Direction     | Protocol              | Timing                 |
|--------------|--------------------------------------|----------------------------------------------|---------------|-----------------------|------------------------|
| IFC-EXT-001  | ADAS Fusion ECU                      | Cooperative perception objects, trust levels  | Out           | CAN FD (E2E)          | 100 ms cycle (10 Hz)  |
| IFC-EXT-002  | Vehicle CAN Gateway                  | Ego vehicle speed, heading, yaw rate         | In            | CAN                   | 20 ms cycle (50 Hz)   |
| IFC-EXT-003  | V2X PKI Backend (via Uu)            | Enrollment certificates, pseudonyms, CRL     | Bidirectional | TLS 1.3 over cellular | Event-driven (hourly CRL) |
| IFC-EXT-004  | Other V2X Participants (V2V, V2I)    | CAM, DENM, CPM, SPAT messages               | Bidirectional | C-V2X PC5 (5.9 GHz)  | 1-10 Hz per participant |
| IFC-EXT-005  | Cellular Network (V2N)               | V2X messages via network, traffic data       | Bidirectional | LTE-V2X / 5G NR-V2X  | Application-dependent  |

### Internal Interfaces

| IFC ID       | Source CMP ID  | Target CMP ID  | Data Item                                      | Mechanism             | Timing              |
|--------------|----------------|-----------------|------------------------------------------------|-----------------------|---------------------|
| IFC-INT-001  | CMP-PC5-01     | CMP-APP-01A     | Received V2X message frames                    | SPI / SDIO            | Event-driven        |
| IFC-INT-002  | CMP-UU-01      | CMP-APP-01A     | Received V2X message frames (Uu path)          | USB / PCIe            | Event-driven        |
| IFC-INT-003  | CMP-APP-01A    | CMP-HSM-01      | Messages for signature verification/signing    | SPI (secure channel)  | Per-message (<5 ms) |
| IFC-INT-004  | CMP-GNSS-01    | CMP-APP-01      | Position, velocity, time (PVT) solution        | UART / SPI            | 10 Hz (100 ms)      |
| IFC-INT-005  | CMP-APP-01A    | CMP-APP-01C     | Authenticated, decoded V2X objects             | Internal memory (QM/ASIL boundary) | Per-message  |

## Failure Containment / Partitioning

### QM / ASIL B Boundary

The V2X architecture has a clear QM/ASIL split at the boundary between the protocol stack and the safety-relevant output formatter:

| Domain             | Components                                    | ASIL  | Rationale                                                    |
|--------------------|-----------------------------------------------|-------|--------------------------------------------------------------|
| Communication (QM) | CMP-PC5-01, CMP-UU-01, CMP-GNSS-01, CMP-APP-01A, CMP-APP-01B, CMP-APP-01D | QM    | Protocol processing, radio management, and certificate management have no direct safety impact. A V2X communication failure means loss of cooperative perception, not a hazardous condition (ego sensors remain available). |
| Security (QM)      | CMP-HSM-01                                    | QM    | Authentication is a cybersecurity function. Failure results in degraded trust mode, not a direct safety impact. |
| Safety Processing (ASIL B) | CMP-APP-01C                          | ASIL B | The plausibility checker and ADAS formatter are the last gate before V2X data influences safety-relevant ADAS decisions. A plausibility checking failure could allow false V2X data to affect ADAS behavior. |

**Boundary enforcement:**
- CMP-APP-01C runs in a protected memory partition with MPU-enforced isolation from the QM software.
- Data crossing the QM/ASIL B boundary (IFC-INT-005) undergoes input range validation, format checking, and rate limiting before entering the ASIL B partition.
- The ADAS output (IFC-EXT-001) includes E2E protection (CRC + sequence counter) generated within the ASIL B partition.

### Degraded Trust Mode

When the HSM reports authentication failures or internal faults, the VCU transitions to MODE-003. In this mode:
- All received V2X data is tagged as "unverified" regardless of signature status.
- The ADAS fusion ECU receives V2X objects with a trust level that causes the fusion algorithm to heavily discount V2X data.
- The VCU ceases transmission (cannot sign outgoing messages without HSM).
- A driver warning is issued via the instrument cluster.

This degradation strategy ensures that loss of V2X security does not silently corrupt the ADAS perception pipeline.

## Architecture Decisions

### AD-01: QM Protocol Stack with ASIL B Output Gate

**Decision:** Implement the V2X protocol stack (encoding, decoding, radio management) at QM and place a dedicated ASIL B plausibility checker and output formatter as the gateway to the ADAS domain.

**Rationale:** The V2X protocol stack is complex (ETSI ITS-G5 + SAE J3161 + C-V2X PHY/MAC), third-party supplied, and frequently updated. Developing the entire stack to ASIL B would be prohibitively expensive and would impede protocol evolution. Instead, a thin ASIL B layer at the output validates the QM stack's output using plausibility checking, confidence scoring, and E2E protection. This follows the ISO 26262 principle of placing the safety mechanism at the boundary rather than certifying the entire element.

**Trade-off:** The ASIL B layer cannot catch all QM stack errors (e.g., systematic message misparse). Mitigated by plausibility checking against ego sensor context, which detects physically implausible V2X data regardless of cause. Accepted because the alternative (ASIL B protocol stack) is impractical for a rapidly evolving communication standard.

### AD-02: Dedicated HSM over Software-Based Cryptography

**Decision:** Use a dedicated hardware security module (CMP-HSM-01) for all V2X cryptographic operations rather than software-based crypto on the application processor.

**Rationale:** V2X message authentication requires ECDSA P-256 signature verification at a sustained rate of 1,000+ messages/second. A dedicated HSM achieves this throughput within the 5 ms per-message latency budget while providing tamper-resistant key storage, secure boot, and hardware-enforced key isolation. Software-based crypto on the application processor would either exceed the latency budget or require a significantly more powerful (and expensive) processor.

**Trade-off:** HSM adds BOM cost and is a potential single point of failure for authentication. Mitigated by the degraded trust mode (MODE-003) which gracefully handles HSM failure. Accepted because the throughput and security requirements cannot be met by software crypto at the target cost point.

### AD-03: Dual-Mode PC5/Uu Architecture over PC5-Only

**Decision:** Support both PC5 (direct) and Uu (cellular) V2X communication modes.

**Rationale:** PC5 provides low-latency direct communication essential for safety-critical use cases (intersection collision warning, emergency vehicle preemption) but requires nearby V2X-equipped participants. Uu provides wide-area coverage via cellular infrastructure, enabling traffic information, cloud-based cooperative perception, and V2X communication in areas without PC5 coverage. Dual-mode maximizes the value of the V2X investment across deployment phases, from early adoption (sparse PC5 penetration, Uu supplements) to full deployment (dense PC5, Uu for extended services).

**Trade-off:** Dual-mode increases hardware cost (two radio modules), software complexity (mode management, duplicate message suppression), and power consumption. Accepted because single-mode deployment risks are high given uncertain regional PC5 vs Uu adoption timelines.
