# Excavation 046 — Perplexity — How Surprised Is the Model?

> **PART V — MAKING ANSWERS USEFUL**
>
> A machine that speaks is not necessarily a machine that knows, helps, or deserves belief.


[Previous: Excavation 045](../045-tiny-gpt/README.md)

Two tiny language models produce fluent-looking text. Which one consistently assigns better probabilities to real held-out sentences?

A reasonable place to begin is: Count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree.

Now place that proposal under pressure: Use the held-out sentence “the tiger sleeps.” Model A assigns the observed tokens probabilities 0.5, 0.5, and 0.5; Model B assigns 0.9, 0.1, and 0.9. A few attractive samples cannot expose B’s severe surprise at the middle token. What information did the attempt lose? Write that requirement before continuing.

What broke tells us what the replacement must preserve: Score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale.

## Build each piece from what just happened

Model A assigns probability 0.5 to each of three observed next tokens. Each costs about 0.693 nats; the average is 0.693. Exponentiating gives 2. The model behaves as if it were choosing among two equally plausible options at each step.

### Give Short Names Only After We Know the Pieces

The token count divides total surprise so longer sentences are comparable. Negative logs turn small assigned probabilities into large costs. Exponentiation reverses the log and returns the result to a probability-like choice scale.

Only now can we compress the exact procedure:

$$
\mathrm{PPL}=\exp\left(-\frac{1}{n}\sum_{i=1}^{n}\log p(t_i\mid t_{<i})\right)
$$

## Where your new idea still breaks

Lower perplexity measures better next-token probability on this data, not truthfulness, usefulness, safety, or reasoning.

The repair is explicit: score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale. Its power is also its boundary; anything not represented in those operations remains undecided.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 047](../047-evaluation/README.md)
