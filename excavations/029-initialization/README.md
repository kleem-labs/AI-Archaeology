# Excavation 029 — Initialization — Where Should Learning Begin?

[Previous: Excavation 028](../028-momentum/README.md)


## Take the First Step Yourself

> **Your problem:** Before training, every weight needs a value. The starting point decides what signals and gradients the first examples can produce.

> **Try your first idea:** Set every weight to zero. Neurons receive identical evidence and remain identical. Use arbitrarily huge random values. Signals explode or gates saturate.

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

## Problem

Before training, every weight needs a value. The starting point decides what signals and gradients the first examples can produce.

## Your First Attempt

Set every weight to zero. Neurons receive identical evidence and remain identical. Use arbitrarily huge random values. Signals explode or gates saturate.

## Break Your First Attempt

Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Set every weight to zero. Neurons receive identical evidence and remain identical. Use arbitrarily huge random values. Signals explode or gates saturate.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

## Repair Your Attempt

Draw small random weights whose scale depends on how many inputs feed the neuron.

## Why It Still Fails

The repair solves the immediate failure, but good initialization creates workable conditions; it does not encode the solution or guarantee stable training at every depth.

## What You Have Just Invented

**Draw small random weights whose scale depends on how many inputs feed the neuron.**

## Only Now Give the Discovery a Mathematical Name

## Build Every Piece from the Concrete Example

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


## Real-World Analogy

A team needs different starting hypotheses, but none should begin shouting so loudly that every later observation is ignored.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Exercises

Use the [invention challenges](exercises.md).

## Connections

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 030](../030-activation-functions/README.md)
