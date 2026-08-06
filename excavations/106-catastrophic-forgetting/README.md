# Excavation 106 — Catastrophic Forgetting

[Previous: Excavation 105](../105-selective-prediction/README.md)

## Take the First Step Yourself

> **Your problem:** After learning task B, the model suddenly fails task A.

> **Try your first idea:** Fine-tune only on the newest data.

> **Now try to break your idea:** Updates useful for B overwrite weights carrying A.

> Stop here. State the missing requirement without naming the repair.

## The Observation

After learning task B, the model suddenly fails task A.

## Your First Attempt

Fine-tune only on the newest data.

## Break Your First Attempt

Updates useful for B overwrite weights carrying A.

## Repair Your Attempt

Rehearse old evidence, protect important parameters, or allocate new capacity.

## What You Have Just Invented

**Rehearse old evidence, protect important parameters, or allocate new capacity.**

## Rebuild the Discovery with a Concrete Case

Learning birds after mammals drops mammal accuracy; mixing a small mammal replay set preserves both.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Real-World Limit

Memory, privacy, and capacity limit rehearsal.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 107](../107-continual-learning/README.md)
