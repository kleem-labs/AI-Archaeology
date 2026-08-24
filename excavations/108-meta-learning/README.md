# Excavation 108 — Meta-Learning

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Continual learning protects the past but may still require many examples for every genuinely new task. Experience across tasks could teach not only solutions, but a better procedure for adapting quickly.

Inside the Hall of Possible Worlds, every old tool is given one honest chance. The keeper of unfinished questions sets the table of mirrored maps between the evidence and the desired answer, then tries to train one universal fixed solution.

For a moment the mark looks complete. Then the evidence refuses to fit: a new task with different labels requires many examples and broad retraining. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The keeper of unfinished questions sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ train one universal fixed solution ──▶ blurred: a new task with different labels…
      │
      └── new lens ──▶ optimize prior parameters or an… ──▶ distinction survives
```

The keeper of unfinished questions lays two translucent sheets over the table of mirrored maps. The first is inscribed, “train one universal fixed solution.” Its path ends where a new task with different labels requires many examples and broad retraining. The second receives the same evidence but is allowed to optimize prior parameters or an update rule so a few new examples produce useful adaptation. Held to the light, the sheets separate at exactly one decision.

No one reaches for a meta-learning formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The keeper of unfinished questions changes only that one responsibility: optimize prior parameters or an update rule so a few new examples produce useful adaptation. When the ink dries, the name **Meta-Learning** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The table of mirrored maps keeps both histories. Its older mark still says, ‘train one universal fixed solution’; beside it, the newer mark says, ‘optimize prior parameters or an update rule so a few new examples produce useful adaptation.’ The distance between those sentences is the exact shape of meta-learning: no larger than the failure required, and no smaller than reality permits.

## Understanding meta-learning

After many two-class tasks, five labeled examples are enough to separate two unseen animal species.

## Where meta-learning runs out

Task distributions can be narrow and meta-learning can overfit them.

At the Hall of Possible Worlds, the keeper of unfinished questions leaves a blank beneath the new mark. Meta-Learning has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the table of mirrored maps

Rebuild the meta-learning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 109](../109-curriculum-learning/README.md)
