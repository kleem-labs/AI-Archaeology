# Excavation 074 — Superposition

[Previous: Excavation 073](../073-attribution/README.md)

## Take the First Step Yourself

> **Your problem:** A network stores more useful features than it has individual neurons.

> **Try your first idea:** Demand one feature per coordinate.

> **Now try to break your idea:** Limited width forces useful patterns to share neurons, producing confusing mixed activations.

> Stop here. State the missing requirement without naming the repair.

## The Observation

A network stores more useful features than it has individual neurons.

## Your First Attempt

Demand one feature per coordinate.

## Break Your First Attempt

Limited width forces useful patterns to share neurons, producing confusing mixed activations.

## Repair Your Attempt

Represent features as directions that can overlap when they rarely need to be active together.

## What You Have Just Invented

**Represent features as directions that can overlap when they rarely need to be active together.**

## Rebuild the Discovery with a Concrete Case

One two-dimensional space stores several sparse directions; collisions occur mainly when multiple stored features activate together.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Real-World Limit

Separating superposed features is difficult and may not yield unique answers.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 075](../075-causal-interventions/README.md)
