# Excavation 199 — The Training Report — Preserve the Decisions, Not Only the Weights

<!-- book-prose-v2 -->

Memorization auditing adds one essential limitation to the evaluation record. A released checkpoint still cannot explain its corpus, mixture, compute, interruptions, exclusions, intended uses, or known failures by inspecting weight tensors.

Before naming anything new, try to publish the final benchmark table and assume the configuration files explain the rest.

Its appeal is not ignorance but economy. The Training Report should not be added until an observation exposes the exact thing the older procedure cannot preserve.

One counterexample is enough to expose the missing job: a score has no visible data lineage, uncertainty, subgroup behavior, energy or hardware context, incident history, or warning about uses the evaluation never tested.

Notice what the counterexample has accomplished for the training report. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: generate a training report from manifests and logs, then add human-reviewed explanations of intended use, out-of-scope use, limitations, incidents, provenance, evaluation conditions, and responsible release decisions.

Humanity eventually gathered this problem and its repairs under the name **The Training Report**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace the training report with the old instruction to publish the final benchmark table and assume the configuration files explain the rest. The result is again that a score has no visible data lineage, uncertainty, subgroup behavior, energy or hardware context, incident history, or warning about uses the evaluation never tested. Put back only the requirement to generate a training report from manifests and logs, then add human-reviewed explanations of intended use, out-of-scope use, limitations, incidents, provenance, evaluation conditions, and responsible release decisions. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when the training report is introduced. The same evidence that defeated the attempt to publish the final benchmark table and assume the configuration files explain the rest is presented again. Only the ability to generate a training report from manifests and logs, then add human-reviewed explanations of intended use, out-of-scope use, limitations, incidents, provenance, evaluation conditions, and responsible release decisions changes, so the repaired conclusion cannot be credited to a conveniently different example.

## Preserve the Decisions, Not Only the Weights

The station's report names corpus and code versions, tokens seen, mixture shares, compute, checkpoint recoveries, per-domain validation, memorization probes, excluded sources, and the exact model artifact hash.

Run the the training report scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

## Where the training report runs out

Documentation improves accountability but can be incomplete, outdated, misleading, or ignored; claims still require inspectable evidence.

Why does that boundary remain? The Training Report was built for one responsibility: generate a training report from manifests and logs, then add human-reviewed explanations of intended use, out-of-scope use, limitations, incidents, provenance, evaluation conditions, and responsible release decisions. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take the training report to the workbench

The argument for the training report is still provisional until a runnable case can make it fail. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running the training report, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the the training report result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: A Tiny Pretraining Factory — Close the Accountable Training Loop](../200-tiny-pretraining-factory/README.md)
