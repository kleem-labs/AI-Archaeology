# Excavation 124 — Adversarial Robustness

[Previous: Excavation 123](../123-federated-learning/README.md)

A tiny input change invisible to a person flips the model’s decision.

Our first construction is deliberately modest: Test only natural clean examples.

It works—right up to this boundary: An attacker follows the model’s sensitivity into a brittle direction.

Crossing that boundary requires one additional idea: Search for worst-case permitted perturbations, train against them, and bound behavior where possible.

## Now work a case you can see

Changing a few pixel values turns tiger into toaster for the model while looking unchanged to a human.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

Robustness to one threat model does not imply robustness to others.

Why does the boundary remain? Our new machinery only knows how to search for worst-case permitted perturbations, train against them, and bound behavior where possible. Solving that problem does not automatically solve every decision built on top of it.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 125](../125-open-ended-research-system/README.md)
