Record counts and schema checks are necessary migration checks, but cannot establish that the register describes the installed assets. The review should start with decisions the digital twin will influence and the consequences of a wrong attribute.

The request supplies the historical finding from NTSB/PAR-11/01, section 1.7.2: an incorrect material description propagated into the GIS, while physical investigation found different construction. I have not independently retrieved the report. The review below is a proposed transfer of that lesson, not a finding about this register.

Prioritize attributes that can change operating limits, inspection methods, repair choices, or isolation decisions. Depending on the assets and intended uses, these may include material/grade, seam or construction type, wall thickness, diameter, installation and modification dates, operating status, and location/topology. Asset identity and segment boundaries come first: excellent evidence about the wrong segment does not resolve the decision.

For each important attribute, preserve its original value, units, source document and locator, date, asset association, author or authority where known, transformation history, and uncertainty. Distinguish reported, inferred, directly observed, and unresolved values. A copied field is not independent corroboration. Retain conflicting values and their sources; do not silently replace an unknown with a default or select the newest record without assessing its basis.

Check the complete import for missing and duplicate IDs, keyed value reconciliation, joins and segment splits, units, transformation rules, null/default handling, relationships, and location plausibility. Preserve source snapshots and mapping versions. These checks address information transfer; separately reconcile decision-critical attributes against installation, maintenance, replacement, and suitable physical evidence.

Start with the following small, purposive inspection set. These are selection categories, not existing asset IDs or a statistically representative sample:

| Select one record or segment in each category | Main inspection question |
| --- | --- |
| High-consequence asset with an old, weakly sourced construction description | What supports the construction and limit used by the decision? |
| Asset with conflicting material or seam descriptions | Do both sources refer to the same physical item, and which evidence explains the conflict? |
| Asset recorded as modified or replaced | Does the register reflect the installed configuration and modification boundary? |
| Segment crossing an import join, split, or location boundary | Were attributes attached to the correct physical extent? |
| Routine asset with recent, well-supported records | Does a straightforward case preserve its evidence and values through the same transformation? |

For each selected item, reconcile documentary lineage first, then plan an authorized, technically suitable physical check where it can discriminate the disputed attribute. Specify the inspection's identification method, measurement limits, competent reviewer, and retained evidence. A visual check alone may not establish grade, thickness, or seam construction. No field inspection is authorized or claimed by this exercise.

Log discrepancies with affected decisions, owners, and resolution evidence. Expand review to records sharing the suspect source or transformation; do not infer the defect rate from this purposive set. Withhold unsupported decision outputs or use an explicitly justified interim basis until the responsible authority resolves them.

A clean import demonstrates that the tested transfer rules preserved and structured source information. It does not establish historical accuracy, present physical condition, fitness of every model calculation, or readiness for unrestricted operational decisions. Accept migration integrity and each intended use on separately stated evidence.
