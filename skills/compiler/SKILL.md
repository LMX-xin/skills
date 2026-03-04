---
name: compiler
description: Compile and link xLLM C++ code safely and reproducibly. Use when user asks /compiler, build, compile, link errors, CMake or Make fixes, or wants a deterministic C++ build command and artifact validation.
---

# Compiler Skill

## Goal

Build xLLM C++ targets with deterministic commands, fast failure feedback, and explicit artifact checks.

## Workflow

1. Detect build system in this order: `CMakeLists.txt`, `BUILD.bazel`, `Makefile`, project scripts.
2. Reuse existing presets and scripts before creating new build entry points.
3. Build with warnings enabled; treat new warnings as potential regressions.
4. If build fails, classify by compiler, linker, dependency, or ABI mismatch.
5. After successful build, verify artifact existence and run smoke execution when possible.

## Commands

### CMake

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo
cmake --build build -j
```

### Make

```bash
make -j
```

## Output Requirements

- Report exact compile command used.
- Report compiler version and target.
- Report success artifacts and their paths.
- Report unresolved warnings and next actions.

## Guardrails

- Do not disable warnings globally to force success.
- Do not bypass failing compile steps without user approval.
- Prefer minimal compile-scope changes for faster iteration.
