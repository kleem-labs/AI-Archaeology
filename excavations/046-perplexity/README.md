# Excavation 046 — Perplexity — How Surprised Is the Model?

[Previous: Excavation 045](../045-tiny-gpt/README.md)

## Take the First Step Yourself

> **Your problem:** Two tiny language models produce fluent-looking text. Which one consistently assigns better probabilities to real held-out sentences?

> **Try your first idea:** Count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree.

> **Now try to break your idea:** Use the held-out sentence “the tiger sleeps.” Model A assigns the observed tokens probabilities 0.5, 0.5, and 0.5; Model B assigns 0.9, 0.1, and 0.9. A few attractive samples cannot expose B’s severe surprise at the middle token.

> Stop here. State what the repair must accomplish in ordinary language. Do not name a standard technique.

## The Observation

Two tiny language models produce fluent-looking text. Which one consistently assigns better probabilities to real held-out sentences?

## Your First Attempt

Count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree.

## Break Your First Attempt

Use the held-out sentence “the tiger sleeps.” Model A assigns the observed tokens probabilities 0.5, 0.5, and 0.5; Model B assigns 0.9, 0.1, and 0.9. A few attractive samples cannot expose B’s severe surprise at the middle token.

What information did the attempt lose? Write that requirement before continuing.

## Repair Your Attempt

Score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale.

## What You Have Just Invented

**Score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale.**

## Build Every Piece from the Concrete Example

Model A assigns probability 0.5 to each of three observed next tokens. Each costs about 0.693 nats; the average is 0.693. Exponentiating gives 2. The model behaves as if it were choosing among two equally plausible options at each step.

### Give Short Names Only After We Know the Pieces

The token count divides total surprise so longer sentences are comparable. Negative logs turn small assigned probabilities into large costs. Exponentiation reverses the log and returns the result to a probability-like choice scale.

Only now can we compress the exact procedure:

$$
\operatorname{PPL}=\exp\left(-\frac{1}{n}\sum_{i=1}^{n}\log p(t_i\mid t_{<i})\right)
$$

## Real-World Limit

Lower perplexity measures better next-token probability on this data, not truthfulness, usefulness, safety, or reasoning.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 047](../047-evaluation/README.md)
