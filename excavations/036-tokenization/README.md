# Excavation 036 — Tokenization: What Can a Language Model See?

[Previous: A Tiny Neural Network](../035-tiny-neural-network/README.md)

## Problem

Our network accepts numbers, but people produce an open stream of words, punctuation, names, code, and writing systems. Before learning language, the machine needs repeatable input pieces.

## Naive Attempt

Give every complete word one ID. Spaces appear to provide the boundaries.

## Why It Fails

Tiger, tiger!, tigers, and an unseen name become unrelated entries. The vocabulary can grow forever, unknown words disappear into one bucket, and many languages do not use English-style spaces.

## Better Attempt

Use characters. Any new spelling can now be represented.

## Why It Still Fails

Common words become long sequences and the model must reconstruct recurring fragments such as ing repeatedly. Words are too large; characters are often too small.

## Key Insight

Begin with universally representable pieces. Count adjacent pairs and repeatedly merge the pair that occurs most often. Frequent structure earns a reusable subword token; rare forms remain constructible from smaller pieces.

## Mathematics Emerges

$$
c(a,b)=\text{number of adjacent occurrences of }(a,b)
$$

$$
(a^*,b^*)=\operatorname*{arg\,max}_{(a,b)}c(a,b)
$$

Count, choose, merge, and repeat. The symbols only compress the procedure already needed.

## Real-World Analogy

Early readers sound out letters. With experience they recognize recurring fragments and whole familiar words while retaining the ability to sound out something new.

## Concrete Discovery

For low, lower, and lowest, the pair l-o repeats three times. Merge it into lo. The pair lo-w then repeats three times, so low becomes reusable. Nobody declared low meaningful; repetition made keeping it whole economical.

## Limits

Tokenization chooses pieces, not meanings. IDs remain arbitrary, and the chosen vocabulary affects sequence length, cost, multilingual coverage, and which patterns are easy to notice.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

## Next Need

Token IDs still contain no relationships. The next excavation must give tokens learnable coordinates and preserve their order.
