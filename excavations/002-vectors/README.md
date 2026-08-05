# Excavation 002 — Vectors

## The Problem

Our features are still separate entries. To compare, store, and transform observations efficiently, we need to treat the measurements as one object.

## The Invention

Choose a stable order—legs, mass, stripes, tooth length—and place the values in that order:

$$\mathbf{x} = [4, 180, 1, 7]$$

This ordered list is a **vector**. Each position is a dimension with a specific meaning. Order matters.

## A Geometric Surprise

With two features, a vector is a point on a plane. With three, it is a point in space. With hundreds, the same idea continues in a space we cannot draw.

- **Record:** one object described by many features.
- **Point:** one location in feature space.

## Scale Matters

Mass may range into hundreds while a stripe flag is zero or one. Larger numeric scales can dominate later calculations. Normalization can help, but must preserve distinctions the task needs.

## The New Problem

“Which objects are alike?” has become “which points are close?” We now need a definition of distance.

---

Previous: [001 — Why Features Exist](../001-why-features-exist/README.md) · Next: [003 — Distance](../003-distance/README.md)
