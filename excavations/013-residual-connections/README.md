# Excavation 013 — Residual Connections

## The Problem: Depth Can Destroy the Message

Suppose a useful representation must pass through 50 transformation blocks. If every block replaces it entirely, even a mediocre early transformation can erase information that later blocks need. Learning an identity mapping—“leave this alone”—should be easy, yet a complicated block may struggle to reproduce its input exactly.

## Failed Attempt: Trust Every Layer to Preserve Everything

We could demand that each transformation $F$ learn both what to preserve and what to change. This burdens every layer with copying the entire representation while making a small improvement. During backpropagation, gradients must also pass through every transformation, where repeated multiplication can shrink or explode them.

## The Invention: Learn the Change

Keep the input and add the block's proposal:

$$
\mathbf{y}=\mathbf{x}+F(\mathbf{x})
$$

The direct path is the **residual connection** or skip connection. $F$ no longer needs to recreate the whole output. It learns the residual—the change from input to desired output.

## Worked Example

Let `x = [10, 5, -2]` and let a block propose `F(x) = [0.5, -1, 0]`. Then:

$$y=[10.5,4,-2]$$

Most information survives while the block edits selected features. If the best action is no change, setting $F(x)=0$ immediately gives the identity.

## Why Gradients Benefit

For scalar intuition:

$$
\frac{dy}{dx}=1+\frac{dF}{dx}
$$

The derivative contains a direct `1` path. Even if the learned branch has a small derivative, a gradient can still flow backward through the skip route. This does not guarantee perfect training, but it greatly improves deep optimization.

## Shape Is a Contract

Addition requires $F(x)$ and $x$ to have the same shape. Transformer attention and FFN sublayers therefore return to the model width before residual addition. If widths differ, a projection must align them.

## Code Walkthrough

`implementation.py` applies a small transformation and adds its output back to the input. It also stacks several residual updates. Compare this with repeatedly replacing the state using only `F(x)`.

## Common Misconceptions

**“A residual connection skips computation.”** The learned branch still runs; the skip preserves an alternate information and gradient route.

**“Residual means the change must be small.”** It can be large, though training often benefits from learning refinements.

**“Skip connections solve every depth problem.”** Initialization, normalization, optimization, and architecture still matter.

## The New Problem

Residual streams repeatedly accumulate contributions. Their scales can drift, and different examples can produce wildly different activation magnitudes. We need controlled numerical conditions without erasing learned structure.

---

Previous: [012 — Feed-Forward Networks](../012-feed-forward-networks/README.md) · Next: [014 — Layer Normalization](../014-layer-normalization/README.md)
