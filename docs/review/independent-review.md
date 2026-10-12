# Independent modernization review

Reviewed and repairs verified 2026-10-12 by a fresh repository-review agent. Repository: `mbse-agents-modernization`, branch `codex/modernize-mbse-skills`; base and HEAD at the initial review were `49e2379f858b05482d7ce1957d08d05ef9d41683`. This review includes the untracked implementation, not only `git diff`. The findings below preserve the initial defects and their verified resolutions. **All three findings are resolved; no material blocker remains in the reviewed scope.**

## Findings

### R1 — P2: Reconcile the corrected clamp with its safety argument and design decision

**Locations initially inspected:** `examples/medical-device/smart-infusion-pump/architecture.md:233`, `:235`, `:251`; related `hazard-analysis.md:78`, `:137`, `:158`.

The revised paragraph introduces a spring-closed clamp with a **powered hold-open actuator** and expressly says its dependencies, independence, and closure are unverified. The same architecture still describes it as entirely mechanical and AD-01 still chooses a passive clamp over an electronically actuated clamp, relying on inherent independence from power/software. CTL-006, its fault-tree discussion, and HZ-005 residual-risk rationale retain the corresponding blanket independence/elimination argument. The architecture also says usability testing confirmed acceptable loading times despite the new notice saying no executed tests are supplied.

This is a substantive disagreement within the safety baseline, not a wording preference. A reader cannot tell which mechanism the requirements, failure analysis, watchdog safe-state claim, and planned tests address. A file-wide illustrative notice does not resolve those conflicting premises or turn the specific test claim into evidence.

**Repair:** use one proposed mechanism throughout; carry its actual release/control dependencies into interfaces and failure analysis; make independence and residual-risk disposition conditional on planned evidence; replace the unsupported usability result with an open validation activity. Preserve CMP-PMA-01C, CTL-006, HZ-005 and requirement/test IDs.

**Status:** resolved on final verification. Architecture lines 233-238 and AD-01 lines 251-257 now consistently propose spring closure with powered hold-open/door interlock and identify the fault-analysis/test work required. REQ-SAF-001 at requirements line 280 states the proposed release behavior and open actuator/interlock coverage. CTL-006 and the fault-tree discussion identify unverified effectiveness/dependencies. Hazard-log and residual-summary rows now say Unassessed; the HZ-005 summary at hazard-analysis line 160 makes effectiveness/failure dependencies open, and line 163 replaces the all-risks-acceptable conclusion with an unresolved assessment. The unsupported usability result is removed. The matrix is expressly an unadopted teaching policy; no risk acceptance is recorded.

### R2 — P2: Keep evidence lifecycle meanings and repeated status mappings consistent

**Locations initially inspected:** `examples/medical-device/smart-infusion-pump/assurance-evidence.md:29`, `:33`, `:53`, `:71`, `:81`.

The former `Baselined` lifecycle row was changed to a second `Planned` row while retaining the meaning “under configuration control.” This makes `Planned` mean both an artifact not started and a controlled configuration. The revised evidence index marks all records Planned, but the FDA gate and EU design/manufacturing mappings still mark overlapping records Drafted. For example, EVD-015 through EVD-018 and EVD-020 are Planned in the index while their corresponding design-review/input/output rows remain Drafted. Their referenced PDF artifacts are absent.

These are incompatible evidence states in an example intended to teach truthful trace and evidence handling. Configuration control, existence of a draft, execution, review and acceptance are distinct facts.

**Repair:** restore distinct lifecycle definitions, retain a separate configuration-control state, and reconcile every repeated EVD status to actual supplied artifacts. Treat absent proposed PDFs as Planned.

**Status:** resolved on verification. Lifecycle definitions distinguish Planned, Drafted, Executed, Reviewed, Accepted and Baselined; the example explicitly says all indexed paths are absent, and FDA/EU/SOUP mappings consistently say Planned.

### R3 — P2: Narrow the source-cleanup claim or finish the cited-clause cleanup

**Locations:** `docs/sources.md:23`; `examples/medical-device/smart-infusion-pump/assurance-evidence.md`, EVD-020 (initially line 58; line 62 after concurrent edits), and the SOUP section (line 133 after concurrent edits).

The source ledger says unverified exact clause assertions were removed from the pump evidence index and discloses that no licensed IEC text was obtained. EVD-020 nevertheless retains `5.3.4; 7.1.3` after the new general applicability caveat, and the SOUP section still asserts evidence requirements “Per IEC 62304 Clauses 5.3.3, 5.3.4, and 7.1.3.” The software applicability table also presents precise clause/class obligations without an identified licensed edition.

This finding does **not** conclude that those clause numbers are wrong. It identifies an unsupported precision and a source-ledger claim that exceeds the cleanup actually performed. The narrower new references appropriately ask for the applicable edition; the teaching evidence file should do the same until its exact obligations are checked.

**Repair:** remove unverified exact obligations from this example or supply the applicable edition and verified locators; accurately describe the remaining review limits in the ledger. Keep the useful SOUP/configuration/anomaly/risk questions.

