# Excavation 154 — Sequence Packing — Stop Training on Empty Space

<!-- book-prose-v2 -->

The input pipeline now keeps the device busy. Inspection shows that many of the tokens occupying each fixed rectangle are padding rather than language.

We can postpone invention if we simply pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste.

If the proposal works on every relevant case, sequence packing is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

Its hidden assumption becomes visible as soon as we observe that the loss ignores padding, but attention and matrix multiplication still spend time and memory carrying those empty positions.

Nothing magical creates sequence packing. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: pack several short examples into each fixed-length row and mask their boundaries so examples cannot read one another.

This boundary between the failed rule and its repair is the subject later work calls **Sequence Packing**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize sequence packing; try to break it by subtraction. Remove the part that knows how to pack several short examples into each fixed-length row and mask their boundaries so examples cannot read one another, leaving only the attempt to pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste. What returns is not a vague weakness but the original contradiction: the loss ignores padding, but attention and matrix multiplication still spend time and memory carrying those empty positions. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste receives the same test as the rule to pack several short examples into each fixed-length row and mask their boundaries so examples cannot read one another. Their different outcomes reveal what sequence packing contributes without asking the reader to trust historical convention.

## Stop Training on Empty Space

Lengths 6, 5, 3, and 2 fill two rows of length 8 exactly. Padding falls from 16 allocated positions with 6 empty to 16 positions with none empty.

Hold the setting, evidence, and desired outcome fixed while testing sequence packing. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

## The calculation hidden inside sequence packing

Do not read the coming Sequence Packing line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Draw two rows with eight boxes each: sixteen paid positions. Place sequences of lengths 6 and 2 in the first row, then 5 and 3 in the second. All sixteen boxes now contain real tokens. To ask what share of the paid space teaches the model, put useful boxes over paid boxes: 16/16. Eta_pack is only a short name for that useful fraction.

The numerator counts language tokens that create lessons; the denominator counts every position for which hardware reserves work.

### Why no cheaper operation does the same job

[Division](../../MATHEMATICAL_MOVES.md#division) forms the useful share per allocated position, making batches of different sizes comparable. A raw token count would reward larger batches even if their wasted fraction were worse. The ratio stays between zero and one because real tokens cannot exceed allocated positions.

Every symbol in Sequence Packing can now be read back into an action already performed. The whole procedure fits in one line:

$$
\eta_{\text{pack}}=\frac{N_{\text{real tokens}}}{N_{\text{allocated positions}}}
$$

## Where sequence packing runs out

Packing improves utilization only if masks and position resets prevent cross-example contamination.

This is where sequence packing runs out for a causal reason. We gave it enough structure to pack several short examples into each fixed-length row and mask their boundaries so examples cannot read one another, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

## Take sequence packing to the workbench

A mathematical story about sequence packing earns trust only when the failed and repaired paths can both be reproduced. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running sequence packing, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the sequence packing result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Rotary Position Embeddings — Let Distance Enter the Match](../155-rotary-position/README.md)
