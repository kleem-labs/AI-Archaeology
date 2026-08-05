# Excavation 096 — Distributed Training

[Previous: Excavation 095](../095-quantization/README.md)

## Take the First Step Yourself

> **Your problem:** One machine cannot hold the model, data, and optimizer state.

> **Try your first idea:** Let many machines train independent copies and combine them occasionally.

> **Now try to break your idea:** Their parameters drift and duplicated work wastes computation.

> Stop here. State the missing requirement without naming the repair.

## The Observation

One machine cannot hold the model, data, and optimizer state.

## Your First Attempt

Let many machines train independent copies and combine them occasionally.

## Break Your First Attempt

Their parameters drift and duplicated work wastes computation.

## Repair Your Attempt

Partition data or model work, synchronize required results, and preserve one coherent update.

## What You Have Just Invented

**Partition data or model work, synchronize required results, and preserve one coherent update.**

## Rebuild the Discovery with a Concrete Case

Two workers compute gradients on different batches, average them, then apply the same update.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Real-World Limit

Communication, failure recovery, and numerical nondeterminism become bottlenecks.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 097](../097-inference-serving/README.md)
