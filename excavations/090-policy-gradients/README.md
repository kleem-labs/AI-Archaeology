# Excavation 090 — Policy Gradients — Improving the Choices Directly

<!-- book-prose-v2 -->

Q-learning estimates the value of each action and then still needs a policy for choosing among them. We can instead ask how reward should directly change the probabilities of the choices the agent actually made.

The obvious economy is to always choose the highest estimated action.

The proposal deserves a fair hearing. For policy gradients, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Its hidden assumption becomes visible as soon as we observe that early errors remove exploration and discrete choice blocks ordinary differentiation.

The failure changes the question behind policy gradients. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: sample from a policy and increase probability of actions followed by better-than-expected returns.

Only at this point does the inherited name **Policy Gradients** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of policy gradients by mentally removing the repair. We fall back to the proposal to always choose the highest estimated action; then early errors remove exploration and discrete choice blocks ordinary differentiation. Restore only the ability to sample from a policy and increase probability of actions followed by better-than-expected returns, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to always choose the highest estimated action to requiring the system to sample from a policy and increase probability of actions followed by better-than-expected returns. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to policy gradients.

## Improving the Choices Directly

An action chosen with 20% probability produces unusually high reward; its probability is nudged upward.

Put the old procedure beside policy gradients. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## The calculation hidden inside policy gradients

Do not read the coming Policy Gradients line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

A rescue robot sometimes chooses the river path and sometimes the ridge path. On one trip it samples the ridge with probability 0.30 and eventually reaches the hiker safely, earning a strong return. The learning signal should make that sampled choice somewhat more likely. On a failed trip, the return reverses the pressure. The policy gradient is the bookkeeping rule that connects how the trip ended to how the probability of the chosen action should change.

The sampled action probability comes from policy πθ.
Its log converts repeated action probabilities into additive learning signals.
Return G says how the chosen action eventually turned out.
The gradient changes θ in the direction that makes above-average rewarded actions more likely.

### Why no cheaper operation does the same job

[The policy log](../../MATHEMATICAL_MOVES.md#logarithm) turns a product of action probabilities along a trajectory into additive terms and yields a convenient relative sensitivity: how a small parameter change alters chosen-action probability.
[Multiplying by return G](../../MATHEMATICAL_MOVES.md#multiplication) makes successful sampled actions more influential and harmful ones push the opposite way; adding G would shift advice without scaling responsibility.
[Expectation](../../MATHEMATICAL_MOVES.md#expectation) averages this noisy sampled advice across trajectories according to how often the policy produces them.

Every symbol in Policy Gradients can now be read back into an action already performed. The whole procedure fits in one line:

$$
\nabla_\theta J=\mathbb{E}\left[G\nabla_\theta\log\pi_\theta(a\mid s)\right]
$$

## Where policy gradients runs out

Policy gradients are noisy and can exploit reward flaws.

The limit follows from the job assigned to policy gradients. Its repair knows how to sample from a policy and increase probability of actions followed by better-than-expected returns. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take policy gradients to the workbench

A claim about policy gradients now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running policy gradients, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the policy gradients result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 091](../091-multimodal-alignment/README.md)
