# Excavation 108 — Meta-Learning

[Previous: Excavation 107](../107-continual-learning/README.md)

Can experience across many tasks teach the model how to learn a new task quickly?

At first, the simplest answer is tempting: Train one universal fixed solution.

But the simplicity has discarded something important: A new task with different labels requires many examples and broad retraining.

The missing information determines the next move: Optimize prior parameters or an update rule so a few new examples produce useful adaptation.

## Now work a case you can see

After many two-class tasks, five labeled examples are enough to separate two unseen animal species.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

Task distributions can be narrow and meta-learning can overfit them.

The reason is visible in the procedure. It knows how to optimize prior parameters or an update rule so a few new examples produce useful adaptation. The limitation above asks for another judgment, and no part of the procedure makes that judgment.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 109](../109-curriculum-learning/README.md)
