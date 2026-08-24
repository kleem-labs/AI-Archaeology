# Excavation 021 — Cross-Entropy — Paying for Confidently Wrong Predictions

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Information Theory](../../MATHEMATICS_ATLAS.md#information) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Learning from uncertainty and error

Entropy measures how uncertain reality itself is. A learning machine introduces a second distribution—its own proposed beliefs—and can be far more certain than the evidence deserves.

A new case arrives at the Lantern Observatory, but the keeper of uncertain stories first reaches for the familiar ring of glass lanterns. Its promise is simple: use zero for correct and one for wrong.

Then the quiet test arrives: it treats barely wrong and confidently wrong as equal. Use ordinary distance between probabilities; it does not directly price the information wasted by the prediction. What looked like simplicity is revealed as a missing distinction.

*The keeper of uncertain stories sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: use zero for correct and one for wrong
                         │
                         └── mismatch: it treats barely wrong and…

reference evidence ──▶ measured repair: charge the information cost assigned…
```

The keeper of uncertain stories turns the ring of glass lanterns toward the light. Through the old engraving, use zero for correct and one for wrong, the evidence ends in the same contradiction: it treats barely wrong and confidently wrong as equal. Use ordinary distance between probabilities; it does not directly price the information wasted by the prediction. A second engraving adds only the power to charge the information cost assigned by the predicted distribution to the outcome that actually occurred. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The keeper of uncertain stories circles the place where the two cross-entropy cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: charge the information cost assigned by the predicted distribution to the outcome that actually occurred. The keeper of uncertain stories writes **Cross-Entropy** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The keeper of uncertain stories does not memorize cross-entropy. Instead, the keeper of uncertain stories memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can charge the information cost assigned by the predicted distribution to the outcome that actually occurred. The formal name merely lets that motion be shared.

<!-- memory-film-v1:start -->
> **Memory realm 3 of 18 — [Lantern Observatory](../../MEMORY_PALACE.md#realm-3)**
>
> **The question carried into this chamber:** What fails if we use zero for correct and one for wrong?

## When the chamber changes

Keep the formal name Cross-Entropy covered for another moment. The surviving image is enough to rebuild it.

First hold the failed picture still: The bridge follows the tempting path—use zero for correct and one for wrong. Then the evidence answers: it treats barely wrong and confidently wrong as equal. Use ordinary distance between probabilities; it does not directly price the information wasted by the prediction.

Now let the chamber move: The keeper of uncertain stories changes one moving part. The bridge can now charge the information cost assigned by the predicted distribution to the outcome that actually occurred.

The object that should remain after the terminology disappears is **the cross-entropy bridge mounted on the ring of glass lanterns**.

> **Memory seal — Cross-Entropy**
>
> Cross-Entropy keeps the missing power: charge the information cost assigned by the predicted distribution to the outcome that actually occurred.

Give the idea a bodily path: Touch the cross-entropy bridge in imagination: tilt one hand as the broken rule and use the other to bring the necessary distinction back into balance.
<!-- memory-film-v1:end -->

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
