# Excavation 194 — Sharded Checkpoints — Save One Recoverable State Without Gathering It

<!-- book-prose-v2 -->

Three-dimensional parallelism spreads parameters, moments, gradients, and progress across many owners. Asking one coordinator to gather everything before saving can exceed its memory and stall the cluster.

Nothing yet appears to demand a new invention. We can let every worker write its local tensors and call the directory a checkpoint.

There is a real principle behind this restraint: the complexity of sharded checkpoints must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

Its hidden assumption becomes visible as soon as we observe that a worker fails before writing, two shards belong to different steps, or a filename is reused. The directory exists but cannot reconstruct one globally consistent training state.

That distinction is the hinge on which sharded checkpoints turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: write versioned shards to temporary locations, record hashes and ownership in a checkpoint manifest, and publish one atomic completion marker only after every required shard is durable.

We have earned the chapter's shorter name: **Sharded Checkpoints**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that sharded checkpoints is necessary rather than decorative. Delete its new responsibility and use the earlier plan to let every worker write its local tensors and call the directory a checkpoint. Immediately, a worker fails before writing, two shards belong to different steps, or a filename is reused. The directory exists but cannot reconstruct one globally consistent training state. Reintroduce the single job to write versioned shards to temporary locations, record hashes and ownership in a checkpoint manifest, and publish one atomic completion marker only after every required shard is durable. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can write versioned shards to temporary locations, record hashes and ownership in a checkpoint manifest, and publish one atomic completion marker only after every required shard is durable. Because the old plan to let every worker write its local tensors and call the directory a checkpoint is the only displaced piece, the reader can locate exactly where sharded checkpoints changes the outcome.

## Save One Recoverable State Without Gathering It

Twenty-four workers save step 8,000. The manifest expects twenty-four parameter shards, optimizer shards, scheduler state, RNG state, and data cursors; the checkpoint becomes eligible for recovery only when every recorded hash verifies.

The name sharded checkpoints is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

## Where sharded checkpoints runs out

A complete checkpoint limits lost work but consumes storage and I/O bandwidth; frequent synchronous saves can dominate training time.

The weakness is not an accidental footnote. Every operation in sharded checkpoints serves the narrower purpose to write versioned shards to temporary locations, record hashes and ownership in a checkpoint manifest, and publish one atomic completion marker only after every required shard is durable; none was designed to answer the new question. We have reached the honest edge of the invention.

## Take sharded checkpoints to the workbench

Understanding sharded checkpoints now means predicting its intermediate results before asking software for an answer. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running sharded checkpoints, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the sharded checkpoints result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Deterministic Resume — Continue the Same Experiment, Not a Similar One](../195-deterministic-resume/README.md)
