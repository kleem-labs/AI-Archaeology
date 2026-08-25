# Excavation 070 — Bandits — Learning While Choosing

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Learning in the world and interpretability

Controlled experiments isolate causal effects by holding alternatives steady. In a live recommender, withholding every uncertain choice until a long experiment ends sacrifices opportunities to learn while serving users.

A new case arrives at the Living Watchgarden. Nothing yet demands a new invention, so the field naturalist uses the weathered observation slate to always choose the currently best option.

This is precisely the kind of shortcut a careful builder should try first. The instruction to always choose the currently best option preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: an unlucky first result permanently hides a better alternative.

The counterexample separates two questions that the attempt to always choose the currently best option had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the weathered observation slate fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now reserve some choices for exploration while exploiting accumulated evidence. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Bandits**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## Learning While Choosing

Cafe A wins its first two trials; continuing to sample B reveals it succeeds eight out of ten times.

## Where bandits runs out

Exploration has real cost and can be unacceptable for high-risk actions.

The bandits repair holds, but the world asks for something it was never given. At the Living Watchgarden, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the weathered observation slate

Rebuild the bandits scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 071](../071-features-inside-networks/README.md)
