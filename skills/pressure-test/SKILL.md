---
name: pressure-test
description: Execute stress, load, and benchmark tests for xLLM services. Use when user asks for pressure testing, load testing, throughput, latency p95 or p99, saturation behavior, or /pressure-test.
---

# Pressure Test Skill

## Goal

Measure stability and performance under load and detect regressions before deployment.

## Workflow

1. Identify target endpoint, traffic profile, and SLO thresholds.
2. Run warmup, steady-state, and peak phases.
3. Capture p50, p95, p99 latency, throughput, error rate, and resource usage.
4. Repeat runs to reduce variance and report confidence.
5. Compare with baseline and flag regressions.

## Test Matrix

- concurrency levels
- request length and output length
- model or feature flags
- duration per phase

## Reporting

- Include command, config, and hardware context.
- Include per-phase metrics and regression deltas.
- Include bottleneck hypothesis and next test.
