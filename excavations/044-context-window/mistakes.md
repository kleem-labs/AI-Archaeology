# Mistakes — 044

## Naive idea

Attend to the entire history forever. Computation and memory grow, and the model eventually exceeds positions it was trained to handle.

## Failure

A larger window is not perfect memory. Retrieval, compression, recurrence, and careful data are separate inventions.

## Discovery

Choose a maximum context, train within it, and reuse cached keys and values during generation instead of recomputing the unchanged past.
