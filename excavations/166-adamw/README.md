# Excavation 166 — AdamW — Keep Shrinkage Separate from Adaptation

<!-- book-prose-v2 -->

Adam trains the block, but adding an L2 penalty to the loss sends shrinkage through the optimizer's coordinate-wise rescaling.

We can postpone invention if we simply treat penalty gradients and data gradients identically because both appear in one total loss.

If the proposal works on every relevant case, adamw is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The decisive test is this: coordinates with different gradient histories receive different effective shrinkage even when the intended rule was to decay all selected weights at one rate.

Nothing magical creates adamw. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: apply Adam's adaptive data update and parameter decay as separate operations.

This boundary between the failed rule and its repair is the subject later work calls **AdamW**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize adamw; try to break it by subtraction. Remove the part that knows how to apply Adam's adaptive data update and parameter decay as separate operations, leaving only the attempt to treat penalty gradients and data gradients identically because both appear in one total loss. What returns is not a vague weakness but the original contradiction: coordinates with different gradient histories receive different effective shrinkage even when the intended rule was to decay all selected weights at one rate. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to treat penalty gradients and data gradients identically because both appear in one total loss receives the same test as the rule to apply Adam's adaptive data update and parameter decay as separate operations. Their different outcomes reveal what adamw contributes without asking the reader to trust historical convention.

## Keep Shrinkage Separate from Adaptation

Two equal weights with different gradient histories receive different Adam steps but the same proportional decay.

Hold the setting, evidence, and desired outcome fixed while testing adamw. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

## The calculation hidden inside adamw

Do not read the coming AdamW line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Suppose two weights both equal 2, although their gradient histories differ. If decay means 'remove one tenth of one percent of the present weight this step,' both should lose the same proportion before their evidence-driven Adam movements differ. Multiplying theta by 1−eta lambda performs that direct shrink. The separate subtraction then applies Adam's learned direction, preventing gradient history from secretly changing the intended decay rule.

lambda is decay strength; the first term shrinks the old parameter directly; the second is Adam's data-driven update.

### Why no cheaper operation does the same job

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) by 1−eta lambda makes decay proportional to current parameter size: a zero weight stays zero and doubling a weight doubles shrinkage. [Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) then applies the independently adapted loss step. Hiding decay inside m and v would mix two jobs the formula deliberately separates.

Every symbol in AdamW can now be read back into an action already performed. The whole procedure fits in one line:

$$
\theta_{t+1}=(1-\eta\lambda)\theta_t-\eta\frac{\widehat m_t}{\sqrt{\widehat v_t}+\epsilon}
$$

## Where adamw runs out

Decoupled decay still requires choosing which parameters to decay and how strongly.

This is where adamw runs out for a causal reason. We gave it enough structure to apply Adam's adaptive data update and parameter decay as separate operations, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

## Take adamw to the workbench

A mathematical story about adamw earns trust only when the failed and repaired paths can both be reproduced. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running adamw, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the adamw result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Gradient Clipping — Stop One Shock from Becoming a Catastrophe](../167-gradient-clipping/README.md)
