# Excavation 213 — Taylor Approximation — Borrowing a Function’s Local Shape

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Calculus & Differential Change](../../MATHEMATICS_ATLAS.md#calculus) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Mathematical roots beneath the machine

> **You are here:** Realm 3 of 5 — [The River of Change](../../MATHEMATICAL_ROOTS.md#realm-3)
>
> **Question waiting in this chamber:** How much nearby terrain can be rebuilt from clues gathered at one point?
>
> **Do not take the answer yet:** first let the object fail.

The Hessian reveals local bending. Re-evaluating a complicated model for every nearby possibility remains costly, and a slope alone fails as soon as curvature matters.

The stair below the completed AI factory does not descend into abstraction. It opens into the Undercroft of First Principles, where the familiar word **Taylor Approximation** has been covered so that only the unsolved situation remains.

The ranger knows a signal's value, slope, and curvature at dial setting a. A nearby setting a+h must be estimated before the expensive full detector can run.

The chamber has reduced the abstraction to one physical thing: **a torn map, a tangent ruler, and nested pieces of curved parchment**. The question carved beside it asks: *How much nearby terrain can be rebuilt from clues gathered at one point?*

The first move is honest because it uses the nearest tool already in our hands: **extend the tangent line indefinitely and assume constant slope everywhere**.

The proposal deserves a real trial, not a ceremonial rejection. For a curved signal the linear prediction drifts, and doubling h can more than double the error. The tangent remembers direction but forgets that the direction itself changes.

```text
known tool ──tempts us──▶ first attempt
                              │
                         concrete failure
                              │
                              ▼
                    missing responsibility
                              │
                              ▼
                           Taylor Approximation
```

Now the reader can name the requirement before the textbook can name the method: we must build a local polynomial: start with the known value, add slope times displacement, then add curvature times squared displacement with the counting factor required by repeated differentiation.

This is the hinge of the Taylor Approximation excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

## When the chamber changes

Hold the failed picture still for one breath: The straight tangent predicts well for one step, then walks directly away from the bending road.

Now let the scene move. Begin with the current height, add the slope's straight correction, then add curvature and finer corrections only as distance makes them necessary.

The transformation is the discovery of Taylor Approximation made visible. Nothing has been defined by authority; this particular room changed because the old action could not preserve what mattered. Only after seeing that change do we press Taylor Approximation into memory:

> **Memory seal — Taylor Approximation**
>
> A Taylor approximation rebuilds nearby shape from value, slope, curvature, and finer local clues.

Make the memory bodily, not merely verbal: Lay one flat hand as a tangent, then gradually bend the other around it.

## Taylor Approximation on the stone workbench

Use `f(x)=eˣ` near zero. Its value, slope, and curvature at zero are all 1. At h=0.1, the second-order estimate is `1 + 0.1 + 0.1²/2 = 1.105`, close to the true 1.10517. Removing the squared term gives 1.1 and visibly loses curvature.

The point of keeping the objects named while rebuilding Taylor Approximation is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

## The calculation hidden inside taylor approximation

Return to the named Taylor Approximation scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

### Naming what is already on the table

**a** is the known location and **h** the nearby displacement. **f(a)** anchors the estimate. **f′(a)h** carries local slope through the displacement. **f″(a)h²/2** repairs the first curvature error. The approximation sign admits omitted higher-order terms.

### Why the melody needs these exact notes

[Addition](../../MATHEMATICAL_MOVES.md#addition) lets distinct orders contribute without erasing one another. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) makes each derivative act through its displacement, while [powers](../../MATHEMATICAL_MOVES.md#powers) make curvature shrink faster than slope as h becomes tiny. Multiplying all terms together would make any zero term erase the approximation.

The operations inside Taylor Approximation form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
f(a+h)\approx f(a)+f'(a)h+\frac{f''(a)}{2}h^2
$$

Read the Taylor Approximation line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

## A real-world echo

A sculptor reconstructs the nearby curve from how the stone faces now, how its direction changes, and how quickly that change itself bends.

That echo helps Taylor Approximation remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

## What this chamber was connected to

Gradient descent trusts the first-order term; Newton methods use the second; neural tangent analyses study regimes where the local linear picture remains informative.

The older excavation and this Taylor Approximation chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

Before leaving The River of Change, look back at its path—**approach → local change → coupled change → bending → nearby prediction → accumulation → hidden rhythm**. Taylor Approximation occupies one necessary step in that motion. Its object, **a torn map, a tangent ruler, and nested pieces of curved parchment**, stays in the room so that the equation can later be recovered from an image rather than recalled as an orphaned line.

## Where the promise of taylor approximation breaks

Taylor pieces describe local behavior. To recover total water, distance, probability, or change across a whole interval, many small contributions must be accumulated rather than inspected near one point.

The boundary belongs beside the discovery of Taylor Approximation because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Taylor Approximation tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 214: Integrals — Reconstructing a Whole from Infinitesimal Pieces](../214-integrals/README.md)
