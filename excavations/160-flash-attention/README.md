# Excavation 160 — FlashAttention — The Arithmetic Was Not the Bottleneck

Grouped-query attention makes generation economical, yet training long packed sequences still materializes a large attention-score matrix in slow device memory.

Perhaps we reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost.

It survives until the measured run answers back. Approximation changes the model, while profiling shows much of the time is spent writing and rereading exact intermediate scores rather than multiplying them.

Now the missing requirement is concrete. Tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once.

## Let one run decide

Process two score tiles. Carry only the running maximum, normalized denominator, and weighted value total into the next tile; the final answer matches ordinary softmax attention.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

The model's first attention tile contains scores 1 and 4, so 4 becomes the remembered safety ceiling. The next tile contains 3 and 2; neither exceeds 4, so the ceiling remains 4. If a later tile contained 7, the ceiling would become 7 and the earlier exponential totals would be rescaled. Thus m is the largest score already processed, the s_j values are the arriving tile, and m-prime is the one maximum covering both histories.

m is the largest score already seen, s_j are scores in the new tile, and m-prime is the safe maximum for the combined tiles.

### Why these operations are forced

[Maximum](../../MATHEMATICAL_MOVES.md#maximum) preserves the one value needed to stabilize exponentials across both old and new tiles. Addition would invent a score that never occurred; averaging could be lower than the true maximum and allow overflow. The prime marks the updated running version; see [symbol decorations](../../MATHEMATICAL_MOVES.md#symbol-decorations).

Only now can we compress the procedure:

$$
m^{\prime}=\max(m,\max_j s_j)
$$

## What this repair cannot do

FlashAttention removes avoidable memory traffic, not quadratic pairwise arithmetic itself.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: RMSNorm — Do We Need to Subtract the Centre?](../161-rmsnorm/README.md)
