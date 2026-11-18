---
name: mbse-operational-scenarios
description: "Trace an operational scenario from trigger to outcome through actor actions, system responses, exceptions, and recovery."
---

# Develop Operational Scenarios

Write the scenario so that a reviewer can walk it from the trigger and initial mode to an observable outcome. Identify who acts, what each actor knows at that point, what crosses the system boundary, and how the system responds. Keep the intended procedure and expected behavior under workload or degraded information visible wherever they differ.

Follow exceptions that could change the outcome or design, such as stale inputs, unavailable dependencies, handover, and interrupted work. Check decision authority, guards, deadlines, and what must be true before resuming. If a branch depends on an unknown operator decision or system response, locate that gap where it occurs.

Replay the paths that matter before handing them over. Each alternate path should rejoin at a valid state or end with a clear disposition. Retain source facts and IDs. Label observations that could become requirements or validation cases as candidates. Use [scenario records](references/scenario-records.md) for a scenario set, sequence diagram, or state model.
