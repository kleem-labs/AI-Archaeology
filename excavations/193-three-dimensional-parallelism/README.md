# Excavation 193 — Three-Dimensional Parallelism — Give Each Memory Wall Its Own Axis

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Data and pretraining operations

Pipeline micro-batches keep layer stages busy. A large run may still exceed memory inside one layer, require more independent data witnesses, and contain too many layers for one device group.

Morning reaches the Archive Foundry before anyone has a name for today's difficulty. Beside the chain-of-custody ledger, the archivist-engineer tries the smallest continuation of what already works: increase whichever parallel technique was introduced most recently until the model fits.

The rule survives the easy cases. The next case leaves a crack through the middle of it: more pipeline stages increase bubbles, more tensor splits increase frequent communication, and more data replicas preserve full model memory. One axis cannot solve three different limits efficiently. More confidence cannot repair information that never entered the rule.

*The archivist-engineer sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   increase whichever parallel technique… more pipeline stages increase…
            \        /
             \      /
              compose tensor parallelism within…
```

Two trails now cross the chain-of-custody ledger. The pale trail bears the instruction “increase whichever parallel technique was introduced most recently until the model fits.” It disappears into the observed failure: more pipeline stages increase bubbles, more tensor splits increase frequent communication, and more data replicas preserve full model memory. One axis cannot solve three different limits efficiently. The darker trail carries one additional capacity—to compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed three-dimensional parallelism mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the chain-of-custody ledger is altered in exactly one way: compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost. Much later, people will call this territory **Three-Dimensional Parallelism**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the chain-of-custody ledger. The failed path remains visible beneath the repair, because three-dimensional parallelism is easier to remember when its scar remains attached to it. The scar reads, ‘more pipeline stages increase bubbles, more tensor splits increase frequent communication, and more data replicas preserve full model memory. One axis cannot solve three different limits efficiently’; the new line exists only to keep that loss from happening again.

<!-- memory-film-v1:start -->
> **Memory realm 13 of 18 — [Archive Foundry](../../MEMORY_PALACE.md#realm-13)**
>
> **The question carried into this chamber:** What fails if we increase whichever parallel technique was introduced most recently until the model fits?

## When the chamber changes

Before leaving Three-Dimensional Parallelism, replay the discovery as motion rather than as a definition.

First hold the failed picture still: The lens follows the tempting path—increase whichever parallel technique was introduced most recently until the model fits. Then the evidence answers: more pipeline stages increase bubbles, more tensor splits increase frequent communication, and more data replicas preserve full model memory. One axis cannot solve three different limits efficiently.

Now let the chamber move: The archivist-engineer changes one moving part. The lens can now compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost.

The object that should remain after the terminology disappears is **the three-dimensional parallelism lens mounted on the chain-of-custody ledger**.

> **Memory seal — Three-Dimensional Parallelism**
>
> Three-Dimensional Parallelism keeps the missing power: compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost.

Give the idea a bodily path: Touch the three-dimensional parallelism lens in imagination: hold both hands as the two failed alternatives, then move one hand through the repaired route.
<!-- memory-film-v1:end -->

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
