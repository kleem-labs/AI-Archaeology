# Excavation 003 — Distance

[Previous: Vectors](../002-vectors/README.md)


## Take the First Step Yourself

> **Your problem:** How can weight, speed, and age disagreements become one similarity answer?

> **Try your first idea:** Add +5, +1, and −1. Then test +100 and −100. Did real disagreement disappear?

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

The king asks for the animal most similar to Tiger A.

```text
Tiger A = [220, 65, 6]
Tiger B = [225, 66, 5]
Rabbit  = [  2, 45, 1]
```

The answer feels obvious. A computer still needs a procedure.

## First attempt: compare one feature

Weight alone can find a crocodile that weighs the same as a tiger. Add speed and another unrelated animal may still match. Every omitted property is a place for a false conclusion to hide.

## Second attempt: keep every difference

Comparing Tiger A with Tiger B gives:

```text
weight:  5
speed:   1
age:    -1
```

This is accurate, but it is not a decision. With a thousand attributes we receive a thousand answers. We need one measure of separation.

## Your derivation

You proposed the entire path yourself:

> Find the difference of similar features. If it is negative, that is wrong for distance, so square the differences, add them, and take the root.

Why not simply add? Because opposite differences cancel. A change of `100` and `-100` would produce zero, falsely declaring two objects identical.

Why square? Every changed coordinate becomes positive, and a large disagreement contributes more strongly than a small one.

Why add? We need every feature to contribute to one answer.

Why take the root? The direct line across a space is not the sum of its side lengths. A move of 3 in one direction and 4 in another forms a right triangle whose direct separation is 5. The root returns us from squared separation to ordinary distance.

Only after the reasoning is complete does the notation help:

## Build Every Piece from the Concrete Example

Tiger A has weight 220 kg, speed 65 km/h, and age 6 years.

Tiger B has weight 225 kg, speed 66 km/h, and age 5 years.

Compare the same property with the same property:

~~~text
weight difference = 225 - 220 =  5
speed difference  =  66 -  65 =  1
age difference    =   5 -   6 = -1
~~~

Adding gives 5 + 1 - 1 = 5. That is wrong: being one year younger cancelled part of the other disagreement.

~~~text
weight disagreement squared = 5 squared    = 25
speed disagreement squared  = 1 squared    =  1
age disagreement squared    = (-1) squared =  1
total                                      = 27
~~~

The total is in squared differences. Its square root gives one ordinary separation: about 5.20.

### Give Short Names Only After We Know the Pieces

- **x** is only a nickname for Tiger A's ordered measurements.
- **y** is only a nickname for Tiger B's ordered measurements.
- **x1 and y1** are their weights; index 2 means speed; index 3 means age.
- **xi−yi** abbreviates “compare the same named property,” exactly as above.
- Squaring repairs the cancellation we just witnessed.
- Summing combines weight, speed, and age into one answer.
- The root changes total 27 into distance 5.20.
- **d(x,y)** merely names “the one separation between these two tigers.”

Only now can we compress that reasoning:

$$
d(\mathbf{x},\mathbf{y})
=\sqrt{(x_1-y_1)^2+(x_2-y_2)^2+\cdots+(x_n-y_n)^2}
$$


The formula is your procedure written compactly.

## A limit we must remember

If weight is measured in kilograms and a stripe flag is only zero or one, weight can dominate. Distance treats coordinate scales as meaningful. Representation and normalization therefore matter as much as arithmetic.

Distance also answers **similarity**, not every kind of relationship. That distinction will become decisive when we reach attention.

## Challenge

Construct two pairs of two-dimensional points whose signed differences add to zero even though neither pair is identical. Then explain why squaring prevents the mistake.

Then test your prediction in the [Tiger Distance Field Lab](../../labs/01_distance_lab.py). Read the file from the top: it builds the tempting wrong rule before repairing it.

## What the next excavation needs

So far a vector has described where an object is in feature space. But an arrow can also describe how something changes. That second meaning will lead us toward transformations.

[Next: Vectors as Change](../004-vectors-as-change/README.md)
