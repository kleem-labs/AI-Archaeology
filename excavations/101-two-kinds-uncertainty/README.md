# Excavation 101 — Two Kinds of Uncertainty

[Previous: Excavation 100](../100-complete-ai-system/README.md)

## Take the First Step Yourself

> **Your problem:** The model is unsure whether a blurry animal is a tiger. Is the image ambiguous, or has the model never seen this species?

> **Try your first idea:** Represent every uncertainty with one low confidence number.

> **Now try to break your idea:** A clearer image can repair blur, but not missing knowledge; more training data can repair missing knowledge, but not a genuinely coin-flip outcome.

> Stop here. State the missing requirement without naming the repair.

## The Observation

The model is unsure whether a blurry animal is a tiger. Is the image ambiguous, or has the model never seen this species?

## Your First Attempt

Represent every uncertainty with one low confidence number.

## Break Your First Attempt

A clearer image can repair blur, but not missing knowledge; more training data can repair missing knowledge, but not a genuinely coin-flip outcome.

## Repair Your Attempt

Separate uncertainty in the observation from uncertainty in the model’s knowledge.

## What You Have Just Invented

**Separate uncertainty in the observation from uncertainty in the model’s knowledge.**

## Rebuild the Discovery with a Concrete Case

A foggy known tiger remains ambiguous even for an expert; a clear pangolin confuses a tiger-only learner for a different reason.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Real-World Limit

The two sources interact and are difficult to estimate perfectly.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 102](../102-bayesian-updating/README.md)
