# Excavation 192 — Pipeline Parallelism — Stop Waiting for the Whole Model to Cross One Device at a Time

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Data parallel workers process different examples, but each replica still needs the model's sequential layers. Splitting those layers across devices makes only one device active if a whole batch traverses the stages at once.

At the Archive Foundry, the archivist-engineer returns to the chain-of-custody ledger. Yesterday's instrument still lies open, so the first move asks for no new magic: send one complete batch through stage one, then stage two, then stage three.

For a moment the mark looks complete. Then the evidence refuses to fit: while stage two works, stage one and stage three wait. The model fits, but most devices are idle for most of the step. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The archivist-engineer sketches the break before changing it:*

```text
observation
    │
    ▼
[send one complete batch through stage…]
    │
    ╳  while stage two works, stage one and…
    │
    ▼
[split the batch into micro-batches…]
```

The archivist-engineer lays two translucent sheets over the chain-of-custody ledger. The first is inscribed, “send one complete batch through stage one, then stage two, then stage three.” Its path ends where while stage two works, stage one and stage three wait. The model fits, but most devices are idle for most of the step. The second receives the same evidence but is allowed to split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently. Held to the light, the sheets separate at exactly one decision.

No one reaches for a pipeline parallelism formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The archivist-engineer changes only that one responsibility: split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently. When the ink dries, the name **Pipeline Parallelism** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The chain-of-custody ledger keeps both histories. Its older mark still says, ‘send one complete batch through stage one, then stage two, then stage three’; beside it, the newer mark says, ‘split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently.’ The distance between those sentences is the exact shape of pipeline parallelism: no larger than the failure required, and no smaller than reality permits.

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
