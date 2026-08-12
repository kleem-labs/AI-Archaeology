# Excavation 064 — Observability — Seeing Why an Agent Failed

Multi-agent coordination divides work and introduces new boundaries, shared resources, and failure modes. When the result is wrong, the team needs enough trace to locate which assumption, handoff, or tool effect failed.

Using what we have, we log only the final response, or log every hidden detail without structure.

The world refuses to cooperate: the first gives no diagnosis; the second creates an unreadable, expensive, privacy-sensitive transcript.

Now we can see what is missing: we must record structured events for decisions, tool calls, state changes, costs, timing, evidence, and outcomes while redacting sensitive content.

## Let the case decide

A trace shows retrieval returned an outdated policy, the planner accepted it, and verification checked format but not date. The repair can now target the real failure.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## The boundary of the discovery

Logs describe what instrumentation captured. Missing fields, privacy limits, and misleading metrics still constrain diagnosis.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 065](../065-bounded-autonomy/README.md)
