# Excavation 018 — Likelihood — Which Hidden Story Produced This Evidence?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality)
>
> **Applied territory:** Learning from uncertainty and error

Probability lets the trackers preserve several possible outcomes instead of pretending to know. Now they face the reverse problem: one footprint has arrived, and several hidden animals could have produced it.

The ring of glass lanterns at the Lantern Observatory still carries the marks of the previous discovery. The keeper of uncertain stories follows them as far as they seem willing to go: ask which story is generally more believable.

For a moment the mark looks complete. Then the evidence refuses to fit: that ignores the actual print. Or ask for the probability of the story directly, although the story is what we are trying to judge. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The keeper of uncertain stories sketches the break before changing it:*

```text
OLD PATH:  request ──▶ ask which story is generally more… ──▶ that ignores the actual print. Or ask…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ reverse the question: if this story… ──▶ accountable result
```

The keeper of uncertain stories lays two translucent sheets over the ring of glass lanterns. The first is inscribed, “ask which story is generally more believable.” Its path ends where that ignores the actual print. Or ask for the probability of the story directly, although the story is what we are trying to judge. The second receives the same evidence but is allowed to reverse the question: if this story were true, how expected would the observed evidence be? That score is likelihood. Held to the light, the sheets separate at exactly one decision.

No one reaches for a likelihood formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The keeper of uncertain stories changes only that one responsibility: reverse the question: if this story were true, how expected would the observed evidence be? That score is likelihood. When the ink dries, the name **Likelihood** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because that ignores the actual print. Or ask for the probability of the story directly, although the story is what we are trying to judge, while the other can reverse the question: if this story were true, how expected would the observed evidence be? That score is likelihood. That fork—not the vocabulary—is where likelihood lives.

<!-- memory-film-v1:start -->
> **Memory realm 3 of 18 — [Lantern Observatory](../../MEMORY_PALACE.md#realm-3)**
>
> **The question carried into this chamber:** Which Hidden Story Produced This Evidence?

## When the chamber changes

Before leaving Likelihood, replay the discovery as motion rather than as a definition.

First hold the failed picture still: The key follows the tempting path—ask which story is generally more believable. Then the evidence answers: that ignores the actual print. Or ask for the probability of the story directly, although the story is what we are trying to judge.

Now let the chamber move: The keeper of uncertain stories changes one moving part. The key can now reverse the question: if this story were true, how expected would the observed evidence be? That score is likelihood.

The object that should remain after the terminology disappears is **the likelihood key mounted on the ring of glass lanterns**.

> **Memory seal — Likelihood**
>
> Likelihood keeps the missing power: reverse the question: if this story were true, how expected would the observed evidence be? That score is likelihood.

Give the idea a bodily path: Touch the likelihood key in imagination: draw the old path in the air, stop sharply at its failure, and finish with the new motion.
<!-- memory-film-v1:end -->

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
