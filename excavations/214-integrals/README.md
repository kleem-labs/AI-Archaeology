# Excavation 214 — Integrals — Reconstructing a Whole from Infinitesimal Pieces

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->



Taylor approximation reconstructs a function near one point. The factory's meters report rates—tokens per second, energy per second, water flow per minute—but the final account needs a total across time.

The Integrals chamber continues the same investigation. What looked complete in the previous room now meets a situation it cannot preserve.

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

The failure and repair now form one continuous argument for Integrals: this idea earns its place by preserving exactly what the earlier action lost.

## The calculation hidden inside integrals

The symbols for integrals will compress the same concrete case without replacing it. The objects and actions remain visible while their repeated responsibilities receive shorter names.

### Testing Integrals against the named case

Over four one-minute intervals the measured rates are 1, 2, 3, and 4 litres per minute. Rectangles give `1×1 + 2×1 + 3×1 + 4×1 = 10` litres. Halving the interval uses more, thinner rectangles and follows the changing flow more closely. The integral is the value these sums approach as no interval remains visibly wide.

### Naming what is already on the table

**[a,b]** is the time interval. **Δtᵢ** is one slice width and **r(tᵢ)** its sampled rate. Their product is a small amount, not a rate. Summation combines slice amounts; the limit removes dependence on a coarse partition. The integral sign names the accumulated whole.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) converts rate times duration into amount. [Summation](../../MATHEMATICAL_MOVES.md#summation) joins disjoint amounts; multiplication among slices would make one zero-flow moment erase all water. [The limit](../../MATHEMATICAL_MOVES.md#limit) forces the partition error arbitrarily small.

Every operation required by integrals now has a visible job in the named case, so the complete construction can be written compactly:

$$
\int_a^b r(t)dt=\lim_{\max\Delta t_i\to0}\sum_i r(t_i)\Delta t_i
$$

## A real-world echo

A mosaic becomes an image because each tiny tile contributes colour to a place; making the tiles finer reveals the curve rather than changing the scene.

## What this unlocks elsewhere

Expected values are integrals over possible outcomes, Neural ODEs integrate hidden-state change, and continuous-time signals become discrete computations through numerical quadrature.

## Where the promise of integrals breaks

Accumulation tells how much signal exists but can hide the simple repeating components inside it. Audio waves that look tangled in time may become sparse when described by frequency.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Integrals tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 215: Fourier Analysis — Hearing Frequencies Hidden Inside Time](../215-fourier-analysis/README.md)
