# Excavation 004 — Vectors as Change

## The Problem

A vector can describe where something is. But how do we describe movement, growth, or the transformation from one state into another?

## The Invention

Suppose an object moves from position $\mathbf{a}$ to $\mathbf{b}$. Subtract the starting point:

$$\Delta = \mathbf{b} - \mathbf{a}$$

The resulting vector is a displacement: a reusable instruction for change. Adding it to the starting point recovers the destination:

$$\mathbf{a} + \Delta = \mathbf{b}$$

## More Than Motion

The same idea works in any feature space. The difference between a small house and a larger one might encode “add a bedroom and 30 square meters.” The difference between two word representations can sometimes capture a meaningful relationship.

## Direction and Magnitude

A change vector contains two ideas:

- **Direction** tells us the kind of change.
- **Magnitude** tells us how much change occurred.

Scaling a vector changes its magnitude. Adding vectors composes changes. These simple operations will later let neural networks build and combine representations.

## The New Problem

Applying one carefully chosen change is useful. Applying a coordinated collection of changes to every dimension would be far more powerful. We need a machine for transforming vectors.

---

Previous: [003 — Distance](../003-distance/README.md) · Next: [005 — Matrices](../005-matrices/README.md)
