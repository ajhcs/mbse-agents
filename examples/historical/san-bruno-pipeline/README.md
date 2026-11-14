# San Bruno: preserve the provenance of configuration data

**HG-21 · 2010 · energy · failure**

Digitizing a record does not validate the physical configuration it describes.

All `HG-` identifiers are new teaching identifiers. Historical facts below
are attributed to sources; the boundary, decisions, artifact, questions, and
transfer exercise are newly authored. No local historical simulation was performed.

## Source-grounded facts

- **HG-21-F1:** The pipeline GIS described the rupture segment as seamless pipe using information traced through a survey sheet to an accounting voucher with an erroneous material description. [HG-21-S1](https://www.ntsb.gov/investigations/AccidentReports/Reports/PAR1101.pdf); Section 1.7.2, pp. 26–27.
- **HG-21-F2:** Investigators found welded short pipe sections with defects and configuration details that were not reflected in the GIS. [HG-21-S1](https://www.ntsb.gov/investigations/AccidentReports/Reports/PAR1101.pdf); Section 1.7.2, p. 27; section 1.8.

## Retrospective systems analysis

**Boundary.** Physical asset, construction records, accounting records, survey sheets, GIS, integrity analysis, inspections, and operating decisions form the configuration-evidence chain.

**Interfaces to examine**

- Legacy record → digital model: transformation must preserve origin and confidence instead of laundering uncertainty.
- Model attribute → integrity decision: uncertain material identity changes which analyses are applicable.

**Decision.** What should happen when an important configuration field has weak provenance?

- Treat a populated database field as authoritative.
- Mark the uncertainty, bound its decision consequences, and seek suitable confirming evidence.

**Teaching recommendation.** Differentiate administrative records, engineering records, and observations of the installed asset.

**Uncertainty.** A missing record does not by itself prove a defect; it limits the claims that can be supported.

## HG-21-A1: Configuration provenance ledger

This proposed artifact is a compact starting point for review. Its evidence
requests are unexecuted; its rows are not recovered project requirements.

| Item | Proposed disposition | Evidence to seek |
| --- | --- | --- |
| Material identity | Retain source chain and conflicts | Engineering record or suitable physical confirmation |
| Asset segmentation | Represent actual changes in construction | Inspection and as-built reconciliation |
| Decision applicability | Flag analyses sensitive to uncertain fields | Conservative bounds and owned resolution plan |

## Practice engineering judgment

1. How can information become more convincing without becoming more accurate?
2. What should a digital twin display when material identity is unresolved?
3. Write an uncertainty statement that avoids both false assurance and unsupported failure claims.

**Reasoning signals for a formative review**

- Tracks the origin of each decision-critical attribute.
- Propagates uncertainty into analysis applicability.
- Separates absence of evidence from evidence of defect.

**Transfer exercise.** Synthetic: migrate a legacy asset registry into a digital model. Define three provenance classes and rules preventing unsupported promotion to verified.

**Limits.** No pipeline integrity calculation or operating recommendation is made. All new ledger IDs are instructional.

## Sources and access

- **HG-21-S1: [NTSB Pipeline Accident Report PAR-11/01](https://www.ntsb.gov/investigations/AccidentReports/Reports/PAR1101.pdf)**
  — 2011-08-30; original investigation.
  Locator: Section 1.7.2, printed pp. 25–28; section 1.8.
  Relevant content inspected 2026-11-13. Relevant sections inspected; this is not a reconstruction of every event or finding.

[Structured case record](analysis.json) · [Gallery](../README.md) · [Source register](../../../docs/sources-historical.md)
