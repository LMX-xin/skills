# AGENTS.md instructions for /export/home/limenxin1/xllm_wyf/skills

<INSTRUCTIONS>
## Skills

Use local skills from `./skills/*/SKILL.md`.

### xLLM engineering skills

- `xllm-dev-loop`: Manual full workflow for compile -> start service -> run tests -> fix bugs iteratively -> write review logs -> final style and risk review.
- `compiler`: Manual compile/build skill.
- `test-npu`: Manual NPU precision and correctness skill.
- `test-gpu`: Manual GPU precision and correctness skill.
- `pressure-test`: Manual load/stress/benchmark skill.
- `google-cpp-style`: Manual C++ style and comment规范 skill.
- `code-review-risk`: Manual risk-focused review skill.
- `skill-capture`: Capture a successful workflow as a reusable skill.

### Manual Trigger Policy

- Do not auto-trigger xLLM skills by default.
- Select skills only after explicit user intent or explicit command phrases.
- Recommended command phrases:
  - `/xllm-dev-loop`: run end-to-end workflow
  - `/compiler`
  - `/test npu`
  - `/test gpu`
  - `/pressure-test`
  - `/style`
  - `/risk-review`
- If the user asks for full closed-loop delivery, prefer `xllm-dev-loop` and then invoke subskills as needed.
- For xLLM C++ delivery sign-off, run `google-cpp-style` and `code-review-risk` before final completion.

### Skill capture policy

- When user says the current workflow should become reusable, use `skill-capture`.
- Save the new skill under `skills/<skill-name>/`.
- Register it in `xllm/manifest.json`.
- Run:
  - `python3 scripts/sync_marketplace.py`
  - `python3 skills/skill-creator/scripts/quick_validate.py skills/<skill-name>`
</INSTRUCTIONS>
