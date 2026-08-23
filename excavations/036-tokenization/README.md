# Excavation 036 — Tokenization: What Can a Language Model See?

<!-- book-prose-v2 -->

> **PART IV — BUILDING A TINY GPT**
>
> You have built a learner. Now place language in its hands and discover every mechanism required to make one token predict another.

The tiny neural network now learns from numbered examples. People do not speak in fixed numerical columns; they produce an open stream of words, punctuation, names, code, and writing systems.

The least expensive next move is to give every complete word one ID.

The proposal deserves a fair hearing. For tokenization, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The proposal breaks for a specific reason, not by authority: spaces appear to provide the boundaries.

The failure changes the question behind tokenization. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: use characters. Any new spelling can now be represented.

Only at this point does the inherited name **Tokenization** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of tokenization by mentally removing the repair. We fall back to the proposal to give every complete word one ID.; then spaces appear to provide the boundaries. Restore only the ability to use characters. Any new spelling can now be represented, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to give every complete word one ID. to requiring the system to use characters. Any new spelling can now be represented. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to tokenization.

## The calculation hidden inside tokenization

Do not read the coming Tokenization line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Common words become long sequences and the model must reconstruct recurring fragments such as ing repeatedly. Words are too large; characters are often too small.

In low, lower, lowest, pair l-o appears three times, more than e-r once. Counting selects l-o; merging creates lo. Recounting can then select lo-w and create reusable low.

### Names for pieces we have already used

**a and b** are neighboring current tokens; c(a,b) counts their repeated adjacency because repetition is the evidence for reuse.
The star marks the pair selected for merging.
**arg max** returns the pair itself, not its count, because that pair must be replaced.
Maximizing over every candidate pair makes the merge arise from the corpus rather than a hand-written linguistic rule.

Count, choose, merge, and repeat. The symbols only compress the procedure already needed.

### Why no cheaper operation does the same job

[The first equality](../../MATHEMATICAL_MOVES.md#equals) defines c(a,b) as the observed adjacency count; the parentheses keep the candidate pair together.
[Arg max](../../MATHEMATICAL_MOVES.md#arg-max) returns the pair whose count is largest because the tokenizer must know **what to merge**. Max alone would return only the winning count.
[The star](../../MATHEMATICAL_MOVES.md#symbol-decorations) marks the selected winner; it is a label on a and b, not multiplication or exponentiation.

The notation is finally shorter than the story that created it:

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

The limit follows from the job assigned to tokenization. Its repair knows how to use characters. Any new spelling can now be represented. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take tokenization to the workbench

A claim about tokenization now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running tokenization, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the tokenization result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Input Embeddings](../037-input-embeddings/README.md)
