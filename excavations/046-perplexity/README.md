# Excavation 046 — Perplexity — How Surprised Is the Model?

<!-- book-prose-v2 -->

> **PART V — MAKING ANSWERS USEFUL**
>
> A machine that speaks is not necessarily a machine that knows, helps, or deserves belief.

The loop closes and the tiny GPT produces fluent-looking text. Fluency is easy to admire and hard to compare, so two trained models still need a common test on text neither was allowed to study.

We can postpone invention if we simply count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree.

If the proposal works on every relevant case, perplexity is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The decisive test is this: the held-out sentence “the tiger sleeps” reveals the weakness. Model A assigns the observed tokens probabilities 0.5, 0.5, and 0.5; Model B assigns 0.9, 0.1, and 0.9. A few attractive samples cannot expose B’s severe surprise at the middle token.

Nothing magical creates perplexity. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale.

This boundary between the failed rule and its repair is the subject later work calls **Perplexity**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize perplexity; try to break it by subtraction. Remove the part that knows how to score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale, leaving only the attempt to count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree. What returns is not a vague weakness but the original contradiction: the held-out sentence “the tiger sleeps” reveals the weakness. Model A assigns the observed tokens probabilities 0.5, 0.5, and 0.5; Model B assigns 0.9, 0.1, and 0.9. A few attractive samples cannot expose B’s severe surprise at the middle token. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to count how many generated sentences sound good. The sample is small, decoding choices interfere, and two people may disagree receives the same test as the rule to score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale. Their different outcomes reveal what perplexity contributes without asking the reader to trust historical convention.

## The calculation hidden inside perplexity

Do not read the coming Perplexity line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Model A assigns probability 0.5 to each of three observed next tokens. Each costs about 0.693 nats; the average is 0.693. Exponentiating gives 2. The model behaves as if it were choosing among two equally plausible options at each step.

### Names for pieces we have already used

The token count divides total surprise so longer sentences are comparable. Negative logs turn small assigned probabilities into large costs. Exponentiation reverses the log and returns the result to a probability-like choice scale.

### Why no cheaper operation does the same job

[The log](../../MATHEMATICAL_MOVES.md#logarithm) converts the product of many observed-token probabilities into additive surprise, avoiding a tiny unstable product for a long sentence.
[Summing](../../MATHEMATICAL_MOVES.md#summation) collects surprise from every actual next token, and [dividing by n](../../MATHEMATICAL_MOVES.md#division) makes sentences of different lengths comparable per token.
[The minus sign](../../MATHEMATICAL_MOVES.md#negative-sign) makes low probabilities costly; [the final exponential](../../MATHEMATICAL_MOVES.md#exponential) reverses the log scale so the answer reads like an equivalent number of equally likely choices.

Every symbol in Perplexity can now be read back into an action already performed. The whole procedure fits in one line:

$$
\mathrm{PPL}=\exp\left(-\frac{1}{n}\sum_{i=1}^{n}\log p(t_i\mid t_{<i})\right)
$$

## Where perplexity runs out

Lower perplexity measures better next-token probability on this data, not truthfulness, usefulness, safety, or reasoning.

This is where perplexity runs out for a causal reason. We gave it enough structure to score the probability assigned to every actual next token, combine those costs, and convert the average back into an intuitive “equally likely choices” scale, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

## Take perplexity to the workbench

A mathematical story about perplexity earns trust only when the failed and repaired paths can both be reproduced. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running perplexity, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the perplexity result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 047](../047-evaluation/README.md)
