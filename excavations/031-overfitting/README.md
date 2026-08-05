# Excavation 031 — Overfitting — When Perfect Memory Pretends to Be Intelligence

[Previous: Excavation 030](../030-activation-functions/README.md)

## Problem

A model scores perfectly on every training example, then fails on a new animal seen from a different angle.

## Naive Attempt

Celebrate zero training error. The model may have memorized scratches and shadows. Make the model infinitely flexible; it can store even more irrelevant detail.

## Why It Fails

Performance on remembered observations does not measure performance on unseen reality.

## Better Attempt

Reserve unseen cases and compare training success with performance outside the training memory.

## Why It Still Fails

The repair solves the immediate failure, but a gap diagnoses overfitting but does not identify its cause. Leakage, distribution shift, and noisy evaluation can mislead us.

## Key Insight

**Reserve unseen cases and compare training success with performance outside the training memory.**

## Mathematics Emerges

$$
\text{generalization gap}=L_{\text{unseen}}-L_{\text{train}}
$$

Every operation records a need established above; the equation is the fossil, not the living discovery.

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
