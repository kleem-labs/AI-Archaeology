# Excavation 018 — Likelihood — Which Hidden Story Produced This Evidence?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality)
>
> **Applied territory:** Learning from uncertainty and error

Probability lets the trackers preserve several possible outcomes instead of pretending to know. Now they face the reverse problem: one footprint has arrived, and several hidden animals could have produced it.

A new case arrives at the Lantern Observatory. Nothing yet demands a new invention, so the keeper of uncertain stories uses the ring of glass lanterns to ask which story is generally more believable.

This is precisely the kind of shortcut a careful builder should try first. The instruction to ask which story is generally more believable preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: that ignores the actual print. Or ask for the probability of the story directly, although the story is what we are trying to judge.

The counterexample separates two questions that the attempt to ask which story is generally more believable had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the ring of glass lanterns fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now reverse the question: if this story were true, how expected would the observed evidence be? With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Likelihood**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## The calculation hidden inside likelihood

The keeper of uncertain stories carries the likelihood scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Story A says a deep print occurs 80% of the time; Story B says 20%. After observing a deep print, the same evidence has likelihood 0.8 under A and 0.2 under B, so A explains this clue four times as well.

### Naming what is already on the table

**θ** is one proposed hidden explanation.
**x** is the evidence already observed.
The vertical bar means “under the assumption that.”
**P(x|θ)** asks how expected this evidence would be if θ were true—the reversal forced by comparing stories.
**L(θ|x)** names that same quantity when x is held fixed and explanations vary; it is not automatically a probability over θ.

### Why the melody needs these exact notes

[The conditional bar](../../MATHEMATICAL_MOVES.md#conditional-bar) deliberately asks how expected this footprint would be **if** a tiger story were true. Reversing the two sides asks a different question and would silently mix evidence with prior belief.
[Equality](../../MATHEMATICAL_MOVES.md#equals) renames that conditional evidence score as likelihood when θ is treated as the candidate story and x as fixed evidence.

Every mark needed for likelihood is now visible on the ring of glass lanterns. The symbols do not add an idea; they bind the discovered moves into one line:

$$
\mathcal{L}(\theta\mid x)=P(x\mid\theta)
$$

## Likelihood beyond this one case

A detective compares suspects by asking how well each suspect explains the clues, not how common the suspect is in the population.

## Where likelihood runs out

Likelihood compares explanations for fixed evidence; it is not itself a normalized probability over explanations. Priors will matter later.

At the Lantern Observatory, the keeper of uncertain stories leaves a blank beneath the new mark. Likelihood has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the ring of glass lanterns

Rebuild the likelihood scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
