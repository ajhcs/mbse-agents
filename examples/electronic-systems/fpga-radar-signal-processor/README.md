# FPGA Radar Signal Processor

## Overview

The FPGA Radar Signal Processor (FRSP) is a real-time digital signal processing subsystem for an airborne phased array radar. The FRSP implements the complete signal processing chain from raw ADC samples through pulse compression, Doppler FFT, constant false alarm rate (CFAR) detection, and target report generation on a single Xilinx Versal ACAP device. The design operates across multiple clock domains (250 MHz ADC sampling clock, 400 MHz processing clock, 200 MHz MIL-STD-1553 bus clock) and processes 16 simultaneous receive channels at a pulse repetition frequency of up to 20 kHz. The FRSP is classified DO-254 DAL B with MIL-STD-882E safety analysis for unintended radar emissions and spurious radiation hazards.

## System Boundary

**Inside the system boundary:**
- Versal ACAP FPGA device and configuration logic
- ADC interface logic (16-channel, 14-bit, 250 MSPS per channel)
- Digital pulse compression engine (matched filter, sidelobe weighting)
- Doppler processing chain (range-gated FFT, clutter rejection)
- CFAR detection engine (cell-averaging and ordered-statistic CFAR)
- Target report formatter and track-before-detect preprocessor
- Clock domain crossing logic (ADC, processing, bus domains)
- Built-in test and diagnostic functions
- MIL-STD-1553 bus interface controller
- Bitstream configuration management and scrubbing logic

**Outside the system boundary:**
- Phased array antenna and RF front-end (T/R modules, beam steering controller)
- ADC modules (analog components; digital interface is inside boundary)
- Radar controller (waveform scheduling, beam management, mode sequencing)
- Track processor (multi-target tracking, data correlation)
- Aircraft mission computer and displays
- Power supply and cooling for the LRU chassis

## Operational Environment

The FRSP resides in a line-replaceable unit (LRU) within an airborne radar system, operating at altitudes from sea level to 50,000 ft, ambient temperatures from -55 C to +71 C (MIL-STD-810H Method 501.7/502.7), and vibration per MIL-STD-810H Method 514.8 Category 7 (jet aircraft). The FPGA junction temperature is maintained below 100 C by conduction cooling to the LRU cold wall. The device interfaces with 16 ADC channels via LVDS links, the radar controller via a dedicated SpaceWire link, the track processor via Ethernet, and the aircraft avionics bus via MIL-STD-1553B.

## Operating Modes

| Mode ID   | Name                     | Description                                                                | Active Functions                                              | Constraints                                              |
|-----------|--------------------------|----------------------------------------------------------------------------|---------------------------------------------------------------|----------------------------------------------------------|
| MODE-001  | Search                   | Long-range air search with wide beam scanning and Doppler filtering        | All FUN- functions active; CFAR threshold set for low PFA     | Full processing pipeline; all 16 channels active         |
| MODE-002  | Track                    | Dedicated beam dwell on tracked targets with fine range/Doppler resolution | FUN-PC-01, FUN-DOP-01, FUN-DET-01 at high update rate        | Reduced search coverage; higher PRF for velocity resolution |
| MODE-003  | Built-In Test            | FPGA self-test with loopback patterns and BIST on embedded memories        | FUN-BIT-01 active; no radar transmission or processing       | Antenna RF output inhibited; test patterns on ADC inputs |
| MODE-004  | Maintenance/Reprogram    | Bitstream reload, firmware update, diagnostic access                       | Configuration logic active; no signal processing              | LRU powered, aircraft on ground, maintenance crew access |

## Key Technical Challenges

1. **Multi-clock domain integrity.** The design crosses three clock domains (250 MHz ADC, 400 MHz processing, 200 MHz bus) with asynchronous boundaries. DO-254 requires formal analysis of all clock domain crossings (CDCs) to demonstrate that no metastability event can produce an undetected erroneous target report.

2. **Timing closure at DAL B.** DO-254 DAL B requires that the FPGA design meets timing under worst-case PVT (process, voltage, temperature) corners with demonstrated margin. The pulse compression engine operates at 400 MHz with deep pipelining; timing closure evidence must cover all P&R iterations and demonstrate reproducibility.

3. **CFAR threshold stability across environments.** The CFAR detection engine must maintain a constant false alarm rate across clutter conditions ranging from clear air to heavy ground clutter and weather. Adaptive thresholding must not mask real targets adjacent to strong clutter returns.

4. **SEU mitigation for mission-critical processing.** Single-event upsets in the FPGA configuration memory can silently corrupt the processing pipeline. Configuration scrubbing and output reasonableness checks must detect and recover from SEU-induced errors within one radar dwell.

## Stakeholders

| Stakeholder                  | Role                                                                     |
|------------------------------|--------------------------------------------------------------------------|
| Radar system engineer        | Defines processing requirements, waveforms, and detection thresholds     |
| FPGA design engineer         | Implements RTL, performs synthesis/P&R, generates bitstream               |
| DO-254 DER/designee          | Reviews DAL B planning, verification, and configuration management       |
| Safety engineer              | Performs MIL-STD-882E hazard analysis for radar radiation hazards         |
| Test engineer                | Executes hardware verification on target and in environmental test       |
| Aircraft integrator          | Integrates LRU into aircraft, validates MIL-STD-1553 bus interface       |

## Standards Applicability

| Standard       | Applicability                                                                                           |
|----------------|---------------------------------------------------------------------------------------------------------|
| DO-254         | Airborne electronic hardware design assurance; DAL B lifecycle from PHAC through verification           |
| MIL-STD-882E   | System safety: hazard analysis for unintended radar emission, spurious radiation, personnel exposure     |
| MIL-HDBK-217   | Reliability prediction for FPGA and LRU components; MTBF estimation                                    |
| MIL-STD-1553B  | Aircraft avionics data bus interface for target reports and radar commands                               |
| MIL-STD-810H   | Environmental engineering considerations for airborne LRU qualification                                 |
