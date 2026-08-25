# Excavation 023 — The Chain Rule — Following One Change Through Many Machines

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Calculus & Differential Change](../../MATHEMATICS_ATLAS.md#calculus) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Learning from uncertainty and error

A derivative can question one weight when its effect on loss is direct. Inside the network, that weight first changes a hidden signal, then a score, then a probability, and only then the loss.

Inside the Lantern Observatory, the old method is given an honest chance. The keeper of uncertain stories places the evidence on the ring of glass lanterns and tries to measure only the first effect or only the final effect.

Nothing about this first move is careless. To measure only the first effect or only the final effect is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: either breaks the causal path. Recompute the whole network separately for every weight; that repeats enormous amounts of work.

The important discovery is not merely that trying to measure only the first effect or only the final effect failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the ring of glass lanterns, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to multiply local sensitivities along the causal path. Each stage tells how strongly it passes a small change onward. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **The Chain Rule**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## The calculation hidden inside the chain rule

The keeper of uncertain stories carries the chain rule scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Turn an oven knob slightly. The first mechanism doubles that movement into a fuel change; the next triples the fuel change into temperature; the bread-loss rule magnifies the temperature error fourfold. A one-unit knob change therefore becomes 2, then 6, then 24 units of final sensitivity. Each machine contributes one local multiplier, and the whole causal path requires all of them.

### Naming what is already on the table

**w→x→y→L** is the causal path through successive machines.
Each fraction is one local sensitivity: how its output changes when its input changes.
Multiplication is forced because a change is scaled at every link it traverses.
The product gives the effect of w on L without pretending they touch directly.

### Why the melody needs these exact notes

Each [derivative](../../MATHEMATICAL_MOVES.md#derivative) is a local conversion rate: loss per y, y per x, and x per weight.
[Multiplying the rates](../../MATHEMATICAL_MOVES.md#multiplication) is forced because one unit of weight change produces dx/dw units of x, each produces dy/dx units of y, and each of those produces dL/dy loss. Adding would mix rates with incompatible units.

The calculation reuses familiar motions: **the whispered question**—the present slope answers how a tiny movement would alter the outcome; and **the lock and key**—one influence matters through another, and either missing factor can close the path. Together they keep the path from the concrete case to notation intact.

The ring of glass lanterns already contains the complete chain rule mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
\frac{dL}{dw}=\frac{dL}{dy}\frac{dy}{dx}\frac{dx}{dw}
$$

## The Chain Rule beyond this one case

A line of gears passes motion onward. To know the final turn from the first gear, combine the ratio contributed by every contact.

## Where the chain rule runs out

Branches require sensitivities from every downstream path to be added, not merely one chain followed.

Here the new path ends honestly. Chain Rule can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the ring of glass lanterns

Rebuild the chain rule scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
