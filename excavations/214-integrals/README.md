# Excavation 214 — Integrals — Reconstructing a Whole from Infinitesimal Pieces

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Calculus & Differential Change](../../MATHEMATICS_ATLAS.md#calculus) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

> **You are here:** Realm 3 of 5 — [The River of Change](../../MATHEMATICAL_ROOTS.md#realm-3)
>
> **Question waiting in this chamber:** How can a changing rate become the total water actually delivered?
>
> **Do not take the answer yet:** first let the object fail.

Taylor approximation reconstructs a function near one point. The factory's meters report rates—tokens per second, energy per second, water flow per minute—but the final account needs a total across time.

In the next chamber of the Undercroft, the mathematical archaeologist removes the label from **Integrals**. A name would let us recognize the answer too early; the stone workbench gives us only a stubborn observation.

A rescue tank fills at a changing rate r(t). The ranger reads the rate at many moments but wants the total water delivered between dawn a and dusk b.

The chamber has reduced the abstraction to one physical thing: **a river gauge and thousands of increasingly thin glass cups**. The question carved beside it asks: *How can a changing rate become the total water actually delivered?*

Nothing yet suggests a new invention. We naturally multiply one chosen rate by the entire duration.

For a moment the shortcut feels complete. Then the smallest contrary case arrives. The flow is slow at dawn and fast at noon, so one sample grants every moment the wrong rate. Taking more samples helps, but their contributions need a rule that survives as slices become thinner.

```text
observation
    ↓
our own proposal ──▶ test case ──▶ impossible answer
                                      ↓
                              preserve what vanished
                                      ↓
                                    Integrals
```

What survives the failure is a precise demand. The repaired construction must divide time into small intervals, multiply each interval's width by a representative rate, add the resulting little volumes, and take the limit as the widest interval shrinks toward zero.

This is the hinge of the Integrals excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

## When the chamber changes

Hold the failed picture still for one breath: One noon reading is multiplied across the whole day, granting dawn and dusk a rate they never had.

Now let the scene move. Let each tiny interval fill its own cup at its own rate, add the cups, and make them thinner until coarse partition error disappears.

The transformation is the discovery of Integrals made visible. Nothing has been defined by authority; this particular room changed because the old action could not preserve what mattered. Only after seeing that change do we press Integrals into memory:

> **Memory seal — Integrals**
>
> An integral rebuilds a whole by accumulating locally honest pieces.

Make the memory bodily, not merely verbal: Cup both hands repeatedly, then gather the imagined pieces into one vessel.

## Integrals on the stone workbench

Over four one-minute intervals the measured rates are 1, 2, 3, and 4 litres per minute. Rectangles give `1×1 + 2×1 + 3×1 + 4×1 = 10` litres. Halving the interval uses more, thinner rectangles and follows the changing flow more closely. The integral is the value these sums approach as no interval remains visibly wide.

The point of keeping the objects named while rebuilding Integrals is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

## The calculation hidden inside integrals

Return to the named Integrals scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

### Naming what is already on the table

**[a,b]** is the time interval. **Δtᵢ** is one slice width and **r(tᵢ)** its sampled rate. Their product is a small amount, not a rate. Summation combines slice amounts; the limit removes dependence on a coarse partition. The integral sign names the accumulated whole.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) converts rate times duration into amount. [Summation](../../MATHEMATICAL_MOVES.md#summation) joins disjoint amounts; multiplication among slices would make one zero-flow moment erase all water. [The limit](../../MATHEMATICAL_MOVES.md#limit) forces the partition error arbitrarily small.

The operations inside Integrals form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
\int_a^b r(t)dt=\lim_{\max\Delta t_i\to0}\sum_i r(t_i)\Delta t_i
$$

Read the Integrals line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

## A real-world echo

A mosaic becomes an image because each tiny tile contributes colour to a place; making the tiles finer reveals the curve rather than changing the scene.

That echo helps Integrals remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

## What this chamber was connected to

Expected values are integrals over possible outcomes, Neural ODEs integrate hidden-state change, and continuous-time signals become discrete computations through numerical quadrature.

The older excavation and this Integrals chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

Before leaving The River of Change, look back at its path—**approach → local change → coupled change → bending → nearby prediction → accumulation → hidden rhythm**. Integrals occupies one necessary step in that motion. Its object, **a river gauge and thousands of increasingly thin glass cups**, stays in the room so that the equation can later be recovered from an image rather than recalled as an orphaned line.

## Where the promise of integrals breaks

Accumulation tells how much signal exists but can hide the simple repeating components inside it. Audio waves that look tangled in time may become sparse when described by frequency.

The boundary belongs beside the discovery of Integrals because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Integrals tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 215: Fourier Analysis — Hearing Frequencies Hidden Inside Time](../215-fourier-analysis/README.md)
