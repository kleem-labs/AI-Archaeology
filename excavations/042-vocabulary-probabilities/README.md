# Excavation 042 — Vocabulary Probabilities — Turning Scores into a Prediction

<!-- book-prose-v2 -->

The output head lets every vocabulary token present a raw compatibility score. Those logits may be negative, enormous, or shifted together; neither the reader nor the loss can treat them as comparable beliefs yet.

The obvious economy is to divide each logit by their sum.

The proposal deserves a fair hearing. For vocabulary probabilities, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Its hidden assumption becomes visible as soon as we observe that negative values break probability and shifting all scores changes the result.

The failure changes the question behind vocabulary probabilities. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token.

Only at this point does the inherited name **Vocabulary Probabilities** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of vocabulary probabilities by mentally removing the repair. We fall back to the proposal to divide each logit by their sum.; then negative values break probability and shifting all scores changes the result. Restore only the ability to exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to divide each logit by their sum. to requiring the system to exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to vocabulary probabilities.

## The calculation hidden inside vocabulary probabilities

Do not read the coming Vocabulary Probabilities line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

A probability distribution expresses model confidence, not truth. Poor calibration and biased data remain possible.

Suppose *tiger* receives score 2 and *leopard* score 1 after “the striped animal is a.” Softmax turns them into shares of about 0.73 and 0.27. If the observed answer is *tiger*, the model pays the surprise of assigning it 0.73. Had it assigned tiger only 0.01, the penalty would be far larger. The loss therefore records not merely whether the guess won, but how much belief the model risked on reality.

### Names for pieces we have already used

**ℓ_i** is candidate i's raw score.
Dividing exponentiated evidence by the sum over all j creates positive probabilities p_i that total one.
**y** is the observed next-token index, so p_y is the probability assigned to what happened.
The logarithm converts products across examples into sums and the minus sign makes low assigned probability a large positive loss L.

### Why no cheaper operation does the same job

[Exponentials](../../MATHEMATICAL_MOVES.md#exponential) create positive candidate weights and preserve score order; squaring would make strongly negative logits look desirable.
[Summing all weights](../../MATHEMATICAL_MOVES.md#summation) measures the whole amount to be shared, and [division](../../MATHEMATICAL_MOVES.md#division) turns each candidate's weight into a probability share.
[The log](../../MATHEMATICAL_MOVES.md#logarithm) turns the probability assigned to the observed token into additive information cost; [the minus sign](../../MATHEMATICAL_MOVES.md#negative-sign) makes low probability expensive and certainty cost zero.

The notation is finally shorter than the story that created it:

$$
p_i=\frac{e^{\ell_i}}{\sum_j e^{\ell_j}}
$$

$$
L=-\log p_y
$$

The equation arrives after every operation has a job.

## Vocabulary Probabilities beyond this one case

A race score becomes odds only after every competitor is considered together.

## Take vocabulary probabilities to the workbench

A claim about vocabulary probabilities now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running vocabulary probabilities, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the vocabulary probabilities result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 043](../043-sampling/README.md)
