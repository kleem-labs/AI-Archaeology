# Excavation 108 — Meta-Learning

Continual learning protects the past but may still require many examples for every genuinely new task. Experience across tasks could teach not only solutions, but a better procedure for adapting quickly.

Perhaps we train one universal fixed solution.

That confidence lasts only until a new task with different labels requires many examples and broad retraining.

Now we can see what is missing: we must optimize prior parameters or an update rule so a few new examples produce useful adaptation.

## Let the case decide

After many two-class tasks, five labeled examples are enough to separate two unseen animal species.

## The boundary of the discovery

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
