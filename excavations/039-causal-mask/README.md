# Excavation 039 — Causal Masking — Preventing the Future from Leaking Backward

[Previous: Excavation 038](../038-position/README.md)

## Problem

During next-token training the whole sentence is available. Without a barrier, the representation at cat can inspect the answer sitting to its right.

## Naive Attempt

Train each prefix in a separate forward pass. It prevents cheating but repeats nearly identical work.

## Why It Fails

The attempt either gives the model forbidden information, discards useful structure, or performs repeated work without solving the actual representation problem.

## Better Attempt

Process all positions together while blocking attention from position i to every later position j.

## Why It Still Fails

A mask prevents direct attention leakage; shifted targets and data pipelines must also align correctly.

## Key Insight

**Process all positions together while blocking attention from position i to every later position j.**

## Mathematics Emerges

## Why Every Term Must Exist Before the Equation

- **i** is the receiving position and **j** a possible source position.
- When j≤i, the source is present or past, so adding zero leaves its attention score unchanged.
- When j>i, the source is future; adding −∞ makes its later softmax weight zero.
- **M_ij** stores that allowed-or-forbidden correction for every pair.

Only now can we compress that reasoning:

$$
M_{ij}=\begin{cases}0&j\le i\\-\infty&j>i\end{cases}
$$


The equation arrives after every operation has a job.

## Real-World Analogy

An exam sheet can contain later questions, but an opaque cover hides everything beyond the current line.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 040](../040-next-token-examples/README.md)
