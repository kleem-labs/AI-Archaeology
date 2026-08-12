# Excavation 123 — Federated Learning

Differential privacy limits the observable influence of one record. Hospitals and devices may be unwilling or legally unable to centralize their raw data even when collective learning would help everyone.

At first we upload every user record to one server.

That confidence lasts only until central collection increases privacy and governance risk.

We need to send model updates to devices, train locally, aggregate protected updates, and return a shared model.

## Let the case decide

Phones compute keyboard gradients locally; the server receives an aggregate, not typed messages.

## The boundary of the discovery

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
