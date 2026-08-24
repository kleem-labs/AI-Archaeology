# Excavation 225 — Numerical Stability — Preserving Mathematics Inside a Finite Machine

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

> **You are here:** Realm 5 of 5 — [The Garden of Futures](../../MATHEMATICAL_ROOTS.md#realm-5)
>
> **Question waiting in this chamber:** How can a finite machine travel to the same mathematical truth without overflowing on the way?
>
> **Do not take the answer yet:** first let the object fail.

Convexity can make an exact mathematical landscape trustworthy. The machine that evaluates it has finite memory and finite precision, so an algebraically correct formula can still overflow, underflow, or erase a small but important difference.

The stair below the completed AI factory does not descend into abstraction. It opens into the Undercroft of First Principles, where the familiar word **Numerical Stability** has been covered so that only the unsolved situation remains.

Three logits are 1000, 999, and 998. Their exponentials should have sensible relative sizes, yet an ordinary floating-point calculator cannot store `e¹⁰⁰⁰`; the first operation becomes infinity before normalization can rescue it.

The chamber has reduced the abstraction to one physical thing: **a small brass instrument facing three unbearably bright exponential flames**. The question carved beside it asks: *How can a finite machine travel to the same mathematical truth without overflowing on the way?*

The first move is honest because it uses the nearest tool already in our hands: **evaluate the written formula literally and assume algebraic equivalence guarantees computational equivalence**.

The proposal deserves a real trial, not a ceremonial rejection. Finite arithmetic has ceilings, floors, and rounding. Overflow turns meaningful ratios into `∞/∞`; subtracting nearly equal large numbers can discard the very digits carrying their difference.

```text
known tool ──tempts us──▶ first attempt
                              │
                         concrete failure
                              │
                              ▼
                    missing responsibility
                              │
                              ▼
                           Numerical Stability
```

Now the reader can name the requirement before the textbook can name the method: we must rewrite the calculation so intermediate values remain in a safe range while the exact mathematical result stays unchanged.

This is the hinge of the Numerical Stability excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

## When the chamber changes

Hold the failed picture still for one breath: The first flame becomes infinity before the machine can compare it with the others; a meaningful ratio collapses into infinity divided by infinity.

Now let the scene move. Transpose every score by the largest one. The flames shrink into the instrument's range while their relative brightness remains unchanged; restore the removed scale only at the end.

The transformation is the discovery of Numerical Stability made visible. Nothing has been defined by authority; this particular room changed because the old action could not preserve what mattered. Only after seeing that change do we press Numerical Stability into memory:

> **Memory seal — Numerical Stability**
>
> Numerical stability is a safer computational path to the same mathematical truth.

Make the memory bodily, not merely verbal: Lower both hands together without changing the distance between them, then raise the shared scale at the end.

## Numerical Stability on the stone workbench

Let m be the largest logit, 1000. Subtract it first, producing `[0,-1,-2]`. Their exponentials are now `[1,e⁻¹,e⁻²]`, all representable. Because factoring out `eᵐ` from the original sum contributes m after the logarithm, the stable result is `1000 + log(1+e⁻¹+e⁻²)`—the same real number reached by a safer path.

The point of keeping the objects named while rebuilding Numerical Stability is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

## The calculation hidden inside numerical stability

Return to the named Numerical Stability scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

### Naming what is already on the table

**xᵢ** are the original scores. **m** is their maximum. **xᵢ-m** shifts every score without changing exponential ratios. The inner sum combines safe positive contributions. The outer logarithm returns from exponential scale, and adding m restores the factored scale.

### Why the melody needs these exact notes

[Maximum](../../MATHEMATICAL_MOVES.md#maximum) chooses a shift that makes every exponent nonpositive. [Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) creates that safe range. [The exponential](../../MATHEMATICAL_MOVES.md#exponential) recovers relative positive weights, [summation](../../MATHEMATICAL_MOVES.md#summation) combines alternatives, and [the logarithm](../../MATHEMATICAL_MOVES.md#logarithm) returns to log scale. Clipping would avoid overflow by changing the answer; this rearrangement preserves it.

The operations inside Numerical Stability form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
\log\sum_i e^{x_i}=m+\log\sum_i e^{x_i-m},\quad m=\max_i x_i
$$

Read the Numerical Stability line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

## A real-world echo

A priceless melody can be played on a small instrument only if it is transposed into the instrument's range. The relationships survive although the absolute register temporarily changes.

That echo helps Numerical Stability remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

## What this chamber was connected to

Stable softmax, log-likelihoods, mixed precision, gradient scaling, normalization, and online attention all distinguish a mathematical identity from a safe computational route.

The older excavation and this Numerical Stability chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

Before leaving The Garden of Futures, look back at its path—**sufficient present → remembered futures → trustworthy landscape → safe computation**. Numerical Stability occupies one necessary step in that motion. Its object, **a small brass instrument facing three unbearably bright exponential flames**, stays in the room so that the equation can later be recovered from an image rather than recalled as an orphaned line.

## Where the promise of numerical stability breaks

Stability cannot restore information already lost to poor data, an ill-conditioned problem, or insufficient precision. It asks a final engineering question: which equivalent path preserves the mathematical meaning on the machine we actually possess?

The boundary belongs beside the discovery of Numerical Stability because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Numerical Stability tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Return to the living Math Mandala](../../math-mandala/README.md), where every recovered idea remains connected to the chapters that needed it.

## The stair returns to daylight

The final carving is not an answer but a habit. We began with an observation, risked an idea of our own, listened when a small case broke it, and invented only the operation needed to preserve what had vanished. Symbols arrived as nicknames for things our hands and imagination already knew.

That rhythm now runs through the whole archive—from counting tigers to making models accountable. The mandala is not a wall of formulas to memorize. It is a map of human necessities. Touch any node and ask: *What failed so completely that someone had to invent this?* The mathematics will no longer feel borrowed. It will remember the path by which it became yours.
