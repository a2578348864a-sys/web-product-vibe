# Comparable Project Research Method

Use comparable projects to learn patterns, not to accumulate features.

## Search portfolio

Aim for a small diverse set, usually 4–8 references:

- 1–2 established/high-adoption projects
- 1–2 actively maintained modern projects
- 1–2 UX/product-oriented examples
- 1–2 technically different alternatives

Prefer recent maintenance and primary sources.

## Extraction matrix

For each project record:

| Layer | Questions |
|---|---|
| Product | Who is it for? What job does it solve? Why use it? |
| Journey | What is the first action? What is the shortest path to value? |
| UX/UI | Navigation, hierarchy, states, feedback, recovery, next step |
| Technical | Stack, data flow, architecture choices worth understanding |
| Trade-offs | Complexity, assumptions, limitations, what not to copy |

## Adoption gate

A reference pattern may be adopted only when all are true:

1. It maps to a real problem in our target journey.
2. The problem is current, not hypothetical.
3. Existing behavior cannot solve it adequately.
4. No materially simpler solution exists.
5. Added product/maintenance complexity is acceptable.

Otherwise record it in PARKING_LOT.md.

## Anti-patterns

- Star count as proof of product fit
- Copying architecture without copying the problem
- Treating a backend library as a full product reference
- Adding an AI/Agent/RAG/MCP feature because it is fashionable
- Copying enterprise complexity into an MVP
- Ignoring UI because the reference repository is code-heavy
