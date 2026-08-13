# Excavation 170 — Gradient Accumulation — Build a Large Batch That Does Not Fit

The optimizer needs a less noisy effective batch, but all its examples and activations cannot coexist on one device.

Perhaps we reduce the batch until it fits and change nothing else.

It survives until the measured run answers back. The gradient becomes noisier and the training regime changes; increasing the learning rate cannot recreate evidence never averaged together.

Now the missing requirement is concrete. Run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step.

## Let one run decide

Four micro-batches of eight examples create one effective batch of thirty-two while only eight examples' activations are resident at a time.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

Imagine four small tables of eight examples arriving one after another. Each table gives its own average advice about the weights, but none is allowed to update yet. Add the four pieces of advice into one pending total, then share that total across the four witnesses. K counts those witnesses, g_k names one witness's advice, and g_effective is what the single optimizer step hears.

K is the number of micro-batches and g_k is the gradient average produced by micro-batch k of equal size.

### Why these operations are forced

[Summation](../../MATHEMATICAL_MOVES.md#summation) lets every micro-batch contribute to the same pending update. [Division](../../MATHEMATICAL_MOVES.md#division) returns advice per micro-batch so increasing K does not enlarge the step by itself. Multiplication would let a zero coordinate in one micro-batch erase all others.

Only now can we compress the procedure:

$$
g_{\text{effective}}=\frac1K\sum_{k=1}^{K}g_k
$$

## What this repair cannot do

Accumulation lowers activation memory but adds serial work and does not reduce parameter or optimizer-state memory.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Activation Checkpointing — Remember Less, Recompute Exactly](../171-activation-checkpointing/README.md)
