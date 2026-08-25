# Excavation 158 — Multi-Query Attention — Why Cache Separate Copies for Every Head?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

Caching turns repeated arithmetic into memory reads. Profiling now shows decoding limited by loading separate key and value histories for every attention head.

A new case arrives at the Engine Cavern. Nothing yet demands a new invention, so the enginewright uses the brass reference machine to preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections.

This is precisely the kind of shortcut a careful builder should try first. The instruction to preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: the caches grow with both sequence length and head count, and loading them dominates the arithmetic for one new token.

The counterexample separates two questions that the attempt to preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the brass reference machine fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now keep many query heads but share one key head and one value head across them. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Multi-Query Attention**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## Why Cache Separate Copies for Every Head

Eight query experts ask eight different questions of the same cached catalog. Cache entries fall from eight key-value pairs per token to one pair per token.

## The calculation hidden inside multi-query attention

The enginewright carries the multi-query attention scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Take one layer with 100 remembered tokens. If each KV head stores 64 coordinates, one head needs 100×64 coordinate slots for keys and the same again for values. Eight heads need eight copies of those slots. The three counts—tokens L, KV heads H_KV, and width d_h—multiply because every choice from one count is paired with every choice from the others.

L is cached sequence length, H_KV is the number of key-value heads, and d_h is the width stored per head.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) appears because every token stores every KV head's coordinates: doubling any factor doubles memory. [Proportionality](../../MATHEMATICAL_MOVES.md#proportionality) omits fixed factors such as both K and V, bytes per number, layers, and batch size while preserving the scaling argument.

The mandala has curved back upon itself. In this chamber we meet **the lock and key**—one influence matters through another, and either missing factor can close the path. What seemed like a new formula is older mathematical instinct arranged around a new need.

Nothing remains unnamed in the multi-query attention case on the brass reference machine. We can finally trade the long route for its compact map:

$$
M_{\text{KV}}\propto L H_{\text{KV}} d_h
$$

## Where multi-query attention runs out

A single shared catalog can remove distinctions that genuinely need different key-value spaces.

A final test reaches beyond the new instrument. It does not refute Multi-Query Attention; it reveals the edge of what was constructed. The enginewright carries that edge into the following room.

## Return to the brass reference machine

Rebuild the multi-query attention scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Grouped-Query Attention — Recover Some Specialist Memory](../159-grouped-query-attention/README.md)
