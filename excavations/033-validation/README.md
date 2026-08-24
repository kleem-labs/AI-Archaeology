# Excavation 033 — Validation — Testing Without Peeking at the Final Exam

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Learning from uncertainty and error

Regularization changes which fitted explanation the learner prefers. Choosing its strength by repeatedly checking the final exam would quietly turn that exam into more training data.

Morning reaches the Lantern Observatory before anyone has a name for today's difficulty. Beside the ring of glass lanterns, the keeper of uncertain stories tries the smallest continuation of what already works: use training loss for every choice; it rewards memorization.

Then the quiet test arrives: check the test set repeatedly; every decision leaks test information back into development. What looked like simplicity is revealed as a missing distinction.

*The keeper of uncertain stories sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: use training loss for every choice;…
                         │
                         └── mismatch: check the test set repeatedly; every…

reference evidence ──▶ measured repair: split data by role: training changes…
```

The keeper of uncertain stories turns the ring of glass lanterns toward the light. Through the old engraving, use training loss for every choice; it rewards memorization, the evidence ends in the same contradiction: check the test set repeatedly; every decision leaks test information back into development. A second engraving adds only the power to split data by role: training changes weights, validation changes design decisions, and test data is opened once at the end. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The keeper of uncertain stories circles the place where the two validation cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: split data by role: training changes weights, validation changes design decisions, and test data is opened once at the end. The keeper of uncertain stories writes **Validation** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The keeper of uncertain stories does not memorize validation. Instead, the keeper of uncertain stories memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can split data by role: training changes weights, validation changes design decisions, and test data is opened once at the end. The formal name merely lets that motion be shared.

## The calculation hidden inside validation

The keeper of uncertain stories carries the validation scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but random splits fail when future, users, families, or duplicated records leak across boundaries. The split must match the real deployment question.

With 100 examples, use 60 to change weights, 20 to choose learning rate, and keep 20 sealed. If the sealed 20 guide choices, they stop being an honest final test.

### Naming what is already on the table

**D** is all available data.
The three named subsets exist because weight learning, design choices, and final measurement must not share feedback.
Union means they reconstruct the available collection.
The intended split also requires no example to leak between sets, even though the compact union symbol alone does not state disjointness.

### Why the melody needs these exact notes

[Union](../../MATHEMATICAL_MOVES.md#union) says the complete dataset contains the members assigned to training, validation, or test roles. Ordinary addition is for numeric quantities, not for joining collections of examples.
Separate names preserve separate responsibilities; the union sign alone does not guarantee the sets do not overlap, so the split procedure must enforce that boundary.

The story of validation has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
D=D_{\text{train}}\cup D_{\text{validation}}\cup D_{\text{test}}
$$

## Validation beyond this one case

A practice exam guides study. A sealed final exam measures what survived without feedback.

## Return to the ring of glass lanterns

Rebuild the validation scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Excavation 034](../034-generalization/README.md)
