# Excavation 059 — Memory — What Should Survive After the Context Ends?

[Previous: Excavation 058](../058-planning/README.md)

## Take the First Step Yourself

> **Your problem:** An assistant learns the user’s preferred writing style today, but tomorrow the conversation window no longer contains it.

> **Try your first idea:** Store every message forever and paste all history into every new prompt.

> **Now try to break your idea:** Cost grows, irrelevant details drown current evidence, contradictions accumulate, and sensitive information persists without purpose.

> Stop here. State what a repair must guarantee without using the chapter title.

## The Observation

An assistant learns the user’s preferred writing style today, but tomorrow the conversation window no longer contains it.

## Your First Attempt

Store every message forever and paste all history into every new prompt.

## Break Your First Attempt

Cost grows, irrelevant details drown current evidence, contradictions accumulate, and sensitive information persists without purpose.

Name the missing guarantee before continuing.

## Repair Your Attempt

Separate short-term working context from durable memory. Store only useful facts with source, time, scope, and a way to update or forget them.

## What You Have Just Invented

**Separate short-term working context from durable memory. Store only useful facts with source, time, scope, and a way to update or forget them.**

## Rebuild the Discovery with a Concrete Case

Save “prefers concise status reports” with its source and date. Do not save a temporary hotel door code. Retrieve the preference only for relevant writing tasks.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## Real-World Limit

Remembered facts can become stale or wrong. Memory needs consent, provenance, expiration, correction, and deletion.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 060](../060-state-machines/README.md)
