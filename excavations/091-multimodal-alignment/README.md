# Excavation 091 — Multimodal Alignment

[Previous: Excavation 090](../090-policy-gradients/README.md)

## Take the First Step Yourself

> **Your problem:** How can an image and its caption meet in one representation?

> **Try your first idea:** Compare raw pixels directly with token IDs.

> **Now try to break your idea:** Their coordinates have unrelated meanings and shapes.

> Stop here. State the missing requirement without naming the repair.

## The Observation

How can an image and its caption meet in one representation?

## Your First Attempt

Compare raw pixels directly with token IDs.

## Break Your First Attempt

Their coordinates have unrelated meanings and shapes.

## Repair Your Attempt

Use separate encoders and train paired image-text examples to become nearby.

## What You Have Just Invented

**Use separate encoders and train paired image-text examples to become nearby.**

## Rebuild the Discovery with a Concrete Case

A tiger photo and “striped big cat” move together; mismatched captions move apart.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Real-World Limit

Pairs can contain weak, biased, or incomplete descriptions.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 092](../092-contrastive-learning/README.md)
