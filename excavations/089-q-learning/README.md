# Excavation 089 — Q-Learning — Improving Values from Experience

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

A value estimate represents future consequences from a state. Experience must now revise those estimates without waiting to rediscover every long future from scratch.

Morning reaches the Road of Consequences before anyone has a name for today's difficulty. Beside the map of branching journeys, the expedition leader tries the smallest continuation of what already works: replace its value with the immediate reward.

At the edge of the map of branching journeys, the shortcut produces its consequence: the update ignores the valuable state reached afterward. That consequence, not a textbook, earns the next move.

*The expedition leader sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   replace its value with the immediate… the update ignores the valuable state…
            \        /
             \      /
              move the estimate toward reward plus…
```

The expedition leader covers the new mark and the old contradiction returns: the update ignores the valuable state reached afterward. The cover is lifted, restoring the ability to move the estimate toward reward plus the best discounted value available next, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason q-learning exists.

What must change for q-learning is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: move the estimate toward reward plus the best discounted value available next. That threshold is where **Q-Learning** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In q-learning, that memory takes a precise form: whenever the update ignores the valuable state reached afterward, preserve enough structure to move the estimate toward reward plus the best discounted value available next.

<!-- memory-film-v1:start -->
> **Memory realm 9 of 18 — [Road of Consequences](../../MEMORY_PALACE.md#realm-9)**
>
> **The question carried into this chamber:** What fails if we replace its value with the immediate reward?

## When the chamber changes

The mathematical name Q-Learning can now rest. What matters is whether its transformation remains visible.

First hold the failed picture still: The vessel follows the tempting path—replace its value with the immediate reward. Then the evidence answers: the update ignores the valuable state reached afterward.

Now let the chamber move: The expedition leader changes one moving part. The vessel can now move the estimate toward reward plus the best discounted value available next.

The object that should remain after the terminology disappears is **the q-learning vessel mounted on the map of branching journeys**.

> **Memory seal — Q-Learning**
>
> Q-Learning keeps the missing power: move the estimate toward reward plus the best discounted value available next.

Give the idea a bodily path: Touch the q-learning vessel in imagination: hold both hands as the two failed alternatives, then move one hand through the repaired route.
<!-- memory-film-v1:end -->

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
