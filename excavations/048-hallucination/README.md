# Excavation 048 — Hallucination — When Fluent Prediction Outruns Evidence

[Previous: Excavation 047](../047-evaluation/README.md)

Asked for a paper that does not exist, the model confidently invents a title, authors, and journal.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Trust fluent language because uncertainty should sound hesitant.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Training rewards plausible continuations. A fabricated citation can match the shape of real citations and therefore sound more natural than “I do not know.”

What information did the attempt lose? Write that requirement before continuing.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

The prompt asks for the 2018 paper “Tiger Attention Networks.” Search returns no matching source. A supported system must say no source was found instead of completing the familiar citation pattern.

No new equation is needed here. The invention is a procedure and a separation of responsibilities, so forcing symbols into the chapter would hide rather than clarify it.

## Where your new idea still breaks

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
