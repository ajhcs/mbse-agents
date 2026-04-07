# Electronic Systems Examples

Reference systems demonstrating electronic systems engineering artifacts for safety-critical ASIC/FPGA/SoC and quantum computing hardware programs. The flagship quantum processor control example includes IEC 61508 SIL evidence mapping, FMEA/FMECA at component level, formal verification coverage metrics, and EDA tool qualification — all cross-referenced through a shared ID taxonomy.

| System | Tier | Key Standards | Artifacts |
|:-------|:-----|:--------------|:----------|
| [Quantum Processor Control](quantum-processor-control/) | Flagship | IEC 61508, IEEE 1076/1800 | Full: README, requirements, architecture, hazard analysis, traceability, assurance evidence |
| [Safety-Critical SoC](safety-critical-soc/) | Fleet | ISO 26262-11, AEC-Q100 | Core: README, requirements, architecture |
| [FPGA Radar Signal Processor](fpga-radar-signal-processor/) | Fleet | DO-254, MIL-STD-882E | Core: README, requirements, architecture |
| [HPC Cluster Orchestration](hpc-cluster-orchestration/) | Fleet | IEC 61508 | Core: README, requirements, architecture |

## What These Examples Demonstrate

- **Quantum processor flagship**: Cryogenic/room-temperature boundary as architectural driver, FMEA for RF pulse and flux bias control, IEC 61508 SIL 2 for safety-critical calibration, formal verification of control sequences, EDA tool qualification
- **Safety-critical SoC**: ISO 26262-11 semiconductor process, lockstep CPU architecture, ASIL D random HW fault metrics (SPFM/LFM/PMHF), AEC-Q100 qualification
- **FPGA radar**: DO-254 DAL B lifecycle, signal processing chain architecture, multi-clock domain crossing, SEU mitigation
- **HPC cluster**: IEC 61508 SIL 1 for regulated batch processes, ALCOA+ data integrity, checkpoint/restart fault recovery, hash-chain audit logging
