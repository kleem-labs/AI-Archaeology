# Excavation 170 — Gradient Accumulation — Build a Large Batch That Does Not Fit

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Calculus & Differential Change](../../MATHEMATICS_ATLAS.md#calculus) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

The optimizer needs a less noisy effective batch, but all its examples and activations cannot coexist on one device.

The brass reference machine at the Engine Cavern still carries the marks of the previous discovery. The enginewright follows them as far as they seem willing to go: reduce the batch until it fits and change nothing else.

Reality answers without terminology: the gradient becomes noisier and the training regime changes; increasing the learning rate cannot recreate evidence never averaged together. The brass reference machine now holds two situations the old rule cannot keep apart.

*The enginewright sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   reduce the batch until it fits and… the gradient becomes noisier and the…
            \        /
             \      /
              run several micro-batches, sum their…
```

The brass reference machine is divided down the middle. Left side: “reduce the batch until it fits and change nothing else.” Its final mark records the gradient becomes noisier and the training regime changes; increasing the learning rate cannot recreate evidence never averaged together. Right side: the same starting evidence, now allowed to run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given gradient accumulation a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step. The name **Gradient Accumulation** arrives afterward, like a title given to a path whose stones are already underfoot.

A thread now runs backward from gradient accumulation through the room. Tug it and the repair disappears; tug again and the old rule returns; follow that rule to its end and the gradient becomes noisier and the training regime changes; increasing the learning rate cannot recreate evidence never averaged together. The mathematics is not a collection of names but a chain of consequences that can be walked in either direction.

<!-- memory-film-v1:start -->
> **Memory realm 12 of 18 — [Engine Cavern](../../MEMORY_PALACE.md#realm-12)**
>
> **The question carried into this chamber:** What fails if we reduce the batch until it fits and change nothing else?

## When the chamber changes

The Gradient Accumulation room does not ask you to memorize its name. It asks you to watch one object change.

First hold the failed picture still: The gate follows the tempting path—reduce the batch until it fits and change nothing else. Then the evidence answers: the gradient becomes noisier and the training regime changes; increasing the learning rate cannot recreate evidence never averaged together.

Now let the chamber move: The enginewright changes one moving part. The gate can now run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step.

The object that should remain after the terminology disappears is **the gradient accumulation gate mounted on the brass reference machine**.

> **Memory seal — Gradient Accumulation**
>
> Gradient Accumulation keeps the missing power: run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step.

Give the idea a bodily path: Touch the gradient accumulation gate in imagination: draw the old path in the air, stop sharply at its failure, and finish with the new motion.
<!-- memory-film-v1:end -->

## Build a Large Batch That Does Not Fit

Four micro-batches of eight examples create one effective batch of thirty-two while only eight examples' activations are resident at a time.

## The calculation hidden inside gradient accumulation

The enginewright carries the gradient accumulation scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Imagine four small tables of eight examples arriving one after another. Each table gives its own average advice about the weights, but none is allowed to update yet. Add the four pieces of advice into one pending total, then share that total across the four witnesses. K counts those witnesses, g_k names one witness's advice, and g_effective is what the single optimizer step hears.

K is the number of micro-batches and g_k is the gradient average produced by micro-batch k of equal size.

### Why the melody needs these exact notes

[Summation](../../MATHEMATICAL_MOVES.md#summation) lets every micro-batch contribute to the same pending update. [Division](../../MATHEMATICAL_MOVES.md#division) returns advice per micro-batch so increasing K does not enlarge the step by itself. Multiplication would let a zero coordinate in one micro-batch erase all others.

Three old motions cast new shadows here: **the chorus**—many witnesses contribute to one answer without one silence erasing the rest; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Nothing remains unnamed in the gradient accumulation case on the brass reference machine. We can finally trade the long route for its compact map:

$$
g_{\text{effective}}=\frac1K\sum_{k=1}^{K}g_k
$$

## Where gradient accumulation runs out

Accumulation lowers activation memory but adds serial work and does not reduce parameter or optimizer-state memory.

A final test reaches beyond the new instrument. It does not refute Gradient Accumulation; it reveals the edge of what was constructed. The enginewright carries that edge into the following room.

## Return to the brass reference machine

Rebuild the gradient accumulation scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Activation Checkpointing — Remember Less, Recompute Exactly](../171-activation-checkpointing/README.md)
