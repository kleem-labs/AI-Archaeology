# Excavation 008 — Attention

## The Problem: The Same Word Needs Different Information

Compare:

1. “The animal did not cross the street because **it** was tired.”
2. “The animal did not cross the street because **it** was flooded.”

In the first sentence, *it* depends strongly on *animal*. In the second, it depends on *street*. The token is identical, but the useful context differs.

A fixed embedding cannot decide this alone. We need a new representation for each token in each sentence.

## Failed Attempt 1: Average Every Word

Give each token the average of the whole sentence. This includes context, but every token receives the same mixture. Important clues and irrelevant words contribute equally. The animal and street lose their distinct roles.

## Failed Attempt 2: Use Only Nearby Words

A fixed window works for “red car,” but language can connect distant positions:

> The keys to the old cabinet near the stairs **are** missing.

The verb agrees with *keys*, not the closer nouns *cabinet* or *stairs*. Relevant information is not always adjacent.

## Failed Attempt 3: Compress the Past into One State

Recurrent models pass a running state from token to token. This is powerful, but every past detail must travel through one evolving bottleneck. Long-range information can become difficult to preserve and retrieve.

## The Invention: Let Each Token Choose

For a receiving token $i$, assign every available token $j$ a relevance weight $\alpha_{ij}$, then mix their information vectors $\mathbf{v}_j$:

$$
\text{output}_i=\sum_j\alpha_{ij}\mathbf{v}_j
$$

This is **attention**. Each receiving token gets its own weighted view of the sequence.

## Worked Example

Suppose the possible sources are:

```text
animal value = [1.0, 0.2]
street value = [0.1, 1.0]
tired  value = [0.8, 0.3]
```

For interpreting *it* in the tired sentence, imagine weights:

```text
animal: 0.65
street: 0.05
tired:  0.30
```

The output is:

$$
0.65[1,0.2]+0.05[0.1,1]+0.30[0.8,0.3]
=[0.895,0.27]
$$

It resembles the animal information while incorporating the clue *tired*. In the flooded sentence, higher weight on street would produce a different representation.

## Attention as Information Routing

Attention answers two separate questions:

1. **Where should information come from?** The weights.
2. **What should be transported?** The value vectors.

This makes attention more than similarity visualization. It is a computational route through which one representation changes another.

## Self-Attention

When queries, candidate sources, and values all come from the same sequence, the operation is **self-attention**. Every token can construct a context-sensitive version of itself by consulting the others.

In other settings, a decoder may attend to representations produced by an encoder. The central idea remains weighted retrieval.

## Code Walkthrough

`implementation.py` isolates the final step: `weighted_sum`. It checks that there is one weight per vector, that weights sum to one, and that all vectors share a width.

Run:

```bash
python3 excavations/008-attention/implementation.py
```

Then change the weights to `[0.05, 0.80, 0.15]`. The available value vectors stay fixed, but the output moves toward street. Attention changes representation by changing routing.

## Common Misconceptions

**“Attention weights are guaranteed explanations.”** They show part of a model's information flow, but behavior may be distributed across heads, layers, value transformations, and later computation.

**“Attention stores knowledge.”** Model parameters store learned transformations; attention dynamically combines representations for the current input.

**“The highest weight is all that matters.”** Several moderate contributions can jointly determine the output.

## The New Problem

We have assumed valid weights. Real relevance scores may be negative, unbounded, and fail to sum to one. We need a smooth conversion from arbitrary scores to a usable distribution.

---

Previous: [007 — Embeddings](../007-embeddings/README.md) · Next: [009 — Softmax](../009-softmax/README.md)
