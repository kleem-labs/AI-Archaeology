# Excavation 021 — Cross-Entropy — Paying for Confidently Wrong Predictions

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Information Theory](../../MATHEMATICS_ATLAS.md#information) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Learning from uncertainty and error

Entropy measures how uncertain reality itself is. A learning machine introduces a second distribution—its own proposed beliefs—and can be far more certain than the evidence deserves.

The previous discovery reaches the Lantern Observatory carrying one unfinished problem. Beside the ring of glass lanterns, the keeper of uncertain stories first tries to use zero for correct and one for wrong.

There is good reason to begin this way. If we use zero for correct and one for wrong, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: it treats barely wrong and confidently wrong as equal. Use ordinary distance between probabilities; it does not directly price the information wasted by the prediction.

This failure cannot be repaired by performing the instruction to use zero for correct and one for wrong more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the ring of glass lanterns; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to charge the information cost assigned by the predicted distribution to the outcome that actually occurred. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Cross-Entropy**. The name is simply a handle for the distinction already reconstructed.

## The calculation hidden inside cross-entropy

The keeper of uncertain stories carries the cross-entropy scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Reality says the answer is tiger. A model assigning tiger 0.9 pays -log(0.9), about 0.105. A model assigning 0.01 pays about 4.605. The confident wrong model is charged far more.

### Naming what is already on the table

**P** is the distribution reality supplies; pᵢ weights which outcomes actually occur.
**Q** is the model's proposed distribution; qᵢ is the probability it assigned outcome i.
**−log qᵢ** makes confident neglect extremely costly.
Summing the reality-weighted costs gives one expected prediction penalty H(P,Q).

### Why the melody needs these exact notes

[−log qᵢ](../../MATHEMATICAL_MOVES.md#logarithm) charges a large price when the model assigns tiny probability to what occurs; logarithms also let sequence costs add instead of multiplying many small probabilities.
[Multiplying by pᵢ](../../MATHEMATICAL_MOVES.md#multiplication) asks reality how often that charge should count. Without pᵢ, impossible and common outcomes would receive equal influence.
[The sum](../../MATHEMATICAL_MOVES.md#summation) forms one expected bill across outcomes. A product would allow one zero-weighted outcome to erase every other prediction error.

Trace each operation by touch rather than by name: **the spiral stair**—compounded chances become steps that can be accumulated; **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the chorus**—many witnesses contribute to one answer without one silence erasing the rest. Together they form the smallest mechanism that survives the counterexample.

The story of cross-entropy has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
H(P,Q)=-\sum_i p_i\log q_i
$$

## Cross-Entropy beyond this one case

A bad map that assigns almost no chance to the road you actually encounter deserves a much larger penalty than a map that admitted uncertainty.

## Where cross-entropy runs out

Cross-entropy judges probabilities, so the model outputs must form a valid distribution. It tells us the error but not yet how each weight caused it.

One unsolved mark remains on the ring of glass lanterns. None of the responsibilities inside Cross-Entropy can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the ring of glass lanterns

Rebuild the cross-entropy scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
