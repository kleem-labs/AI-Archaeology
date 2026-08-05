# Excavation 089 — Q-Learning — Improving Values from Experience

[Previous: Excavation 088](../088-value-functions/README.md)

## Take the First Step Yourself

> **Your problem:** How should one experience update the value of an action?

> **Try your first idea:** Replace its value with the immediate reward.

> **Now try to break your idea:** The update ignores the valuable state reached afterward.

> Stop here. State the missing requirement without naming the repair.

## The Observation

How should one experience update the value of an action?

## Your First Attempt

Replace its value with the immediate reward.

## Break Your First Attempt

The update ignores the valuable state reached afterward.

## Repair Your Attempt

Move the estimate toward reward plus the best discounted value available next.

## What You Have Just Invented

**Move the estimate toward reward plus the best discounted value available next.**

## Rebuild the Discovery with a Concrete Case

Reward 0 leads to a next state valued 10; with discount .9 the target is 9, not 0.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build Every Piece from the Concrete Example

- The immediate reward is what happened now.
- The largest next-state Q value represents the best continuation currently known.
- Discount γ reduces distant evidence and keeps unending sums bounded.
- Adding immediate and discounted future reward creates the target the old estimate moves toward.

Only now can we compress the procedure:

$$
\text{target}=r+\gamma\max_{a^\prime}Q(s^\prime,a^\prime)
$$

## Real-World Limit

Maximization can overestimate noisy actions and offline data limits safe exploration.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 090](../090-policy-gradients/README.md)
