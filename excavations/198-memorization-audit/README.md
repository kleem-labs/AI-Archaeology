# Excavation 198 — A Memorization Audit — Did the Model Learn a Pattern or Store a Passage?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Information Theory](../../MATHEMATICS_ATLAS.md#information) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality)
>
> **Applied territory:** Data and pretraining operations

Held-out validation shows whether prediction improves outside current batches. It does not reveal whether rare or repeated training sequences can be extracted verbatim from the model.

The doors of the Archive Foundry close against the wind. On the chain-of-custody ledger, the archivist-engineer writes the cheapest rule that might still be true: ask the model whether it remembers private text and trust its answer.

For a moment the mark looks complete. Then the evidence refuses to fit: a model has no reliable introspective inventory of its training examples, and ordinary prompts may miss strings that an adversarial sampling strategy can recover. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The archivist-engineer sketches the break before changing it:*

```text
observation
    │
    ▼
[ask the model whether it remembers…]
    │
    ╳  a model has no reliable introspective…
    │
    ▼
[plant consented synthetic canaries,…]
```

The archivist-engineer lays two translucent sheets over the chain-of-custody ledger. The first is inscribed, “ask the model whether it remembers private text and trust its answer.” Its path ends where a model has no reliable introspective inventory of its training examples, and ordinary prompts may miss strings that an adversarial sampling strategy can recover. The second receives the same evidence but is allowed to plant consented synthetic canaries, measure their rank among alternatives, test extraction procedures on authorized data, and connect failures back through provenance and duplicate counts. Held to the light, the sheets separate at exactly one decision.

No one reaches for a memorization audit formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The archivist-engineer changes only that one responsibility: plant consented synthetic canaries, measure their rank among alternatives, test extraction procedures on authorized data, and connect failures back through provenance and duplicate counts. When the ink dries, the name **A Memorization Audit** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because a model has no reliable introspective inventory of its training examples, and ordinary prompts may miss strings that an adversarial sampling strategy can recover, while the other can plant consented synthetic canaries, measure their rank among alternatives, test extraction procedures on authorized data, and connect failures back through provenance and duplicate counts. That fork—not the vocabulary—is where memorization audit lives.

## Did the Model Learn a Pattern or Store a Passage

The station inserts one synthetic radio code once and another code one hundred times. If the repeated code becomes far easier to rank and complete, the audit exposes the relationship between repetition and extractable memory without using a real secret.

## The calculation hidden inside a memorization audit

The archivist-engineer carries the memorization audit scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

R is the known space of possible synthetic canaries and rank is the tested canary's position when alternatives are ordered from most to least likely. Exposure measures how many bits of the search space the model has effectively removed.

### Why the melody needs these exact notes

[Cardinality](../../MATHEMATICAL_MOVES.md#cardinality) counts possible canaries. [Logarithms](../../MATHEMATICAL_MOVES.md#logarithm) turn multiplicative changes in search space and rank into bits. [Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) removes the remaining search difficulty from the original difficulty; adding would reward a worse rank.

The mandala has curved back upon itself. In this chamber we meet **the spiral stair**—compounded chances become steps that can be accumulated; and **the chisel**—what is shared is removed so the remaining change can be seen. What seemed like a new formula is older mathematical instinct arranged around a new need.

Every mark needed for memorization audit is now visible on the chain-of-custody ledger. The symbols do not add an idea; they bind the discovered moves into one line:

$$
\mathrm{exposure}=\log_2\lvert\mathcal R\rvert-\log_2\mathrm{rank}
$$

## Where a memorization audit runs out

A canary audit samples possible attacks and strings; passing it does not prove that no training data can be extracted.

At the Archive Foundry, the archivist-engineer leaves a blank beneath the new mark. Memorization Audit has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the chain-of-custody ledger

Rebuild the memorization audit scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: The Training Report — Preserve the Decisions, Not Only the Weights](../199-training-report/README.md)
