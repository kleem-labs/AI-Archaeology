# Excavation 014 — Layer Normalization

## The Problem: Representations Drift in Scale

After many transformations and residual additions, one token might contain `[0.01, 0.02, 0.03]` while another contains `[100, 200, 300]`. Later dot products and nonlinearities respond very differently to those scales. Training must constantly compensate for shifting numerical conditions.

## Failed Attempt: Use One Global Scale

A global dataset mean cannot adapt to each token's current representation. Batch normalization uses statistics across examples, but language batches may have different lengths, padding patterns, and inference conditions. We want normalization that works for one token independently.

## The Invention: Normalize Across Features

For one token vector $\mathbf{x}$ with $d$ features, compute:

$$
\mu=\frac{1}{d}\sum_i x_i,
\qquad
\sigma^2=\frac{1}{d}\sum_i(x_i-\mu)^2
$$

Then normalize and apply learned scale and shift:

$$
\operatorname{LN}(x_i)=\gamma_i\frac{x_i-\mu}{\sqrt{\sigma^2+\epsilon}}+\beta_i
$$

$\epsilon$ prevents division by zero. Learned $\gamma$ and $\beta$ let the model restore useful scales and offsets rather than forcing every feature to remain standardized forever.

## Worked Example

For `[1, 2, 3]`, the mean is 2 and variance is $2/3$. Before learned scale and shift, normalization produces approximately `[-1.225, 0, 1.225]`. For `[10, 20, 30]`, it produces the same pattern. Absolute scale is removed; relative structure remains.

## Pre-Norm and Post-Norm

Two common layouts are:

$$x+F(\operatorname{LN}(x))\quad\text{(pre-norm)}$$

and

$$\operatorname{LN}(x+F(x))\quad\text{(post-norm)}$$

They contain the same ingredients but create different optimization behavior. Many modern large transformers use pre-norm because the residual stream retains a particularly direct path.

## Code Walkthrough

`implementation.py` calculates mean, variance, normalization, and optional learned scale and shift. Run it on `[1,2,3]` and `[10,20,30]`. Then try `[5,5,5]` to see why epsilon is necessary.

## Common Misconceptions

**“Normalization deletes magnitude information permanently.”** Learned scale and surrounding transformations can encode magnitude; normalization controls one unstable degree of freedom.

**“Layer normalization mixes examples.”** It normally computes statistics across features within each token independently.

**“Normalized means every output lies between 0 and 1.”** Layer normalization targets zero mean and unit variance before learned affine parameters.

## The New Problem

We now possess the major parts of a transformer block, but every matrix still contains arbitrary numbers. How does experience alter millions or billions of parameters so predictions improve? We must invent learning.

---

Previous: [013 — Residual Connections](../013-residual-connections/README.md) · Next: [015 — Learning](../015-learning/README.md)
