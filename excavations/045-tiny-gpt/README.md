# Excavation 045 — A Tiny GPT — Close the Prediction Loop

<!-- book-prose-v2 -->

A context window bounds how much past the model can carry. We have now earned every part of a tiny GPT; the remaining question is whether those parts actually cooperate in one prediction-and-generation loop.

At this point the shortest path seems to be to call a framework Transformer and hide the causal chain.

This is how a tiny gpt ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

Reality now asks a question the retained information cannot answer: or connect the parts without checking shapes, leakage, and target alignment.

The wrong answer makes the need for a tiny gpt inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: assemble token and position embeddings, masked Transformer blocks, vocabulary logits, cross-entropy training, and iterative sampling in one traceable program.

The usual name, **A Tiny GPT**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to call a framework Transformer and hide the causal chain. produces the observed failure: or connect the parts without checking shapes, leakage, and target alignment. Starting with the repaired demand to assemble token and position embeddings, masked Transformer blocks, vocabulary logits, cross-entropy training, and iterative sampling in one traceable program preserves the information the shortcut lost. The subject of a tiny gpt lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to assemble token and position embeddings, masked Transformer blocks, vocabulary logits, cross-entropy training, and iterative sampling in one traceable program instead of merely trying to call a framework Transformer and hide the causal chain.. That controlled contrast is what turns a plausible explanation of a tiny gpt into an understandable derivation.

## The calculation hidden inside a tiny gpt

Before A Tiny GPT receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

A tiny GPT demonstrates the mechanism, not modern capability. Scale, data quality, optimization, evaluation, and safety now become the next landscape.

Begin with the prompt “the tiger.” Its token addresses fetch learned starting descriptions; position marks preserve order; masked attention gathers only allowed context; token workshops transform what was gathered; and the output scores every possible next word. Suppose sampling chooses *sleeps*. Appending that choice creates “the tiger sleeps,” and the same mechanism now faces a new prediction. The language model exists only when this entire loop closes.

### Names for pieces we have already used

**tokens** are discrete addresses produced by the tokenizer.
**embeddings** turn addresses into vectors; Transformer **blocks** contextualize them under causal masking.
**logits** score every next-token candidate; **loss** compares those scores with the observed answer.
**update** changes parameters using backpropagated error.
**sample** chooses a continuation and feeds it back as the next token.
The arrows encode one closed causal loop, not an unexplained algebraic equality.

### Why no cheaper operation does the same job

[Arrows](../../MATHEMATICAL_MOVES.md#arrows) show dependency and order rather than equality: tokens become representations, representations produce scores, loss produces gradients, and an update changes what the next sample can be.
The loop matters more than any isolated sign. Removing one arrow breaks the causal path by which observed text can change future generation.

The notation is finally shorter than the story that created it:

$$
tokens\to embeddings\to blocks\to logits\to loss\to update\to sample
$$

The equation arrives after every operation has a job.

## A Tiny GPT beyond this one case

An archaeological reconstruction succeeds when the rebuilt machine moves, not when labeled components remain on separate tables.

## Take a tiny gpt to the workbench

The reader has reconstructed a tiny gpt in words; the workbench tests whether those words specify a real procedure. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Close the loop yourself in the [Transparent Generation Field Lab](../../labs/05_generation_lab.py). Every generated token prints the scores, probabilities, choice, and updated context. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running a tiny gpt, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the a tiny gpt result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Perplexity](../046-perplexity/README.md)
