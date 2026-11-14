---
name: mbse-architecture
description: "Reason about system behavior and structure, explain architectural choices, and develop or review functions, allocations, interfaces, and design trades."
---

# Design a System Architecture

Connect the required behavior to a workable system structure. Use the actual boundary, operating modes, requirements, and constraints. Decompose functions before treating a component list as a complete architecture. Consider alternative allocations or mechanisms when they affect performance, risk, maintainability, or feasibility.

Explain how interactions produce the desired behavior and where delays, feedback, contention, or mismatched assumptions could defeat it. Reason at both system and element levels: a locally adequate component can still participate in an inadequate system. Include people, operational procedures, and external organizations when they carry essential functions.

Define interfaces with direction, exchanged item, semantics, units, timing, validity, error handling, and responsibility as relevant. Make resource budgets and dependencies visible. Evaluate shared power, clocks, processors, data, suppliers, and human roles before claiming redundancy or isolation.

Deliver traceable function-to-component and requirement allocations, interface contracts, design decisions with rationale, and unresolved assumptions. Feed newly derived constraints back into requirements and risk analysis. Use the user's modeling tool when available; otherwise provide a clearly labeled textual or diagrammatic proposal without claiming a live model was changed.

Use [architecture records](references/architecture-records.md) for deeper allocation or trade work. Continue until the requested architecture is consistent enough for review, with gaps explicitly located.
