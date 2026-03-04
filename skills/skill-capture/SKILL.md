---
name: skill-capture
description: Capture a newly learned agent workflow as a reusable skill and save it into this repository. Use when user asks to turn current behavior into a skill, migrate能力, 沉淀经验, or build inheritable agent abilities.
---

# Skill Capture

## Goal

Convert a successful one-off agent workflow into a reusable skill in this repository.

## Capture Workflow

1. Extract stable workflow steps from current task history.
2. Define trigger phrases, inputs, outputs, and success criteria.
3. Create a new skill folder under `skills/<skill-name>/`.
4. Write `SKILL.md` with strong trigger description and executable steps.
5. Add scripts or references only if reuse is likely.
6. Validate with `skills/skill-creator/scripts/quick_validate.py`.
7. Register the skill in `xllm/manifest.json` and sync marketplace.

## Commands

### Create skill skeleton

```bash
python3 scripts/create_skill.py --name <skill-name> --description "<trigger + purpose>" --resources scripts,references
```

### Validate

```bash
python3 skills/skill-creator/scripts/quick_validate.py skills/<skill-name>
```

### Sync plugin metadata

```bash
python3 scripts/sync_marketplace.py
```

## Definition of Done

- New skill folder exists with valid frontmatter.
- Validation passes.
- Skill is listed in `xllm/manifest.json`.
- Marketplace plugin entry includes the skill.
