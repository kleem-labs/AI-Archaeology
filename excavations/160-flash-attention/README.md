# Excavation 160 — FlashAttention — The Arithmetic Was Not the Bottleneck

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Model systems and engine optimization

Grouped-query attention makes generation economical, yet training long packed sequences still materializes a large attention-score matrix in slow device memory.

At the Engine Cavern, the enginewright meets the next case beside the brass reference machine. The nearest idea is also the most reasonable one: reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost.

The attraction of this attempt is easy to see. To reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: approximation changes the model, while profiling shows much of the time is spent writing and rereading exact intermediate scores rather than multiplying them.

The contradiction matters because it identifies a structural loss in the instruction to reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The brass reference machine will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **FlashAttention**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

## The Arithmetic Was Not the Bottleneck

Process two score tiles. Carry only the running maximum, normalized denominator, and weighted value total into the next tile; the final answer matches ordinary softmax attention.

## The calculation hidden inside flashattention

The enginewright carries the flashattention scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The model's first attention tile contains scores 1 and 4, so 4 becomes the remembered safety ceiling. The next tile contains 3 and 2; neither exceeds 4, so the ceiling remains 4. If a later tile contained 7, the ceiling would become 7 and the earlier exponential totals would be rescaled. Thus m is the largest score already processed, the s_j values are the arriving tile, and m-prime is the one maximum covering both histories.

m is the largest score already seen, s_j are scores in the new tile, and m-prime is the safe maximum for the combined tiles.

### Why the melody needs these exact notes

[Maximum](../../MATHEMATICAL_MOVES.md#maximum) preserves the one value needed to stabilize exponentials across both old and new tiles. Addition would invent a score that never occurred; averaging could be lower than the true maximum and allow overflow. The prime marks the updated running version; see [symbol decorations](../../MATHEMATICAL_MOVES.md#symbol-decorations).

Listen beneath flashattention: **the highest lantern**—the strongest surviving possibility sets the visible ceiling. These are not ornamental comparisons. Each image keeps the exact job of an operation visible while its symbols change.

Every mark in the coming flashattention equation now belongs to a visible part of the case. The compressed form is:

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
