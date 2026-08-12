# Excavation 090 — Policy Gradients — Improving the Choices Directly

Q-learning estimates the value of each action and then still needs a policy for choosing among them. We can instead ask how reward should directly change the probabilities of the choices the agent actually made.

Perhaps we always choose the highest estimated action.

But early errors remove exploration and discrete choice blocks ordinary differentiation.

So we sample from a policy and increase probability of actions followed by better-than-expected returns.

## Let the case decide

An action chosen with 20% probability produces unusually high reward; its probability is nudged upward.

## The arithmetic we have earned

A rescue robot sometimes chooses the river path and sometimes the ridge path. On one trip it samples the ridge with probability 0.30 and eventually reaches the hiker safely, earning a strong return. The learning signal should make that sampled choice somewhat more likely. On a failed trip, the return reverses the pressure. The policy gradient is the bookkeeping rule that connects how the trip ended to how the probability of the chosen action should change.

- The sampled action probability comes from policy πθ.
- Its log converts repeated action probabilities into additive learning signals.
- Return G says how the chosen action eventually turned out.
- The gradient changes θ in the direction that makes above-average rewarded actions more likely.

Only now can we compress the procedure:

$$
\nabla_\theta J=\mathbb{E}\left[G\nabla_\theta\log\pi_\theta(a\mid s)\right]
$$

## The boundary of the discovery

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
