# Excavation 018 — Likelihood — Which Hidden Story Produced This Evidence?

[Previous excavation](../017-probability/README.md)

Two trackers propose different worlds. One says tigers usually leave deep round prints; another says deer do. We have observed one print and must compare the stories.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Ask which story is generally more believable. That ignores the actual print. Or ask for the probability of the story directly, although the story is what we are trying to judge.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Ask which story is generally more believable. That ignores the actual print. Or ask for the probability of the story directly, although the story is what we are trying to judge.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Reverse the question: if this story were true, how expected would the observed evidence be? That score is likelihood.

Only after that reasoning may we give your discovery its inherited name.

## Why It Still Fails

The verbal procedure is now useful, but it is too long to repeat consistently and too vague to implement at scale. Every operation has earned a precise role; only now should notation compress it.

## Compress your discovery into mathematics


## Build each piece from what just happened

Story A says a deep print occurs 80% of the time; Story B says 20%. After observing a deep print, the same evidence has likelihood 0.8 under A and 0.2 under B, so A explains this clue four times as well.

### Give Short Names Only After We Know the Pieces

- **θ** is one proposed hidden explanation.
- **x** is the evidence already observed.
- The vertical bar means “under the assumption that.”
- **P(x|θ)** asks how expected this evidence would be if θ were true—the reversal forced by comparing stories.
- **L(θ|x)** names that same quantity when x is held fixed and explanations vary; it is not automatically a probability over θ.

Only now can we compress that reasoning:

$$
\mathcal{L}(\theta\mid x)=P(x\mid\theta)
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

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
