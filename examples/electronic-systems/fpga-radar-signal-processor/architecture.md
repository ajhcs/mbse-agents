# Architecture

## System Context

```mermaid
graph TB
    subgraph FRSP["FPGA Radar Signal Processor"]
        ADC_IF["CMP-ADC-01<br/>ADC Interface"]
        PC["CMP-PC-01<br/>Pulse Compression Engine"]
        DOP["CMP-DOP-01<br/>Doppler Processor"]
        DET["CMP-DET-01<br/>CFAR Detection Engine"]
        RPT["CMP-RPT-01<br/>Report Formatter"]
        BIT["CMP-BIT-01<br/>Built-In Test"]
        CFG["CMP-CFG-01<br/>Configuration & Scrub"]
        BUS["CMP-BUS-01<br/>MIL-STD-1553 Controller"]
    end

    ANT["Phased Array Antenna<br/>& RF Front-End"]
    CTRL["Radar Controller"]
    TRK["Track Processor"]
    MC["Aircraft Mission Computer"]
    PWR["LRU Power Supply"]

    ANT -->|16ch ADC samples (LVDS)| ADC_IF
    CTRL -->|Waveform params, beam cmds (SpaceWire)| RPT
    RPT -->|Target reports (Ethernet)| TRK
    BUS -->|Status, BIT (1553)| MC
    FRSP -->|RF Inhibit| CTRL
    PWR -->|DC power| FRSP
```

## Functional Architecture

| FUN ID       | Function Name                         | Description                                                              | Inputs                                       | Outputs                                     | Dependencies        |
|--------------|---------------------------------------|--------------------------------------------------------------------------|----------------------------------------------|---------------------------------------------|----------------------|
| FUN-ADC-01   | ADC Sample Acquisition                | Receive, deserialize, and time-align 16 LVDS ADC channels                | Raw LVDS bit streams                         | Time-aligned 14-bit sample vectors          | None                 |
| FUN-PC-01    | Pulse Compression                     | Apply programmable matched filter and sidelobe weighting to each channel | Time-aligned samples, filter coefficients    | Range-compressed data matrix                | FUN-ADC-01           |
| FUN-DOP-01   | Doppler Processing                    | Perform range-gated FFT across coherent processing interval              | Range-compressed data, CPI parameters        | Range-Doppler map                           | FUN-PC-01            |
| FUN-DET-01   | CFAR Detection                        | Apply adaptive threshold to range-Doppler map and declare detections     | Range-Doppler map, CFAR algorithm selection  | Detection list (range, Doppler, SNR)        | FUN-DOP-01           |
| FUN-RPT-01   | Target Report Generation              | Format detections into structured target reports with angles and quality  | Detection list, beam steering angles         | Target reports to track processor           | FUN-DET-01           |
| FUN-BIT-01   | Built-In Test                         | Execute loopback, BIST, and signal integrity checks                      | Test commands, loopback patterns             | BIT results, fault flags                    | None                 |
| FUN-CFG-01   | Configuration Scrubbing               | Continuously verify FPGA configuration memory CRC and repair SEU errors  | Configuration frame readback                 | Scrub status, SEU count, repair actions     | None                 |
| FUN-BUS-01   | Avionics Bus Communication            | Exchange status, commands, and BIT data with mission computer via 1553   | 1553 commands, BIT results                   | Status words, command responses             | None                 |

## Physical Architecture

### Component Hierarchy

| CMP ID        | Component Name                        | Type      | Parent   | Description                                                        |
|---------------|---------------------------------------|-----------|----------|--------------------------------------------------------------------|
| CMP-ADC-01    | ADC Interface Block                   | Hardware  | System   | 16-channel LVDS deserializer with sample alignment FIFO            |
| CMP-PC-01     | Pulse Compression Engine              | Hardware  | System   | Pipelined FIR matched filter bank operating at 400 MHz             |
| CMP-PC-01A    | Coefficient Memory                    | Hardware  | CMP-PC-01 | Dual-port BRAM storing programmable matched filter coefficients   |
| CMP-DOP-01    | Doppler Processor                     | Hardware  | System   | Range-gated 64/128/256-point FFT with windowing                   |
| CMP-DOP-01A   | FFT Core                              | Hardware  | CMP-DOP-01 | Radix-2/4 pipelined FFT with butterfly units                     |
| CMP-DOP-01B   | Clutter Rejection Filter              | Hardware  | CMP-DOP-01 | Doppler notch filter for mainbeam clutter suppression             |
| CMP-DET-01    | CFAR Detection Engine                 | Hardware  | System   | Cell-averaging and ordered-statistic CFAR with programmable guard/reference cells |
| CMP-RPT-01    | Report Formatter                      | Hardware  | System   | Target report packetizer with Ethernet MAC                        |
| CMP-BIT-01    | Built-In Test Controller              | Hardware  | System   | BIST sequencer, loopback multiplexers, and RF inhibit assertion   |
| CMP-CFG-01    | Configuration and Scrub Controller    | Hardware  | System   | FPGA configuration memory CRC monitor and partial reconfiguration controller |
| CMP-BUS-01    | MIL-STD-1553 Bus Controller          | Hardware  | System   | Dual-redundant 1553B remote terminal controller                   |

