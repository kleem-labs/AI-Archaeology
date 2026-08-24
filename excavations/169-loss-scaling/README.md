# Excavation 169 — Loss Scaling — Rescue Gradients Too Small to Represent

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Calculus & Differential Change](../../MATHEMATICS_ATLAS.md#calculus) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

The forward pass looks correct, but some half-precision gradients round to zero before the optimizer can use them.

Morning reaches the Engine Cavern before anyone has a name for today's difficulty. Beside the brass reference machine, the enginewright tries the smallest continuation of what already works: increase the learning rate so small updates become visible.

The rule survives the easy cases. The next case leaves a crack through the middle of it: the learning rate acts after gradients are formed; it cannot recover values that already underflowed to zero, and it enlarges every surviving update. More confidence cannot repair information that never entered the rule.

*The enginewright sketches the break before changing it:*

```text
observation
    │
    ▼
[increase the learning rate so small…]
    │
    ╳  the learning rate acts after…
    │
    ▼
[multiply the loss before…]
```

Two trails now cross the brass reference machine. The pale trail bears the instruction “increase the learning rate so small updates become visible.” It disappears into the observed failure: the learning rate acts after gradients are formed; it cannot recover values that already underflowed to zero, and it enlarges every surviving update. The darker trail carries one additional capacity—to multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed loss scaling mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the brass reference machine is altered in exactly one way: multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating. Much later, people will call this territory **Loss Scaling**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the brass reference machine. The failed path remains visible beneath the repair, because loss scaling is easier to remember when its scar remains attached to it. The scar reads, ‘the learning rate acts after gradients are formed; it cannot recover values that already underflowed to zero, and it enlarges every surviving update’; the new line exists only to keep that loss from happening again.

<!-- memory-film-v1:start -->
> **Memory realm 12 of 18 — [Engine Cavern](../../MEMORY_PALACE.md#realm-12)**
>
> **The question carried into this chamber:** What fails if we increase the learning rate so small updates become visible?

## When the chamber changes

The mathematical name Loss Scaling can now rest. What matters is whether its transformation remains visible.

First hold the failed picture still: The vessel follows the tempting path—increase the learning rate so small updates become visible. Then the evidence answers: the learning rate acts after gradients are formed; it cannot recover values that already underflowed to zero, and it enlarges every surviving update.

Now let the chamber move: The enginewright changes one moving part. The vessel can now multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating.

The object that should remain after the terminology disappears is **the loss scaling vessel mounted on the brass reference machine**.

> **Memory seal — Loss Scaling**
>
> Loss Scaling keeps the missing power: multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating.

Give the idea a bodily path: Touch the loss scaling vessel in imagination: hold both hands as the two failed alternatives, then move one hand through the repaired route.
<!-- memory-film-v1:end -->

## Rescue Gradients Too Small to Represent

A gradient 0.000001 becomes 0.001 when loss scale is 1000, survives backpropagation, and returns to 0.000001 after unscaling.

## The calculation hidden inside loss scaling

The enginewright carries the loss scaling scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A true gradient of 0.000001 may vanish in half precision. Before differentiation, make the loss one thousand times larger; every loss-derived gradient becomes 0.001 and survives. Before updating the weight, divide by the same thousand and recover 0.000001. S names this temporary magnifier, L the original loss, and g the restored gradient—the model has not been told to learn a thousand times faster.

L is original loss, S is a temporary positive scale, and g is the recovered gradient in the loss's original units.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) by S enlarges every loss-derived gradient before narrow arithmetic can erase it. [Division](../../MATHEMATICAL_MOVES.md#division) by the same S reverses that temporary unit change before the optimizer. Adding S would not proportionally enlarge tiny sensitivities and could not be undone uniformly.

The calculation borrows several gestures already encountered elsewhere: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. loss scaling feels new because the objects are new; the gestures remain recognizably human.

The enginewright reads the journey of loss scaling once more across the brass reference machine, then lets the words contract without losing their order:

$$
g=\frac{1}{S}\nabla_\theta(SL)
$$

## Where loss scaling runs out

A scale large enough to prevent underflow can cause overflow, so practical systems adjust it dynamically.

The brass reference machine answers today's question and falls silent at the next. That silence is precise: Loss Scaling was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the brass reference machine

Rebuild the loss scaling scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Gradient Accumulation — Build a Large Batch That Does Not Fit](../170-gradient-accumulation/README.md)
