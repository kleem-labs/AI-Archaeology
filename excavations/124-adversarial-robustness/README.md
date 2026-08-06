# Excavation 124 — Adversarial Robustness

[Previous: Excavation 123](../123-federated-learning/README.md)

## Take the First Step Yourself

> **Your problem:** A tiny input change invisible to a person flips the model’s decision.

> **Try your first idea:** Test only natural clean examples.

> **Now try to break your idea:** An attacker follows the model’s sensitivity into a brittle direction.

> Stop here. State the missing requirement without naming the repair.

## The Observation

A tiny input change invisible to a person flips the model’s decision.

## Your First Attempt

Test only natural clean examples.

## Break Your First Attempt

An attacker follows the model’s sensitivity into a brittle direction.

## Repair Your Attempt

Search for worst-case permitted perturbations, train against them, and bound behavior where possible.

## What You Have Just Invented

**Search for worst-case permitted perturbations, train against them, and bound behavior where possible.**

## Rebuild the Discovery with a Concrete Case

Changing a few pixel values turns tiger into toaster for the model while looking unchanged to a human.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Real-World Limit

Robustness to one threat model does not imply robustness to others.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 125](../125-open-ended-research-system/README.md)
