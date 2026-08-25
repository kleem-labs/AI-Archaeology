# Excavation 224 — Convexity — A Landscape Without Hidden Valleys

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->



Dynamic programming replaces repeated futures with stored values, but learning those values or fitting a model still asks an optimizer to descend a landscape. Some landscapes conceal many valleys; others make every local descent globally trustworthy.

At this depth, Convexity begins as a need inside the world rather than as a name outside it.

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

The failure and repair now form one continuous argument for Convexity: this idea earns its place by preserving exactly what the earlier action lost.

## The calculation hidden inside convexity

The symbols for convexity will compress the same concrete case without replacing it. The objects and actions remain visible while their repeated responsibilities receive shorter names.

### Testing Convexity against the named case

For the bowl `f(x)=x²`, choose x=-2, y=2, and λ=1/2. Their midpoint is 0, where the bowl has height 0. The midpoint of endpoint heights is `(4+4)/2=4`; the bowl lies below its chord. Repeating this test for every pair and mixture weight is the geometric promise of convexity.

### Naming what is already on the table

**x** and **y** are any two candidate points. **λ** lies between 0 and 1 and chooses a point along their segment. The left side evaluates the function at the mixed input. The right side mixes the two endpoint heights. The inequality demands that the function never rise above that chord.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) allocates complementary shares λ and 1-λ. [Addition](../../MATHEMATICAL_MOVES.md#addition) forms the mixtures. [Inequalities](../../MATHEMATICAL_MOVES.md#inequalities) compare the curved surface with its straight chord. Equality alone would describe only affine functions and exclude genuine bowls.

Every operation required by convexity now has a visible job in the named case, so the complete construction can be written compactly:

$$
f(\lambda x+(1-\lambda)y)\leq\lambda f(x)+(1-\lambda)f(y),\quad 0\leq\lambda\leq1
$$

## A real-world echo

A valley shaped like a single bowl may be steep or shallow, but it contains no secret lower chamber behind a ridge.

## What this unlocks elsewhere

Linear regression losses, logistic objectives, support-vector machines, and regularizers expose why some optimization guarantees are possible. Deep neural networks are generally nonconvex, so their success requires more delicate geometry.

## Where the promise of convexity breaks

Convexity is a powerful global promise, not a description of every useful model. It does not choose a stable numerical representation, prevent overflow, or make finite-precision arithmetic exact.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Convexity tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 225: Numerical Stability — Preserving Mathematics Inside a Finite Machine](../225-numerical-stability/README.md)