## Allocation

| FUN ID       | REQ ID(s)                                    | CMP ID(s)                          | Assurance Level | Rationale                                                    |
|--------------|----------------------------------------------|-------------------------------------|-----------------|--------------------------------------------------------------|
| FUN-ADC-01   | REQ-FUN-001                                  | CMP-ADC-01                          | DAL B           | Sample alignment errors propagate through entire processing chain |
| FUN-PC-01    | REQ-FUN-002, REQ-FUN-006                     | CMP-PC-01                           | DAL B           | Pulse compression fidelity affects detection performance      |
| FUN-DOP-01   | REQ-FUN-003, REQ-FUN-006                     | CMP-DOP-01                          | DAL B           | Doppler accuracy affects target velocity measurement         |
| FUN-DET-01   | REQ-FUN-004, REQ-FUN-006                     | CMP-DET-01                          | DAL B           | Detection threshold directly impacts safety (missed targets / false alarms) |
| FUN-RPT-01   | REQ-FUN-005, REQ-IFC-001                     | CMP-RPT-01                          | DAL B           | Report formatting and delivery timeliness affect track quality |
| FUN-BIT-01   | REQ-SAF-001                                  | CMP-BIT-01                          | DAL B           | BIT failure detection triggers RF inhibit safety function     |
| FUN-CFG-01   | REQ-SAF-002                                  | CMP-CFG-01                          | DAL B           | SEU detection and recovery preserves processing integrity     |
| FUN-BUS-01   | REQ-IFC-002                                  | CMP-BUS-01                          | DAL C           | Bus interface is not in the detection or RF control path      |

## Interfaces

### External Interfaces

| IFC ID       | Partner System                  | Data Item                                    | Direction     | Protocol              | Timing                    |
|--------------|---------------------------------|----------------------------------------------|---------------|-----------------------|---------------------------|
| IFC-EXT-001  | Phased Array Antenna (ADCs)     | 16-ch raw ADC samples (14-bit, 250 MSPS)     | In            | LVDS (serialized)     | Continuous at sample rate  |
| IFC-EXT-002  | Radar Controller                | Waveform parameters, beam steering commands   | In            | SpaceWire (200 Mbps)  | Per dwell (< 50 us)       |
| IFC-EXT-003  | Track Processor                 | Target detection reports                      | Out           | Ethernet (1 Gbps)     | Per dwell (< 2 ms)        |
| IFC-EXT-004  | Aircraft Mission Computer       | Radar status, BIT results                     | Bidirectional | MIL-STD-1553B         | 20 Hz status, async cmd   |
| IFC-EXT-005  | Radar Controller                | RF Inhibit assertion                          | Out           | Hardwired discrete    | < 10 us                   |
| IFC-EXT-006  | LRU Power Supply                | DC power rails (3.3V, 1.8V, 0.85V)           | In            | Electrical (DC)       | Continuous                 |

### Internal Interfaces

