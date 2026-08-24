# Mistakes Worth Preserving — Excavation 222

## The tempting idea

We tried to assign one fixed next-location distribution regardless of the current location.

## The evidence that refused it

the river makes village likely while deep forest makes river likely. Erasing the present state destroys exactly the information that changes the next step.

## What the wreckage taught us

The next construction had to choose a state description rich enough that, once the present state is known, earlier history adds no further information about the next-state distribution.

Keep this wrong idea. It is the negative space around Markov Chains: it records why the accepted method has exactly the responsibilities it does.
