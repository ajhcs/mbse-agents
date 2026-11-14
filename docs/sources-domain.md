# Domain-model source checks

Checked 2026-11-13. These checks support methods and narrow corrections. They do
not validate the twenty designs, their parameter values or their complete
standards bases. Each example's `source-review.md` and `review-status.json` retain
individual candidate requirement sources and their unresolved applicability.

| Source | Edition and inspected locator | Supported use and limit |
| --- | --- | --- |
| [NASA Fault Tree Handbook with Aerospace Applications](https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/Fault%20Tree%20Handbook_NASA.pdf) | Version 1.1, August 2002; Chapter 7, printed pp. 81–84; Appendix A, pp. 158–161 | Boolean minimal cuts and quantitative interpretation. The supplied examples use exhaustive disjoint-state sums; no NASA parameter values are transplanted into the gallery. The handbook does not establish these authored events or independence assumptions. |
| [FAA AC 25.1309-1B](https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_25.1309-1B.pdf) | August 30, 2024; §§7.4 and 7.6, printed pp. 7-2 and 7-5–7-6; purpose on cover | The assessment considers common causes and exposure/flight context. A product of several per-hour rates is not itself a valid average probability per flight hour. The AC describes an acceptable means and does not by itself approve an aircraft design or make synthetic demand probabilities equivalent to a flight-hour objective. |

The MIL-STD-882E copy on the US Army site returned 502; the DAU risk-management
brief returned 403 on direct retrieval. Their search snippets were insufficient
for a current clause-level authority determination. The GCS now leaves authority,
delegation and numerical risk allocation tied to the actual program basis; it
does not assert the former unverified DASD(SE) chain or a universal 1e-6/FH target.

Licensed SAE, ISO, IEC and ARINC text was not supplied. Existing clause references
remain candidate citations in claim-level registers. Retained design targets,
including the steering example's 50 ms switchover, are proposed project values
until their source and applicability are established. They are not discarded to
make verification easier. New executable models test explicitly authored logic
and parameter hypotheses; physical and program evidence remains to be obtained.
