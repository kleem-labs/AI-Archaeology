# Excavation 207 — Orthogonality and Projection — Finding the Closest Shadow

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

> **You are here:** Realm 2 of 5 — [The Chamber of Directions](../../MATHEMATICAL_ROOTS.md#realm-2)
>
> **Question waiting in this chamber:** What is the closest honest shadow of this track on the only rail our map allows?
>
> **Do not take the answer yet:** first let the object fail.

Eigenvectors expose directions preserved by a transformation. The vault now presents a simpler geometric failure: an observed arrow does not lie on the one-dimensional rail our model is allowed to use.

The stair below the completed AI factory does not descend into abstraction. It opens into the Undercroft of First Principles, where the familiar word **Orthogonality and Projection** has been covered so that only the unsolved situation remains.

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

Now the reader can name the requirement before the textbook can name the method: we must choose the shadow whose leftover error is perpendicular to the allowed direction, because then no further movement along the rail can reduce the distance.

This is the hinge of the Orthogonality and Projection excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

## When the chamber changes

Hold the failed picture still for one breath: An arbitrary shadow leaves an error that still runs partly along the rail, proving that some allowed information was unnecessarily discarded.

Now let the scene move. Slide the shadow until the leftover error stands exactly perpendicular to the rail. No further allowed slide can make the disagreement smaller.

The transformation is the discovery of Orthogonality and Projection made visible. Nothing has been defined by authority; this particular room changed because the old action could not preserve what mattered. Only after seeing that change do we press Orthogonality and Projection into memory:

> **Memory seal — Orthogonality and Projection**
>
> Projection is the closest honest shadow an allowed space can keep.

Make the memory bodily, not merely verbal: Drop one hand straight onto an imagined tabletop, forming a right angle with the discarded height.

## Orthogonality and Projection on the stone workbench

Project `[3,2]` onto east `[1,0]`. Their dot product is 3; east's dot product with itself is 1; the required scale is therefore 3. The shadow is `[3,0]`, leaving error `[0,2]`. That error has zero dot product with east, so every remaining disagreement points outside the allowed rail.

The point of keeping the objects named while rebuilding Orthogonality and Projection is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

## The calculation hidden inside orthogonality and projection

Return to the named Orthogonality and Projection scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

### Naming what is already on the table

**v** is the observed track and **u** the allowed direction. **v·u** measures alignment; **u·u** measures u's squared length. Their ratio finds how much u fits inside v. Multiplying u by that ratio constructs the shadow.

### Why the melody needs these exact notes

[The dot product](../../MATHEMATICAL_MOVES.md#dot-product) measures directional agreement. [Division](../../MATHEMATICAL_MOVES.md#division) removes dependence on the chosen length of u, and [multiplication](../../MATHEMATICAL_MOVES.md#multiplication) rebuilds the shadow in the allowed direction. Using raw v·u alone would change the answer if the same rail were described by a longer basis arrow.

The operations inside Orthogonality and Projection form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
\mathrm{proj}_{\mathbf u}(\mathbf v)=\frac{\mathbf v\cdot\mathbf u}{\mathbf u\cdot\mathbf u}\mathbf u
$$

Read the Orthogonality and Projection line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

## A real-world echo

A sundial's shadow is not the object, but under a fixed light it is the closest information the ground plane can retain.

That echo helps Orthogonality and Projection remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

## What this chamber was connected to

Linear probes project hidden states onto readable directions; least squares projects observations into a model subspace; attention projects embeddings into query, key, and value spaces.

The older excavation and this Orthogonality and Projection chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

Before leaving The Chamber of Directions, look back at its path—**language of space → new directions → persistent directions → honest shadows → strongest channels**. Orthogonality and Projection occupies one necessary step in that motion. Its object, **a lantern, a tiger track, and one polished rail**, stays in the room so that the equation can later be recovered from an image rather than recalled as an orphaned line.

## Where the promise of orthogonality and projection breaks

Projection handles one chosen subspace. For an arbitrary rectangular matrix, we still need to discover the paired input and output directions that carry most of its action.

The boundary belongs beside the discovery of Orthogonality and Projection because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Orthogonality and Projection tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 208: Singular Value Decomposition — The Important Directions of Any Matrix](../208-singular-value-decomposition/README.md)
