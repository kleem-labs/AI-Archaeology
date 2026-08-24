# Excavation 078 — Pooling — Keeping Evidence While Shrinking the Map

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Vision and generative models

Convolution slides one local detector across the whole image. The resulting activation maps preserve every detected location and quickly become too large for deeper processing.

The doors of the Glass Menagerie close against the wind. On the wall of illuminated tiles, the maker of seeing-machines writes the cheapest rule that might still be true: keep every activation at full resolution through every layer.

For a moment the mark looks complete. Then the evidence refuses to fit: memory explodes and tiny shifts move evidence to neighboring cells. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The maker of seeing-machines sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   keep every activation at full… memory explodes and tiny shifts move…
            \        /
             \      /
              summarize small neighborhoods while…
```

The maker of seeing-machines lays two translucent sheets over the wall of illuminated tiles. The first is inscribed, “keep every activation at full resolution through every layer.” Its path ends where memory explodes and tiny shifts move evidence to neighboring cells. The second receives the same evidence but is allowed to summarize small neighborhoods while retaining the strongest or average evidence. Held to the light, the sheets separate at exactly one decision.

No one reaches for a pooling formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The maker of seeing-machines changes only that one responsibility: summarize small neighborhoods while retaining the strongest or average evidence. When the ink dries, the name **Pooling** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because memory explodes and tiny shifts move evidence to neighboring cells, while the other can summarize small neighborhoods while retaining the strongest or average evidence. That fork—not the vocabulary—is where pooling lives.

<!-- memory-film-v1:start -->
> **Memory realm 8 of 18 — [Glass Menagerie](../../MEMORY_PALACE.md#realm-8)**
>
> **The question carried into this chamber:** What fails if we keep every activation at full resolution through every layer?

## When the chamber changes

Before leaving Pooling, replay the discovery as motion rather than as a definition.

First hold the failed picture still: The gear follows the tempting path—keep every activation at full resolution through every layer. Then the evidence answers: memory explodes and tiny shifts move evidence to neighboring cells.

Now let the chamber move: The maker of seeing-machines changes one moving part. The gear can now summarize small neighborhoods while retaining the strongest or average evidence.

The object that should remain after the terminology disappears is **the pooling gear mounted on the wall of illuminated tiles**.

> **Memory seal — Pooling**
>
> Pooling keeps the missing power: summarize small neighborhoods while retaining the strongest or average evidence.

Give the idea a bodily path: Touch the pooling gear in imagination: make a narrow gate with both hands, block the old path, then open only the route the evidence permits.
<!-- memory-film-v1:end -->

## Keeping Evidence While Shrinking the Map

Max pooling [1,7,2,3] keeps 7: an edge existed somewhere in that patch.

## Where pooling runs out

Pooling discards exact location and can erase subtle patterns.

At the Glass Menagerie, the maker of seeing-machines leaves a blank beneath the new mark. Pooling has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the wall of illuminated tiles

Rebuild the pooling scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 079](../079-cnn-hierarchy/README.md)
