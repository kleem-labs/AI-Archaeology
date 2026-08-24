# Excavation 194 — Sharded Checkpoints — Save One Recoverable State Without Gathering It

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Three-dimensional parallelism spreads parameters, moments, gradients, and progress across many owners. Asking one coordinator to gather everything before saving can exceed its memory and stall the cluster.

The chain-of-custody ledger at the Archive Foundry still carries the marks of the previous discovery. The archivist-engineer follows them as far as they seem willing to go: let every worker write its local tensors and call the directory a checkpoint.

Reality answers without terminology: a worker fails before writing, two shards belong to different steps, or a filename is reused. The directory exists but cannot reconstruct one globally consistent training state. The chain-of-custody ledger now holds two situations the old rule cannot keep apart.

*The archivist-engineer sketches the break before changing it:*

```text
OLD PATH:  request ──▶ let every worker write its local… ──▶ a worker fails before writing, two…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ write versioned shards to temporary… ──▶ accountable result
```

The chain-of-custody ledger is divided down the middle. Left side: “let every worker write its local tensors and call the directory a checkpoint.” Its final mark records a worker fails before writing, two shards belong to different steps, or a filename is reused. The directory exists but cannot reconstruct one globally consistent training state. Right side: the same starting evidence, now allowed to write versioned shards to temporary locations, record hashes and ownership in a checkpoint manifest, and publish one atomic completion marker only after every required shard is durable. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given sharded checkpoints a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: write versioned shards to temporary locations, record hashes and ownership in a checkpoint manifest, and publish one atomic completion marker only after every required shard is durable. The name **Sharded Checkpoints** arrives afterward, like a title given to a path whose stones are already underfoot.

A thread now runs backward from sharded checkpoints through the room. Tug it and the repair disappears; tug again and the old rule returns; follow that rule to its end and a worker fails before writing, two shards belong to different steps, or a filename is reused. The directory exists but cannot reconstruct one globally consistent training state. The mathematics is not a collection of names but a chain of consequences that can be walked in either direction.

## Save One Recoverable State Without Gathering It

Twenty-four workers save step 8,000. The manifest expects twenty-four parameter shards, optimizer shards, scheduler state, RNG state, and data cursors; the checkpoint becomes eligible for recovery only when every recorded hash verifies.

## Where sharded checkpoints runs out

A complete checkpoint limits lost work but consumes storage and I/O bandwidth; frequent synchronous saves can dominate training time.

A final test reaches beyond the new instrument. It does not refute Sharded Checkpoints; it reveals the edge of what was constructed. The archivist-engineer carries that edge into the following room.

## Return to the chain-of-custody ledger

Rebuild the sharded checkpoints scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Deterministic Resume — Continue the Same Experiment, Not a Similar One](../195-deterministic-resume/README.md)
