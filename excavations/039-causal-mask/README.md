# Excavation 039 — Causal Masking — Preventing the Future from Leaking Backward

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Position marks make order visible. During next-token training, however, the correct answer is sitting to the right inside the same sentence, where an unrestricted attention mechanism can simply look at it.

Nothing in the Clockwork Scriptorium yet bears today's mathematical name. There is only the mechanist, the sentence-wheel, and one plausible action: train each prefix in a separate forward pass.

Then the quiet test arrives: it prevents cheating but repeats nearly identical work. What looked like simplicity is revealed as a missing distinction.

*The mechanist sketches the break before changing it:*

```text
observation
    │
    ▼
[train each prefix in a separate…]
    │
    ╳  it prevents cheating but repeats…
    │
    ▼
[we need to process all positions…]
```

The mechanist turns the sentence-wheel toward the light. Through the old engraving, train each prefix in a separate forward pass, the evidence ends in the same contradiction: it prevents cheating but repeats nearly identical work. A second engraving adds only the power to process all positions together while blocking attention from position i to every later position j. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The mechanist circles the place where the two causal masking cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: we need to process all positions together while blocking attention from position i to every later position j. The mechanist writes **Causal Masking** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The mechanist places a finger over the new distinction. At once the two cases collapse and it prevents cheating but repeats nearly identical work. Lifting the finger restores only this capacity: process all positions together while blocking attention from position i to every later position j. That tiny reversible motion is the chapter's proof of necessity.

## The calculation hidden inside causal masking

The mechanist carries the causal masking scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A mask prevents direct attention leakage; shifted targets and data pipelines must also align correctly.

While learning from “the tiger sleeps,” the model sees the complete training sentence. At the position after *the*, the correct next token *tiger* is already sitting to the right. Place an impassable barrier on every connection pointing into the future. In score language, those forbidden paths receive a value whose exponential contribution becomes zero, while present and earlier words remain available.

### Naming what is already on the table

**i** is the receiving position and **j** a possible source position.
When j≤i, the source is present or past, so adding zero leaves its attention score unchanged.
When j>i, the source is future; adding −∞ makes its later softmax weight zero.
**M_ij** stores that allowed-or-forbidden correction for every pair.

### Why the melody needs these exact notes

[Cases](../../MATHEMATICAL_MOVES.md#cases) are forced because visible and forbidden positions obey genuinely different rules.
[j ≤ i and j > i](../../MATHEMATICAL_MOVES.md#inequalities) divide earlier-or-current keys from future keys for query position i.
Zero leaves an allowed attention score unchanged. [Negative infinity](../../MATHEMATICAL_MOVES.md#negative-sign) makes a forbidden score's exponential weight zero after softmax; a large positive value would do the opposite.

Before the line is compressed, notice its recurring motions: **the turning wind**—an uphill quantity is made to point downhill, or surprise is made to count as cost. They are the handholds by which the reader can later climb back from notation to meaning.

The story of causal masking has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
M_{ij}=\begin{cases}0&j\le i\\-\infty&j>i\end{cases}
$$

The equation arrives after every operation has a job.

## Causal Masking beyond this one case

An exam sheet can contain later questions, but an opaque cover hides everything beyond the current line.

## Return to the sentence-wheel

Rebuild the causal masking scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 040](../040-next-token-examples/README.md)
