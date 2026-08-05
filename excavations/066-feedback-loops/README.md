# Excavation 066 — Feedback Loops

[Previous: Excavation 065](../065-bounded-autonomy/README.md)

## Take the First Step Yourself

> **Your problem:** Recommendations change what users see, and those changed choices become tomorrow’s training data.

> **Try your first idea:** Treat every click as independent evidence of natural preference.

> **Now try to break your idea:** Show one song repeatedly; its extra clicks now appear to prove it deserved repetition.

> Stop here. State the missing requirement without naming the repair.

## The Observation

Recommendations change what users see, and those changed choices become tomorrow’s training data.

## Your First Attempt

Treat every click as independent evidence of natural preference.

## Break Your First Attempt

Show one song repeatedly; its extra clicks now appear to prove it deserved repetition.

## Repair Your Attempt

Record how the system influenced each observation and evaluate outcomes against a control or exploration policy.

## What You Have Just Invented

**Record how the system influenced each observation and evaluate outcomes against a control or exploration policy.**

## Rebuild the Discovery with a Concrete Case

Two equal songs begin with ten listeners each. The agent promotes A to ninety more people; A receives more clicks because it received more chances, not necessarily because it was better.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Real-World Limit

Feedback can create self-fulfilling popularity and erase unexposed alternatives.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 067](../067-online-learning/README.md)
