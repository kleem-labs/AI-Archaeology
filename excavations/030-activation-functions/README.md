# Excavation 030 — Activation Functions — Why a Network Must Bend

<!-- book-prose-v2 -->

Careful initialization keeps early signals alive and breaks symmetry. But a tower made only from linear transformations still collapses algebraically into one linear transformation, no matter how many layers we stack.

The obvious economy is to add more linear layers.

The proposal deserves a fair hearing. For activation functions, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The decisive test is this: depth increases, but expressive power does not. Use a hard yes-or-no threshold; it creates decisions but supplies almost no useful gradient.

The failure changes the question behind activation functions. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: place an activation after a linear transformation. ReLU opens positive paths; smoother gates such as GELU vary them gradually.

Only at this point does the inherited name **Activation Functions** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of activation functions by mentally removing the repair. We fall back to the proposal to add more linear layers.; then depth increases, but expressive power does not. Use a hard yes-or-no threshold; it creates decisions but supplies almost no useful gradient. Restore only the ability to place an activation after a linear transformation. ReLU opens positive paths; smoother gates such as GELU vary them gradually, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to add more linear layers. to requiring the system to place an activation after a linear transformation. ReLU opens positive paths; smoother gates such as GELU vary them gradually. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to activation functions.

## The calculation hidden inside activation functions

Do not read the coming Activation Functions line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

The repair solves the immediate failure, but every activation has tradeoffs: dead ReLUs, saturation, computational cost, or assumptions about input scale.

A gatekeeper receives a danger signal. Two ordinary scaling rules—double it, then triple it—always behave like one rule that multiplies by six. Adding more such rules has created no new decision. Put a gate between them: negative evidence is closed to zero while positive evidence continues. Now the same machinery treats warning evidence and reassuring evidence differently, something one multiplication cannot reproduce.

### Names for pieces we have already used

**x** is the incoming representation.
**W** mixes its features; **b** permits learned thresholds and offsets.
**φ** is the necessary nonlinear gate; without it, stacked layers collapse into one linear map.
**h** is the hidden representation after both mixing and gating.

### Why no cheaper operation does the same job

[Wx](../../MATHEMATICAL_MOVES.md#multiplication) lets every learned input weight scale and mix its matching feature; [adding b](../../MATHEMATICAL_MOVES.md#addition) supplies a learnable baseline.
[Applying φ](../../MATHEMATICAL_MOVES.md#function-application) bends the result. Without φ, repeated multiply-and-add stages remain one linear map, no matter how many layers are stacked.

The notation is finally shorter than the story that created it:

$$
h=\phi(Wx+b)
$$

## Activation Functions beyond this one case

A railway switch changes which route a signal can take. Without switches, many track segments still form only one fixed route.

## Take activation functions to the workbench

A claim about activation functions now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running activation functions, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the activation functions result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Excavation 031](../031-overfitting/README.md)
