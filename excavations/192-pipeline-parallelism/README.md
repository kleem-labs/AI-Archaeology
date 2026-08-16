# Excavation 192 — Pipeline Parallelism — Stop Waiting for the Whole Model to Cross One Device at a Time

Data parallel workers process different examples, but each replica still needs the model's sequential layers. Splitting those layers across devices makes only one device active if a whole batch traverses the stages at once.

Using what we have, we send one complete batch through stage one, then stage two, then stage three.

The plan survives only until the evidence is counted. While stage two works, stage one and stage three wait. The model fits, but most devices are idle for most of the step.

The lost information tells us what must come next. Split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently.

## Let one run decide

With four pipeline stages and eight micro-batches, the first few clock slots fill the pipeline, eight slots carry useful work, and the last few drain it. More micro-batches shrink the idle fraction.

## The arithmetic we have earned

m is the number of model micro-batches and p the number of pipeline stages in a simple forward pipeline. Useful work occupies m slots; filling and draining add p−1 slots; U is the idealized occupied share.

### Why these operations are forced

[Addition](../../MATHEMATICAL_MOVES.md#addition) joins useful slots with unavoidable fill-and-drain slots. [Division](../../MATHEMATICAL_MOVES.md#division) turns useful slots into a share of total schedule time. Multiplying m and p would count stage-tasks, not the fraction of time one stage remains usefully occupied.

Only now can we compress the procedure:

$$
U=\frac{m}{m+p-1}
$$

## What this repair cannot do

Because sequential layer dependencies require the pipeline to fill and drain, pipeline parallelism introduces bubbles and activation transfers; making micro-batches too small can then reduce the efficiency of each matrix operation.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Three-Dimensional Parallelism — Give Each Memory Wall Its Own Axis](../193-three-dimensional-parallelism/README.md)
