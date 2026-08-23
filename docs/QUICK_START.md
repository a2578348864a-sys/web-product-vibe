# Quick Start

## 1. Install

### Windows

```powershell
.\install.ps1 -HostType all -ProjectRoot "D:\your-project"
```

Host choices: `codex` / `claude` / `dsh` / `all`.

### macOS / Linux

```bash
./install.sh all /path/to/your-project
```

## 2. Start with the right mode

### New project: research first

```text
Use web-product-vibe. Enter DISCOVER.
My project idea is ...
Research comparable active GitHub projects first. Compare product positioning,
user journey, UX/UI, technical choices and trade-offs. Do not write code yet.
```

### Once the idea is clear

```text
Enter DESIGN. Define the core user journey, screens, interactions, states,
failure recovery, persistence and next step before architecture.
```

For a non-trivial new Web product or major UI redesign:

```text
Build Product Skeleton (Slice 0) first.
Make the core journey clickable with representative states and fixtures/mocks where needed.
Run a real-browser Skeleton Gate before substantial backend implementation.
```

Then:

```text
Enter PLAN. Freeze the MVP and non-goals, then derive the minimum technical design
and split implementation into vertical slices.
```

### Build incrementally

```text
Enter BUILD. Implement Slice 1 as a complete vertical behavior:
frontend + interaction + backend + persistence + refresh truth + failure recovery.
Then enter ACCEPT and verify it through a real browser before continuing.
```

Recommended loop:

```text
DISCOVER → DESIGN → PRODUCT SKELETON → Skeleton ACCEPT → PLAN
→ BUILD 1 → ACCEPT → BUILD 2 → ACCEPT → ... → Full ACCEPT
```

## 3. If you want the agent to keep running without stopping

Use this pattern:

```text
Continue through the approved plan without waiting for manual confirmation.
Do not interpret continuous execution as backend-first execution.
Complete Product Skeleton / Slice N with frontend + backend + persistence + real-browser acceptance
before moving to Slice N+1. If acceptance fails, fix the smallest blocker, re-test, then continue.
Do not expand frozen scope automatically.
```

This preserves autonomous execution while preventing the common failure mode:

```text
all backend done → old UI left unchanged → final product unusable
```

## 4. Existing project that feels wrong

```text
Use web-product-vibe. Enter AUDIT.
Start from the real user entry and walk the core journey.
Find front/back disconnects, old UI that no longer represents current backend behavior,
misleading UI state, missing persistence, refresh problems, failure recovery gaps and dead ends.
Do not start with architecture cleanup.
```

## 5. New idea during development

```text
Enter CHANGE.
Classify this idea as REQUIRED NOW / VALUABLE NEXT / PARK / REPLACE.
Do not implement it automatically.
```

## 6. Completion labels

Use these precisely:

- `Backend PASS` — backend/data/business behavior is correct
- `Frontend PASS` — UI/interaction/state behavior exists
- `Slice DONE` — Backend PASS + Frontend PASS + real-browser user-journey acceptance

## 7. Validate this package

```bash
python tools/check_skill.py
```

Expected result:

```text
PASS: canonical skill package is valid for Codex + Claude Code + DeepSeek Harness installation
```
