# Excavation 159 — Grouped-Query Attention — Recover Some Specialist Memory

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Model systems and engine optimization

One shared KV head makes decoding light enough for the station, but evaluation finds a quality loss on relationships that benefited from distinct catalogs.

Nothing in the Engine Cavern yet bears today's mathematical name. There is only the enginewright, the brass reference machine, and one plausible action: return immediately to one KV head per query head.

Then the quiet test arrives: quality recovers, but so does the full cache and bandwidth cost that forced sharing. What looked like simplicity is revealed as a missing distinction.

*The enginewright sketches the break before changing it:*

```text
OLD PATH:  request ──▶ return immediately to one KV head per… ──▶ quality recovers, but so does the…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ partition query heads into groups;… ──▶ accountable result
```

The enginewright turns the brass reference machine toward the light. Through the old engraving, return immediately to one KV head per query head, the evidence ends in the same contradiction: quality recovers, but so does the full cache and bandwidth cost that forced sharing. A second engraving adds only the power to partition query heads into groups; queries remain distinct while each group shares one key-value head. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The enginewright circles the place where the two grouped-query attention cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: partition query heads into groups; queries remain distinct while each group shares one key-value head. The enginewright writes **Grouped-Query Attention** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The enginewright places a finger over the new distinction. At once the two cases collapse and quality recovers, but so does the full cache and bandwidth cost that forced sharing. Lifting the finger restores only this capacity: partition query heads into groups; queries remain distinct while each group shares one key-value head. That tiny reversible motion is the chapter's proof of necessity.

<!-- memory-film-v1:start -->
> **Memory realm 12 of 18 — [Engine Cavern](../../MEMORY_PALACE.md#realm-12)**
>
> **The question carried into this chamber:** What fails if we return immediately to one KV head per query head?

## When the chamber changes

The mathematical name Grouped-Query Attention can now rest. What matters is whether its transformation remains visible.

First hold the failed picture still: The prism follows the tempting path—return immediately to one KV head per query head. Then the evidence answers: quality recovers, but so does the full cache and bandwidth cost that forced sharing.

Now let the chamber move: The enginewright changes one moving part. The prism can now partition query heads into groups; queries remain distinct while each group shares one key-value head.

The object that should remain after the terminology disappears is **the grouped-query attention prism mounted on the brass reference machine**.

> **Memory seal — Grouped-Query Attention**
>
> Grouped-Query Attention keeps the missing power: partition query heads into groups; queries remain distinct while each group shares one key-value head.

Give the idea a bodily path: Touch the grouped-query attention prism in imagination: tap five fingertips in order—question, object, failure, transformation, seal—without saying the formal name.
<!-- memory-film-v1:end -->

## Recover Some Specialist Memory

Eight query heads arranged into two KV groups preserve two catalogs. The cache is twice MQA's size but one quarter of ordinary eight-head KV storage.

## The calculation hidden inside grouped-query attention

The enginewright carries the grouped-query attention scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Line up the model's eight query heads and two KV catalogs. Four consecutive query heads must point to catalog 0 and the next four to catalog 1. Scaling head number h from the eight-head range into the two-catalog range gives h×2/8; rounding down turns positions 0 through 3 into address 0 and positions 4 through 7 into address 1. The name g(h) records that address-making rule.

h is a query-head index, H_Q counts query heads, H_KV counts shared KV groups, and g(h) selects the group serving head h.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) spreads the KV group range across query-head indices; [division](../../MATHEMATICAL_MOVES.md#division) converts one query index into its proportional group location. The floor deliberately [rounds](../../MATHEMATICAL_MOVES.md#rounding) down so every head receives one valid discrete group rather than a fractional address.

Before the line is compressed, notice its recurring motions: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. They are the handholds by which the reader can later climb back from notation to meaning.

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
