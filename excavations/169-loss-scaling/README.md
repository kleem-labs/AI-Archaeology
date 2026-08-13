# Excavation 169 — Loss Scaling — Rescue Gradients Too Small to Represent

The forward pass looks correct, but some half-precision gradients round to zero before the optimizer can use them.

Perhaps we increase the learning rate so small updates become visible.

It survives until the measured run answers back. The learning rate acts after gradients are formed; it cannot recover values that already underflowed to zero, and it enlarges every surviving update.

Now the missing requirement is concrete. Multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating.

## Let one run decide

A gradient 0.000001 becomes 0.001 when loss scale is 1000, survives backpropagation, and returns to 0.000001 after unscaling.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

A true gradient of 0.000001 may vanish in half precision. Before differentiation, make the loss one thousand times larger; every loss-derived gradient becomes 0.001 and survives. Before updating the weight, divide by the same thousand and recover 0.000001. S names this temporary magnifier, L the original loss, and g the restored gradient—the model has not been told to learn a thousand times faster.

L is original loss, S is a temporary positive scale, and g is the recovered gradient in the loss's original units.

### Why these operations are forced

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) by S enlarges every loss-derived gradient before narrow arithmetic can erase it. [Division](../../MATHEMATICAL_MOVES.md#division) by the same S reverses that temporary unit change before the optimizer. Adding S would not proportionally enlarge tiny sensitivities and could not be undone uniformly.

Only now can we compress the procedure:

$$
g=\frac{1}{S}\nabla_\theta(SL)
$$

## What this repair cannot do

A scale large enough to prevent underflow can cause overflow, so practical systems adjust it dynamically.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Gradient Accumulation — Build a Large Batch That Does Not Fit](../170-gradient-accumulation/README.md)
