# Excavation 038 — Position — Why Order Must Enter the Model

<!-- book-prose-v2 -->

An embedding table gives every token a learned starting description. The sentences “dog bites man” and “man bites dog” still contain the same three descriptions, so the machine cannot tell who did what.

Nothing yet appears to demand a new invention. We can sort tokens by ID or trust their array slot without exposing it to the model.

There is a real principle behind this restraint: the complexity of position must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The decisive test is this: the first invents arbitrary order; the second stores position outside the computation.

That distinction is the hinge on which position turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: add a position-specific vector to each token vector before attention. Content says what; position says where.

We have earned the chapter's shorter name: **Position**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that position is necessary rather than decorative. Delete its new responsibility and use the earlier plan to sort tokens by ID or trust their array slot without exposing it to the model.. Immediately, the first invents arbitrary order; the second stores position outside the computation. Reintroduce the single job to add a position-specific vector to each token vector before attention. Content says what; position says where. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can add a position-specific vector to each token vector before attention. Content says what; position says where. Because the old plan to sort tokens by ID or trust their array slot without exposing it to the model. is the only displaced piece, the reader can locate exactly where position changes the outcome.

## The calculation hidden inside position

Do not read the coming Position line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

A fixed learned table cannot extend beyond trained positions, and absolute location is not always the relationship language needs.

Compare “tiger chases deer” with “deer chases tiger.” The same three word cards appear, so content alone cannot distinguish hunter from hunted. Give the first slot one reusable position mark, the second another, and the third another. Adding the appropriate mark to each word leaves *tiger* recognizable while also telling later attention whether this occurrence came first or last.

### Names for pieces we have already used

**token_i** is the vocabulary address appearing at sequence location i.
**E[token_i]** retrieves what that token currently represents.
**P_i** represents where the occurrence sits.
Addition is possible because both vectors share width and is necessary so every later operation receives content and position together.
**z_i** is the combined input at position i.

### Why no cheaper operation does the same job

[Addition](../../MATHEMATICAL_MOVES.md#addition) overlays the token's learned content and this occurrence's position while keeping the vector width unchanged. Concatenation would widen every later layer and keep the two sources permanently separate.
[The shared index i](../../MATHEMATICAL_MOVES.md#indices) forces the token and position from the same slot to meet; mismatched indices would attach the wrong location.

The notation is finally shorter than the story that created it:

$$
z_i=E[token_i]+P_i
$$

The equation arrives after every operation has a job.

## Position beyond this one case

Seat numbers do not describe passengers, but they preserve who sat where.

## Take position to the workbench

Understanding position now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running position, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the position result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 039](../039-causal-mask/README.md)
