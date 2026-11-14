# Systems engineering judgment exercises

Start with [the benchmark guide](../../docs/benchmark.md) for practice, isolated
agent packets, independent explanation review and comparisons.

`items.json` contains public questions, reasoning dimensions, split assignments,
selected skills and primary-source locators. `keys.json` contains proposed
selections, explanations and reviewer criteria. Keep the latter out of producer
packets and installed skill references. Its public availability means a prepared
packet is input separation, not a secure held-out test.

The initial bank contains authored engineering situations and historical transfer
questions. Supplied facts in an authored vignette are exercise assumptions.
Historical sources support the supplied historical facts; they do not establish
that the proposed modern intervention is effective. Question selections and
review criteria require independent adjudication.

The adjacent [performance bank](../cases.json) covers artifact work and open
engineering reasoning. Its criteria remain separately maintained. Historical
HO-01 evidence is retained unchanged; its unknown model/settings do not become
known because a new benchmark exists.

Use `python3 scripts/benchmark.py validate` from the repository root to check
bank structure, source references and key consistency. Tests use synthetic
response records to qualify scoring behavior. Neither check is an agent score.

Version 0.2.0 replaces the original choices with competing engineering judgments,
repairs ambiguous lifecycle and command-authorization stems, clarifies a selected
system boundary and rebalances option labels within each split. All splits were
available during this revision. The original [bank and scorer](../archive/benchmark-0.1.0/manifest.json)
and [failed three-arm diagnostic](../evidence/quiz-diagnostic-20261113/README.md)
remain unchanged. Do not score old responses against the revised labels.

`python3 scripts/benchmark.py diagnose` reports measured answer-length shortcuts,
ties and position distributions. It is a construction diagnostic, not a content
validity test. Packets, responses and optional reviews now use schema 2 binding;
the archived schema 1 runs are historical records, not retroactively validated.
