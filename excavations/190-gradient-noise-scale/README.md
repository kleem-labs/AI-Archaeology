# Excavation 190 — Gradient Noise Scale — When More Examples Stop Buying More Direction

<!-- book-prose-v2 -->

The schedule controls how far one global update moves. We still do not know how many examples should vote in that update before extra devices mostly repeat the same directional evidence.

We can postpone invention if we simply make the global batch as large as the cluster permits.

If the proposal works on every relevant case, gradient noise scale is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The decisive test is this: early doubling reduces disagreement and improves the direction, but beyond a workload-dependent point the averaged gradient barely changes while each update consumes twice as many tokens.

Nothing magical creates gradient noise scale. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: measure disagreement among micro-batch gradients relative to the strength of their shared direction, and use that noise scale as evidence for the largest useful batch rather than a hardware target.

This boundary between the failed rule and its repair is the subject later work calls **Gradient Noise Scale**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize gradient noise scale; try to break it by subtraction. Remove the part that knows how to measure disagreement among micro-batch gradients relative to the strength of their shared direction, and use that noise scale as evidence for the largest useful batch rather than a hardware target, leaving only the attempt to make the global batch as large as the cluster permits. What returns is not a vague weakness but the original contradiction: early doubling reduces disagreement and improves the direction, but beyond a workload-dependent point the averaged gradient barely changes while each update consumes twice as many tokens. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to make the global batch as large as the cluster permits receives the same test as the rule to measure disagreement among micro-batch gradients relative to the strength of their shared direction, and use that noise scale as evidence for the largest useful batch rather than a hardware target. Their different outcomes reveal what gradient noise scale contributes without asking the reader to trust historical convention.

## When More Examples Stop Buying More Direction

Three named micro-batches question the same two weights: the field reports propose [2.0,1.0], science proposes [2.1,0.9], and books propose [1.9,1.1]. The first number is advice to the tiger-before-river weight; the second is advice to a punctuation weight. Their mean [2.0,1.0] is strong and their disagreement around it is small. If the witnesses instead propose [4,−2], [0,4], and [2,1], disagreement is large relative to the same broad direction, so a larger batch can still buy useful certainty.

Hold the setting, evidence, and desired outcome fixed while testing gradient noise scale. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

## The calculation hidden inside gradient noise scale

Do not read the coming Gradient Noise Scale line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Each g_i is one model micro-batch's gradient advice. The covariance measures how those witnesses disagree; its trace totals disagreement across coordinates. The squared norm of their mean measures the strength of the shared direction; G compares noise with signal.

### Why no cheaper operation does the same job

[Covariance](../../MATHEMATICAL_MOVES.md#covariance) keeps variation around the common advice rather than raw gradient size. [Trace](../../MATHEMATICAL_MOVES.md#trace) gathers coordinate variances without inventing cross-coordinate units. [Division](../../MATHEMATICAL_MOVES.md#division) asks disagreement per unit of squared shared direction; subtraction would not remove dependence on signal scale.

Every symbol in Gradient Noise Scale can now be read back into an action already performed. The whole procedure fits in one line:

$$
G=\frac{\mathrm{tr}(\mathrm{Cov}[g_i])}{\lVert E[g_i]\rVert^2}
$$

## Where gradient noise scale runs out

Gradient noise scale is an empirical guide, not a universal batch-size law; it changes during training and with the task and optimizer.

This is where gradient noise scale runs out for a causal reason. We gave it enough structure to measure disagreement among micro-batch gradients relative to the strength of their shared direction, and use that noise scale as evidence for the largest useful batch rather than a hardware target, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

## Take gradient noise scale to the workbench

A mathematical story about gradient noise scale earns trust only when the failed and repaired paths can both be reproduced. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running gradient noise scale, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the gradient noise scale result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Data Parallelism — Let Several Workers Observe Different Evidence](../191-data-parallelism/README.md)
