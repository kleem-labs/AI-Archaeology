# Mistakes Worth Preserving — Excavation 211

## The tempting idea

We tried to differentiate only the first output and reuse that gradient as the sensitivity of the entire transformation.

## The evidence that refused it

the second output's response disappears. Downstream uncertainty, volume change, and chain-rule propagation become wrong because one row of evidence impersonates the whole map.

## What the wreckage taught us

The next construction had to give every output its own gradient row and arrange all output-input sensitivities into one matrix.

Keep this wrong idea. It is the negative space around Jacobians: it records why the accepted method has exactly the responsibilities it does.
