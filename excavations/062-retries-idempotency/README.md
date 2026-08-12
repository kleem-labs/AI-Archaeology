# Excavation 062 — Retries and Idempotency — Trying Again Without Doing It Twice

Verification compares the intended effect with reality. When the evidence is absent because a request timed out, trying again may repeat an action that actually succeeded the first time.

One tempting answer is to retry the action whenever a response is missing.

The trouble appears immediately: the first payment succeeded and the retry charges the customer twice.

So we give each logical action a stable idempotency key, query existing state, and make repeated requests return the first result instead of repeating the effect.

## Let the case decide

Both payment attempts carry order-417. The server records that key with the first charge; the retry retrieves the same receipt rather than creating another charge.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## The boundary of the discovery

Not every external operation supports idempotency. Agents need reconciliation and human escalation when outcome is ambiguous.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 063](../063-multi-agent-coordination/README.md)
