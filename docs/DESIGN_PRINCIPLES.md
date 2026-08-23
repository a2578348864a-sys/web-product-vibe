# Design Principles

## Product truth before technical truth

A technically valid system can still be a failed product. Architecture exists to support observable user outcomes, not the other way around.

## User journey before architecture

Do not begin a non-trivial Web project with database tables, APIs or agent topology unless the task is explicitly technical-only.

## GitHub is a solution library, not a requirements generator

Research broadly. Copy selectively. A borrowed idea must materially improve the current core journey or solve a real constraint.

## Scope must be explicit

A frozen version has a primary outcome and explicit non-goals. New ideas are evaluated through `CHANGE` instead of silently expanding scope.

## Vertical slices beat giant implementations

A small end-to-end slice is easier to verify, easier to roll back and exposes product mistakes earlier.

## Browser evidence is product evidence

Tests and APIs prove components. A browser journey proves that a user can actually complete the task.
