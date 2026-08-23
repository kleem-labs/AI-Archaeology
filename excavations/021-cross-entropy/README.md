# Excavation 021 — Cross-Entropy — Paying for Confidently Wrong Predictions

<!-- book-prose-v2 -->

Entropy measures how uncertain reality itself is. A learning machine introduces a second distribution—its own proposed beliefs—and can be far more certain than the evidence deserves.

At this point the shortest path seems to be to use zero for correct and one for wrong.

This is how cross-entropy ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

Reality now asks a question the retained information cannot answer: it treats barely wrong and confidently wrong as equal. Use ordinary distance between probabilities; it does not directly price the information wasted by the prediction.

The wrong answer makes the need for cross-entropy inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: charge the information cost assigned by the predicted distribution to the outcome that actually occurred.

The usual name, **Cross-Entropy**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to use zero for correct and one for wrong. produces the observed failure: it treats barely wrong and confidently wrong as equal. Use ordinary distance between probabilities; it does not directly price the information wasted by the prediction. Starting with the repaired demand to charge the information cost assigned by the predicted distribution to the outcome that actually occurred preserves the information the shortcut lost. The subject of cross-entropy lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to charge the information cost assigned by the predicted distribution to the outcome that actually occurred instead of merely trying to use zero for correct and one for wrong.. That controlled contrast is what turns a plausible explanation of cross-entropy into an understandable derivation.

## The calculation hidden inside cross-entropy

Before Cross-Entropy receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Reality says the answer is tiger. A model assigning tiger 0.9 pays -log(0.9), about 0.105. A model assigning 0.01 pays about 4.605. The confident wrong model is charged far more.

### Names for pieces we have already used

**P** is the distribution reality supplies; pᵢ weights which outcomes actually occur.
**Q** is the model's proposed distribution; qᵢ is the probability it assigned outcome i.
**−log qᵢ** makes confident neglect extremely costly.
Summing the reality-weighted costs gives one expected prediction penalty H(P,Q).

### Why no cheaper operation does the same job

[−log qᵢ](../../MATHEMATICAL_MOVES.md#logarithm) charges a large price when the model assigns tiny probability to what occurs; logarithms also let sequence costs add instead of multiplying many small probabilities.
[Multiplying by pᵢ](../../MATHEMATICAL_MOVES.md#multiplication) asks reality how often that charge should count. Without pᵢ, impossible and common outcomes would receive equal influence.
[The sum](../../MATHEMATICAL_MOVES.md#summation) forms one expected bill across outcomes. A product would allow one zero-weighted outcome to erase every other prediction error.

The notation is finally shorter than the story that created it:

$$
H(P,Q)=-\sum_i p_i\log q_i
$$

## Cross-Entropy beyond this one case

A bad map that assigns almost no chance to the road you actually encounter deserves a much larger penalty than a map that admitted uncertainty.

## Where cross-entropy runs out

Cross-entropy judges probabilities, so the model outputs must form a valid distribution. It tells us the error but not yet how each weight caused it.

Look back at what cross-entropy actually preserves: it can charge the information cost assigned by the predicted distribution to the outcome that actually occurred. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

## Take cross-entropy to the workbench

The reader has reconstructed cross-entropy in words; the workbench tests whether those words specify a real procedure. Build the wrong idea first, break it, then use [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running cross-entropy, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the cross-entropy result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
