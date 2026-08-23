# Comprehensive Project Plan

This document is the execution contract for a non-trivial Web project. Keep it complete enough to guide implementation, but mark irrelevant sections `N/A` instead of inventing complexity.

## 1. Executive summary

- Product:
- Primary user:
- Primary outcome:
- Recommended solution:
- Current version / milestone:
- Definition of success:

## 2. Decision basis

### Confirmed facts

### Interpretations

### Goals

### Constraints

### Unverified assumptions

| Assumption | Why it matters | Validation / owner | Blocking? |
|---|---|---|---|
| | | | |

## 3. Scope and boundaries

### In scope

### Supporting outcomes (max 2–3)

### Explicit non-goals

### Deferred / parking lot

### Removal candidates

## 4. Core user journey

`real entry → action → feedback → useful result → next step`

Reference the detailed user-journey spec if it exists.

## 5. Information architecture and screens

| Route / screen | Purpose | Entry | Primary action | Next step |
|---|---|---|---|---|
| | | | | |

## 6. Frontend plan

- Framework / existing patterns to reuse:
- Route/navigation structure:
- Main components and boundaries:
- State ownership:
- Data-fetch / mutation behavior:
- Empty / loading / running / success / partial / error / disabled states:
- Optimistic vs confirmed UI behavior:
- Refresh/reopen behavior:
- Responsive requirements:
- Accessibility requirements:
- Frontend failure/recovery behavior:

## 7. Backend plan

- Main services/modules:
- APIs/actions/workflows:
- Business rules:
- State-transition rules:
- Validation:
- Error semantics:
- Idempotency / concurrency requirements where applicable:
- Background jobs / queues where applicable:
- What is intentionally not abstracted:

## 8. Data and source-of-truth plan

| Business concept | Source of truth | Written by | Read by | User-visible meaning |
|---|---|---|---|---|
| | | | | |

- Schema changes:
- Data lifecycle / retention:
- Migration:
- Backup / restore:
- Seed / fixture strategy:
- Data consistency / conflict rules:

## 9. AI / Agent plan (N/A if not needed)

- What AI is allowed to decide:
- What AI must not decide:
- Model/provider:
- Inputs / context:
- Structured output / schema:
- Human review / confirmation points:
- Hallucination / uncertainty handling:
- Prompt-injection / untrusted-content boundary:
- Evaluation / quality gate:
- Cost / rate-limit strategy:
- Fallback behavior:

## 10. Security, privacy, and permissions

- Authentication:
- Authorization / role model:
- Secrets / environment variables:
- Sensitive data / PII:
- User input validation:
- File upload constraints:
- Remote URL / SSRF boundary:
- XSS / CSRF / injection concerns where applicable:
- AI prompt-injection / tool-permission concerns where applicable:
- Rate limiting / abuse controls:
- Auditability:

## 11. External dependencies

| Dependency | Why needed | Failure mode | Fallback / degradation | Lock-in / cost risk |
|---|---|---|---|---|
| | | | | |

## 12. Engineering and module boundaries

- Repository areas affected:
- Existing modules to reuse:
- New modules:
- Boundaries that must not be crossed:
- Configuration / environment strategy:
- Compatibility constraints:
- Technical debt explicitly accepted:

## 13. Reliability and failure semantics

- Expected failure classes:
- Retry rules:
- Partial-success behavior:
- Timeout / cancellation behavior:
- Duplicate-operation protection:
- Recovery path:
- What the user sees for each important failure:

## 14. Observability and diagnostics

- Required logs:
- Correlation / run IDs:
- Audit trail:
- Metrics:
- Error reporting:
- Read-only diagnostic commands / admin viewer for non-programmer inspection:

## 15. Testing strategy

### Unit / logic

### Integration / contract

### Data / migration

### Security / permission

### Browser / E2E

For Web/UI, real-browser acceptance is mandatory and cannot be replaced by API/tests/build.

## 16. Deployment and release

- Environments:
- Build / release path:
- Required config / secrets:
- Migration order:
- Smoke test:
- Rollback trigger:
- Rollback procedure:
- Backward compatibility:

## 17. Performance and cost budgets (N/A if immaterial)

- Latency target:
- Volume / scale assumption:
- AI/API cost budget:
- Browser automation / compute budget:
- Known bottleneck:

## 18. Product Skeleton (Slice 0)

Define the runnable UI shell to validate before substantial backend implementation.

- Required routes/screens:
- Required navigation:
- Representative fixture/mock states:
- Mobile/responsive expectations:
- Skeleton browser acceptance:

## 19. Vertical implementation slices

| Slice | Observable user outcome | Frontend | Backend/data | Failure/recovery | Browser gate |
|---|---|---|---|---|---|
| 0 | Product Skeleton | | | | |
| 1 | | | | | |
| 2 | | | | | |

Slices must be end-to-end user behaviors, not `DB first / API first / frontend last` technical layers.

## 20. Front/back sync contract

| User action | Frontend expression | Backend effect | Persisted truth | Refresh/reopen truth |
|---|---|---|---|---|
| | | | | |

## 21. Acceptance matrix

| User journey / requirement | Technical evidence | Browser evidence | Final criterion |
|---|---|---|---|
| | | | |

Completion labels:

- `Backend PASS`
- `Frontend PASS`
- `Slice DONE` = Backend PASS + Frontend PASS + real-browser acceptance
- `Project DONE` = frozen core journey passes full E2E

## 22. Main risks and exit conditions

| Risk | Probability / impact | Early warning | Mitigation | Kill / rollback condition |
|---|---|---|---|---|
| | | | | |

## 23. Readiness / freeze checklist

- [ ] Recommended solution is singular and explicit
- [ ] Facts, interpretations, constraints, and assumptions are separated
- [ ] Core user journey is complete
- [ ] Frontend states and navigation are specified
- [ ] Backend/business semantics are specified
- [ ] Data/source-of-truth semantics are clear
- [ ] AI boundaries are clear where applicable
- [ ] Security/privacy/permissions are covered where applicable
- [ ] External dependency failure boundaries are covered
- [ ] Testing and browser acceptance are defined
- [ ] Deployment/migration/rollback are defined where applicable
- [ ] Product Skeleton is defined
- [ ] Vertical slices are full-stack
- [ ] Non-goals are explicit
- [ ] Main risks and exit criteria are explicit

## 24. Final verdict

`READY / READY WITH CONDITIONS / NOT READY`

Conditions, if any:

Once frozen, implementation must follow this plan unless a change is explicitly accepted through CHANGE mode.