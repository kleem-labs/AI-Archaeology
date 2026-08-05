# Excavation 078 — Pooling — Keeping Evidence While Shrinking the Map

[Previous: Excavation 077](../077-convolution/README.md)

## Take the First Step Yourself

> **Your problem:** Local detectors create large activation maps.

> **Try your first idea:** Keep every activation at full resolution through every layer.

> **Now try to break your idea:** Memory explodes and tiny shifts move evidence to neighboring cells.

> Stop here. State the missing requirement without naming the repair.

## The Observation

Local detectors create large activation maps.

## Your First Attempt

Keep every activation at full resolution through every layer.

## Break Your First Attempt

Memory explodes and tiny shifts move evidence to neighboring cells.

## Repair Your Attempt

Summarize small neighborhoods while retaining the strongest or average evidence.

## What You Have Just Invented

**Summarize small neighborhoods while retaining the strongest or average evidence.**

## Rebuild the Discovery with a Concrete Case

Max pooling [1,7,2,3] keeps 7: an edge existed somewhere in that patch.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Real-World Limit

Pooling discards exact location and can erase subtle patterns.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 079](../079-cnn-hierarchy/README.md)
