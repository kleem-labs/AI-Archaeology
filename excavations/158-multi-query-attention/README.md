# Excavation 158 — Multi-Query Attention — Why Cache Separate Copies for Every Head?

Caching turns repeated arithmetic into memory reads. Profiling now shows decoding limited by loading separate key and value histories for every attention head.

Perhaps we preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections.

It survives until the measured run answers back. The caches grow with both sequence length and head count, and loading them dominates the arithmetic for one new token.

Now the missing requirement is concrete. Keep many query heads but share one key head and one value head across them.

## Let one run decide

Eight query experts ask eight different questions of the same cached catalog. Cache entries fall from eight key-value pairs per token to one pair per token.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

Take one layer with 100 remembered tokens. If each KV head stores 64 coordinates, one head needs 100×64 coordinate slots for keys and the same again for values. Eight heads need eight copies of those slots. The three counts—tokens L, KV heads H_KV, and width d_h—multiply because every choice from one count is paired with every choice from the others.

L is cached sequence length, H_KV is the number of key-value heads, and d_h is the width stored per head.

### Why these operations are forced

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) appears because every token stores every KV head's coordinates: doubling any factor doubles memory. [Proportionality](../../MATHEMATICAL_MOVES.md#proportionality) omits fixed factors such as both K and V, bytes per number, layers, and batch size while preserving the scaling argument.

Only now can we compress the procedure:

$$
M_{\text{KV}}\propto L H_{\text{KV}} d_h
$$

## What this repair cannot do

A single shared catalog can remove distinctions that genuinely need different key-value spaces.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Grouped-Query Attention — Recover Some Specialist Memory](../159-grouped-query-attention/README.md)
