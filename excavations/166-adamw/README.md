# Excavation 166 — AdamW — Keep Shrinkage Separate from Adaptation

Adam trains the block, but adding an L2 penalty to the loss sends shrinkage through the optimizer's coordinate-wise rescaling.

Perhaps we treat penalty gradients and data gradients identically because both appear in one total loss.

It survives until the measured run answers back. Coordinates with different gradient histories receive different effective shrinkage even when the intended rule was to decay all selected weights at one rate.

Now the missing requirement is concrete. Apply Adam's adaptive data update and parameter decay as separate operations.

## Let one run decide

Two equal weights with different gradient histories receive different Adam steps but the same proportional decay.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

Suppose two weights both equal 2, although their gradient histories differ. If decay means 'remove one tenth of one percent of the present weight this step,' both should lose the same proportion before their evidence-driven Adam movements differ. Multiplying theta by 1−eta lambda performs that direct shrink. The separate subtraction then applies Adam's learned direction, preventing gradient history from secretly changing the intended decay rule.

lambda is decay strength; the first term shrinks the old parameter directly; the second is Adam's data-driven update.

### Why these operations are forced

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) by 1−eta lambda makes decay proportional to current parameter size: a zero weight stays zero and doubling a weight doubles shrinkage. [Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) then applies the independently adapted loss step. Hiding decay inside m and v would mix two jobs the formula deliberately separates.

Only now can we compress the procedure:

$$
\theta_{t+1}=(1-\eta\lambda)\theta_t-\eta\frac{\widehat m_t}{\sqrt{\widehat v_t}+\epsilon}
$$

## What this repair cannot do

Decoupled decay still requires choosing which parameters to decay and how strongly.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Gradient Clipping — Stop One Shock from Becoming a Catastrophe](../167-gradient-clipping/README.md)
