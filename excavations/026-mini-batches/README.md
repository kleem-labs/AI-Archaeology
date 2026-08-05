# Excavation 026 — Mini-Batches — Learning from More Than One Example

[Previous: Excavation 025](../025-gradient-descent/README.md)

## Problem

A hunter updates the danger rule after every single footprint. One muddy print says “tiger”; the next says “deer.” The rule jerks back and forth.

## Naive Attempt

Use one example per update. It is fast, but noisy accidents dominate. Use every observation before each update. It is stable, but painfully slow and cannot react until the whole archive is read.

## Why It Fails

A single example is too noisy; the entire archive is too expensive.

## Better Attempt

Average the evidence from a small group. Each batch is large enough to soften accidents and small enough to update frequently.

## Why It Still Fails

The repair solves the immediate failure, but batch gradients are still estimates. Batch size changes noise, memory use, and sometimes what kind of solution training finds.

## Key Insight

**Average the evidence from a small group. Each batch is large enough to soften accidents and small enough to update frequently.**

## Mathematics Emerges

$$
g_B=\frac{1}{|B|}\sum_{i\in B}\nabla_\theta L_i
$$

Every operation records a need established above; the equation is the fossil, not the living discovery.

## Real-World Analogy

A council does not ask one witness or the entire nation. It hears a manageable panel, makes a decision, then hears another.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Exercises

Use the [invention challenges](exercises.md).

## Connections

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 027](../027-learning-rate/README.md)
