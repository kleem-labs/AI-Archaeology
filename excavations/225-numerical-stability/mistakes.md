# Mistakes Worth Preserving — Excavation 225

## The tempting idea

We tried to evaluate the written formula literally and assume algebraic equivalence guarantees computational equivalence.

## The evidence that refused it

finite arithmetic has ceilings, floors, and rounding. Overflow turns meaningful ratios into `∞/∞`; subtracting nearly equal large numbers can discard the very digits carrying their difference.

## What the wreckage taught us

The next construction had to rewrite the calculation so intermediate values remain in a safe range while the exact mathematical result stays unchanged.

Keep this wrong idea. It is the negative space around Numerical Stability: it records why the accepted method has exactly the responsibilities it does.
