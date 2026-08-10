# Excavation 059 — Memory — What Should Survive After the Context Ends?

[Previous: Excavation 058](../058-planning/README.md)

An assistant learns the user’s preferred writing style today, but tomorrow the conversation window no longer contains it.

Our first construction is deliberately modest: Store every message forever and paste all history into every new prompt.

It works—right up to this boundary: Cost grows, irrelevant details drown current evidence, contradictions accumulate, and sensitive information persists without purpose. Name the missing guarantee before continuing.

Crossing that boundary requires one additional idea: Separate short-term working context from durable memory. Store only useful facts with source, time, scope, and a way to update or forget them.

## Now work a case you can see

Save “prefers concise status reports” with its source and date. Do not save a temporary hotel door code. Retrieve the preference only for relevant writing tasks.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## Where your new idea still breaks

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
