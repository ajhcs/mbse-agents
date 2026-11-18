---
name: mbse-architecture
description: "Allocate system functions, define interfaces, and compare architectures against required behavior and constraints."
---

# Design a System Architecture

Show how the required behavior is realized within the system boundary. Allocate functions to responsible elements, including people and organizations that carry essential work. Compare credible allocations when their effects on feasibility, timing, risk, or support could change the choice. Trace the selected mechanism through a representative operating mode and the failure or recovery path that most challenges it.

Make the interface contract explicit where behavior depends on it. Check direction, exchanged item, semantics, units, timing, validity, fault response, and ownership against the assumptions on both sides. Trace resource and timing budgets end to end where margins matter and account for feedback or contention. Inspect shared supplies, clocks, software, communications, and human or supplier dependencies before claiming redundancy or isolation.

For model work, use the project's tool where available and verify the model semantics there. For a visual deliverable, use the supplied reference or a representative project view for notation, hierarchy, and layout. Render the editable source, inspect labels, boundaries, and relationship directions at the intended viewing size, and correct ambiguities. Exercise the controls the viewer will use when the deliverable is interactive. Label proposed views and report the checks actually run.

The result is ready when reviewers can trace the required behaviors to allocations, check the interfaces and budgets supporting the decision, and locate design assumptions and derived requirements or risks. Use [architecture records](references/architecture-records.md) for detailed trade, dependency, or interchange work.
