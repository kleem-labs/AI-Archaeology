# Excavation 218 — Expectation, Variance, and Covariance — Centre, Spread, and Shared Motion

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->



Bayes' rule returns a full distribution after evidence. To budget supplies or compare models, the station needs summaries, but one central value must not pretend that uncertainty and joint movement disappeared.

At this depth, Expectation, Variance, and Covariance begins as a need inside the world rather than as a name outside it.

Two routes both average one tiger sighting per day. Route A always sees exactly one. Route B sees zero half the time and two half the time. The means agree; their risks do not.

The chamber has reduced the abstraction to one physical thing: **a hanging flock-mobile with a central spindle and paired threads**. The question carved beside it asks: *Where does uncertainty balance, how widely does it wander, and what moves together?*

We try to spend no new mathematics at all and simply report only the average and treat distributions sharing it as interchangeable.

The test is deliberately small enough to follow by hand, so the failure cannot hide inside complexity. The average hides spread. It also cannot reveal whether tiger count and alarm count rise together or move independently, which matters when one is used to predict the other.

```text
no symbols yet
      ↓
one named example
      ↓
a rule we would naturally try
      ↓
the case that refuses it
      ↓
Expectation, Variance, and Covariance becomes necessary
```

At last there is something worth inventing. Whatever we build must compute expectation as a probability-weighted centre, variance as average squared departure from that centre, and covariance as average product of paired departures.

The failure and repair now form one continuous argument for Expectation, Variance, and Covariance: this idea earns its place by preserving exactly what the earlier action lost.

## The calculation hidden inside expectation, variance, and covariance

The symbols for expectation, variance, and covariance will compress the same concrete case without replacing it. The objects and actions remain visible while their repeated responsibilities receive shorter names.

### Testing Expectation, Variance, and Covariance against the named case

Route A's count is always 1, so every departure from mean 1 is zero and variance is zero. Route B's departures are -1 and +1; squaring gives 1 in either case, so variance is 1. If alarm departures carry the same signs as tiger departures, their products are positive and covariance reveals shared movement.

### Naming what is already on the table

**μ** is the expected centre. **X-μ** is one departure. Squaring prevents low and high outcomes from cancelling in variance. **Y-E[Y]** is the paired departure of a second quantity. Multiplying paired departures records same-direction as positive and opposite-direction as negative.

### Why the melody needs these exact notes

[Expectation](../../MATHEMATICAL_MOVES.md#expectation) lets each possible value contribute in proportion to its probability. [Variance](../../MATHEMATICAL_MOVES.md#variance) uses squared departures so opposite errors do not cancel. [Covariance](../../MATHEMATICAL_MOVES.md#covariance) multiplies paired departures; adding them would lose whether the two quantities moved together on the same occasion.

Every operation required by expectation, variance, and covariance now has a visible job in the named case, so the complete construction can be written compactly:

$$
E[X]=\sum_x xP(X=x),\quad Var(X)=E[(X-E[X])^2],\quad Cov(X,Y)=E[(X-E[X])(Y-E[Y])]
$$

## A real-world echo

The centre of a flock says where to look; its spread says how wide to search; synchronized turns say which birds respond to the same wind.

## What this unlocks elsewhere

Normalization uses means and variances, PCA diagonalizes covariance, initialization controls signal variance, and gradient-noise analysis compares shared direction with disagreement.

## Where the promise of expectation, variance, and covariance breaks

These quantities are usually estimated from samples. Before trusting them, we need a reason that accumulating more independent evidence makes sample averages settle rather than wander forever.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Expectation, Variance, and Covariance tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 219: The Law of Large Numbers — Why Averages Eventually Settle](../219-law-large-numbers/README.md)
