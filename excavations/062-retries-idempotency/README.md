# Excavation 062 — Retries and Idempotency — Trying Again Without Doing It Twice

[Previous: Excavation 061](../061-verification/README.md)

## Take the First Step Yourself

> **Your problem:** An agent sends a payment request, the network times out, and no response arrives. Did the payment fail, or did only the reply disappear?

> **Try your first idea:** Retry the action whenever a response is missing.

> **Now try to break your idea:** The first payment succeeded and the retry charges the customer twice.

> Stop here. State what a repair must guarantee without using the chapter title.

## The Observation

An agent sends a payment request, the network times out, and no response arrives. Did the payment fail, or did only the reply disappear?

## Your First Attempt

Retry the action whenever a response is missing.

## Break Your First Attempt

The first payment succeeded and the retry charges the customer twice.

Name the missing guarantee before continuing.

## Repair Your Attempt

Give each logical action a stable idempotency key, query existing state, and make repeated requests return the first result instead of repeating the effect.

## What You Have Just Invented

**Give each logical action a stable idempotency key, query existing state, and make repeated requests return the first result instead of repeating the effect.**

## Rebuild the Discovery with a Concrete Case

Both payment attempts carry order-417. The server records that key with the first charge; the retry retrieves the same receipt rather than creating another charge.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## Real-World Limit

Not every external operation supports idempotency. Agents need reconciliation and human escalation when outcome is ambiguous.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 063](../063-multi-agent-coordination/README.md)
