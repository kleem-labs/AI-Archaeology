# Excavation 059 — Memory — What Should Survive After the Context Ends?

Planning turns a goal into steps the agent can inspect and revise. A plan that outlives the current context needs selected facts and decisions to survive without preserving every irrelevant token forever.

An obvious shortcut is to store every message forever and paste all history into every new prompt.

The world refuses to cooperate: cost grows, irrelevant details drown current evidence, contradictions accumulate, and sensitive information persists without purpose.

We need to separate short-term working context from durable memory. Store only useful facts with source, time, scope, and a way to update or forget them.

## Let the case decide

Save “prefers concise status reports” with its source and date. Do not save a temporary hotel door code. Retrieve the preference only for relevant writing tasks.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## The boundary of the discovery

Remembered facts can become stale or wrong. Memory needs consent, provenance, expiration, correction, and deletion.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 060](../060-state-machines/README.md)
