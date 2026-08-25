# Excavation 046 — Perplexity — How Surprised Is the Model?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Information Theory](../../MATHEMATICS_ATLAS.md#information) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Language models and useful answers

> **PART V — MAKING ANSWERS USEFUL**
>
> A machine that speaks is not necessarily a machine that knows, helps, or deserves belief.

The loop closes and the tiny GPT produces fluent-looking text. Fluency is easy to admire and hard to compare, so two trained models still need a common test on text neither was allowed to study.

A new case arrives at the Hall of Voices. Nothing yet demands a new invention, so the public archivist uses the listening table to count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree.

This is precisely the kind of shortcut a careful builder should try first. The instruction to count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: the held-out sentence “the tiger sleeps” reveals the weakness. Model A assigns the observed tokens probabilities 0.5, 0.5, and 0.5; Model B assigns 0.9, 0.1, and 0.9. A few attractive samples cannot expose B’s severe surprise at the middle token.

The counterexample separates two questions that the attempt to count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the listening table fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Perplexity**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## The calculation hidden inside perplexity

The public archivist carries the perplexity scene to the listening table. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Model A assigns probability 0.5 to each of three observed next tokens. Each costs about 0.693 nats; the average is 0.693. Exponentiating gives 2. The model behaves as if it were choosing among two equally plausible options at each step.

### Naming what is already on the table

The token count divides total surprise so longer sentences are comparable. Negative logs turn small assigned probabilities into large costs. Exponentiation reverses the log and returns the result to a probability-like choice scale.

### Why the melody needs these exact notes

[The log](../../MATHEMATICAL_MOVES.md#logarithm) converts the product of many observed-token probabilities into additive surprise, avoiding a tiny unstable product for a long sentence.
[Summing](../../MATHEMATICAL_MOVES.md#summation) collects surprise from every actual next token, and [dividing by n](../../MATHEMATICAL_MOVES.md#division) makes sentences of different lengths comparable per token.
[The minus sign](../../MATHEMATICAL_MOVES.md#negative-sign) makes low probabilities costly; [the final exponential](../../MATHEMATICAL_MOVES.md#exponential) reverses the log scale so the answer reads like an equivalent number of equally likely choices.

The mandala has curved back upon itself. In this chamber we meet **the spiral stair**—compounded chances become steps that can be accumulated; **the chorus**—many witnesses contribute to one answer without one silence erasing the rest; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. What seemed like a new formula is older mathematical instinct arranged around a new need.

Every mark in the coming perplexity equation now belongs to a visible part of the case. The compressed form is:

$$
\mathrm{PPL}=\exp\left(-\frac{1}{n}\sum_{i=1}^{n}\log p(t_i\mid t_{<i})\right)
$$

## Where perplexity runs out

Lower perplexity measures better next-token probability on this data, not truthfulness, usefulness, safety, or reasoning.

The perplexity repair holds, but the world asks for something it was never given. At the Hall of Voices, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the listening table

Rebuild the perplexity scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 047](../047-evaluation/README.md)
