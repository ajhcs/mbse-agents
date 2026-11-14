# Reasoning situations

Use the questions that expose uncertainty in the current task. They are not an interview script or a required sequence.

| Situation | Useful reasoning | Reviewable result |
| --- | --- | --- |
| The request names a solution before the problem is understood | Recover the desired outcome, present failure or limitation, affected people, boundary, and real constraints; distinguish preference from necessity | A supported problem framing and alternatives that address it |
| Several stakeholders disagree | Locate the different objectives, operating situations, facts, definitions, and decision rights; identify which disagreement evidence can settle | Visible conflicts, feasible reconciliations, and decisions that still need an owner |
| A system behaves unexpectedly | Separate observation from interpretation; trace causal paths, modes, delays, resources, and dependencies; compare explanations against available observations | A bounded diagnosis, competing causes, and a discriminating next check |
| Specialist results disagree | Align configuration, units, timing, environment, uncertainty, abstraction, and assumptions before combining conclusions | A reconciled engineering argument or a precisely located incompatibility |
| A user asks for an explanation | Start from the behavior or decision they care about; identify the mechanism and demonstrate it with the smallest useful example | A clear explanation whose assumptions and limits are apparent |
| A change improves one measure | Trace effects through interfaces, workloads, lifecycle costs, risks, and evidence; inspect who receives the benefit and who inherits the burden | A recommendation based on the whole-system consequence |
| Evidence is incomplete | Separate what is known, inferred, proposed, and unresolved; choose the least costly observation that could change the decision | A provisional conclusion and an actionable uncertainty reduction step |

A causal sketch does not establish causation. Measurements can be biased by the observation method or configuration; a model may omit the behavior that matters. A failed prediction should lead to examining assumptions, competing explanations, and the model's scope, not quietly weakening the claim.

Use synthesis to connect evidence, not conceal disagreement. For example, if operations expects a person to recover an outage but the staffing concept provides no person at that time, the gap is a system responsibility decision. It cannot be resolved merely by assigning a software component a recovery function.

When explaining a recommendation, give the decisive premises, alternatives considered, and reason for the choice. State uncertainty in terms of its consequence: which conclusion depends on it and what information would reverse or strengthen that conclusion. Avoid invented confidence percentages.
