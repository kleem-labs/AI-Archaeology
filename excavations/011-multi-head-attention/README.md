# Excavation 011 — Multi-Head Attention

## The Problem: One Notion of Relevance Is Not Enough

Read: “The small robot beside the red boxes **moves** because **it** detects smoke.” To represent *it*, a model may need to connect it to *robot*. To represent *moves*, it may need grammatical agreement with *robot*. To understand *red*, it should modify *boxes*. Position, syntax, reference, and meaning coexist.

A single attention operation creates one score matrix—one geometry of relevance. Asking it to express every useful relationship at once creates a bottleneck.

## Failed Attempt: Make One Head Wider

More dimensions give one head capacity, but it still produces one softmax distribution per query. Strong unrelated patterns compete for the same probability mass. If one relationship needs to emphasize a nearby adjective and another needs a distant subject, one compromise distribution may serve neither cleanly.

## The Invention: Parallel Attention Heads

Give the same input several independent sets of projections:

$$
\text{head}_h=\operatorname{Attention}(XW_Q^{(h)},XW_K^{(h)},XW_V^{(h)})
$$

Each head learns its own query, key, and value space. Concatenate their outputs and mix them with a final matrix:

$$
\operatorname{MultiHead}(X)=\operatorname{Concat}(\text{head}_1,\ldots,\text{head}_H)W_O
$$

One head can route by locality while another routes by reference—not because we assign those roles, but because training can benefit from specialization.

## Worked Shape Example

Suppose the model width is 4 and we use two heads of width 2. For three tokens, input $X$ has shape `3 × 4`. Each head projects it into queries, keys, and values of shape `3 × 2`, then returns `3 × 2`. Concatenation restores `3 × 4`; $W_O$ mixes information across heads while preserving model width.

Splitting the width keeps total attention output manageable. Two heads do not necessarily double the representation size.

## Why Concatenate Instead of Average?

Averaging would blur head identities before the model can decide how to use them. Concatenation preserves every head's coordinates; the output projection learns which combinations matter.

## Code Walkthrough

`implementation.py` reuses scaled attention, runs two heads with distinct projections, concatenates corresponding token outputs, and applies an output matrix. Run it and inspect how changing one head alters only part of the concatenated vector before $W_O$ mixes it.

## Common Misconceptions

**“Every head has a neat linguistic job.”** Some specialize, some overlap, and some appear redundant. Roles are learned, not labeled.

**“More heads are always better.”** Too many tiny heads can lack capacity; architecture choices trade width against parallel views.

**“Heads operate independently forever.”** Their outputs are mixed immediately by $W_O$ and later layers.

## The New Problem

Attention lets tokens exchange information, but its output is still a weighted mixture of existing values. Each token now needs private computation that can transform, combine, and create features. That is the feed-forward network.

---

Previous: [010 — Query, Key, Value](../010-query-key-value/README.md) · Next: [012 — Feed-Forward Networks](../012-feed-forward-networks/README.md)
