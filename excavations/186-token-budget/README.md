# Excavation 186 — The Token Budget — Convert a Training Plan into a Count of Lessons

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Information Theory](../../MATHEMATICS_ATLAS.md#information)
>
> **Applied territory:** Data and pretraining operations

Seeded mixture sampling can produce an ordered stream. The run still says “train for a while,” so neither cost nor source exposure is bounded.

A new case arrives at the Archive Foundry. Nothing yet demands a new invention, so the archivist-engineer uses the chain-of-custody ledger to stop when the wall clock reaches an affordable date.

This is precisely the kind of shortcut a careful builder should try first. The instruction to stop when the wall clock reaches an affordable date preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: faster hardware sees more tokens, interruptions see fewer, and two runs with the same calendar budget teach different amounts of evidence.

The counterexample separates two questions that the attempt to stop when the wall clock reaches an affordable date had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the chain-of-custody ledger fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **The Token Budget**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## Convert a Training Plan into a Count of Lessons

A tiny run uses 2,000 updates with 32 sequences of 128 real tokens each. Every update carries 4,096 lessons, so the complete plan exposes 8,192,000 tokens.

## The calculation hidden inside the token budget

The archivist-engineer carries the token budget scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

T is the planned number of optimizer updates, B_tokens counts real loss-bearing tokens in one global batch, and N_tokens is the complete exposure budget.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) appears because every one of T updates consumes B_tokens lessons. Addition would count only one update plus one batch. Padding is excluded because it occupies hardware but contributes no language target.

Three old motions cast new shadows here: **the lock and key**—one influence matters through another, and either missing factor can close the path. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Every mark needed for token budget is now visible on the chain-of-custody ledger. The symbols do not add an idea; they bind the discovered moves into one line:

$$
N_{\text{tokens}}=T B_{\text{tokens}}
$$

## Where the token budget runs out

Equal token counts do not imply equal compute when model size, sequence length, sparsity, or hardware efficiency differs.

At the Archive Foundry, the archivist-engineer leaves a blank beneath the new mark. Token Budget has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the chain-of-custody ledger

Rebuild the token budget scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Compute-Optimal Allocation — Buy a Larger Memory or More Experience?](../187-compute-optimal-allocation/README.md)
