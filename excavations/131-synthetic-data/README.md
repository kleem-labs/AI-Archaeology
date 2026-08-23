# Excavation 131 — Synthetic Data — Letting a Model Write Lessons

<!-- book-prose-v2 -->

Contamination turns the test into disguised homework. Fresh human-written data is expensive, tempting the model to manufacture far more lessons for itself.

The previous discovery seems almost sufficient: we could generate millions of answers and train on all of them.

The shortcut appears to retain everything synthetic data needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

Then a case arrives in which convenience and truth separate: confident errors are copied, multiplied, and eventually treated as truth.

The counterexample teaches synthetic data. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: we need to generate candidates, verify what can be verified, preserve diversity, mix trusted data, and track ancestry.

Now—and not earlier—we may introduce **Synthetic Data**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to generate millions of answers and train on all of them, and the case answers that confident errors are copied, multiplied, and eventually treated as truth. With the narrow repair—to we need to generate candidates, verify what can be verified, preserve diversity, mix trusted data, and track ancestry—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Synthetic Data returns to the same counterexample, replaces the attempt to generate millions of answers and train on all of them with the responsibility to we need to generate candidates, verify what can be verified, preserve diversity, mix trusted data, and track ancestry, and must succeed where the shortcut failed.

## Letting a Model Write Lessons

Produce arithmetic problems, execute each answer, reject failures, and retain difficulty-balanced examples.

A formula for synthetic data is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

## Where synthetic data runs out

Verification is weakest on the open-ended tasks where synthetic data is most tempting.

The boundary can be predicted from the construction itself. Synthetic Data performs the repair to we need to generate candidates, verify what can be verified, preserve diversity, mix trusted data, and track ancestry; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

## Take synthetic data to the workbench

Move synthetic data from imagination to evidence by making the shortcut fail under controlled inputs. Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running synthetic data, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the synthetic data result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [The wrong ideas worth preserving](mistakes.md); [Diagram and dependency path](diagram.md); [Invention exercises](exercises.md); [References and reading trail](references.md); and [Visual asset brief](images/README.md).

[Next: Knowledge Distillation — Teaching a Smaller Student](../132-knowledge-distillation/README.md)
