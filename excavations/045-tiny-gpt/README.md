# Excavation 045 — A Tiny GPT — Close the Prediction Loop

[Previous: Excavation 044](../044-context-window/README.md)

We have excavated every component of an autoregressive language model, but isolated demonstrations do not prove the parts cooperate.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Call a framework Transformer and hide the causal chain. Or connect the parts without checking shapes, leakage, and target alignment.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Call a framework Transformer and hide the causal chain. Or connect the parts without checking shapes, leakage, and target alignment.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Assemble token and position embeddings, masked Transformer blocks, vocabulary logits, cross-entropy training, and iterative sampling in one traceable program.

Only after that reasoning may we give your discovery its inherited name.

## Why It Still Fails

A tiny GPT demonstrates the mechanism, not modern capability. Scale, data quality, optimization, evaluation, and safety now become the next landscape.

## Compress your discovery into mathematics


## Build each piece from what just happened

Prompt IDs enter embeddings, pass through a masked block, and produce logits [1,3,0]. Softmax favors the second token; sampling selects it, appends it to the prompt, and runs the same loop again.

### Give Short Names Only After We Know the Pieces

- **tokens** are discrete addresses produced by the tokenizer.
- **embeddings** turn addresses into vectors; Transformer **blocks** contextualize them under causal masking.
- **logits** score every next-token candidate; **loss** compares those scores with the observed answer.
- **update** changes parameters using backpropagated error.
- **sample** chooses a continuation and feeds it back as the next token.
- The arrows encode one closed causal loop, not an unexplained algebraic equality.

Only now can we compress that reasoning:

$$
tokens\to embeddings\to blocks\to logits\to loss\to update\to sample
$$


The equation arrives after every operation has a job.

## Carry the idea back into the world

An archaeological reconstruction succeeds when the rebuilt machine moves, not when labeled components remain on separate tables.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

Close the loop yourself in the [Transparent Generation Field Lab](../../labs/05_generation_lab.py). Every generated token prints the scores, probabilities, choice, and updated context.

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

## Next Need

The mechanism now runs. The next excavations must test what it learned, where it fails, and how modern systems extend it.

[Next: Perplexity](../046-perplexity/README.md)
