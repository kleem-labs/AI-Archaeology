# Excavation 104 — Active Learning

[Previous: Excavation 103](../103-ensembles/README.md)

Labeling one example is expensive. Which unlabeled case should a human inspect next?

Our first construction is deliberately modest: Label random examples forever.

It works—right up to this boundary: Thousands of easy repeated cases consume effort while the decision boundary remains unclear.

Crossing that boundary requires one additional idea: Ask for labels where the model is uncertain or where examples add new coverage.

## Now work a case you can see

The model knows obvious cats and dogs but splits 50–50 on one fox-like animal; labeling it teaches more than another obvious cat.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

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
