# Excavation 052 — Instruction Tuning — From Continuation to Cooperation

[Previous: Excavation 051](../051-scaling-laws/README.md)

## Take the First Step Yourself

> **Your problem:** A pretrained model continues text well but may continue a question instead of answering it.

> **Try your first idea:** Prompt more forcefully and hope next-token prediction infers the desired interaction.

> **Now try to break your idea:** Given “Translate cat to French,” raw continuation may produce more translation examples, commentary, or unrelated web text. Pretraining learned many formats, not one cooperative policy.

> Stop here. State what the repair must accomplish in ordinary language. Do not name a standard technique.

## The Observation

A pretrained model continues text well but may continue a question instead of answering it.

## Your First Attempt

Prompt more forcefully and hope next-token prediction infers the desired interaction.

## Break Your First Attempt

Given “Translate cat to French,” raw continuation may produce more translation examples, commentary, or unrelated web text. Pretraining learned many formats, not one cooperative policy.

What information did the attempt lose? Write that requirement before continuing.

## Repair Your Attempt

Show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern.

## What You Have Just Invented

**Show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern.**

## Rebuild the Discovery with a Concrete Case

Training examples pair “Summarize: [paragraph]” with a concise summary and “Classify sentiment: [review]” with a label. A new instruction can reuse the demonstrated relation between request and response.

No new equation is needed here. The invention is a procedure and a separation of responsibilities, so forcing symbols into the chapter would hide rather than clarify it.

## Real-World Limit

Instruction tuning teaches behavioral patterns from its examples; it does not guarantee truth, safety, or correct obedience to every request.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 053](../053-preference-learning/README.md)
