# Excavation 062 — Retries and Idempotency — Trying Again Without Doing It Twice

[Previous: Excavation 061](../061-verification/README.md)

An agent sends a payment request, the network times out, and no response arrives. Did the payment fail, or did only the reply disappear?

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Retry the action whenever a response is missing.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* The first payment succeeded and the retry charges the customer twice.

Name the missing guarantee before continuing.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Give each logical action a stable idempotency key, query existing state, and make repeated requests return the first result instead of repeating the effect.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

Both payment attempts carry order-417. The server records that key with the first charge; the retry retrieves the same receipt rather than creating another charge.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## Where your new idea still breaks

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
