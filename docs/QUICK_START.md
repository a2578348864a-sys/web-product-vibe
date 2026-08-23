# Quick Start

## 1. Install

### Maintained adapters

#### Windows

```powershell
.\install.ps1 -HostType all -ProjectRoot "D:\your-project"
```

Host choices: `codex` / `claude` / `dsh` / `all`.

#### macOS / Linux

```bash
./install.sh all /path/to/your-project
```

### Any other coding agent / harness

The core Skill is model-agnostic and host-neutral. Copy the entire canonical folder:

```text
skill/web-product-vibe/
```

into the host's supported Skill / rules / project-instructions location. Keep `SKILL.md`, `references/`, and `templates/` together.

If the host has no formal Skill mechanism, expose `SKILL.md` as persistent project instructions and keep the sibling files accessible to the agent.

See [`platforms/GENERIC_AGENT.md`](../platforms/GENERIC_AGENT.md) for capability levels and integration rules.

## 2. New project: follow the decision chain

### DISCOVER — research comparable projects first

```text
Use web-product-vibe. Enter DISCOVER.
My project idea is ...
Research comparable active/new GitHub projects and products.
Compare target user, user journey, UX/UI, technical choices and trade-offs.
Keep facts separate from inference. Do not write code yet.
```

### SYNTHESIZE — decide our own solution

```text
Enter SYNTHESIZE.
Based on the research and my constraints, decide what we should actually build.
Separate confirmed facts, interpretations, goals, constraints and assumptions.
Show what to adopt / adapt / reject / park, then give one recommended solution,
its prerequisites, biggest failure mode, and what evidence would change the recommendation.
If a critical assumption can change the direction, design the lowest-cost validation first.
```

### DESIGN — turn the chosen solution into a real user experience

```text
Enter DESIGN.
Define the primary user journey, screens/routes, actions, information hierarchy,
empty/loading/running/success/error states, persistence, refresh behavior,
recovery paths and clear next steps.
```

### PLAN — generate the complete project plan before execution

```text
Enter PLAN.
Generate the comprehensive project plan before coding.
Cover all applicable dimensions: product/scope, frontend, backend, data/source of truth,
AI/Agent boundaries, security/privacy/permissions, external dependencies,
engineering/module boundaries, reliability, observability, testing,
deployment/migration/rollback, cost/performance where material,
Product Skeleton, vertical slices, front/back sync contract and real-browser acceptance.
Mark irrelevant sections N/A instead of inventing complexity.
Give READY / READY WITH CONDITIONS / NOT READY and freeze only when ready.
```

Recommended planning chain:

```text
IDEA → DISCOVER → SYNTHESIZE → DESIGN → PLAN → FREEZE
```

## 3. First execution stage: Product Skeleton

After the plan is frozen:

```text
Enter BUILD and implement Product Skeleton (Slice 0) first.
Make the planned core journey clickable with real routes/navigation and representative states.
Use fixtures/mocks only where the real backend is not built yet.
Then run a real-browser Skeleton Gate before broad backend implementation.
```

## 4. Build vertical slices

```text
Implement Slice 1 from the frozen plan as one complete user-observable behavior:
frontend + interaction + backend + persistence + refresh truth + failure recovery.
Then enter ACCEPT and verify it through a real browser before Slice 2.
```

Execution loop:

```text
Product Skeleton → Skeleton ACCEPT
→ BUILD 1 → ACCEPT
→ BUILD 2 → ACCEPT
→ ...
→ Full E2E ACCEPT
```

## 5. If you want the agent to keep running without stopping

```text
Continue through the frozen plan without waiting for manual confirmation.
Do not change scope and do not interpret continuous execution as backend-first execution.
Complete Slice N with frontend + backend + persistence + recovery + real-browser acceptance
before moving to Slice N+1. If acceptance fails, fix the smallest blocker, re-test, then continue.
```

## 6. Existing project that feels wrong

```text
Use web-product-vibe. Enter AUDIT.
Start from the real user entry and walk the core journey.
Find stale UI, front/back disconnects, misleading state, missing persistence,
refresh problems, failure-recovery gaps, permission/security mismatches and dead ends.
Do not start with architecture cleanup.
```

## 7. New idea during development

```text
Enter CHANGE.
Classify this idea as REQUIRED NOW / VALUABLE NEXT / PARK / REPLACE.
Do not implement it automatically.
```

## 8. Completion labels

- `Backend PASS` — backend/data/business behavior is correct
- `Frontend PASS` — UI/interaction/state behavior is correct
- `Slice DONE` — Backend PASS + Frontend PASS + real-browser acceptance
- `Project DONE` — the frozen core user journey passes full E2E

## 9. Capability rule

The underlying model family does not determine compatibility. The host's tools determine which claims can be verified:

- instructions/context only → planning modes
- repository + shell/tests → BUILD
- browser / Playwright-equivalent → full Web/UI ACCEPT

Missing capability means missing evidence, not fake PASS.

## 10. Validate this package

```bash
python tools/check_skill.py
```

Expected result:

```text
PASS: canonical model-agnostic skill package is valid; maintained adapters: Codex + Claude Code + DeepSeek Harness
```