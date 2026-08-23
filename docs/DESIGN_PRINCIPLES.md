# Design Principles

## Product truth before technical truth

A technically valid system can still be a failed product. Architecture exists to support observable user outcomes, not the other way around.

## User journey before architecture

Do not begin a non-trivial Web project with database tables, APIs or agent topology unless the task is explicitly technical-only.

## Product Skeleton before heavy implementation

For new Web products and major redesigns, validate the runnable product shell before substantial backend work. Core routes, navigation, primary actions and representative UI states should be visible in a real browser early.

The Product Skeleton is not fake completion. It is an early product-structure gate that makes wrong UX cheap to change.

## GitHub is a solution library, not a requirements generator

Research broadly. Copy selectively. A borrowed idea must materially improve the current core journey or solve a real constraint.

## Scope must be explicit

A frozen version has a primary outcome and explicit non-goals. New ideas are evaluated through `CHANGE` instead of silently expanding scope.

## Vertical slices beat horizontal layers

For interactive Web work, avoid the default sequence `all database → all APIs → all agents → frontend later`.

Prefer `UI + interaction + backend + persistence + browser acceptance` for one user-observable slice at a time.

This keeps the frontend and backend on the same product version.

## Continuous execution must preserve gates

An autonomous agent may continue through the approved plan without waiting for a human between slices, but it must not skip Product Skeleton or browser gates, silently expand scope, or push all frontend work to the end.

“Do not stop” means **continue the validated sequence**, not **abandon the product sequence**.

## Frontend and backend need one shared truth

Every important backend state needs an understandable frontend expression. Every important UI state needs a real source of truth once wired to real data.

A backend can be correct while the product is still wrong if the UI represents an older workflow or stale business semantics.

## Three levels of completion

- `Backend PASS`: backend/data/business logic is correct
- `Frontend PASS`: required page/interaction/state behavior exists
- `Slice DONE`: Backend PASS + Frontend PASS + real-browser user-journey acceptance

Do not collapse these labels.

## Browser evidence is product evidence

Tests and APIs prove components. A browser journey proves that a user can actually complete the task.
