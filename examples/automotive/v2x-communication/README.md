# V2X Communication Unit

## Overview

The V2X Communication Unit (VCU) is an on-board unit enabling vehicle-to-everything communication using C-V2X technology in both PC5 (direct short-range) and Uu (cellular network) modes. The unit receives and transmits Cooperative Awareness Messages (CAM), Decentralized Environmental Notification Messages (DENM), and Collective Perception Messages (CPM), providing the ADAS fusion ECU with cooperative perception data that extends sensor coverage beyond line-of-sight. The VCU manages V2X message authentication through an integrated Hardware Security Module (HSM) and IEEE 1609.2 / ETSI TS 103 097 public-key infrastructure. Because V2X data informs safety-relevant ADAS decisions, the safety-relevant message processing path is classified ASIL B while the communication protocol stack operates at QM.

## System Boundary

**Inside the system boundary:**
- C-V2X PC5 radio module (sidelink direct communication, 5.9 GHz ITS band)
- C-V2X Uu cellular modem (LTE-V2X / 5G NR-V2X network communication)
- GNSS receiver with dead-reckoning augmentation
- Hardware Security Module (HSM) for V2X PKI and certificate management
- VCU application processor (message encoding/decoding, plausibility checking, fusion formatting)
- VCU application software (ITS-G5 stack, SAE J3161 facilities layer, security credential management)

**Outside the system boundary:**
- ADAS fusion ECU (consumes V2X object data; VCU delivers formatted messages)
- Vehicle CAN gateway (bridges VCU data to the vehicle network)
- V2X PKI backend (provides certificates; VCU manages local credential store)
- Cellular network infrastructure (provides Uu connectivity; VCU is a subscriber)
- Roadside units (RSU) and other vehicles (external V2X participants)
- Vehicle dynamics sensors (ego vehicle speed, heading consumed from CAN for message generation)

## Operational Environment

The VCU operates in passenger vehicles on public roads within C-V2X deployment regions. PC5 direct communication range is 300--1000 m depending on terrain and obstruction. Uu communication depends on cellular coverage. The operating temperature range is -40C to +85C. The VCU interfaces with the ADAS domain via CAN FD and with the vehicle gateway via CAN. GNSS antenna is roof-mounted. The PC5 and Uu antennas are integrated into the vehicle shark-fin antenna module.

## Operating Modes

| Mode ID   | Name                    | Description                                                              | Active Functions                                                | Constraints                                                |
|-----------|-------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------|------------------------------------------------------------|
| MODE-001  | Full V2X                | PC5 and Uu active; transmitting and receiving; GNSS locked               | All FUN- functions active                                      | None                                                       |
| MODE-002  | PC5-Only                | Cellular modem unavailable; direct V2X communication only                | PC5 Tx/Rx, GNSS, message authentication; no Uu services       | No cloud-based traffic information; local awareness only   |
| MODE-003  | Degraded Trust          | Certificate validation failure or HSM fault; messages received but untrusted | Receive-only with plausibility filtering; no authenticated Tx  | ADAS fusion discounts V2X data confidence; driver warning  |
| MODE-004  | Silent Listening        | Transmitter inhibited (e.g., privacy zone, regulatory restriction)       | Receive and process only; no transmission                      | No cooperative awareness broadcast; ego vehicle invisible to V2X peers |

## Key Technical Challenges

1. **SOTIF for cooperative perception.** V2X messages from other vehicles or RSUs may be delayed, incorrect, or spoofed. The ADAS system must not make hazardous decisions based on false V2X data. The VCU must perform plausibility checking against ego sensor data and provide confidence metrics to the ADAS fusion ECU, per ISO 21448 SOTIF analysis.

2. **QM vs ASIL B integrity split.** The C-V2X protocol stack (encoding, decoding, radio management) is QM, but the path from decoded message to ADAS safety decision must meet ASIL B. This requires a well-defined QM/ASIL boundary with input validation, plausibility checks, and E2E protection on the safety-relevant data path.

3. **V2X PKI and certificate management.** Real-time message authentication requires sub-10 ms signature verification per received message. The HSM must support high-throughput ECDSA verification while managing certificate lifecycle (enrollment, pseudonym rotation, revocation list updates) without interrupting message processing.

4. **Dual-mode PC5/Uu coexistence.** The VCU must seamlessly switch between PC5 direct and Uu network modes depending on coverage, congestion, and application requirements, without message loss or duplication during mode transitions.

## Stakeholders

| Stakeholder                    | Role                                                                            |
|--------------------------------|---------------------------------------------------------------------------------|
| Vehicle driver                 | Indirect beneficiary of extended perception via V2X; receives V2X-based warnings |
| Vehicle OEM integration team   | Integrates VCU with ADAS and vehicle network; manages V2X safety argument      |
| Tier-1 V2X supplier            | Designs and delivers VCU hardware and protocol stack                           |
| ADAS integration team          | Consumes V2X cooperative perception data in sensor fusion                       |
| V2X PKI authority              | Issues and manages V2X security credentials; defines trust policies            |
| Regulatory authority           | Defines V2X spectrum allocation, message sets, and deployment mandates         |

## Standards Applicability

| Standard       | Applicability                                                                                     |
|----------------|---------------------------------------------------------------------------------------------------|
| ISO 21434      | Cybersecurity engineering; TARA for V2X communication interfaces and PKI                         |
| ISO 21448      | SOTIF for cooperative perception; addresses delayed, incorrect, or spoofed V2X data              |
| ETSI ITS-G5    | European ITS communication profile; message formats (CAM, DENM, CPM)                            |
| SAE J3161      | V2X communication for safety applications; BSM and cooperative perception                        |
| IEEE 802.11p   | WAVE/DSRC physical layer (legacy interoperability; C-V2X PC5 is primary)                         |
| ISO 26262      | Functional safety for ASIL B message processing path; QM for protocol stack                      |
