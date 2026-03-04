#!/usr/bin/env python3
"""Install this repository's custom skills into ~/.codex/skills."""

from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path


def load_manifest(repo: Path) -> dict:
    path = repo / "xllm" / "manifest.json"
    return json.loads(path.read_text(encoding="utf-8"))


def ensure_clean_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def install_skill(src: Path, dst: Path, mode: str) -> None:
    ensure_clean_path(dst)
    if mode == "symlink":
        dst.symlink_to(src)
    elif mode == "copy":
        shutil.copytree(src, dst)
    else:
        raise ValueError(f"unsupported mode: {mode}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Install xLLM skills into Codex")
    parser.add_argument("--repo", default=".", help="skills repo root")
    parser.add_argument(
        "--codex-home",
        default=os.environ.get("CODEX_HOME", str(Path.home() / ".codex")),
        help="codex home directory",
    )
    parser.add_argument("--mode", choices=["symlink", "copy"], default="symlink")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    codex_home = Path(args.codex_home).resolve()
    target_root = codex_home / "skills"
    target_root.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest(repo)
    skill_names = manifest.get("skills", [])

    for name in skill_names:
        src = repo / "skills" / name
        dst = target_root / name
        if not src.exists():
            raise SystemExit(f"missing skill path: {src}")
        if args.dry_run:
            print(f"[dry-run] {args.mode}: {src} -> {dst}")
            continue
        install_skill(src, dst, args.mode)
        print(f"installed: {name} ({args.mode})")

    print("done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
