# Excavation 070 — Bandits — Learning While Choosing

[Previous: Excavation 069](../069-controlled-experiments/README.md)

## Take the First Step Yourself

> **Your problem:** An agent must choose recommendations while still learning which are useful.

> **Try your first idea:** Always choose the currently best option.

> **Now try to break your idea:** An unlucky first result permanently hides a better alternative.

> Stop here. State the missing requirement without naming the repair.

## The Observation

An agent must choose recommendations while still learning which are useful.

## Your First Attempt

Always choose the currently best option.

## Break Your First Attempt

An unlucky first result permanently hides a better alternative.

## Repair Your Attempt

Reserve some choices for exploration while exploiting accumulated evidence.

## What You Have Just Invented

**Reserve some choices for exploration while exploiting accumulated evidence.**

## Rebuild the Discovery with a Concrete Case

Cafe A wins its first two trials; continuing to sample B reveals it succeeds eight out of ten times.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Real-World Limit

Exploration has real cost and can be unacceptable for high-risk actions.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 071](../071-features-inside-networks/README.md)
