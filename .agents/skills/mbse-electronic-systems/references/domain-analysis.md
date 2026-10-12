# Electronic-systems analysis and review

This reference preserves hardware engineering topics and review criteria. Exact obligations depend on the adopted DO-254, IEC 61508, ISO 26262 or other basis, toolchain, and technology. Consumer, industrial, avionics, automotive, and quantum-control designs have different assurance contexts.

## Architecture and implementation

Establish functions, technology, timing, power/thermal limits, environment, lifetime, manufacturing/supply assumptions, and HW/SW responsibility. Compare ASIC, FPGA, SoC, processor, or mixed-signal options using feasibility, changeability, performance, assurance, and lifecycle cost. Include clock/reset, power domains, startup, failure behavior, diagnostic and update paths.

Define register contracts with bit fields, reset values, read/write side effects, atomicity, privileges, invalid access, and versioning. Define interrupts, shared memory, DMA, endianness, time base, and timeout behavior. A block diagram cannot resolve a HW/SW race.

Inspect CDC/RDC protocols, synchronizers, reset release, asynchronous paths, constraints, and waivers. Ideal RTL simulation does not model all physical metastability risks. Timing closure should retain clocks, modes, corners, exceptions, unconstrained paths, and margin. Verify constraints against the actual design.

Track implementation transformations: RTL/model, synthesis, netlist, placement/routing, bitstream or silicon, board, and delivered configuration. Address equivalence, timing, initialization, manufacturing variation, errata, radiation where relevant, and obsolescence. A qualified tool name or clean simulation does not establish delivered hardware behavior.

## Verification and formal analysis

Derive verification objectives from requirements. Use simulation, UVM/other test environments, static checks, formal property analysis, equivalence, timing analysis, emulation, and target testing where each establishes the claim. Keep requirement, functional, structural, and property coverage distinct. Complete RTL line coverage does not mean complete requirement verification.

For a formal result, identify property IDs and associated requirements, assumptions, reset/model scope, bounds, vacuity checks, tool/version, and outcomes. A bounded proof does not establish an unbounded property; an overconstrained environment can exclude the intended failure. A counterexample is useful evidence, not a reason to silently weaken the property.

These are generic engineering practices, not methods attributed to Cole's unsupplied chapter notes. Include course methods only with the actual material and provenance.

For coverage-driven simulation, define stimulus and bins from intended behavior, boundaries, and failure conditions. Retain seeds and configuration for reproducibility. Evaluate exclusions and unreachable bins with rationale; do not confuse an arbitrary percentage with an assurance objective.

## Application assurance

For airborne hardware, align evidence with the hardware development and verification basis and accepted tool-assessment approach. Do not automatically apply software DO-330 criteria or MC/DC requirements to DO-254 hardware. FAA hardware guidance and the program's PHAC determine the accepted approach; name the credit and independent checks for each transformation.

For industrial/automotive safety, connect failure modes and diagnostic mechanisms to application hazards and adopted metrics. Keep circuit/application context, failure-rate sources, diagnostic coverage evidence, dependent failures, and assumptions. Do not manufacture SFF, PMHF, or systematic capability conclusions from a generic block table.

For quantum-control electronics, address waveform/sample fidelity, timing and synchronization, calibration, drift, noise, crosstalk, cryogenic/room-temperature interfaces, and configuration of the control chain. Quantum performance claims need experimental conditions and data. Digital-controller verification does not prove quantum-system fidelity.

## Artifact mappings and review

| Engineering thread | Proposed model content | Evidence focus |
| --- | --- | --- |
| HW requirement | Function/component allocation | Requirements-based verification |
| HW/SW boundary | Register, interrupt, timing contract | Integration and error behavior |
| Clock/power/reset | Domain and transition relationships | Constraints, CDC/RDC, startup |
| Formal claim | Property-to-requirement relationship | Scope, assumptions, vacuity, outcomes |
| Implementation chain | Controlled configurations/transforms | Equivalence and target applicability |
| Supplier part | Configuration, errata, lifecycle dependency | Application-specific assessment |

Capella/SysML carry system relationships; HDL and EDA tools remain detailed design and analysis sources. Link them rather than duplicating unmaintainable content. Confirm profile/version, extraction, and reconciliation for controlled exports.

Review pressure points: line coverage used as completeness proof; hidden unconstrained paths; unsupported diagnostic percentages; unassessed errata; missing register semantics; overconstrained formal models; obsolete implementation evidence; ignored manufacturing/thermal environment; software qualification rules asserted for hardware without an adopted basis.
