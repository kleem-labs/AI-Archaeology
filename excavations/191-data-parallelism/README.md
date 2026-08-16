# Excavation 191 — Data Parallelism — Let Several Workers Observe Different Evidence

Gradient noise measurements choose a useful global batch. One device cannot process that batch quickly enough, even though the modern model and optimizer state now fit through sharding.

At first we send the same mini-batch to every worker and average their gradients.

Reality objects. All workers repeat the same computation and return the same evidence, so hardware cost rises without increasing batch diversity or reducing step time meaningfully.

That evidence forces a repair. Replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update.

## Let one run decide

Four workers each read eight different sequences. Their four average gradients become one average over thirty-two sequences before any worker advances the parameters.

## The arithmetic we have earned

P is the number of data-parallel workers, g_p is worker p's average gradient from different examples, and g is the single gradient used by the shared optimizer step.

### Why these operations are forced

[Summation](../../MATHEMATICAL_MOVES.md#summation) lets every worker's independent evidence contribute. [Division](../../MATHEMATICAL_MOVES.md#division) returns advice per worker so adding hardware does not enlarge the update by itself. Multiplication would let a zero coordinate from one worker erase all others.

Only now can we compress the procedure:

$$
g=\frac1P\sum_{p=1}^{P}g_p
$$

## What this repair cannot do

Because one shared update cannot proceed until every worker's evidence has joined the average, synchronous data parallelism waits for the slowest worker and communicates a full update's worth of gradient information.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Pipeline Parallelism — Stop Waiting for the Whole Model to Cross One Device at a Time](../192-pipeline-parallelism/README.md)
