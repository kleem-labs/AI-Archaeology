# Excavation 046 — Perplexity — How Surprised Is the Model?

> **PART V — MAKING ANSWERS USEFUL**
>
> A machine that speaks is not necessarily a machine that knows, helps, or deserves belief.

The loop closes and the tiny GPT produces fluent-looking text. Fluency is easy to admire and hard to compare, so two trained models still need a common test on text neither was allowed to study.

Using what we have, we count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree.

Yet the held-out sentence “the tiger sleeps” reveals the weakness. Model A assigns the observed tokens probabilities 0.5, 0.5, and 0.5; Model B assigns 0.9, 0.1, and 0.9. A few attractive samples cannot expose B’s severe surprise at the middle token.

So we score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale.

## The arithmetic we have earned

Model A assigns probability 0.5 to each of three observed next tokens. Each costs about 0.693 nats; the average is 0.693. Exponentiating gives 2. The model behaves as if it were choosing among two equally plausible options at each step.

### Only now do the symbols earn names

The token count divides total surprise so longer sentences are comparable. Negative logs turn small assigned probabilities into large costs. Exponentiation reverses the log and returns the result to a probability-like choice scale.

Only now can we compress the exact procedure:

$$
\mathrm{PPL}=\exp\left(-\frac{1}{n}\sum_{i=1}^{n}\log p(t_i\mid t_{<i})\right)
$$

## The boundary of the discovery

Lower perplexity measures better next-token probability on this data, not truthfulness, usefulness, safety, or reasoning.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 047](../047-evaluation/README.md)
