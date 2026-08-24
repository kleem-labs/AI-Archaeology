# Excavation 204 — Bases and Coordinates — The Same Object in Another Language

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Mathematical roots beneath the machine

### Realm 2 — The Chamber of Directions

The brass function opens a many-sided room. Rulers rotate in the walls, arrows cross the floor, and a high window turns every object into a shadow.

Listen for sliding rulers, turning stone, and distant bells. The questions in this realm travel as one chain:

```text
language of space → new directions → persistent directions → honest shadows → strongest channels
```

> **You are here:** Realm 2 of 5 — [The Chamber of Directions](../../MATHEMATICAL_ROOTS.md#realm-2)
>
> **Question waiting in this chamber:** When the coordinate numbers change, what stayed the same?
>
> **Do not take the answer yet:** first let the object fail.

Functions turn inputs into dependable outputs. Our vector functions seem to operate directly on lists of coordinates, yet rotating the ruler changes every coordinate while leaving the animal's physical displacement untouched.

Another vault door opens. The carving that once named **Bases and Coordinates** has weathered away, which is useful: we must recover the idea from what a ranger, builder, or machine can actually observe.

A ranger walks three steps east and two north. On the square floor this is recorded as `[3,2]`. Another ranger carries diagonal rulers: one points northeast, the other northwest. The same walk must acquire different numbers in that language.

The chamber has reduced the abstraction to one physical thing: **two rotating ruler frames laid over one footprint**. The question carved beside it asks: *When the coordinate numbers change, what stayed the same?*

The old machinery invites a plausible shortcut: treat the coordinate list as the vector itself and conclude that changing the list changes the underlying displacement.

The stone does not object with terminology; it objects with a result we already know cannot be right. The east-north list `[3,2]` and its diagonal-coordinate list disagree numerically even though both return the ranger to the same physical endpoint. Coordinates depend on the chosen measuring directions.

```text
scene → guess → calculate → compare with reality
          ▲                       │
          └──── change the idea ──┘
                       ↓
                     Bases and Coordinates
```

We do not leap to a famous formula. We carry one missing responsibility forward: choose a set of basis directions and define coordinates as the amounts of those directions whose combination reconstructs the vector.

This is the hinge of the Bases and Coordinates excavation. The repair is not justified by its reputation or by the fact that later mathematics adopted it. It earns its place because the named example has left us no cheaper honest way to keep the information that matters.

## When the chamber changes

Hold the failed picture still for one breath: The walk receives two different number pairs, and the record falsely declares that the ranger took two different journeys.

Now let the scene move. Keep the footprint fixed while rotating the rulers beneath it. Rebuild the same endpoint from new amounts of the new directions.

The transformation is the discovery of Bases and Coordinates made visible. Nothing has been defined by authority; this particular room changed because the old action could not preserve what mattered. Only after seeing that change do we press Bases and Coordinates into memory:

> **Memory seal — Bases and Coordinates**
>
> A basis is a chosen language for describing directions; the vector is the journey, not its coordinates.

Make the memory bodily, not merely verbal: Hold one finger still as a destination while rotating your other hand like a ruler frame.

## Bases and Coordinates on the stone workbench

With basis arrows east `[1,0]` and north `[0,1]`, the walk is `3 east + 2 north`. If the new basis uses northeast `[1,1]` and northwest `[-1,1]`, then `2.5 northeast - 0.5 northwest` reconstructs `[3,2]`. The coefficients changed; the endpoint did not.

The point of keeping the objects named while rebuilding Bases and Coordinates is that each movement can still be challenged. We can ask what the tiger, track, state, model, or measurement contributes; we can change one value and watch the consequence travel. The calculation remains an experience before it becomes notation.

## The calculation hidden inside bases and coordinates

Return to the named Bases and Coordinates scene above. The ranger, model, measurement, or state in that scene remains the owner of every quantity. Every symbol below will be only a short name for an object or action we have already handled there. If one mark cannot be translated back into that scene, it has arrived too early.

### Naming what is already on the table

**v** is the displacement being described. **b₁,…,bₙ** are the chosen basis directions. **c₁,…,cₙ** are coordinates in that basis. Multiplying a basis direction by its coordinate stretches or reverses it; adding the contributions reconstructs v.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) scales each basis direction by the amount required. [Addition](../../MATHEMATICAL_MOVES.md#addition) joins independent directional contributions. Concatenating the numbers would merely store them side by side and would not reconstruct the displacement.

The operations inside Bases and Coordinates form a sequence of jobs rather than a decorative string. Remove one and a stated need becomes unanswered; replace one with its tempting neighbour and the earlier counterexample returns. Only now has the long human reasoning become familiar enough to compress:

$$
\mathbf v=c_1\mathbf b_1+c_2\mathbf b_2+\cdots+c_n\mathbf b_n
$$

Read the Bases and Coordinates line back into its scene once. The equation is not where the discovery happened. It is the smallest faithful record of the discovery we have already reconstructed.

## A real-world echo

The same melody can be written for piano or violin. The marks change because the instrument's basis changes; the melody's relationships survive.

That echo helps Bases and Coordinates remain relational in memory. When the same job appears inside a dataset, a Transformer, a laboratory measurement, or an ordinary decision, the operation should feel like a familiar tool rather than an arbitrary sign.

## What this chamber was connected to

Embeddings choose learned coordinates, attention projects them into query and key bases, and RoPE rotates coordinate pairs. A representation is always a choice of mathematical language.

The older excavation and this Bases and Coordinates chamber are not merely cross-references. The earlier mechanism created the pressure; this chapter exposes the mathematical promise that pressure had been using. Following such links turns the book into a dependency map rather than a sequence of isolated definitions.

Before leaving The Chamber of Directions, look back at its path—**language of space → new directions → persistent directions → honest shadows → strongest channels**. Bases and Coordinates occupies one necessary step in that motion. Its object, **two rotating ruler frames laid over one footprint**, stays in the room so that the equation can later be recovered from an image rather than recalled as an orphaned line.

## Where the promise of bases and coordinates breaks

A collection of candidate basis directions may contain redundancy or fail to reach part of the space. We need to know which directions are genuinely new and what region their combinations can cover.

The boundary belongs beside the discovery of Bases and Coordinates because usefulness depends on assumptions. A formula remembered without its failure conditions becomes a spell; a formula remembered with them becomes an instrument.

## Rebuild the discovery in the laboratory

First preserve the wrong idea in [mistakes.md](mistakes.md). Then use the [chapter diagram](diagram.md) to retell the failure without notation. Finally build the same repair in [Pure Python, NumPy, and PyTorch](implementation/README.md), predicting the named intermediate values before running any file. The [invention exercises](exercises.md) ask you to alter the world until a new requirement becomes visible.

The [visual brief](images/README.md) keeps Bases and Coordinates tied to its concrete scene, while the [primary research trail](references.md) opens the historical and modern papers only after the concept has become yours.

[Continue to Excavation 205: Span and Linear Independence — Which Directions Are Truly New?](../205-span-linear-independence/README.md)
