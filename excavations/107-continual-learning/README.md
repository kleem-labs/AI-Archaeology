# Excavation 107 — Continual Learning

[Previous: Excavation 106](../106-catastrophic-forgetting/README.md)

## Take the First Step Yourself

> **Your problem:** A deployed learner faces a stream of changing tasks without clear boundaries.

> **Try your first idea:** Periodically retrain from scratch on everything.

> **Now try to break your idea:** Storage and compute grow forever, and old raw data may be unavailable.

> Stop here. State the missing requirement without naming the repair.

## The Observation

A deployed learner faces a stream of changing tasks without clear boundaries.

## Your First Attempt

Periodically retrain from scratch on everything.

## Break Your First Attempt

Storage and compute grow forever, and old raw data may be unavailable.

## Repair Your Attempt

Detect change, consolidate stable knowledge, adapt limited components, and evaluate past and present tasks together.

## What You Have Just Invented

**Detect change, consolidate stable knowledge, adapt limited components, and evaluate past and present tasks together.**

## Rebuild the Discovery with a Concrete Case

A seasonal model adapts its demand head while preserving reusable product representations.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Real-World Limit

Stability and adaptability remain in tension.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 108](../108-meta-learning/README.md)
