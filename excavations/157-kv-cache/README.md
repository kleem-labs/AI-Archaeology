# Excavation 157 — The KV Cache — Stop Re-reading the Entire Past

Relative position now behaves predictably, but autoregressive generation still reruns the Transformer over the full prefix after appending each token.

Perhaps we at step t, recompute keys and values for positions 1 through t because the prefix is presented again.

It survives until the measured run answers back. Past token representations are unchanged in causal decoding, so the same projections are calculated repeatedly while one new token is added.

Now the missing requirement is concrete. Store each layer's past keys and values once, append only the new pair, and let the new query attend to the cache.

## Let one run decide

Generating token 101 computes one new key and value, then reads the 100 cached pairs. It does not rebuild pairs 1 through 100.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

At token 101, write the hundred old keys on cards and compute one new card. Nothing on the old cards has changed, so combining must mean placing card 101 after cards 1 through 100—not adding their numbers together. K_1:t−1 names the ordered stack already present, k_t the one new card, and K_1:t the longer stack after appending.

K_1:t−1 is the unchanged past cache, k_t is the newly computed key, and K_1:t is the cache available to the current query.

### Why these operations are forced

[Function application](../../MATHEMATICAL_MOVES.md#function-application) names one append operation. Appending preserves order and old values; [addition](../../MATHEMATICAL_MOVES.md#addition) would numerically blend keys and destroy which token produced each one. The indices show that only position t is new.

Only now can we compress the procedure:

$$
K_{1:t}=\mathrm{append}(K_{1:t-1},k_t)
$$

## What this repair cannot do

Because every past key and value must remain available, saved computation becomes growing memory and memory-bandwidth cost, especially for long contexts and many users.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Multi-Query Attention — Why Cache Separate Copies for Every Head?](../158-multi-query-attention/README.md)
