# Excavation 029 — Initialization — Where Should Learning Begin?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Learning from uncertainty and error

Momentum remembers persistent direction and damps contradictory wobble. Before any of these learning rules can act, though, every weight needs a starting value that allows different neurons to learn different things without exploding or falling silent.

A new case arrives at the Lantern Observatory, but the keeper of uncertain stories first reaches for the familiar ring of glass lanterns. Its promise is simple: set every weight to zero.

At the edge of the ring of glass lanterns, the shortcut produces its consequence: neurons receive identical evidence and remain identical. Use arbitrarily huge random values. Signals explode or gates saturate. That consequence, not a textbook, earns the next move.

*The keeper of uncertain stories sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   set every weight to zero   neurons receive identical evidence…
            \        /
             \      /
              draw small random weights whose scale…
```

The keeper of uncertain stories covers the new mark and the old contradiction returns: neurons receive identical evidence and remain identical. Use arbitrarily huge random values. Signals explode or gates saturate. The cover is lifted, restoring the ability to draw small random weights whose scale depends on how many inputs feed the neuron, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason initialization exists.

What must change for initialization is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: draw small random weights whose scale depends on how many inputs feed the neuron. That threshold is where **Initialization** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In initialization, that memory takes a precise form: whenever neurons receive identical evidence and remain identical. Use arbitrarily huge random values. Signals explode or gates saturate, preserve enough structure to draw small random weights whose scale depends on how many inputs feed the neuron.

## The calculation hidden inside initialization

The keeper of uncertain stories carries the initialization scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but good initialization creates workable conditions; it does not encode the solution or guarantee stable training at every depth.

Imagine one hundred weak sensors feeding an alarm. If every sensor signal and every connecting weight is typically near 1, adding all one hundred contributions produces a signal near 100; deeper layers can make it explode further. Giving the starting weights a typical size near one tenth keeps the combined signal near the scale of one useful observation. The factor `1/√100` is therefore a scale-preserving choice, not a magic constant.

### Naming what is already on the table

**w** is one newly initialized weight.
**Var(w)** measures the typical squared spread of starting weights, not their meaning.
**n_in** counts signals entering the neuron.
Dividing by n_in compensates for adding more independent inputs, preventing their combined signal scale from growing with width.
“Approximately” leaves room for activation-specific constants such as Xavier or He scaling.

### Why the melody needs these exact notes

[Variance](../../MATHEMATICAL_MOVES.md#variance) describes the typical squared size of random starting weights without requiring every sampled weight to have that exact magnitude.
[Dividing by the number of incoming signals](../../MATHEMATICAL_MOVES.md#division) makes each individual weight smaller when more signals will be added, preventing total activation scale from growing with fan-in.
[The approximately sign](../../MATHEMATICAL_MOVES.md#approximation) admits a design target rather than claiming every finite random sample has exactly this variance; see [equality](../../MATHEMATICAL_MOVES.md#equals) for the stronger claim it avoids.

Trace each operation by touch rather than by name: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. Together they form the smallest mechanism that survives the counterexample.

The ring of glass lanterns already contains the complete initialization mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
\mathrm{Var}(w)\approx\frac{1}{n_{\text{in}}}
$$

## Initialization beyond this one case

A team needs different starting hypotheses, but none should begin shouting so loudly that every later observation is ignored.

## Return to the ring of glass lanterns

Rebuild the initialization scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Excavation 030](../030-activation-functions/README.md)
