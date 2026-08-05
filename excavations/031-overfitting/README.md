# Excavation 031 — Overfitting — When Perfect Memory Pretends to Be Intelligence

[Previous: Excavation 030](../030-activation-functions/README.md)


## Take the First Step Yourself

> **Your problem:** A model scores perfectly on every training example, then fails on a new animal seen from a different angle.

> **Try your first idea:** Celebrate zero training error. The model may have memorized scratches and shadows. Make the model infinitely flexible; it can store even more irrelevant detail.

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

## Problem

A model scores perfectly on every training example, then fails on a new animal seen from a different angle.

## Your First Attempt

Celebrate zero training error. The model may have memorized scratches and shadows. Make the model infinitely flexible; it can store even more irrelevant detail.

## Break Your First Attempt

Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Celebrate zero training error. The model may have memorized scratches and shadows. Make the model infinitely flexible; it can store even more irrelevant detail.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

## Repair Your Attempt

Reserve unseen cases and compare training success with performance outside the training memory.

## Why It Still Fails

The repair solves the immediate failure, but a gap diagnoses overfitting but does not identify its cause. Leakage, distribution shift, and noisy evaluation can mislead us.

## What You Have Just Invented

**Reserve unseen cases and compare training success with performance outside the training memory.**

## Only Now Give the Discovery a Mathematical Name

## Build Every Piece from the Concrete Example

A model has training loss 0.02 and unseen loss 0.17. Subtracting gives a gap of 0.15. The low training number shows memory; the gap measures how much success disappeared outside it.

### Give Short Names Only After We Know the Pieces

- **L_train** measures error on examples allowed to shape the model.
- **L_unseen** measures error on held-out observations.
- Subtraction isolates deterioration outside memory instead of confusing it with absolute task difficulty.
- A positive generalization gap is evidence that training success did not fully survive.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
\text{generalization gap}=L_{\text{unseen}}-L_{\text{train}}
$$


## Real-World Analogy

A student who memorizes answer positions can ace the practice sheet and fail when the same ideas are rearranged.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Exercises

Use the [invention challenges](exercises.md).

## Connections

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 032](../032-regularization/README.md)
