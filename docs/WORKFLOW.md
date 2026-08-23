# Workflow

Web Product Vibe uses a deliberately small product-development loop.

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

## 3. PLAN — freeze before building

Freeze:

- MVP
- non-goals
- assumptions
- acceptance criteria

Only then derive the minimum architecture and split work into vertical slices that each cross UI → backend → data → observable result.

## 4. BUILD — one slice at a time

A slice is not “build the backend first.” A valid slice should deliver a user-observable behavior end to end.

## 5. ACCEPT — real browser evidence

Verify from the actual user entry point. Confirm:

1. the user can find the action
2. the UI communicates what is happening
3. the backend capability is really triggered
4. data is saved correctly
5. reload preserves the correct state
6. failures are understandable and recoverable
7. the next action is discoverable
8. frontend state matches business truth

## 6. CHANGE — prevent silent scope drift

Every new idea is classified before implementation:

- `REQUIRED NOW`
- `VALUABLE NEXT`
- `PARK`
- `REPLACE`

## 7. AUDIT — repair product truth

For an existing project, start with the real journey, not architecture aesthetics. Find where user-visible behavior diverges from backend capability or persisted state.
