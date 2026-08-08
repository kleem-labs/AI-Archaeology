# Excavation 042 — Vocabulary Probabilities — Turning Scores into a Prediction

[Previous: Excavation 041](../041-logits/README.md)

The output head gives arbitrary positive and negative logits. We need comparable probabilities and a training loss.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Divide each logit by their sum. Negative values break probability and shifting all scores changes the result.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Divide each logit by their sum. Negative values break probability and shifting all scores changes the result.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token.

Only after that reasoning may we give your discovery its inherited name.

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
