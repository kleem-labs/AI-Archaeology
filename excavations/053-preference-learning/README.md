# Excavation 053 — Preference Learning — When Several Answers Are Correct but Not Equally Helpful

Instruction tuning turns continuation into cooperation on demonstrated tasks. Several answers can obey the same instruction while differing sharply in clarity, honesty, safety, and usefulness.

An obvious shortcut is to write one perfect target response for every prompt and train only to imitate it.

That confidence lasts only until many answers can be valid. A single target penalizes harmless alternatives and cannot express that answer A is preferred to B without being the only possible answer.

That failure tells us to collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy.

## The arithmetic we have earned

For “How do I reset my router?”, answer A gives three safe ordered steps; answer B gives twenty vague paragraphs. A reviewer chooses A. Repeated comparisons teach concision and usefulness without declaring one exact sentence mandatory.

### Only now do the symbols earn names

The reward scores two responses to the same prompt. Their difference matters, not the absolute score. The logistic function turns that difference into a preference probability; larger positive differences favor the chosen answer.

Only now can we compress the exact procedure:

$$
P(A\succ B)=\frac{1}{1+\exp(-(r_A-r_B))}
$$

## The boundary of the discovery

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
