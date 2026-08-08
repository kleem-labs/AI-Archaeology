# Excavation 101 — Two Kinds of Uncertainty

> **PART X — LEARNING WHAT WE STILL DO NOT KNOW**
>
> The complete system now meets the frontier: ignorance, changing tasks, causal questions, proofs, attacks, and open-ended research.


[Previous: Excavation 100](../100-complete-ai-system/README.md)

The model is unsure whether a blurry animal is a tiger. Is the image ambiguous, or has the model never seen this species?

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Represent every uncertainty with one low confidence number.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* A clearer image can repair blur, but not missing knowledge; more training data can repair missing knowledge, but not a genuinely coin-flip outcome.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Separate uncertainty in the observation from uncertainty in the model’s knowledge.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

A foggy known tiger remains ambiguous even for an expert; a clear pangolin confuses a tiger-only learner for a different reason.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

The two sources interact and are difficult to estimate perfectly.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 102](../102-bayesian-updating/README.md)
