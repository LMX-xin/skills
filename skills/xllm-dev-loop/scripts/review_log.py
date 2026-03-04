#!/usr/bin/env python3
"""Initialize and append xLLM dev-loop review documents."""

from __future__ import annotations

import argparse
from pathlib import Path


def init_file(path: Path, goal: str, env: str, build: str, service: str, test: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise SystemExit(f"review file already exists: {path}")

    content = f"""# xLLM Iteration Review

## Session Summary

- Task goal: {goal}
- Environment: {env}
- Build command: `{build}`
- Service command: `{service}`
- Test command: `{test}`
- Success criteria: [fill me]

## Final Review

### Style Check (google-cpp-style)

### Hidden Risk Review (code-review-risk)

### Release Recommendation
"""
    path.write_text(content, encoding="utf-8")


def append_iteration(
    path: Path,
    iteration: int,
    work: str,
    bug_trigger: str,
    fix: str,
    result: str,
    next_step: str,
) -> None:
    if not path.exists():
        raise SystemExit(f"review file not found: {path}")

    block = f"""
## Iteration {iteration}

### Work
{work}

### Bug Trigger / Root Cause
{bug_trigger}

### Fix Applied
{fix}

### Result
{result}

### Next Step
{next_step}
"""
    with path.open("a", encoding="utf-8") as fp:
        fp.write(block)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="xLLM review log manager")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init", help="initialize a new review markdown")
    p_init.add_argument("--file", required=True)
    p_init.add_argument("--goal", required=True)
    p_init.add_argument("--env", required=True)
    p_init.add_argument("--build", required=True)
    p_init.add_argument("--service", required=True)
    p_init.add_argument("--test", required=True)

    p_add = sub.add_parser("add", help="append one iteration entry")
    p_add.add_argument("--file", required=True)
    p_add.add_argument("--iter", type=int, required=True)
    p_add.add_argument("--work", required=True)
    p_add.add_argument("--bug-trigger", required=True)
    p_add.add_argument("--fix", required=True)
    p_add.add_argument("--result", required=True)
    p_add.add_argument("--next", required=True)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    path = Path(args.file)

    if args.cmd == "init":
        init_file(path, args.goal, args.env, args.build, args.service, args.test)
        print(f"initialized: {path}")
        return 0

    if args.cmd == "add":
        append_iteration(
            path=path,
            iteration=args.iter,
            work=args.work,
            bug_trigger=args.bug_trigger,
            fix=args.fix,
            result=args.result,
            next_step=args.next,
        )
        print(f"appended iteration {args.iter}: {path}")
        return 0

    raise SystemExit("unsupported command")


if __name__ == "__main__":
    raise SystemExit(main())
