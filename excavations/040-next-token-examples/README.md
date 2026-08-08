# Excavation 040 — Next-Token Examples — One Sentence Becomes Many Lessons

[Previous: Excavation 039](../039-causal-mask/README.md)

We have tokens, positions, and a causal boundary. The model still needs explicit questions and answers.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Treat an entire sentence as one training example with one answer. Most of its transitions provide no learning signal.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Treat an entire sentence as one training example with one answer. Most of its transitions provide no learning signal.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Shift the sequence by one position so every visible prefix predicts the token immediately following it.

Only after that reasoning may we give your discovery its inherited name.

## Why It Still Fails

Padding and document boundaries can create false targets unless their losses are masked.

## Compress your discovery into mathematics


## Build each piece from what just happened

Tokens [the,cat,slept] become inputs [the,cat] and targets [cat,slept]. One forward pass therefore asks “after the?” and “after the cat?” at separate positions.

### Give Short Names Only After We Know the Pieces

- **t₀…t_n** are consecutive tokens from one observed sequence.
- Input x stops one token early because each position needs an answer to its right.
- Target y starts one token later so y_i is exactly the next token after x_i.
- The shared length lets one forward pass create a supervised lesson at every position.

Only now can we compress that reasoning:

$$
x=(t_0,\ldots,t_{n-1}),\qquad y=(t_1,\ldots,t_n)
$$


The equation arrives after every operation has a job.

## Carry the idea back into the world

A reading teacher pauses after every word, not only at the final period.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 041](../041-logits/README.md)
