# Excavation 105 — Selective Prediction

[Previous: Excavation 104](../104-active-learning/README.md)

## Take the First Step Yourself

> **Your problem:** Must the model answer every question, even when evidence is weak?

> **Try your first idea:** Always return the highest-scoring answer.

> **Now try to break your idea:** A forced answer converts uncertainty into confident-looking error.

> Stop here. State the missing requirement without naming the repair.

## The Observation

Must the model answer every question, even when evidence is weak?

## Your First Attempt

Always return the highest-scoring answer.

## Break Your First Attempt

A forced answer converts uncertainty into confident-looking error.

## Repair Your Attempt

Allow abstention and choose a coverage level whose retained answers meet a risk target.

## What You Have Just Invented

**Allow abstention and choose a coverage level whose retained answers meet a risk target.**

## Rebuild the Discovery with a Concrete Case

The system answers 80 of 100 cases and is correct on 78; the other 20 go to a human rather than becoming guesses.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Real-World Limit

Abstention shifts work and may fail unevenly across groups.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 106](../106-catastrophic-forgetting/README.md)
