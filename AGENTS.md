# Working on MBSE Agents

- Read the relevant `.agents/skills/*/SKILL.md` before editing it. Use references
  when they affect the task. Keep entrypoints focused on the requested result
  and the checks a reviewer needs. Regenerate discovery outputs with
  `python3 scripts/catalog.py --write` after metadata edits.
- Preserve engineering IDs and evidence status in teaching cases. Distinguish
  requirements, guidance, judgment, and illustrative data. Verify precise
  regulatory or standards claims against applicable primary sources and record
  edition, locator, and access limits in `docs/sources.md`. Claim approvals, tool
  access, course provenance, and executed evidence only where established.
- Installations must preserve existing project instructions and refuse
  collisions. For packaging or validation changes, run
  `python3 scripts/validate.py` and `python3 -m unittest discover -s tests`
  with disposable fixtures. Use `docs/evaluation.md` for model behavior claims.
