# Excavation 159 — Grouped-Query Attention — Recover Some Specialist Memory

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Model systems and engine optimization

One shared KV head makes decoding light enough for the station, but evaluation finds a quality loss on relationships that benefited from distinct catalogs.

Inside the Engine Cavern, the old method is given an honest chance. The enginewright places the evidence on the brass reference machine and tries to return immediately to one KV head per query head.

Nothing about this first move is careless. To return immediately to one KV head per query head is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: quality recovers, but so does the full cache and bandwidth cost that forced sharing.

The important discovery is not merely that trying to return immediately to one KV head per query head failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the brass reference machine, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to partition query heads into groups; queries remain distinct while each group shares one key-value head. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Grouped-Query Attention**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## Recover Some Specialist Memory

Eight query heads arranged into two KV groups preserve two catalogs. The cache is twice MQA's size but one quarter of ordinary eight-head KV storage.

## The calculation hidden inside grouped-query attention

The enginewright carries the grouped-query attention scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Line up the model's eight query heads and two KV catalogs. Four consecutive query heads must point to catalog 0 and the next four to catalog 1. Scaling head number h from the eight-head range into the two-catalog range gives h×2/8; rounding down turns positions 0 through 3 into address 0 and positions 4 through 7 into address 1. The name g(h) records that address-making rule.

h is a query-head index, H_Q counts query heads, H_KV counts shared KV groups, and g(h) selects the group serving head h.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) spreads the KV group range across query-head indices; [division](../../MATHEMATICAL_MOVES.md#division) converts one query index into its proportional group location. The floor deliberately [rounds](../../MATHEMATICAL_MOVES.md#rounding) down so every head receives one valid discrete group rather than a fractional address.

The calculation reuses familiar motions: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. Together they keep the path from the concrete case to notation intact.

The story of grouped-query attention has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
g(h)=\left\lfloor\frac{hH_{\text{KV}}}{H_Q}\right\rfloor
$$

## Where grouped-query attention runs out

Because sharing deliberately removes independent KV views, the number and assignment of groups remain empirical design choices whose quality must be measured.

One unsolved mark remains on the brass reference machine. None of the responsibilities inside Grouped-Query Attention can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the brass reference machine

Rebuild the grouped-query attention scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: FlashAttention — The Arithmetic Was Not the Bottleneck](../160-flash-attention/README.md)
