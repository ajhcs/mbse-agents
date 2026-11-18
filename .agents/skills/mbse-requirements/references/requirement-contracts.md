# Requirement contracts

Maintain the fields a designer, tester, or change reviewer needs to locate and interpret the requirement. Useful fields include ID, statement, source ID and locator, rationale, type, conditions, acceptance criterion, parent or derivation link, owner, status, allocation, and verification intent.

For a source-sensitive baseline, record the source revision/edition, applicable system and jurisdiction, claim verified, access limits, and whether it is an obligation, guidance, stakeholder statement, observation, or proposal. A newer publication does not silently replace the program's adopted basis.

Example project proposal: "The alarm controller shall assert the local high-temperature alarm within 100 ms after a valid temperature has remained at or above 8 deg C continuously for 2 s." The threshold and duration are project assumptions until confirmed; the timer starts at the first valid threshold-crossing sample. Neither value is a regulatory limit.

Check sources in both directions. Confirm that each stakeholder need has a disposition and each requirement has an identifiable basis. A many-to-many trace can be correct. Check whether child requirements collectively cover the original behavior and conditions, including any shared constraints.

If acceptance cannot be specified yet, mark the requirement provisional and record the missing decision and its owner. Keep the verification criterion distinct from the validation of the stakeholder outcome.

For each open decision, retain affected IDs, the consequence if the assumption is wrong, the evidence needed, and its eventual resolution. A question with no consequence for the current work need not block the draft.

Keep an ID for a continuing requirement and record revisions to its content. Splits, merges, replacements, or removals need new/retired IDs as appropriate, a supersession record, disposition of every original obligation, and reassessment of downstream allocations/evidence. Never recycle a retired ID for unrelated behavior. A source link records basis; a derived-from link additionally needs a derivation rationale.
