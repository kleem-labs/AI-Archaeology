# Excavation 022 — Derivatives — Asking One Weight What It Changed

[Previous excavation](../021-cross-entropy/README.md)

## Problem

The loss is high. The model has thousands of adjustable numbers. For one weight, should we increase it or decrease it?

## Naive Attempt

Try a large jump and keep it if loss falls. Large jumps can leap over improvements. Try every possible value; there are infinitely many.

## Why It Fails

The attempt either throws away uncertainty, measures the wrong thing, or repeats work that the next step must preserve. We need a procedure whose parts answer the failure directly.

## Better Attempt

Nudge the weight by a tiny amount, observe the change in loss, and divide change in loss by change in weight. Then imagine the nudge shrinking toward zero.

## Why It Still Fails

The verbal procedure is now useful, but it is too long to repeat consistently and too vague to implement at scale. Every operation has earned a precise role; only now should notation compress it.

## Key Insight

**Nudge the weight by a tiny amount, observe the change in loss, and divide change in loss by change in weight. Then imagine the nudge shrinking toward zero.**

## Mathematics Emerges

$$
\frac{dL}{dw}=\lim_{\epsilon\to0}\frac{L(w+\epsilon)-L(w)}{\epsilon}
$$

The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

## Real-World Analogy

A derivative is a local slope on a mountain trail: it says which direction rises and how sharply, only near the current step.

## Limits

A derivative is local advice. Curved landscapes can change direction, flatten, or hide better valleys elsewhere.

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
