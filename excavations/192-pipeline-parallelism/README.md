# Excavation 192 — Pipeline Parallelism — Stop Waiting for the Whole Model to Cross One Device at a Time

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Data and pretraining operations

Data parallel workers process different examples, but each replica still needs the model's sequential layers. Splitting those layers across devices makes only one device active if a whole batch traverses the stages at once.

At the Archive Foundry, the archivist-engineer meets the next case beside the chain-of-custody ledger. The nearest idea is also the most reasonable one: send one complete batch through stage one, then stage two, then stage three.

The attraction of this attempt is easy to see. To send one complete batch through stage one, then stage two, then stage three reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: while stage two works, stage one and stage three wait. The model fits, but most devices are idle for most of the step.

The contradiction matters because it identifies a structural loss in the instruction to send one complete batch through stage one, then stage two, then stage three, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The chain-of-custody ledger will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Pipeline Parallelism**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

## Stop Waiting for the Whole Model to Cross One Device at a Time

With four pipeline stages and eight micro-batches, the first few clock slots fill the pipeline, eight slots carry useful work, and the last few drain it. More micro-batches shrink the idle fraction.

## The calculation hidden inside pipeline parallelism

The archivist-engineer carries the pipeline parallelism scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

m is the number of model micro-batches and p the number of pipeline stages in a simple forward pipeline. Useful work occupies m slots; filling and draining add p−1 slots; U is the idealized occupied share.

### Why the melody needs these exact notes

[Addition](../../MATHEMATICAL_MOVES.md#addition) joins useful slots with unavoidable fill-and-drain slots. [Division](../../MATHEMATICAL_MOVES.md#division) turns useful slots into a share of total schedule time. Multiplying m and p would count stage-tasks, not the fraction of time one stage remains usefully occupied.

Listen beneath pipeline parallelism: **the joining river**—separate contributions meet without losing where they came from; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. These are not ornamental comparisons. Each image keeps the exact job of an operation visible while its symbols change.

Every mark needed for pipeline parallelism is now visible on the chain-of-custody ledger. The symbols do not add an idea; they bind the discovered moves into one line:

$$
U=\frac{m}{m+p-1}
$$

## Where pipeline parallelism runs out

Because sequential layer dependencies require the pipeline to fill and drain, pipeline parallelism introduces bubbles and activation transfers; making micro-batches too small can then reduce the efficiency of each matrix operation.

At the Archive Foundry, the archivist-engineer leaves a blank beneath the new mark. Pipeline Parallelism has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the chain-of-custody ledger

Rebuild the pipeline parallelism scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Three-Dimensional Parallelism — Give Each Memory Wall Its Own Axis](../193-three-dimensional-parallelism/README.md)
