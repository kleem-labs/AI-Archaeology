# Excavation 076 — Pixels — Turning Light into Numbers

[Previous: Excavation 075](../075-causal-interventions/README.md)

## Take the First Step Yourself

> **Your problem:** A camera gives a grid of colored light, not objects.

> **Try your first idea:** Assign one label to the entire raw byte sequence.

> **Now try to break your idea:** A one-pixel shift changes thousands of byte positions although the same tiger remains.

> Stop here. State the missing requirement without naming the repair.

## The Observation

A camera gives a grid of colored light, not objects.

## Your First Attempt

Assign one label to the entire raw byte sequence.

## Break Your First Attempt

A one-pixel shift changes thousands of byte positions although the same tiger remains.

## Repair Your Attempt

Preserve local spatial arrangement and compare nearby color measurements.

## What You Have Just Invented

**Preserve local spatial arrangement and compare nearby color measurements.**

## Rebuild the Discovery with a Concrete Case

A 2×2 grayscale patch becomes four intensities with explicit row and column positions.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Real-World Limit

Pixels depend on lighting, sensor, scale, and viewpoint.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 077](../077-convolution/README.md)
