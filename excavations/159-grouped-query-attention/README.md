# Excavation 159 — Grouped-Query Attention — Recover Some Specialist Memory

<!-- book-prose-v2 -->

One shared KV head makes decoding light enough for the station, but evaluation finds a quality loss on relationships that benefited from distinct catalogs.

The machinery already in our hands suggests that we return immediately to one KV head per query head.

This is how grouped-query attention ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

One counterexample is enough to expose the missing job: quality recovers, but so does the full cache and bandwidth cost that forced sharing.

The wrong answer makes the need for grouped-query attention inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: partition query heads into groups; queries remain distinct while each group shares one key-value head.

The usual name, **Grouped-Query Attention**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to return immediately to one KV head per query head produces the observed failure: quality recovers, but so does the full cache and bandwidth cost that forced sharing. Starting with the repaired demand to partition query heads into groups; queries remain distinct while each group shares one key-value head preserves the information the shortcut lost. The subject of grouped-query attention lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to partition query heads into groups; queries remain distinct while each group shares one key-value head instead of merely trying to return immediately to one KV head per query head. That controlled contrast is what turns a plausible explanation of grouped-query attention into an understandable derivation.

## Recover Some Specialist Memory

Eight query heads arranged into two KV groups preserve two catalogs. The cache is twice MQA's size but one quarter of ordinary eight-head KV storage.

There are now two histories of this grouped-query attention case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

## The calculation hidden inside grouped-query attention

Before Grouped-Query Attention receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Line up the model's eight query heads and two KV catalogs. Four consecutive query heads must point to catalog 0 and the next four to catalog 1. Scaling head number h from the eight-head range into the two-catalog range gives h×2/8; rounding down turns positions 0 through 3 into address 0 and positions 4 through 7 into address 1. The name g(h) records that address-making rule.

h is a query-head index, H_Q counts query heads, H_KV counts shared KV groups, and g(h) selects the group serving head h.

### Why no cheaper operation does the same job

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) spreads the KV group range across query-head indices; [division](../../MATHEMATICAL_MOVES.md#division) converts one query index into its proportional group location. The floor deliberately [rounds](../../MATHEMATICAL_MOVES.md#rounding) down so every head receives one valid discrete group rather than a fractional address.

Every symbol in Grouped-Query Attention can now be read back into an action already performed. The whole procedure fits in one line:

$$
g(h)=\left\lfloor\frac{hH_{\text{KV}}}{H_Q}\right\rfloor
$$

## Where grouped-query attention runs out

Because sharing deliberately removes independent KV views, the number and assignment of groups remain empirical design choices whose quality must be measured.

Look back at what grouped-query attention actually preserves: it can partition query heads into groups; queries remain distinct while each group shares one key-value head. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

## Take grouped-query attention to the workbench

The reader has reconstructed grouped-query attention in words; the workbench tests whether those words specify a real procedure. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running grouped-query attention, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the grouped-query attention result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: FlashAttention — The Arithmetic Was Not the Bottleneck](../160-flash-attention/README.md)
