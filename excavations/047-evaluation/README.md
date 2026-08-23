# Excavation 047 — Evaluation — What Does “Better” Actually Mean?

<!-- book-prose-v2 -->

Perplexity measures how surprised a model is by held-out language. A lower surprise does not automatically mean a safer answer, a truer claim, or a more useful assistant.

The previous discovery seems almost sufficient: we could choose one benchmark score and call it intelligence.

The shortcut appears to retain everything evaluation needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

One counterexample is enough to expose the missing job: the trouble appears immediately: a calculator can ace arithmetic while failing conversation; a fluent model can pass style tests while inventing facts. One number silently chooses which failures do not matter.

The counterexample teaches evaluation. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: we need to name the intended job, create separate tests for its required abilities and risks, and inspect real failures rather than averaging them away.

Now—and not earlier—we may introduce **Evaluation**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to choose one benchmark score and call it intelligence, and the case answers that the trouble appears immediately: a calculator can ace arithmetic while failing conversation; a fluent model can pass style tests while inventing facts. One number silently chooses which failures do not matter. With the narrow repair—to we need to name the intended job, create separate tests for its required abilities and risks, and inspect real failures rather than averaging them away—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Evaluation returns to the same counterexample, replaces the attempt to choose one benchmark score and call it intelligence with the responsibility to we need to name the intended job, create separate tests for its required abilities and risks, and inspect real failures rather than averaging them away, and must succeed where the shortcut failed.

## What Does “Better” Actually Mean

For a travel assistant, test factual date retrieval, instruction following, refusal when information is missing, citation accuracy, latency, and cost separately. A single average must not let perfect tone hide fabricated flight times.

A formula for evaluation is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

## Where evaluation runs out

Every evaluation is a model of future use. Benchmarks can leak into training and become targets rather than measurements.

The boundary can be predicted from the construction itself. Evaluation performs the repair to we need to name the intended job, create separate tests for its required abilities and risks, and inspect real failures rather than averaging them away; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

## Take evaluation to the workbench

Move evaluation from imagination to evidence by making the shortcut fail under controlled inputs. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running evaluation, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the evaluation result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 048](../048-hallucination/README.md)
