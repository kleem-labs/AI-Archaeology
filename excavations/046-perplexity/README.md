# Excavation 046 — Perplexity — How Surprised Is the Model?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Information Theory](../../MATHEMATICS_ATLAS.md#information) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Language models and useful answers

> **PART V — MAKING ANSWERS USEFUL**
>
> A machine that speaks is not necessarily a machine that knows, helps, or deserves belief.

The loop closes and the tiny GPT produces fluent-looking text. Fluency is easy to admire and hard to compare, so two trained models still need a common test on text neither was allowed to study.

The doors of the Hall of Voices close against the wind. On the listening table, the public archivist writes the cheapest rule that might still be true: count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree.

The public archivist repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: the held-out sentence “the tiger sleeps” reveals the weakness. Model A assigns the observed tokens probabilities 0.5, 0.5, and 0.5; Model B assigns 0.9, 0.1, and 0.9. A few attractive samples cannot expose B’s severe surprise at the middle token. The failure is stable enough to become evidence.

*The public archivist sketches the break before changing it:*

```text
OLD PATH:  request ──▶ count how many generated sentences… ──▶ the held-out sentence “the tiger…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ score the probability assigned to… ──▶ accountable result
```

Across the listening table, the old path and the repaired path run side by side. One carries “count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree”; the other knows how to score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale. When the failure—the held-out sentence “the tiger sleeps” reveals the weakness. Model A assigns the observed tokens probabilities 0.5, 0.5, and 0.5; Model B assigns 0.9, 0.1, and 0.9. A few attractive samples cannot expose B’s severe surprise at the middle token—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to perplexity. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale. This problem and its repair will travel under the name **Perplexity**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree? The answer remains the held-out sentence “the tiger sleeps” reveals the weakness. Model A assigns the observed tokens probabilities 0.5, 0.5, and 0.5; Model B assigns 0.9, 0.1, and 0.9. A few attractive samples cannot expose B’s severe surprise at the middle token. The new construction earns its permanence by answering that old question without pretending it was foolish to ask. In the Hall of Voices, perplexity inherits the mathematics of honest comparison: measure on the same evidence, separate memory from observation, and preserve uncertainty until a source can resolve it. Fluent words do not repeal those older obligations.

<!-- memory-film-v1:start -->
> **Memory realm 5 of 18 — [Hall of Voices](../../MEMORY_PALACE.md#realm-5)**
>
> **The question carried into this chamber:** How Surprised Is the Model?

## When the chamber changes

Keep the formal name Perplexity covered for another moment. The surviving image is enough to rebuild it.

First hold the failed picture still: The gear follows the tempting path—count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree. Then the evidence answers: the held-out sentence “the tiger sleeps” reveals the weakness. Model A assigns the observed tokens probabilities 0.5, 0.5, and 0.5; Model B assigns 0.9, 0.1, and 0.9. A few attractive samples cannot expose B’s severe surprise at the middle token.

Now let the chamber move: The public archivist changes one moving part. The gear can now score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale.

The object that should remain after the terminology disappears is **the perplexity gear mounted on the listening table**.

> **Memory seal — Perplexity**
>
> Perplexity keeps the missing power: score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale.

Give the idea a bodily path: Touch the perplexity gear in imagination: make a narrow gate with both hands, block the old path, then open only the route the evidence permits.
<!-- memory-film-v1:end -->

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

Cover the prose about perplexity and each mark can still be recovered from the case. Only now is the compressed form safe to write:

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
