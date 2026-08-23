# Workflow

Web Product Vibe uses a product-first loop that can run autonomously without drifting into backend-first development.

## 1. DISCOVER — research before commitment

Start from a rough intent. Research comparable products and GitHub projects, preferring active maintenance, meaningful adoption, recent approaches, and real UI evidence. Extract:

- target user and job
- entry → action → result → next step
- navigation, hierarchy and state feedback
- technical choices
- trade-offs and things not worth copying

Interesting features do not become requirements automatically.

## 2. DESIGN — make the product understandable

Before architecture, define:

- primary user
- primary user outcome
- core journey
- required screens
- primary / secondary actions
- empty / loading / success / error / partial states
- persistence and refresh behavior
- recovery path
- clear next step

## 3. PRODUCT SKELETON — validate the product before heavy backend work

For a non-trivial new Web product or major UI redesign, build a runnable UI shell first:

- core routes/screens
- real navigation
- primary actions
- representative states
- fixture/mock data where necessary
- responsive behavior where required

Then run a real browser / Playwright-equivalent Skeleton Gate.

The goal is to catch “the whole page/journey is wrong” before the database, APIs, and agents are heavily implemented.

## 4. PLAN — freeze before building

Freeze:

- MVP
- non-goals
- assumptions
- acceptance criteria

Only then derive the minimum architecture and split work into vertical slices.

## 5. BUILD — one vertical slice at a time

A valid slice crosses the whole user-observable behavior:

`UI → interaction → backend → persistence → refresh truth → failure recovery`

Do not use this default sequence for interactive Web work:

`all DB → all APIs → all agents → UI at the end`

Instead use:

`Skeleton → Slice 1 full stack → browser gate → Slice 2 full stack → browser gate → ...`

## 6. Continuous execution — keep going without going horizontal

If the user says “do not stop” or asks for autonomous completion, continue through already-approved slices without waiting for manual confirmation.

But autonomy does **not** allow:

- finishing all backend layers before the frontend
- skipping browser gates
- changing frozen scope silently
- calling Backend PASS the same thing as product DONE

If a slice fails, fix the smallest blocking product issue, re-run its browser acceptance, then continue.

## 7. Front/back sync contract

For every important user action, map:

| User action | Frontend expression | Backend effect | Persisted truth | Refresh/reopen truth |
|---|---|---|---|---|
| | | | | |

Every important backend state needs an understandable UI expression. Every important UI state needs a real source of truth once the slice is wired to real data.

## 8. ACCEPT — real browser evidence

Verify from the actual user entry point. Confirm:

1. the user can find the action
2. the UI communicates what is happening
3. the backend capability is really triggered
4. data is saved correctly
5. reload preserves the correct state
6. failures are understandable and recoverable
7. the next action is discoverable
8. frontend state matches business truth

Completion labels:

- `Backend PASS`: backend/data/business logic is correct
- `Frontend PASS`: page/interaction/state behavior exists
- `Slice DONE`: Backend PASS + Frontend PASS + real-browser product acceptance

## 9. CHANGE — prevent silent scope drift

Every new idea is classified before implementation:

- `REQUIRED NOW`
- `VALUABLE NEXT`
- `PARK`
- `REPLACE`

## 10. AUDIT — repair product truth

For an existing project, start with the real journey, not architecture aesthetics. Find where user-visible behavior diverges from backend capability or persisted state, especially when the backend has moved to a new version while the UI still expresses the old one.
