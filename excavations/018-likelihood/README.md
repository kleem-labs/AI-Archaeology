# Excavation 018 — Likelihood — Which Hidden Story Produced This Evidence?

<!-- book-prose-v2 -->

Probability lets the trackers preserve several possible outcomes instead of pretending to know. Now they face the reverse problem: one footprint has arrived, and several hidden animals could have produced it.

The obvious economy is to ask which story is generally more believable.

The proposal deserves a fair hearing. For likelihood, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Its hidden assumption becomes visible as soon as we observe that that ignores the actual print. Or ask for the probability of the story directly, although the story is what we are trying to judge.

The failure changes the question behind likelihood. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: reverse the question: if this story were true, how expected would the observed evidence be? That score is likelihood.

Only at this point does the inherited name **Likelihood** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of likelihood by mentally removing the repair. We fall back to the proposal to ask which story is generally more believable.; then that ignores the actual print. Or ask for the probability of the story directly, although the story is what we are trying to judge. Restore only the ability to reverse the question: if this story were true, how expected would the observed evidence be? That score is likelihood, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to ask which story is generally more believable. to requiring the system to reverse the question: if this story were true, how expected would the observed evidence be? That score is likelihood. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to likelihood.

## The calculation hidden inside likelihood

Do not read the coming Likelihood line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Story A says a deep print occurs 80% of the time; Story B says 20%. After observing a deep print, the same evidence has likelihood 0.8 under A and 0.2 under B, so A explains this clue four times as well.

### Names for pieces we have already used

**θ** is one proposed hidden explanation.
**x** is the evidence already observed.
The vertical bar means “under the assumption that.”
**P(x|θ)** asks how expected this evidence would be if θ were true—the reversal forced by comparing stories.
**L(θ|x)** names that same quantity when x is held fixed and explanations vary; it is not automatically a probability over θ.

### Why no cheaper operation does the same job

[The conditional bar](../../MATHEMATICAL_MOVES.md#conditional-bar) deliberately asks how expected this footprint would be **if** a tiger story were true. Reversing the two sides asks a different question and would silently mix evidence with prior belief.
[Equality](../../MATHEMATICAL_MOVES.md#equals) renames that conditional evidence score as likelihood when θ is treated as the candidate story and x as fixed evidence.

The notation is finally shorter than the story that created it:

$$
\mathcal{L}(\theta\mid x)=P(x\mid\theta)
$$

## Likelihood beyond this one case

A detective compares suspects by asking how well each suspect explains the clues, not how common the suspect is in the population.

## Where likelihood runs out

Likelihood compares explanations for fixed evidence; it is not itself a normalized probability over explanations. Priors will matter later.

The limit follows from the job assigned to likelihood. Its repair knows how to reverse the question: if this story were true, how expected would the observed evidence be? That score is likelihood. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take likelihood to the workbench

A claim about likelihood now exists on the page; the laboratory must be able to contradict it. Build the wrong idea first, break it, then use [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running likelihood, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the likelihood result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
