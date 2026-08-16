# Excavation 176 — A Corpus Manifest — Know What Entered the Run

> **PART XIII — A PRETRAINING FACTORY WE CAN ACCOUNT FOR**
>
> The engine can run. Now every document, update, shard, interruption, and release claim must leave enough evidence to reconstruct the same experiment.

The modern tiny language-model engine preserves a reference path through training and serving. It still cannot explain which documents will shape its weights, because no corpus has been frozen as part of the experiment.

Perhaps we copy every available text file into one large folder and begin tokenizing.

But the run answers back. A file is replaced upstream, another is silently skipped, and a third appears twice under different paths. The same training command now describes a different body of evidence.

The failure leaves one precise requirement. Create an immutable manifest that records each source, version, content hash, license or usage basis, processing stage, and document count before any training shard exists.

## Let one run decide

The ranger station records `field-reports/v3`, its retrieval date, 8,412 documents, and the hash of its manifest. A later run can prove whether it used the same evidence.

## What this repair cannot do

A manifest makes the corpus accountable; it cannot prove that every recorded document is suitable, lawful, accurate, or harmless.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Document Boundaries — Keep One Story from Leaking into Another](../177-document-boundaries/README.md)
