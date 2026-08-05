# Excavation 082 — Latent Space — Coordinates for Hidden Causes

[Previous: Excavation 081](../081-autoencoders/README.md)

## Take the First Step Yourself

> **Your problem:** The bottleneck contains numbers, but do nearby codes vary meaningfully?

> **Try your first idea:** Assume any compressed coordinates form a smooth useful space.

> **Now try to break your idea:** Tiny code changes can cause abrupt unrelated outputs.

> Stop here. State the missing requirement without naming the repair.

## The Observation

The bottleneck contains numbers, but do nearby codes vary meaningfully?

## Your First Attempt

Assume any compressed coordinates form a smooth useful space.

## Break Your First Attempt

Tiny code changes can cause abrupt unrelated outputs.

## Repair Your Attempt

Shape the latent distribution and train nearby codes to decode coherently.

## What You Have Just Invented

**Shape the latent distribution and train nearby codes to decode coherently.**

## Rebuild the Discovery with a Concrete Case

Moving one latent coordinate gradually changes image brightness while another changes pose.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Real-World Limit

Latent directions need not be independent or human-readable.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 083](../083-autoregressive-generation/README.md)
