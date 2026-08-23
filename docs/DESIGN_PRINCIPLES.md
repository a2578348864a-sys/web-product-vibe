# Design Principles

## Product truth before technical truth

A technically valid system can still be a failed product. Architecture exists to support observable user outcomes, not the other way around.

## Facts, interpretations, goals, constraints, and assumptions are different things

Do not let an attractive interpretation become a requirement. Confirmed facts should be traceable; assumptions should remain visible until they are validated or consciously accepted.

## Research is not a decision

Comparable projects are solution libraries. Research should reveal patterns, trade-offs and failure modes, but must end in a synthesized recommendation for this product rather than a pile of borrowed features.

## Only ask questions that can change the path

Do not stall the user with exhaustive questionnaires. If the missing answer would not materially change the product direction, state the assumption and proceed.

## Prefer decisive reality checks over more discussion

When one unresolved assumption could change feasibility, architecture, cost, or product direction, validate it with the lowest-cost reversible test that can produce real feedback.

## User journey before architecture

Do not begin a non-trivial Web project with database tables, APIs, or agent topology unless the task is explicitly technical-only.

## The project plan is an execution contract, not a backend document

For a non-trivial project, the frozen plan must cover all applicable product, frontend, backend, data, AI, security, engineering, testing, deployment, rollback, and acceptance concerns. Mark irrelevant dimensions `N/A` instead of ignoring them or inventing complexity.

## Product Skeleton before heavy backend implementation

After the plan is frozen, validate the planned journey through a runnable UI shell before expensive backend work makes product mistakes harder to change.

## Vertical slices beat horizontal completion

A valid implementation slice delivers one user-observable behavior across frontend, backend, persistence, recovery, and browser acceptance. “All backend first, UI later” is not the default for interactive Web work.

## Scope must be explicit

A frozen version has one primary outcome and explicit non-goals. New ideas are evaluated through `CHANGE` instead of silently expanding scope.

## Browser evidence is product evidence

Tests and APIs prove components. A browser journey proves that a user can actually complete the task. Web/UI work without real-browser evidence is not DONE.

## Stop when the goal is achieved

Once the frozen user goal passes end-to-end acceptance, stop optimizing. Do not turn a successful small product into a framework just because more abstractions are possible.