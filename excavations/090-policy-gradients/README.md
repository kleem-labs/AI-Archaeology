# Excavation 090 — Policy Gradients — Improving the Choices Directly

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Calculus & Differential Change](../../MATHEMATICS_ATLAS.md#calculus) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Q-learning estimates the value of each action and then still needs a policy for choosing among them. We can instead ask how reward should directly change the probabilities of the choices the agent actually made.

The map of branching journeys at the Road of Consequences still carries the marks of the previous discovery. The expedition leader follows them as far as they seem willing to go: always choose the highest estimated action.

For a moment the mark looks complete. Then the evidence refuses to fit: early errors remove exploration and discrete choice blocks ordinary differentiation. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The expedition leader sketches the break before changing it:*

```text
OLD PATH:  request ──▶ always choose the highest estimated… ──▶ early errors remove exploration and…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ sample from a policy and increase… ──▶ accountable result
```

The expedition leader lays two translucent sheets over the map of branching journeys. The first is inscribed, “always choose the highest estimated action.” Its path ends where early errors remove exploration and discrete choice blocks ordinary differentiation. The second receives the same evidence but is allowed to sample from a policy and increase probability of actions followed by better-than-expected returns. Held to the light, the sheets separate at exactly one decision.

No one reaches for a policy gradients formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The expedition leader changes only that one responsibility: sample from a policy and increase probability of actions followed by better-than-expected returns. When the ink dries, the name **Policy Gradients** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because early errors remove exploration and discrete choice blocks ordinary differentiation, while the other can sample from a policy and increase probability of actions followed by better-than-expected returns. That fork—not the vocabulary—is where policy gradients lives.

<!-- memory-film-v1:start -->
> **Memory realm 9 of 18 — [Road of Consequences](../../MEMORY_PALACE.md#realm-9)**
>
> **The question carried into this chamber:** What fails if we always choose the highest estimated action?

## When the chamber changes

The Policy Gradients room does not ask you to memorize its name. It asks you to watch one object change.

First hold the failed picture still: The gate follows the tempting path—always choose the highest estimated action. Then the evidence answers: early errors remove exploration and discrete choice blocks ordinary differentiation.

Now let the chamber move: The expedition leader changes one moving part. The gate can now sample from a policy and increase probability of actions followed by better-than-expected returns.

The object that should remain after the terminology disappears is **the policy gradients gate mounted on the map of branching journeys**.

> **Memory seal — Policy Gradients**
>
> Policy Gradients keeps the missing power: sample from a policy and increase probability of actions followed by better-than-expected returns.

Give the idea a bodily path: Touch the policy gradients gate in imagination: draw the old path in the air, stop sharply at its failure, and finish with the new motion.
<!-- memory-film-v1:end -->

## Improving the Choices Directly

An action chosen with 20% probability produces unusually high reward; its probability is nudged upward.

## The calculation hidden inside policy gradients

The expedition leader carries the policy gradients scene to the map of branching journeys. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A rescue robot sometimes chooses the river path and sometimes the ridge path. On one trip it samples the ridge with probability 0.30 and eventually reaches the hiker safely, earning a strong return. The learning signal should make that sampled choice somewhat more likely. On a failed trip, the return reverses the pressure. The policy gradient is the bookkeeping rule that connects how the trip ended to how the probability of the chosen action should change.

The sampled action probability comes from policy πθ.
Its log converts repeated action probabilities into additive learning signals.
Return G says how the chosen action eventually turned out.
The gradient changes θ in the direction that makes above-average rewarded actions more likely.

### Why the melody needs these exact notes

[The policy log](../../MATHEMATICAL_MOVES.md#logarithm) turns a product of action probabilities along a trajectory into additive terms and yields a convenient relative sensitivity: how a small parameter change alters chosen-action probability.
[Multiplying by return G](../../MATHEMATICAL_MOVES.md#multiplication) makes successful sampled actions more influential and harmful ones push the opposite way; adding G would shift advice without scaling responsibility.
[Expectation](../../MATHEMATICAL_MOVES.md#expectation) averages this noisy sampled advice across trajectories according to how often the policy produces them.

Three old motions cast new shadows here: **the spiral stair**—compounded chances become steps that can be accumulated; **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the council of possible worlds**—each future speaks in proportion to how often it may arrive. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Every mark needed for policy gradients is now visible on the map of branching journeys. The symbols do not add an idea; they bind the discovered moves into one line:

$$
\nabla_\theta J=\mathbb{E}\left[G\nabla_\theta\log\pi_\theta(a\mid s)\right]
$$

## Where policy gradients runs out

Policy gradients are noisy and can exploit reward flaws.

At the Road of Consequences, the expedition leader leaves a blank beneath the new mark. Policy Gradients has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the map of branching journeys

Rebuild the policy gradients scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 091](../091-multimodal-alignment/README.md)
