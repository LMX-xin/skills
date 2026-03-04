---
name: code-review-risk
description: Perform risk-focused code review for regressions and production impact. Use when user asks for review, risk analysis, hidden bugs, reliability concerns, or pre-merge safety checks.
---

# Code Review Risk Skill

## Goal

Identify defects, regressions, and operational risks before merge.

## Review Priorities

1. Correctness: logic errors, edge cases, invariant violations.
2. Safety: null access, bounds issues, data races, deadlocks.
3. Behavior changes: API contracts, backward compatibility, config defaults.
4. Performance risk: algorithmic blowups, memory growth, latency shifts.
5. Test coverage: missing tests for new paths and failure paths.

## Output Format

- Findings first, ordered by severity.
- For each finding: file, line, risk, impact, and fix suggestion.
- If no findings: state that clearly and list residual testing gaps.

## Guardrails

- Do not focus on cosmetic nits before safety issues.
- Do not approve behavior-changing code without tests.
