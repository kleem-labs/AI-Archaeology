# Excavation 077 — Convolution — Reusing the Same Local Detector

[Previous: Excavation 076](../076-pixels/README.md)

## Take the First Step Yourself

> **Your problem:** An edge can appear anywhere in an image.

> **Try your first idea:** Learn a separate edge detector for every location.

> **Now try to break your idea:** The model relearns the same pattern thousands of times and fails when it moves.

> Stop here. State the missing requirement without naming the repair.

## The Observation

An edge can appear anywhere in an image.

## Your First Attempt

Learn a separate edge detector for every location.

## Break Your First Attempt

The model relearns the same pattern thousands of times and fails when it moves.

## Repair Your Attempt

Slide one small learned filter across all positions and reuse its weights.

## What You Have Just Invented

**Slide one small learned filter across all positions and reuse its weights.**

## Rebuild the Discovery with a Concrete Case

The filter [-1,1] produces a large response wherever neighboring brightness jumps from dark to light.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build Every Piece from the Concrete Example

- The signal values are neighboring brightness measurements.
- The kernel values are the same small detector reused at every location.
- Multiplication measures how each local measurement agrees with its detector weight.
- Summation combines the local evidence; shifting i moves the same detector instead of learning a new one.

Only now can we compress the procedure:

$$
y_i=\sum_{j=0}^{k-1}x_{i+j}w_j
$$

## Real-World Limit

Convolution assumes useful locality and translation reuse.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 078](../078-pooling/README.md)
