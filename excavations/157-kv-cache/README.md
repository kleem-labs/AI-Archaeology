# Excavation 157 — The KV Cache — Stop Re-reading the Entire Past

<!-- book-prose-v2 -->

Relative position now behaves predictably, but autoregressive generation still reruns the Transformer over the full prefix after appending each token.

For a moment, remain loyal to the simplest proposal: at step t, recompute keys and values for positions 1 through t because the prefix is presented again.

Its appeal is not ignorance but economy. The KV Cache should not be added until an observation exposes the exact thing the older procedure cannot preserve.

Reality now asks a question the retained information cannot answer: past token representations are unchanged in causal decoding, so the same projections are calculated repeatedly while one new token is added.

Notice what the counterexample has accomplished for the kv cache. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: store each layer's past keys and values once, append only the new pair, and let the new query attend to the cache.

Humanity eventually gathered this problem and its repairs under the name **The KV Cache**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace the kv cache with the old instruction to at step t, recompute keys and values for positions 1 through t because the prefix is presented again. The result is again that past token representations are unchanged in causal decoding, so the same projections are calculated repeatedly while one new token is added. Put back only the requirement to store each layer's past keys and values once, append only the new pair, and let the new query attend to the cache. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when the kv cache is introduced. The same evidence that defeated the attempt to at step t, recompute keys and values for positions 1 through t because the prefix is presented again is presented again. Only the ability to store each layer's past keys and values once, append only the new pair, and let the new query attend to the cache changes, so the repaired conclusion cannot be credited to a conveniently different example.

## Stop Re-reading the Entire Past

Generating token 101 computes one new key and value, then reads the 100 cached pairs. It does not rebuild pairs 1 through 100.

Run the the kv cache scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

## The calculation hidden inside the kv cache

Before The KV Cache receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

At token 101, write the hundred old keys on cards and compute one new card. Nothing on the old cards has changed, so combining must mean placing card 101 after cards 1 through 100—not adding their numbers together. K_1:t−1 names the ordered stack already present, k_t the one new card, and K_1:t the longer stack after appending.

K_1:t−1 is the unchanged past cache, k_t is the newly computed key, and K_1:t is the cache available to the current query.

### Why no cheaper operation does the same job

[Function application](../../MATHEMATICAL_MOVES.md#function-application) names one append operation. Appending preserves order and old values; [addition](../../MATHEMATICAL_MOVES.md#addition) would numerically blend keys and destroy which token produced each one. The indices show that only position t is new.

Every symbol in The KV Cache can now be read back into an action already performed. The whole procedure fits in one line:

$$
K_{1:t}=\mathrm{append}(K_{1:t-1},k_t)
$$

## Where the kv cache runs out

Because every past key and value must remain available, saved computation becomes growing memory and memory-bandwidth cost, especially for long contexts and many users.

Why does that boundary remain? The KV Cache was built for one responsibility: store each layer's past keys and values once, append only the new pair, and let the new query attend to the cache. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take the kv cache to the workbench

The argument for the kv cache is still provisional until a runnable case can make it fail. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running the kv cache, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the the kv cache result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Multi-Query Attention — Why Cache Separate Copies for Every Head?](../158-multi-query-attention/README.md)
