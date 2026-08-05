# Excavation 087 — States, Actions, and Transitions

[Previous: Excavation 086](../086-rewards/README.md)

## Take the First Step Yourself

> **Your problem:** To learn from reward, what must one experience record?

> **Try your first idea:** Store only action and final reward.

> **Now try to break your idea:** The same action helps in one situation and harms in another.

> Stop here. State the missing requirement without naming the repair.

## The Observation

To learn from reward, what must one experience record?

## Your First Attempt

Store only action and final reward.

## Break Your First Attempt

The same action helps in one situation and harms in another.

## Repair Your Attempt

Record current state, chosen action, reward, and resulting state.

## What You Have Just Invented

**Record current state, chosen action, reward, and resulting state.**

## Rebuild the Discovery with a Concrete Case

“Move right” from left of the door succeeds; the same action beside a cliff fails because state differs.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Real-World Limit

A state representation may omit information needed for future decisions.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 088](../088-value-functions/README.md)
