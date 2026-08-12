# Excavation 104 — Active Learning

An ensemble turns disagreement into evidence about model uncertainty. When labels are expensive, that disagreement can guide which unlabeled case deserves a human answer next.

One tempting answer is to label random examples forever.

The world refuses to cooperate: thousands of easy repeated cases consume effort while the decision boundary remains unclear.

Now we can see what is missing: we must ask for labels where the model is uncertain or where examples add new coverage.

## Let the case decide

The model knows obvious cats and dogs but splits 50–50 on one fox-like animal; labeling it teaches more than another obvious cat.

## The boundary of the discovery

Uncertainty sampling can chase noise or outliers.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 105](../105-selective-prediction/README.md)
