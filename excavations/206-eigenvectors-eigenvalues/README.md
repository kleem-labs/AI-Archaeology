# Excavation 206 — Eigenvectors and Eigenvalues — Directions a Transformation Cannot Turn

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics)
>
> **Applied territory:** Mathematical roots beneath the machine

Span and independence reveal the true directions available in a space. When one matrix is applied again and again—one transition, message-passing step, or layer after another—the coordinate picture can still become difficult to follow.

At this depth, mathematics feels less like a catalogue and more like memory. We meet **Eigenvectors and Eigenvalues** first as an ordinary human need, before anyone has decided what marks should record it.

On the vault floor, a transformation doubles east-west displacement but leaves north-south displacement unchanged. Most arrows change both length and direction. An arrow pointing exactly east does something quieter: it remains east and only stretches.

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

This is the hinge of the Eigenvectors and Eigenvalues excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

## Eigenvectors and Eigenvalues on the stone workbench

Apply the matrix `[[2,0],[0,1]]` to east `[1,0]`: the result is `[2,0]`, exactly twice east. Apply it to north `[0,1]`: the result remains north. East has scale 2 and north scale 1. Apply it repeatedly and any arrow with an east component becomes increasingly east-dominated.

The point of keeping the objects named while rebuilding Eigenvectors and Eigenvalues is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

## The calculation hidden inside eigenvectors and eigenvalues

Return to the named Eigenvectors and Eigenvalues scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

### Naming what is already on the table

**A** is the transformation. **v** is a nonzero direction. **λ** is the scalar stretch, shrinkage, or sign reversal. Equality says transforming v and merely scaling v reach the same arrow, so direction is preserved.

### Why the melody needs these exact notes

[Function application](../../MATHEMATICAL_MOVES.md#function-application) applies the transformation to the direction. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) scales that same direction, and [equality](../../MATHEMATICAL_MOVES.md#equals) demands the two routes coincide. Adding λ would translate the arrow rather than describe proportional stretching.

The operations inside Eigenvectors and Eigenvalues form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
A\mathbf v=\lambda\mathbf v
$$

Read the Eigenvectors and Eigenvalues line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

## A real-world echo

In a river, most leaves swirl, but a leaf placed on the main current keeps pointing downstream while its distance from the bridge changes predictably.

That echo helps Eigenvectors and Eigenvalues remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

## What this chamber was connected to

PageRank studies a persistent direction of repeated link transitions; covariance eigenvectors become principal directions; training stability depends on repeated transformations' spectral behavior.

The older excavation and this Eigenvectors and Eigenvalues chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

## Where the promise of eigenvectors and eigenvalues breaks

Not every matrix has enough real eigenvectors to form a basis, and rectangular matrices do not even map a space back into itself. We still need a way to cast the closest shadow and expose the important input-output directions of any matrix.

The boundary belongs beside the discovery of Eigenvectors and Eigenvalues because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Eigenvectors and Eigenvalues tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 207: Orthogonality and Projection — Finding the Closest Shadow](../207-orthogonality-projection/README.md)
