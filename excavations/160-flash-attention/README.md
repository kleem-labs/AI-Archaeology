# Excavation 160 — FlashAttention — The Arithmetic Was Not the Bottleneck

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Grouped-query attention makes generation economical, yet training long packed sequences still materializes a large attention-score matrix in slow device memory.

At the Engine Cavern, the enginewright returns to the brass reference machine. Yesterday's instrument still lies open, so the first move asks for no new magic: reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost.

The enginewright repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: approximation changes the model, while profiling shows much of the time is spent writing and rereading exact intermediate scores rather than multiplying them. The failure is stable enough to become evidence.

*The enginewright sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ reduce arithmetic by approximating… ──▶ blurred: approximation changes the model,…
      │
      └── new lens ──▶ tile queries, keys, and values into… ──▶ distinction survives
```

Across the brass reference machine, the old path and the repaired path run side by side. One carries “reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost”; the other knows how to tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once. When the failure—approximation changes the model, while profiling shows much of the time is spent writing and rereading exact intermediate scores rather than multiplying them—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to flashattention. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once. This problem and its repair will travel under the name **FlashAttention**, but the name carries no knowledge the scene has not earned.

What changed on the brass reference machine can be said without symbols. Before, the method could only reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost; now it can also tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it.

## The Arithmetic Was Not the Bottleneck

Process two score tiles. Carry only the running maximum, normalized denominator, and weighted value total into the next tile; the final answer matches ordinary softmax attention.

## The calculation hidden inside flashattention

The enginewright carries the flashattention scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The model's first attention tile contains scores 1 and 4, so 4 becomes the remembered safety ceiling. The next tile contains 3 and 2; neither exceeds 4, so the ceiling remains 4. If a later tile contained 7, the ceiling would become 7 and the earlier exponential totals would be rescaled. Thus m is the largest score already processed, the s_j values are the arriving tile, and m-prime is the one maximum covering both histories.

m is the largest score already seen, s_j are scores in the new tile, and m-prime is the safe maximum for the combined tiles.

### Why the melody needs these exact notes

[Maximum](../../MATHEMATICAL_MOVES.md#maximum) preserves the one value needed to stabilize exponentials across both old and new tiles. Addition would invent a score that never occurred; averaging could be lower than the true maximum and allow overflow. The prime marks the updated running version; see [symbol decorations](../../MATHEMATICAL_MOVES.md#symbol-decorations).

Listen beneath flashattention: **the highest lantern**—the strongest surviving possibility sets the visible ceiling. These are not ornamental comparisons. Each image keeps the exact job of an operation visible while its symbols change.

Cover the prose about flashattention and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
m^{\prime}=\max(m,\max_j s_j)
$$

## Where flashattention runs out

FlashAttention removes avoidable memory traffic, not quadratic pairwise arithmetic itself.

The flashattention repair holds, but the world asks for something it was never given. At the Engine Cavern, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the brass reference machine

Rebuild the flashattention scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: RMSNorm — Do We Need to Subtract the Centre?](../161-rmsnorm/README.md)
