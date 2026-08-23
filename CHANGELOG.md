# Changelog

All notable changes to Web Product Vibe are documented here.

## [Unreleased]

### Changed

- Added Product Skeleton (Slice 0) as an early real-browser product-structure gate for non-trivial new Web products and major UI redesigns.
- Added a P0 rule that forbids backend-first completion for interactive Web work.
- Defined continuous/autonomous execution precisely: agents may keep running without manual confirmation, but must preserve Product Skeleton → vertical slice → browser-gate order.
- Added a front/back sync contract mapping user actions to frontend expression, backend effect, persisted truth, and refresh/reopen truth.
- Added three completion layers: `Backend PASS`, `Frontend PASS`, and `Slice DONE`.
- Strengthened AUDIT guidance for the common failure where backend capability advances while the UI still represents an older product version.
- Updated Quick Start, workflow, design principles, README files, implementation slice template, acceptance report, and package validation.

## [0.3.0] - 2026-08-23

### Changed

- Reworked the repository into a public GitHub-friendly project structure.
- Added English and Simplified Chinese landing READMEs.
- Made `skill/web-product-vibe/` the single source of truth for all hosts.
- Updated installers to deploy the canonical skill to Codex, Claude Code, or DeepSeek Harness.
- Added concise workflow and design-principle documentation.
- Added MIT license and contribution guide.

### Kept

- Seven modes: DISCOVER, DESIGN, PLAN, BUILD, ACCEPT, CHANGE, AUDIT.
- Product-first planning and mandatory real-browser acceptance for Web/UI completion.

## [0.2.0] - 2026-08-23

- Added Codex, Claude Code and DeepSeek Harness compatibility.
- Added reversible installers with backup behavior.

## [0.1.0] - 2026-08-23

- Initial product-first Web vibe-coding skill.
