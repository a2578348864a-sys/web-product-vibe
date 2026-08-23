# Implementation Slice

## Observable user outcome

## Entry point

## User actions

## Frontend changes

## Backend/data changes

## Persisted truth

## Refresh/reopen behavior

## Failure/recovery behavior

## Front/back sync contract

| User action | Frontend expression | Backend effect | Persisted truth | Refresh/reopen truth |
|---|---|---|---|---|
| | | | | |

## Out of scope

## Technical checks

### Backend PASS

- [ ] Required backend/business behavior is correct
- [ ] Relevant API/data behavior passes
- [ ] Relevant technical checks pass

### Frontend PASS

- [ ] Required page/interaction exists
- [ ] Empty/loading/success/error states are represented where relevant
- [ ] Navigation and next-step behavior are clear

## Real-browser acceptance

- [ ] User can find the action from a realistic entry point
- [ ] User can complete the intended action
- [ ] Visible feedback matches backend/business state
- [ ] Data is actually persisted where required
- [ ] Refresh/reopen remains correct
- [ ] Failure is understandable and recoverable
- [ ] Next step is discoverable
- [ ] Frontend and backend represent the same business semantics/version

## Final slice verdict

`Slice DONE` requires Backend PASS + Frontend PASS + real-browser acceptance for this same user-observable behavior.

PASS / CONDITIONAL PASS / FAIL / INSUFFICIENT EVIDENCE
