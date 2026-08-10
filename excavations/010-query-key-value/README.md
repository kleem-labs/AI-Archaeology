# Excavation 010 — Query, Key, and Value

[Previous: Softmax](../009-softmax/README.md)

Return to the trophy sentence. The word *it* is looking for something like “a previously mentioned physical object that can participate in this size relationship.” Each earlier word offers different clues.

This suggests two cards:

```text
Query: what information am I looking for?
Key:   what kind of match can I offer?
```

## Similarity is the wrong question

At first we might reuse Euclidean distance. You rejected that for the right reason:

> Distance says similar. Here we are looking for relevant.

A doctor and a hospital are not similar objects, yet they can be strongly related. Attention asks a directional question: “How useful are you to me right now?”

## Your scoring operation

You proposed comparing corresponding features, multiplying them, and adding everything to get one score.

Suppose a query is `[1, 2, 3]` and a key is `[2, 1, 4]`. Feature by feature:

```text
1×2 contributes 2
2×1 contributes 2
3×4 contributes 12
```

If both sides care strongly about the same feature, the contribution is large. If one side has zero interest, the contribution vanishes. Opposing signs create negative evidence rather than being discarded. Adding the contributions gives one relevance score.

Only now do we write the operation you rediscovered—the dot product:

## Build Every Piece from the Concrete Example

A librarian hears, “Find me the book about a striped predator.” The request emphasizes *animal* and *stripes*. A catalogue card advertises the same properties; matching request-property to catalogue-property produces relevance. If that card wins three quarters of the attention, three quarters of the book's stored content—not three quarters of its catalogue description—travels into the answer. The request becomes the query, the catalogue becomes the key, and the retrievable content becomes the value only after those jobs are distinct.

### Give Short Names Only After We Know the Pieces

- **qᵢ** states what receiving token i needs; **kⱼ** states what source j offers.
- Multiplying matching coordinates rewards aligned needs and offers; opposite signs become negative evidence.
- Summing over feature r turns many alignments into one score sᵢⱼ.
- **αᵢⱼ** is that score after normalization: how much i listens to j.
- **vⱼ** is the content source j contributes; multiplying by α scales its voice.
- Summing over j combines every permitted source into output oᵢ.


Learned matrices create query, key, and value views from each current representation. Their formulas record three roles we already needed; they are not arbitrary symmetry.

Only now can we compress that reasoning:

$$
s_{ij}=\mathbf{q}_i\cdot\mathbf{k}_j
=\sum_r q_{ir}k_{jr}
$$

For each receiving word, its whole query is compared with the whole key of every available source word. The feature-wise products happen inside each comparison; the sum creates one score per source.

## Why a third vector exists

Query and key decide who matters. They do not say what information should travel.

When asked how three experts should contribute, you answered:

> Each expert contributes what they do—the knowledge related to their profession and domain.

Exactly. A historian's matching description is not the historical knowledge we want to retrieve. Each source therefore needs a **Value**: the content it contributes if selected.

```text
Query ↔ Key → score → softmax weight
Value × weight → contributed information
```

The output for one token is finally the weighted sum of source values:

$$
\mathbf{o}_i=\sum_j \alpha_{ij}\mathbf{v}_j
$$


## Challenge

For a library search, identify the query, the key-like catalog information, and the value-like content returned. Explain why catalog fields and book contents should not be the same object.

Make those three jobs visible in the [Attention Field Lab](../../labs/03_attention_lab.py): change a key without changing its value, then reverse the experiment.

## What the next excavation needs

One relevance system can pursue one mixture of relationships. Language needs several kinds of relevance at the same time.

[Next: Multi-Head Attention](../011-multi-head-attention/README.md)
