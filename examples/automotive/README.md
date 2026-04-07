# Automotive Examples

Reference systems demonstrating automotive systems engineering artifacts for ADAS and powertrain programs. The flagship AEB example includes a full ISO 26262 HARA with ASIL decomposition, ISO 21434 TARA, SOTIF triggering conditions, and AUTOSAR Classic/Adaptive architecture — all cross-referenced through a shared ID taxonomy.

| System | Tier | Key Standards | Artifacts |
|:-------|:-----|:--------------|:----------|
| [Autonomous Emergency Braking](autonomous-emergency-braking/) | Flagship | ISO 26262, ISO 21448, ISO 21434 | Full: README, requirements, architecture, hazard analysis, traceability, assurance evidence, cybersecurity |
| [EV Battery Management System](ev-battery-management/) | Fleet | ISO 26262, UN R100 | Core: README, requirements, architecture |
| [Steer-by-Wire](steer-by-wire/) | Fleet | ISO 26262, UN R79 | Core: README, requirements, architecture |
| [V2X Communication Unit](v2x-communication/) | Fleet | ISO 21434, SAE J3161 | Core: README, requirements, architecture |

## What These Examples Demonstrate

- **AEB flagship**: HARA with S/E/C classification, safety goals, ASIL decomposition (camera B(D) + radar B(D) = fusion D), AUTOSAR Adaptive/Classic split, ISO 21434 TARA with attack feasibility, SOTIF triggering conditions, GSN safety case structure
- **BMS**: 800V high-voltage boundary, ASIL C/D decomposition (monitoring vs actuation), thermal runaway prevention, UN R100 crash safety
- **Steer-by-wire**: Fail-operational without mechanical fallback, dual-channel freedom-from-interference, dissimilar silicon for common-cause mitigation
- **V2X**: QM/ASIL B boundary, V2X message authentication, SOTIF for cooperative perception, PC5/Uu dual-mode architecture
