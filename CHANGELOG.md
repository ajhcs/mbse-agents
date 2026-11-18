# Changes

## 2.0.0-alpha.2

- Rewrote all 13 skills and their starter prompts around the engineering result
  and the checks a reviewer will use. Added guidance on reasoning effort,
  parallel review, and checking diagrams at the intended viewing size.
- Added a deterministic replay for numeric go/hold tables. It checks the issued
  Markdown against independently derived cases and records the input hashes.
- Added synthetic review cases for timing uncertainty and event qualification.
  Offline checks cover packaging, discovery, and replay. Live model behavior
  with the rewritten prompts remains untested.

## 2.0.0-alpha.1 — release candidate

This candidate develops MBSE Agents into a connected systems-engineering agent
with a reasoning entrypoint, judgment benchmark, historical project studies,
executable domain analyses and portable plugin packaging. It replaces the earlier
persona-based presentation with explicit capabilities and source-linked results.

The canonical skill names are listed in [the catalog](docs/skills.md). The founder
review is archived outside the shipped engineering catalog. Existing local skill
edits remain protected during installation and updates.

Release qualification and publication status are recorded separately from
implementation in [the release report](docs/release-report.md). Historical
reviews remain records of their original scope and revision.
