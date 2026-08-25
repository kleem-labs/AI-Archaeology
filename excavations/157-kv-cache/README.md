# Excavation 157 — The KV Cache — Stop Re-reading the Entire Past

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Model systems and engine optimization

Relative position now behaves predictably, but autoregressive generation still reruns the Transformer over the full prefix after appending each token.

The previous discovery reaches the Engine Cavern carrying one unfinished problem. Beside the brass reference machine, the enginewright first tries to at step t, recompute keys and values for positions 1 through t because the prefix is presented again.

There is good reason to begin this way. If we at step t, recompute keys and values for positions 1 through t because the prefix is presented again, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: past token representations are unchanged in causal decoding, so the same projections are calculated repeatedly while one new token is added.

This failure cannot be repaired by performing the instruction to at step t, recompute keys and values for positions 1 through t because the prefix is presented again more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the brass reference machine; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to store each layer's past keys and values once, append only the new pair, and let the new query attend to the cache. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **The KV Cache**. The name is simply a handle for the distinction already reconstructed.

## Stop Re-reading the Entire Past

Generating token 101 computes one new key and value, then reads the 100 cached pairs. It does not rebuild pairs 1 through 100.

## The calculation hidden inside the kv cache

The enginewright carries the kv cache scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

At token 101, write the hundred old keys on cards and compute one new card. Nothing on the old cards has changed, so combining must mean placing card 101 after cards 1 through 100—not adding their numbers together. K_1:t−1 names the ordered stack already present, k_t the one new card, and K_1:t the longer stack after appending.

K_1:t−1 is the unchanged past cache, k_t is the newly computed key, and K_1:t is the cache available to the current query.

### Why the melody needs these exact notes

[Function application](../../MATHEMATICAL_MOVES.md#function-application) names one append operation. Appending preserves order and old values; [addition](../../MATHEMATICAL_MOVES.md#addition) would numerically blend keys and destroy which token produced each one. The indices show that only position t is new.

Trace each operation by touch rather than by name: **the joining river**—separate contributions meet without losing where they came from. Together they form the smallest mechanism that survives the counterexample.

The enginewright reads the journey of kv cache once more across the brass reference machine, then lets the words contract without losing their order:

$$
K_{1:t}=\mathrm{append}(K_{1:t-1},k_t)
$$

## Where the kv cache runs out

Because every past key and value must remain available, saved computation becomes growing memory and memory-bandwidth cost, especially for long contexts and many users.

The brass reference machine answers today's question and falls silent at the next. That silence is precise: KV Cache was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the brass reference machine

Rebuild the kv cache scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Multi-Query Attention — Why Cache Separate Copies for Every Head?](../158-multi-query-attention/README.md)
