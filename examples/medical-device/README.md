# Medical Device Examples

Reference systems demonstrating medical device systems engineering artifacts for Class II/III and SaMD programs. The flagship infusion pump example includes ISO 14971 risk management (hazardous situation to harm chain), FDA design control mapping, EU MDR technical documentation structure, and IEC 62304 evidence by safety class — all cross-referenced through a shared ID taxonomy.

| System | Tier | Key Standards | Artifacts |
|:-------|:-----|:--------------|:----------|
| [Smart Infusion Pump](smart-infusion-pump/) | Flagship | IEC 62304, ISO 14971, FDA QMSR, EU MDR | Full: README, requirements, architecture, hazard analysis, traceability, assurance evidence |
| [Surgical Robot Platform](surgical-robot-platform/) | Fleet | IEC 62304, IEC 80601-2-77 | Core: README, requirements, architecture |
| [Continuous Glucose Monitor](continuous-glucose-monitor/) | Fleet | IEC 62304, IMDRF SaMD N41 | Core: README, requirements, architecture |
| [Patient Monitoring Network](patient-monitoring-network/) | Fleet | IEC 62304, IEC 60601-1-8 | Core: README, requirements, architecture |

## What These Examples Demonstrate

- **Infusion pump flagship**: ISO 14971 full risk management (estimation, evaluation, risk-benefit, overall residual risk), DERS alert fatigue as design challenge, SOUP risk management, FDA design controls waterfall, EU MDR Annex II/III, IEC 62304 Class C evidence, post-market surveillance
- **Surgical robot**: Master-slave teleoperation boundary, haptic latency requirements, De Novo pathway, IEC 80601-2-77
- **CGM**: SaMD classification per IMDRF N41, three-software-item boundary (sensor/app/cloud), IEC 62304 Class B/A split
- **Patient monitoring**: IEC 60601-1-8 alarm management, alarm fatigue reduction, IEC 80001-1 network risk, bedside-first alarm independence
