# Excavation 123 — Federated Learning

[Previous: Excavation 122](../122-differential-privacy/README.md)

Can many devices train together without centralizing raw data?

At first, the simplest answer is tempting: Upload every user record to one server.

But the simplicity has discarded something important: Central collection increases privacy and governance risk.

The missing information determines the next move: Send model updates to devices, train locally, aggregate protected updates, and return a shared model.

## Now work a case you can see

Phones compute keyboard gradients locally; the server receives an aggregate, not typed messages.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

Updates can still leak information and devices are unreliable or biased.

The reason is visible in the procedure. It knows how to send model updates to devices, train locally, aggregate protected updates, and return a shared model. The limitation above asks for another judgment, and no part of the procedure makes that judgment.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 124](../124-adversarial-robustness/README.md)
