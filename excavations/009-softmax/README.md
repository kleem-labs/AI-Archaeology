# Excavation 009 — Softmax

## The Problem

Attention produces relevance scores such as `[2.0, 1.0, -1.0]`. They are not yet mixture weights: one is negative and they do not sum to one.

## Failed Attempts

Dividing by the sum fails when scores are negative or cancel to zero. Clipping negatives destroys useful ordering and creates abrupt boundaries. Selecting only the largest score prevents softer combinations.

## The Invention

Exponentiate every score and normalize:

$$
\operatorname{softmax}(z_i)=\frac{e^{z_i}}{\sum_j e^{z_j}}
$$

Exponentials are positive, so every result is positive. Dividing by their sum makes the results add to one. Larger scores receive disproportionately more weight while smaller scores still receive some.

## Numerical Stability

Large exponentials overflow. Subtracting the largest score changes no softmax probability:

$$
\frac{e^{z_i-m}}{\sum_j e^{z_j-m}}
$$

This stable form is the one implementations should use.

## Temperature

Dividing scores by temperature $T$ controls sharpness. Low temperature approaches winner-take-all; high temperature produces a flatter distribution.

## The New Problem

We can normalize scores, but where should relevance scores come from? Each token must express what it seeks, what it offers for matching, and what information it can contribute. These become queries, keys, and values.

---

Previous: [008 — Attention](../008-attention/README.md) · Next: [010 — Query, Key, Value](../010-query-key-value/README.md)
