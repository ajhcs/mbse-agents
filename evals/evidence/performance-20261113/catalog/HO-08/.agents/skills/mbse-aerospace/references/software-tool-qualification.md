# Software tool qualification

Use this reference for a civil-aviation software tool-credit question. It is not a hardware qualification process or a determination that a particular tool is qualified.

Tool qualification is decided by tool use, potential impact, credit claimed, and checks on outputs. DO-178C section 12.2 supplies the decision framework; DO-330 supplies qualification objectives and lifecycle data. Criterion 3 can fail to detect an error in its intended use; it does **not** mean an output with no effect or automatic exemption.

[FAA AC 20-115D](https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-115D.pdf), paragraph 10 and Table 2 (printed page 11), publishes the following correlation in its legacy-tool context:

| Software level | Criterion 1 | Criterion 2 | Criterion 3 |
| --- | --- | --- | --- |
| A | TQL-1 | TQL-4 | TQL-5 |
| B | TQL-2 | TQL-4 | TQL-5 |
| C | TQL-3 | TQL-5 | TQL-5 |
| D | TQL-4 | TQL-5 | TQL-5 |

Apply the licensed DO-178C Table 12-1 and actual qualification decision for a new use. A requirements repository, code generator, coverage analyzer, or equivalence checker is not assigned a criterion merely by its name. Explain which process is reduced or eliminated, how outputs are checked, and what faults could escape. Public FAA guidance does not verify every objective in the applicable licensed standards.
