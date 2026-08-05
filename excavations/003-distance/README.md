# Excavation 003 — Distance

## The Problem

Vectors place observations in feature space. To find similar objects, we need to measure how far apart two points are.

## First Attempt: Count Different Features

Counting positions that differ treats one kilogram like one hundred kilograms. It ignores magnitude.

## Rediscovering Euclidean Distance

For two features, coordinate differences form a right triangle. Its diagonal is:

$$d(\mathbf{x}, \mathbf{y}) = \sqrt{\sum_i (x_i-y_i)^2}$$

Subtract each feature, square to remove signs, add the contributions, and take the square root.

## Distance Encodes Judgment

Euclidean distance is not automatically correct. Manhattan distance adds absolute differences. Weighted distance makes some features more important. Cosine similarity compares direction instead of magnitude.

Choosing a distance means choosing what “similar” means.

## The Scale Trap

If mass varies by hundreds and stripes by one, mass dominates. Normalization and feature weights are part of the model, not mere housekeeping.

## The New Problem

Subtracting two vectors describes how one point must change to become another. That difference deserves attention of its own.

---

Previous: [002 — Vectors](../002-vectors/README.md) · Next: [004 — Vectors as Change](../004-vectors-as-change/README.md)
