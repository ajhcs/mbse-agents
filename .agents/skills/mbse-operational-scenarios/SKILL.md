---
name: mbse-operational-scenarios
description: "Explore or explain operational scenarios, then develop actor actions, system responses, modes, exchanges, exceptions, and recovery when a scenario artifact is needed."
---

# Develop Operational Scenarios

Develop the requested scenario or scenario set from a recognizable operational trigger and outcome. Define actors, context, preconditions, system mode, and boundary. Describe actor actions and observable system responses, including exchanged information, material, or energy where relevant.

Explore exceptions that matter to this use case: interrupted work, invalid input, unavailable dependencies, degraded resources, misuse, and recovery. Expose ambiguous authority, hidden timing constraints, and unsafe transitions. Choose scenario coverage based on operational consequence and variation; do not mechanically enumerate every combination.

Use the scenario to test understanding: what does each actor know, what can they observe, and why would they choose the next action? Distinguish the intended procedure from likely behavior under workload, missing information, or conflicting incentives. An unexplained transition is a question to resolve, not a reason to invent an actor decision.

Deliver coherent normal and exception flows, final conditions, assumptions, and observations that could become requirements or validation cases. Preserve source facts and IDs. Check that an alternative path actually rejoins a defined state or ends with a clear disposition.

Use [scenario records](references/scenario-records.md) for structured handoffs. These records describe operations; do not silently convert every action into a design requirement.
