# Excavation 207 — Orthogonality and Projection — Finding the Closest Shadow

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->



Eigenvectors expose directions preserved by a transformation. The vault now presents a simpler geometric failure: an observed arrow does not lie on the one-dimensional rail our model is allowed to use.

The stair toward Orthogonality and Projection opens into an older workshop, where the machine's abstraction returns to ordinary objects and human decisions.

A tiger track points `[3,2]`, but the ranger's simplified map retains only the eastward rail `[1,0]`. We need the point on that rail that misrepresents the track as little as possible.

The chamber has reduced the abstraction to one physical thing: **a lantern, a tiger track, and one polished rail**. The question carved beside it asks: *What is the closest honest shadow of this track on the only rail our map allows?*

The first move is honest because it uses the nearest tool already in our hands: **copy whichever coordinate looks largest or slide to an arbitrary point on the allowed rail**.

The proposal deserves a real trial, not a ceremonial rejection. The chosen point changes when coordinates are renamed and gives no proof that another allowed point is not closer. The discarded error may still point partly along the rail, revealing that more of the track could have been retained.

```text
known tool ──tempts us──▶ first attempt
                              │
                         concrete failure
                              │
                              ▼
                    missing responsibility
                              │
                              ▼
                           Orthogonality and Projection
```

The failed case reveals the missing requirement: we must choose the shadow whose leftover error is perpendicular to the allowed direction, because then no further movement along the rail can reduce the distance.

The failure and repair now form one continuous argument for Orthogonality and Projection: this idea earns its place by preserving exactly what the earlier action lost.

## The calculation hidden inside orthogonality and projection

The symbols for orthogonality and projection will compress the same concrete case without replacing it. The objects and actions remain visible while their repeated responsibilities receive shorter names.

### Testing Orthogonality and Projection against the named case

Project `[3,2]` onto east `[1,0]`. Their dot product is 3; east's dot product with itself is 1; the required scale is therefore 3. The shadow is `[3,0]`, leaving error `[0,2]`. That error has zero dot product with east, so every remaining disagreement points outside the allowed rail.

### Naming what is already on the table

**v** is the observed track and **u** the allowed direction. **v·u** measures alignment; **u·u** measures u's squared length. Their ratio finds how much u fits inside v. Multiplying u by that ratio constructs the shadow.

### Why the melody needs these exact notes

[The dot product](../../MATHEMATICAL_MOVES.md#dot-product) measures directional agreement. [Division](../../MATHEMATICAL_MOVES.md#division) removes dependence on the chosen length of u, and [multiplication](../../MATHEMATICAL_MOVES.md#multiplication) rebuilds the shadow in the allowed direction. Using raw v·u alone would change the answer if the same rail were described by a longer basis arrow.

Every operation required by orthogonality and projection now has a visible job in the named case, so the complete construction can be written compactly:

$$
\mathrm{proj}_{\mathbf u}(\mathbf v)=\frac{\mathbf v\cdot\mathbf u}{\mathbf u\cdot\mathbf u}\mathbf u
$$

## A real-world echo

A sundial's shadow is not the object, but under a fixed light it is the closest information the ground plane can retain.

## What this unlocks elsewhere

Linear probes project hidden states onto readable directions; least squares projects observations into a model subspace; attention projects embeddings into query, key, and value spaces.

## Where the promise of orthogonality and projection breaks

Projection handles one chosen subspace, but it does not discover which subspace matters. For an arbitrary rectangular matrix, we still need paired input and output directions that preserve most of its action.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Orthogonality and Projection tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 208: Singular Value Decomposition — The Important Directions of Any Matrix](../208-singular-value-decomposition/README.md)
