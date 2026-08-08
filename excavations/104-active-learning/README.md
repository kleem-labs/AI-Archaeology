# Excavation 104 — Active Learning

[Previous: Excavation 103](../103-ensembles/README.md)

Labeling one example is expensive. Which unlabeled case should a human inspect next?

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Label random examples forever.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Thousands of easy repeated cases consume effort while the decision boundary remains unclear.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Ask for labels where the model is uncertain or where examples add new coverage.

Only after that reasoning may we give your discovery its inherited name.

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
