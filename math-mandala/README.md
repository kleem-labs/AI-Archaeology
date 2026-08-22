# The Living Mathematical Mandala

This is not a poster placed on top of the mathematics. It is a memory of how
the mathematics grew.

[![The AI Archaeology Mathematical Mandala](math-mandala.svg)](math-mandala.svg)

Open the image and click a node:

- the **heart** opens the [Mathematical Gist](../MATHEMATICAL_GIST.md), where the equations remain in discovery order;
- a **mathematical job** opens the map of [Mathematical Moves](../MATHEMATICAL_MOVES.md#map-of-the-moves);
- a **move** such as subtraction, summation, or logarithm opens its reusable mental model;
- a **numbered equation** opens the excavation in which the reader was forced to invent it.

## Read the rings from the heart outward

    observation
        ↓ creates a need
    mathematical job
        ↓ chooses a relationship-preserving move
    operation
        ↓ compresses the discovered reasoning
    equation

Equations that answer the same kind of human need stay in the same part of the
mandala, even when they were discovered many chapters apart. The faint gold
thread preserves the chronological path from one equation to the next.

- **Where does this equation belong?** Follow its color and spoke inward.
- **What did we discover next?** Follow the gold thread.

The current mandala contains **110 equations from
98 excavations**, connected through
**45 reusable mathematical moves**.

## It grows with the book

The mandala has no hand-maintained equation list. Its builder reads every
displayed equation and every Mathematical Moves link from the excavation
sources. When a future chapter earns a new equation, explain the required
operations in that chapter and link them to <code>MATHEMATICAL_MOVES.md</code>.
Then run <code>python tools/build_math_mandala.py</code>. The new equation will
enter the right conceptual neighborhood, and the next outer ring will appear
when it is needed.
