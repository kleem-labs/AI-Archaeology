# Excavation 029 — Initialization — Where Should Learning Begin?

[Previous: Excavation 028](../028-momentum/README.md)

Before training, every weight needs a value. The starting point decides what signals and gradients the first examples can produce.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Set every weight to zero. Neurons receive identical evidence and remain identical. Use arbitrarily huge random values. Signals explode or gates saturate.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Set every weight to zero. Neurons receive identical evidence and remain identical. Use arbitrarily huge random values. Signals explode or gates saturate.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Draw small random weights whose scale depends on how many inputs feed the neuron.

Only after that reasoning may we give your discovery its inherited name.

## Why It Still Fails

The repair solves the immediate failure, but good initialization creates workable conditions; it does not encode the solution or guarantee stable training at every depth.

## Compress your discovery into mathematics


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
\operatorname{Var}(w)\approx\frac{1}{n_{\text{in}}}
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
