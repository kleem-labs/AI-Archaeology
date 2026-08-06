# Excavation 103 — Ensembles

[Previous: Excavation 102](../102-bayesian-updating/README.md)

## Take the First Step Yourself

> **Your problem:** One trained model gives a confident answer. Would another equally trained model agree?

> **Try your first idea:** Trust one training run as the unique learned truth.

> **Now try to break your idea:** Different initialization and data order produce different boundaries.

> Stop here. State the missing requirement without naming the repair.

## The Observation

One trained model gives a confident answer. Would another equally trained model agree?

## Your First Attempt

Trust one training run as the unique learned truth.

## Break Your First Attempt

Different initialization and data order produce different boundaries.

## Repair Your Attempt

Train several diverse models and combine predictions while inspecting disagreement.

## What You Have Just Invented

**Train several diverse models and combine predictions while inspecting disagreement.**

## Rebuild the Discovery with a Concrete Case

Five models vote tiger probabilities .9,.85,.88,.3,.25; the average is moderate and disagreement warns of model uncertainty.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Real-World Limit

Ensembles cost more and shared data can produce shared mistakes.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 104](../104-active-learning/README.md)
