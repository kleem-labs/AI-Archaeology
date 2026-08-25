# Excavation 019 — Information — Why Surprise Needs a Number

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Information Theory](../../MATHEMATICS_ATLAS.md#information) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Learning from uncertainty and error

Likelihood ranks hidden stories against the evidence in front of us. Yet two clues can favor the same story by very different amounts, and the trackers need to know how much each clue actually taught them.

Inside the Lantern Observatory, the old method is given an honest chance. The keeper of uncertain stories places the evidence on the ring of glass lanterns and tries to measure information by message length.

Nothing about this first move is careless. To measure information by message length is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: a long predictable greeting can contain less news than one unexpected word. Use raw surprise such as one divided by probability, but independent surprises then multiply instead of add.

The important discovery is not merely that trying to measure information by message length failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the ring of glass lanterns, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to rare events to carry more information, certain events to carry none, and independent messages to add. The negative logarithm satisfies all three needs. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Information**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## The calculation hidden inside information

The keeper of uncertain stories carries the information scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

An event with probability 1/2 carries 1 bit because -log₂(1/2)=1. An event with probability 1/8 carries 3 bits. The rarer observation eliminates more alternatives, so it teaches more.

### Naming what is already on the table

**P(x)** measures how expected observation x was.
The logarithm is needed because independent probabilities multiply while information from independent messages should add.
Probabilities below one have negative logs, so the minus sign makes information nonnegative.
A certain event has P=1 and therefore zero information; rarer events receive more.

### Why the melody needs these exact notes

[The logarithm](../../MATHEMATICAL_MOVES.md#logarithm) is forced because independent probabilities multiply while learned information should accumulate by addition. It converts a product of probabilities into a sum of surprises.
[The negative sign](../../MATHEMATICAL_MOVES.md#negative-sign) reverses the negative log of probabilities below one, making rare events carry larger positive information and a certain event carry zero.
Using 1/P would also grow for rare events, but its independent surprises would multiply rather than add; that is why it fails the job we established.

The symbols are about to change costume, but their work has appeared before: **the spiral stair**—compounded chances become steps that can be accumulated; and **the turning wind**—an uphill quantity is made to point downhill, or surprise is made to count as cost. This is how distant excavations begin to sound like variations of one melody.

The keeper of uncertain stories reads the journey of information once more across the ring of glass lanterns, then lets the words contract without losing their order:

$$
I(x)=-\log P(x)
$$

## Information beyond this one case

A locked door code is informative because many alternatives were possible. Learning that a two-sided coin landed on some side is less informative.

## Where information runs out

Information depends on the probability model. A surprise to one observer may be expected to another.

The ring of glass lanterns answers today's question and falls silent at the next. That silence is precise: Information was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the ring of glass lanterns

Rebuild the information scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
