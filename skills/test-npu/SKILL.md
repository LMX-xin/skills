---
name: test-npu
description: Run NPU precision and correctness validation for xLLM. Use when user asks /test npu, NPU accuracy checks, NPU regression verification, or parity checks against baseline outputs.
---

# Test NPU Skill

## Goal

Validate NPU output quality and numerical correctness with reproducible evidence.

## Workflow

1. Discover existing NPU test entry points from repo scripts and CI.
2. Run correctness tests first, then accuracy or parity tests.
3. Record seed, model, batch size, and precision mode for every run.
4. Compare against baseline outputs and compute deltas.
5. Mark result failed if thresholds are exceeded.

## Minimum Metrics

- pass/fail status
- max absolute error
- mean absolute error
- mismatch count or mismatch rate
- latency per request or token if available

## Reporting

- Include command lines, key env vars, and artifact paths.
- Include threshold values and whether each metric passes.
- If failed, provide smallest repro command.
