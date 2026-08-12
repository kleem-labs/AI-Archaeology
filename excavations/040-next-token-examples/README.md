# Excavation 040 — Next-Token Examples — One Sentence Becomes Many Lessons

Causal masking prevents the learner from reading future answers. The model still needs to turn one sentence into all the honest prediction questions hidden inside it.

Using what we have, we treat an entire sentence as one training example with one answer. Most of its transitions provide no learning signal.

Now we can see what is missing: we must shift the sequence by one position so every visible prefix predicts the token immediately following it.

## From procedure to notation

Padding and document boundaries can create false targets unless their losses are masked.

## The arithmetic we have earned

Tokens [the,cat,slept] become inputs [the,cat] and targets [cat,slept]. One forward pass therefore asks “after the?” and “after the cat?” at separate positions.

### Only now do the symbols earn names

- **t₀…t_n** are consecutive tokens from one observed sequence.
- Input x stops one token early because each position needs an answer to its right.
- Target y starts one token later so y_i is exactly the next token after x_i.
- The shared length lets one forward pass create a supervised lesson at every position.

### Why these operations are forced

- [Parentheses](../../MATHEMATICAL_MOVES.md#brackets) keep each ordered token sequence intact; summing the tokens would destroy both identity and order.
- [The shifted indices](../../MATHEMATICAL_MOVES.md#indices) remove the final token from inputs and the first token from targets, so target position i is exactly the next token after input position i.

Only now can we compress that reasoning:

$$
x=(t_0,\ldots,t_{n-1})
$$

$$
y=(t_1,\ldots,t_n)
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
