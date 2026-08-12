# Excavation 018 — Likelihood — Which Hidden Story Produced This Evidence?

Probability lets the trackers preserve several possible outcomes instead of pretending to know. Now they face the reverse problem: one footprint has arrived, and several hidden animals could have produced it.

Perhaps we ask which story is generally more believable. That ignores the actual print. Or ask for the probability of the story directly, although the story is what we are trying to judge.

So we reverse the question: if this story were true, how expected would the observed evidence be? That score is likelihood.

## From procedure to notation

The procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.

## The arithmetic we have earned

Story A says a deep print occurs 80% of the time; Story B says 20%. After observing a deep print, the same evidence has likelihood 0.8 under A and 0.2 under B, so A explains this clue four times as well.

### Only now do the symbols earn names

- **θ** is one proposed hidden explanation.
- **x** is the evidence already observed.
- The vertical bar means “under the assumption that.”
- **P(x|θ)** asks how expected this evidence would be if θ were true—the reversal forced by comparing stories.
- **L(θ|x)** names that same quantity when x is held fixed and explanations vary; it is not automatically a probability over θ.

Only now can we compress that reasoning:

$$
\mathcal{L}(\theta\mid x)=P(x\mid\theta)
$$

## Carry the idea back into the world

A detective compares suspects by asking how well each suspect explains the clues, not how common the suspect is in the population.

## Limits

Likelihood compares explanations for fixed evidence; it is not itself a normalized probability over explanations. Priors will matter later.

## Enter the laboratory

Build the wrong idea first, break it, then use [Pure Python → NumPy → PyTorch](implementation/README.md).

## Test what you believe

Use the [invention exercises](exercises.md), not as a quiz but as a request to rediscover the idea.

## What this discovery now makes possible

- [Mistakes and failed ideas](mistakes.md)
- [Mermaid and ASCII diagram](diagram.md)
- [References](references.md)
- [Visual asset brief](images/README.md)

The limitation in this excavation creates the need for the next one.
