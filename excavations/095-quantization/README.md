# Excavation 095 — Quantization

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Low-rank adaptation learns a small correction while preserving the base model. The unchanged base weights still consume memory and arithmetic every time the adapted model answers.

Inside the Road of Consequences, the old method is given an honest chance. The expedition leader places the evidence on the map of branching journeys and tries to round every weight aggressively without measuring effect.

Nothing about this first move is careless. To round every weight aggressively without measuring effect is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: small but important distinctions disappear and outputs degrade.

The important discovery is not merely that trying to round every weight aggressively without measuring effect failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the map of branching journeys, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to map values to a limited set of levels using calibrated scale and test sensitive layers. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Quantization**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## Understanding quantization

Weights from -1 to 1 become 256 integer levels; a stored integer plus scale approximately reconstructs each value.

## The calculation hidden inside quantization

The expedition leader carries the quantization scene to the map of branching journeys. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Suppose one learned weight is `0.73`, but the device can store only integer steps of size `0.10`. Dividing by the step size says the weight is 7.3 steps; rounding stores integer 7. During computation, multiplying 7 by `0.10` reconstructs `0.70`. The device has traded an error of `0.03` for cheaper storage and arithmetic. The scale decides which real differences survive.

Real weight w is divided by scale s to express it in integer-sized steps.
Rounding chooses the nearest allowed integer q.
Multiplying q by s reconstructs the approximate weight used in computation.
The scale is calibrated so important values fit the available integer range.

### Why the melody needs these exact notes

[Dividing by scale s](../../MATHEMATICAL_MOVES.md#division) expresses a real weight in units of one quantization step.
[Rounding](../../MATHEMATICAL_MOVES.md#rounding) chooses the nearest integer level because storage permits only discrete codes; this is the deliberate lossy step.
[Multiplying q by s](../../MATHEMATICAL_MOVES.md#multiplication) converts the stored step count back to the weight's approximate real scale. [The hat on w](../../MATHEMATICAL_MOVES.md#symbol-decorations) marks this reconstructed approximation; addition would shift levels rather than restore their unit size.

The calculation reuses familiar motions: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large; and **the lock and key**—one influence matters through another, and either missing factor can close the path. Together they keep the path from the concrete case to notation intact.

The map of branching journeys already contains the complete quantization mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
q=\mathrm{round}(w/s)
$$

$$
\widehat w=sq
$$

## Where quantization runs out

Lower precision trades accuracy for efficiency and hardware support varies.

Here the new path ends honestly. Quantization can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the map of branching journeys

Rebuild the quantization scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 096](../096-distributed-training/README.md)
