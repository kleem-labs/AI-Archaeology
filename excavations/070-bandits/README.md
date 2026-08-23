# Excavation 070 — Bandits — Learning While Choosing

<!-- book-prose-v2 -->

Controlled experiments isolate causal effects by holding alternatives steady. In a live recommender, withholding every uncertain choice until a long experiment ends sacrifices opportunities to learn while serving users.

We can postpone invention if we simply always choose the currently best option.

If the proposal works on every relevant case, bandits is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The decisive test is this: an unlucky first result permanently hides a better alternative.

Nothing magical creates bandits. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: reserve some choices for exploration while exploiting accumulated evidence.

This boundary between the failed rule and its repair is the subject later work calls **Bandits**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize bandits; try to break it by subtraction. Remove the part that knows how to reserve some choices for exploration while exploiting accumulated evidence, leaving only the attempt to always choose the currently best option. What returns is not a vague weakness but the original contradiction: an unlucky first result permanently hides a better alternative. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to always choose the currently best option receives the same test as the rule to reserve some choices for exploration while exploiting accumulated evidence. Their different outcomes reveal what bandits contributes without asking the reader to trust historical convention.

## Learning While Choosing

Cafe A wins its first two trials; continuing to sample B reveals it succeeds eight out of ten times.

Hold the setting, evidence, and desired outcome fixed while testing bandits. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

## Where bandits runs out

Exploration has real cost and can be unacceptable for high-risk actions.

This is where bandits runs out for a causal reason. We gave it enough structure to reserve some choices for exploration while exploiting accumulated evidence, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

## Take bandits to the workbench

A mathematical story about bandits earns trust only when the failed and repaired paths can both be reproduced. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running bandits, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the bandits result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 071](../071-features-inside-networks/README.md)
