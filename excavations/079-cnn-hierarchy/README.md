# Excavation 079 — CNN Hierarchies

[Previous: Excavation 078](../078-pooling/README.md)

## Take the First Step Yourself

> **Your problem:** Edges are not yet eyes, stripes, or tigers.

> **Try your first idea:** Classify directly from isolated edge responses.

> **Now try to break your idea:** One edge has no object-level meaning.

> Stop here. State the missing requirement without naming the repair.

## The Observation

Edges are not yet eyes, stripes, or tigers.

## Your First Attempt

Classify directly from isolated edge responses.

## Break Your First Attempt

One edge has no object-level meaning.

## Repair Your Attempt

Stack local detectors so later layers combine earlier patterns over wider regions.

## What You Have Just Invented

**Stack local detectors so later layers combine earlier patterns over wider regions.**

## Rebuild the Discovery with a Concrete Case

Edges form corners; corners and textures form stripes; repeated stripes plus shape support tiger.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Real-World Limit

The hierarchy is learned, not guaranteed to match human parts.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 080](../080-vision-transformers/README.md)
