# Excavation 159 — Grouped-Query Attention — Recover Some Specialist Memory

One shared KV head makes decoding light enough for the station, but evaluation finds a quality loss on relationships that benefited from distinct catalogs.

Perhaps we return immediately to one KV head per query head.

It survives until the measured run answers back. Quality recovers, but so does the full cache and bandwidth cost that forced sharing.

Now the missing requirement is concrete. Partition query heads into groups; queries remain distinct while each group shares one key-value head.

## Let one run decide

Eight query heads arranged into two KV groups preserve two catalogs. The cache is twice MQA's size but one quarter of ordinary eight-head KV storage.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

Line up the model's eight query heads and two KV catalogs. Four consecutive query heads must point to catalog 0 and the next four to catalog 1. Scaling head number h from the eight-head range into the two-catalog range gives h×2/8; rounding down turns positions 0 through 3 into address 0 and positions 4 through 7 into address 1. The name g(h) records that address-making rule.

h is a query-head index, H_Q counts query heads, H_KV counts shared KV groups, and g(h) selects the group serving head h.

### Why these operations are forced

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) spreads the KV group range across query-head indices; [division](../../MATHEMATICAL_MOVES.md#division) converts one query index into its proportional group location. The floor deliberately [rounds](../../MATHEMATICAL_MOVES.md#rounding) down so every head receives one valid discrete group rather than a fractional address.

Only now can we compress the procedure:

$$
g(h)=\left\lfloor\frac{hH_{\text{KV}}}{H_Q}\right\rfloor
$$

## What this repair cannot do

Because sharing deliberately removes independent KV views, the number and assignment of groups remain empirical design choices whose quality must be measured.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: FlashAttention — The Arithmetic Was Not the Bottleneck](../160-flash-attention/README.md)
