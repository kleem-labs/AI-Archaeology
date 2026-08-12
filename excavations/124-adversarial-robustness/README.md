# Excavation 124 — Adversarial Robustness

Federated learning moves computation to distributed data. Model updates and inputs remain vulnerable to malicious or tiny perturbations that preserve human meaning while flipping machine behavior.

Using what we have, we test only natural clean examples.

The world refuses to cooperate: an attacker follows the model’s sensitivity into a brittle direction.

Now we can see what is missing: we must search for worst-case permitted perturbations, train against them, and bound behavior where possible.

## Let the case decide

Changing a few pixel values turns tiger into toaster for the model while looking unchanged to a human.

## The boundary of the discovery

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
