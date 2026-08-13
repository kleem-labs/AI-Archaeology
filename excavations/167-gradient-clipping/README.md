# Excavation 167 — Gradient Clipping — Stop One Shock from Becoming a Catastrophe

Most steps are stable, but a rare batch produces an enormous global gradient norm and overwhelms Adam's still-developing moment estimates.

Perhaps we discard the entire batch whenever any gradient coordinate looks large.

It survives until the measured run answers back. Useful directional evidence is lost, and one arbitrary coordinate threshold ignores the size of the full update vector.

Now the missing requirement is concrete. Preserve the gradient's direction but scale its whole norm down only when it exceeds a chosen ceiling.

## Let one run decide

A gradient of length 20 with ceiling 5 is multiplied by one quarter. A gradient of length 3 passes unchanged.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

The model's current gradient points in a useful direction but has length 20, while this run permits length 5. The required scale is 5/20, or one quarter, so every component shrinks by one quarter and direction survives. If the next gradient has length 3, the fraction 5/3 would enlarge it—exactly what we do not want—so we cap the multiplier at 1. We call the ceiling c, the original advice g, and the safe advice g-prime.

g is the original gradient vector, c is the allowed norm ceiling, and g-prime is the gradient actually given to the optimizer.

### Why these operations are forced

[Division](../../MATHEMATICAL_MOVES.md#division) computes the fraction needed to bring the current norm down to c. [Minimum](../../MATHEMATICAL_MOVES.md#minimum) chooses at most one, so small gradients are never enlarged. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) scales every coordinate equally, preserving direction; clipping coordinates separately would rotate the update.

Only now can we compress the procedure:

$$
g^{\prime}=g\min\left(1,\frac{c}{\lVert g\rVert}\right)
$$

## What this repair cannot do

Clipping limits damage; it can hide a broken loss, corrupt data, or an unsuitable learning rate if used without diagnosis.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Mixed Precision — Stop Storing Every Number with Unneeded Detail](../168-mixed-precision/README.md)
