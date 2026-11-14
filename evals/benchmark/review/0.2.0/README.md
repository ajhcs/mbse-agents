# Version 0.2.0 construction diagnostics

These records inspect the question bank, not a participant. They include keyed
option labels and must remain outside producer packets and installed skills.

- `candidate-diagnostics.json` records the first complete revision reviewed on
  2026-11-13, before source-label spacing was corrected.
- `candidate2-diagnostics.json` records the same question, choice and key content
  with corrected spacing in source titles and locators. Its bank hash identifies
  the current candidate submitted for independent content review.

Both were generated with `python3 scripts/benchmark.py diagnose --output PATH`.
The scorer source hash was
`5b0a18f5dd881812622e8cc8f8c70f1c795bc92d2ab8aec43321fc6e31a44bcf`.
The files retain actual item lengths, keyed positions, tie decisions and shortcut
accuracy by split. The change from the original cueable bank is a construction
repair, not evidence of model improvement or complete question validity.

The final scorer subsequently added rejection of numeric exponent overflow
(`1e999`) as well as explicit nonfinite JSON tokens. Its SHA-256 is
`f693899802f6e16752559f5df2df4f959703e295cce94b7cafe8f787d94b9a3d`.
This repair does not change either diagnostic's finite inputs or computed results.

The [initial diagnostic](../../../evidence/quiz-diagnostic-20261113/README.md)
and [original source archive](../../../archive/benchmark-0.1.0/manifest.json)
preserve the evidence that motivated the repair. Version 0.2.0 was authored with
access to all splits; it is not a protected or untouched evaluation set.
