# Excavation 188 — Learning-Rate Warmup — Let Adam Learn the Terrain Before Running

<!-- book-prose-v2 -->

Compute allocation chooses the model and token horizon. At the first update, Adam's moment memories contain almost no history, while randomly initialized activations and gradients are changing fastest.

The first defensible move is to begin immediately at the peak learning rate chosen for the stable middle of training.

There is a real principle behind this restraint: the complexity of learning-rate warmup must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The proposal breaks for a specific reason, not by authority: the first noisy batches can make large updates before the optimizer's scale estimates become trustworthy, producing a loss spike that the later stable rate would not have caused.

That distinction is the hinge on which learning-rate warmup turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: increase the learning rate gradually from zero or a small value during a recorded warmup interval, then hand control to the main schedule.

We have earned the chapter's shorter name: **Learning-Rate Warmup**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that learning-rate warmup is necessary rather than decorative. Delete its new responsibility and use the earlier plan to begin immediately at the peak learning rate chosen for the stable middle of training. Immediately, the first noisy batches can make large updates before the optimizer's scale estimates become trustworthy, producing a loss spike that the later stable rate would not have caused. Reintroduce the single job to increase the learning rate gradually from zero or a small value during a recorded warmup interval, then hand control to the main schedule. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can increase the learning rate gradually from zero or a small value during a recorded warmup interval, then hand control to the main schedule. Because the old plan to begin immediately at the peak learning rate chosen for the stable middle of training is the only displaced piece, the reader can locate exactly where learning-rate warmup changes the outcome.

## Let Adam Learn the Terrain Before Running

With peak rate 0.001 and 100 warmup updates, update 25 receives 0.00025, update 50 receives 0.0005, and update 100 finally reaches 0.001.

The name learning-rate warmup is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

## The calculation hidden inside learning-rate warmup

Do not read the coming Learning-Rate Warmup line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

t is the current model warmup update, T_warm is the number of warmup updates, eta_peak is the intended stable rate, and eta_t is the smaller rate used now.

### Why no cheaper operation does the same job

[Division](../../MATHEMATICAL_MOVES.md#division) turns elapsed warmup steps into a progress fraction from zero to one. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) applies that fraction to the peak rate. Adding t would mix step counts with a rate; jumping directly to eta_peak recreates the failed attempt.

Every symbol in Learning-Rate Warmup can now be read back into an action already performed. The whole procedure fits in one line:

$$
\eta_t=\eta_{\text{peak}}\frac{t}{T_{\text{warm}}}\quad(0\le t\le T_{\text{warm}})
$$

## Where learning-rate warmup runs out

Warmup reduces early shock but cannot rescue an unsuitable peak rate, broken initialization, corrupt batch, or incorrect optimizer state.

The weakness is not an accidental footnote. Every operation in learning-rate warmup serves the narrower purpose to increase the learning rate gradually from zero or a small value during a recorded warmup interval, then hand control to the main schedule; none was designed to answer the new question. We have reached the honest edge of the invention.

## Take learning-rate warmup to the workbench

Understanding learning-rate warmup now means predicting its intermediate results before asking software for an answer. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running learning-rate warmup, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the learning-rate warmup result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Cosine Decay — Make Late Corrections Smaller Without a Cliff](../189-cosine-decay/README.md)
