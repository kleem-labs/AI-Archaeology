# Excavation 004 — Vectors as Change

[Previous: Distance](../003-distance/README.md)

You are standing in the jungle. Someone tells you, “Walk five meters.” You cannot obey.

Five tells you how much, but movement also needs a direction. “Five meters north” is complete. It does not describe where you are; it describes what must change.

## Location and instruction are different

Yesterday you began at the river. Today you begin at the camp. The instruction “five meters north” remains the same, although the destination changes.

That is the second life of a vector: not a state, but a reusable description of change.

```text
state + change = new state
```

Suppose a traveler starts at `[2, 3]` and ends at `[7, 1]`. We can discover the change coordinate by coordinate: `+5` in the first direction and `-2` in the second. The change vector is `[5, -2]`.

Only now is an equation useful:

## Why Every Term Must Exist Before the Equation

- **a** is the starting state and **b** the observed destination.
- Subtraction is forced because we need the change that remains after removing the start.
- **Δ** names that reusable change, including its signs and directions.
- Adding Δ back to a must recover b; this second equation checks the meaning of the first.

Only now can we compress that reasoning:

$$
\Delta=\mathbf{b}-\mathbf{a}=[7-2,1-3]=[5,-2]
$$

Add it back and the meaning becomes visible:

$$
\mathbf{a}+\Delta=\mathbf{b}
$$


## Why changes add

Walk three steps east, then two north. Could one instruction replace both? Yes: the diagonal change that produces the same destination.

Vector addition was not chosen because brackets look convenient. Independent changes accumulate. Two pushes on a box, two deposits into an account, and two corrections to a model all demand one equivalent net change.

You supplied three memorable cancellation examples:

- sending and receiving the same amount;
- eating and burning 100 calories;
- throwing a ball up and catching it at the starting height.

Opposite changes cancel because the final state contains no net displacement along that feature.

## Why distance was not enough

Distance says how much separation exists but discards direction. Many destinations are five units from the same start. A change vector preserves both magnitude and direction.

This distinction matters in learning. A model's current parameters are a state. Training must say which weights to increase, which to decrease, and by how much. That instruction is a vector of change.

## Challenge

Explain why `[5, 0]` can represent the same change from many starting points but cannot represent one absolute destination without more information.

## What the next excavation needs

One fixed change is useful. We now want a machine that receives any vector and produces an appropriate new vector consistently.

[Next: Matrices](../005-matrices/README.md)
