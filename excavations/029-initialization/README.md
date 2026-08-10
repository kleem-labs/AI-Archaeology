# Excavation 029 — Initialization — Where Should Learning Begin?

[Previous: Excavation 028](../028-momentum/README.md)

Before training, every weight needs a value. The starting point decides what signals and gradients the first examples can produce.

Our first construction is deliberately modest: Set every weight to zero. Neurons receive identical evidence and remain identical. Use arbitrarily huge random values. Signals explode or gates saturate.

The cost of that attempt points to the missing operation: Draw small random weights whose scale depends on how many inputs feed the neuron.

## From procedure to notation

The repair solves the immediate failure, but good initialization creates workable conditions; it does not encode the solution or guarantee stable training at every depth.



## Build each piece from what just happened

If 100 independent inputs each arrive near unit scale, weights near unit scale make their sum huge. Scaling typical weight spread by 1/sqrt(100)=0.1 keeps their combined signal near a workable scale.

### Give Short Names Only After We Know the Pieces

- **w** is one newly initialized weight.
- **Var(w)** measures the typical squared spread of starting weights, not their meaning.
- **n_in** counts signals entering the neuron.
- Dividing by n_in compensates for adding more independent inputs, preventing their combined signal scale from growing with width.
- “Approximately” leaves room for activation-specific constants such as Xavier or He scaling.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
\mathrm{Var}(w)\approx\frac{1}{n_{\text{in}}}
$$

## Carry the idea back into the world

A team needs different starting hypotheses, but none should begin shouting so loudly that every later observation is ignored.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Test what you believe

Use the [invention challenges](exercises.md).

## What this discovery now makes possible

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 030](../030-activation-functions/README.md)
