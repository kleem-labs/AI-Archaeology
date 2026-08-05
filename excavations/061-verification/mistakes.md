# Mistakes — 061

## First idea

Trust the absence of an error message or the model’s own description of its work.

## Counterexample

The changed code compiles but breaks another case. Confidence is not evidence of the requested outcome.

## Repair

Define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state.
