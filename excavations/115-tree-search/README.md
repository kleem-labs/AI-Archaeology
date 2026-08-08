# Excavation 115 — Tree Search

[Previous: Excavation 114](../114-model-based-planning/README.md)

Exploring every future action sequence becomes impossible.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Expand every branch equally.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Most computation is wasted on obviously poor branches.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Balance exploring uncertain branches with deepening promising ones, then propagate outcomes backward.

Only after that reasoning may we give your discovery its inherited name.

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
\operatorname{score}(a)=\overline R_a+c\sqrt{\frac{\log N}{n_a}}
$$

## Where your new idea still breaks

Search quality depends on simulations and evaluation estimates.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 116](../116-reasoning-and-verification/README.md)
