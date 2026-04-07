# Tactical SDR Radio

## Overview

The Tactical Software-Defined Radio (SDR) is a multi-channel, multi-waveform radio platform for Joint Tactical Radio System (JTRS) waveform hosting in dismounted, vehicular, and airborne configurations. The radio conforms to the Software Communications Architecture (SCA) 4.1, providing a standardized waveform deployment environment that separates waveform application software from platform-specific hardware. The platform supports simultaneous operation of up to four waveform channels across HF, VHF, UHF, and L-band frequencies, with mobile ad-hoc networking (MANET) capability for infrastructure-free tactical communications. COMSEC and TRANSEC functions are provided by an embedded NSA Type 1 cryptographic module, with the crypto boundary separating red (plaintext) from black (ciphertext) domains. The FACE 3.1 transport and platform profiles govern software portability for the host platform services.

## System Boundary

**Inside the system boundary:**
- SDR Processing Platform (SCA 4.1 Core Framework, waveform execution environment)
- RF Transceiver Module (multi-band front end, digital IF processing)
- Cryptographic Module (NSA Type 1, COMSEC/TRANSEC, key management)
- FACE Platform Host (transport services, platform-specific services, OS abstraction)
- Waveform application software (SINCGARS, MUOS, SRW, ANW2 as mission-loadable)

**Outside the system boundary:**
- Antenna subsystem (broadband antenna, antenna tuning unit -- supplied by host platform)
- Host platform power and physical mounting (vehicle, manpack frame, or airborne rack)
- External key management infrastructure (KMI/SKL devices for key fill)
- Network management system (waveform planning and COMSEC net management)
- Connected C2/data terminals (laptops, mission systems consuming radio transport)

## Operational Environment

The radio operates in dismounted (manpack), vehicular (HMMWV/JLTV), and airborne (rotary-wing) configurations across -40C to +60C ambient temperature per MIL-STD-810H. Electromagnetic environment compliance per MIL-STD-461G. The system withstands tactical shock and vibration per MIL-STD-810H Method 514. TEMPEST requirements per NSTISSAM TEMPEST/1-92 apply to all processing and cryptographic equipment.

## Operating Modes

| Mode ID   | Name                   | Description                                                        | Active Functions                            | Constraints                                    |
|-----------|------------------------|--------------------------------------------------------------------|---------------------------------------------|------------------------------------------------|
| MODE-001  | Full Operational       | All waveform channels active with COMSEC enabled                   | All FUN- functions active                   | None                                           |
| MODE-002  | COMSEC Bypass          | Communications without encryption for interoperability or emergency | FUN-WFM-01, FUN-RF-01 active; FUN-CRY-01 bypassed | Plaintext transmission; requires operator authorization |
| MODE-003  | Crypto Zeroize         | Emergency destruction of all cryptographic key material            | FUN-CRY-03 active; all other functions suspended | Radio non-operational until rekeyed            |
| MODE-004  | Maintenance / Test     | Waveform loading, BIT, RF calibration, no operational transmission | FUN-BIT-01, FUN-DLD-01 active              | RF output inhibited                            |

Mode IDs are referenced by requirements.md.

## Key Technical Challenges

1. **SCA 4.1 real-time performance with waveform portability.** The SCA framework provides waveform portability across radio platforms but introduces middleware overhead that can impact real-time RF processing. Meeting waveform timing requirements (symbol rates, hopping sequences) while maintaining SCA conformance requires careful partitioning between the general-purpose waveform environment and hard-real-time DSP processing on the RF transceiver.

2. **COMSEC/TRANSEC boundary integrity.** The crypto boundary between red and black domains must be maintained through hardware enforcement, not software alone. All plaintext data paths must be physically or logically isolated from ciphertext paths, and the NSA Type 1 certification requires formal evidence of boundary integrity under all operating modes including fault conditions.

3. **Multi-channel spectrum management.** Simultaneous operation of four waveform channels across multiple frequency bands requires careful spectrum management to prevent self-interference. The RF front end must provide sufficient isolation between channels and handle dynamic frequency assignment without cross-channel spurious emissions.

4. **Waveform loading and trust.** Waveform software is mission-loadable from external media. The SCA framework must verify waveform integrity and authenticity before deployment to prevent compromised waveform code from accessing the crypto module or leaking key material.

## Stakeholders

| Stakeholder                        | Role                                                            |
|------------------------------------|-----------------------------------------------------------------|
| Tactical radio operator            | Operates radio, manages waveforms, performs COMSEC functions    |
| Signal/communications officer      | Plans waveform assignments, manages crypto nets                 |
| NSA / COMSEC custodian             | Certifies crypto implementation; manages key material           |
| PEO C3T                            | Acquisition oversight for tactical radio programs               |
| Waveform developers                | Develop and port waveform software to the SCA platform          |
| Host platform integrator           | Integrates radio into vehicle, manpack, or airborne platform    |

## Standards Applicability

| Standard        | Applicability                                                                             |
|-----------------|-------------------------------------------------------------------------------------------|
| SCA 4.1         | Software Communications Architecture; waveform portability and radio platform framework   |
| FACE 3.1        | Software architecture; transport and platform profiles for host services                  |
| MIL-STD-882E    | System safety; COMSEC zeroization, RF safety, battery/power hazards                       |
| NSA CNSS / CNSSP 11 | Cryptographic security policy for Type 1 devices                                     |
| MIL-STD-461G    | EMI/EMC requirements for tactical radio equipment                                         |
| MIL-STD-810H    | Environmental requirements for tactical field deployment                                  |
