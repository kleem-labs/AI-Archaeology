# Excavation 048 — Hallucination — When Fluent Prediction Outruns Evidence

Evaluation therefore begins with the job the system is supposed to perform. On that job, a disturbing failure remains: the model can produce a beautifully fluent answer even when no evidence supports it.

Perhaps we trust fluent language because uncertainty should sound hesitant.

That confidence lasts only until training rewards plausible continuations. A fabricated citation can match the shape of real citations and therefore sound more natural than “I do not know.”

Now we can see what is missing: we must separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source.

## Let the case decide

The prompt asks for the 2018 paper “Tiger Attention Networks.” Search returns no matching source. A supported system must say no source was found instead of completing the familiar citation pattern.

## The boundary of the discovery

Evidence reduces unsupported claims but sources can be wrong, stale, conflicting, or misread.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 049](../049-calibration/README.md)
