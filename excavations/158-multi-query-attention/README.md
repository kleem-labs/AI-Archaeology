# Excavation 158 — Multi-Query Attention — Why Cache Separate Copies for Every Head?

<!-- book-prose-v2 -->

Caching turns repeated arithmetic into memory reads. Profiling now shows decoding limited by loading separate key and value histories for every attention head.

Nothing yet appears to demand a new invention. We can preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections.

There is a real principle behind this restraint: the complexity of multi-query attention must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The decisive test is this: the caches grow with both sequence length and head count, and loading them dominates the arithmetic for one new token.

That distinction is the hinge on which multi-query attention turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: keep many query heads but share one key head and one value head across them.

We have earned the chapter's shorter name: **Multi-Query Attention**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that multi-query attention is necessary rather than decorative. Delete its new responsibility and use the earlier plan to preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections. Immediately, the caches grow with both sequence length and head count, and loading them dominates the arithmetic for one new token. Reintroduce the single job to keep many query heads but share one key head and one value head across them. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can keep many query heads but share one key head and one value head across them. Because the old plan to preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections is the only displaced piece, the reader can locate exactly where multi-query attention changes the outcome.

## Why Cache Separate Copies for Every Head

Eight query experts ask eight different questions of the same cached catalog. Cache entries fall from eight key-value pairs per token to one pair per token.

The name multi-query attention is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

## The calculation hidden inside multi-query attention

Do not read the coming Multi-Query Attention line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Take one layer with 100 remembered tokens. If each KV head stores 64 coordinates, one head needs 100×64 coordinate slots for keys and the same again for values. Eight heads need eight copies of those slots. The three counts—tokens L, KV heads H_KV, and width d_h—multiply because every choice from one count is paired with every choice from the others.

L is cached sequence length, H_KV is the number of key-value heads, and d_h is the width stored per head.

### Why no cheaper operation does the same job

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) appears because every token stores every KV head's coordinates: doubling any factor doubles memory. [Proportionality](../../MATHEMATICAL_MOVES.md#proportionality) omits fixed factors such as both K and V, bytes per number, layers, and batch size while preserving the scaling argument.

Every symbol in Multi-Query Attention can now be read back into an action already performed. The whole procedure fits in one line:

$$
M_{\text{KV}}\propto L H_{\text{KV}} d_h
$$

## Where multi-query attention runs out

A single shared catalog can remove distinctions that genuinely need different key-value spaces.

The weakness is not an accidental footnote. Every operation in multi-query attention serves the narrower purpose to keep many query heads but share one key head and one value head across them; none was designed to answer the new question. We have reached the honest edge of the invention.

## Take multi-query attention to the workbench

Understanding multi-query attention now means predicting its intermediate results before asking software for an answer. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running multi-query attention, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the multi-query attention result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Grouped-Query Attention — Recover Some Specialist Memory](../159-grouped-query-attention/README.md)
