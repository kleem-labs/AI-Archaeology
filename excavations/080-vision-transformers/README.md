# Excavation 080 — Vision Transformers

[Previous: Excavation 079](../079-cnn-hierarchy/README.md)

## Take the First Step Yourself

> **Your problem:** Convolutions bake in locality, but distant image regions may need direct comparison.

> **Try your first idea:** Treat every pixel as a token.

> **Now try to break your idea:** The sequence becomes enormous and individual pixels carry little stable structure.

> Stop here. State the missing requirement without naming the repair.

## The Observation

Convolutions bake in locality, but distant image regions may need direct comparison.

## Your First Attempt

Treat every pixel as a token.

## Break Your First Attempt

The sequence becomes enormous and individual pixels carry little stable structure.

## Repair Your Attempt

Group pixels into patches, embed them as tokens, add position, and apply attention.

## What You Have Just Invented

**Group pixels into patches, embed them as tokens, add position, and apply attention.**

## Rebuild the Discovery with a Concrete Case

A 224×224 image with 16×16 patches becomes 196 tokens instead of 50,176 pixel tokens.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Real-World Limit

Patch size trades detail for cost and needs substantial data.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 081](../081-autoencoders/README.md)
