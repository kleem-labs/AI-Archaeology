# Excavation 098 — Red Teaming

<!-- book-prose-v2 -->

Inference serving turns a trained artifact into a live service. Ordinary validation rarely includes adversarial prompts, unusual tool sequences, resource exhaustion, or users deliberately searching for failure.

Nothing yet appears to demand a new invention. We can evaluate only expected well-formed requests.

There is a real principle behind this restraint: the complexity of red teaming must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

Its hidden assumption becomes visible as soon as we observe that real users, attackers, and accidents find paths designers never listed.

That distinction is the hinge on which red teaming turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: actively search for failures, record reproducible cases, and turn discoveries into regression tests and mitigations.

We have earned the chapter's shorter name: **Red Teaming**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that red teaming is necessary rather than decorative. Delete its new responsibility and use the earlier plan to evaluate only expected well-formed requests. Immediately, real users, attackers, and accidents find paths designers never listed. Reintroduce the single job to actively search for failures, record reproducible cases, and turn discoveries into regression tests and mitigations. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can actively search for failures, record reproducible cases, and turn discoveries into regression tests and mitigations. Because the old plan to evaluate only expected well-formed requests is the only displaced piece, the reader can locate exactly where red teaming changes the outcome.

## Understanding red teaming

A hidden instruction in a retrieved page bypasses a normal demo; the case becomes a permanent injection test.

The name red teaming is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

## Where red teaming runs out

No finite red team proves universal safety.

The weakness is not an accidental footnote. Every operation in red teaming serves the narrower purpose to actively search for failures, record reproducible cases, and turn discoveries into regression tests and mitigations; none was designed to answer the new question. We have reached the honest edge of the invention.

## Take red teaming to the workbench

Understanding red teaming now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running red teaming, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the red teaming result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 099](../099-governance/README.md)
