# Architecture records

Function record: ID, required transformation, input/output, modes, allocated requirements, allocated components. Component record: ID, responsibility, interfaces, resource constraints, failure behavior. Interface record: source/target, item, direction, format, unit, rate, latency, validity, timeout, and ownership. Decision record: problem, alternatives, constraints, chosen option, evidence, consequences, and revisit condition.

For an independence claim, inspect both physical and logical dependencies: common supply, reset, clock, enclosure, cooling, communication, shared code, configuration, manufacturing, and maintenance. A second processor is evidence of duplication, not proof of independence.

Assess timing from the initiating event through sensing, scheduling, communication, action, and observable completion. Record budget assumptions and margins. An interface timeout and actuator delay can invalidate an otherwise plausible safety response.

Tool mappings are illustrative until verified in the project's tool/profile version. Preserve IDs, direction, and relation semantics in export/import and compare a round trip before adopting it as a controlled interchange.
