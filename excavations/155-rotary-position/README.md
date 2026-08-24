# Excavation 155 — Rotary Position Embeddings — Let Distance Enter the Match

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

Packed training supplies dense sequences, but the learned absolute position cards from our first GPT bind each slot to a private identity rather than making relative displacement part of the query-key match.

Night gathers around the Engine Cavern. Under the light of the brass reference machine, the enginewright refuses to invent prematurely and begins with the plain rule: learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples.

At the edge of the brass reference machine, the shortcut produces its consequence: moving the same phrase from positions 10–12 to 110–112 changes every position vector although the internal distances are unchanged. That consequence, not a textbook, earns the next move.

*The enginewright sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: learn an unrelated vector for every…
possible road B ─┘              └── loses: moving the same phrase from positions…

same roads ──▶ repaired map ──▶ rotate pairs of query and key…
```

The enginewright covers the new mark and the old contradiction returns: moving the same phrase from positions 10–12 to 110–112 changes every position vector although the internal distances are unchanged. The cover is lifted, restoring the ability to rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason rotary position embeddings exists.

What must change for rotary position embeddings is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference. That threshold is where **Rotary Position Embeddings** enters the story.

The marks on the brass reference machine form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. rotary position embeddings is not any single point. It is the path connecting them in the only order that makes the last point necessary.

<!-- memory-film-v1:start -->
> **Memory realm 12 of 18 — [Engine Cavern](../../MEMORY_PALACE.md#realm-12)**
>
> **The question carried into this chamber:** What fails if we learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples?

## When the chamber changes

The Rotary Position Embeddings room does not ask you to memorize its name. It asks you to watch one object change.

First hold the failed picture still: The wheel follows the tempting path—learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples. Then the evidence answers: moving the same phrase from positions 10–12 to 110–112 changes every position vector although the internal distances are unchanged.

Now let the chamber move: The enginewright changes one moving part. The wheel can now rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference.

The object that should remain after the terminology disappears is **the rotary position embeddings wheel mounted on the brass reference machine**.

> **Memory seal — Rotary Position Embeddings**
>
> Rotary Position Embeddings keeps the missing power: rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference.

Give the idea a bodily path: Touch the rotary position embeddings wheel in imagination: close one fist around the lost information, then open it as the repair restores that information.
<!-- memory-film-v1:end -->

## Let Distance Enter the Match

Rotate the two coordinates of tiger by angle mθ and river by nθ. Their match depends on (m−n)θ, so shifting both tokens together preserves their separation signal.

## The calculation hidden inside rotary position embeddings

The enginewright carries the rotary position embeddings scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Imagine the pair of coordinates as a clock hand beginning at [1,0]. At position one, a quarter-turn sends it to [0,1]; at position two, another quarter-turn sends it to [−1,0]. The hand's length never changes—only its angle does. Multiplying position p by the chosen turn theta tells us the total angle; the four cosine-and-sine entries record how any starting pair must contribute to its two rotated coordinates.

p is token position, theta is one rotation frequency, and R rotates one coordinate pair without changing its length.

### Why the melody needs these exact notes

[Function application](../../MATHEMATICAL_MOVES.md#function-application) applies the same rotation rule at each position. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) mixes the two coordinates according to cosine and sine; [addition](../../MATHEMATICAL_MOVES.md#addition) combines their signed contributions. Squaring or adding p would change magnitude instead of encoding position as an angle whose differences survive a shared shift.

The symbols are about to change costume, but their work has appeared before: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the joining river**—separate contributions meet without losing where they came from. This is how distant excavations begin to sound like variations of one melody.

The brass reference machine already contains the complete rotary position embeddings mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
R(p\theta)=\begin{bmatrix}\cos(p\theta)&-\sin(p\theta)\\\sin(p\theta)&\cos(p\theta)\end{bmatrix}
$$

## Where rotary position embeddings runs out

RoPE supplies structured relative position, but distances far beyond training still produce unfamiliar phases.

Here the new path ends honestly. Rotary Position Embeddings can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the brass reference machine

Rebuild the rotary position embeddings scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Relative Position Bias — What Should Happen Beyond the Seen Window?](../156-relative-position-bias/README.md)
