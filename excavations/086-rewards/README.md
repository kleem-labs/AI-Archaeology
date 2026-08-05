# Excavation 086 — Rewards — Learning Without Correct Answers

[Previous: Excavation 085](../085-denoising/README.md)

## Take the First Step Yourself

> **Your problem:** An agent acts over time and receives only eventual success or failure.

> **Try your first idea:** Label the correct action at every moment.

> **Now try to break your idea:** For exploration or games, nobody knows every correct intermediate move.

> Stop here. State the missing requirement without naming the repair.

## The Observation

An agent acts over time and receives only eventual success or failure.

## Your First Attempt

Label the correct action at every moment.

## Break Your First Attempt

For exploration or games, nobody knows every correct intermediate move.

## Repair Your Attempt

Provide outcome feedback and let experience connect actions with later consequences.

## What You Have Just Invented

**Provide outcome feedback and let experience connect actions with later consequences.**

## Rebuild the Discovery with a Concrete Case

A maze gives +1 only at the exit; repeated trials reveal which earlier turns tend to reach it.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Real-World Limit

Poor rewards create unintended shortcuts.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 087](../087-states-actions-transitions/README.md)
