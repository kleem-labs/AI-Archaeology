# Excavation 009 — From Scores to Attention

[Previous: Attention](../008-attention/README.md)


## Take the First Step Yourself

> **Your problem:** Scores are 15, 14.9, and 1. How should all three influence the result?

> **Try your first idea:** Pick only the winner, then divide raw scores containing a negative value.

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

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

## Build Every Piece from the Concrete Example

For scores [1,2], exponentiation gives about [2.72,7.39]. Their total is 10.11. Dividing produces [0.27,0.73]: both remain possible, the larger score gets more weight, and the weights total one.

### Give Short Names Only After We Know the Pieces

- **sᵢ** is the raw relevance score for candidate i.
- Exponentiation makes every weight positive, preserves ordering, suppresses negative evidence, and amplifies strong evidence.
- The denominator sums evidence from every candidate j because a weight is meaningful only relative to its competitors.
- Division makes all resulting weights sum to one.


For scores `[2, 4, 8]`, the largest score receives almost all the weight, but the others are not forbidden from contributing.

Softmax does not discover relevance. It converts already-computed relevance scores into a smooth distribution of attention.

Only now can we compress that reasoning:

$$
\operatorname{softmax}(s_i)=\frac{e^{s_i}}{\sum_j e^{s_j}}
$$


## The missing question

We now know **who matters**, but weights are not knowledge. If a historian receives weight `0.90`, what does the historian actually say? That distinction leads to values.

## Challenge

Explain why squaring `[-5, 1]` violates the meaning of a negative relevance score, and why exponentiation does not.

## What the next excavation needs

We must derive both the relevance scores and the information being mixed. Those are different jobs.

[Next: Query, Key, and Value](../010-query-key-value/README.md)
