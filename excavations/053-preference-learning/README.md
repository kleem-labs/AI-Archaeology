# Excavation 053 — Preference Learning — When Several Answers Are Correct but Not Equally Helpful

[Previous: Excavation 052](../052-instruction-tuning/README.md)

Two answers are factually acceptable, but one is clearer, safer, and better aligned with the user’s intent.

At first, the simplest answer is tempting: Write one perfect target response for every prompt and train only to imitate it.

But the simplicity has discarded something important: Many answers can be valid. A single target penalizes harmless alternatives and cannot express that answer A is preferred to B without being the only possible answer. What information did the attempt lose? Write that requirement before continuing.

The missing information determines the next move: Collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy.

## Build each piece from what just happened

For “How do I reset my router?”, answer A gives three safe ordered steps; answer B gives twenty vague paragraphs. A reviewer chooses A. Repeated comparisons teach concision and usefulness without declaring one exact sentence mandatory.

### Give Short Names Only After We Know the Pieces

The reward scores two responses to the same prompt. Their difference matters, not the absolute score. The logistic function turns that difference into a preference probability; larger positive differences favor the chosen answer.

Only now can we compress the exact procedure:

$$
P(A\succ B)=\frac{1}{1+\exp(-(r_A-r_B))}
$$

## Where your new idea still breaks

Human preferences conflict, annotators make mistakes, and optimizing a learned reward can exploit its blind spots.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 054](../054-retrieval-augmented-generation/README.md)
