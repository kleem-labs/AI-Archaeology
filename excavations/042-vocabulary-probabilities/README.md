# Excavation 042 — Vocabulary Probabilities — Turning Scores into a Prediction

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

The output head lets every vocabulary token present a raw compatibility score. Those logits may be negative, enormous, or shifted together; neither the reader nor the loss can treat them as comparable beliefs yet.

The sentence-wheel at the Clockwork Scriptorium still carries the marks of the previous discovery. The mechanist follows them as far as they seem willing to go: divide each logit by their sum.

For a moment the mark looks complete. Then the evidence refuses to fit: negative values break probability and shifting all scores changes the result. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The mechanist sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ divide each logit by their sum ──▶ blurred: negative values break probability and…
      │
      └── new lens ──▶ exponentiate relative scores,… ──▶ distinction survives
```

The mechanist lays two translucent sheets over the sentence-wheel. The first is inscribed, “divide each logit by their sum.” Its path ends where negative values break probability and shifting all scores changes the result. The second receives the same evidence but is allowed to exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token. Held to the light, the sheets separate at exactly one decision.

No one reaches for a vocabulary probabilities formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The mechanist changes only that one responsibility: exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token. When the ink dries, the name **Vocabulary Probabilities** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because negative values break probability and shifting all scores changes the result, while the other can exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token. That fork—not the vocabulary—is where vocabulary probabilities lives.

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
