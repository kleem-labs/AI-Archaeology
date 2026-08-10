# Excavation 041 — Logits — Let Every Vocabulary Token Compete

[Previous: Excavation 040](../040-next-token-examples/README.md)

The Transformer produces one contextual vector per position. A vector is not yet a prediction such as tiger, river, or runs.

A reasonable place to begin is: Choose the nearest input embedding directly. That restricts the scoring rule and hides how every vocabulary candidate should compete.

What broke tells us what the replacement must preserve: Use a learned linear map to produce one raw score for every vocabulary item.

## From procedure to notation

Logits have no standalone probability meaning and can shift together without changing the final distribution.



## Build each piece from what just happened

After reading “the striped animal is a,” the model holds one contextual description. Every vocabulary candidate now presents a learned question: how well does this description support *tiger*, *river*, *sleeping*, and so on? Matching the same context against each candidate produces one raw score per word. Those scores are logits; they are competitors, not probabilities yet.

### Give Short Names Only After We Know the Pieces

- **h** is one contextual token vector containing what the Transformer currently knows.
- **W_vocab** has one scoring direction per vocabulary candidate; multiplication compares h with all candidates at once.
- **b** allows each token a learned baseline tendency.
- **ℓ_i** is the resulting unconstrained logit for candidate i—not yet a probability.

Only now can we compress that reasoning:

$$
\ell_i=hW_{\text{vocab}}+b
$$


The equation arrives after every operation has a job.

## Carry the idea back into the world

Judges first assign unconstrained scores to every contestant before those scores are converted into shares.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 042](../042-vocabulary-probabilities/README.md)
