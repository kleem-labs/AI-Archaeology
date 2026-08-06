# Excavation 114 — Model-Based Planning

[Previous: Excavation 113](../113-counterfactuals/README.md)

## Take the First Step Yourself

> **Your problem:** A world model can predict one step. How should the agent choose a long action sequence?

> **Try your first idea:** Commit to the first sequence imagined.

> **Now try to break your idea:** One forecast may exploit model error or miss better branches.

> Stop here. State the missing requirement without naming the repair.

## The Observation

A world model can predict one step. How should the agent choose a long action sequence?

## Your First Attempt

Commit to the first sequence imagined.

## Break Your First Attempt

One forecast may exploit model error or miss better branches.

## Repair Your Attempt

Simulate multiple candidate sequences, score outcomes, act briefly, observe reality, and plan again.

## What You Have Just Invented

**Simulate multiple candidate sequences, score outcomes, act briefly, observe reality, and plan again.**

## Rebuild the Discovery with a Concrete Case

A robot simulates left-right paths, takes one safe step, then updates after detecting an obstacle.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Real-World Limit

Planning cost grows with horizon and branching.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 115](../115-tree-search/README.md)
