# Excavation 210 — Partial Derivatives and Gradients — One Landscape, Many Directions

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->



Limits make ‘arbitrarily small’ precise. A loss surface has not one input but millions, and moving stripe sensitivity while freezing weight sensitivity answers a different question from moving both together.

The vault of Partial Derivatives and Gradients opens onto a problem a ranger, builder, or machine could encounter without knowing any modern terminology.

The tiger alarm has two dials: stripe weight w₁ and size weight w₂. Its local loss is a hillside over the floor. The ranger can nudge east, north, or diagonally and observe different changes.

The chamber has reduced the abstraction to one physical thing: **a compass resting on a many-dimensional hillside**. The question carved beside it asks: *If every weight can move, which combined direction changes the loss fastest?*

The old machinery invites a plausible shortcut: compute one ordinary derivative as if the entire parameter vector were a single undifferentiated number.

The stone does not object with terminology; it objects with a result we already know cannot be right. The answer cannot say which dial caused which part of the change or which physical direction rises fastest. Different paths through the same point produce different slopes.

```text
scene → guess → calculate → compare with reality
          ▲                       │
          └──── change the idea ──┘
                       ↓
                     Partial Derivatives and Gradients
```

We do not leap to a famous formula. We carry one missing responsibility forward: hold every other dial fixed to measure one partial derivative at a time, then gather those coordinate sensitivities into the gradient vector.

The failure and repair now form one continuous argument for Partial Derivatives and Gradients: this idea earns its place by preserving exactly what the earlier action lost.

## The calculation hidden inside partial derivatives and gradients

The symbols for partial derivatives and gradients will compress the same concrete case without replacing it. The objects and actions remain visible while their repeated responsibilities receive shorter names.

### Testing Partial Derivatives and Gradients against the named case

Near the current setting, nudging w₁ by 0.01 raises loss by about 0.03, giving sensitivity 3. Nudging w₂ by 0.01 lowers loss by about 0.01, giving sensitivity -1. The gradient `[3,-1]` points toward fastest local increase; its negative points toward fastest local decrease under ordinary Euclidean distance.

### Naming what is already on the table

**L** is the loss landscape and **w₁,…,wₙ** its adjustable coordinates. **∂L/∂wᵢ** asks what L does when only wᵢ moves infinitesimally. **∇L** stores every such answer in coordinate order.

### Why the melody needs these exact notes

[Partial derivatives](../../MATHEMATICAL_MOVES.md#partial-derivative) isolate one coordinate while others are fixed. [Concatenation](../../MATHEMATICAL_MOVES.md#concatenation) preserves the separate sensitivities as one ordered vector. Summing them would erase direction and could let positive and negative effects cancel.

Every operation required by partial derivatives and gradients now has a visible job in the named case, so the complete construction can be written compactly:

$$
\nabla L(\mathbf w)=\left[\frac{\partial L}{\partial w_1},\ldots,\frac{\partial L}{\partial w_n}\right]
$$

## A real-world echo

At a mountain pass, ‘the slope’ is incomplete until you say which way you face. The gradient is the compass arrow assembled from every coordinate-facing slope.

## What this unlocks elsewhere

Gradient descent, backpropagation, Adam, clipping, and attribution all use this object. Earlier chapters used it operationally; this excavation reveals why its components must remain ordered.

## Where the promise of partial derivatives and gradients breaks

A gradient describes one scalar output. A layer often maps many inputs to many outputs, so one vector cannot preserve every input-output sensitivity.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Partial Derivatives and Gradients tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 211: Jacobians — When Many Outputs Change Together](../211-jacobians/README.md)
