# Excavation 036 — Tokenization: What Can a Language Model See?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Information Theory](../../MATHEMATICS_ATLAS.md#information) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Language models and useful answers

> **PART IV — BUILDING A TINY GPT**
>
> You have built a learner. Now place language in its hands and discover every mechanism required to make one token predict another.

The tiny neural network now learns from numbered examples. People do not speak in fixed numerical columns; they produce an open stream of words, punctuation, names, code, and writing systems.

Inside the Clockwork Scriptorium, every old tool is given one honest chance. The mechanist sets the sentence-wheel between the evidence and the desired answer, then tries to give every complete word one ID.

For a moment the mark looks complete. Then the evidence refuses to fit: spaces appear to provide the boundaries. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The mechanist sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ give every complete word one ID ──▶ blurred: spaces appear to provide the…
      │
      └── new lens ──▶ use characters. Any new spelling can… ──▶ distinction survives
```

The mechanist lays two translucent sheets over the sentence-wheel. The first is inscribed, “give every complete word one ID.” Its path ends where spaces appear to provide the boundaries. The second receives the same evidence but is allowed to use characters. Any new spelling can now be represented. Held to the light, the sheets separate at exactly one decision.

No one reaches for a tokenization formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The mechanist changes only that one responsibility: use characters. Any new spelling can now be represented. When the ink dries, the name **Tokenization** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The sentence-wheel keeps both histories. Its older mark still says, ‘give every complete word one ID’; beside it, the newer mark says, ‘use characters. Any new spelling can now be represented.’ The distance between those sentences is the exact shape of tokenization: no larger than the failure required, and no smaller than reality permits. The sentence-wheel turns with machinery earned long before language: indices retrieve, vectors carry features, dot products compare directions, and weighted sums gather context. tokenization changes what travels through the machine, not why those operations exist.

## The calculation hidden inside tokenization

The mechanist carries the tokenization scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Common words become long sequences and the model must reconstruct recurring fragments such as ing repeatedly. Words are too large; characters are often too small.

In low, lower, lowest, pair l-o appears three times, more than e-r once. Counting selects l-o; merging creates lo. Recounting can then select lo-w and create reusable low.

### Naming what is already on the table

**a and b** are neighboring current tokens; c(a,b) counts their repeated adjacency because repetition is the evidence for reuse.
The star marks the pair selected for merging.
**arg max** returns the pair itself, not its count, because that pair must be replaced.
Maximizing over every candidate pair makes the merge arise from the corpus rather than a hand-written linguistic rule.

Count, choose, merge, and repeat. The symbols only compress the procedure already needed.

### Why the melody needs these exact notes

[The first equality](../../MATHEMATICAL_MOVES.md#equals) defines c(a,b) as the observed adjacency count; the parentheses keep the candidate pair together.
[Arg max](../../MATHEMATICAL_MOVES.md#arg-max) returns the pair whose count is largest because the tokenizer must know **what to merge**. Max alone would return only the winning count.
[The star](../../MATHEMATICAL_MOVES.md#symbol-decorations) marks the selected winner; it is a label on a and b, not multiplication or exponentiation.

Every mark needed for tokenization is now visible on the sentence-wheel. The symbols do not add an idea; they bind the discovered moves into one line:

$$
c(a,b)=\text{number of adjacent occurrences of }(a,b)
$$

$$
(a^*,b^*)=\underset{(a,b)}{\text{arg max}} c(a,b)
$$

## Tokenization beyond this one case

Early readers sound out letters. With experience they recognize recurring fragments and whole familiar words while retaining the ability to sound out something new.

## Concrete Discovery

For low, lower, and lowest, the pair l-o repeats three times. Merge it into lo. The pair lo-w then repeats three times, so low becomes reusable. Nobody declared low meaningful; repetition made keeping it whole economical.

## Where tokenization runs out

Tokenization chooses pieces, not meanings. IDs remain arbitrary, and the chosen vocabulary affects sequence length, cost, multilingual coverage, and which patterns are easy to notice.

At the Clockwork Scriptorium, the mechanist leaves a blank beneath the new mark. Tokenization has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the sentence-wheel

Rebuild the tokenization scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Input Embeddings](../037-input-embeddings/README.md)
