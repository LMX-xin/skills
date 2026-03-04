---
name: test-gpu
description: Run GPU precision and correctness validation for xLLM. Use when user asks /test gpu, GPU accuracy checks, CUDA regression verification, or GPU baseline parity tests.
---

# Test GPU Skill

## Goal

Verify GPU correctness and numerical stability with reproducible commands and thresholded metrics.

## Workflow

1. Use repository-native GPU test commands before inventing new ones.
2. Execute unit or functional correctness tests first.
3. Execute precision-parity tests against trusted baseline.
4. Capture device info, driver version, CUDA toolkit, and precision mode.
5. Report pass/fail using explicit thresholds.

## Minimum Metrics

- pass/fail status
- max absolute error
- relative error percentiles
- throughput and latency where available
- OOM or kernel failure signals

## Guardrails

- Do not mix baseline and candidate with inconsistent precision settings.
- Do not claim parity without metric evidence.
