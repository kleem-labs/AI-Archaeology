# Excavation 191 — Data Parallelism — Let Several Workers Observe Different Evidence

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Data and pretraining operations

Gradient noise measurements choose a useful global batch. One device cannot process that batch quickly enough, even though the modern model and optimizer state now fit through sharding.

Nothing in the Archive Foundry yet bears today's mathematical name. There is only the archivist-engineer, the chain-of-custody ledger, and one plausible action: send the same mini-batch to every worker and average their gradients.

At the edge of the chain-of-custody ledger, the shortcut produces its consequence: all workers repeat the same computation and return the same evidence, so hardware cost rises without increasing batch diversity or reducing step time meaningfully. That consequence, not a textbook, earns the next move.

*The archivist-engineer sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: send the same mini-batch to every…
                         │
                         └── mismatch: all workers repeat the same…

reference evidence ──▶ measured repair: replicate the current model view,…
```

The archivist-engineer covers the new mark and the old contradiction returns: all workers repeat the same computation and return the same evidence, so hardware cost rises without increasing batch diversity or reducing step time meaningfully. The cover is lifted, restoring the ability to replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason data parallelism exists.

What must change for data parallelism is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update. That threshold is where **Data Parallelism** enters the story.

The marks on the chain-of-custody ledger form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. data parallelism is not any single point. It is the path connecting them in the only order that makes the last point necessary.

<!-- memory-film-v1:start -->
> **Memory realm 13 of 18 — [Archive Foundry](../../MEMORY_PALACE.md#realm-13)**
>
> **The question carried into this chamber:** What fails if we send the same mini-batch to every worker and average their gradients?

## When the chamber changes

Keep the formal name Data Parallelism covered for another moment. The surviving image is enough to rebuild it.

First hold the failed picture still: The prism follows the tempting path—send the same mini-batch to every worker and average their gradients. Then the evidence answers: all workers repeat the same computation and return the same evidence, so hardware cost rises without increasing batch diversity or reducing step time meaningfully.

Now let the chamber move: The archivist-engineer changes one moving part. The prism can now replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update.

The object that should remain after the terminology disappears is **the data parallelism prism mounted on the chain-of-custody ledger**.

> **Memory seal — Data Parallelism**
>
> Data Parallelism keeps the missing power: replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update.

Give the idea a bodily path: Touch the data parallelism prism in imagination: tap five fingertips in order—question, object, failure, transformation, seal—without saying the formal name.
<!-- memory-film-v1:end -->

## Let Several Workers Observe Different Evidence

Four workers each read eight different sequences. Their four average gradients become one average over thirty-two sequences before any worker advances the parameters.

## The calculation hidden inside data parallelism

The archivist-engineer carries the data parallelism scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

P is the number of data-parallel workers, g_p is worker p's average gradient from different examples, and g is the single gradient used by the shared optimizer step.

### Why the melody needs these exact notes

[Summation](../../MATHEMATICAL_MOVES.md#summation) lets every worker's independent evidence contribute. [Division](../../MATHEMATICAL_MOVES.md#division) returns advice per worker so adding hardware does not enlarge the update by itself. Multiplication would let a zero coordinate from one worker erase all others.

Before the line is compressed, notice its recurring motions: **the chorus**—many witnesses contribute to one answer without one silence erasing the rest; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. They are the handholds by which the reader can later climb back from notation to meaning.

The chain-of-custody ledger already contains the complete data parallelism mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
g=\frac1P\sum_{p=1}^{P}g_p
$$

## Where data parallelism runs out

Because one shared update cannot proceed until every worker's evidence has joined the average, synchronous data parallelism waits for the slowest worker and communicates a full update's worth of gradient information.

Here the new path ends honestly. Data Parallelism can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the chain-of-custody ledger

Rebuild the data parallelism scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Pipeline Parallelism — Stop Waiting for the Whole Model to Cross One Device at a Time](../192-pipeline-parallelism/README.md)
