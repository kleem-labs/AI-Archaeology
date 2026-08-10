# Excavation 107 — Continual Learning

[Previous: Excavation 106](../106-catastrophic-forgetting/README.md)

A deployed learner faces a stream of changing tasks without clear boundaries.

Without knowing the inherited method, we might try this: Periodically retrain from scratch on everything.

Its hidden assumption appears in the following case: Storage and compute grow forever, and old raw data may be unavailable.

Remove that assumption and the needed repair becomes clear: Detect change, consolidate stable knowledge, adapt limited components, and evaluate past and present tasks together.

## Now work a case you can see

A seasonal model adapts its demand head while preserving reusable product representations.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

Stability and adaptability remain in tension.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 108](../108-meta-learning/README.md)
