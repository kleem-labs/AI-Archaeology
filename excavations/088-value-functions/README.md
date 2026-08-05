# Excavation 088 — Value — Estimating Future Consequences

[Previous: Excavation 087](../087-states-actions-transitions/README.md)

## Take the First Step Yourself

> **Your problem:** Immediate reward cannot distinguish a step toward a distant goal from a dead end.

> **Try your first idea:** Choose the action with the largest reward right now.

> **Now try to break your idea:** A small immediate treat can prevent reaching a larger later reward.

> Stop here. State the missing requirement without naming the repair.

## The Observation

Immediate reward cannot distinguish a step toward a distant goal from a dead end.

## Your First Attempt

Choose the action with the largest reward right now.

## Break Your First Attempt

A small immediate treat can prevent reaching a larger later reward.

## Repair Your Attempt

Estimate the future reward expected from a state or state-action pair.

## What You Have Just Invented

**Estimate the future reward expected from a state or state-action pair.**

## Rebuild the Discovery with a Concrete Case

One path gives 1 now; another gives 0 now and 10 next. Future value makes the second preferable.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Real-World Limit

Value estimates inherit errors from limited experience.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 089](../089-q-learning/README.md)