**Status:** resolved on verification. EVD-020's trailing clause numbers are removed; the precise clause/class table is replaced with a proposed work/evidence plan requiring the adopted licensed edition; the SOUP section now describes proposed application-specific records without asserting exact clauses.

## Checks and evidence

Used `C:\Users\colet\AppData\Local\Programs\Python\Python312\python.exe`; no model API, credentials, publication, live model mutation, or implementation edits were performed by this reviewer.

| Check | Observed result |
| --- | --- |
| Read root AGENTS.md, all 13 canonical SKILL.md entrypoints and their references | Task/domain substance, usable completion boundaries, uncertainty handling and portable local references present |
| Inventory, base diff and new-file inspection | Inspected modified legacy migration notices, canonical skills/catalog, scripts/tests, model/install/discovery docs, worked example, gallery correction, evaluation setup and contribution templates |
| `python scripts/validate.py` | PASS initially and after final repairs: packaging/discovery/local links, worked trace/configuration and six reference-model procedures; explicitly excludes comparative model quality and hardware acceptance |
| `python -m unittest discover -s tests -v` | Initially 18 tests passed; repair pass: all 21 tests passed, including new packet-preservation/separation and all-package portability cases |
| `python scripts/catalog.py` | Discovery files current |
| `git diff --check <base>` | Passed |
| Independent disposable installer fixture | All 13 packages installed; repeat was unchanged; AGENTS.md, CLAUDE.md and `.codex/config.toml` remained byte-identical; each entrypoint's local references existed; adding local package notes caused update refusal and preserved the notes |
| Independent `prepare_eval.prepare` fixtures, HO-04 and HO-08 | Exact request plus selected package files only; copied bytes matched sources. HO-04: 7 files/2 skills. HO-08: 1 request file/0 skills. No rubric, worked-answer or benchmark files included |
| Worked-example read and execution through validator/tests | Proposed requirements and design connect to executed sampled-model results with hashes, preserved IDs, and explicit open physical/human validation; README accurately calls the example hand-authored |
| Contribution forms and policy inspection | Bug, feature and new skill/agent requests accept an initial request without mandatory expertise, sources or implementation; illustrative-PR policy is consistent across domains |

Primary-source spot checks support the narrow corrections: [21 CFR 880.5725](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-880/subpart-F/section-880.5725), (a)-(b), supports the general infusion-pump Class II correction; [21 CFR 820.10](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/subpart-A/section-820.10), (a)-(c), supports the current ISO 13485/design-development basis. Both pages displayed Title 21 current to October 8, 2026. [MDCG 2021-24 Rev.1](https://health.ec.europa.eu/system/files/2021-10/mdcg_2021-24_en_0.pdf), April 2026, printed pages 47-48, supports the Rule 11/software versus Rule 12/administration distinction and potentially hazardous infusion-pump IIb example; it is nonbinding guidance and device-specific classification remains open. [FAA AC 20-115D](https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-115D.pdf), paragraphs 10 and Table 2, printed page 11, matches the proposed TQL table and its disclosed legacy-correlation limitation. The official DoDAF SV-5a page appeared in primary-domain search results, but direct retrieval returned 403; the ledger's retrieval limit is truthful.

## Assessment and remaining limits

The modernization substantially replaces persona prompts with portable, task-focused skills while retaining useful domain review questions and distinguishing requirements, proposed practice and evidence. Installation preservation and discovery consistency passed the observed checks. No P0/P1 defect was identified in the inspected scope. R1-R3 are repaired and verified; no material blocker remains in this review's scope.

Prepared packets provide file separation, not a secure held-out environment; public rubric files remain reachable from a full checkout. The documentation acknowledges this and recommends fresh variants after exposure. I did not read `evals/rubrics.json` or the concurrent producing agent's output. As a nonblocking evaluation-design limit, HO-08's prepared packet has no skills installed, so it cannot by itself measure whether a host with the full catalog avoids unnecessary implicit activation. A future discovery test should expose the catalog and observe activation.

The gallery review was sampled, with the corrected pump thread examined closely; it was not a clause-by-clause audit of all 20 retained baselines. Licensed standards, real supplier/configuration data, hardware behavior, stakeholder acceptance, and controlled Sol/Astra comparisons were not established. File existence, hash and link checks do not establish semantic adequacy. The separate skill-use exercise was outside this repository-review agent's work and has not been assessed here.

## Final small-delta verification

On 2026-10-12, independently inspected the added `prepare_eval.py --catalog` / `expose_catalog=True` option, its packet test, and the related evaluation documentation. The option selects all 13 catalog packages while copying only the same request and canonical package contents; it does not copy rubrics, worked answers or benchmark files. The default remains the case's selected packages. Existing-directory refusal and default HO-01 packet behavior remain covered.

Reran the full fast suite: **22 tests passed**, including the new full-catalog HO-08 packet-separation test. `scripts/validate.py` passed and the base diff check reported no whitespace error. The documentation accurately says full-catalog behavioral routing has not been run. This addresses the earlier tooling limitation without making a behavioral activation claim. No material finding was introduced by this delta; no broader repository rereview was performed. The HO-01 outputs were not changed, and their separate completed assessment is saved in `mbse-ho01-assessment.md`.
