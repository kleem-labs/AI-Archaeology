# Excavation 009 — From Scores to Attention

Suppose *she* compares itself with earlier words and receives:

```text
John   2
Mary   8
book   4
```

The ranking is useful, but these are not yet mixing weights. Another sentence may produce `200, 800, 400`, or include negatives. We need a stable answer to: how much should each source contribute?

## Failed ideas

Choose only the maximum, and uncertainty disappears. Mary may matter most while *book* still supplies useful context.

Divide by the sum, and negative scores can create negative shares or the total can be zero.

Clip negatives, and a tiny movement across zero abruptly switches a path on or off. We want smooth corrections during learning.

The desired transformation should:

- make every share positive;
- preserve which score is larger;
- make strong evidence more decisive;
- let bad negative matches fade toward zero;
- normalize the shares to a total of one.

## Let the requirements choose the operation

An exponential does something useful: positive evidence grows quickly, while negative evidence becomes a small positive number.

```text
score:          2      4       8
exponential:   ~7     ~55    ~2981
```

Squares also amplify large scores, but they turn `-5` into `25`, converting strong negative evidence into a strong positive match. Exponentials preserve order instead.

After exponentiating, divide each result by their total. Now the values are positive and sum to one. Only after deriving those requirements do we name the result **softmax**:

## The calculation hidden inside from scores to attention

Mary, John, and the book are possible sources for the word *she*. The sentence gives Mary the strongest relevance, the book a weaker connection, and John the weakest. Raw relevance can be negative or arbitrarily large, so it cannot yet say what share each source should contribute. Exponentiation turns every candidate into positive evidence; dividing by their shared total converts that evidence into portions of one whole.

### Naming what is already on the table

- **sᵢ** is the raw relevance score for candidate i.
- Exponentiation makes every weight positive, preserves ordering, suppresses negative evidence, and amplifies strong evidence.
- The denominator sums evidence from every candidate j because a weight is meaningful only relative to its competitors.
- Division makes all resulting weights sum to one.

For scores `[2, 4, 8]`, the largest score receives almost all the weight, but the others are not forbidden from contributing.

Softmax does not discover relevance. It converts already-computed relevance scores into a smooth distribution of attention.

### Why the melody needs these exact notes

[Exponentiation](../../MATHEMATICAL_MOVES.md#exponential) makes every raw score positive while preserving order and turning score gaps into stable ratios. Squaring would make a large negative score look strong; clipping would destroy gap information.
[The sum](../../MATHEMATICAL_MOVES.md#summation) gathers every candidate's positive weight because all candidates must share one unit of attention. A product would not describe a total available amount.
[Dividing by that total](../../MATHEMATICAL_MOVES.md#division) converts each weight into its share. Without it, multiplying every score scale would change the amount of information mixed rather than only its distribution.

The calculation borrows several gestures already encountered elsewhere: **the rising flame**—a small score difference becomes positive relative evidence; **the chorus**—many witnesses contribute to one answer without one silence erasing the rest; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. from scores to attention feels new because the objects are new; the gestures remain recognizably human.

The story of from scores to attention has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
\mathrm{softmax}(s_i)=\frac{e^{s_i}}{\sum_j e^{s_j}}
$$

## The missing question

We now know **who matters**, but weights are not knowledge. If a historian receives weight `0.90`, what does the historian actually say? That distinction leads to values.

## Challenge

Explain why squaring `[-5, 1]` violates the meaning of a negative relevance score, and why exponentiation does not.

Before changing any code, predict what colder and hotter temperatures will do. Then run the [Softmax Temperature Field Lab](../../labs/02_softmax_lab.py).

## What the next excavation needs

We must derive both the relevance scores and the information being mixed. Those are different jobs.

[Next: Query, Key, and Value](../010-query-key-value/README.md)

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->
