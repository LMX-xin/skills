---
name: xllm-dev-loop
description: "Manual full-cycle xLLM development loop for compile, service startup, test execution, bug fixing, and iteration logging. Use when user explicitly asks for end-to-end execution such as compile xLLM, start service, run provided tests, fix bugs in closed loop, and write iteration review records."
---

# xLLM Dev Loop

## Invocation Mode

Use this skill only when the user explicitly asks for end-to-end loop execution or directly invokes `/xllm-dev-loop`.

## Goal

Complete a deterministic engineering loop:

1. Compile xLLM.
2. Start xLLM service with user-provided runtime parameters.
3. Run user-provided tests.
4. Detect and fix bugs in repeated iterations.
5. Record every iteration in a review document.
6. Run final code review for style and hidden risks.

## Required Inputs

- Build parameters and target.
- Service startup command and runtime args.
- Test command(s), expected behavior, and success threshold.
- Stop conditions (for example: max iterations, target accuracy, target error rate).

## Iteration Workflow

### 1. Session init

- Create or reuse a review file under `reviews/`.
- Initialize review file with goal, environment, commands, and baseline.

```bash
python3 skills/xllm-dev-loop/scripts/review_log.py init \
  --file reviews/<session>.md \
  --goal "<task goal>" \
  --env "<env summary>" \
  --build "<build command>" \
  --service "<service command>" \
  --test "<test command>"
```

### 2. Execute one iteration

- Run compile and capture errors.
- Start service and verify health.
- Run tests and collect metrics.
- If failed, identify bug trigger and root cause hypothesis.
- Apply minimal fix and retest.
- Append iteration record.

```bash
python3 skills/xllm-dev-loop/scripts/review_log.py add \
  --file reviews/<session>.md \
  --iter <N> \
  --work "<what was done>" \
  --bug-trigger "<why bug happened>" \
  --fix "<what was changed>" \
  --result "<metrics and pass/fail>" \
  --next "<next action>"
```

### 3. Loop control

- Continue until all success criteria are met or user-defined stop condition hits.
- If blocked, write blocker reason and the minimum next experiment.

### 4. Final quality gate

After loop success, run:

- `google-cpp-style` for C++ style and comment conformance.
- `code-review-risk` for hidden risk and regression review.

Append final decision to review document.

## Output Contract

Before completion, return:

- Final status (pass/fail).
- Iteration count and summary.
- Review document path.
- Remaining risks and recommended follow-up.

## Reference

Read `references/review-template.md` when creating or auditing iteration records.
