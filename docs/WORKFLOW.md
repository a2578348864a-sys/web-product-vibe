# Workflow

Web Product Vibe separates **research, decision, design, planning, implementation, and acceptance** so AI does not jump from “I found some GitHub projects” straight into backend code.

## 1. DISCOVER — learn before deciding

Start from a rough intent. Research comparable products and GitHub projects, preferring active maintenance, meaningful adoption, recent approaches, and visible UI/product behavior.

For each reference, reverse-engineer:

- target user and job
- entry → action → result → next step
- information architecture, interaction, feedback, states
- important technical choices
- what actually creates the quality difference
- trade-offs, hidden resources, and what should not be copied

Keep verified facts separate from inference. Interesting features do not become requirements automatically.

## 2. SYNTHESIZE — turn research into our own solution

Research is not the plan.

SYNTHESIZE must decide:

- what problem we are really solving
- what is confirmed vs assumed
- what to adopt / adapt / reject / park
- what real alternatives exist
- what solution we recommend and why
- what must be true for it to work
- what evidence would change the recommendation
- whether a low-cost validation is needed before planning

If one assumption could change the product direction or architecture, validate that assumption with the smallest reversible experiment instead of continuing to debate it.

## 3. DESIGN — make the chosen solution usable

Define:

- primary user and primary outcome
- core journey
- required screens/routes
- primary and secondary actions
- information hierarchy
- empty / loading / running / success / partial / error / disabled states
- persistence and refresh behavior
- recovery path
- clear next step
- responsive/accessibility expectations where relevant

The goal is to make the product understandable before implementation begins.

## 4. PLAN — create the complete execution contract

For a non-trivial new project or major redesign, generate the comprehensive project plan before BUILD.

The plan covers all applicable dimensions:

- product and scope
- frontend and UX-state contract
- backend/business rules
- data/source of truth
- AI/Agent boundaries
- security/privacy/permissions
- third-party dependencies
- engineering/module boundaries
- reliability/error semantics
- observability/diagnostics
- testing
- deployment/migration/rollback
- performance/cost where material
- Product Skeleton
- vertical slices
- front/back sync contract
- browser acceptance and final DONE definition

Irrelevant sections are marked `N/A` instead of filled with invented complexity.

Only `READY` or an explicitly accepted `READY WITH CONDITIONS` plan is frozen for implementation.

## 5. PRODUCT SKELETON — first execution stage

After the plan is frozen, build Slice 0 for a non-trivial new Web product or major UI redesign:

- core routes/screens
- real navigation
- primary actions
- representative states
- fixture/mock data where real capabilities are not wired yet
- responsive behavior where required

Then run a real browser / Playwright-equivalent Skeleton Gate.

This catches “the whole page/journey is wrong” before the backend becomes expensive to change.

## 6. BUILD — one vertical slice at a time

A valid slice crosses the full user-observable behavior:

`UI → interaction → backend → persistence → refresh truth → failure recovery`

Do not default to:

`all DB → all APIs → all agents → UI at the end`

Instead:

`frozen plan → Skeleton → browser gate → Slice 1 full stack → browser gate → Slice 2 ...`

## 7. Continuous execution — keep going without going horizontal

If the user asks the agent to “keep going” or finish autonomously, continue through already-approved slices without waiting for manual confirmation.

Autonomy does **not** allow:

- changing frozen scope silently
- finishing all backend layers before frontend
- skipping browser gates
- calling Backend PASS the same thing as product DONE

If a slice fails, fix the smallest blocking product issue, re-run acceptance, then continue.

## 8. Front/back sync contract

For every important user action, map:

| User action | Frontend expression | Backend effect | Persisted truth | Refresh/reopen truth |
|---|---|---|---|---|
| | | | | |

Every important backend state needs a useful UI expression. Every important UI state needs a real source of truth once wired to real data.

## 9. ACCEPT — real browser evidence

Verify from the actual user entry point:

1. user can find and understand the action
2. UI communicates what is happening
3. intended backend capability is really triggered
4. data is saved correctly
5. reload/reopen preserves correct state
6. failures are understandable and recoverable
7. next action is discoverable
8. frontend state matches business truth

Completion labels:

- `Backend PASS`
- `Frontend PASS`
- `Slice DONE` = both + real-browser acceptance
- `Project DONE` = frozen core journey passes full E2E

## 10. CHANGE — prevent silent scope drift

Every new idea after freeze is classified before implementation:

- `REQUIRED NOW`
- `VALUABLE NEXT`
- `PARK`
- `REPLACE`

Prefer substitution over accumulation.

## 11. AUDIT — repair product truth

For an existing project, start with the real user journey, not architecture aesthetics. Find where user-visible behavior diverges from backend capability, persisted state, security/permission truth, or the current product version.