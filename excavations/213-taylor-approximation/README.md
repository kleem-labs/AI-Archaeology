# Excavation 213 — Taylor Approximation — Borrowing a Function’s Local Shape

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->



The Hessian reveals local bending. Re-evaluating a complicated model for every nearby possibility remains costly, and a slope alone fails as soon as curvature matters.

The stair toward Taylor Approximation opens into an older workshop, where the machine's abstraction returns to ordinary objects and human decisions.

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

The failed case reveals the missing requirement: we must build a local polynomial: start with the known value, add slope times displacement, then add curvature times squared displacement with the counting factor required by repeated differentiation.

The failure and repair now form one continuous argument for Taylor Approximation: this idea earns its place by preserving exactly what the earlier action lost.

## The calculation hidden inside taylor approximation

The symbols for taylor approximation will compress the same concrete case without replacing it. The objects and actions remain visible while their repeated responsibilities receive shorter names.

### Testing Taylor Approximation against the named case

Use `f(x)=eˣ` near zero. Its value, slope, and curvature at zero are all 1. At h=0.1, the second-order estimate is `1 + 0.1 + 0.1²/2 = 1.105`, close to the true 1.10517. Removing the squared term gives 1.1 and visibly loses curvature.

### Naming what is already on the table

**a** is the known location and **h** the nearby displacement. **f(a)** anchors the estimate. **f′(a)h** carries local slope through the displacement. **f″(a)h²/2** repairs the first curvature error. The approximation sign admits omitted higher-order terms.

### Why the melody needs these exact notes

[Addition](../../MATHEMATICAL_MOVES.md#addition) lets distinct orders contribute without erasing one another. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) makes each derivative act through its displacement, while [powers](../../MATHEMATICAL_MOVES.md#powers) make curvature shrink faster than slope as h becomes tiny. Multiplying all terms together would make any zero term erase the approximation.

Every operation required by taylor approximation now has a visible job in the named case, so the complete construction can be written compactly:

$$
f(a+h)\approx f(a)+f'(a)h+\frac{f''(a)}{2}h^2
$$

## A real-world echo

A sculptor reconstructs the nearby curve from how the stone faces now, how its direction changes, and how quickly that change itself bends.

## What this unlocks elsewhere

Gradient descent trusts the first-order term; Newton methods use the second; neural tangent analyses study regimes where the local linear picture remains informative.

## Where the promise of taylor approximation breaks

Taylor pieces describe local behavior. To recover total water, distance, probability, or change across a whole interval, many small contributions must be accumulated rather than inspected near one point.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Taylor Approximation tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 214: Integrals — Reconstructing a Whole from Infinitesimal Pieces](../214-integrals/README.md)
