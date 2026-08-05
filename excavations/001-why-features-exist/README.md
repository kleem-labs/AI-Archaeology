# Excavation 001 — Why Features Exist

## The Problem: Experience Is Too Large

Imagine building a machine that must warn a village when a dangerous animal approaches. Its camera sees one million pixel values per image. You have only six labeled examples: three harmless animals and three dangerous ones.

What should the machine compare?

Raw pixels are fragile. Move an animal one step to the left and nearly every pixel changes, although the danger has not. We need measurements that remain useful when irrelevant details change.

## Failed Attempt 1: Compare Every Pixel

Exact pixel matching memorizes backgrounds, lighting, and camera position. It may conclude that a tiger in rain is unrelated to the same tiger in sunlight.

The failure is not insufficient computation. We asked the machine to treat every recorded difference as equally meaningful.

## Failed Attempt 2: Use One Obvious Property

Perhaps “has stripes” is enough. Then a zebra becomes dangerous. Perhaps “has four legs” is enough. Then deer, dogs, and tigers collapse into one category.

One feature is easy to understand but rarely captures the whole problem.

## The Invention: Features

A **feature** is a measurable property chosen because it may help with a task. For an animal-warning system, we might record:

| Feature | Tiger | Zebra | Deer |
|---|---:|---:|---:|
| legs | 4 | 4 | 4 |
| mass (kg) | 180 | 350 | 90 |
| stripes | 1 | 1 | 0 |
| tooth length (cm) | 7.0 | 2.5 | 1.5 |
| stalks prey | 1 | 0 | 0 |

No single column solves the problem. Together they create a more useful description.

## Worked Example: The Three-Legged Tiger

A tiger injured in a trap now has three legs. If “four legs” were a rigid rule, the system would call it something else. A feature is not necessarily a requirement; it is evidence.

Compare two informal rules:

- **Rigid rule:** dangerous only if all expected properties match.
- **Evidence rule:** danger increases with long teeth, predatory movement, body shape, and known patterns; missing one usual property does not erase the others.

This distinction—between features and hard definitions—will later let models tolerate noise and exceptions.

## Features Depend on the Task

Suppose the same dataset is used for three goals:

- Predict danger: tooth length and stalking behavior matter.
- Predict food needed per day: mass may dominate.
- Identify individual animals: scar patterns may matter.

There is no universally “best” feature set. A property is useful relative to a question.

## Invariance: Ignoring the Right Changes

A good danger feature should ideally remain stable when lighting, camera angle, or background changes. We call this **invariance**: the representation ignores transformations irrelevant to the task.

But invariance has a cost. A feature invariant to color cannot help distinguish ripe from unripe fruit. Every discarded variation closes some future possibility.

## Code Walkthrough

Open `implementation.py`. The constant `FEATURES` fixes a shared order:

```python
FEATURES = ("legs", "mass_kg", "has_stripes", "tooth_cm")
```

`extract_features` reads those names from an observation and returns their numeric values in that exact order. Try deleting `tooth_cm` from one animal: the program raises an error rather than silently inventing data. This is useful—the representation contract has been broken.

Run it from the repository root:

```bash
python3 excavations/001-why-features-exist/implementation.py
```

The output is compact, but the important act happened before execution: someone decided which properties deserved a column.

## Common Misconceptions

**“More features are always better.”** Irrelevant features add noise, cost, and opportunities to memorize accidents.

**“Features are objective facts.”** Measurements may be objective, but choosing them is a modeling decision.

**“Modern deep learning eliminates features.”** Deep networks learn many internal features automatically, but input representation and training objective still determine what can be learned.

## What We Unearthed

Features turn unmanageable experience into comparable measurements. But separate named values are awkward to calculate with. We need to bind them into one ordered mathematical object.

That object is a vector.

---

Previous: [000 — Before Mathematics Existed](../000-before-mathematics-existed/README.md) · Next: [002 — Vectors](../002-vectors/README.md)
