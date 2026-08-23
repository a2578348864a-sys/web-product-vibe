# Changelog

All notable changes to Web Product Vibe are documented here.

## [Unreleased]

### Changed

- Added `SYNTHESIZE` as a first-class mode between research and design so comparable-project research ends in one recommended solution instead of flowing directly into implementation.
- Added explicit separation of confirmed facts, interpretations, goals, constraints, and unverified assumptions.
- Added a “question only if it can change the path” rule to reduce unnecessary clarification loops.
- Added low-cost reversible validation for critical assumptions that could change product direction, architecture, cost, or feasibility.
- Added `SOLUTION_PROPOSAL.md` for adopt/adapt/reject/park decisions, critical assumptions, failure/exit conditions, and recommendation-changing evidence.
- Reworked `PLAN` into a comprehensive project execution contract covering product, frontend, backend, data, AI, security/privacy/permissions, dependencies, engineering boundaries, reliability, observability, testing, deployment/rollback, cost/performance, Product Skeleton, vertical slices, sync contract, and acceptance.
- Added `PROJECT_PLAN.md` as the master plan template and moved Product Skeleton execution after plan readiness/freeze.
- Added Product Skeleton (Slice 0) as an early real-browser product-structure gate for non-trivial new Web products and major UI redesigns.
- Added a P0 rule that forbids backend-first completion for interactive Web work.
- Defined continuous/autonomous execution precisely: agents may keep running without manual confirmation, but must preserve frozen plan → Product Skeleton → vertical slice → browser-gate order.
- Added a front/back sync contract mapping user actions to frontend expression, backend effect, persisted truth, and refresh/reopen truth.
- Added completion layers: `Backend PASS`, `Frontend PASS`, `Slice DONE`, and `Project DONE`.
- Strengthened AUDIT guidance for stale UI, product truth drift, and security/permission mismatches.
- Updated README files, Quick Start, workflow, design principles, package validation, and templates.

## [0.3.0] - 2026-08-23

### Changed

- Reworked the repository into a public GitHub-friendly project structure.
- Added English and Simplified Chinese landing READMEs.
- Made `skill/web-product-vibe/` the single source of truth for all hosts.
- Updated installers to deploy the canonical skill to Codex, Claude Code, or DeepSeek Harness.
- Added concise workflow and design-principle documentation.
- Added MIT license and contribution guide.

### Kept

- Product-first planning and mandatory real-browser acceptance for Web/UI completion.

## [0.2.0] - 2026-08-23

- Added Codex, Claude Code and DeepSeek Harness compatibility.
- Added reversible installers with backup behavior.

## [0.1.0] - 2026-08-23

- Initial product-first Web vibe-coding skill.