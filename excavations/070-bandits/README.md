# Excavation 070 — Bandits — Learning While Choosing

Controlled experiments isolate causal effects by holding alternatives steady. In a live recommender, withholding every uncertain choice until a long experiment ends sacrifices opportunities to learn while serving users.

Using what we have, we always choose the currently best option.

But an unlucky first result permanently hides a better alternative.

So we reserve some choices for exploration while exploiting accumulated evidence.

## Let the case decide

Cafe A wins its first two trials; continuing to sample B reveals it succeeds eight out of ten times.

## The boundary of the discovery

Exploration has real cost and can be unacceptable for high-risk actions.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 071](../071-features-inside-networks/README.md)
