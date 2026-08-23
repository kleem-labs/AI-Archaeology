# Excavation 020 — Entropy — Measuring the Uncertainty of a Whole Situation

<!-- book-prose-v2 -->

Information gives one surprising observation a numerical weight. Before opening the next envelope, however, the community needs to compare the uncertainty of entire situations, not only the surprise of one event after it happens.

The first defensible move is to count the number of outcomes.

There is a real principle behind this restraint: the complexity of entropy must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The proposal breaks for a specific reason, not by authority: both bags contain stones, and both have two named colors if we list an absent possibility. Or inspect only the most likely outcome, losing the rest of the distribution.

That distinction is the hinge on which entropy turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: average the information of every possible outcome, weighted by how often that outcome occurs.

We have earned the chapter's shorter name: **Entropy**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that entropy is necessary rather than decorative. Delete its new responsibility and use the earlier plan to count the number of outcomes.. Immediately, both bags contain stones, and both have two named colors if we list an absent possibility. Or inspect only the most likely outcome, losing the rest of the distribution. Reintroduce the single job to average the information of every possible outcome, weighted by how often that outcome occurs. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can average the information of every possible outcome, weighted by how often that outcome occurs. Because the old plan to count the number of outcomes. is the only displaced piece, the reader can locate exactly where entropy changes the outcome.

## The calculation hidden inside entropy

Do not read the coming Entropy line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

For a fair coin, each outcome has probability 1/2 and information 1 bit. Weighting gives 0.5×1+0.5×1=1 expected bit. A coin guaranteed heads gives -log₂(1)=0, so its entropy is zero.

### Names for pieces we have already used

**pᵢ** is the probability of possible outcome i.
**−log pᵢ** is the information received if i occurs.
Multiplying by pᵢ weights that surprise by how often it is expected to occur.
Summing over every i computes average surprise before the outcome is known.
**H(P)** names uncertainty of the whole distribution P.

### Why no cheaper operation does the same job

[Multiplying each surprise by pᵢ](../../MATHEMATICAL_MOVES.md#multiplication) lets common outcomes speak more often than rare ones when measuring the uncertainty of the whole situation.
[Summing](../../MATHEMATICAL_MOVES.md#summation) combines those mutually exclusive outcome contributions into one expected uncertainty; multiplying them would make any certain zero-surprise outcome erase all others.
[The log](../../MATHEMATICAL_MOVES.md#logarithm) still converts probability products into additive information, and [the minus sign](../../MATHEMATICAL_MOVES.md#negative-sign) keeps that information nonnegative.

The notation is finally shorter than the story that created it:

$$
H(P)=-\sum_i p_i\log p_i
$$

## Entropy beyond this one case

Entropy is the expected surprise before opening a sealed envelope. A guaranteed message brings none; evenly balanced alternatives bring more.

## Where entropy runs out

Entropy measures uncertainty in a stated distribution, not disorder in every everyday sense.

The weakness is not an accidental footnote. Every operation in entropy serves the narrower purpose to average the information of every possible outcome, weighted by how often that outcome occurs; none was designed to answer the new question. We have reached the honest edge of the invention.

## Take entropy to the workbench

Understanding entropy now means predicting its intermediate results before asking software for an answer. Build the wrong idea first, break it, then use [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running entropy, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the entropy result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
