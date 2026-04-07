# Aerospace Examples

Reference systems demonstrating aerospace systems engineering artifacts for civil aviation, space, and launch vehicle programs. The flagship FMS example includes a complete artifact set with ARP4761A hazard analysis, DO-178C/DO-254 certification evidence, and DO-326A cybersecurity — all cross-referenced through a shared ID taxonomy.

| System | Tier | Key Standards | Artifacts |
|:-------|:-----|:--------------|:----------|
| [Integrated Flight Management System](flight-management-system/) | Flagship | ARP4754A, DO-178C, DO-254, DO-326A | Full: README, requirements, architecture, hazard analysis, traceability, assurance evidence, cybersecurity |
| [CubeSat Constellation](cubesat-constellation/) | Fleet | NPR 7123.1, CCSDS | Core: README, requirements, architecture |
| [EVA Suit Life Support](eva-suit-life-support/) | Fleet | NPR 8705.2, NASA-STD-5005 | Core: README, requirements, architecture |
| [Launch Vehicle Avionics](launch-vehicle-avionics/) | Fleet | EWR 127-1, DO-178C | Core: README, requirements, architecture |

## What These Examples Demonstrate

- **FMS flagship**: FAA SOI progression, FHA/PSSA/SSA flow, DAL allocation across LRUs, DO-178C Table A objective mapping, dissimilar redundancy with ARINC 653 partitioning, DO-326A threat-to-hazard linking
- **CubeSat**: NASA Class C tailoring rationale, constellation vs spacecraft boundary, CCSDS protocol mapping
- **EVA suit**: Human-rating requirements, two-fault tolerance for life-critical functions, crew abort as operating mode
- **Launch vehicle**: FTS/GN&C DAL split rationale, range safety requirements, irreversible flight termination mode
