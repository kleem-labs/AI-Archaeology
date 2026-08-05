# Excavation 002 — Vectors

[Previous: Why Features Exist](../001-why-features-exist/README.md)

Civilization has grown. Reports arrive all day:

```text
tiger near river
three deer north
hunter injured
water low
```

The crisis is no longer noticing. It is organizing.

A table helps: one row per animal, one column per property. But to compare, copy, or transform one animal, we want to lift its row out as a single object.

## The package

First agree on an order:

```text
[weight, speed, age]
```

Then an animal can be carried as:

```text
tiger = [220, 65, 6]
rabbit = [2, 45, 1]
```

The brackets are not the discovery. The discovery is that many related measurements can travel together without losing which feature each position represents. Only now do we call that ordered package a **vector**.

## What fails if order is ignored

If one person writes `[weight, speed, age]` and another reads `[age, weight, speed]`, the numbers survive but the meaning does not. A vector is never “just numbers.” It is numbers plus an agreement about what each coordinate means.

## From a package to a place

Imagine using only weight and speed. Every animal now has a location—not in the jungle, but in a space whose directions mean properties.

```text
speed
  ↑       rabbit •
  |
  |                         • tiger
  +--------------------------------→ weight
```

The tiger's properties locate it. With three features it lies in three-dimensional feature space. With ten thousand features the same idea continues, even though we cannot picture it.

This was the great leap in your original excavation: geometry stopped meaning only “Where is the tiger?” It could now help answer “What is the tiger like?”

Nearby locations can represent similar objects. A movie can be located by humor, romance, and violence. A song can be located by tempo, instrumentation, and mood. Modern AI uses the same move: turn something difficult to compare into a point whose coordinates can be compared.

## The first equation earns its place

We already understand the object, so notation can compress it:

## Walk It Once with Concrete Values

A tiger recorded as weight 220, speed 65, and age 6 becomes [220, 65, 6]. The first slot must always mean weight; otherwise [220, 65, 6] could describe nonsense.

## Why Every Term Must Exist Before the Equation

- **x** is the object we needed to carry as one package.
- **x₁ through xₙ** are its agreed measurements; subscripts preserve which feature is which.
- **n** exists because different problems keep different numbers of features.
- The brackets bind the measurements without adding or comparing them yet.


This says only: one object carries an ordered measurement for each of $n$ agreed features.

Only now can we compress that reasoning:

$$
\mathbf{x}=[x_1,x_2,\ldots,x_n]
$$


## Challenge

Two vectors contain the same numbers in different orders. Are they the same representation? State the missing agreement needed to answer.

## What the next excavation needs

A thousand feature differences still give a thousand answers. To say which animal is closest, we need those differences to become one number.

[Next: Distance](../003-distance/README.md)