| IFC ID       | Source CMP ID  | Target CMP ID  | Data Item                                | Mechanism              | Timing               |
|--------------|----------------|-----------------|------------------------------------------|------------------------|----------------------|
| IFC-INT-001  | CMP-ADC-01     | CMP-PC-01       | Time-aligned sample vectors              | AXI-Stream (400 MHz)   | Continuous streaming |
| IFC-INT-002  | CMP-PC-01      | CMP-DOP-01      | Range-compressed data                    | AXI-Stream (400 MHz)   | Per PRI              |
| IFC-INT-003  | CMP-DOP-01     | CMP-DET-01      | Range-Doppler map cells                  | AXI-Stream (400 MHz)   | Per CPI              |
| IFC-INT-004  | CMP-DET-01     | CMP-RPT-01      | Detection list (range, Doppler, SNR)     | AXI-Stream             | Per dwell            |
| IFC-INT-005  | CMP-BIT-01     | CMP-RPT-01      | RF inhibit command                       | Register write         | < 10 us              |
| IFC-INT-006  | CMP-CFG-01     | CMP-BIT-01      | SEU error notification                   | Interrupt              | Per scrub cycle      |

## Failure Containment / Partitioning

### Clock Domain Isolation

The three clock domains (ADC 250 MHz, processing 400 MHz, bus 200 MHz) are isolated through dual-clock FIFOs at each boundary. Each FIFO is sized for worst-case rate mismatch and includes full/empty flags monitored by FUN-BIT-01. Formal CDC verification (REQ-SAF-003) ensures all asynchronous crossings use proper synchronization structures. A metastability event in one domain is contained by the FIFO and does not propagate to adjacent domains.

### Processing Pipeline Data Integrity

Each stage of the processing pipeline (CMP-ADC-01 through CMP-RPT-01) includes end-of-frame CRC checks. If any stage detects a CRC mismatch, the affected dwell data is tagged as invalid and excluded from the target report. This containment prevents a single processing error from producing a false target detection that could influence track processor behavior.

### RF Inhibit Independence

The RF inhibit output (IFC-EXT-005) is driven by dedicated logic in CMP-BIT-01 that operates on an independent clock and has a direct path to the output pin. The inhibit logic is not in the signal processing pipeline datapath, ensuring that a processing pipeline fault (stuck data, corrupted coefficients) cannot prevent the inhibit from being asserted. The inhibit defaults to asserted (active-low) on power-up and is released only after successful BIT completion.

## Architecture Decisions

### AD-01: Single FPGA over Multi-Chip DSP Architecture

**Decision:** Implement the entire signal processing chain on a single Xilinx Versal ACAP rather than distributing processing across multiple DSP chips or a multi-FPGA board.

**Rationale:** A single-device solution eliminates inter-chip communication latency and board-level signal integrity challenges for high-speed data paths. The Versal ACAP provides sufficient DSP resources (approximately 1,968 DSP58 slices) and AI Engine tiles for the 16-channel processing throughput. Single-device DO-254 configuration management is significantly simpler than managing multiple FPGA bitstreams with version dependencies.

**Trade-off:** Concentrating all processing in one device creates a single point of failure. Mitigated by continuous BIT (FUN-BIT-01) and SEU scrubbing (FUN-CFG-01) with rapid RF inhibit assertion on fault detection. The radar system provides graceful degradation at the system level when the FRSP is offline.

### AD-02: AXI-Stream Pipeline over Shared Memory Architecture

**Decision:** Connect processing stages via AXI-Stream point-to-point links with backpressure rather than a shared-memory architecture with DMA engines.

**Rationale:** Streaming architecture provides deterministic latency through the processing chain, which is critical for meeting the 50 us per-PRI processing budget (REQ-FUN-006). Shared-memory approaches introduce non-deterministic DMA arbitration latency and require more complex verification of memory access ordering. Streaming also enables pipelining where multiple PRIs are in-flight simultaneously across different processing stages.

**Trade-off:** Less flexibility for non-linear data access patterns (e.g., track-before-detect algorithms that need random access to range-Doppler history). Mitigated by providing dedicated BRAM buffers within CMP-DOP-01 for the Doppler history required by the clutter rejection filter.

### AD-03: Hardware RF Inhibit with Active-Low Default

**Decision:** Implement the RF inhibit output as an active-low signal with a pull-up resistor, such that the default state (FPGA unconfigured, BIT not passed) inhibits radar transmission.

**Rationale:** MIL-STD-882E requires that the system default to a safe state. If the FPGA fails to configure, loses power, or has a BIT failure, the RF inhibit remains asserted (low), preventing unintended radar emission. This fail-safe design ensures that no single FPGA fault can enable RF transmission without successful BIT completion.

**Trade-off:** Requires explicit de-assertion by the BIT controller after successful startup, adding approximately 500 ms to the radar warm-up time. Accepted because personnel safety from unintended radiation exposure takes priority over startup latency.
