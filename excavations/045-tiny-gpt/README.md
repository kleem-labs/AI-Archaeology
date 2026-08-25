# Excavation 045 — A Tiny GPT — Close the Prediction Loop

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Language models and useful answers

A context window bounds how much past the model can carry. We have now earned every part of a tiny GPT; the remaining question is whether those parts actually cooperate in one prediction-and-generation loop.

The previous discovery reaches the Clockwork Scriptorium carrying one unfinished problem. Beside the sentence-wheel, the mechanist first tries to call a framework Transformer and hide the causal chain.

There is good reason to begin this way. If we call a framework Transformer and hide the causal chain, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: or connect the parts without checking shapes, leakage, and target alignment.

This failure cannot be repaired by performing the instruction to call a framework Transformer and hide the causal chain more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the sentence-wheel; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to assemble token and position embeddings, masked Transformer blocks, vocabulary logits, cross-entropy training, and iterative sampling in one traceable program. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **A Tiny GPT**. The name is simply a handle for the distinction already reconstructed.

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
