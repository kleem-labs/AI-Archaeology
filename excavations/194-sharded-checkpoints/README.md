# Excavation 194 — Sharded Checkpoints — Save One Recoverable State Without Gathering It

Three-dimensional parallelism spreads parameters, moments, gradients, and progress across many owners. Asking one coordinator to gather everything before saving can exceed its memory and stall the cluster.

Perhaps we let every worker write its local tensors and call the directory a checkpoint.

But the run answers back. A worker fails before writing, two shards belong to different steps, or a filename is reused. The directory exists but cannot reconstruct one globally consistent training state.

The failure leaves one precise requirement. Write versioned shards to temporary locations, record hashes and ownership in a checkpoint manifest, and publish one atomic completion marker only after every required shard is durable.

## Let one run decide

Twenty-four workers save step 8,000. The manifest expects twenty-four parameter shards, optimizer shards, scheduler state, RNG state, and data cursors; the checkpoint becomes eligible for recovery only when every recorded hash verifies.

## What this repair cannot do

A complete checkpoint limits lost work but consumes storage and I/O bandwidth; frequent synchronous saves can dominate training time.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Deterministic Resume — Continue the Same Experiment, Not a Similar One](../195-deterministic-resume/README.md)
