# Excavation 179 — Exact Deduplication — Stop Paying Twice for the Same Document

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Language labels make the intended corpus measurable. Counting the accepted files now reveals identical reports mirrored across archives and repeated under new filenames.

Night gathers around the Archive Foundry. Under the light of the chain-of-custody ledger, the archivist-engineer refuses to invent prematurely and begins with the plain rule: leave duplicates in place because more training examples should always help.

At the edge of the chain-of-custody ledger, the shortcut produces its consequence: one press release copied to a thousand sites receives a thousand votes, while a rare field observation receives one. Compute is spent memorizing repetition rather than encountering new evidence. That consequence, not a textbook, earns the next move.

*The archivist-engineer sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: leave duplicates in place because…
                         │
                         └── mismatch: one press release copied to a…

reference evidence ──▶ measured repair: normalize only irrelevant formatting,…
```

The archivist-engineer covers the new mark and the old contradiction returns: one press release copied to a thousand sites receives a thousand votes, while a rare field observation receives one. Compute is spent memorizing repetition rather than encountering new evidence. The cover is lifted, restoring the ability to normalize only irrelevant formatting, hash the resulting document, and keep one accountable representative for each identical hash while preserving duplicate counts in the ledger, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason exact deduplication exists.

What must change for exact deduplication is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: normalize only irrelevant formatting, hash the resulting document, and keep one accountable representative for each identical hash while preserving duplicate counts in the ledger. That threshold is where **Exact Deduplication** enters the story.

The marks on the chain-of-custody ledger form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. exact deduplication is not any single point. It is the path connecting them in the only order that makes the last point necessary.

## Stop Paying Twice for the Same Document

Three files differ only in line endings and trailing spaces. After recorded normalization they produce the same fingerprint, so one enters training and the manifest records three original locations.

## The calculation hidden inside exact deduplication

The archivist-engineer carries the exact deduplication scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

d is the original tiger field-report document, N performs the recorded normalization, H is a deterministic content-hash function, and h(d) is the fingerprint used to group exact copies.

### Why the melody needs these exact notes

[Function composition](../../MATHEMATICAL_MOVES.md#function-composition) fixes the order: normalize first, hash second. Reversing the order leaves irrelevant byte differences visible. [Equality](../../MATHEMATICAL_MOVES.md#equals) groups only matching fingerprints; adding hashes has no interpretation and would not identify copies.

The chain-of-custody ledger already contains the complete exact deduplication mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
h(d)=H(N(d))
$$

## Where exact deduplication runs out

Because a cryptographic hash reacts to any retained content change, exact hashes catch identical normalized text but give a copied article with one inserted advertisement a different fingerprint.

Here the new path ends honestly. Exact Deduplication can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the chain-of-custody ledger

Rebuild the exact deduplication scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Near Deduplication — When a Copy Changes a Few Words](../180-near-deduplication/README.md)
