# Excavation 003 — Distance

[Previous: Vectors](../002-vectors/README.md)

The king asks for the animal most similar to Tiger A.

```text
Tiger A = [220, 65, 6]
Tiger B = [225, 66, 5]
Rabbit  = [  2, 45, 1]
```

The answer feels obvious. A computer still needs a procedure.

## First attempt: compare one feature

Weight alone can find a crocodile that weighs the same as a tiger. Add speed and another unrelated animal may still match. Every omitted property is a place for a false conclusion to hide.

## Second attempt: keep every difference

Comparing Tiger A with Tiger B gives:

```text
weight:  5
speed:   1
age:    -1
```

This is accurate, but it is not a decision. With a thousand attributes we receive a thousand answers. We need one measure of separation.

## Your derivation

You proposed the entire path yourself:

> Find the difference of similar features. If it is negative, that is wrong for distance, so square the differences, add them, and take the root.

Why not simply add? Because opposite differences cancel. A change of `100` and `-100` would produce zero, falsely declaring two objects identical.

Why square? Every changed coordinate becomes positive, and a large disagreement contributes more strongly than a small one.

Why add? We need every feature to contribute to one answer.

Why take the root? The direct line across a space is not the sum of its side lengths. A move of 3 in one direction and 4 in another forms a right triangle whose direct separation is 5. The root returns us from squared separation to ordinary distance.

Only after the reasoning is complete does the notation help:

## Why Every Term Must Exist Before the Equation

- **x and y** are the two objects being compared; **xᵢ and yᵢ** are the same feature in each.
- **xᵢ−yᵢ** records disagreement feature by feature.
- Squaring prevents opposite disagreements from cancelling and makes large mismatches matter more.
- Summing lets every retained feature contribute one answer.
- The square root returns squared separation to the original distance scale.
- **d(x,y)** names the single separation the king asked for.

Only now can we compress that reasoning:

$$
d(\mathbf{x},\mathbf{y})
=\sqrt{(x_1-y_1)^2+(x_2-y_2)^2+\cdots+(x_n-y_n)^2}
$$


The formula is your procedure written compactly.

## A limit we must remember

If weight is measured in kilograms and a stripe flag is only zero or one, weight can dominate. Distance treats coordinate scales as meaningful. Representation and normalization therefore matter as much as arithmetic.

Distance also answers **similarity**, not every kind of relationship. That distinction will become decisive when we reach attention.

## Challenge

Construct two pairs of two-dimensional points whose signed differences add to zero even though neither pair is identical. Then explain why squaring prevents the mistake.

## What the next excavation needs

So far a vector has described where an object is in feature space. But an arrow can also describe how something changes. That second meaning will lead us toward transformations.

[Next: Vectors as Change](../004-vectors-as-change/README.md)
