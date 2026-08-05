# Excavation 038 — Position — Why Order Must Enter the Model

[Previous: Excavation 037](../037-input-embeddings/README.md)

## Problem

dog bites man and man bites dog retrieve the same token vectors. Attention compares content, but content alone does not say which occurrence came first.

## Naive Attempt

Sort tokens by ID or trust their array slot without exposing it to the model. The first invents arbitrary order; the second stores position outside the computation.

## Why It Fails

The attempt either gives the model forbidden information, discards useful structure, or performs repeated work without solving the actual representation problem.

## Better Attempt

Add a position-specific vector to each token vector before attention. Content says what; position says where.

## Why It Still Fails

A fixed learned table cannot extend beyond trained positions, and absolute location is not always the relationship language needs.

## Key Insight

**Add a position-specific vector to each token vector before attention. Content says what; position says where.**

## Mathematics Emerges

$$
z_i=E[token_i]+P_i
$$

The equation arrives after every operation has a job.

## Real-World Analogy

Seat numbers do not describe passengers, but they preserve who sat where.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 039](../039-causal-mask/README.md)
