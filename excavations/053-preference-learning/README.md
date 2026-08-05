# Excavation 053 — Preference Learning — When Several Answers Are Correct but Not Equally Helpful

[Previous: Excavation 052](../052-instruction-tuning/README.md)

## Take the First Step Yourself

> **Your problem:** Two answers are factually acceptable, but one is clearer, safer, and better aligned with the user’s intent.

> **Try your first idea:** Write one perfect target response for every prompt and train only to imitate it.

> **Now try to break your idea:** Many answers can be valid. A single target penalizes harmless alternatives and cannot express that answer A is preferred to B without being the only possible answer.

> Stop here. State what the repair must accomplish in ordinary language. Do not name a standard technique.

## The Observation

Two answers are factually acceptable, but one is clearer, safer, and better aligned with the user’s intent.

## Your First Attempt

Write one perfect target response for every prompt and train only to imitate it.

## Break Your First Attempt

Many answers can be valid. A single target penalizes harmless alternatives and cannot express that answer A is preferred to B without being the only possible answer.

What information did the attempt lose? Write that requirement before continuing.

## Repair Your Attempt

Collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy.

## What You Have Just Invented

**Collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy.**

## Build Every Piece from the Concrete Example

For “How do I reset my router?”, answer A gives three safe ordered steps; answer B gives twenty vague paragraphs. A reviewer chooses A. Repeated comparisons teach concision and usefulness without declaring one exact sentence mandatory.

### Give Short Names Only After We Know the Pieces

The reward scores two responses to the same prompt. Their difference matters, not the absolute score. The logistic function turns that difference into a preference probability; larger positive differences favor the chosen answer.

Only now can we compress the exact procedure:

$$
P(A\succ B)=\frac{1}{1+\exp(-(r_A-r_B))}
$$

## Real-World Limit

Human preferences conflict, annotators make mistakes, and optimizing a learned reward can exploit its blind spots.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 054](../054-retrieval-augmented-generation/README.md)
