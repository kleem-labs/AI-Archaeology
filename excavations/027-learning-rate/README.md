# Excavation 027 — Learning Rate — How Large Should the Next Step Be?

[Previous: Excavation 026](../026-mini-batches/README.md)

## Problem

The gradient points downhill, but it does not say how far to walk. A correct direction can still produce a disastrous step.

## Naive Attempt

Always take a huge step: leap across the valley and oscillate. Always take a microscopic step: improve so slowly that the expedition ends first.

## Why It Fails

Direction without step size is not an update.

## Better Attempt

Multiply the gradient by a learning rate, observe whether loss descends, and adjust the rate over time.

## Why It Still Fails

The repair solves the immediate failure, but no single learning rate is best throughout training. Scale, curvature, batch noise, and parameter units all matter.

## Key Insight

**Multiply the gradient by a learning rate, observe whether loss descends, and adjust the rate over time.**

## Mathematics Emerges

## Build Every Piece from the Concrete Example

At weight 8 the gradient is 10. Rate 1 moves to -2 and overshoots; rate 0.1 moves to 7; rate 0.01 moves to 7.9. The rate controls travel distance, not downhill direction.

### Give Short Names Only After We Know the Pieces

- **g_t** is the downhill evidence measured at step t.
- **η_t** converts direction into a chosen travel distance and may change with time.
- The minus sign moves against increasing loss.
- **θ_t** and **θ_{t+1}** distinguish the old and updated parameter states.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
\theta_{t+1}=\theta_t-\eta_t g_t
$$


## Real-World Analogy

A mountain guide chooses shorter steps on steep or uncertain ground and can walk farther on a smooth open slope.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Exercises

Use the [invention challenges](exercises.md).

## Connections

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 028](../028-momentum/README.md)
