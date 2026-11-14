# HG-05 connected review task

All IDs in this bundle are newly assigned teaching IDs. The source facts are
attributed historical findings; the interfaces and claims are teaching
reconstructions. The change request is synthetic and was never proposed to the
original program. No test in this bundle has been executed.

Read [source facts](source-facts.csv), [interfaces](interfaces.csv),
[claim/evidence register](claim-evidence.csv), and [change request](change.json)
together. Use the [case sources and locators](README.md#sources-and-access) to
challenge an assertion. The [relation view](relations.mmd) is an editable
information-flow aid, not a formal SysML model.

## Decision to produce

Write a disposition of HG-05-CH1 with a claim-by-claim evidence status.
Revise HG-05-I1 to state how version and unit semantics are recognized, what
happens to unknown inputs, and who owns the acceptance sample. Identify which
existing files can support testing and which require provenance recovery.

Produce an acceptance matrix with at least a valid sample, an unrecognized
unit, a missing unit, and a disagreement between metadata and an independently
known quantity. State the oracle, expected disposition, and evidence still
needed. Do not mark any row passed.

End with a short status message to an integration lead: decision, reason,
remaining gap, owner, and the next review trigger.

Review your result using the [review guide](review-guide.md). The guide is public
formative material; this task is not a hidden performance benchmark.
