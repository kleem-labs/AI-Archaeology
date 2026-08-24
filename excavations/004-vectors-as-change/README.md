# Excavation 004 — Vectors as Change

Distance has given the trackers one number for how far apart two places are. It throws away something they now urgently need: which way to walk from one place to the other.

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

## The calculation hidden inside vectors as change

A rescue party marks its camp on a paper map. It walks five kilometres east and two kilometres south to reach an injured ranger. Those instructions still work if a second party begins from another camp: move five east and two south. Only after the route has a meaning do we record east–west and north–south change as `[5, -2]`.

### Naming what is already on the table

- **a** is the starting state and **b** the observed destination.
- Subtraction is forced because we need the change that remains after removing the start.
- **Δ** names that reusable change, including its signs and directions.
- Adding Δ back to a must recover b; this second equation checks the meaning of the first.

### Why the melody needs these exact notes

[Destination minus starting point](../../MATHEMATICAL_MOVES.md#subtraction) is forced because we want the change that would carry **a** to **b**, not their combined location.
[A negative coordinate](../../MATHEMATICAL_MOVES.md#negative-sign) keeps direction: −2 means move two units opposite that axis, not that the movement has an impossible size.
[Adding the change back](../../MATHEMATICAL_MOVES.md#addition) is the check: starting place plus the discovered movement must recover the destination.

Inside vectors as change, familiar operations return with stricter duties: **the chisel**—what is shared is removed so the remaining change can be seen; **the turning wind**—an uphill quantity is made to point downhill, or surprise is made to count as cost; and **the joining river**—separate contributions meet without losing where they came from. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Cover the prose about vectors as change and each mark can still be recovered from the case. Only now is the compressed form safe to write:

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

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Foundations and representation
