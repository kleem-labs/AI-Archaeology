# Excavation 216 — Random Variables and Distributions — Turning Outcomes into Quantities

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

### Realm 4 — The Observatory of Possible Worlds

The river empties beneath a glass dome. Each lantern shows a different possible tomorrow; none may be extinguished merely because we do not yet know which world is real.

Listen for turning lenses, weighted chains, and many quiet witnesses. The questions in this realm travel as one chain:

```text
possible worlds → evidence → centre and spread → settling averages → bell-shaped error → convincing claims
```



Fourier analysis gives deterministic signals new coordinates. The ranger's camera, however, may record zero, one, or several tigers tomorrow; before the observation, the count is not an unknown fixed number but a quantity attached to several possible worlds.

The vault of Random Variables and Distributions opens onto a problem a ranger, builder, or machine could encounter without knowing any modern terminology.

Three cards describe tomorrow: no tiger, one tiger, and two tigers. Each card has a probability, but the station wants to compute expected food use and variation in the *count*.

The chamber has reduced the abstraction to one physical thing: **possible-world cards passing through a numbered brass sieve**. The question carved beside it asks: *How can stories about possible tomorrows become quantities we can calculate with?*

The old machinery invites a plausible shortcut: treat the outcome label itself as a number and perform arithmetic directly on names such as ‘no sighting’ and ‘two sightings’.

The stone does not object with terminology; it objects with a result we already know cannot be right. Outcomes may be stories, images, or paths rather than numbers, and the same numerical question can group many different outcomes. Arithmetic needs a mapping from possible worlds to values.

```text
scene → guess → calculate → compare with reality
          ▲                       │
          └──── change the idea ──┘
                       ↓
                     Random Variables and Distributions
```

We do not leap to a famous formula. We carry one missing responsibility forward: define a random variable as a function assigning a numerical value to every outcome, then transfer probability mass through that mapping to form its distribution.

The failure and repair now form one continuous argument for Random Variables and Distributions: this idea earns its place by preserving exactly what the earlier action lost.

## The calculation hidden inside random variables and distributions

The symbols for random variables and distributions will compress the same concrete case without replacing it. The objects and actions remain visible while their repeated responsibilities receive shorter names.

### Testing Random Variables and Distributions against the named case

Let Ω contain four equally likely camera histories. Two contain no tiger, one contains one tiger, and one contains two. The counting function X maps them to 0, 0, 1, and 2. Therefore `P(X=0)=2/4`, `P(X=1)=1/4`, and `P(X=2)=1/4`. Different histories can share one count without becoming the same history.

### Naming what is already on the table

**Ω** is the sample space of possible histories. **X** is the function turning a history into a real count. **P(X=x)** gathers the probability of every history mapped to value x. The distribution is the resulting allocation of probability across possible numerical values.

### Why the melody needs these exact notes

[Function application](../../MATHEMATICAL_MOVES.md#function-application) converts each outcome into the quantity we care about. [Probability](../../MATHEMATICAL_MOVES.md#probability) preserves how much possibility maps to each value, and [summation](../../MATHEMATICAL_MOVES.md#summation) combines different outcomes sharing the same value. Multiplying their probabilities would describe all histories occurring together, a different event.

Every operation required by random variables and distributions now has a visible job in the named case, so the complete construction can be written compactly:

$$
P(X=x)=\sum_{\omega:X(\omega)=x}P(\omega)
$$

## A real-world echo

Weather is a story; temperature is a random variable extracted from that story. The number is a question asked of the world, not the whole world itself.

## What this unlocks elsewhere

Loss, reward, token count, model output, and gradient noise are random variables. Their distributions—not isolated values—determine learning and evaluation.

## Where the promise of random variables and distributions breaks

A distribution describes current uncertainty, but it cannot update itself when evidence arrives. When a paw print appears, the probabilities must be rearranged according to how compatible each hidden story was with that evidence.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Random Variables and Distributions tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 217: Conditional Probability and Bayes’ Rule — Let Evidence Rearrange Belief](../217-conditional-probability-bayes/README.md)
