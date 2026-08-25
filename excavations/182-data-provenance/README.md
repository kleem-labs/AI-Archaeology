# Excavation 182 — Data Provenance — Keep the Path Back to Every Source

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Data and pretraining operations

Quality filtering produces an accepted set and a rejected set. Without a trace through each transformation, neither set can explain how a source document reached its decision.

A new case arrives at the Archive Foundry. Nothing yet demands a new invention, so the archivist-engineer uses the chain-of-custody ledger to save only the final cleaned text because intermediate metadata costs storage.

This is precisely the kind of shortcut a careful builder should try first. The instruction to save only the final cleaned text because intermediate metadata costs storage preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: a rights request, filtering bug, or benchmark contamination report arrives, but the final shard cannot be mapped back to the source record or processing rule that produced it.

The counterexample separates two questions that the attempt to save only the final cleaned text because intermediate metadata costs storage had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the chain-of-custody ledger fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now assign stable document identities and record a lineage edge for every fetch, normalization, filter, redaction, deduplication group, and output shard. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Data Provenance**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## Keep the Path Back to Every Source

Document `river-0042` points to its source URL, retrieval time, raw hash, language decision, duplicate cluster, quality audit, redaction record, and final shard offset.

## Where data provenance runs out

Provenance makes decisions inspectable; it cannot repair a source that was collected without sufficient rights, consent, or context.

A final test reaches beyond the new instrument. It does not refute Data Provenance; it reveals the edge of what was constructed. The archivist-engineer carries that edge into the following room.

## Return to the chain-of-custody ledger

Rebuild the data provenance scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: PII Redaction — Do Not Turn Accidental Secrets into Lessons](../183-pii-redaction/README.md)
