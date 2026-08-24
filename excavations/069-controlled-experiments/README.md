# Excavation 069 — Controlled Experiments

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality) · [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics)
>
> **Applied territory:** Learning in the world and interpretability

Drift detection says that the input or outcome distribution moved. It does not say whether a new model, a holiday, a policy change, or chance caused the observed performance difference.

A new case arrives at the Living Watchgarden, but the field naturalist first reaches for the familiar weathered observation slate. Its promise is simple: compare this week with last week.

Then the quiet test arrives: a holiday raises sales for both systems and receives credit as a model improvement. What looked like simplicity is revealed as a missing distinction.

*The field naturalist sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ compare this week with last week ──▶ blurred: a holiday raises sales for both…
      │
      └── new lens ──▶ randomly assign comparable cases to… ──▶ distinction survives
```

The field naturalist turns the weathered observation slate toward the light. Through the old engraving, compare this week with last week, the evidence ends in the same contradiction: a holiday raises sales for both systems and receives credit as a model improvement. A second engraving adds only the power to randomly assign comparable cases to old and new behavior and compare predefined outcomes. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The field naturalist circles the place where the two controlled experiments cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: randomly assign comparable cases to old and new behavior and compare predefined outcomes. The field naturalist writes **Controlled Experiments** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The field naturalist does not memorize controlled experiments. Instead, the field naturalist memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can randomly assign comparable cases to old and new behavior and compare predefined outcomes. The formal name merely lets that motion be shared.

## Understanding controlled experiments

Split 10,000 simultaneous visitors evenly; conversion is 5% for control and 5.5% for treatment under the same week.

## Where controlled experiments runs out

Experiments require sufficient samples, ethical limits, and careful metrics.

One unsolved mark remains on the weathered observation slate. None of the responsibilities inside Controlled Experiments can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the weathered observation slate

Rebuild the controlled experiments scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 070](../070-bandits/README.md)
