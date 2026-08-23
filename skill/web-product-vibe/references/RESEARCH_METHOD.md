# Comparable Project Research Method

Use comparable projects to learn patterns and trade-offs, not to accumulate features.

## 1. Set the research frame

Before searching, define:

- target problem / product category
- current date or historical cutoff
- what decision the research must inform
- comparison dimensions
- what counts as “enough evidence to move on”

Do not research indefinitely. The purpose is to improve a product decision.

## 2. Search portfolio

Aim for a small diverse set, usually 4–8 references:

- 1–2 established/high-adoption projects
- 1–2 actively maintained modern projects
- 1–2 UX/product-oriented examples
- 1–2 technically different alternatives

Prefer primary sources, recent maintenance, real product/UI evidence, and genuinely different approaches rather than clones.

Star count is a signal, not proof of fit or quality.

## 3. Evidence discipline

For time-sensitive claims, verify current facts when tools allow it.

Keep these distinct:

- verified fact
- inference from evidence
- project/author claim
- opinion/value judgment
- unknown / not verified

The strength of a recommendation must not exceed the evidence supporting it.

## 4. Reverse-engineer each reference

Do not stop at “what features does it have?”. For each project record:

| Layer | Questions |
|---|---|
| Product | Who is it for? What job does it solve? What is success? |
| Journey | Entry → action → feedback → result → next step |
| UX/UI | Navigation, hierarchy, states, feedback, recovery, persistence |
| Quality difference | Which choices actually make it easier, faster, safer, or clearer? |
| Technical | Stack, data flow, source of truth, architecture choices worth understanding |
| Trade-offs | Complexity, assumptions, limitations, hidden resources, what not to copy |

Also ask:

- Which principle is transferable?
- Which detail only works because of that project’s scale, brand, data, team, or infrastructure?
- What failure path is not visible from the happy-path demo?

## 5. Compare on common dimensions

Do not compare projects using different criteria for each one. Use the same dimensions where possible:

- target user
- value proposition
- shortest path to value
- UX complexity
- technical complexity
- data requirements
- AI/automation dependence
- security/permission burden
- maintenance burden
- cost / infrastructure
- distinctive strength
- important weakness

Explain why the projects are actually comparable.

## 6. Adoption gate

A reference pattern may be adopted only when all are true:

1. It maps to a real problem in our target journey.
2. The problem is current, not hypothetical.
3. Existing behavior cannot solve it adequately.
4. No materially simpler solution exists.
5. Added UI/state/data/security/maintenance/testing complexity is acceptable.

Otherwise mark it `REJECT` or `PARK` during SYNTHESIZE.

## 7. Hand-off to SYNTHESIZE

DISCOVER should end with research findings, not an implementation plan.

Pass forward:

- confirmed findings
- useful transferable principles
- conflicting approaches
- important unknowns
- candidate ideas to adopt/adapt/reject/park

SYNTHESIZE then decides our solution.

## Anti-patterns

- Star count as proof of product fit
- Copying architecture without copying the problem
- Treating a backend library as a full product reference
- Adding AI/Agent/RAG/MCP because it is fashionable
- Copying enterprise complexity into an MVP
- Ignoring UI because the reference repository is code-heavy
- Repeating README marketing claims as verified facts
- Turning research notes directly into scope without a synthesis decision