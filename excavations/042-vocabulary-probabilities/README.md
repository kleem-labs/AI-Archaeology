# Excavation 042 — Vocabulary Probabilities — Turning Scores into a Prediction

[Previous: Excavation 041](../041-logits/README.md)

The output head gives arbitrary positive and negative logits. We need comparable probabilities and a training loss.

Without knowing the inherited method, we might try this: Divide each logit by their sum. Negative values break probability and shifting all scores changes the result.

Its hidden assumption appears in the following case: Divide each logit by their sum. Negative values break probability and shifting all scores changes the result.

Remove that assumption and the needed repair becomes clear: Exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token.

## Why It Still Fails

A probability distribution expresses model confidence, not truth. Poor calibration and biased data remain possible.

## Compress your discovery into mathematics


## Build each piece from what just happened

For logits [1,2], softmax gives about [0.27,0.73]. If the observed token is the second, loss is -log(0.73), about 0.31. Assigning it 0.01 would cost about 4.61.

### Give Short Names Only After We Know the Pieces

- **ℓ_i** is candidate i's raw score.
- Dividing exponentiated evidence by the sum over all j creates positive probabilities p_i that total one.
- **y** is the observed next-token index, so p_y is the probability assigned to what happened.
- The logarithm converts products across examples into sums and the minus sign makes low assigned probability a large positive loss L.

Only now can we compress that reasoning:

$$
p_i=\frac{e^{\ell_i}}{\sum_j e^{\ell_j}},\qquad L=-\log p_y
$$


The equation arrives after every operation has a job.

## Carry the idea back into the world

A race score becomes odds only after every competitor is considered together.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 043](../043-sampling/README.md)
