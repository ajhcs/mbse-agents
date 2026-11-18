---
name: mbse-electronic-systems
description: "Assess ASIC, FPGA, SoC, and control-electronics designs where physical limits, HW/SW interfaces, or verification affect system behavior."
---

# Electronic Systems Engineering

Explain how the proposed or observed hardware behavior follows from the real implementation and its HW/SW interfaces. Focus on the clock, reset, timing, analog, power, thermal, manufacturing, or service assumptions that could change the decision. Follow the consequence from the affected element to the system behavior.

Check assumptions across algorithm, RTL, synthesized or routed design, board, and deployed system as applicable. Match each verification method to the claim it can establish. Use [electronics analysis](references/domain-analysis.md) for interface contracts, timing and domain crossing, formal results, or application-specific assurance.

The result should let reviewers locate the affected requirements and interfaces, see which design revision and tool settings produced the evidence, and understand which physical or integration behavior still needs checking. Verify exact process obligations against the adopted edition and the actual application and tool use. Record open assumptions and derived constraints against the affected IDs.
