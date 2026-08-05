# Mistakes — 038

## Naive idea

Sort tokens by ID or trust their array slot without exposing it to the model. The first invents arbitrary order; the second stores position outside the computation.

## Failure

A fixed learned table cannot extend beyond trained positions, and absolute location is not always the relationship language needs.

## Discovery

Add a position-specific vector to each token vector before attention. Content says what; position says where.
