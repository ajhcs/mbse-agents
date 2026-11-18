# Software tool qualification

Use this reference to review a specific civil aviation software tool use and the credit the program plans to claim. Use the hardware program basis for hardware tool assessment.

Tool qualification is decided by tool use, potential impact, credit claimed, and checks on outputs. DO-178C section 12.2 supplies the decision framework; DO-330 supplies qualification objectives and lifecycle data. Criterion 3 can fail to detect an error in its intended use; it does **not** mean an output with no effect or automatic exemption.

[FAA AC 20-115D](https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-115D.pdf), paragraph 10 and Table 2 (printed page 11), publishes the following correlation in its legacy-tool context:

| Software level | Criterion 1 | Criterion 2 | Criterion 3 |
| --- | --- | --- | --- |
| A | TQL-1 | TQL-4 | TQL-5 |
| B | TQL-2 | TQL-4 | TQL-5 |
| C | TQL-3 | TQL-5 | TQL-5 |
| D | TQL-4 | TQL-5 | TQL-5 |

For a new use, check the actual decision against the licensed DO-178C Table 12-1. A reviewer should be able to see which process is reduced or eliminated, which outputs are independently checked, and which errors could escape in this tool use. Cite the governing basis and identify what remains to be verified in the applicable licensed text.
