# Excavation 210 — Partial Derivatives and Gradients — One Landscape, Many Directions

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Calculus & Differential Change](../../MATHEMATICS_ATLAS.md#calculus) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Mathematical roots beneath the machine

Limits make ‘arbitrarily small’ precise. A loss surface has not one input but millions, and moving stripe sensitivity while freezing weight sensitivity answers a different question from moving both together.

Another vault door opens. The carving that once named **Partial Derivatives and Gradients** has weathered away, which is useful: we must recover the idea from what a ranger, builder, or machine can actually observe.

The tiger alarm has two dials: stripe weight w₁ and size weight w₂. Its local loss is a hillside over the floor. The ranger can nudge east, north, or diagonally and observe different changes.

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

This is the hinge of the Partial Derivatives and Gradients excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

## Partial Derivatives and Gradients on the stone workbench

Near the current setting, nudging w₁ by 0.01 raises loss by about 0.03, giving sensitivity 3. Nudging w₂ by 0.01 lowers loss by about 0.01, giving sensitivity -1. The gradient `[3,-1]` points toward fastest local increase; its negative points toward fastest local decrease under ordinary Euclidean distance.

The point of keeping the objects named while rebuilding Partial Derivatives and Gradients is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

## The calculation hidden inside partial derivatives and gradients

Return to the named Partial Derivatives and Gradients scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

### Naming what is already on the table

**L** is the loss landscape and **w₁,…,wₙ** its adjustable coordinates. **∂L/∂wᵢ** asks what L does when only wᵢ moves infinitesimally. **∇L** stores every such answer in coordinate order.

### Why the melody needs these exact notes

[Partial derivatives](../../MATHEMATICAL_MOVES.md#partial-derivative) isolate one coordinate while others are fixed. [Concatenation](../../MATHEMATICAL_MOVES.md#concatenation) preserves the separate sensitivities as one ordered vector. Summing them would erase direction and could let positive and negative effects cancel.

The operations inside Partial Derivatives and Gradients form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
\nabla L(\mathbf w)=\left[\frac{\partial L}{\partial w_1},\ldots,\frac{\partial L}{\partial w_n}\right]
$$

Read the Partial Derivatives and Gradients line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

## A real-world echo

At a mountain pass, ‘the slope’ is incomplete until you say which way you face. The gradient is the compass arrow assembled from every coordinate-facing slope.

That echo helps Partial Derivatives and Gradients remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

## What this chamber was connected to

Gradient descent, backpropagation, Adam, clipping, and attribution all use this object. Earlier chapters used it operationally; this excavation reveals why its components must remain ordered.

The older excavation and this Partial Derivatives and Gradients chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

## Where the promise of partial derivatives and gradients breaks

A gradient describes one scalar output. A layer often maps many inputs to many outputs, so one vector cannot preserve every input-output sensitivity.

The boundary belongs beside the discovery of Partial Derivatives and Gradients because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Partial Derivatives and Gradients tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 211: Jacobians — When Many Outputs Change Together](../211-jacobians/README.md)
