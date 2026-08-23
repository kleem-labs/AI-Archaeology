# Excavation 023 — The Chain Rule — Following One Change Through Many Machines

<!-- book-prose-v2 -->

A derivative can question one weight when its effect on loss is direct. Inside the network, that weight first changes a hidden signal, then a score, then a probability, and only then the loss.

The previous discovery seems almost sufficient: we could measure only the first effect or only the final effect.

The shortcut appears to retain everything the chain rule needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

One counterexample is enough to expose the missing job: either breaks the causal path. Recompute the whole network separately for every weight; that repeats enormous amounts of work.

The counterexample teaches the chain rule. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: we need to multiply local sensitivities along the causal path. Each stage tells how strongly it passes a small change onward.

Now—and not earlier—we may introduce **The Chain Rule**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to measure only the first effect or only the final effect., and the case answers that either breaks the causal path. Recompute the whole network separately for every weight; that repeats enormous amounts of work. With the narrow repair—to we need to multiply local sensitivities along the causal path. Each stage tells how strongly it passes a small change onward—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. The Chain Rule returns to the same counterexample, replaces the attempt to measure only the first effect or only the final effect. with the responsibility to we need to multiply local sensitivities along the causal path. Each stage tells how strongly it passes a small change onward, and must succeed where the shortcut failed.

## The calculation hidden inside the chain rule

Before The Chain Rule receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Turn an oven knob slightly. The first mechanism doubles that movement into a fuel change; the next triples the fuel change into temperature; the bread-loss rule magnifies the temperature error fourfold. A one-unit knob change therefore becomes 2, then 6, then 24 units of final sensitivity. Each machine contributes one local multiplier, and the whole causal path requires all of them.

### Names for pieces we have already used

**w→x→y→L** is the causal path through successive machines.
Each fraction is one local sensitivity: how its output changes when its input changes.
Multiplication is forced because a change is scaled at every link it traverses.
The product gives the effect of w on L without pretending they touch directly.

### Why no cheaper operation does the same job

Each [derivative](../../MATHEMATICAL_MOVES.md#derivative) is a local conversion rate: loss per y, y per x, and x per weight.
[Multiplying the rates](../../MATHEMATICAL_MOVES.md#multiplication) is forced because one unit of weight change produces dx/dw units of x, each produces dy/dx units of y, and each of those produces dL/dy loss. Adding would mix rates with incompatible units.

The notation is finally shorter than the story that created it:

$$
\frac{dL}{dw}=\frac{dL}{dy}\frac{dy}{dx}\frac{dx}{dw}
$$

## The Chain Rule beyond this one case

A line of gears passes motion onward. To know the final turn from the first gear, combine the ratio contributed by every contact.

## Where the chain rule runs out

Branches require sensitivities from every downstream path to be added, not merely one chain followed.

The boundary can be predicted from the construction itself. The Chain Rule performs the repair to we need to multiply local sensitivities along the causal path. Each stage tells how strongly it passes a small change onward; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

## Take the chain rule to the workbench

Move the chain rule from imagination to evidence by making the shortcut fail under controlled inputs. Build the wrong idea first, break it, then use [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running the chain rule, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the the chain rule result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
