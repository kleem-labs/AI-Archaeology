# Excavation 090 — Policy Gradients — Improving the Choices Directly

[Previous: Excavation 089](../089-q-learning/README.md)

Value learning still needs a rule converting estimates into action probabilities.

The first solution that suggests itself is this: Always choose the highest estimated action.

The idea survives only until we test it against reality: Early errors remove exploration and discrete choice blocks ordinary differentiation.

The failure gives us a precise requirement: Sample from a policy and increase probability of actions followed by better-than-expected returns.

## Now work a case you can see

An action chosen with 20% probability produces unusually high reward; its probability is nudged upward.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build each piece from what just happened

- The sampled action probability comes from policy πθ.
- Its log converts repeated action probabilities into additive learning signals.
- Return G says how the chosen action eventually turned out.
- The gradient changes θ in the direction that makes above-average rewarded actions more likely.

Only now can we compress the procedure:

$$
\nabla_\theta J=\mathbb{E}\left[G\,\nabla_\theta\log\pi_\theta(a\mid s)\right]
$$

## Where your new idea still breaks

Policy gradients are noisy and can exploit reward flaws.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 091](../091-multimodal-alignment/README.md)
