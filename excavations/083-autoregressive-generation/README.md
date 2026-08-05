# Excavation 083 — Autoregressive Generation Beyond Text

[Previous: Excavation 082](../082-latent-space/README.md)

## Take the First Step Yourself

> **Your problem:** How can a model generate an image one piece at a time?

> **Try your first idea:** Predict all pixels independently.

> **Now try to break your idea:** Independent pixels produce noise because neighboring colors and shapes constrain one another.

> Stop here. State the missing requirement without naming the repair.

## The Observation

How can a model generate an image one piece at a time?

## Your First Attempt

Predict all pixels independently.

## Break Your First Attempt

Independent pixels produce noise because neighboring colors and shapes constrain one another.

## Repair Your Attempt

Choose an order and predict each piece from previously generated pieces.

## What You Have Just Invented

**Choose an order and predict each piece from previously generated pieces.**

## Rebuild the Discovery with a Concrete Case

After generating sky pixels, the model gives blue neighbors higher probability.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Real-World Limit

Sequential generation can be slow and ordering introduces bias.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 084](../084-diffusion/README.md)
