# Excavation 025 — Gradient Descent — Teaching a Tiny Network

[Previous excavation](../024-backpropagation/README.md)

## Problem

We can now assign blame to every weight. The network still needs a disciplined way to turn those sensitivities into repeated improvement.

## Naive Attempt

Jump directly opposite the gradient with no step control; the model may overshoot and diverge. Take microscopic steps; learning may take forever. Trust one example; its noisy advice can undo another.

## Why It Fails

The attempt either throws away uncertainty, measures the wrong thing, or repeats work that the next step must preserve. We need a procedure whose parts answer the failure directly.

## Better Attempt

Move every parameter a controlled distance opposite its gradient, repeat on batches of examples, and watch loss rather than assuming progress.

## Why It Still Fails

The verbal procedure is now useful, but it is too long to repeat consistently and too vague to implement at scale. Every operation has earned a precise role; only now should notation compress it.

## Key Insight

**Move every parameter a controlled distance opposite its gradient, repeat on batches of examples, and watch loss rather than assuming progress.**

## Mathematics Emerges

$$
\theta_{t+1}=\theta_t-\eta\nabla_\theta L
$$

The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

## Real-World Analogy

Descending in fog requires frequent local slope readings and careful steps. Momentum and adaptive methods are better walking strategies, not different destinations.

## Limits

Gradient descent finds a reachable low region, not necessarily the unique best explanation. Data, initialization, scale, and step size all shape the journey.

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
