# Excavation 003 — Distance

## The Problem: What Does “Similar” Mean?

Vectors place objects in a shared space. Suppose a new animal has vector `[4, 200, 1, 6]`. Is it more like our tiger `[4, 180, 1, 7]`, zebra `[4, 350, 1, 2.5]`, or deer `[4, 90, 0, 1.5]`?

Looking at four columns is manageable. Looking at four thousand is not. We need one number summarizing separation.

## Failed Attempt 1: Count Unequal Coordinates

The new animal differs from the tiger in mass and tooth length: two coordinates. It also differs from the zebra in mass and tooth length: two coordinates. This method calls them equally distant.

But 20 kilograms is not the same change as 150 kilograms. Counting differences throws away magnitude.

## Failed Attempt 2: Add Signed Differences

Try summing coordinate differences. Between `[0, 10]` and `[10, 0]`, the differences are `-10` and `10`; their sum is zero. Two large changes cancel and falsely imply no distance.

A distance needs every changed dimension to contribute positively.

## Rediscovering Euclidean Distance

Start in two dimensions. From point `[1, 2]` to `[4, 6]`, we move 3 units horizontally and 4 vertically. Those movements form the sides of a right triangle. The direct path is its hypotenuse:

$$
d=\sqrt{3^2+4^2}=5
$$

For any number of dimensions:

$$
d(\mathbf{x},\mathbf{y})=\sqrt{\sum_i(x_i-y_i)^2}
$$

The formula follows four deliberate steps:

1. Subtract corresponding coordinates.
2. Square each difference so signs cannot cancel.
3. Add every dimension's contribution.
4. Take the square root to undo the squared units.

## Worked Animal Example

Using only normalized mass and tooth length, suppose:

- query: `[0.42, 0.82]`
- tiger: `[0.35, 1.00]`
- zebra: `[1.00, 0.18]`

Then:

$$
d(\text{query},\text{tiger})
=\sqrt{(0.42-0.35)^2+(0.82-1)^2}
\approx0.193
$$

$$
d(\text{query},\text{zebra})
=\sqrt{(0.42-1)^2+(0.82-0.18)^2}
\approx0.864
$$

The query is much closer to the tiger under this representation and metric.

## Different Distances Ask Different Questions

**Manhattan distance** adds absolute changes:

$$d_1(\mathbf{x},\mathbf{y})=\sum_i|x_i-y_i|$$

It imagines movement along grid lines. **Euclidean distance** measures the straight path. **Cosine similarity**, introduced later, asks whether vectors point in similar directions and largely ignores their lengths.

No metric is simply “the truth.” A metric encodes which differences matter and how they combine.

## Weighted Distance

If tooth length is twice as important as mass for danger, we can use:

$$
d=\sqrt{1(x_{mass}-y_{mass})^2+2(x_{tooth}-y_{tooth})^2}
$$

Choosing weights is choosing a geometry. The same points acquire different neighbors when the geometry changes.

## Code Walkthrough

`implementation.py` defines Euclidean and Manhattan distance directly. Both call `_check` because comparing vectors with different schemas is undefined.

Run:

```bash
python3 excavations/003-distance/implementation.py
```

The raw calculation is dominated by mass. Modify the data to normalized values and observe how the ranking can change. That is not a bug; it reveals that preprocessing participates in the definition of similarity.

## Common Misconceptions

**“The nearest item is objectively the most similar.”** It is nearest under a particular representation, scaling, and metric.

**“Distance works naturally in any number of dimensions.”** In very high dimensions, distances can concentrate and intuitive notions of neighborhood become less reliable.

**“Units do not matter.”** Mixing centimeters, kilograms, and binary flags without scaling lets units dominate.

## What We Unearthed

Distance began with subtraction. But the difference vector contains more information than its length: it tells us exactly how one point would need to change to reach another.

---

Previous: [002 — Vectors](../002-vectors/README.md) · Next: [004 — Vectors as Change](../004-vectors-as-change/README.md)
