# Excavation 206 — Eigenvectors and Eigenvalues — Directions a Transformation Cannot Turn

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->



Span and independence reveal the true directions available in a space. When one matrix is applied again and again—one transition, message-passing step, or layer after another—the coordinate picture can still become difficult to follow.

At this depth, Eigenvectors and Eigenvalues begins as a need inside the world rather than as a name outside it.

On the vault floor, a transformation doubles east-west displacement but leaves north-south displacement unchanged. Most arrows change both length and direction. An arrow pointing exactly east does something quieter: it remains east and only stretches.

The chamber has reduced the abstraction to one physical thing: **a moving stone floor crossed by compass arrows**. The question carved beside it asks: *Which direction can pass through the transformation without being turned?*

We try to spend no new mathematics at all and simply track every coordinate of every repeatedly transformed arrow and hope the long-term pattern becomes obvious.

The test is deliberately small enough to follow by hand, so the failure cannot hide inside complexity. Coordinate expressions grow while the persistent behavior stays hidden. Two initial arrows can look unrelated even when repeated transformation eventually makes both align with the same dominant direction.

```text
no symbols yet
      ↓
one named example
      ↓
a rule we would naturally try
      ↓
the case that refuses it
      ↓
Eigenvectors and Eigenvalues becomes necessary
```

At last there is something worth inventing. Whatever we build must search for nonzero directions that the transformation only scales, and record the corresponding scale factors.

The failure and repair now form one continuous argument for Eigenvectors and Eigenvalues: this idea earns its place by preserving exactly what the earlier action lost.

## The calculation hidden inside eigenvectors and eigenvalues

The symbols for eigenvectors and eigenvalues will compress the same concrete case without replacing it. The objects and actions remain visible while their repeated responsibilities receive shorter names.

### Testing Eigenvectors and Eigenvalues against the named case

Apply the matrix `[[2,0],[0,1]]` to east `[1,0]`: the result is `[2,0]`, exactly twice east. Apply it to north `[0,1]`: the result remains north. East has scale 2 and north scale 1. Apply it repeatedly and any arrow with an east component becomes increasingly east-dominated.

### Naming what is already on the table

**A** is the transformation. **v** is a nonzero direction. **λ** is the scalar stretch, shrinkage, or sign reversal. Equality says transforming v and merely scaling v reach the same arrow, so direction is preserved.

### Why the melody needs these exact notes

[Function application](../../MATHEMATICAL_MOVES.md#function-application) applies the transformation to the direction. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) scales that same direction, and [equality](../../MATHEMATICAL_MOVES.md#equals) demands the two routes coincide. Adding λ would translate the arrow rather than describe proportional stretching.

Every operation required by eigenvectors and eigenvalues now has a visible job in the named case, so the complete construction can be written compactly:

$$
A\mathbf v=\lambda\mathbf v
$$

## A real-world echo

In a river, most leaves swirl, but a leaf placed on the main current keeps pointing downstream while its distance from the bridge changes predictably.

## What this unlocks elsewhere

PageRank studies a persistent direction of repeated link transitions; covariance eigenvectors become principal directions; training stability depends on repeated transformations' spectral behavior.

## Where the promise of eigenvectors and eigenvalues breaks

Not every matrix has enough real eigenvectors to form a basis, and rectangular matrices do not even map a space back into itself. We still need a way to cast the closest shadow and expose the important input-output directions of any matrix.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Eigenvectors and Eigenvalues tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 207: Orthogonality and Projection — Finding the Closest Shadow](../207-orthogonality-projection/README.md)
