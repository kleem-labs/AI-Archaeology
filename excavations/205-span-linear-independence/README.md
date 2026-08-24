# Excavation 205 — Span and Linear Independence — Which Directions Are Truly New?

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

A basis gives coordinates meaning only if its directions reach the required space without secretly repeating one another. Adding more arrows to the table can create the appearance of capacity while contributing no new possible movement.

Far below the Transformer, the Undercroft stores no formula sheet. For **Span and Linear Independence**, it preserves a scene, a tempting tool, and the mark left where that tool broke.

The cartographer offers east `[1,0]`, north `[0,1]`, and northeast `[1,1]` as three foundational directions on a two-dimensional map. The third feels useful, but the first two can already reconstruct it.

With no standard method to recite, the most economical proposal is to count every stored direction as a new dimension and assign each one an independent coordinate.

A useful wrong idea is one that leaves a clean fossil of its missing responsibility. Northeast equals east plus north, so the same displacement receives many coefficient lists. The coordinate system can no longer tell which explanation is unique, and parameter count exaggerates true capacity.

```text
what we kept       what disappeared
     │                     │
     └──── first attempt ──┘
               │
          failure mark
               │
       one necessary repair
               │
             Span and Linear Independence
```

The next idea is forced only because the evidence asks us to call the reachable collection of combinations the span, and call directions independent only when no nontrivial weighted combination collapses to zero.

This is the hinge of the Span and Linear Independence excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

## Span and Linear Independence on the stone workbench

Ask whether `a·east + b·north + c·northeast` can return to `[0,0]` without all weights being zero. Choosing `a=-1`, `b=-1`, and `c=1` does exactly that. Northeast therefore adds no new reachable point. East and north alone span the entire floor and give each displacement one coordinate pair.

The point of keeping the objects named while rebuilding Span and Linear Independence is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

## The calculation hidden inside span and linear independence

Return to the named Span and Linear Independence scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

### Naming what is already on the table

**span(v₁,…,vₖ)** is every vector obtainable by scaling and adding the listed directions. **aᵢ** are proposed weights. The zero vector represents no movement. If the only weights producing zero are all zero, no direction can be reconstructed from the others.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) scales candidate directions and [summation](../../MATHEMATICAL_MOVES.md#summation) combines them. [Equality](../../MATHEMATICAL_MOVES.md#equals) asks whether the combination collapses to zero. Merely counting vectors cannot detect that one is already contained in the others' span.

The operations inside Span and Linear Independence form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
a_1\mathbf v_1+\cdots+a_k\mathbf v_k=\mathbf0\Longrightarrow a_1=\cdots=a_k=0
$$

Read the Span and Linear Independence line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

## A real-world echo

Three keys on a ring do not open three doors when one key is only a copy. Independence counts new access, not metal objects.

That echo helps Span and Linear Independence remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

## What this chamber was connected to

Superposition asks how many useful feature directions share a space; LoRA asks how many update directions are actually needed. Rank and independence make those capacity claims precise.

The older excavation and this Span and Linear Independence chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

## Where the promise of span and linear independence breaks

Independence tells which directions are new but not how a transformation repeatedly stretches the space. Some directions persist under repeated application while others turn and mix.

The boundary belongs beside the discovery of Span and Linear Independence because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Span and Linear Independence tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 206: Eigenvectors and Eigenvalues — Directions a Transformation Cannot Turn](../206-eigenvectors-eigenvalues/README.md)
