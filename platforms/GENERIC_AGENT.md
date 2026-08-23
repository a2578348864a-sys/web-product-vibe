# Generic / Any-Agent Compatibility

Web Product Vibe is **model-agnostic** and **host-neutral** at its core.

The workflow does not depend on GPT, Claude, DeepSeek, Gemini, Qwen, Kimi, or any other specific model family. The practical integration boundary is the **coding host / agent harness**, not the underlying model.

## What “compatible” means

A host can use Web Product Vibe when it can load the canonical `skill/web-product-vibe/` instructions, or expose those instructions to the model as persistent project context.

Capability depends on the tools the host exposes:

| Host capability | What Web Product Vibe can do |
|---|---|
| Read Markdown / project instructions only | `DISCOVER` / `SYNTHESIZE` / `DESIGN` / `PLAN` where the host can access the needed context |
| Repository/file access + shell/tests | Adds practical `BUILD` support |
| Real browser / Playwright-equivalent access | Enables full `ACCEPT` and Web/UI `DONE` evidence |
| Web/GitHub research access | Enables live comparable-project research in `DISCOVER` |

If a capability is missing, keep the workflow but report the missing evidence. Never invent a `PASS`.

## Generic installation

1. Copy the entire canonical folder:

```text
skill/web-product-vibe/
```

2. Put it in the host's supported Skill / rules / project-instructions location.
3. Keep `SKILL.md`, `references/`, and `templates/` together so relative links remain valid.
4. If the host has no formal Skill mechanism, expose `SKILL.md` as persistent project instructions and make the sibling `references/` and `templates/` available to the agent.

There is no universal filesystem path because every coding host chooses its own convention.

## Maintained adapters vs core compatibility

The repository currently includes explicit installation guidance for:

- Codex
- Claude Code
- DeepSeek Harness

These are **maintained adapters/examples**, not an exclusive compatibility list.

Other coding agents, IDE agents, CLI harnesses, local-model harnesses, or future tools can use the same canonical Skill when they provide an equivalent instruction-loading mechanism.

## Important distinction: model vs host

Changing the underlying model normally does not require changing Web Product Vibe.

For example, a host may use GPT today and another model tomorrow. If the host still loads the same Skill and exposes the required repository/browser tools, the workflow stays the same.

A raw chat/API model with no repository, shell, or browser tools can still use the planning parts of the Skill, but it cannot honestly perform full implementation or real-browser acceptance on its own.