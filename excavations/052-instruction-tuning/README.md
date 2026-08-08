# Excavation 052 — Instruction Tuning — From Continuation to Cooperation

[Previous: Excavation 051](../051-scaling-laws/README.md)

A pretrained model continues text well but may continue a question instead of answering it.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Prompt more forcefully and hope next-token prediction infers the desired interaction.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Given “Translate cat to French,” raw continuation may produce more translation examples, commentary, or unrelated web text. Pretraining learned many formats, not one cooperative policy.

What information did the attempt lose? Write that requirement before continuing.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

Training examples pair “Summarize: [paragraph]” with a concise summary and “Classify sentiment: [review]” with a label. A new instruction can reuse the demonstrated relation between request and response.

No new equation is needed here. The invention is a procedure and a separation of responsibilities, so forcing symbols into the chapter would hide rather than clarify it.

## Where your new idea still breaks

Instruction tuning teaches behavioral patterns from its examples; it does not guarantee truth, safety, or correct obedience to every request.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 053](../053-preference-learning/README.md)
