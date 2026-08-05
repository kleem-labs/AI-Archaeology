# Excavation 048 — Hallucination — When Fluent Prediction Outruns Evidence

[Previous: Excavation 047](../047-evaluation/README.md)

## Take the First Step Yourself

> **Your problem:** Asked for a paper that does not exist, the model confidently invents a title, authors, and journal.

> **Try your first idea:** Trust fluent language because uncertainty should sound hesitant.

> **Now try to break your idea:** Training rewards plausible continuations. A fabricated citation can match the shape of real citations and therefore sound more natural than “I do not know.”

> Stop here. State what the repair must accomplish in ordinary language. Do not name a standard technique.

## The Observation

Asked for a paper that does not exist, the model confidently invents a title, authors, and journal.

## Your First Attempt

Trust fluent language because uncertainty should sound hesitant.

## Break Your First Attempt

Training rewards plausible continuations. A fabricated citation can match the shape of real citations and therefore sound more natural than “I do not know.”

What information did the attempt lose? Write that requirement before continuing.

## Repair Your Attempt

Separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source.

## What You Have Just Invented

**Separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source.**

## Rebuild the Discovery with a Concrete Case

The prompt asks for the 2018 paper “Tiger Attention Networks.” Search returns no matching source. A supported system must say no source was found instead of completing the familiar citation pattern.

No new equation is needed here. The invention is a procedure and a separation of responsibilities, so forcing symbols into the chapter would hide rather than clarify it.

## Real-World Limit

Evidence reduces unsupported claims but sources can be wrong, stale, conflicting, or misread.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 049](../049-calibration/README.md)
