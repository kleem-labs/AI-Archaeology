# Excavation 042 — Vocabulary Probabilities — Turning Scores into a Prediction

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Language models and useful answers

The output head lets every vocabulary token present a raw compatibility score. Those logits may be negative, enormous, or shifted together; they cannot yet serve as comparable beliefs or a stable training target.

A new case arrives at the Clockwork Scriptorium. Nothing yet demands a new invention, so the mechanist uses the sentence-wheel to divide each logit by their sum.

This is precisely the kind of shortcut a careful builder should try first. The instruction to divide each logit by their sum preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: negative values break probability and shifting all scores changes the result.

The counterexample separates two questions that the attempt to divide each logit by their sum had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the sentence-wheel fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Vocabulary Probabilities**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## The calculation hidden inside vocabulary probabilities

The mechanist carries the vocabulary probabilities scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A probability distribution expresses model confidence, not truth. Poor calibration and biased data remain possible.

Suppose *tiger* receives score 2 and *leopard* score 1 after “the striped animal is a.” Softmax turns them into shares of about 0.73 and 0.27. If the observed answer is *tiger*, the model pays the surprise of assigning it 0.73. Had it assigned tiger only 0.01, the penalty would be far larger. The loss therefore records not merely whether the guess won, but how much belief the model risked on reality.

### Naming what is already on the table

**ℓ_i** is candidate i's raw score.
Dividing exponentiated evidence by the sum over all j creates positive probabilities p_i that total one.
**y** is the observed next-token index, so p_y is the probability assigned to what happened.
The logarithm converts products across examples into sums and the minus sign makes low assigned probability a large positive loss L.

### Why the melody needs these exact notes

[Exponentials](../../MATHEMATICAL_MOVES.md#exponential) create positive candidate weights and preserve score order; squaring would make strongly negative logits look desirable.
[Summing all weights](../../MATHEMATICAL_MOVES.md#summation) measures the whole amount to be shared, and [division](../../MATHEMATICAL_MOVES.md#division) turns each candidate's weight into a probability share.
[The log](../../MATHEMATICAL_MOVES.md#logarithm) turns the probability assigned to the observed token into additive information cost; [the minus sign](../../MATHEMATICAL_MOVES.md#negative-sign) makes low probability expensive and certainty cost zero.

Three old motions cast new shadows here: **the rising flame**—a small score difference becomes positive relative evidence; **the chorus**—many witnesses contribute to one answer without one silence erasing the rest; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Every mark needed for vocabulary probabilities is now visible on the sentence-wheel. The symbols do not add an idea; they bind the discovered moves into one line:

$$
p_i=\frac{e^{\ell_i}}{\sum_j e^{\ell_j}}
$$

$$
L=-\log p_y
$$

The equation arrives after every operation has a job.

## Vocabulary Probabilities beyond this one case

A race score becomes odds only after every competitor is considered together.

## Return to the sentence-wheel

Rebuild the vocabulary probabilities scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 043](../043-sampling/README.md)
