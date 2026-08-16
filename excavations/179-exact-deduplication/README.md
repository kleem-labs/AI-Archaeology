# Excavation 179 — Exact Deduplication — Stop Paying Twice for the Same Document

Language labels make the intended corpus measurable. Counting the accepted files now reveals identical reports mirrored across archives and repeated under new filenames.

At first we leave duplicates in place because more training examples should always help.

Reality objects. One press release copied to a thousand sites receives a thousand votes, while a rare field observation receives one. Compute is spent memorizing repetition rather than encountering new evidence.

That evidence forces a repair. Normalize only irrelevant formatting, hash the resulting document, and keep one accountable representative for each identical hash while preserving duplicate counts in the ledger.

## Let one run decide

Three files differ only in line endings and trailing spaces. After recorded normalization they produce the same fingerprint, so one enters training and the manifest records three original locations.

## The arithmetic we have earned

d is the original tiger field-report document, N performs the recorded normalization, H is a deterministic content-hash function, and h(d) is the fingerprint used to group exact copies.

### Why these operations are forced

[Function composition](../../MATHEMATICAL_MOVES.md#function-composition) fixes the order: normalize first, hash second. Reversing the order leaves irrelevant byte differences visible. [Equality](../../MATHEMATICAL_MOVES.md#equals) groups only matching fingerprints; adding hashes has no interpretation and would not identify copies.

Only now can we compress the procedure:

$$
h(d)=H(N(d))
$$

## What this repair cannot do

Because a cryptographic hash reacts to any retained content change, exact hashes catch identical normalized text but give a copied article with one inserted advertisement a different fingerprint.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Near Deduplication — When a Copy Changes a Few Words](../180-near-deduplication/README.md)
