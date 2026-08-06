# Excavation 108 — Meta-Learning

[Previous: Excavation 107](../107-continual-learning/README.md)

## Take the First Step Yourself

> **Your problem:** Can experience across many tasks teach the model how to learn a new task quickly?

> **Try your first idea:** Train one universal fixed solution.

> **Now try to break your idea:** A new task with different labels requires many examples and broad retraining.

> Stop here. State the missing requirement without naming the repair.

## The Observation

Can experience across many tasks teach the model how to learn a new task quickly?

## Your First Attempt

Train one universal fixed solution.

## Break Your First Attempt

A new task with different labels requires many examples and broad retraining.

## Repair Your Attempt

Optimize prior parameters or an update rule so a few new examples produce useful adaptation.

## What You Have Just Invented

**Optimize prior parameters or an update rule so a few new examples produce useful adaptation.**

## Rebuild the Discovery with a Concrete Case

After many two-class tasks, five labeled examples are enough to separate two unseen animal species.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Real-World Limit

Task distributions can be narrow and meta-learning can overfit them.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 109](../109-curriculum-learning/README.md)
