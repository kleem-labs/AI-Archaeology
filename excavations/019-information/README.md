# Excavation 019 — Information — Why Surprise Needs a Number

<!-- book-prose-v2 -->

Likelihood ranks hidden stories against the evidence in front of us. Yet two clues can favor the same story by very different amounts, and the trackers need to know how much each clue actually taught them.

Before naming anything new, try to measure information by message length.

Its appeal is not ignorance but economy. Information should not be added until an observation exposes the exact thing the older procedure cannot preserve.

Then a case arrives in which convenience and truth separate: a long predictable greeting can contain less news than one unexpected word. Use raw surprise such as one divided by probability, but independent surprises then multiply instead of add.

Notice what the counterexample has accomplished for information. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: we need rare events to carry more information, certain events to carry none, and independent messages to add. The negative logarithm satisfies all three needs.

Humanity eventually gathered this problem and its repairs under the name **Information**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace information with the old instruction to measure information by message length.. The result is again that a long predictable greeting can contain less news than one unexpected word. Use raw surprise such as one divided by probability, but independent surprises then multiply instead of add. Put back only the requirement to we need rare events to carry more information, certain events to carry none, and independent messages to add. The negative logarithm satisfies all three needs. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when information is introduced. The same evidence that defeated the attempt to measure information by message length. is presented again. Only the ability to we need rare events to carry more information, certain events to carry none, and independent messages to add. The negative logarithm satisfies all three needs changes, so the repaired conclusion cannot be credited to a conveniently different example.

## The calculation hidden inside information

Before Information receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

An event with probability 1/2 carries 1 bit because -log₂(1/2)=1. An event with probability 1/8 carries 3 bits. The rarer observation eliminates more alternatives, so it teaches more.

### Names for pieces we have already used

**P(x)** measures how expected observation x was.
The logarithm is needed because independent probabilities multiply while information from independent messages should add.
Probabilities below one have negative logs, so the minus sign makes information nonnegative.
A certain event has P=1 and therefore zero information; rarer events receive more.

### Why no cheaper operation does the same job

[The logarithm](../../MATHEMATICAL_MOVES.md#logarithm) is forced because independent probabilities multiply while learned information should accumulate by addition. It converts a product of probabilities into a sum of surprises.
[The negative sign](../../MATHEMATICAL_MOVES.md#negative-sign) reverses the negative log of probabilities below one, making rare events carry larger positive information and a certain event carry zero.
Using 1/P would also grow for rare events, but its independent surprises would multiply rather than add; that is why it fails the job we established.

The notation is finally shorter than the story that created it:

$$
I(x)=-\log P(x)
$$

## Information beyond this one case

A locked door code is informative because many alternatives were possible. Learning that a two-sided coin landed on some side is less informative.

## Where information runs out

Information depends on the probability model. A surprise to one observer may be expected to another.

Why does that boundary remain? Information was built for one responsibility: we need rare events to carry more information, certain events to carry none, and independent messages to add. The negative logarithm satisfies all three needs. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take information to the workbench

The argument for information is still provisional until a runnable case can make it fail. Build the wrong idea first, break it, then use [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running information, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the information result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
