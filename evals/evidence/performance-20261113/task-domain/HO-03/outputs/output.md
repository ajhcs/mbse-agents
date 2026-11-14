The colleague's two blanket statements are incorrect. Criterion 3 permits an error to escape detection; it does not mean “no effect” or exemption from qualification. A Criterion 1 tool used for Level B software maps to TQL-2, not TQL-1. The log processor's final criterion remains open because “removing manual checking” does not identify which process credit is claimed.

Qualification starts with the intended use: which required activity is automated, reduced or eliminated, whether tool error could introduce or conceal a software error, and which effective checks remain on its output. Independently verifying the relevant output can change the need for qualification; a nominal review or spot check is not evidence that all credited error-detection work remains covered. FAA identifies DO-178C section 12.2 and DO-330 as its acceptable qualification method. [FAA AC 20-115D, 21 July 2017, paragraph 10](https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-115D.pdf).

The decision boundaries are:

| Criterion | Impact/use boundary | Application to the proposed workflow |
| --- | --- | --- |
| 1 | Output becomes part of the airborne software and can introduce error. | A generated executable/configuration may qualify; producing a test report alone does not establish this boundary. |
| 2 | Verification automation can miss error, and its output justifies reducing/eliminating other verification processes or development processes affecting the airborne software. | Candidate if the report is used to waive additional testing, reviews or development work beyond the log-analysis activity it performs. |
| 3 | Within intended use, the tool can fail to detect error, without the Criterion 2 additional credit. | Candidate if it replaces only the manual evaluation of those test logs, while the other applicable processes remain. Qualification can still be needed. |

These distinctions are paraphrased from [NASA/CR–2017-219371, *Formal Methods Tool Qualification*, February 2017, section 3.3.1, printed p. 11, Table 2](https://shemesh.larc.nasa.gov/fm/FMinCert/NASA-CR-2017-219371.pdf). This is an accessible NASA-sponsored research report, not a substitute for the adopted standards or an authority decision.

| Software level | Criterion 1 | Criterion 2 | Criterion 3 |
| --- | --- | --- | --- |
| A | TQL-1 | TQL-4 | TQL-5 |
| B | TQL-2 | TQL-4 | TQL-5 |
| C | TQL-3 | TQL-5 | TQL-5 |
| D | TQL-4 | TQL-5 | TQL-5 |

The mapping is visible in [FAA AC 20-115D, Table 2, printed p. 11](https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-115D.pdf). Its context is correlation/transition of legacy DO-178B tools. For a new use, confirm the decision against DO-178C section 12.2 and Table 12-1, and the applicable DO-330 objectives. A generator's name does not prove Criterion 1 qualification is required: examine whether its generated output enters the airborne product, the credit claimed, and output verification. Conversely, an applicable Criterion 1 generator for Level A maps to TQL-1 and for Level B to TQL-2.

Before choosing between Level A TQL-4 and TQL-5 for this processor, obtain this minimum decision package:

1. **Credit ledger:** each existing manual check and associated objective; exactly what the tool automates; any additional activities to be removed; remaining reviewers/checkers and their detection scope. Show the before/after workflow, including raw-log retention.
2. **Use and configuration:** executable/version, parser and comparison rules, expected input formats, operating environment, configuration, users, interfaces, supported and excluded cases. Identify whether it only summarizes or also decides pass/fail, filters evidence, computes coverage, or creates loadable data.
3. **Failure/escape analysis:** missing/truncated/reordered logs, wrong test IDs or build, unit/rounding and timestamp errors, silently ignored failures, unexpected records, and a falsely successful report. For each, identify which independent check detects it and which software error could otherwise escape.
4. **Program basis:** authority, accepted software level and DO-178/DO-330 editions, legacy/new use, tool operational requirements, qualification plan/data and any supplier limitations. Qualification is tied to this use and configuration; possessing a tool certificate or another project's evidence is insufficient alone.

Proposed next step: retain the current manual checking while the project decides the credited workflow. If qualification is required, scope its objectives and operational requirements to that workflow and establish evidence for normal, malformed and error-containing logs, independently known expected results, configuration control and problem handling. Alternatively, retain adequate independent output verification and document what credit is no longer claimed. No tool execution, qualification result or authorization to remove checking is established here.

Sources were accessed 2026-11-13. Full licensed DO-178C and DO-330 texts were not available/read; no new licensed clause content is asserted. Six cases shared one participant context, so this assessment is not a separately isolated participant run.
