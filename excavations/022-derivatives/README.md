# Excavation 022 — Derivatives — Asking One Weight What It Changed

<!-- book-prose-v2 -->

Cross-entropy turns the model's misplaced confidence into one loss. One number can announce that the whole machine is wrong, but it cannot yet tell any particular weight whether moving up or down would help.

We can postpone invention if we simply try a large jump and keep it if loss falls.

If the proposal works on every relevant case, derivatives is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The decisive test is this: large jumps can leap over improvements. Try every possible value; there are infinitely many.

Nothing magical creates derivatives. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: nudge the weight by a tiny amount, observe the change in loss, and divide change in loss by change in weight. Then imagine the nudge shrinking toward zero.

This boundary between the failed rule and its repair is the subject later work calls **Derivatives**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize derivatives; try to break it by subtraction. Remove the part that knows how to nudge the weight by a tiny amount, observe the change in loss, and divide change in loss by change in weight. Then imagine the nudge shrinking toward zero, leaving only the attempt to try a large jump and keep it if loss falls.. What returns is not a vague weakness but the original contradiction: large jumps can leap over improvements. Try every possible value; there are infinitely many. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to try a large jump and keep it if loss falls. receives the same test as the rule to nudge the weight by a tiny amount, observe the change in loss, and divide change in loss by change in weight. Then imagine the nudge shrinking toward zero. Their different outcomes reveal what derivatives contributes without asking the reader to trust historical convention.

## The calculation hidden inside derivatives

Do not read the coming Derivatives line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

A village adjusts one alarm dial controlling how much smoke is needed before ringing a bell. At setting 3 the false-alarm cost is 9. Raising the dial by only 0.001 changes the cost to about 9.006001. The extra cost divided by the tiny dial movement is about 6. Repeating with ever smaller movements reveals the local sensitivity at the current setting rather than the effect of one arbitrary jump.

### Names for pieces we have already used

**w** is the one weight whose responsibility we are probing.
**ε** is a small experimental nudge.
**L(w+ε)−L(w)** measures the loss change caused by that nudge.
Dividing by ε turns total change into change per unit of weight.
The limit shrinks the nudge so the answer becomes local rather than dependent on an arbitrary test step.
**dL/dw** names that local sensitivity.

### Why no cheaper operation does the same job

[The numerator subtracts](../../MATHEMATICAL_MOVES.md#subtraction) old loss from nudged loss to isolate what the nudge changed; adding them would mix level with change.
[Division by the weight nudge](../../MATHEMATICAL_MOVES.md#division) converts raw loss change into loss change **per unit of weight change**, making different probe sizes comparable.
[The limit](../../MATHEMATICAL_MOVES.md#limit) lets the probe approach zero so curvature across a large jump does not disguise the local slope; setting ε equal to zero directly would divide by zero.

The notation is finally shorter than the story that created it:

$$
\frac{dL}{dw}=\lim_{\epsilon\to0}\frac{L(w+\epsilon)-L(w)}{\epsilon}
$$

## Derivatives beyond this one case

A derivative is a local slope on a mountain trail: it says which direction rises and how sharply, only near the current step.

## Where derivatives runs out

A derivative is local advice. Curved landscapes can change direction, flatten, or hide better valleys elsewhere.

This is where derivatives runs out for a causal reason. We gave it enough structure to nudge the weight by a tiny amount, observe the change in loss, and divide change in loss by change in weight. Then imagine the nudge shrinking toward zero, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

## Take derivatives to the workbench

A mathematical story about derivatives earns trust only when the failed and repaired paths can both be reproduced. Build the wrong idea first, break it, then use [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running derivatives, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the derivatives result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
