---
name: mbse-systems-engineering
description: "Diagnose system behavior and weigh cross-discipline tradeoffs when a decision spans several parts of a system or its lifecycle."
---

# Systems Engineering

Answer the decision the user can make with the system they have. Establish whose outcome matters, where the boundary lies, and under which conditions the answer holds. Read the available records before asking for input. Distinguish observations, stakeholder statements, and adopted obligations from assumptions and explanations. If a proposed solution addresses the wrong outcome, explain the mismatch using the user's constraints. Ask about uncertainties that could change the answer and carry independent work forward with named provisional assumptions.

Follow the mechanisms that could explain the observed behavior, including interactions among people, organizations, software, hardware, and the environment. For a quick explanation, a short scenario, calculation, or causal sketch may be enough. For a diagnosis, test competing explanations against the observations and identify a check that could distinguish the remaining ones. For a recommendation, compare credible alternatives and follow effects across interfaces and lifecycle stages until you can explain where each option moves workload, cost, delay, or risk.

Use [reasoning situations](references/reasoning-situations.md) when an observation or disagreement is hard to explain. For connected work, share one input revision, system boundary, terminology, and set of IDs. Use subagents as needed where the host and user permit delegation and the questions can advance independently. Give each a bounded question or owned artifact and ask for findings tied to the supplied sources. Reconcile modes, units, timing, and assumptions in the [integrated result](references/connected-work.md).

Finish when the user can follow the decisive facts, adopted constraints, inference, and uncertainties that could reverse the conclusion. On authorized baseline edits, check the actual updated artifacts for consistency, including affected interfaces, requirements, risks, and evidence applicability. Use [engineering records](references/engineering-records.md) when those decisions or links need to persist. Keep proposed actions, executed checks, and authorized acceptance independently traceable.

For operator handoffs with numeric go/hold gates, check source-derived branches against the exact delivered table, including each binding threshold and the fallback path. Use the operating gate replay in `mbse-verification-evidence` when available. Add a focused task or domain skill when it resolves a specific part of the work.
