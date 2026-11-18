# Architecture records

Select fields that let reviewers follow the behavior and test the tradeoff.

| Record | Useful fields |
| --- | --- |
| Function | ID, required transformation, inputs and outputs, modes, allocated requirements and elements |
| Component | ID, responsibility, interfaces, resource constraints, failure behavior |
| Interface | Source, target, exchange, direction, format, unit, rate, latency, validity, timeout, ownership |
| Decision | Problem, alternatives, constraints, selected option, evidence, consequences, condition for reopening |

An allocation identifies responsibility, including human or organizational responsibility. A satisfaction relationship records a design claim against a requirement; it does not establish executed verification. State relationship direction and meaning in the project's chosen notation rather than relying on a generic trace arrow.

For an independence claim, inspect both physical and logical dependencies: common supply, reset, clock, enclosure, cooling, communication, shared code, configuration, manufacturing, and maintenance. A second processor is evidence of duplication, not proof of independence.

Assess timing from the initiating event through sensing, scheduling, communication, action, and observable completion. Record budget assumptions and margins. An interface timeout and actuator delay can invalidate an otherwise plausible safety response.

For a controlled interchange, test a round trip using the project's actual tool and profile version. Compare the IDs, endpoints, directions, and relationship meanings after import. For a review diagram, trace a representative exchange in the rendered view and reconcile its labels and direction with the editable model.

A general risk/control record can connect affected outcome, failure or threat, causal mechanism, operating condition, consequence, proposed control, responsible element, effectiveness evidence, introduced risks, and unresolved disposition. Keep proposed, implemented, verified, and accepted facts distinct. Use the adopted risk process when one applies; otherwise describe consequence and uncertainty without inventing a scoring scale or acceptance authority.
