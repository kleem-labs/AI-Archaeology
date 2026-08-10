# Excavation 042 — Vocabulary Probabilities — Turning Scores into a Prediction

[Previous: Excavation 041](../041-logits/README.md)

The output head gives arbitrary positive and negative logits. We need comparable probabilities and a training loss.

Without knowing the inherited method, we might try this: Divide each logit by their sum. Negative values break probability and shifting all scores changes the result.

Remove that assumption and the needed repair becomes clear: Exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token.

## From procedure to notation

A probability distribution expresses model confidence, not truth. Poor calibration and biased data remain possible.



## Build each piece from what just happened

Suppose *tiger* receives score 2 and *leopard* score 1 after “the striped animal is a.” Softmax turns them into shares of about 0.73 and 0.27. If the observed answer is *tiger*, the model pays the surprise of assigning it 0.73. Had it assigned tiger only 0.01, the penalty would be far larger. The loss therefore records not merely whether the guess won, but how much belief the model risked on reality.

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
