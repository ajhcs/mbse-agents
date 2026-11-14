# Proposed controller revision B

The revised baseline is [requirements.md](requirements.md), [architecture.md](architecture.md), [verification.md](verification.md), with the preserved [source.md](source.md), [CR-1](change-request.md), and [historical report](report-old.json). [change-review.md](change-review.md) records changes, findings, applicability and remaining decisions.

REQ-7 is now 200 ms with its identity and all other statement wording retained. REQ-8 and the protected source note are unchanged. Recovery now requires an eligible explicit local resume in the proposed architecture; network/data restoration alone keeps the inhibit latched and visible.

The inherited serial budget is 260 ms, implementation changes are unselected, and EVD-A-7 remains a 460 ms historical record for revision A's 500 ms criterion. No revision-B report was created and no controller test ran. Artifact-preservation checks are separate from engineering verification.
