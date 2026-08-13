# Excavation 154 — Sequence Packing — Stop Training on Empty Space

The input pipeline now keeps the device busy. Inspection shows that many of the tokens occupying each fixed rectangle are padding rather than language.

Perhaps we pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste.

It survives until the measured run answers back. The loss ignores padding, but attention and matrix multiplication still spend time and memory carrying those empty positions.

Now the missing requirement is concrete. Pack several short examples into each fixed-length row and mask their boundaries so examples cannot read one another.

## Let one run decide

Lengths 6, 5, 3, and 2 fill two rows of length 8 exactly. Padding falls from 16 allocated positions with 6 empty to 16 positions with none empty.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

Draw two rows with eight boxes each: sixteen paid positions. Place sequences of lengths 6 and 2 in the first row, then 5 and 3 in the second. All sixteen boxes now contain real tokens. To ask what share of the paid space teaches the model, put useful boxes over paid boxes: 16/16. Eta_pack is only a short name for that useful fraction.

The numerator counts language tokens that create lessons; the denominator counts every position for which hardware reserves work.

### Why these operations are forced

[Division](../../MATHEMATICAL_MOVES.md#division) forms the useful share per allocated position, making batches of different sizes comparable. A raw token count would reward larger batches even if their wasted fraction were worse. The ratio stays between zero and one because real tokens cannot exceed allocated positions.

Only now can we compress the procedure:

$$
\eta_{\text{pack}}=\frac{N_{\text{real tokens}}}{N_{\text{allocated positions}}}
$$

## What this repair cannot do

Packing improves utilization only if masks and position resets prevent cross-example contamination.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Rotary Position Embeddings — Let Distance Enter the Match](../155-rotary-position/README.md)
