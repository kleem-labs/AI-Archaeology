# Excavation 123 — Federated Learning

[Previous: Excavation 122](../122-differential-privacy/README.md)

Can many devices train together without centralizing raw data?

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Upload every user record to one server.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Central collection increases privacy and governance risk.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Send model updates to devices, train locally, aggregate protected updates, and return a shared model.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

Phones compute keyboard gradients locally; the server receives an aggregate, not typed messages.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

Updates can still leak information and devices are unreliable or biased.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 124](../124-adversarial-robustness/README.md)
