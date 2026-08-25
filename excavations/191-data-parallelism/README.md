# Excavation 191 — Data Parallelism — Let Several Workers Observe Different Evidence

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Data and pretraining operations

Gradient noise measurements choose a useful global batch. One device cannot process that batch quickly enough, even though the modern model and optimizer state now fit through sharding.

Inside the Archive Foundry, the old method is given an honest chance. The archivist-engineer places the evidence on the chain-of-custody ledger and tries to send the same mini-batch to every worker and average their gradients.

Nothing about this first move is careless. To send the same mini-batch to every worker and average their gradients is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: all workers repeat the same computation and return the same evidence, so hardware cost rises without increasing batch diversity or reducing step time meaningfully.

The important discovery is not merely that trying to send the same mini-batch to every worker and average their gradients failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the chain-of-custody ledger, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Data Parallelism**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## Let Several Workers Observe Different Evidence

Four workers each read eight different sequences. Their four average gradients become one average over thirty-two sequences before any worker advances the parameters.

## The calculation hidden inside data parallelism

The archivist-engineer carries the data parallelism scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

P is the number of data-parallel workers, g_p is worker p's average gradient from different examples, and g is the single gradient used by the shared optimizer step.

### Why the melody needs these exact notes

[Summation](../../MATHEMATICAL_MOVES.md#summation) lets every worker's independent evidence contribute. [Division](../../MATHEMATICAL_MOVES.md#division) returns advice per worker so adding hardware does not enlarge the update by itself. Multiplication would let a zero coordinate from one worker erase all others.

The calculation reuses familiar motions: **the chorus**—many witnesses contribute to one answer without one silence erasing the rest; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. Together they keep the path from the concrete case to notation intact.

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
