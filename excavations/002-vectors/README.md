# Excavation 002 — Vectors

## The Problem: A Bag of Measurements Is Not Yet Geometry

Our tiger has four measurements: 4 legs, 180 kilograms, a stripe flag of 1, and 7-centimeter teeth. Keeping them as separate variables works for one animal. For a million animals, every comparison becomes a tangle of special cases.

We want one object that can be stored, compared, moved, and transformed by general rules.

## The Invention: An Ordered List

Choose a feature order:

```text
[legs, mass_kg, has_stripes, tooth_cm]
```

Now write the tiger as:

$$
\mathbf{x}=[4,180,1,7]
$$

This is a **vector**. The brackets are not the important part. The agreement about position is.

## Failed Attempt: Ignore Order

Suppose one program writes `[4, 180, 1, 7]`, while another expects `[mass, legs, tooth, stripes]`. The second program reads the same numbers as 4 kilograms, 180 legs, 1-centimeter teeth, and 7 stripe flags.

The computer performs the calculation flawlessly on a meaningless representation.

Vector dimensions do not carry names inside the arithmetic. Meaning comes from the schema surrounding them.

## The Geometric Leap

For two features, a vector is a point on a plane. Imagine describing fruit by sweetness and acidity:

| Fruit | Sweetness | Acidity | Vector |
|---|---:|---:|---|
| lemon | 1 | 9 | `[1, 9]` |
| orange | 6 | 6 | `[6, 6]` |
| banana | 9 | 2 | `[9, 2]` |

Plotting these points turns a table into a map. Nearby regions may correspond to similar tastes. With 300 features, we cannot draw the space, but the arithmetic works exactly the same way.

This gives a vector two interpretations:

- A **record** containing features about one object.
- A **position** in a feature space shared by all objects.

## Worked Example: Adding Vectors

If `[2, 3]` represents two resource quantities and `[4, 1]` represents more resources, then:

$$
[2,3]+[4,1]=[6,4]
$$

Addition operates coordinate by coordinate. It is meaningful only when corresponding coordinates describe compatible things. Adding `[height, weight]` to `[temperature, price]` is legal arithmetic but nonsense modeling.

## The Scale Trap

Return to the animal vectors. Mass ranges from 90 to 350; the stripe flag ranges only from 0 to 1. In many calculations, a 100-kilogram difference overwhelms every other feature.

Min-max normalization maps each observed feature into the range 0 to 1:

$$
x'=\frac{x-x_{\min}}{x_{\max}-x_{\min}}
$$

For masses 90, 180, and 350 kilograms, the normalized values are approximately 0, 0.346, and 1. Normalization does not discover importance; it merely prevents numeric units from deciding importance accidentally.

## Code Walkthrough

`implementation.py` builds three operations from plain Python:

- `add` combines matching dimensions.
- `scale` multiplies every coordinate by one number.
- `min_max_normalize` finds each column's range, then rescales its values.

Notice the dimension check in `add`. Try `add([1, 2], [3])`. Refusing mismatched vectors is better than returning a plausible-looking wrong answer.

Run:

```bash
python3 excavations/002-vectors/implementation.py
```

The leg dimension becomes zero for every animal because all observed animals have four legs. Within this tiny dataset, that feature provides no information for distinguishing them.

## Common Misconceptions

**“A vector is an arrow.”** An arrow is a useful geometric picture. In AI, a vector is usually an ordered array whose dimensions encode a representation.

**“More dimensions always mean more knowledge.”** Extra dimensions can be redundant or noisy.

**“Normalization makes features equally important.”** It makes scales comparable. The model can still weight them differently.

## What We Unearthed

Vectors give observations positions in a shared space. The next unavoidable question is: how do we decide whether two positions are close?

---

Previous: [001 — Why Features Exist](../001-why-features-exist/README.md) · Next: [003 — Distance](../003-distance/README.md)
