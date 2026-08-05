# Excavation 094 — Low-Rank Adaptation

[Previous: Excavation 093](../093-speech-audio/README.md)

## Take the First Step Yourself

> **Your problem:** How can a huge pretrained model learn a new task without changing every weight?

> **Try your first idea:** Copy and fine-tune all parameters for every task.

> **Now try to break your idea:** Storage and training cost multiply, and the base model is harder to preserve.

> Stop here. State the missing requirement without naming the repair.

## The Observation

How can a huge pretrained model learn a new task without changing every weight?

## Your First Attempt

Copy and fine-tune all parameters for every task.

## Break Your First Attempt

Storage and training cost multiply, and the base model is harder to preserve.

## Repair Your Attempt

Freeze the base and learn a small low-rank correction to selected matrices.

## What You Have Just Invented

**Freeze the base and learn a small low-rank correction to selected matrices.**

## Rebuild the Discovery with a Concrete Case

Instead of a million-value update, two narrow matrices produce a constrained correction with far fewer trainable values.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build Every Piece from the Concrete Example

- W is the frozen large matrix we refuse to duplicate.
- A and B are the two narrow trainable matrices.
- Their product BA creates a full-shaped correction while using far fewer values.
- Addition preserves the base behavior and applies only the learned adaptation.

Only now can we compress the procedure:

$$
W^\prime=W+BA
$$

## Real-World Limit

Low rank may be insufficient for large behavioral changes.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 095](../095-quantization/README.md)
