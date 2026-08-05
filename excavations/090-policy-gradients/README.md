# Excavation 090 — Policy Gradients — Improving the Choices Directly

[Previous: Excavation 089](../089-q-learning/README.md)

## Take the First Step Yourself

> **Your problem:** Value learning still needs a rule converting estimates into action probabilities.

> **Try your first idea:** Always choose the highest estimated action.

> **Now try to break your idea:** Early errors remove exploration and discrete choice blocks ordinary differentiation.

> Stop here. State the missing requirement without naming the repair.

## The Observation

Value learning still needs a rule converting estimates into action probabilities.

## Your First Attempt

Always choose the highest estimated action.

## Break Your First Attempt

Early errors remove exploration and discrete choice blocks ordinary differentiation.

## Repair Your Attempt

Sample from a policy and increase probability of actions followed by better-than-expected returns.

## What You Have Just Invented

**Sample from a policy and increase probability of actions followed by better-than-expected returns.**

## Rebuild the Discovery with a Concrete Case

An action chosen with 20% probability produces unusually high reward; its probability is nudged upward.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build Every Piece from the Concrete Example

- The sampled action probability comes from policy πθ.
- Its log converts repeated action probabilities into additive learning signals.
- Return G says how the chosen action eventually turned out.
- The gradient changes θ in the direction that makes above-average rewarded actions more likely.

Only now can we compress the procedure:

$$
\nabla_\theta J=\mathbb{E}\left[G\,\nabla_\theta\log\pi_\theta(a\mid s)\right]
$$

## Real-World Limit

Policy gradients are noisy and can exploit reward flaws.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 091](../091-multimodal-alignment/README.md)
