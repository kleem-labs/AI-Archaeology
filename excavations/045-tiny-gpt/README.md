# Excavation 045 — A Tiny GPT — Close the Prediction Loop

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Language models and useful answers

A context window bounds how much past the model can carry. We have now earned every part of a tiny GPT; the remaining question is whether those parts actually cooperate in one prediction-and-generation loop.

A new case arrives at the Clockwork Scriptorium, but the mechanist first reaches for the familiar sentence-wheel. Its promise is simple: call a framework Transformer and hide the causal chain.

Then the quiet test arrives: or connect the parts without checking shapes, leakage, and target alignment. What looked like simplicity is revealed as a missing distinction.

*The mechanist sketches the break before changing it:*

```text
observation
    │
    ▼
[call a framework Transformer and hide…]
    │
    ╳  or connect the parts without checking…
    │
    ▼
[assemble token and position…]
```

The mechanist turns the sentence-wheel toward the light. Through the old engraving, call a framework Transformer and hide the causal chain, the evidence ends in the same contradiction: or connect the parts without checking shapes, leakage, and target alignment. A second engraving adds only the power to assemble token and position embeddings, masked Transformer blocks, vocabulary logits, cross-entropy training, and iterative sampling in one traceable program. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The mechanist circles the place where the two tiny gpt cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: assemble token and position embeddings, masked Transformer blocks, vocabulary logits, cross-entropy training, and iterative sampling in one traceable program. The mechanist writes **A Tiny GPT** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The mechanist does not memorize tiny gpt. Instead, the mechanist memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can assemble token and position embeddings, masked Transformer blocks, vocabulary logits, cross-entropy training, and iterative sampling in one traceable program. The formal name merely lets that motion be shared.

## The calculation hidden inside a tiny gpt

The mechanist carries the tiny gpt scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A tiny GPT demonstrates the mechanism, not modern capability. Scale, data quality, optimization, evaluation, and safety now become the next landscape.

Begin with the prompt “the tiger.” Its token addresses fetch learned starting descriptions; position marks preserve order; masked attention gathers only allowed context; token workshops transform what was gathered; and the output scores every possible next word. Suppose sampling chooses *sleeps*. Appending that choice creates “the tiger sleeps,” and the same mechanism now faces a new prediction. The language model exists only when this entire loop closes.

### Naming what is already on the table

**tokens** are discrete addresses produced by the tokenizer.
**embeddings** turn addresses into vectors; Transformer **blocks** contextualize them under causal masking.
**logits** score every next-token candidate; **loss** compares those scores with the observed answer.
**update** changes parameters using backpropagated error.
**sample** chooses a continuation and feeds it back as the next token.
The arrows encode one closed causal loop, not an unexplained algebraic equality.

### Why the melody needs these exact notes

[Arrows](../../MATHEMATICAL_MOVES.md#arrows) show dependency and order rather than equality: tokens become representations, representations produce scores, loss produces gradients, and an update changes what the next sample can be.
The loop matters more than any isolated sign. Removing one arrow breaks the causal path by which observed text can change future generation.

The story of tiny gpt has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
tokens\to embeddings\to blocks\to logits\to loss\to update\to sample
$$

The equation arrives after every operation has a job.

## A Tiny GPT beyond this one case

An archaeological reconstruction succeeds when the rebuilt machine moves, not when labeled components remain on separate tables.

## A sentence enters; a future leaves

Characters became tokens, tokens found coordinates, positions supplied order, masks protected honesty, and logits opened a competition among possible next words. The tiny GPT is not one invention. It is a procession of necessities moving through a sentence.

```text
text → tokens → positions → context → probabilities → next token
```

The trail called *a sentence enters; a future leaves* is what remains when one necessity becomes another.

## Return to the sentence-wheel

Rebuild the tiny gpt scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Perplexity](../046-perplexity/README.md)
