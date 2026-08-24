# Mistakes Worth Preserving — Excavation 203

## The tempting idea

We tried to keep any relation between inputs and outputs, then choose one of the available outputs whenever the procedure runs.

## The evidence that refused it

the relation may omit an input entirely or attach several outputs to it. A reusable procedure cannot promise what it will do, and composition breaks because the next machine may receive nothing or an arbitrary value.

## What the wreckage taught us

The next construction had to require every allowed input to point to exactly one output, while permitting different inputs to share the same output.

Keep this wrong idea. It is the negative space around Functions: it records why the accepted method has exactly the responsibilities it does.
