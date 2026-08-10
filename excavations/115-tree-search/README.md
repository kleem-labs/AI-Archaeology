# Excavation 115 — Tree Search

[Previous: Excavation 114](../114-model-based-planning/README.md)

Exploring every future action sequence becomes impossible.

The first solution that suggests itself is this: Expand every branch equally.

The idea survives only until we test it against reality: Most computation is wasted on obviously poor branches.

The failure gives us a precise requirement: Balance exploring uncertain branches with deepening promising ones, then propagate outcomes backward.

## Now work a case you can see

A game search revisits a move that won often while still testing a less explored alternative.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Build each piece from what just happened

- The average reward records how well one branch has performed.
- Visit count shrinks the exploration bonus as evidence accumulates.
- Total visits increase pressure to reconsider neglected branches.
- The constant controls how much uncertainty competes with known reward.

Only now can we compress the procedure:

$$
\mathrm{score}(a)=\overline R_a+c\sqrt{\frac{\log N}{n_a}}
$$

## Where your new idea still breaks

Search quality depends on simulations and evaluation estimates.

The boundary follows from the mechanism itself. We designed it to Balance exploring uncertain branches with deepening promising ones, then propagate outcomes backward. That operation solves the failure we had reached, but it contains no step that answers the additional problem above.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 116](../116-reasoning-and-verification/README.md)
