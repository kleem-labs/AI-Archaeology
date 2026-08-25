# Excavation 193 — Three-Dimensional Parallelism — Give Each Memory Wall Its Own Axis

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Data and pretraining operations

Pipeline micro-batches keep layer stages busy. A large run may still exceed memory inside one layer, require more independent data witnesses, and contain too many layers for one device group.

The previous discovery reaches the Archive Foundry carrying one unfinished problem. Beside the chain-of-custody ledger, the archivist-engineer first tries to increase whichever parallel technique was introduced most recently until the model fits.

There is good reason to begin this way. If we increase whichever parallel technique was introduced most recently until the model fits, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: more pipeline stages increase bubbles, more tensor splits increase frequent communication, and more data replicas preserve full model memory. One axis cannot solve three different limits efficiently.

This failure cannot be repaired by performing the instruction to increase whichever parallel technique was introduced most recently until the model fits more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the chain-of-custody ledger; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Three-Dimensional Parallelism**. The name is simply a handle for the distinction already reconstructed.

## Give Each Memory Wall Its Own Axis

Two tensor workers form each layer, four pipeline stages hold the depth, and three data replicas see different examples. The run uses 2×4×3=24 workers with each axis performing one named job.

## The calculation hidden inside three-dimensional parallelism

The archivist-engineer carries the three-dimensional parallelism scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Each factor counts independent choices along one model-parallel axis. Selecting one tensor rank, one pipeline rank, and one data rank identifies exactly one worker; P_total counts all such combinations.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced by the product rule: every choice on one axis pairs with every choice on the others. Addition would count axis labels rather than workers. [Equality](../../MATHEMATICAL_MOVES.md#equals) assumes the grid is fully populated.

The calculation borrows several gestures already encountered elsewhere: **the lock and key**—one influence matters through another, and either missing factor can close the path. three-dimensional parallelism feels new because the objects are new; the gestures remain recognizably human.

The archivist-engineer reads the journey of three-dimensional parallelism once more across the chain-of-custody ledger, then lets the words contract without losing their order:

$$
P_{\text{total}}=P_{\text{tensor}}P_{\text{pipeline}}P_{\text{data}}
$$

## Where three-dimensional parallelism runs out

Three-dimensional parallelism increases coordination and configuration complexity; a poor mapping to the physical network can spend more time communicating than computing.

The chain-of-custody ledger answers today's question and falls silent at the next. That silence is precise: Three-Dimensional Parallelism was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the chain-of-custody ledger

Rebuild the three-dimensional parallelism scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Sharded Checkpoints — Save One Recoverable State Without Gathering It](../194-sharded-checkpoints/README.md)
