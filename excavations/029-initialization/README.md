# Excavation 029 — Initialization — Where Should Learning Begin?

Momentum remembers persistent direction and damps contradictory wobble. Before any of these learning rules can act, though, every weight needs a starting value that allows different neurons to learn different things without exploding or falling silent.

An obvious shortcut is to set every weight to zero. Neurons receive identical evidence and remain identical. Use arbitrarily huge random values. Signals explode or gates saturate.

That failure tells us to draw small random weights whose scale depends on how many inputs feed the neuron.

## From procedure to notation

The repair solves the immediate failure, but good initialization creates workable conditions; it does not encode the solution or guarantee stable training at every depth.

## The arithmetic we have earned

Imagine one hundred weak sensors feeding an alarm. If every sensor signal and every connecting weight is typically near 1, adding all one hundred contributions produces a signal near 100; deeper layers can make it explode further. Giving the starting weights a typical size near one tenth keeps the combined signal near the scale of one useful observation. The factor `1/√100` is therefore a scale-preserving choice, not a magic constant.

### Only now do the symbols earn names

- **w** is one newly initialized weight.
- **Var(w)** measures the typical squared spread of starting weights, not their meaning.
- **n_in** counts signals entering the neuron.
- Dividing by n_in compensates for adding more independent inputs, preventing their combined signal scale from growing with width.
- “Approximately” leaves room for activation-specific constants such as Xavier or He scaling.

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
