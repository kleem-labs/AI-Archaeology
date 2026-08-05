# Excavation 040 — Next-Token Examples — One Sentence Becomes Many Lessons

[Previous: Excavation 039](../039-causal-mask/README.md)

## Problem

We have tokens, positions, and a causal boundary. The model still needs explicit questions and answers.

## Naive Attempt

Treat an entire sentence as one training example with one answer. Most of its transitions provide no learning signal.

## Why It Fails

The attempt either gives the model forbidden information, discards useful structure, or performs repeated work without solving the actual representation problem.

## Better Attempt

Shift the sequence by one position so every visible prefix predicts the token immediately following it.

## Why It Still Fails

Padding and document boundaries can create false targets unless their losses are masked.

## Key Insight

**Shift the sequence by one position so every visible prefix predicts the token immediately following it.**

## Mathematics Emerges

$$
x=(t_0,\ldots,t_{n-1}),\qquad y=(t_1,\ldots,t_n)
$$

The equation arrives after every operation has a job.

## Real-World Analogy

A reading teacher pauses after every word, not only at the final period.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 041](../041-logits/README.md)
