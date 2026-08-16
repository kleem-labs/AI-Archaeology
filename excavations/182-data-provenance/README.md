# Excavation 182 — Data Provenance — Keep the Path Back to Every Source

Quality filtering produces an accepted set and a rejected set. Without a trace through each transformation, neither set can explain how a source document reached its decision.

Perhaps we save only the final cleaned text because intermediate metadata costs storage.

But the run answers back. A rights request, filtering bug, or benchmark contamination report arrives, but the final shard cannot be mapped back to the source record or processing rule that produced it.

The failure leaves one precise requirement. Assign stable document identities and record a lineage edge for every fetch, normalization, filter, redaction, deduplication group, and output shard.

## Let one run decide

Document `river-0042` points to its source URL, retrieval time, raw hash, language decision, duplicate cluster, quality audit, redaction record, and final shard offset.

## What this repair cannot do

Provenance makes decisions inspectable; it cannot repair a source that was collected without sufficient rights, consent, or context.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: PII Redaction — Do Not Turn Accidental Secrets into Lessons](../183-pii-redaction/README.md)
