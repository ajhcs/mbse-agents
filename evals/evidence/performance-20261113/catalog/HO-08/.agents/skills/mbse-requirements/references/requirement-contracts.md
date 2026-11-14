# Requirement contracts

Useful fields: ID, statement, source ID and locator, rationale, type, conditions, acceptance criterion, parent/derived relation, owner, status, allocation, verification intent.

For a source-sensitive baseline, record the source revision/edition, applicable system and jurisdiction, claim verified, access limits, and whether it is an obligation, guidance, stakeholder statement, observation, or proposal. A newer publication does not silently replace the program's adopted basis.

Example project proposal: "The alarm controller shall assert the local high-temperature alarm within 100 ms after a valid temperature has remained at or above 8 deg C continuously for 2 s." The threshold and duration are project assumptions until confirmed; the timer starts at the first valid threshold-crossing sample. Neither value is a regulatory limit.

Check sources in both directions: each stakeholder need should have a disposition, and each requirement should have an identifiable basis. A many-to-many trace can be correct. Links alone do not demonstrate that decomposition preserves the parent's meaning.

If acceptance cannot be specified yet, record the missing decision and its owner. Avoid marking a provisional requirement approved. Keep requirement verification distinct from stakeholder validation.

For each open decision, retain affected IDs, the consequence if the assumption is wrong, the evidence needed, and its eventual resolution. A question with no consequence for the current work need not block the draft.

Keep an ID for a continuing requirement and record revisions to its content. Splits, merges, replacements, or removals need new/retired IDs as appropriate, a supersession record, disposition of every original obligation, and reassessment of downstream allocations/evidence. Never recycle a retired ID for unrelated behavior. A source link records basis; a derived-from link additionally needs a derivation rationale.
