# Product Skeleton

The Product Skeleton is **Slice 0** for non-trivial new Web products and major UI redesigns.

Its purpose is to validate the product structure before substantial backend implementation. It is not a fake DONE state and it does not need real business data yet.

## Goal

Make the complete core journey visible and navigable early enough to catch product mistakes cheaply.

## Core journey shell

Describe the primary journey in one line:

`entry → screen/action → screen/action → useful outcome → next step`

## Required screens / routes

| Screen / route | Purpose | Entry | Primary action | Next step |
|---|---|---|---|---|
| | | | | |

## Required UI states

For each important screen, cover the states that affect understanding:

- empty
- loading / running
- mock success / representative result
- error
- partial / blocked where relevant
- disabled where relevant

## Fixture / mock contract

Fixtures or mock data are allowed only to validate product structure and interaction before the real backend is wired.

Record:

- what is mocked
- what behavior is representative only
- what must become real in later vertical slices
- what must never be presented as production truth

## Real-browser Skeleton Gate

- [ ] All core routes/screens render
- [ ] A first-time user can identify the primary action quickly
- [ ] The complete core journey is clickable end to end
- [ ] Primary actions produce visible feedback, even if fixture-backed
- [ ] Navigation/back/next-step behavior is understandable
- [ ] Core empty/loading/success/error states can be inspected
- [ ] Responsive behavior is acceptable where required
- [ ] No blocking browser-console errors
- [ ] Screenshots, trace, video, or equivalent browser evidence exists

## Non-goals

- Real backend completion
- Full database integration
- Production AI/provider integration
- Performance tuning
- Final visual polish unless it affects usability

## Gate verdict

`PASS / CONDITIONAL PASS / FAIL / INSUFFICIENT EVIDENCE`

Substantial backend implementation must not begin for a non-trivial new UI or major redesign until this gate is at least `CONDITIONAL PASS` with explicit conditions.