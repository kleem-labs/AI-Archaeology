# Excavation 192 — Pipeline Parallelism — Stop Waiting for the Whole Model to Cross One Device at a Time

<!-- book-prose-v2 -->

Data parallel workers process different examples, but each replica still needs the model's sequential layers. Splitting those layers across devices makes only one device active if a whole batch traverses the stages at once.

The least expensive next move is to send one complete batch through stage one, then stage two, then stage three.

The proposal deserves a fair hearing. For pipeline parallelism, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Now keep that rule fixed and let the difficult case enter: while stage two works, stage one and stage three wait. The model fits, but most devices are idle for most of the step.

The failure changes the question behind pipeline parallelism. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently.

Only at this point does the inherited name **Pipeline Parallelism** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of pipeline parallelism by mentally removing the repair. We fall back to the proposal to send one complete batch through stage one, then stage two, then stage three; then while stage two works, stage one and stage three wait. The model fits, but most devices are idle for most of the step. Restore only the ability to split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to send one complete batch through stage one, then stage two, then stage three to requiring the system to split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to pipeline parallelism.

## Stop Waiting for the Whole Model to Cross One Device at a Time

With four pipeline stages and eight micro-batches, the first few clock slots fill the pipeline, eight slots carry useful work, and the last few drain it. More micro-batches shrink the idle fraction.

Put the old procedure beside pipeline parallelism. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## The calculation hidden inside pipeline parallelism

Do not read the coming Pipeline Parallelism line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

m is the number of model micro-batches and p the number of pipeline stages in a simple forward pipeline. Useful work occupies m slots; filling and draining add p−1 slots; U is the idealized occupied share.

### Why no cheaper operation does the same job

[Addition](../../MATHEMATICAL_MOVES.md#addition) joins useful slots with unavoidable fill-and-drain slots. [Division](../../MATHEMATICAL_MOVES.md#division) turns useful slots into a share of total schedule time. Multiplying m and p would count stage-tasks, not the fraction of time one stage remains usefully occupied.

Every symbol in Pipeline Parallelism can now be read back into an action already performed. The whole procedure fits in one line:

$$
U=\frac{m}{m+p-1}
$$

## Where pipeline parallelism runs out

Because sequential layer dependencies require the pipeline to fill and drain, pipeline parallelism introduces bubbles and activation transfers; making micro-batches too small can then reduce the efficiency of each matrix operation.

The limit follows from the job assigned to pipeline parallelism. Its repair knows how to split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take pipeline parallelism to the workbench

A claim about pipeline parallelism now exists on the page; the laboratory must be able to contradict it. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running pipeline parallelism, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the pipeline parallelism result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Three-Dimensional Parallelism — Give Each Memory Wall Its Own Axis](../193-three-dimensional-parallelism/README.md)
