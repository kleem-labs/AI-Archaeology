# Excavation 124 — Adversarial Robustness

[Previous: Excavation 123](../123-federated-learning/README.md)

A tiny input change invisible to a person flips the model’s decision.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Test only natural clean examples.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* An attacker follows the model’s sensitivity into a brittle direction.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Search for worst-case permitted perturbations, train against them, and bound behavior where possible.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

Changing a few pixel values turns tiger into toaster for the model while looking unchanged to a human.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

Robustness to one threat model does not imply robustness to others.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 125](../125-open-ended-research-system/README.md)
