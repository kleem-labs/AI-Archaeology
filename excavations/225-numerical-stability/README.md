# Excavation 225 — Numerical Stability — Preserving Mathematics Inside a Finite Machine

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->



Convexity can make an exact mathematical landscape trustworthy. The machine that evaluates it has finite memory and finite precision, so an algebraically correct formula can still overflow, underflow, or erase a small but important difference.

The stair toward Numerical Stability opens into an older workshop, where the machine's abstraction returns to ordinary objects and human decisions.

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

The failed case reveals the missing requirement: we must rewrite the calculation so intermediate values remain in a safe range while the exact mathematical result stays unchanged.

The failure and repair now form one continuous argument for Numerical Stability: this idea earns its place by preserving exactly what the earlier action lost.

## The calculation hidden inside numerical stability

The symbols for numerical stability will compress the same concrete case without replacing it. The objects and actions remain visible while their repeated responsibilities receive shorter names.

### Testing Numerical Stability against the named case

Let m be the largest logit, 1000. Subtract it first, producing `[0,-1,-2]`. Their exponentials are now `[1,e⁻¹,e⁻²]`, all representable. Because factoring out `eᵐ` from the original sum contributes m after the logarithm, the stable result is `1000 + log(1+e⁻¹+e⁻²)`—the same real number reached by a safer path.

### Naming what is already on the table

**xᵢ** are the original scores. **m** is their maximum. **xᵢ-m** shifts every score without changing exponential ratios. The inner sum combines safe positive contributions. The outer logarithm returns from exponential scale, and adding m restores the factored scale.

### Why the melody needs these exact notes

[Maximum](../../MATHEMATICAL_MOVES.md#maximum) chooses a shift that makes every exponent nonpositive. [Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) creates that safe range. [The exponential](../../MATHEMATICAL_MOVES.md#exponential) recovers relative positive weights, [summation](../../MATHEMATICAL_MOVES.md#summation) combines alternatives, and [the logarithm](../../MATHEMATICAL_MOVES.md#logarithm) returns to log scale. Clipping would avoid overflow by changing the answer; this rearrangement preserves it.

Every operation required by numerical stability now has a visible job in the named case, so the complete construction can be written compactly:

$$
\log\sum_i e^{x_i}=m+\log\sum_i e^{x_i-m},\quad m=\max_i x_i
$$

## A real-world echo

A priceless melody can be played on a small instrument only if it is transposed into the instrument's range. The relationships survive although the absolute register temporarily changes.

## What this unlocks elsewhere

Stable softmax, log-likelihoods, mixed precision, gradient scaling, normalization, and online attention all distinguish a mathematical identity from a safe computational route.

## Where the promise of numerical stability breaks

Stability cannot restore information already lost to poor data, an ill-conditioned problem, or insufficient precision. It asks a final engineering question: which equivalent path preserves the mathematical meaning on the machine we actually possess?

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Numerical Stability tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Return to the living Math Mandala](../../math-mandala/README.md), where every recovered idea remains connected to the chapters that needed it.

## The stair returns to daylight

The final carving is not an answer but a habit. We began with an observation, risked an idea of our own, listened when a small case broke it, and invented only the operation needed to preserve what had vanished. Symbols arrived as nicknames for things our hands and imagination already knew.

That rhythm now runs through the whole archive—from counting tigers to making models accountable. The mandala is not a wall of formulas to memorize. It is a map of human necessities. Touch any node and ask: *What failed so completely that someone had to invent this?* The mathematics will no longer feel borrowed. It will remember the path by which it became yours.
