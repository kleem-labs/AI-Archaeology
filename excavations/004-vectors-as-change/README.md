# Excavation 004 — Vectors as Change

## A Second Meaning for Vectors

So far, `[2, 3]` has meant a location. But the same pair of numbers can mean an instruction: move 2 units right and 3 units up.

This distinction is subtle and powerful. A point answers **where?** A displacement answers **how must it change?**

## Deriving Change from Two States

Suppose a traveler begins at:

$$\mathbf{a}=[2,3]$$

and reaches:

$$\mathbf{b}=[7,1]$$

We seek a vector $\Delta$ satisfying:

$$\mathbf{a}+\Delta=\mathbf{b}$$

Subtract $\mathbf{a}$ from both sides:

$$
\Delta=\mathbf{b}-\mathbf{a}=[7-2,1-3]=[5,-2]
$$

The traveler moved 5 units right and 2 down. Add the displacement back to verify it:

$$[2,3]+[5,-2]=[7,1]$$

## Failed Attempt: Store Only the Distance

The Euclidean distance is $\sqrt{29}$. That tells us how much movement occurred but not where it led. Infinitely many destinations lie $\sqrt{29}$ units away.

Distance is magnitude without direction. The difference vector preserves both.

## Composing Changes

The traveler next moves from `[7, 1]` to `[8, 5]`, a displacement of `[1, 4]`. The full journey is:

$$
[5,-2]+[1,4]=[6,2]
$$

Starting at `[2, 3]` and applying `[6, 2]` reaches `[8, 5]`. Vector addition composes changes without needing the intermediate stop.

## Scaling Change

Multiplying `[5, -2]` by `0.5` gives `[2.5, -1]`: half the displacement in the same direction. Multiplying by `-1` gives `[-5, 2]`: the reverse direction.

This is why vector arithmetic is useful for velocities, forces, gradients, and learned representation changes. It gives us a language for direction and amount.

## Change Outside Physical Space

Imagine a house represented as `[bedrooms, area_m², price_units]`. The difference between a small and renovated version might be `[1, 30, 2]`. This vector is not a physical arrow. It is a coordinated change across features.

Later, neural networks will repeatedly transform representation vectors. Their internal “directions” may encode changes such as becoming more plural, more formal, or more relevant to the current context—although such interpretations are rarely perfect or isolated in one coordinate.

## Code Walkthrough

`implementation.py` builds `subtract` from two simpler ideas: negate the second vector, then add. It computes two legs of a journey, adds them, and reconstructs the final point.

Run:

```bash
python3 excavations/004-vectors-as-change/implementation.py
```

Then change the waypoint while keeping the start and finish fixed. The individual displacements change, but their sum remains the same. Net displacement ignores the path.

## Common Misconceptions

**“Points and displacements are identical.”** They may use the same array representation, but their interpretation and valid operations differ.

**“A larger vector means a better representation.”** Magnitude only has meaning relative to the representation and task.

**“Vector analogies prove concepts are perfectly encoded.”** A direction can reveal a pattern without capturing every nuance of the concept.

## The New Problem

Adding one chosen change is useful. We now want a reusable machine that can mix every input dimension into several coordinated output dimensions. That machine is a matrix.

---

Previous: [003 — Distance](../003-distance/README.md) · Next: [005 — Matrices](../005-matrices/README.md)
