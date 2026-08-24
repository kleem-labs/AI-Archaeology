# Excavation 186 — The Token Budget — Convert a Training Plan into a Count of Lessons

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Information Theory](../../MATHEMATICS_ATLAS.md#information)
>
> **Applied territory:** Data and pretraining operations

Seeded mixture sampling can produce an ordered stream. The run still says “train for a while,” so neither cost nor source exposure is bounded.

The chain-of-custody ledger at the Archive Foundry still carries the marks of the previous discovery. The archivist-engineer follows them as far as they seem willing to go: stop when the wall clock reaches an affordable date.

For a moment the mark looks complete. Then the evidence refuses to fit: faster hardware sees more tokens, interruptions see fewer, and two runs with the same calendar budget teach different amounts of evidence. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The archivist-engineer sketches the break before changing it:*

```text
observation
    │
    ▼
[stop when the wall clock reaches an…]
    │
    ╳  faster hardware sees more tokens,…
    │
    ▼
[define the run by optimization steps…]
```

The archivist-engineer lays two translucent sheets over the chain-of-custody ledger. The first is inscribed, “stop when the wall clock reaches an affordable date.” Its path ends where faster hardware sees more tokens, interruptions see fewer, and two runs with the same calendar budget teach different amounts of evidence. The second receives the same evidence but is allowed to define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute. Held to the light, the sheets separate at exactly one decision.

No one reaches for a token budget formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The archivist-engineer changes only that one responsibility: define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute. When the ink dries, the name **The Token Budget** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because faster hardware sees more tokens, interruptions see fewer, and two runs with the same calendar budget teach different amounts of evidence, while the other can define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute. That fork—not the vocabulary—is where token budget lives.

<!-- memory-film-v1:start -->
> **Memory realm 13 of 18 — [Archive Foundry](../../MEMORY_PALACE.md#realm-13)**
>
> **The question carried into this chamber:** What fails if we stop when the wall clock reaches an affordable date?

## When the chamber changes

Keep the formal name The Token Budget covered for another moment. The surviving image is enough to rebuild it.

First hold the failed picture still: The gate follows the tempting path—stop when the wall clock reaches an affordable date. Then the evidence answers: faster hardware sees more tokens, interruptions see fewer, and two runs with the same calendar budget teach different amounts of evidence.

Now let the chamber move: The archivist-engineer changes one moving part. The gate can now define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute.

The object that should remain after the terminology disappears is **the token budget gate mounted on the chain-of-custody ledger**.

> **Memory seal — The Token Budget**
>
> The Token Budget keeps the missing power: define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute.

Give the idea a bodily path: Touch the token budget gate in imagination: draw the old path in the air, stop sharply at its failure, and finish with the new motion.
<!-- memory-film-v1:end -->

## Convert a Training Plan into a Count of Lessons

A tiny run uses 2,000 updates with 32 sequences of 128 real tokens each. Every update carries 4,096 lessons, so the complete plan exposes 8,192,000 tokens.

## The calculation hidden inside the token budget

The archivist-engineer carries the token budget scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

T is the planned number of optimizer updates, B_tokens counts real loss-bearing tokens in one global batch, and N_tokens is the complete exposure budget.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) appears because every one of T updates consumes B_tokens lessons. Addition would count only one update plus one batch. Padding is excluded because it occupies hardware but contributes no language target.

Three old motions cast new shadows here: **the lock and key**—one influence matters through another, and either missing factor can close the path. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Every mark needed for token budget is now visible on the chain-of-custody ledger. The symbols do not add an idea; they bind the discovered moves into one line:

$$
N_{\text{tokens}}=T B_{\text{tokens}}
$$

## Where the token budget runs out

Equal token counts do not imply equal compute when model size, sequence length, sparsity, or hardware efficiency differs.

At the Archive Foundry, the archivist-engineer leaves a blank beneath the new mark. Token Budget has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the chain-of-custody ledger

Rebuild the token budget scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Compute-Optimal Allocation — Buy a Larger Memory or More Experience?](../187-compute-optimal-allocation/README.md)
