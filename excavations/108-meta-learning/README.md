# Excavation 108 — Meta-Learning

[Previous: Excavation 107](../107-continual-learning/README.md)

Can experience across many tasks teach the model how to learn a new task quickly?

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Train one universal fixed solution.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* A new task with different labels requires many examples and broad retraining.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Optimize prior parameters or an update rule so a few new examples produce useful adaptation.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

After many two-class tasks, five labeled examples are enough to separate two unseen animal species.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

Task distributions can be narrow and meta-learning can overfit them.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 109](../109-curriculum-learning/README.md)
