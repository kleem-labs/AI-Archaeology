# Excavation 198 — A Memorization Audit — Did the Model Learn a Pattern or Store a Passage?

Held-out validation shows whether prediction improves outside current batches. It does not reveal whether rare or repeated training sequences can be extracted verbatim from the model.

Using what we have, we ask the model whether it remembers private text and trust its answer.

The plan survives only until the evidence is counted. A model has no reliable introspective inventory of its training examples, and ordinary prompts may miss strings that an adversarial sampling strategy can recover.

The lost information tells us what must come next. Plant consented synthetic canaries, measure their rank among alternatives, test extraction procedures on authorized data, and connect failures back through provenance and duplicate counts.

## Let one run decide

The station inserts one synthetic radio code once and another code one hundred times. If the repeated code becomes far easier to rank and complete, the audit exposes the relationship between repetition and extractable memory without using a real secret.

## The arithmetic we have earned

R is the known space of possible synthetic canaries and rank is the tested canary's position when alternatives are ordered from most to least likely. Exposure measures how many bits of the search space the model has effectively removed.

### Why these operations are forced

[Cardinality](../../MATHEMATICAL_MOVES.md#cardinality) counts possible canaries. [Logarithms](../../MATHEMATICAL_MOVES.md#logarithm) turn multiplicative changes in search space and rank into bits. [Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) removes the remaining search difficulty from the original difficulty; adding would reward a worse rank.

Only now can we compress the procedure:

$$
\mathrm{exposure}=\log_2\lvert\mathcal R\rvert-\log_2\mathrm{rank}
$$

## What this repair cannot do

A canary audit samples possible attacks and strings; passing it does not prove that no training data can be extracted.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: The Training Report — Preserve the Decisions, Not Only the Weights](../199-training-report/README.md)
