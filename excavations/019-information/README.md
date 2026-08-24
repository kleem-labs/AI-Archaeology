# Excavation 019 — Information — Why Surprise Needs a Number

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Information Theory](../../MATHEMATICS_ATLAS.md#information) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Learning from uncertainty and error

Likelihood ranks hidden stories against the evidence in front of us. Yet two clues can favor the same story by very different amounts, and the trackers need to know how much each clue actually taught them.

Night gathers around the Lantern Observatory. Under the light of the ring of glass lanterns, the keeper of uncertain stories refuses to invent prematurely and begins with the plain rule: measure information by message length.

The rule survives the easy cases. The next case leaves a crack through the middle of it: a long predictable greeting can contain less news than one unexpected word. Use raw surprise such as one divided by probability, but independent surprises then multiply instead of add. More confidence cannot repair information that never entered the rule.

*The keeper of uncertain stories sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ measure information by message length ──▶ blurred: a long predictable greeting can…
      │
      └── new lens ──▶ we need rare events to carry more… ──▶ distinction survives
```

Two trails now cross the ring of glass lanterns. The pale trail bears the instruction “measure information by message length.” It disappears into the observed failure: a long predictable greeting can contain less news than one unexpected word. Use raw surprise such as one divided by probability, but independent surprises then multiply instead of add. The darker trail carries one additional capacity—to we need rare events to carry more information, certain events to carry none, and independent messages to add. The negative logarithm satisfies all three needs. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed information mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the ring of glass lanterns is altered in exactly one way: we need rare events to carry more information, certain events to carry none, and independent messages to add. The negative logarithm satisfies all three needs. Much later, people will call this territory **Information**. Here the name is only a memory of the failure it can survive.

The ring of glass lanterns has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and information looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.

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
