# Excavation 182 — Data Provenance — Keep the Path Back to Every Source

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Data and pretraining operations

Quality filtering produces an accepted set and a rejected set. Without a trace through each transformation, neither set can explain how a source document reached its decision.

The doors of the Archive Foundry close against the wind. On the chain-of-custody ledger, the archivist-engineer writes the cheapest rule that might still be true: save only the final cleaned text because intermediate metadata costs storage.

Reality answers without terminology: a rights request, filtering bug, or benchmark contamination report arrives, but the final shard cannot be mapped back to the source record or processing rule that produced it. The chain-of-custody ledger now holds two situations the old rule cannot keep apart.

*The archivist-engineer sketches the break before changing it:*

```text
OLD PATH:  request ──▶ save only the final cleaned text… ──▶ a rights request, filtering bug, or…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ assign stable document identities and… ──▶ accountable result
```

The chain-of-custody ledger is divided down the middle. Left side: “save only the final cleaned text because intermediate metadata costs storage.” Its final mark records a rights request, filtering bug, or benchmark contamination report arrives, but the final shard cannot be mapped back to the source record or processing rule that produced it. Right side: the same starting evidence, now allowed to assign stable document identities and record a lineage edge for every fetch, normalization, filter, redaction, deduplication group, and output shard. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given data provenance a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: assign stable document identities and record a lineage edge for every fetch, normalization, filter, redaction, deduplication group, and output shard. The name **Data Provenance** arrives afterward, like a title given to a path whose stones are already underfoot.

A thread now runs backward from data provenance through the room. Tug it and the repair disappears; tug again and the old rule returns; follow that rule to its end and a rights request, filtering bug, or benchmark contamination report arrives, but the final shard cannot be mapped back to the source record or processing rule that produced it. The mathematics is not a collection of names but a chain of consequences that can be walked in either direction.

## Keep the Path Back to Every Source

Document `river-0042` points to its source URL, retrieval time, raw hash, language decision, duplicate cluster, quality audit, redaction record, and final shard offset.

## Where data provenance runs out

Provenance makes decisions inspectable; it cannot repair a source that was collected without sufficient rights, consent, or context.

A final test reaches beyond the new instrument. It does not refute Data Provenance; it reveals the edge of what was constructed. The archivist-engineer carries that edge into the following room.

## Return to the chain-of-custody ledger

Rebuild the data provenance scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: PII Redaction — Do Not Turn Accidental Secrets into Lessons](../183-pii-redaction/README.md)
