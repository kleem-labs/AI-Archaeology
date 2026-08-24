# Excavation 176 — A Corpus Manifest — Know What Entered the Run

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Data and pretraining operations

> **PART XIII — A PRETRAINING FACTORY WE CAN ACCOUNT FOR**
>
> The engine can run. Now every document, update, shard, interruption, and release claim must leave enough evidence to reconstruct the same experiment.

The modern tiny language-model engine preserves a reference path through training and serving. It still cannot explain which documents will shape its weights, because no corpus has been frozen as part of the experiment.

At the Archive Foundry, the archivist-engineer returns to the chain-of-custody ledger. Yesterday's instrument still lies open, so the first move asks for no new magic: copy every available text file into one large folder and begin tokenizing.

Reality answers without terminology: a file is replaced upstream, another is silently skipped, and a third appears twice under different paths. The same training command now describes a different body of evidence. The chain-of-custody ledger now holds two situations the old rule cannot keep apart.

*The archivist-engineer sketches the break before changing it:*

```text
OLD PATH:  request ──▶ copy every available text file into… ──▶ a file is replaced upstream, another…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ create an immutable manifest that… ──▶ accountable result
```

The chain-of-custody ledger is divided down the middle. Left side: “copy every available text file into one large folder and begin tokenizing.” Its final mark records a file is replaced upstream, another is silently skipped, and a third appears twice under different paths. The same training command now describes a different body of evidence. Right side: the same starting evidence, now allowed to create an immutable manifest that records each source, version, content hash, license or usage basis, processing stage, and document count before any training shard exists. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given corpus manifest a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: create an immutable manifest that records each source, version, content hash, license or usage basis, processing stage, and document count before any training shard exists. The name **A Corpus Manifest** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to copy every available text file into one large folder and begin tokenizing; on the other lies the observed fact that a file is replaced upstream, another is silently skipped, and a third appears twice under different paths. The same training command now describes a different body of evidence. The bridge called corpus manifest has exactly the planks needed to create an immutable manifest that records each source, version, content hash, license or usage basis, processing stage, and document count before any training shard exists. In the Archive Foundry, corpus manifest joins mathematics to memory. Sets identify what must be present, hashes preserve identity, counts bound exposure, and arrows keep every transformation attached to its source. A model may forget its documents internally; the factory must not forget them externally.

## Know What Entered the Run

The ranger station records `field-reports/v3`, its retrieval date, 8,412 documents, and the hash of its manifest. A later run can prove whether it used the same evidence.

## Where a corpus manifest runs out

A manifest makes the corpus accountable; it cannot prove that every recorded document is suitable, lawful, accurate, or harmless.

A final test reaches beyond the new instrument. It does not refute Corpus Manifest; it reveals the edge of what was constructed. The archivist-engineer carries that edge into the following room.

## Return to the chain-of-custody ledger

Rebuild the corpus manifest scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Document Boundaries — Keep One Story from Leaking into Another](../177-document-boundaries/README.md)
