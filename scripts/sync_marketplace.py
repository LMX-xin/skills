#!/usr/bin/env python3
"""Sync xLLM custom skills from manifest.json into .claude-plugin/marketplace.json."""

from __future__ import annotations

import json
from pathlib import Path


PLUGIN_NAME_DEFAULT = "xllm-engineering-skills"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    manifest_path = repo / "xllm" / "manifest.json"
    marketplace_path = repo / ".claude-plugin" / "marketplace.json"

    manifest = load_json(manifest_path)
    marketplace = load_json(marketplace_path)

    plugin_name = manifest.get("plugin_name", PLUGIN_NAME_DEFAULT)
    plugin_description = manifest.get("plugin_description", "")
    skills = manifest.get("skills", [])

    skill_paths = [f"./skills/{name}" for name in skills]

    plugins = marketplace.setdefault("plugins", [])
    existing = None
    for entry in plugins:
        if entry.get("name") == plugin_name:
            existing = entry
            break

    if existing is None:
        existing = {
            "name": plugin_name,
            "description": plugin_description,
            "source": "./",
            "strict": False,
            "skills": skill_paths,
        }
        plugins.append(existing)
    else:
        existing["description"] = plugin_description
        existing["source"] = "./"
        existing["strict"] = False
        existing["skills"] = skill_paths

    save_json(marketplace_path, marketplace)
    print(f"synced plugin '{plugin_name}' with {len(skill_paths)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
