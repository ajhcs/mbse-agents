# CR-1 change and review record

**Disposition:** the approved 200 ms change is incorporated into a proposed coherent document baseline. The implementation remains unselected and unverified. The automatic-recovery contradiction is corrected in the proposed architecture, and VER-8 is expanded to assess the unchanged obligation. Nothing in this record authorizes deployment or declares the controller compliant.

## Basis and scope

Inputs examined: `../inputs/change-request.md`, `source.md`, `requirements.md`, `architecture.md`, `verification.md` and `report-old.json`. These are fixture artifacts. The protected source and operator note, approved change and old report are copied unchanged into this output package. The original input tree remains authoritative for revision-A history and is not edited.

Review scope follows N-01 → REQ-7 → COMP-1/COMP-2/COMP-3 and IFC-1/IFC-2 → VER-7 → EVD-A-7, and N-02/operator note → REQ-8 → IFC-3/recovery state behavior → VER-8. No live model, hardware, instrument records, supplier data, complete pressure contract or runtime implementation was available. This is a participant's document revision and consistency review, not an independent acceptance review.

## Change inventory

| Artifact/entity | Disposition and reason |
| --- | --- |
| source.md; N-01,N-02; operator note | Byte-for-byte copy. No source rewrite or changed authority. |
| change-request.md; CR-1 | Byte-for-byte copy of approved change. |
| requirements.md; REQ-7 | Keep ID, source, trigger, end event and operating conditions; replace only statement's 500 ms with 200 ms. Status distinguishes criterion approval from implementation verification. Prior wording remains in inputs. |
| requirements.md; REQ-8 | Complete original table row preserved verbatim. No change or split approved or performed. Its implementation remains unverified. |
| architecture.md; COMP-1–COMP-3, IFC-1–IFC-3 | Preserve IDs/responsibilities and inherited allocations. Display their 260 ms total and unresolved deficit. Replace unsupported automatic recovery with explicit local-resume guard and latched visibility; identify missing motion/display bindings. |
| verification.md; VER-7 | Keep ID; revise criterion and develop the end-to-end plan for the selected B implementation. Mark evidence missing and A result inapplicable to a positive B claim. |
| verification.md; VER-8 | Keep ID; retain visibility intent and add stop release, restoration, explicit local resume and observable motion. This repairs a plan gap without changing REQ-8. |
| report-old.json; EVD-A-7 | Byte-for-byte copy. Retain configuration A, criterion 500 ms, observation 460 ms, recorded pass and historical-fixture scope. No relabeling as a B result. |
| evidence/revision-b-results.json | Remains absent; referenced as a planned artifact only. No fabricated placeholder result. |

## Findings and engineering dispositions

| Finding | Location/fact and consequence | Repair/status; proposed owner |
| --- | --- | --- |
| REV-01 — new timing not established | Inputs architecture path: 150 + 80 + 30 = 260 ms under explicit serial/nonoverlapping assumption. Budget exceeds new 200 ms by 60 ms before any omitted terms. | Unresolved engineering issue. Architecture lists bounded serial optimization, justified path redesign/overlap or component/partition changes. Select implementation and substantiate end-to-end bound. Performance/architecture lead. |
| REV-02 — old link does not establish reuse | CR-1 proposes reusing EVD-A-7 because REQ-7 ID persists. JSON explicitly names A and 500 ms; 460 ms would not satisfy comparable 200 ms. | Reuse-as-pass rejected. Preserve historical record; carry no positive timing result into B. Applicability and uncertainty/method gaps documented in verification.md. Verification lead. |
| REV-03 — recovery contradicts source | Inputs architecture's release-plus-data-return transition omits explicit local resume, contrary to N-02 and REQ-8. Could authorize motion after reconnect/shift change without deliberate action. | Documentation repaired with latch/explicit local guard and visible retained state. Implementation and motion/display bindings unresolved; verify with VER-8. Controls lead + operator representative. |
| REV-04 — VER-8 does not exercise its claim | Inputs verification checks fault-indicator visibility only, omitting stop release, restoration, resume and motion. | Plan repaired; no executed evidence yet. VER-8.a–h distinguish recovery conditions and observe motion. Test lead. |
| REV-05 — missing current result | Inputs verification explicitly says revision-B path does not exist; no B implementation or measurement supplied. | Path remains absent, current outcome unset. Prepare and execute against frozen B configuration; then review and accept separately. Verification/acceptance owners to be assigned. |
| REV-06 — parameters and endpoints under-specified for execution | Pressure threshold/validity are project-controlled but not included; detailed A setup/instrument/uncertainty absent. | Preserve existing contracts; obtain exact adopted versions and endpoint instrumentation before test. Do not invent or silently move t0/t1. Configuration/test lead. |

The 460 ms record is 200 ms above the 260 ms allocation sum, but this difference cannot be attributed to a specific overhead without comparable setup/timestamp evidence. Resolve it before trusting a new timing budget. No claim that all old functions failed follows from that discrepancy.

## Remaining decisions and evidence

CR-1 has approved the requirement change, not an implementation solution. Choose an architecture that can meet 200 ms without changing the trigger or alert endpoint; resolve the existing input/operating contracts and all delay contributions; bind the proposed latch to actual motion and an operator-visible display; and execute/review VER-7 and VER-8. Check shared COMP-2 scheduling and interface changes for regressions. Current design options and recovery event-handling details remain proposals; source obligations remain authoritative.

Static artifact-preservation checks are recorded separately in `artifact-checks.json`. They can establish unchanged inputs, exact retained wording and missing-file status; they do not verify controller timing, motion behavior, warning visibility or human use. No controller tests ran.
