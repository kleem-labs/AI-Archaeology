# Excavation 169 — Loss Scaling — Rescue Gradients Too Small to Represent

<!-- book-prose-v2 -->

The forward pass looks correct, but some half-precision gradients round to zero before the optimizer can use them.

For a moment, remain loyal to the simplest proposal: increase the learning rate so small updates become visible.

Its appeal is not ignorance but economy. Loss Scaling should not be added until an observation exposes the exact thing the older procedure cannot preserve.

The world supplies the one comparison the shortcut hoped never to face: the learning rate acts after gradients are formed; it cannot recover values that already underflowed to zero, and it enlarges every surviving update.

Notice what the counterexample has accomplished for loss scaling. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating.

Humanity eventually gathered this problem and its repairs under the name **Loss Scaling**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace loss scaling with the old instruction to increase the learning rate so small updates become visible. The result is again that the learning rate acts after gradients are formed; it cannot recover values that already underflowed to zero, and it enlarges every surviving update. Put back only the requirement to multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when loss scaling is introduced. The same evidence that defeated the attempt to increase the learning rate so small updates become visible is presented again. Only the ability to multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating changes, so the repaired conclusion cannot be credited to a conveniently different example.

## Rescue Gradients Too Small to Represent

A gradient 0.000001 becomes 0.001 when loss scale is 1000, survives backpropagation, and returns to 0.000001 after unscaling.

Run the loss scaling scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

## The calculation hidden inside loss scaling

Before Loss Scaling receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

A true gradient of 0.000001 may vanish in half precision. Before differentiation, make the loss one thousand times larger; every loss-derived gradient becomes 0.001 and survives. Before updating the weight, divide by the same thousand and recover 0.000001. S names this temporary magnifier, L the original loss, and g the restored gradient—the model has not been told to learn a thousand times faster.

L is original loss, S is a temporary positive scale, and g is the recovered gradient in the loss's original units.

### Why no cheaper operation does the same job

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) by S enlarges every loss-derived gradient before narrow arithmetic can erase it. [Division](../../MATHEMATICAL_MOVES.md#division) by the same S reverses that temporary unit change before the optimizer. Adding S would not proportionally enlarge tiny sensitivities and could not be undone uniformly.

Every symbol in Loss Scaling can now be read back into an action already performed. The whole procedure fits in one line:

$$
g=\frac{1}{S}\nabla_\theta(SL)
$$

## Where loss scaling runs out

A scale large enough to prevent underflow can cause overflow, so practical systems adjust it dynamically.

Why does that boundary remain? Loss Scaling was built for one responsibility: multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take loss scaling to the workbench

The argument for loss scaling is still provisional until a runnable case can make it fail. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running loss scaling, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the loss scaling result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Gradient Accumulation — Build a Large Batch That Does Not Fit](../170-gradient-accumulation/README.md)
