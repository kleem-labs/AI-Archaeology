# Excavation 182 — Data Provenance — Keep the Path Back to Every Source

<!-- book-prose-v2 -->

Quality filtering produces an accepted set and a rejected set. Without a trace through each transformation, neither set can explain how a source document reached its decision.

Nothing yet appears to demand a new invention. We can save only the final cleaned text because intermediate metadata costs storage.

There is a real principle behind this restraint: the complexity of data provenance must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The decisive test is this: a rights request, filtering bug, or benchmark contamination report arrives, but the final shard cannot be mapped back to the source record or processing rule that produced it.

That distinction is the hinge on which data provenance turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: assign stable document identities and record a lineage edge for every fetch, normalization, filter, redaction, deduplication group, and output shard.

We have earned the chapter's shorter name: **Data Provenance**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that data provenance is necessary rather than decorative. Delete its new responsibility and use the earlier plan to save only the final cleaned text because intermediate metadata costs storage. Immediately, a rights request, filtering bug, or benchmark contamination report arrives, but the final shard cannot be mapped back to the source record or processing rule that produced it. Reintroduce the single job to assign stable document identities and record a lineage edge for every fetch, normalization, filter, redaction, deduplication group, and output shard. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can assign stable document identities and record a lineage edge for every fetch, normalization, filter, redaction, deduplication group, and output shard. Because the old plan to save only the final cleaned text because intermediate metadata costs storage is the only displaced piece, the reader can locate exactly where data provenance changes the outcome.

## Keep the Path Back to Every Source

Document `river-0042` points to its source URL, retrieval time, raw hash, language decision, duplicate cluster, quality audit, redaction record, and final shard offset.

The name data provenance is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

## Where data provenance runs out

Provenance makes decisions inspectable; it cannot repair a source that was collected without sufficient rights, consent, or context.

The weakness is not an accidental footnote. Every operation in data provenance serves the narrower purpose to assign stable document identities and record a lineage edge for every fetch, normalization, filter, redaction, deduplication group, and output shard; none was designed to answer the new question. We have reached the honest edge of the invention.

## Take data provenance to the workbench

Understanding data provenance now means predicting its intermediate results before asking software for an answer. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running data provenance, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the data provenance result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: PII Redaction — Do Not Turn Accidental Secrets into Lessons](../183-pii-redaction/README.md)
