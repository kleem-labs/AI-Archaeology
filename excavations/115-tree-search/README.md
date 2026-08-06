# Excavation 115 — Tree Search

[Previous: Excavation 114](../114-model-based-planning/README.md)

## Take the First Step Yourself

> **Your problem:** Exploring every future action sequence becomes impossible.

> **Try your first idea:** Expand every branch equally.

> **Now try to break your idea:** Most computation is wasted on obviously poor branches.

> Stop here. State the missing requirement without naming the repair.

## The Observation

Exploring every future action sequence becomes impossible.

## Your First Attempt

Expand every branch equally.

## Break Your First Attempt

Most computation is wasted on obviously poor branches.

## Repair Your Attempt

Balance exploring uncertain branches with deepening promising ones, then propagate outcomes backward.

## What You Have Just Invented

**Balance exploring uncertain branches with deepening promising ones, then propagate outcomes backward.**

## Rebuild the Discovery with a Concrete Case

A game search revisits a move that won often while still testing a less explored alternative.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Build Every Piece from the Concrete Example

- The average reward records how well one branch has performed.
- Visit count shrinks the exploration bonus as evidence accumulates.
- Total visits increase pressure to reconsider neglected branches.
- The constant controls how much uncertainty competes with known reward.

Only now can we compress the procedure:

$$
\operatorname{score}(a)=\overline R_a+c\sqrt{\frac{\log N}{n_a}}
$$

## Real-World Limit

Search quality depends on simulations and evaluation estimates.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 116](../116-reasoning-and-verification/README.md)
