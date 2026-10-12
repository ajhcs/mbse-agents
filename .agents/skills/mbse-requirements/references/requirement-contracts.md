# Requirement contracts

Useful fields: ID, statement, source ID and locator, rationale, type, conditions, acceptance criterion, parent/derived relation, owner, status, allocation, verification intent.

Example project proposal: "The alarm controller shall assert the local high-temperature alarm within 100 ms after a valid temperature has remained at or above 8 deg C continuously for 2 s." The threshold and duration are project assumptions until confirmed; the timer starts at the first valid threshold-crossing sample. Neither value is a regulatory limit.

Check sources in both directions: each stakeholder need should have a disposition, and each requirement should have an identifiable basis. A many-to-many trace can be correct. Links alone do not demonstrate that decomposition preserves the parent's meaning.

If acceptance cannot be specified yet, record the missing decision and its owner. Avoid marking a provisional requirement approved. Keep requirement verification distinct from stakeholder validation.
