# HG-03-CH1 — fixture acceptance review

**Recommendation: do not close acceptance of HG-03-CH1.** Preserve the auxiliary discrepancy and obtain an independent dimensional check of the replacement fixture as assembled. The two computers share one generated geometry file. Their agreement therefore cannot establish that this common input represents the physical fixture correctly. Replacement alone does not eliminate an error carried through the retained calibration chain.

This is a retrospective metrology teaching exercise. HG-03-F1–F2 are attributed historical findings; the interfaces and claims are teaching reconstructions; the replacement fixture, computers, and disputed result belong to the synthetic change. No numerical uncertainty budget, raw result, released geometry, executed check, or approval is supplied. Proposed role assignments below require confirmation by the laboratory.

The inspected [NASA optical systems failure report](https://ntrs.nasa.gov/api/citations/19910003124/downloads/19910003124.pdf), executive summary, PDF pages 4–6, supports the finding of an incorrectly assembled reference and the lack of an independent dimensional verification after assembly. It also records auxiliary indications being discounted. That historical evidence motivates the review; it does not diagnose the fictional replacement fixture or prove that its auxiliary instrument is correct.

## Claims and interfaces

| Existing claim and status | Current disposition |
| --- | --- |
| HG-03-C1 — `source_supported` | Retain the report-scoped historical statement. The report was inspected; no historical raw optical data are available in the packet. |
| HG-03-C2 — `unsupported_extension` | Keep explicitly unsupported. Different computers do not remove the shared geometry-file dependency. Common source data, algorithms, configuration and calibration may create further dependence, but their details are unknown. |
| HG-03-C3 — `proposed_unexecuted` | Keep open. The replacement fixture's as-assembled dimensions have not been measured in the supplied evidence. Agreement between computer results cannot substitute for that measurement. |

HG-03-I1 connects physical assembly to the primary measurement; HG-03-I3 must connect the actual assembly to its calibration record and released definition. Those are two separate correspondences. HG-03-I4 must carry primary results with their reference and processing lineage, rather than an unexplained agreement statement. HG-03-I2 must preserve the auxiliary result and its unresolved disposition in the same acceptance record.

The proposed registers retain every original field. Added fields specify the evidence and ownership needed without treating a proposal as historical fact. `dependencies.proposed.mmd` retains the supplied relations and adds the two computers, common geometry file, physical references, unknown upstream dependencies, and proposed dimensional check. Solid arrows describe supplied/reconstructed relationships; dotted arrows denote unknown lineage or planned evidence, as labeled.

## Why agreement is weak accuracy evidence

If the geometry generator encodes an erroneous reference, both computers can calculate consistent answers from the same erroneous input. Their agreement then demonstrates consistency for that input, not accuracy against the assembled fixture. A correct calibration certificate also does not prove that the measured hardware, serial identity, assembly state, alignment, or environmental conditions match the certificate. Shared optical raw data, analysis code or transforms are additional possible dependencies requiring inspection, not established facts about this laboratory.

The auxiliary instrument's independence is also unestablished. Preserve its disagreement while recovering its reference, calibration, source data, processing and environmental history. The present evidence supports neither declaring the auxiliary instrument correct nor dismissing it as unreliable. Do not average inconsistent measurements or expand tolerances merely to make them agree.

## Select the discriminating check

Perform **HG-03-V01, an independent dimensional survey of the as-assembled replacement fixture**, before repeating the preferred instrument. Freeze and identify the assembly and current computer inputs first; recover the released definition, then measure relevant reference separations, orientations and alignment with a separately justified calibration and analysis path. Determine the required resolution and uncertainty from the applicable dimensional tolerances and optical sensitivity; neither is supplied. A metrology lead independent of the original geometry-file generation should review the method and data. Independence of people alone does not eliminate shared technical references.

`check-options.csv` compares this with a repeated measurement and a new physical measurement principle. The chosen check targets the missing physical-to-definition link directly. A repeat is useful for random variability or reproducibility but could reproduce the same systematic reference error. A different physical principle can later challenge the primary optical model if its reference, data and analysis chains are sufficiently distinct and its sensitivity is adequate.

Before execution, agree the measurands, configuration, environmental conditions, calibrated instruments, uncertainty model, decision rule, and reviewers. For a two-sided dimensional tolerance, a proposed conservative rule is that the relevant expanded measurement interval must lie within the specified tolerance interval. The coverage basis and treatment of correlated errors require review; overlapping a limit is inconclusive, not automatically acceptable. No numerical tolerance or confidence value is invented here.

A dimensional discrepancy that is resolved beyond the agreed uncertainty would support retaining the acceptance hold and correcting the assembly or reference chain. Dimensional consistency with adequate sensitivity would reduce concern about HG-03-C3 and shift the next investigation toward optical data, processing, and the auxiliary chain; it would not by itself explain the contradiction or close overall acceptance. An inconclusive or insufficiently sensitive result leaves C3 open. Closure could be reconsidered only after configuration-specific dimensional evidence, dependency review, and a defensible disposition of the auxiliary discrepancy are available.

## Acceptance statement and next review

HG-03-CH1 is **not accepted on the supplied evidence**. HG-03-C2 remains an unsupported independence assertion and HG-03-C3 remains unexecuted. The auxiliary disagreement remains an open evidence item under HG-03-I2. No physical measurement or acceptance test was conducted in this review.

The proposed metrology lead owns HG-03-V01 and its uncertainty basis; the fixture configuration custodian owns the released definition and as-assembled identity; the analysis owner owns geometry/source/software lineage for both computers; the auxiliary measurement owner owns the raw result and calibration history. The acceptance review chair owns the discrepancy disposition and final scope. Reopen when the frozen configuration, dimensional results and uncertainty, dependency inventory, and preserved primary/auxiliary data are available together. A new fixture, another matching computation, or the passage of a schedule milestone is not that trigger.
