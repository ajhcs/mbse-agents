# Artifact consistency checks

Checked baseline: GH-DRAFT-01. Check execution: **2026-10-12T16:56:13Z**, obtained from the inherited host clock. These are actual document checks using PowerShell string/regular-expression comparisons and `Get-FileHash`; they are not controller tests or verification results. No network or model API was called. Actual model identity/settings remain unknown.

## Performed checks and results

| Check | Actual scope and result |
|---|---|
| Raw-input preservation | Both raw paragraphs beginning `N-01 Owner:` and `Candidate design:` were extracted from `request.md` and compared as exact substrings against the review guide. 2/2 preserved. |
| Source-ID presence | Checked N-01, N-02, N-03 and N-04 in each of the five core drafts. No missing raw source IDs. Unlabeled narrative inputs remain locators, not invented raw IDs. |
| Definition counts and uniqueness | All expected counts matched and all definitions were unique within their artifact ID prefix: RQ 10, DR 2, F 7, C 7, I 8, AD 4, VA 14, SV 4, D 12, RK 8. |
| Reference resolution | Extracted all artifact-ID references from the five core drafts and checked against definition sets. No undefined references. |
| Requirement trace consistency | For each of 12 requirements, compared planned VA-ID sets in the requirement and trace rows and checked that each linked VA row explicitly names that requirement. No missing rows, empty verification sets or mismatched links. This checks linkage only, not semantic sufficiency. |
| Markdown table structure | Checked field counts in each contiguous table in the five core drafts. No inconsistent row field counts. |
| Relative Markdown links / final report table | At 2026-10-12T16:57:27Z, checked all six saved Markdown artifacts: 15/15 relative links resolved to existing files, no table field-count errors, and all five recorded core hashes matched the files. This row was updated afterward to record that result. |
| Input and draft configuration | SHA-256 hashes were obtained from the actual input and five core artifact files; recorded below. |

The PowerShell host emitted an `InitializeDefaultDrives` warning, but the check command completed with exit code 0 and returned the expected comparison results and hashes. This warning did not prevent packet file reads or artifact creation.

## Semantic review performed

The draft was reviewed against each retained source clause: opening equality and 30 s, brief-dip reset, strict closing threshold and 60 s, local override, explicit automatic resumption, 5 s data absence, fault display, inhibited data-return recovery, remote intent and network-failure local stop. The review kept sampled continuity, closing reset, timestamp origin, physical stop and remote scope unresolved where the input did not settle them. The manager's 50 ms proposal is explicitly unapproved. One MCU/driver and common dependencies are retained; no redundancy, reliability rate or safe position was invented.

Proposed choices remain labeled: direct local latched inhibit, local fault indicator, guarded deliberate recovery, inhibited startup, data eligibility rules and timer-reset policy. Interface and physical behavior need engineering decisions and evidence. All VA/SV activities remain planned; the actual document checks do not count toward verified-requirement totals.

## Configuration fingerprints

Input `../request.md` SHA-256: `434A60FACFAE617C47A0AF1A2DECDF213138A5E75569209CF40F79331EEEDC4D`.

| Core artifact | SHA-256 at check execution |
|---|---|
| [00-review-guide.md](00-review-guide.md) | `2582CE1CC57DCD4F394F4A597F6C4EBDB4F04CD85B4D953FB477288CFBF60F04` |
| [01-requirements.md](01-requirements.md) | `4595C08FD5FAC86688D250354A02048B8CFA2D7647ABDDF74076FAB213111371` |
| [02-architecture.md](02-architecture.md) | `40DC7735A64CC4ECD46259EB2AB4F7EBBFC27D2631C7D1B3443DE6ED242A9EDD` |
| [03-verification-plan.md](03-verification-plan.md) | `2D376BF6344370870DC9F7CEDB3C93144D12B54F9E71BB3ABCAC6CE147E7684E` |
| [04-trace-and-decisions.md](04-trace-and-decisions.md) | `A68053A41319BF1AEBF24F82670EE65F8A5CED24342C7421A66EBBC589F6C4DB` |

This report is excluded from its own hash manifest. Later artifact edits require rerunning relevant checks and updating the fingerprints.

## Remaining limits and blockers

The requested artifact draft is complete. There is no evidence that the physical design meets stopping, sensing, movement or environmental performance. D-01 through D-12 and absent supplier/hardware/test evidence block a final approved design and unconditional acceptance. Missing evidence is a gap, not a failed test or a pass. No source repository, worked examples, evaluation rubrics or other agents' outputs were read.
