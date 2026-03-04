#!/usr/bin/env python3
"""Create a new skill skeleton in this repository."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def normalize_name(name: str) -> str:
    name = name.strip().lower().replace("_", "-").replace(" ", "-")
    name = re.sub(r"[^a-z0-9-]", "", name)
    name = re.sub(r"-+", "-", name).strip("-")
    if not name:
        raise ValueError("invalid skill name after normalization")
    return name


def load_manifest(path: Path) -> dict:
    if not path.exists():
        return {"plugin_name": "xllm-engineering-skills", "plugin_description": "", "skills": []}
    return json.loads(path.read_text(encoding="utf-8"))


def save_manifest(path: Path, manifest: dict) -> None:
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a skill skeleton")
    parser.add_argument("--name", required=True, help="skill name")
    parser.add_argument("--description", required=True, help="frontmatter description")
    parser.add_argument(
        "--resources",
        default="",
        help="comma-separated dirs from scripts,references,assets",
    )
    parser.add_argument(
        "--repo",
        default=".",
        help="repository root path, default current directory",
    )
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    skill_name = normalize_name(args.name)
    skill_dir = repo / "skills" / skill_name
    if skill_dir.exists():
        raise SystemExit(f"skill already exists: {skill_dir}")

    skill_dir.mkdir(parents=True, exist_ok=False)
    skill_md = skill_dir / "SKILL.md"
    skill_md.write_text(
        "---\n"
        f"name: {skill_name}\n"
        f"description: {args.description}\n"
        "---\n\n"
        f"# {skill_name}\n\n"
        "## Goal\n\n"
        "[Describe what this skill should reliably do]\n\n"
        "## Workflow\n\n"
        "1. [Step 1]\n"
        "2. [Step 2]\n"
        "3. [Step 3]\n",
        encoding="utf-8",
    )

    requested = {item.strip() for item in args.resources.split(",") if item.strip()}
    valid = {"scripts", "references", "assets"}
    unknown = requested - valid
    if unknown:
        raise SystemExit(f"unknown resources: {sorted(unknown)}")
    for name in sorted(requested):
        (skill_dir / name).mkdir(parents=True, exist_ok=True)

    manifest_path = repo / "xllm" / "manifest.json"
    manifest = load_manifest(manifest_path)
    skills = list(manifest.get("skills", []))
    if skill_name not in skills:
        skills.append(skill_name)
        manifest["skills"] = skills
        save_manifest(manifest_path, manifest)

    print(f"created skill: {skill_dir}")
    print("next:")
    print(f"  python3 skills/skill-creator/scripts/quick_validate.py skills/{skill_name}")
    print("  python3 scripts/sync_marketplace.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
