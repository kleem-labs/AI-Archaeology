# Excavation 169 — Loss Scaling — Rescue Gradients Too Small to Represent

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Calculus & Differential Change](../../MATHEMATICS_ATLAS.md#calculus) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

The forward pass looks correct, but some half-precision gradients round to zero before the optimizer can use them.

The previous discovery reaches the Engine Cavern carrying one unfinished problem. Beside the brass reference machine, the enginewright first tries to increase the learning rate so small updates become visible.

There is good reason to begin this way. If we increase the learning rate so small updates become visible, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: the learning rate acts after gradients are formed; it cannot recover values that already underflowed to zero, and it enlarges every surviving update.

This failure cannot be repaired by performing the instruction to increase the learning rate so small updates become visible more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the brass reference machine; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Loss Scaling**. The name is simply a handle for the distinction already reconstructed.

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
