# Excavation 154 — Sequence Packing — Stop Training on Empty Space

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

The input pipeline now keeps the device busy. Inspection shows that many of the tokens occupying each fixed rectangle are padding rather than language.

The brass reference machine at the Engine Cavern still carries the marks of the previous discovery. The enginewright follows them as far as they seem willing to go: pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste.

The enginewright repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: the loss ignores padding, but attention and matrix multiplication still spend time and memory carrying those empty positions. The failure is stable enough to become evidence.

*The enginewright sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ pad every sentence to the longest… ──▶ blurred: the loss ignores padding, but…
      │
      └── new lens ──▶ pack several short examples into each… ──▶ distinction survives
```

Across the brass reference machine, the old path and the repaired path run side by side. One carries “pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste”; the other knows how to pack several short examples into each fixed-length row and mask their boundaries so examples cannot read one another. When the failure—the loss ignores padding, but attention and matrix multiplication still spend time and memory carrying those empty positions—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to sequence packing. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: pack several short examples into each fixed-length row and mask their boundaries so examples cannot read one another. This problem and its repair will travel under the name **Sequence Packing**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste? The answer remains the loss ignores padding, but attention and matrix multiplication still spend time and memory carrying those empty positions. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.

## Stop Training on Empty Space

Lengths 6, 5, 3, and 2 fill two rows of length 8 exactly. Padding falls from 16 allocated positions with 6 empty to 16 positions with none empty.

## The calculation hidden inside sequence packing

The enginewright carries the sequence packing scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Draw two rows with eight boxes each: sixteen paid positions. Place sequences of lengths 6 and 2 in the first row, then 5 and 3 in the second. All sixteen boxes now contain real tokens. To ask what share of the paid space teaches the model, put useful boxes over paid boxes: 16/16. Eta_pack is only a short name for that useful fraction.

The numerator counts language tokens that create lessons; the denominator counts every position for which hardware reserves work.

### Why the melody needs these exact notes

[Division](../../MATHEMATICAL_MOVES.md#division) forms the useful share per allocated position, making batches of different sizes comparable. A raw token count would reward larger batches even if their wasted fraction were worse. The ratio stays between zero and one because real tokens cannot exceed allocated positions.

Three old motions cast new shadows here: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Cover the prose about sequence packing and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
\eta_{\text{pack}}=\frac{N_{\text{real tokens}}}{N_{\text{allocated positions}}}
$$

## Where sequence packing runs out

Packing improves utilization only if masks and position resets prevent cross-example contamination.

The sequence packing repair holds, but the world asks for something it was never given. At the Engine Cavern, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the brass reference machine

Rebuild the sequence packing scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Rotary Position Embeddings — Let Distance Enter the Match](../155-rotary-position/README.md)
