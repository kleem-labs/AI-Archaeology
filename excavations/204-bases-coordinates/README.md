# Excavation 204 — Bases and Coordinates — The Same Object in Another Language

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

### Realm 2 — The Chamber of Directions

The brass function opens a many-sided room. Rulers rotate in the walls, arrows cross the floor, and a high window turns every object into a shadow.

Listen for sliding rulers, turning stone, and distant bells. The questions in this realm travel as one chain:

```text
language of space → new directions → persistent directions → honest shadows → strongest channels
```



Functions turn inputs into dependable outputs. Our vector functions seem to operate directly on lists of coordinates, yet rotating the ruler changes every coordinate while leaving the animal's physical displacement untouched.

The vault of Bases and Coordinates opens onto a problem a ranger, builder, or machine could encounter without knowing any modern terminology.

A ranger walks three steps east and two north. On the square floor this is recorded as `[3,2]`. Another ranger carries diagonal rulers: one points northeast, the other northwest. The same walk must acquire different numbers in that language.

The chamber has reduced the abstraction to one physical thing: **two rotating ruler frames laid over one footprint**. The question carved beside it asks: *When the coordinate numbers change, what stayed the same?*

The old machinery invites a plausible shortcut: treat the coordinate list as the vector itself and conclude that changing the list changes the underlying displacement.

The stone does not object with terminology; it objects with a result we already know cannot be right. The east-north list `[3,2]` and its diagonal-coordinate list disagree numerically even though both return the ranger to the same physical endpoint. Coordinates depend on the chosen measuring directions.

```text
scene → guess → calculate → compare with reality
          ▲                       │
          └──── change the idea ──┘
                       ↓
                     Bases and Coordinates
```

We do not leap to a famous formula. We carry one missing responsibility forward: choose a set of basis directions and define coordinates as the amounts of those directions whose combination reconstructs the vector.

The failure and repair now form one continuous argument for Bases and Coordinates: this idea earns its place by preserving exactly what the earlier action lost.

## The calculation hidden inside bases and coordinates

The symbols for bases and coordinates will compress the same concrete case without replacing it. The objects and actions remain visible while their repeated responsibilities receive shorter names.

### Testing Bases and Coordinates against the named case

With basis arrows east `[1,0]` and north `[0,1]`, the walk is `3 east + 2 north`. If the new basis uses northeast `[1,1]` and northwest `[-1,1]`, then `2.5 northeast - 0.5 northwest` reconstructs `[3,2]`. The coefficients changed; the endpoint did not.

### Naming what is already on the table

**v** is the displacement being described. **b₁,…,bₙ** are the chosen basis directions. **c₁,…,cₙ** are coordinates in that basis. Multiplying a basis direction by its coordinate stretches or reverses it; adding the contributions reconstructs v.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) scales each basis direction by the amount required. [Addition](../../MATHEMATICAL_MOVES.md#addition) joins independent directional contributions. Concatenating the numbers would merely store them side by side and would not reconstruct the displacement.

Every operation required by bases and coordinates now has a visible job in the named case, so the complete construction can be written compactly:

$$
\mathbf v=c_1\mathbf b_1+c_2\mathbf b_2+\cdots+c_n\mathbf b_n
$$

## A real-world echo

The same melody can be written for piano or violin. The marks change because the instrument's basis changes; the melody's relationships survive.

## What this unlocks elsewhere

Embeddings choose learned coordinates, attention projects them into query and key bases, and RoPE rotates coordinate pairs. A representation is always a choice of mathematical language.

## Where the promise of bases and coordinates breaks

A collection of candidate basis directions may contain redundancy or fail to reach part of the space. We need to know which directions are genuinely new and what region their combinations can cover.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Bases and Coordinates tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 205: Span and Linear Independence — Which Directions Are Truly New?](../205-span-linear-independence/README.md)
