# Excavation 036 — Tokenization: What Can a Language Model See?

[Previous: A Tiny Neural Network](../035-tiny-neural-network/README.md)


## Take the First Step Yourself

> **Your problem:** Our network accepts numbers, but people produce an open stream of words, punctuation, names, code, and writing systems. Before learning language, the machine needs repeatable input pieces.

> **Try your first idea:** Give every complete word one ID. Spaces appear to provide the boundaries.

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

## Problem

Our network accepts numbers, but people produce an open stream of words, punctuation, names, code, and writing systems. Before learning language, the machine needs repeatable input pieces.

## Your First Attempt

Give every complete word one ID. Spaces appear to provide the boundaries.

## Break Your First Attempt

Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Give every complete word one ID. Spaces appear to provide the boundaries.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

## Repair Your Attempt

Use characters. Any new spelling can now be represented.

## Why It Still Fails

Common words become long sequences and the model must reconstruct recurring fragments such as ing repeatedly. Words are too large; characters are often too small.

## What You Have Just Invented

Begin with universally representable pieces. Count adjacent pairs and repeatedly merge the pair that occurs most often. Frequent structure earns a reusable subword token; rare forms remain constructible from smaller pieces.

## Only Now Give the Discovery a Mathematical Name

## Build Every Piece from the Concrete Example

In low, lower, lowest, pair l-o appears three times, more than e-r once. Counting selects l-o; merging creates lo. Recounting can then select lo-w and create reusable low.

### Give Short Names Only After We Know the Pieces

- **a and b** are neighboring current tokens; c(a,b) counts their repeated adjacency because repetition is the evidence for reuse.
- The star marks the pair selected for merging.
- **arg max** returns the pair itself, not its count, because that pair must be replaced.
- Maximizing over every candidate pair makes the merge arise from the corpus rather than a hand-written linguistic rule.


Count, choose, merge, and repeat. The symbols only compress the procedure already needed.

Only now can we compress that reasoning:

$$
c(a,b)=\text{number of adjacent occurrences of }(a,b)
$$

$$
(a^*,b^*)=\operatorname*{arg\,max}_{(a,b)}c(a,b)
$$


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

[Next: Input Embeddings](../037-input-embeddings/README.md)
