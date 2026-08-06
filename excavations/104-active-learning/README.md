# Excavation 104 — Active Learning

[Previous: Excavation 103](../103-ensembles/README.md)

## Take the First Step Yourself

> **Your problem:** Labeling one example is expensive. Which unlabeled case should a human inspect next?

> **Try your first idea:** Label random examples forever.

> **Now try to break your idea:** Thousands of easy repeated cases consume effort while the decision boundary remains unclear.

> Stop here. State the missing requirement without naming the repair.

## The Observation

Labeling one example is expensive. Which unlabeled case should a human inspect next?

## Your First Attempt

Label random examples forever.

## Break Your First Attempt

Thousands of easy repeated cases consume effort while the decision boundary remains unclear.

## Repair Your Attempt

Ask for labels where the model is uncertain or where examples add new coverage.

## What You Have Just Invented

**Ask for labels where the model is uncertain or where examples add new coverage.**

## Rebuild the Discovery with a Concrete Case

The model knows obvious cats and dogs but splits 50–50 on one fox-like animal; labeling it teaches more than another obvious cat.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Real-World Limit

Uncertainty sampling can chase noise or outliers.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 105](../105-selective-prediction/README.md)
