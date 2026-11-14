# Architecture records

Function record: ID, required transformation, input/output, modes, allocated requirements, allocated components. Component record: ID, responsibility, interfaces, resource constraints, failure behavior. Interface record: source/target, item, direction, format, unit, rate, latency, validity, timeout, and ownership. Decision record: problem, alternatives, constraints, chosen option, evidence, consequences, and revisit condition.

An allocation identifies responsibility, including human or organizational responsibility. A satisfaction relationship records a design claim against a requirement; it does not establish executed verification. State relationship direction and meaning in the project's chosen notation rather than relying on a generic trace arrow.

For an independence claim, inspect both physical and logical dependencies: common supply, reset, clock, enclosure, cooling, communication, shared code, configuration, manufacturing, and maintenance. A second processor is evidence of duplication, not proof of independence.

Assess timing from the initiating event through sensing, scheduling, communication, action, and observable completion. Record budget assumptions and margins. An interface timeout and actuator delay can invalidate an otherwise plausible safety response.

Tool mappings are illustrative until verified in the project's tool/profile version. Preserve IDs, direction, and relation semantics in export/import and compare a round trip before adopting it as a controlled interchange.

A general risk/control record can connect affected outcome, failure or threat, causal mechanism, operating condition, consequence, proposed control, responsible element, effectiveness evidence, introduced risks, and unresolved disposition. Keep proposed, implemented, verified, and accepted facts distinct. Use the adopted risk process when one applies; otherwise describe consequence and uncertainty without inventing a scoring scale or acceptance authority.
