# Excavation 045 — A Tiny GPT — Close the Prediction Loop

[Previous: Excavation 044](../044-context-window/README.md)

## Problem

We have excavated every component of an autoregressive language model, but isolated demonstrations do not prove the parts cooperate.

## Naive Attempt

Call a framework Transformer and hide the causal chain. Or connect the parts without checking shapes, leakage, and target alignment.

## Why It Fails

The attempt either gives the model forbidden information, discards useful structure, or performs repeated work without solving the actual representation problem.

## Better Attempt

Assemble token and position embeddings, masked Transformer blocks, vocabulary logits, cross-entropy training, and iterative sampling in one traceable program.

## Why It Still Fails

A tiny GPT demonstrates the mechanism, not modern capability. Scale, data quality, optimization, evaluation, and safety now become the next landscape.

## Key Insight

**Assemble token and position embeddings, masked Transformer blocks, vocabulary logits, cross-entropy training, and iterative sampling in one traceable program.**

## Mathematics Emerges

## Walk It Once with Concrete Values

Prompt IDs enter embeddings, pass through a masked block, and produce logits [1,3,0]. Softmax favors the second token; sampling selects it, appends it to the prompt, and runs the same loop again.

## Why Every Term Must Exist Before the Equation

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

## Real-World Analogy

An archaeological reconstruction succeeds when the rebuilt machine moves, not when labeled components remain on separate tables.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

## Next Need

The mechanism now runs. The next excavations must test what it learned, where it fails, and how modern systems extend it.
