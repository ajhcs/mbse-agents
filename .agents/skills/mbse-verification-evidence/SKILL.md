---
name: mbse-verification-evidence
description: "Plan verification, replay operator decision tables, or assess evidence for a requirement or intended use, including uncertainty and configuration applicability."
---

# Plan Verification and Evidence

State the claim under review and the configuration and conditions it applies to. For requirements verification, check the specified behavior or limit. For validation, check whether the system serves the users in their intended setting. Choose a test, inspection, demonstration, analysis, or proof that can settle the claim and explain what the resulting observation would establish.

Define input, environment, observation, and acceptance before drawing a conclusion. Exercise the normal, boundary, failure, and recovery cases that could change the result. For numerical limits, use the adopted decision rule and uncertainty interpretation. Check equality, both sides of a limit, and an uncertainty interval that crosses it for contradictory or missing dispositions. For event-triggered timing, match the test stimulus to a qualifying interface event, including the shortest permitted event when it could affect detection. See [evidence contracts](references/evidence-contracts.md) for these cases, controlled results, and proof scope.

When the deliverable is an operator decision table with numeric go/hold gates, derive expected actions from the sources independently of the draft, including boundary readings and the full fallback. Run the [operating gate replay](references/operating-gates.md) on the delivered table for supported formats and gates. Correct discrepancies, rerun the final file, and retain the exact result and its coverage limits.

A reviewer should be able to trace each disposition from its claim and rule to the exact observations and configuration, or see the evidence still needed. Keep planned work, execution outcome, applicability, independent review, and authorized acceptance distinct. Verify any claimed tool or reviewer credit against the applicable basis. When execution is in scope, complete the checks, record failures and repairs, and bind the observations to the artifacts actually checked.
