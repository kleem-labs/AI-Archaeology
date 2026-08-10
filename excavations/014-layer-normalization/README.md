# Excavation 014 — Layer Normalization

[Previous: Residual Connections](../013-residual-connections/README.md)

Several experts are speaking into a shared system. One whispers; another shouts. Even if both carry useful patterns, the next operation may respond mostly to volume.

Representations drift similarly. After many transformations and residual additions, one token may contain values around `0.01`, another around `100`. Dot products and gates react very differently to those scales.

## Failed attempt: one global volume knob

A single dataset-wide adjustment cannot respond to the current feature pattern of each token. We want every token to arrive at the next workshop on a predictable scale while preserving the relative pattern inside it.

## Recenter, then rescale

For one token's feature vector:

1. find its average level;
2. subtract that level from every feature;
3. measure how spread out the centered features are;
4. divide by that spread.

The transformation `[1, 2, 3]` and `[10, 20, 30]` then produces the same normalized pattern. Absolute volume disappears; relative shape remains.

Only after this procedure feels natural do we compress it:

## Build Every Piece from the Concrete Example

Three microphones hear the same roar at volumes 1, 2, and 3 because one sits closer to the tiger. Their shared centre is 2. Subtracting it leaves the pattern `[-1, 0, 1]`: quieter, typical, louder. Dividing by the pattern's spread makes that relative shape comparable with another set recorded by more sensitive microphones. A tiny safety amount is needed when all microphones report the same value and the spread is zero.

### Give Short Names Only After We Know the Pieces

- **xᵢ** is one feature of a token and **d** is its number of features.
- Summing and dividing by d creates μ, the token's average level.
- Subtracting μ recenters every feature.
- Squaring centered values prevents cancellation; averaging them creates variance σ².
- The square root converts variance to ordinary scale.
- Dividing produces comparable spread; ε prevents division by zero when no spread exists.
- **x̂ᵢ** is the normalized feature.


The small $\epsilon$ prevents division by zero when every feature is equal.

Forcing every representation to remain permanently standardized would itself be restrictive. Learned scale and shift parameters therefore let the model restore useful volumes and offsets after normalization.

Layer normalization is not intelligence and does not create meaning. It creates stable numerical conditions in which learned transformations can operate.

Only now can we compress that reasoning:

$$
\mu=\frac1d\sum_i x_i,
\qquad
\sigma^2=\frac1d\sum_i(x_i-\mu)^2
$$

$$
\widehat{x}_i=\frac{x_i-\mu}{\sqrt{\sigma^2+\epsilon}}
$$


## Challenge

Without calculating exact decimals, predict why `[1, 2, 3]` and `[100, 200, 300]` have the same normalized pattern.

## What the next excavation needs

We now have the parts of a Transformer, but every matrix begins random. Architecture provides a brain-shaped machine, not knowledge.

[Next: Learning](../015-learning/README.md)
