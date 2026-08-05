# Excavation 069 — Controlled Experiments

[Previous: Excavation 068](../068-distribution-drift/README.md)

## Take the First Step Yourself

> **Your problem:** A new model performs better after launch, but traffic and season also changed.

> **Try your first idea:** Compare this week with last week.

> **Now try to break your idea:** A holiday raises sales for both systems and receives credit as a model improvement.

> Stop here. State the missing requirement without naming the repair.

## The Observation

A new model performs better after launch, but traffic and season also changed.

## Your First Attempt

Compare this week with last week.

## Break Your First Attempt

A holiday raises sales for both systems and receives credit as a model improvement.

## Repair Your Attempt

Randomly assign comparable cases to old and new behavior and compare predefined outcomes.

## What You Have Just Invented

**Randomly assign comparable cases to old and new behavior and compare predefined outcomes.**

## Rebuild the Discovery with a Concrete Case

Split 10,000 simultaneous visitors evenly; conversion is 5% for control and 5.5% for treatment under the same week.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Real-World Limit

Experiments require sufficient samples, ethical limits, and careful metrics.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 070](../070-bandits/README.md)
