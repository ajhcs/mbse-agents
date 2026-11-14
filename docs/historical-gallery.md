# Historical systems engineering gallery

Use the [historical gallery](../examples/historical/README.md) to practice framing
problems, identifying interfaces, weighing alternatives, examining evidence,
managing change, and communicating decisions. The cases concern work before
2015; some official retrospective sources were published later.

Each case separates attributed historical facts from newly authored analysis and
a proposed teaching artifact. Its `HG-` identifiers belong to this gallery and
are not identifiers recovered from the original program. The gallery includes
successful delivery, resilient recovery, design proposals, and failures.

The [source register](sources-historical.md) gives publication dates, precise
locators, access observations, and limits. Linked original records remain with
their publishers. No full third-party reports are redistributed here.

Read a case's facts first, state the decision and information available, and
then work through the questions before looking at its reasoning signals. Those
signals support formative discussion; they are not a hidden benchmark answer
key or a claim of measured agent quality.

The [evaluation guidance](evaluation.md) governs behavioral performance claims.
Source inspection and local structural validation do not establish engineering
acceptance, historical counterfactual certainty, or physical validity.

## Work through a connected review

The deeper [Mars Climate Orbiter](../examples/historical/mars-climate-orbiter/review-task.md),
[Hubble](../examples/historical/hubble-optics/review-task.md), and
[Heathrow Terminal 5](../examples/historical/heathrow-terminal-5/review-task.md)
exercises each connect seven files. A source-fact register establishes the
historical basis. Interface and claim registers expose the new reconstruction.
A synthetic change request asks for a decision whose affected IDs resolve into
those registers. An editable relation view preserves the direction of the
information flow. The task and public review guide explain the work and the
reasoning to examine.

Produce a decision, its evidence basis, its conditions, and its reopening
trigger. Keep `source_supported`, `unsupported_extension`, and
`proposed_unexecuted` distinct. If you run a new experiment, create a separate
record of the implementation, inputs, oracle, outputs, and limitations; do not
rewrite the historical case as though that experiment occurred in the original
program.

## Add or revise a case

Use an accessible original project record, specification, investigation, or
audit when possible. An official retrospective or contemporaneous summary can
support a narrower case when its status and limits are explicit. An original
researcher's investigation is distinct from a government finding. Inspect the
actual relevant content before adding a claim; a search snippet alone does not
justify `relevant_content_inspected`.

The canonical file is `examples/historical/<slug>/analysis.json`. Keep the
following contracts:

- `year` is the historical event or design-baseline year, before 2015.
  `publication_date` belongs to the source and may be later.
- `HG-nn`, `-S`, `-F`, and `-A` identify the teaching case, sources, facts, and
  proposed artifact. Deeper exercises use `-I`, `-C`, and `-CH` for reconstructed
  interfaces, claims, and synthetic changes. Never imply these are original IDs.
- Every historical fact identifies a source and a precise locator. Preserve
  uncertainty, distinctions among testimony and findings, and corrections or
  addenda relevant to the claim.
- Each analysis states its boundary, interfaces, decision alternatives,
  recommendation, uncertainty, concrete artifact, questions, reasoning signals,
  transfer exercise, and limits. Evidence requests stay unexecuted.
- Record the exact URL, source type, publication information, access date, and
  limits. Do not bundle complete third-party reports, copy long passages, or
  infer permission to reuse their illustrations.
- Treat a historical failure as evidence about the described context. Do not
  assume inevitability, assign unsupported motives, or claim that a proposed
  modern intervention would certainly have prevented it. Treat a success with
  the same care: separate delivery from eventual benefits and intended function
  from observed performance.

Generate the case pages, catalog, index, and source register with
`python3 examples/historical/render_gallery.py --write`. Validate them with
`python3 examples/historical/render_gallery.py --check` and
`python3 scripts/check_historical.py --check`. The checker performs no network
access. Its Python API is `check_gallery(repo_root: pathlib.Path) -> list[str]`.

## Scope of the collection

These cases were selected for inspectable evidence and contrasting reasoning
problems. They are not an exhaustive history, a random sample, or a calibrated
estimate of engineering performance. Most records expose a narrow project
slice. The gallery should grow through new source-grounded work, including
successful routine delivery and maintenance, as suitable original records are
available.
