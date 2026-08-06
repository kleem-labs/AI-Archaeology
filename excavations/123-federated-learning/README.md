# Excavation 123 — Federated Learning

[Previous: Excavation 122](../122-differential-privacy/README.md)

## Take the First Step Yourself

> **Your problem:** Can many devices train together without centralizing raw data?

> **Try your first idea:** Upload every user record to one server.

> **Now try to break your idea:** Central collection increases privacy and governance risk.

> Stop here. State the missing requirement without naming the repair.

## The Observation

Can many devices train together without centralizing raw data?

## Your First Attempt

Upload every user record to one server.

## Break Your First Attempt

Central collection increases privacy and governance risk.

## Repair Your Attempt

Send model updates to devices, train locally, aggregate protected updates, and return a shared model.

## What You Have Just Invented

**Send model updates to devices, train locally, aggregate protected updates, and return a shared model.**

## Rebuild the Discovery with a Concrete Case

Phones compute keyboard gradients locally; the server receives an aggregate, not typed messages.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Real-World Limit

Updates can still leak information and devices are unreliable or biased.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 124](../124-adversarial-robustness/README.md)
