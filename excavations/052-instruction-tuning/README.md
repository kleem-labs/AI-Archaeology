# Excavation 052 — Instruction Tuning — From Continuation to Cooperation

Scaling laws reveal regular trends as resources grow. A larger next-token predictor is still a predictor; nothing in scale alone tells it that a user's instruction should govern the continuation.

Using what we have, we prompt more forcefully and hope next-token prediction infers the desired interaction.

The trouble appears immediately: given “Translate cat to French,” raw continuation may produce more translation examples, commentary, or unrelated web text. Pretraining learned many formats, not one cooperative policy.

Now we can see what is missing: we must show many instruction-input-response examples and continue training so following the requested task becomes a reusable pattern.

## Let the case decide

Training examples pair “Summarize: [paragraph]” with a concise summary and “Classify sentiment: [review]” with a label. A new instruction can reuse the demonstrated relation between request and response.

## The boundary of the discovery

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
