# Excavation 224 — Convexity — A Landscape Without Hidden Valleys

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

> **You are here:** Realm 5 of 5 — [The Garden of Futures](../../MATHEMATICAL_ROOTS.md#realm-5)
>
> **Question waiting in this chamber:** When can a nearby valley be trusted as the lowest valley anywhere?
>
> **Do not take the answer yet:** first let the object fail.

Dynamic programming replaces repeated futures with stored values, but learning those values or fitting a model still asks an optimizer to descend a landscape. Some landscapes conceal many valleys; others make every local descent globally trustworthy.

At this depth, mathematics feels less like a catalogue and more like memory. We meet **Convexity** first as an ordinary human need, before anyone has decided what marks should record it.

Stretch a string between two points on a bowl. Everywhere between the endpoints, the string floats on or above the bowl. Try the same across a rippled cave floor and the string can cut below a hill.

The chamber has reduced the abstraction to one physical thing: **a taut golden string stretched above a single clay bowl**. The question carved beside it asks: *When can a nearby valley be trusted as the lowest valley anywhere?*

We try to spend no new mathematics at all and simply trust any small local minimum as the best possible solution.

The test is deliberately small enough to follow by hand, so the failure cannot hide inside complexity. On a rippled landscape, a nearby valley may be higher than another valley beyond a ridge. Local slope alone cannot certify that no better point exists elsewhere.

```text
no symbols yet
      ↓
one named example
      ↓
a rule we would naturally try
      ↓
the case that refuses it
      ↓
Convexity becomes necessary
```

At last there is something worth inventing. Whatever we build must require every chord between two points to lie on or above the function, preventing a hidden hump from separating a local minimum from a lower global one.

This is the hinge of the Convexity excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

## When the chamber changes

Hold the failed picture still for one breath: On a rippled floor, the traveler settles in a shallow pocket while a deeper valley hides beyond a ridge.

Now let the scene move. Stretch the string between any two points. If the landscape always remains below its chord, no hidden ridge can protect a better local valley.

The transformation is the discovery of Convexity made visible. Nothing has been defined by authority; this particular room changed because the old action could not preserve what mattered. Only after seeing that change do we press Convexity into memory:

> **Memory seal — Convexity**
>
> Convexity is the promise that a landscape contains no secret lower valley.

Make the memory bodily, not merely verbal: Curve one palm into a bowl and stretch one finger of the other hand across it like a chord.

## Convexity on the stone workbench

For the bowl `f(x)=x²`, choose x=-2, y=2, and λ=1/2. Their midpoint is 0, where the bowl has height 0. The midpoint of endpoint heights is `(4+4)/2=4`; the bowl lies below its chord. Repeating this test for every pair and mixture weight is the geometric promise of convexity.

The point of keeping the objects named while rebuilding Convexity is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

## The calculation hidden inside convexity

Return to the named Convexity scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

### Naming what is already on the table

**x** and **y** are any two candidate points. **λ** lies between 0 and 1 and chooses a point along their segment. The left side evaluates the function at the mixed input. The right side mixes the two endpoint heights. The inequality demands that the function never rise above that chord.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) allocates complementary shares λ and 1-λ. [Addition](../../MATHEMATICAL_MOVES.md#addition) forms the mixtures. [Inequalities](../../MATHEMATICAL_MOVES.md#inequalities) compare the curved surface with its straight chord. Equality alone would describe only affine functions and exclude genuine bowls.

The operations inside Convexity form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
f(\lambda x+(1-\lambda)y)\leq\lambda f(x)+(1-\lambda)f(y),\quad 0\leq\lambda\leq1
$$

Read the Convexity line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

## A real-world echo

A valley shaped like a single bowl may be steep or shallow, but it contains no secret lower chamber behind a ridge.

That echo helps Convexity remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

## What this chamber was connected to

Linear regression losses, logistic objectives, support-vector machines, and regularizers expose why some optimization guarantees are possible. Deep neural networks are generally nonconvex, so their success requires more delicate geometry.

The older excavation and this Convexity chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

Before leaving The Garden of Futures, look back at its path—**sufficient present → remembered futures → trustworthy landscape → safe computation**. Convexity occupies one necessary step in that motion. Its object, **a taut golden string stretched above a single clay bowl**, stays in the room so that the equation can later be recovered from an image rather than recalled as an orphaned line.

## Where the promise of convexity breaks

Convexity is a powerful global promise, not a description of every useful model. It does not choose a stable numerical representation, prevent overflow, or make finite-precision arithmetic exact.

The boundary belongs beside the discovery of Convexity because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Convexity tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 225: Numerical Stability — Preserving Mathematics Inside a Finite Machine](../225-numerical-stability/README.md)
