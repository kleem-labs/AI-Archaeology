# Excavation 089 — Q-Learning — Improving Values from Experience

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

A value estimate represents future consequences from a state. Experience must now revise those estimates without waiting to rediscover every long future from scratch.

The previous discovery reaches the Road of Consequences carrying one unfinished problem. Beside the map of branching journeys, the expedition leader first tries to replace its value with the immediate reward.

There is good reason to begin this way. If we replace its value with the immediate reward, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: the update ignores the valuable state reached afterward.

This failure cannot be repaired by performing the instruction to replace its value with the immediate reward more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the map of branching journeys; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to move the estimate toward reward plus the best discounted value available next. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Q-Learning**. The name is simply a handle for the distinction already reconstructed.

## Improving Values from Experience

Reward 0 leads to a next state valued 10; with discount .9 the target is 9, not 0.

## The calculation hidden inside q-learning

The expedition leader carries the q-learning scene to the map of branching journeys. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A rescue robot reaches a fork. Moving left finds one injured hiker now, worth immediate reward 1, and leads to a state whose best known continuation is worth 5. If future reward is discounted by 0.9, the experience proposes `1 + 0.9×5 = 5.5` as the new target value for choosing left. The robot is not claiming certainty; it is joining what happened now with its best current estimate of what can follow.

The immediate reward is what happened now.
The largest next-state Q value represents the best continuation currently known.
Discount γ reduces distant evidence and keeps unending sums bounded.
Adding immediate and discounted future reward creates the target the old estimate moves toward.

### Why the melody needs these exact notes

[Addition](../../MATHEMATICAL_MOVES.md#addition) combines reward received now with estimated value still available afterward because both contribute to total future return.
[γ scales future value](../../MATHEMATICAL_MOVES.md#multiplication) to express delay or uncertainty; adding γ would give the same arbitrary bonus regardless of what future was reached.
[Max](../../MATHEMATICAL_MOVES.md#maximum) uses the value of the best next action because Q-learning asks what return remains under optimal continuation. Averaging would evaluate a different future policy.

The calculation borrows several gestures already encountered elsewhere: **the joining river**—separate contributions meet without losing where they came from; **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the highest lantern**—the strongest surviving possibility sets the visible ceiling. q-learning feels new because the objects are new; the gestures remain recognizably human.

The map of branching journeys already contains the complete q-learning mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
\text{target}=r+\gamma\max_{a^\prime}Q(s^\prime,a^\prime)
$$

## Where q-learning runs out

Maximization can overestimate noisy actions and offline data limits safe exploration.

Here the new path ends honestly. Q-Learning can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the map of branching journeys

Rebuild the q-learning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 090](../090-policy-gradients/README.md)
