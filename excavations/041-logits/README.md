# Excavation 041 — Logits — Let Every Vocabulary Token Compete

[Previous: Excavation 040](../040-next-token-examples/README.md)

The Transformer produces one contextual vector per position. A vector is not yet a prediction such as tiger, river, or runs.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Choose the nearest input embedding directly. That restricts the scoring rule and hides how every vocabulary candidate should compete.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Choose the nearest input embedding directly. That restricts the scoring rule and hides how every vocabulary candidate should compete.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Use a learned linear map to produce one raw score for every vocabulary item.

Only after that reasoning may we give your discovery its inherited name.

## Why It Still Fails

Logits have no standalone probability meaning and can shift together without changing the final distribution.

## Compress your discovery into mathematics


## Build each piece from what just happened

Let hidden state be [2,1]. One candidate column [3,0] scores 6; another [0,4] scores 4. Adding each candidate bias adjusts its baseline. These raw comparisons are logits.

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
