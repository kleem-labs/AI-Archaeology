# Excavation 111 — World Models

[Previous: Excavation 110](../110-self-supervised-learning/README.md)

## Take the First Step Yourself

> **Your problem:** An agent needs to predict consequences before acting.

> **Try your first idea:** Learn only which action was rewarded in previously visited situations.

> **Now try to break your idea:** The agent cannot imagine untried sequences or reuse physical regularities.

> Stop here. State the missing requirement without naming the repair.

## The Observation

An agent needs to predict consequences before acting.

## Your First Attempt

Learn only which action was rewarded in previously visited situations.

## Break Your First Attempt

The agent cannot imagine untried sequences or reuse physical regularities.

## Repair Your Attempt

Learn a compact model that predicts next state and reward from current state and action.

## What You Have Just Invented

**Learn a compact model that predicts next state and reward from current state and action.**

## Rebuild the Discovery with a Concrete Case

From ball position and push direction, predict where the ball will move before choosing the push.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Real-World Limit

Model errors compound during long imagined rollouts.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 112](../112-causal-inference/README.md)
