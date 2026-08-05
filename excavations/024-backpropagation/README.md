# Excavation 024 — Backpropagation — Reusing Blame Instead of Recomputing It

[Previous excavation](../023-chain-rule/README.md)

## Problem

A network has millions of weights and shared intermediate results. The chain rule gives a path, but following every path independently repeats the same downstream calculations.

## Naive Attempt

Perturb each weight and rerun the model. This needs at least one extra forward pass per weight. Or trace paths independently and calculate the same suffix again and again.

## Why It Fails

The attempt either throws away uncertainty, measures the wrong thing, or repeats work that the next step must preserve. We need a procedure whose parts answer the failure directly.

## Better Attempt

Compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream.

## Why It Still Fails

The verbal procedure is now useful, but it is too long to repeat consistently and too vague to implement at scale. Every operation has earned a precise role; only now should notation compress it.

## Key Insight

**Compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream.**

## Mathematics Emerges

$$
\bar{x}=\sum_{y\in children(x)}\bar{y}\frac{\partial y}{\partial x}
$$

The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

## Real-World Analogy

A company traces one final loss through departments. Each department receives accumulated responsibility, then distributes it to the decisions that produced its output.

## Limits

Backpropagation computes gradients; it does not choose the update size or guarantee a good minimum.

## Implementation

Build the wrong idea first, break it, then use [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises

Use the [invention exercises](exercises.md), not as a quiz but as a request to rediscover the idea.

## Connections

- [Mistakes and failed ideas](mistakes.md)
- [Mermaid and ASCII diagram](diagram.md)
- [References](references.md)
- [Visual asset brief](images/README.md)

The limitation in this excavation creates the need for the next one.
