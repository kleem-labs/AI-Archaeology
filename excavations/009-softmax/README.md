# Excavation 009 — Softmax

## The Problem: Scores Are Not Weights

Suppose attention produces relevance scores:

```text
animal:  2.0
street:  1.0
tired:  -1.0
```

These scores express ranking, but cannot directly form a weighted average. One is negative, and together they sum to 2 rather than 1.

We need positive weights that sum to one while preserving the preference ordering.

## Failed Attempt 1: Divide by the Sum

Dividing `[2, 1, -1]` by its sum gives `[1, 0.5, -0.5]`. The values sum to one, but a negative attention weight subtracts information.

Worse, scores `[2, -2]` sum to zero, causing division by zero.

## Failed Attempt 2: Clip Negatives

Replace negative values with zero, then normalize: `[2, 1, 0] → [0.667, 0.333, 0]`.

This produces valid weights, but introduces a hard boundary. A tiny score change from `-0.001` to `0.001` abruptly changes whether a path exists. Smooth learning benefits from smooth transformations.

## Failed Attempt 3: Select Only the Maximum

Winner-take-all maps the scores to `[1, 0, 0]`. It loses uncertainty and blocks information from every secondary source. It is also difficult to learn through because tiny score changes usually do nothing, until the winner suddenly changes.

## The Invention: Exponentiate, Then Normalize

The exponential function turns every finite score positive and preserves order:

$$e^2\approx7.389,\quad e^1\approx2.718,\quad e^{-1}\approx0.368$$

Their sum is about 10.475. Divide each by that total:

$$
\operatorname{softmax}([2,1,-1])
\approx[0.705,0.259,0.035]
$$

In general:

$$
\operatorname{softmax}(z_i)=\frac{e^{z_i}}{\sum_j e^{z_j}}
$$

Every output is positive, all outputs sum to one, and larger scores receive disproportionately larger weights.

## Why Differences Matter More Than Absolute Scores

Add 100 to every score. The probabilities remain identical:

$$
\frac{e^{z_i+100}}{\sum_j e^{z_j+100}}
=\frac{e^{100}e^{z_i}}{e^{100}\sum_j e^{z_j}}
=\frac{e^{z_i}}{\sum_j e^{z_j}}
$$

Softmax responds to score differences, not a shared offset.

## Numerical Stability

Computers cannot safely calculate $e^{1000}$. Since adding or subtracting a shared constant changes nothing, subtract the maximum score $m$ first:

$$
\operatorname{softmax}(z_i)=
\frac{e^{z_i-m}}{\sum_j e^{z_j-m}}
$$

The largest exponent is now $e^0=1$; every other exponent is at most 1. This is mathematically equivalent and computationally safe.

## Temperature: Controlling Certainty

Use a positive temperature $T$:

$$
\operatorname{softmax}(z_i/T)
$$

- Low $T$ magnifies score differences and makes the distribution sharp.
- High $T$ shrinks differences and makes it flatter.

For scores `[2, 1]`, low temperature behaves more like a decisive winner; high temperature behaves more like uncertainty. Temperature changes confidence without changing ranking.

## Code Walkthrough

`implementation.py` rejects empty scores and nonpositive temperatures. It divides by temperature, subtracts the maximum, exponentiates, and normalizes.

Run:

```bash
python3 excavations/009-softmax/implementation.py
```

Observe the same scores at temperatures `0.5`, `1`, and `2`. Then try `[1000, 1001, 1002]`. A naive implementation would overflow; the stable version succeeds.

## Common Misconceptions

**“Softmax finds probabilities that are objectively true.”** It normalizes model scores. Calibration depends on training and data.

**“A tiny softmax weight means no influence.”** Small contributions can accumulate, and later transformations may amplify them.

**“Softmax changes the ranking.”** For a fixed temperature, it preserves score order.

**“The outputs are independent.”** Increasing one score changes the normalization and therefore every output.

## The New Problem

Softmax converts relevance scores to weights, but we still need a flexible way to create the scores and separate matching from transported information. This produces queries, keys, and values.

---

Previous: [008 — Attention](../008-attention/README.md) · Next: [010 — Query, Key, Value](../010-query-key-value/README.md)
