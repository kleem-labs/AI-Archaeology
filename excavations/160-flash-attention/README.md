# Excavation 160 — FlashAttention — The Arithmetic Was Not the Bottleneck

<!-- book-prose-v2 -->

Grouped-query attention makes generation economical, yet training long packed sequences still materializes a large attention-score matrix in slow device memory.

If the old idea can be stretched one step farther, we should reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost.

If the proposal works on every relevant case, flashattention is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

Now keep that rule fixed and let the difficult case enter: approximation changes the model, while profiling shows much of the time is spent writing and rereading exact intermediate scores rather than multiplying them.

Nothing magical creates flashattention. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once.

This boundary between the failed rule and its repair is the subject later work calls **FlashAttention**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize flashattention; try to break it by subtraction. Remove the part that knows how to tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once, leaving only the attempt to reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost. What returns is not a vague weakness but the original contradiction: approximation changes the model, while profiling shows much of the time is spent writing and rereading exact intermediate scores rather than multiplying them. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost receives the same test as the rule to tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once. Their different outcomes reveal what flashattention contributes without asking the reader to trust historical convention.

## The Arithmetic Was Not the Bottleneck

Process two score tiles. Carry only the running maximum, normalized denominator, and weighted value total into the next tile; the final answer matches ordinary softmax attention.

Hold the setting, evidence, and desired outcome fixed while testing flashattention. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

## The calculation hidden inside flashattention

Do not read the coming FlashAttention line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

The model's first attention tile contains scores 1 and 4, so 4 becomes the remembered safety ceiling. The next tile contains 3 and 2; neither exceeds 4, so the ceiling remains 4. If a later tile contained 7, the ceiling would become 7 and the earlier exponential totals would be rescaled. Thus m is the largest score already processed, the s_j values are the arriving tile, and m-prime is the one maximum covering both histories.

m is the largest score already seen, s_j are scores in the new tile, and m-prime is the safe maximum for the combined tiles.

### Why no cheaper operation does the same job

[Maximum](../../MATHEMATICAL_MOVES.md#maximum) preserves the one value needed to stabilize exponentials across both old and new tiles. Addition would invent a score that never occurred; averaging could be lower than the true maximum and allow overflow. The prime marks the updated running version; see [symbol decorations](../../MATHEMATICAL_MOVES.md#symbol-decorations).

Every symbol in FlashAttention can now be read back into an action already performed. The whole procedure fits in one line:

$$
m^{\prime}=\max(m,\max_j s_j)
$$

## Where flashattention runs out

FlashAttention removes avoidable memory traffic, not quadratic pairwise arithmetic itself.

This is where flashattention runs out for a causal reason. We gave it enough structure to tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

## Take flashattention to the workbench

A mathematical story about flashattention earns trust only when the failed and repaired paths can both be reproduced. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running flashattention, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the flashattention result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: RMSNorm — Do We Need to Subtract the Centre?](../161-rmsnorm/README.md)
