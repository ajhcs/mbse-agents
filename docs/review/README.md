# Review history and reproduction

Start with the [release qualification](../release-report.md) and
[observed task evidence](../../evals/evidence/README.md) for the current candidate.
The retained reviews below identify their original scope and dates.

[Independent repository review](independent-review.md) found three material
consistency issues in the pump example, which were repaired and verified.
The review covers skills, installation, discovery, docs, source spot checks,
offline tests, packet separation, and the worked example. Gallery coverage was sampled.

[Fresh skill-use assessment](../../evals/evidence/ho01/independent-assessment.md)
examines the completed greenhouse-controller artifacts. Its four criteria are met
for the draft, with hardware performance and final acceptance explicitly open.

These are dated reviews of the scope and source revisions named in each record.
They do not approve subsequent changes. The greenhouse exercise includes its
[trace and decisions](../../evals/evidence/ho01/outputs/04-trace-and-decisions.md)
and [document checks](../../evals/evidence/ho01/outputs/05-artifact-checks.md).

Use the [public documentation](../site/index.html) for installation, a first
result, task selection, galleries, benchmarks and support. The
[review packet](../preview.html) opens this history first. Both HTML entrypoints
bundle their selected documents, local reference files and images; a web server
is optional. Reviewer answer keys and superseded planning archives are deliberately
outside this bundle and remain in the source repository. Preserved skill-input
copies, superseded packet preparations and reviewer-key/rubric snapshots are also
excluded; actual responses, observed outcomes and independent assessments remain
available. Archived `.md.txt` assessments are presented as their raw text.

The optional documentation build uses the exact dependency in
`requirements-docs.txt`. In a disposable Python environment on the workspace:

```sh
python3 -m pip install -r requirements-docs.txt
python3 scripts/render_preview.py
python3 scripts/render_preview.py --check
python3 -m unittest discover -s tests -p test_preview.py
```

The generated `docs/site/build-manifest.json` records source hashes, a source
snapshot digest, renderer version and output hashes. The build is deterministic;
`--check` refuses missing or stale generated output without writing. The public
site directory also contains an editable SVG and graph ledger derived from the
cold-storage architecture's authored Mermaid source, including the technician
and all four interfaces. It is a logical presentation, not a formal SysML view
or evidence of hardware operation.

Ordinary printing includes the selected document. **Print whole packet** is an
explicit alternative. With JavaScript disabled, the documents remain readable
as one continuous packet.

Run the current repository checks and inspect CI for the proposed release;
historical local passes are not current release evidence. No controlled model
advantage, hardware acceptance, licensed-standards audit or use of unsupplied
course material is established by these documentation checks.
