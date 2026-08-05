# Excavation 035 — A Tiny Neural Network — Assemble the Entire Learning Loop

[Previous: Excavation 034](../034-generalization/README.md)

## Problem

We have excavated features, transformations, nonlinear gates, loss, gradients, batches, and validation separately. A pile of correct parts still does not learn.

## Naive Attempt

Hide everything behind a framework call. The code runs, but the causal chain disappears. Hand-tune outputs without gradients; every new example breaks the tuning.

## Why It Fails

Understanding becomes operational only when one example can travel forward, create loss, send blame backward, and update the same weights.

## Better Attempt

Build a two-layer network, cache its intermediate values, backpropagate every derivative, update on batches, and evaluate on unseen data.

## Why It Still Fails

The repair solves the immediate failure, but a tiny network exposes mechanics but is not yet a language model. The next arc must turn sequences into a trained generative system.

## Key Insight

**Build a two-layer network, cache its intermediate values, backpropagate every derivative, update on batches, and evaluate on unseen data.**

## Mathematics Emerges

$$
x\to Wx+b\to\phi(\cdot)\to\hat y\to L\to\nabla_\theta L\to\theta^\prime
$$

Every operation records a need established above; the equation is the fossil, not the living discovery.

## Real-World Analogy

An engine is understood when fuel, ignition, motion, exhaust, and feedback operate together—not when its parts lie labeled on a table.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Exercises

Use the [invention challenges](exercises.md).

## Connections

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)
