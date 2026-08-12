# Excavation 041 — Logits — Let Every Vocabulary Token Compete

Shifted inputs and targets create one lesson at every position. The Transformer answers each lesson with a contextual vector, but a vector is not yet a competition among words such as tiger, river, or sleeps.

An obvious shortcut is to choose the nearest input embedding directly. That restricts the scoring rule and hides how every vocabulary candidate should compete.

That failure tells us to use a learned linear map to produce one raw score for every vocabulary item.

## From procedure to notation

Logits have no standalone probability meaning and can shift together without changing the final distribution.

## The arithmetic we have earned

After reading “the striped animal is a,” the model holds one contextual description. Every vocabulary candidate now presents a learned question: how well does this description support *tiger*, *river*, *sleeping*, and so on? Matching the same context against each candidate produces one raw score per word. Those scores are logits; they are competitors, not probabilities yet.

### Only now do the symbols earn names

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
