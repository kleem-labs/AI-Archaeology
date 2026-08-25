# Excavation 205 — Span and Linear Independence — Which Directions Are Truly New?

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->



A basis gives coordinates meaning only if its directions reach the required space without secretly repeating one another. Adding more arrows to the table can create the appearance of capacity while contributing no new possible movement.

Far below the Transformer, Span and Linear Independence begins with an ordinary situation and a tool that almost—but not quite—solves it.

The cartographer offers east `[1,0]`, north `[0,1]`, and northeast `[1,1]` as three foundational directions on a two-dimensional map. The third feels useful, but the first two can already reconstruct it.

The chamber has reduced the abstraction to one physical thing: **three floor arrows and a ring carrying one copied key**. The question carved beside it asks: *Does this new arrow open genuinely new movement, or only rename movement already possible?*

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

The failure and repair now form one continuous argument for Span and Linear Independence: this idea earns its place by preserving exactly what the earlier action lost.

## The calculation hidden inside span and linear independence

The symbols for span and linear independence will compress the same concrete case without replacing it. The objects and actions remain visible while their repeated responsibilities receive shorter names.

### Testing Span and Linear Independence against the named case

Ask whether `a·east + b·north + c·northeast` can return to `[0,0]` without all weights being zero. Choosing `a=-1`, `b=-1`, and `c=1` does exactly that. Northeast therefore adds no new reachable point. East and north alone span the entire floor and give each displacement one coordinate pair.

### Naming what is already on the table

**span(v₁,…,vₖ)** is every vector obtainable by scaling and adding the listed directions. **aᵢ** are proposed weights. The zero vector represents no movement. If the only weights producing zero are all zero, no direction can be reconstructed from the others.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) scales candidate directions and [summation](../../MATHEMATICAL_MOVES.md#summation) combines them. [Equality](../../MATHEMATICAL_MOVES.md#equals) asks whether the combination collapses to zero. Merely counting vectors cannot detect that one is already contained in the others' span.

Every operation required by span and linear independence now has a visible job in the named case, so the complete construction can be written compactly:

$$
a_1\mathbf v_1+\cdots+a_k\mathbf v_k=\mathbf0\Longrightarrow a_1=\cdots=a_k=0
$$

## A real-world echo

Three keys on a ring do not open three doors when one key is only a copy. Independence counts new access, not metal objects.

## What this unlocks elsewhere

Superposition asks how many useful feature directions share a space; LoRA asks how many update directions are actually needed. Rank and independence make those capacity claims precise.

## Where the promise of span and linear independence breaks

Independence tells which directions are new but not how a transformation repeatedly stretches the space. Some directions persist under repeated application while others turn and mix.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Span and Linear Independence tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 206: Eigenvectors and Eigenvalues — Directions a Transformation Cannot Turn](../206-eigenvectors-eigenvalues/README.md)
