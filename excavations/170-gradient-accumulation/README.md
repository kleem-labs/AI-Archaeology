# Excavation 170 — Gradient Accumulation — Build a Large Batch That Does Not Fit

<!-- book-prose-v2 -->

The optimizer needs a less noisy effective batch, but all its examples and activations cannot coexist on one device.

Nothing yet appears to demand a new invention. We can reduce the batch until it fits and change nothing else.

There is a real principle behind this restraint: the complexity of gradient accumulation must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

Its hidden assumption becomes visible as soon as we observe that the gradient becomes noisier and the training regime changes; increasing the learning rate cannot recreate evidence never averaged together.

That distinction is the hinge on which gradient accumulation turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step.

We have earned the chapter's shorter name: **Gradient Accumulation**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that gradient accumulation is necessary rather than decorative. Delete its new responsibility and use the earlier plan to reduce the batch until it fits and change nothing else. Immediately, the gradient becomes noisier and the training regime changes; increasing the learning rate cannot recreate evidence never averaged together. Reintroduce the single job to run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step. Because the old plan to reduce the batch until it fits and change nothing else is the only displaced piece, the reader can locate exactly where gradient accumulation changes the outcome.

## Build a Large Batch That Does Not Fit

Four micro-batches of eight examples create one effective batch of thirty-two while only eight examples' activations are resident at a time.

The name gradient accumulation is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

## The calculation hidden inside gradient accumulation

Do not read the coming Gradient Accumulation line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Imagine four small tables of eight examples arriving one after another. Each table gives its own average advice about the weights, but none is allowed to update yet. Add the four pieces of advice into one pending total, then share that total across the four witnesses. K counts those witnesses, g_k names one witness's advice, and g_effective is what the single optimizer step hears.

K is the number of micro-batches and g_k is the gradient average produced by micro-batch k of equal size.

### Why no cheaper operation does the same job

[Summation](../../MATHEMATICAL_MOVES.md#summation) lets every micro-batch contribute to the same pending update. [Division](../../MATHEMATICAL_MOVES.md#division) returns advice per micro-batch so increasing K does not enlarge the step by itself. Multiplication would let a zero coordinate in one micro-batch erase all others.

Every symbol in Gradient Accumulation can now be read back into an action already performed. The whole procedure fits in one line:

$$
g_{\text{effective}}=\frac1K\sum_{k=1}^{K}g_k
$$

## Where gradient accumulation runs out

Accumulation lowers activation memory but adds serial work and does not reduce parameter or optimizer-state memory.

The weakness is not an accidental footnote. Every operation in gradient accumulation serves the narrower purpose to run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step; none was designed to answer the new question. We have reached the honest edge of the invention.

## Take gradient accumulation to the workbench

Understanding gradient accumulation now means predicting its intermediate results before asking software for an answer. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running gradient accumulation, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the gradient accumulation result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Activation Checkpointing — Remember Less, Recompute Exactly](../171-activation-checkpointing/README.md)
