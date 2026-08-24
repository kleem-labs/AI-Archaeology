# Excavation 070 — Bandits — Learning While Choosing

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Controlled experiments isolate causal effects by holding alternatives steady. In a live recommender, withholding every uncertain choice until a long experiment ends sacrifices opportunities to learn while serving users.

The doors of the Living Watchgarden close against the wind. On the weathered observation slate, the field naturalist writes the cheapest rule that might still be true: always choose the currently best option.

The field naturalist repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: an unlucky first result permanently hides a better alternative. The failure is stable enough to become evidence.

*The field naturalist sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: always choose the currently best…
possible road B ─┘              └── loses: an unlucky first result permanently…

same roads ──▶ repaired map ──▶ reserve some choices for exploration…
```

Across the weathered observation slate, the old path and the repaired path run side by side. One carries “always choose the currently best option”; the other knows how to reserve some choices for exploration while exploiting accumulated evidence. When the failure—an unlucky first result permanently hides a better alternative—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to bandits. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: reserve some choices for exploration while exploiting accumulated evidence. This problem and its repair will travel under the name **Bandits**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—always choose the currently best option? The answer remains an unlucky first result permanently hides a better alternative. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.


Before leaving the weathered observation slate, the field naturalist tests the new idea backward. Remove the ability to reserve some choices for exploration while exploiting accumulated evidence, and the method falls back to this tempting instruction: always choose the currently best option. The old consequence returns—an unlucky first result permanently hides a better alternative. Restore the missing ability and that particular contradiction disappears. This reversible test is why bandits belongs to the growing structure rather than to a list of facts to memorize.

## Learning While Choosing

Cafe A wins its first two trials; continuing to sample B reveals it succeeds eight out of ten times.

## Where bandits runs out

Exploration has real cost and can be unacceptable for high-risk actions.

The bandits repair holds, but the world asks for something it was never given. At the Living Watchgarden, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the weathered observation slate

Rebuild the bandits scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 071](../071-features-inside-networks/README.md)
