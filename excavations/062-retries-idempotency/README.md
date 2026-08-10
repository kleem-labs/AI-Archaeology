# Excavation 062 — Retries and Idempotency — Trying Again Without Doing It Twice

[Previous: Excavation 061](../061-verification/README.md)

An agent sends a payment request, the network times out, and no response arrives. Did the payment fail, or did only the reply disappear?

Without knowing the inherited method, we might try this: Retry the action whenever a response is missing.

Its hidden assumption appears in the following case: The first payment succeeded and the retry charges the customer twice. Name the missing guarantee before continuing.

Remove that assumption and the needed repair becomes clear: Give each logical action a stable idempotency key, query existing state, and make repeated requests return the first result instead of repeating the effect.

## Now work a case you can see

Both payment attempts carry order-417. The server records that key with the first charge; the retry retrieves the same receipt rather than creating another charge.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## Where your new idea still breaks

Not every external operation supports idempotency. Agents need reconciliation and human escalation when outcome is ambiguous.

This is not an unrelated warning. The construction can give each logical action a stable idempotency key, query existing state, and make repeated requests return the first result instead of repeating the effect. It cannot infer or control information that never enters that construction.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 063](../063-multi-agent-coordination/README.md)
