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

```text
Enter PLAN. Freeze the MVP and non-goals, then derive the minimum technical design
and split implementation into vertical slices.
```

### Build incrementally

```text
Enter BUILD. Implement Slice 1 only.
Then enter ACCEPT and verify it through a real browser before continuing.
```

Recommended loop:

```text
DISCOVER → DESIGN → PLAN → BUILD 1 → ACCEPT → BUILD 2 → ACCEPT → ... → Full ACCEPT
```

## 3. Existing project that feels wrong

```text
Use web-product-vibe. Enter AUDIT.
Start from the real user entry and walk the core journey.
Find front/back disconnects, misleading UI state, missing persistence,
refresh problems, failure recovery gaps and dead ends.
Do not start with architecture cleanup.
```

## 4. New idea during development

```text
Enter CHANGE.
Classify this idea as REQUIRED NOW / VALUABLE NEXT / PARK / REPLACE.
Do not implement it automatically.
```

## 5. Validate this package

```bash
python tools/check_skill.py
```

Expected result:

```text
PASS: canonical skill package is valid for Codex + Claude Code + DeepSeek Harness installation
```
