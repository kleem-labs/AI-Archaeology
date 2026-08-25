# Excavation 031 — Overfitting — When Perfect Memory Pretends to Be Intelligence

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Learning from uncertainty and error

Activation gates let the network bend and build conditional internal paths. That flexibility also makes a new deception possible: the machine can reproduce every training example without learning what should survive beyond them.

Inside the Lantern Observatory, the old method is given an honest chance. The keeper of uncertain stories places the evidence on the ring of glass lanterns and tries to celebrate zero training error.

Nothing about this first move is careless. To celebrate zero training error is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: the model may have memorized scratches and shadows. Make the model infinitely flexible; it can store even more irrelevant detail.

The important discovery is not merely that trying to celebrate zero training error failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the ring of glass lanterns, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to reserve unseen cases and compare training success with performance outside the training memory. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Overfitting**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## The calculation hidden inside overfitting

The keeper of uncertain stories carries the overfitting scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but a gap diagnoses overfitting but does not identify its cause. Leakage, distribution shift, and noisy evaluation can mislead us.

A model has training loss 0.02 and unseen loss 0.17. Subtracting gives a gap of 0.15. The low training number shows memory; the gap measures how much success disappeared outside it.

### Naming what is already on the table

**L_train** measures error on examples allowed to shape the model.
**L_unseen** measures error on held-out observations.
Subtraction isolates deterioration outside memory instead of confusing it with absolute task difficulty.
A positive generalization gap is evidence that training success did not fully survive.

### Why the melody needs these exact notes

[Unseen loss minus training loss](../../MATHEMATICAL_MOVES.md#subtraction) isolates how much performance deteriorates beyond memorized examples. Adding the losses would measure total error, not the transfer gap.
The order matters: a positive answer naturally means unseen cases are worse. Reversing the subtraction would reverse that interpretation.

The calculation reuses familiar motions: **the chisel**—what is shared is removed so the remaining change can be seen. Together they keep the path from the concrete case to notation intact.

The keeper of uncertain stories reads the journey of overfitting once more across the ring of glass lanterns, then lets the words contract without losing their order:

$$
\text{generalization gap}=L_{\text{unseen}}-L_{\text{train}}
$$

## Overfitting beyond this one case

A student who memorizes answer positions can ace the practice sheet and fail when the same ideas are rearranged.

## Return to the ring of glass lanterns

Rebuild the overfitting scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Excavation 032](../032-regularization/README.md)
