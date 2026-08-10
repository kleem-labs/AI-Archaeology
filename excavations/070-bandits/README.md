# Excavation 070 — Bandits — Learning While Choosing

[Previous: Excavation 069](../069-controlled-experiments/README.md)

An agent must choose recommendations while still learning which are useful.

The first solution that suggests itself is this: Always choose the currently best option.

The idea survives only until we test it against reality: An unlucky first result permanently hides a better alternative.

The failure gives us a precise requirement: Reserve some choices for exploration while exploiting accumulated evidence.

## Now work a case you can see

Cafe A wins its first two trials; continuing to sample B reveals it succeeds eight out of ten times.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

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
