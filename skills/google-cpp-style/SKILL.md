---
name: google-cpp-style
description: Enforce Google-style C++ conventions in xLLM code changes. Use when user asks for C++ style cleanup, code规范, 注释规范, ordering rules, lint fixes, or /style checks.
---

# Google C++ Style Skill

## Goal

Keep xLLM C++ code consistent, readable, and maintainable under Google-style conventions.

## Rules

1. Use clear naming and avoid abbreviations except conventional ones.
2. Prefer `const`, references, and RAII for ownership clarity.
3. Keep class declaration order consistent:
   - public interface first
   - protected second
   - private last
4. Inside each access block, place constructors and methods before data members unless local style guide overrides.
5. Keep comments as intent-focused explanations, not line-by-line narration.
6. Keep includes sorted and minimal; avoid unused headers.

## Validation

- Run project lint or formatter if available.
- Manually check declaration order and comment quality in changed files.
- Flag style exceptions explicitly with rationale.
